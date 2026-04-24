"""
EMSL (Environmental Molecular Sciences Laboratory) loader.

API Documentation:
  - https://api.emsl.pnnl.gov/external/
  - https://api.emsl.pnnl.gov/external/swagger.json
"""

import io
import json
import os
import re
import tarfile
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Any, Generator

import requests

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.pydantic import (
    DataFile,
    DataTypeEnum,
    Dataset,
    ExperimentInstrumentAssociation,
    ExperimentRun,
    ExperimentSampleAssociation,
    FacilityEnum,
    FileFormatEnum,
    Instrument,
    InstrumentCategoryEnum,
    InstrumentStatusEnum,
    ProcessingStatusEnum,
    QuantityValue,
    Sample,
    SampleTypeEnum,
    Study,
    StudyExperimentAssociation,
    StudySampleAssociation,
    TechniqueEnum,
)


class EMSLLoader(BaseLoader):
    """
    Loader for public EMSL API data.

    Supports:
      - sample search via POST /datasets/by_sample_name
      - project enrichment via /projects/{id}
      - resource enrichment via /resources/{id}
      - transaction file listing via /datasets/transaction_info/{transaction_id}

    Identifier behavior for load():
      - "tx:<transaction_id>" loads a transaction directly
      - any other string is treated as sample query text
    """

    source_name = "emsl"
    base_url = "https://api.emsl.pnnl.gov/external"

    # Metadata file patterns to extract from EPU tar archives.
    # Ordered by preference: session-level XML first, then notes.
    _EPU_METADATA_PATTERNS = (
        re.compile(r"EpuSession\.dm$", re.IGNORECASE),
        re.compile(r".*[Ss]ession.*\.dm$"),
        re.compile(r".*[Ss]ession.*\.xml$"),
        re.compile(r"notes?\.txt$", re.IGNORECASE),
        re.compile(r".*[Ss]ession.*[Ss]ummary.*\.yaml$", re.IGNORECASE),
    )

    def __init__(
        self,
        cache: ResponseCache | None = None,
        default_key_filter: str | None = "pncc",
        max_files: int = 200,
        jwt_token: str | None = None,
        epu_timeout: float = 1800.0,
    ):
        self.cache = cache or ResponseCache(enabled=False)
        self.default_key_filter = default_key_filter
        self.max_files = max_files
        # JWT bearer token for authenticated endpoints (download cart, file download).
        # Falls back to the EMSL_JWT environment variable when not provided explicitly.
        self._jwt_token: str | None = jwt_token or os.environ.get("EMSL_JWT")
        self._epu_timeout: float = epu_timeout

    def load(self, identifier: str) -> LoaderResult:
        """
        Load a record from EMSL.

        Args:
            identifier: Either:
              - sample query (e.g., "apo")
              - transaction identifier prefixed with "tx:" (e.g., "tx:3736677")
              - bare transaction identifier (e.g., "3736677")
        """
        normalized = identifier.strip()
        if not normalized:
            raise ValueError("Identifier must not be empty")

        if normalized.startswith("tx:"):
            tx = normalized.removeprefix("tx:").strip()
            if not tx.isdigit():
                raise ValueError(
                    f"Invalid transaction identifier: {identifier}")
            return self.load_transaction(int(tx))

        if normalized.isdigit():
            return self.load_transaction(int(normalized))

        return self.load_by_sample(sample_name=normalized)

    def load_by_sample(
        self,
        sample_name: str,
        transaction_id: int | None = None,
        search_mode: str = "like",
        key_filter: str | None = None,
        exact_match: bool = False,
        similarity_threshold: float | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> LoaderResult:
        """
        Load a dataset by searching sample names.

        When multiple transactions match, the latest returned transaction is used
        unless transaction_id is provided.
        """
        warnings: list[str] = []
        search = self._search_transactions(
            sample_name=sample_name,
            search_mode=search_mode,
            key_filter=key_filter if key_filter is not None else self.default_key_filter,
            exact_match=exact_match,
            similarity_threshold=similarity_threshold,
            limit=limit,
            offset=offset,
        )

        transactions = search.get("transactions") or []
        if not transactions:
            raise ValueError(
                f"No EMSL transactions found for sample query: {sample_name}")

        # Enforce deterministic newest-first ordering independent of API order.
        sorted_transactions = self._sort_transactions(transactions)

        selected: dict[str, Any] | None = None
        if transaction_id is not None:
            tx_id = str(transaction_id)
            selected = next(
                (tx for tx in sorted_transactions if str(
                    tx.get("transaction_id")) == tx_id),
                None,
            )
            if selected is None:
                raise ValueError(
                    f"Transaction {transaction_id} was not found in sample search results"
                )
        else:
            selected = sorted_transactions[0]
            if len(sorted_transactions) > 1:
                warnings.append(
                    f"Multiple transactions matched '{sample_name}'; "
                    f"using most recent transaction {selected.get('transaction_id')}"
                )

        result = self._build_dataset_from_transaction(selected, warnings)
        result.source_url = f"{self.base_url}/datasets/by_sample_name"
        if result.raw_data is None:
            result.raw_data = {}
        result.raw_data["sample_search"] = search
        return result

    def load_transaction(self, transaction_id: int) -> LoaderResult:
        """
        Load a dataset directly from a transaction ID.

        This pathway is useful when a transaction ID is already known.
        """
        warnings: list[str] = []
        files = self._fetch_transaction_files(transaction_id)
        if not files:
            raise ValueError(
                f"No file metadata available for EMSL transaction {transaction_id}"
            )

        first_path = str(files[0].get("path") or "")
        path_parts = first_path.split("/") if first_path else []
        project_id = path_parts[0] if path_parts else None
        sample_value = path_parts[1] if len(
            path_parts) > 1 else f"transaction-{transaction_id}"

        synthetic_transaction: dict[str, Any] = {
            "transaction_id": transaction_id,
            "project_id": project_id,
            "sample_key": "derived.path.sample",
            "sample_value": sample_value,
            "created": None,
            "instrument_id": None,
            "submitter_id": None,
            "similarity_score": None,
        }

        warnings.append(
            "Transaction loaded without sample-search context; "
            "some metadata (e.g., instrument_id, submitter_id) may be missing."
        )
        result = self._build_dataset_from_transaction(
            synthetic_transaction, warnings, transaction_files=files
        )
        result.source_url = (
            f"{self.base_url}/datasets/transaction_info/{transaction_id}"
        )
        return result

    def list_entries(
        self,
        sample_name: str | None = None,
        limit: int | None = None,
        search_mode: str = "like",
        key_filter: str | None = None,
        **_: Any,
    ) -> list[str]:
        """
        List transaction IDs for a sample query.

        Args:
            sample_name: Sample query text (required for EMSL listing)
            limit: Max results to request/return
            search_mode: Search algorithm ("like", "regex", "fuzzy")
            key_filter: Optional key pattern filter (e.g., "pncc")
        """
        if not sample_name:
            return []

        result = self._search_transactions(
            sample_name=sample_name,
            search_mode=search_mode,
            key_filter=key_filter if key_filter is not None else self.default_key_filter,
            limit=limit or 20,
        )

        entries: list[str] = []
        seen: set[str] = set()
        for tx in result.get("transactions") or []:
            tx_id = tx.get("transaction_id")
            if tx_id is None:
                continue
            tx_text = str(tx_id)
            if tx_text in seen:
                continue
            seen.add(tx_text)
            entries.append(tx_text)

        return entries

    # ── EPU XML Parsing ───────────────────────────────────────────────────────

    @staticmethod
    def _text(root: ET.Element, *xpaths: str) -> str | None:
        """Return stripped text of the first matching XPath, or None."""
        for xpath in xpaths:
            el = root.find(xpath)
            if el is not None and el.text:
                return el.text.strip()
        return None

    @staticmethod
    def _float(root: ET.Element, *xpaths: str) -> float | None:
        """Return float value of the first matching XPath, or None."""
        for xpath in xpaths:
            el = root.find(xpath)
            if el is not None and el.text:
                try:
                    return float(el.text.strip())
                except ValueError:
                    pass
        return None

    def _parse_epu_session_xml(self, content: bytes) -> dict[str, Any]:
        """
        Parse an EPU session file (EpuSession.dm or Session*.xml) and return
        a dict of acquisition parameters keyed by ExperimentRun field names.

        EPU XML schema varies across versions; this parser tries multiple known
        XPaths per field and falls back gracefully. All returned values are raw
        Python types (float, str, int) — QuantityValue wrapping is done by
        the caller.

        Returns an empty dict if the file cannot be parsed as valid XML.
        """
        try:
            root = ET.fromstring(content)
        except ET.ParseError:
            return {}

        # Strip all namespace prefixes for XPath simplicity.
        for el in root.iter():
            if "}" in el.tag:
                el.tag = el.tag.split("}", 1)[1]

        result: dict[str, Any] = {}

        # Software version — several possible locations across EPU versions.
        version = self._text(
            root,
            ".//Version",
            ".//SoftwareVersion",
            ".//ApplicationVersion",
            ".//version",
        )
        if version:
            result["acquisition_software_version"] = version

        # Magnification
        mag = self._float(
            root,
            ".//Magnification",
            ".//NominalMagnification",
            ".//magnification",
            ".//Optics/Magnification",
        )
        if mag:
            result["magnification"] = {"numeric_value": mag, "unit": "x"}

        # Calibrated pixel size — EPU stores in meters, convert to Å.
        for xpath in (".//PixelSize", ".//pixelSize", ".//CalibratedPixelSize"):
            el = root.find(xpath)
            if el is not None and el.text:
                try:
                    px_m = float(el.text.strip())
                    # Values > 1e-6 are already in µm or Å (old EPU); < 1e-6 are meters.
                    if px_m < 1e-6:
                        px_angstrom = px_m * 1e10
                    elif px_m < 1e-3:
                        px_angstrom = px_m * 1e4  # µm → Å
                    else:
                        px_angstrom = px_m  # already Å-range
                    result["calibrated_pixel_size"] = {
                        "numeric_value": round(px_angstrom, 4),
                        "unit": "Å/pixel",
                    }
                    break
                except ValueError:
                    pass

        # Camera binning
        binning = self._float(
            root,
            ".//Binning",
            ".//CameraBinning",
            ".//binning",
            ".//CameraPreset/Binning",
        )
        if binning is not None:
            result["camera_binning"] = {"numeric_value": binning, "unit": ""}

        # Exposure time per frame — may be in seconds, convert to ms.
        for xpath in (
            ".//ExposureTime",
            ".//FrameExposureTime",
            ".//exposureTime",
            ".//CameraPreset/ExposureTime",
        ):
            el = root.find(xpath)
            if el is not None and el.text:
                try:
                    t = float(el.text.strip())
                    # Values < 10 are likely seconds; > 10 are likely ms.
                    t_ms = t * 1000 if t < 10 else t
                    result["exposure_time_per_frame"] = {
                        "numeric_value": round(t_ms, 3),
                        "unit": "ms",
                    }
                    break
                except ValueError:
                    pass

        # Frames per movie
        frames = self._float(
            root,
            ".//NumberOffractions",
            ".//FramesPerExposure",
            ".//FrameMultiplier",
            ".//framesPerExposure",
            ".//Acquisition/FramesPerShot",
            ".//CameraPreset/NumberOffractions",
        )
        if frames is not None:
            result["frames_per_movie"] = {"numeric_value": int(frames), "unit": ""}

        # Total dose (e-/Å²)
        dose = self._float(
            root,
            ".//TotalExposureDose",
            ".//TotalDose",
            ".//DosePerFrame",
            ".//totalDose",
        )
        if dose:
            # If dose looks like per-frame dose (< 5), multiply by frames to get total.
            if dose < 5 and "frames_per_movie" in result:
                dose_total = dose * result["frames_per_movie"]["numeric_value"]
                result["total_dose"] = {"numeric_value": round(dose_total, 2), "unit": "e-/Å²"}
                result["dose_per_frame"] = {"numeric_value": round(dose, 4), "unit": "e-/Å²/frame"}
            else:
                result["total_dose"] = {"numeric_value": round(dose, 2), "unit": "e-/Å²"}

        # Dose rate
        dose_rate = self._float(root, ".//DoseRate", ".//doseRate")
        if dose_rate:
            result["dose_rate"] = {"numeric_value": dose_rate, "unit": "e-/pixel/s"}

        # Defocus target / range
        defocus_target = self._float(
            root,
            ".//TargetDefocus",
            ".//DefocusTarget",
            ".//defocusTarget",
            ".//Presets/AutoFocus/Defocus",
        )
        if defocus_target is not None:
            # EPU stores in meters; convert to µm.
            if abs(defocus_target) < 0.1:
                defocus_target = defocus_target * 1e6
            result["defocus_target"] = {
                "numeric_value": round(defocus_target, 3),
                "unit": "µm",
            }

        defocus_min = self._float(root, ".//MinDefocus", ".//DefocusMin", ".//minDefocus")
        defocus_max = self._float(root, ".//MaxDefocus", ".//DefocusMax", ".//maxDefocus")
        if defocus_min is not None:
            if abs(defocus_min) < 0.1:
                defocus_min = defocus_min * 1e6
            result["defocus_range_min"] = {"numeric_value": round(defocus_min, 3), "unit": "µm"}
        if defocus_max is not None:
            if abs(defocus_max) < 0.1:
                defocus_max = defocus_max * 1e6
            result["defocus_range_max"] = {"numeric_value": round(defocus_max, 3), "unit": "µm"}

        # Shots per hole
        shots = self._float(
            root,
            ".//ShotsPerHole",
            ".//shotsPerHole",
            ".//NumberOfShotsPerHole",
            ".//Acquisition/ShotsPerHole",
        )
        if shots is not None:
            result["shots_per_hole"] = {"numeric_value": int(shots), "unit": ""}

        # Holes per group
        holes = self._float(
            root,
            ".//HolesPerGroup",
            ".//holesPerGroup",
            ".//NumberOfHoles",
        )
        if holes is not None:
            result["holes_per_group"] = {"numeric_value": int(holes), "unit": ""}

        # Stage tilt
        tilt = self._float(root, ".//StageTilt", ".//stageTilt", ".//TiltAngle")
        if tilt is not None:
            result["stage_tilt"] = {"numeric_value": round(tilt, 2), "unit": "degrees"}

        return result

    # ── Public Enhanced Load ──────────────────────────────────────────────────

    def extract_session_metadata(self, transaction_id: int | str) -> dict[str, Any] | None:
        """
        Fetch and parse EPU session metadata from a transaction's tar archive.

        Requires a JWT token (EMSL_JWT env var or jwt_token= constructor arg).
        Returns a dict of acquisition parameter fields keyed by ExperimentRun
        field names, or None when the token is absent or no metadata file is found.

        Emits a warning to stderr when JWT is not configured so callers can
        treat the absence gracefully.

        Example::

            loader = EMSLLoader()  # reads EMSL_JWT from environment
            params = loader.extract_session_metadata(3736677)
            if params:
                print(params["magnification"])
        """
        if not self._jwt_token:
            import sys
            print(
                "Warning: EMSL_JWT not set — skipping EPU session metadata extraction. "
                "Set the EMSL_JWT environment variable to enable.",
                file=sys.stderr,
            )
            return None

        tx_id = str(transaction_id)
        try:
            retrieval_url = self._get_retrieval_url(tx_id)
        except (requests.HTTPError, RuntimeError, TimeoutError) as exc:
            import sys
            print(f"Warning: could not create download cart for tx {tx_id}: {exc}", file=sys.stderr)
            return None

        found: dict[str, Any] = {}
        notes_content: str | None = None

        for name, content in self._stream_tar_members(retrieval_url):
            lower = name.lower()
            if lower.endswith((".dm", ".xml")):
                parsed = self._parse_epu_session_xml(content)
                if parsed:
                    found.update(parsed)
                    found["_source_file"] = name
                    break  # session XML found, stop streaming
            elif lower.endswith((".yaml", ".yml")):
                # Try YAML session summary — parse as key/value dict.
                try:
                    import yaml  # type: ignore[import]
                    data = yaml.safe_load(content.decode("utf-8", errors="replace"))
                    if isinstance(data, dict):
                        found.update({"_yaml_source": name, "_yaml_raw": data})
                except Exception:
                    pass
            elif "notes" in lower:
                notes_content = content.decode("utf-8", errors="replace").strip()

        if notes_content:
            found["_notes"] = notes_content

        return found if found else None

    def _sort_transactions(self, transactions: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Sort transactions by most recent creation time, then by transaction ID."""

        def parse_created(value: Any) -> datetime:
            if not value:
                return datetime.min.replace(tzinfo=timezone.utc)
            text = str(value).strip()
            if not text:
                return datetime.min.replace(tzinfo=timezone.utc)
            # EMSL timestamps may be naive ISO or UTC "Z"-suffixed.
            normalized = text.replace("Z", "+00:00")
            try:
                parsed = datetime.fromisoformat(normalized)
                if parsed.tzinfo is None:
                    return parsed.replace(tzinfo=timezone.utc)
                return parsed.astimezone(timezone.utc)
            except ValueError:
                return datetime.min.replace(tzinfo=timezone.utc)

        def parse_tx_id(value: Any) -> int:
            try:
                return int(str(value))
            except (TypeError, ValueError):
                return -1

        return sorted(
            transactions,
            key=lambda tx: (
                parse_created(tx.get("created")),
                parse_tx_id(tx.get("transaction_id")),
            ),
            reverse=True,
        )

    # ── Authentication ────────────────────────────────────────────────────────

    def _get_auth_headers(self) -> dict[str, str]:
        """Return Authorization header dict if a JWT token is available."""
        if self._jwt_token:
            return {"Authorization": f"Bearer {self._jwt_token}"}
        return {}

    # ── Download Cart ─────────────────────────────────────────────────────────

    def _create_download_cart(self, transaction_id: int | str) -> dict[str, Any]:
        """
        Create a download cart for a transaction.

        Calls GET /datasets/request/{transaction_id} with JWT auth and returns
        the Cart Info response containing download_uuid and retrieval_url.

        Raises:
            RuntimeError: If no JWT token is configured.
            requests.HTTPError: On non-2xx response.
        """
        if not self._jwt_token:
            raise RuntimeError(
                "Downloading data from EMSL requires a JWT bearer token. "
                "Set the EMSL_JWT environment variable or pass jwt_token= to EMSLLoader."
            )
        tx_id = str(transaction_id)
        response = requests.get(
            f"{self.base_url}/datasets/request/{tx_id}",
            headers=self._get_auth_headers(),
            timeout=30,
        )
        response.raise_for_status()
        return self._parse_json_response(response, "download cart creation")

    def _poll_download_cart(
        self,
        download_uuid: str,
        poll_interval: float = 5.0,
        timeout: float = 300.0,
    ) -> dict[str, Any]:
        """
        Poll GET /datasets/download/{download_uuid} until the cart is ready.

        Returns the final Cart Info dict (with retrieval_url populated).

        Raises:
            TimeoutError: If cart preparation exceeds timeout seconds.
            requests.HTTPError: On non-2xx response.
        """
        import sys
        deadline = time.monotonic() + timeout
        while True:
            response = requests.get(
                f"{self.base_url}/datasets/download/{download_uuid}",
                headers=self._get_auth_headers(),
                timeout=30,
            )
            response.raise_for_status()
            cart = self._parse_json_response(response, "download cart poll")
            status = str(cart.get("status") or "").lower()
            display = cart.get("display_status") or status
            print(f"  cart {download_uuid}: {display} (status={status!r})", file=sys.stderr)
            # Consider the cart ready when:
            #   - status matches a known "done" keyword, OR
            #   - success=True and retrieval_url is present (covers "File Retrieval" etc.)
            retrieval_url = cart.get("retrieval_url")
            if status in ("ready", "complete", "completed"):
                return cart
            if cart.get("success") is True and retrieval_url:
                return cart
            if status in ("error", "failed", "cancelled"):
                raise RuntimeError(
                    f"EMSL download cart {download_uuid} entered error state: {status}. "
                    f"message={cart.get('message')}"
                )
            if time.monotonic() > deadline:
                raise TimeoutError(
                    f"EMSL download cart {download_uuid} not ready after {timeout}s "
                    f"(last status: {status!r})"
                )
            time.sleep(poll_interval)

    def _resolve_url(self, url: str) -> str:
        """Resolve a potentially relative API URL to an absolute HTTPS URL."""
        if url.startswith("http://") or url.startswith("https://"):
            return url
        # Relative paths like /external/datasets/download/... — prepend the host.
        host = "https://api.emsl.pnnl.gov"
        return host + url if url.startswith("/") else f"{host}/{url}"

    def _extract_cart_uuid(self, cart: dict[str, Any]) -> str | None:
        """Extract the cart UUID from a cart response, handling field name variants."""
        return (
            cart.get("download_uuid")
            or cart.get("cart_uuid")
            or cart.get("uuid")
        )

    def _get_retrieval_url(self, transaction_id: int | str) -> str:
        """
        Create a download cart and wait for it to be ready, returning the retrieval URL.
        """
        cart = self._create_download_cart(transaction_id)
        cart_uuid = self._extract_cart_uuid(cart)
        retrieval_url: str | None = cart.get("retrieval_url")

        # If the cart already has a retrieval_url and appears ready, return immediately.
        status = str(cart.get("status") or "").lower()
        if retrieval_url and status in ("ready", "complete", "completed"):
            return self._resolve_url(retrieval_url)

        # Otherwise poll until ready.
        if not cart_uuid:
            raise RuntimeError(
                f"EMSL download cart response missing download_uuid/cart_uuid: {cart}"
            )
        ready_cart = self._poll_download_cart(cart_uuid, timeout=self._epu_timeout)
        retrieval_url = ready_cart.get("retrieval_url")
        if not retrieval_url:
            raise RuntimeError(
                f"EMSL download cart {cart_uuid} is ready but has no retrieval_url"
            )
        return self._resolve_url(retrieval_url)

    # ── Streaming Tar Extraction ──────────────────────────────────────────────

    def _stream_tar_members(
        self,
        url: str,
        chunk_size: int = 1024 * 1024,
    ) -> Generator[tuple[str, bytes], None, None]:
        """
        Stream a remote .tar file and yield (member_name, content) for each
        member whose name matches one of _EPU_METADATA_PATTERNS.

        Uses sequential tarfile streaming (mode='r|') so only the first
        matching members need to be downloaded — the stream is closed early
        once all pattern groups are satisfied.

        Args:
            url: HTTPS URL to stream the tar file from.
            chunk_size: Read chunk size in bytes.

        Yields:
            Tuples of (tar_member_name, raw_bytes).
        """
        with requests.get(
            url,
            headers=self._get_auth_headers(),
            stream=True,
            timeout=60,
        ) as response:
            response.raise_for_status()

            class _StreamingFileObj(io.RawIOBase):
                """Wrap a requests streaming response as a file-like object."""
                def __init__(self, resp: requests.Response) -> None:
                    self._iter = resp.iter_content(chunk_size=chunk_size)
                    self._buf = b""

                def readinto(self, b: bytearray) -> int:
                    while len(self._buf) < len(b):
                        try:
                            self._buf += next(self._iter)
                        except StopIteration:
                            break
                    n = min(len(b), len(self._buf))
                    b[:n] = self._buf[:n]
                    self._buf = self._buf[n:]
                    return n

                def readable(self) -> bool:
                    return True

            fileobj = io.BufferedReader(_StreamingFileObj(response))
            satisfied: set[int] = set()

            with tarfile.open(fileobj=fileobj, mode="r|*") as tf:
                for member in tf:
                    name = member.name
                    for idx, pattern in enumerate(self._EPU_METADATA_PATTERNS):
                        if idx in satisfied:
                            continue
                        if pattern.search(name):
                            fobj = tf.extractfile(member)
                            if fobj is not None:
                                yield name, fobj.read()
                                satisfied.add(idx)
                            break
                    # Stop streaming once we have found one match per pattern group.
                    if len(satisfied) >= len(self._EPU_METADATA_PATTERNS):
                        break

    def _parse_json_response(
        self,
        response: requests.Response,
        operation: str,
    ) -> Any:
        """Parse an EMSL JSON response and surface upstream HTML rejections clearly."""
        try:
            return response.json()
        except ValueError as exc:
            body = response.text or ""
            support_id = self._extract_rejection_support_id(body)
            if support_id is not None:
                raise ValueError(
                    f"EMSL {operation} was rejected by the upstream service "
                    f"(support ID: {support_id})"
                ) from exc

            content_type = response.headers.get("content-type") or "unknown"
            snippet = re.sub(r"\s+", " ", body).strip()[:200]
            detail = f" content-type={content_type}"
            if snippet:
                detail += f" body={snippet!r}"
            raise ValueError(
                f"EMSL {operation} returned a non-JSON response.{detail}"
            ) from exc

    @staticmethod
    def _extract_rejection_support_id(body: str) -> str | None:
        """Extract the support ID from EMSL's HTML rejection page."""
        match = re.search(r"support ID is:\s*([0-9]+)", body, flags=re.IGNORECASE)
        if match:
            return match.group(1)
        return None

    def _search_transactions(
        self,
        sample_name: str,
        search_mode: str = "like",
        key_filter: str | None = None,
        exact_match: bool = False,
        similarity_threshold: float | None = None,
        limit: int = 20,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Search transaction records by sample name."""
        payload: dict[str, Any] = {
            "sample_name": sample_name,
            "search_mode": search_mode,
            "exact_match": exact_match,
            "limit": limit,
            "offset": offset,
        }
        if key_filter:
            payload["key_filter"] = key_filter
        if similarity_threshold is not None:
            payload["similarity_threshold"] = similarity_threshold

        cache_key = f"emsl/by_sample_name/{json.dumps(payload, sort_keys=True)}"

        def fetch() -> dict[str, Any]:
            response = requests.post(
                f"{self.base_url}/datasets/by_sample_name",
                json=payload,
                timeout=30,
            )
            response.raise_for_status()
            return {
                "payload": self._parse_json_response(
                    response, "sample search"
                )
            }

        cached = self.cache.get_or_fetch(cache_key, fetch)
        return cached["payload"]

    def _fetch_project(self, project_id: str) -> dict[str, Any]:
        """Fetch project details."""
        cache_key = f"emsl/project/{project_id}"

        def fetch() -> dict[str, Any]:
            response = requests.get(
                f"{self.base_url}/projects/{project_id}",
                timeout=30,
            )
            response.raise_for_status()
            return {"payload": self._parse_json_response(response, "project lookup")}

        return self.cache.get_or_fetch(cache_key, fetch)["payload"]

    def _fetch_resource(self, resource_id: int | str) -> dict[str, Any] | None:
        """Fetch resource details."""
        cache_key = f"emsl/resource/{resource_id}"

        def fetch() -> dict[str, Any]:
            response = requests.get(
                f"{self.base_url}/resources/{resource_id}",
                timeout=30,
            )
            response.raise_for_status()
            payload = self._parse_json_response(response, "resource lookup")
            return {"payload": payload}

        payload = self.cache.get_or_fetch(cache_key, fetch)["payload"]
        if isinstance(payload, list):
            return payload[0] if payload else None
        if isinstance(payload, dict):
            return payload
        return None

    def _fetch_transaction_files(self, transaction_id: int | str) -> list[dict[str, Any]]:
        """Fetch file metadata for a transaction."""
        tx_id = str(transaction_id)
        cache_key = f"emsl/transaction_info/{tx_id}"

        def fetch() -> dict[str, Any]:
            response = requests.get(
                f"{self.base_url}/datasets/transaction_info/{tx_id}",
                timeout=60,
            )
            response.raise_for_status()
            return {
                "payload": self._parse_json_response(
                    response, "transaction file lookup"
                )
            }

        payload = self.cache.get_or_fetch(cache_key, fetch)["payload"]
        files = payload.get(tx_id)
        if isinstance(files, list):
            return files
        return []

    def _build_dataset_from_transaction(
        self,
        transaction: dict[str, Any],
        warnings: list[str],
        transaction_files: list[dict[str, Any]] | None = None,
    ) -> LoaderResult:
        """Create a Dataset from a single transaction record."""
        transaction_id = transaction.get("transaction_id")
        if transaction_id is None:
            raise ValueError("Transaction record missing transaction_id")
        tx_id = str(transaction_id)

        project_id = (
            str(transaction.get("project_id"))
            if transaction.get("project_id") is not None
            else None
        )
        instrument_id = transaction.get("instrument_id")
        sample_key = str(transaction.get("sample_key") or "sample_key")
        sample_value = str(transaction.get("sample_value")
                           or f"transaction-{tx_id}")
        created = transaction.get("created")
        submitter_id = transaction.get("submitter_id")

        project: dict[str, Any] | None = None
        if project_id:
            try:
                project = self._fetch_project(project_id)
            except requests.HTTPError:
                warnings.append(
                    f"Could not resolve project metadata for project_id={project_id}")

        resource: dict[str, Any] | None = None
        if instrument_id is not None:
            try:
                resource = self._fetch_resource(instrument_id)
            except requests.HTTPError:
                warnings.append(
                    f"Could not resolve instrument metadata for instrument_id={instrument_id}"
                )
            if resource is None:
                warnings.append(
                    f"No public resource metadata for instrument_id={instrument_id}")

        files = transaction_files
        if files is None:
            files = self._fetch_transaction_files(tx_id)
        if not files:
            warnings.append(
                f"No file metadata returned for transaction {tx_id}")

        project_title = (
            str(project.get("title"))
            if project and project.get("title")
            else f"EMSL Project {project_id}" if project_id else f"EMSL Transaction {tx_id}"
        )
        dataset_title = f"{project_title} - {sample_value}"

        study_id = f"emsl:project_{project_id}" if project_id else f"emsl:study_{tx_id}"
        sample_id = f"emsl:sample_{self._slugify(sample_value)}_{tx_id}"
        experiment_id = f"emsl:transaction_{tx_id}"

        study = Study(
            id=study_id,
            title=project_title,
            description=project.get("abstract") if project else None,
            keywords=[k for k in ["EMSL", project.get(
                "project_type") if project else None] if k],
        )

        sample = Sample(
            id=sample_id,
            sample_code=sample_value,
            sample_type=self._infer_sample_type(sample_value),
            title=sample_value,
            description=f"Source key: {sample_key}",
        )

        technique = self._infer_technique(
            sample_key, sample_value, resource, files)

        # Optional: enrich with EPU session metadata from tar archive (requires JWT).
        epu = self._build_epu_quantity_values(
            self.extract_session_metadata(tx_id)
            if self._jwt_token else None
        )

        experiment = ExperimentRun(
            id=experiment_id,
            experiment_code=f"EMSL-TX-{tx_id}",
            experiment_date=created,
            operator_id=str(
                submitter_id) if submitter_id is not None else None,
            technique=technique,
            raw_data_location=(files[0].get("path") if files else None),
            processing_status=ProcessingStatusEnum.collected,
            acquisition_software=self._infer_acquisition_software(files),
            acquisition_software_version=epu.get("acquisition_software_version"),
            magnification=epu.get("magnification"),
            calibrated_pixel_size=epu.get("calibrated_pixel_size"),
            camera_binning=epu.get("camera_binning"),
            exposure_time_per_frame=epu.get("exposure_time_per_frame"),
            frames_per_movie=epu.get("frames_per_movie"),
            total_dose=epu.get("total_dose"),
            dose_rate=epu.get("dose_rate"),
            defocus_target=epu.get("defocus_target"),
            defocus_range_min=epu.get("defocus_range_min"),
            defocus_range_max=epu.get("defocus_range_max"),
            shots_per_hole=epu.get("shots_per_hole"),
            holes_per_group=epu.get("holes_per_group"),
            stage_tilt=epu.get("stage_tilt"),
        )

        instruments: list[Instrument] = []
        experiment_instrument_associations: list[ExperimentInstrumentAssociation] = [
        ]
        if resource:
            resource_id = resource.get("id", instrument_id)
            resource_name = str(resource.get(
                "name") or f"Resource {resource_id}")
            instrument = Instrument(
                id=f"emsl:resource_{resource_id}",
                instrument_code=f"EMSL-{self._slugify(resource_name)}-{resource_id}",
                title=str(resource.get("display_name") or resource_name),
                description=self._build_resource_description(resource),
                facility_name=FacilityEnum.Environmental_Molecular_Sciences_Laboratory,
                facility_ror="https://ror.org/05h992307",
                instrument_category=self._infer_instrument_category(
                    resource_name),
                model=resource_name,
                current_status=(
                    InstrumentStatusEnum.operational
                    if resource.get("active") is True
                    else InstrumentStatusEnum.offline
                ),
            )
            instruments = [instrument]
            experiment_instrument_associations = [
                ExperimentInstrumentAssociation(
                    experiment_id=experiment_id,
                    instrument_id=instrument.id,
                )
            ]

        data_files = self._create_data_files(
            files=files,
            created=created,
            experiment_id=experiment_id,
            warnings=warnings,
        )

        dataset = Dataset(
            id=f"emsl:transaction_{tx_id}",
            title=dataset_title,
            description=f"EMSL transaction {tx_id} for sample '{sample_value}'",
            keywords=["EMSL", sample_key],
            studies=[study],
            instruments=instruments,
            samples=[sample],
            experiment_runs=[experiment],
            data_files=data_files,
            study_sample_associations=[
                StudySampleAssociation(study_id=study.id, sample_id=sample.id)
            ],
            study_experiment_associations=[
                StudyExperimentAssociation(
                    study_id=study.id, experiment_id=experiment.id)
            ],
            experiment_sample_associations=[
                ExperimentSampleAssociation(
                    experiment_id=experiment.id,
                    sample_id=sample.id,
                )
            ],
            experiment_instrument_associations=experiment_instrument_associations,
        )

        doi = self._normalize_doi(project.get(
            "award_doi") if project else None)
        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            doi=doi,
            raw_data={
                "transaction": transaction,
                "project": project,
                "resource": resource,
                "files": files,
            },
        )

    def _create_data_files(
        self,
        files: list[dict[str, Any]],
        created: str | None,
        experiment_id: str,
        warnings: list[str],
    ) -> list[DataFile]:
        """Create DataFile entities from transaction file metadata."""
        data_files: list[DataFile] = []
        for index, item in enumerate(files):
            if index >= self.max_files:
                warnings.append(
                    f"Truncated file list at {self.max_files} entries "
                    f"(transaction returned {len(files)} files)"
                )
                break

            name = item.get("name")
            if not name:
                warnings.append(
                    "Skipped file with missing name in transaction_info payload")
                continue

            file_format = self._infer_file_format(name)
            if file_format is None:
                warnings.append(
                    f"Skipped file with unsupported format: {name}")
                continue

            path = item.get("path")
            file_path = f"{path}/{name}" if path else name

            file_id = item.get("file_id", f"{experiment_id}_{index}")
            size = item.get("size")
            size_value = (
                QuantityValue(numeric_value=float(size), unit="bytes")
                if size is not None
                else None
            )

            data_files.append(
                DataFile(
                    id=f"emsl:file_{file_id}",
                    file_name=name,
                    file_path=file_path,
                    file_format=file_format,
                    file_size_bytes=size_value,
                    creation_date=created,
                    data_type=DataTypeEnum.raw_data,
                    related_entity=experiment_id,
                    file_role="raw",
                )
            )

        return data_files

    def _infer_file_format(self, file_name: str) -> FileFormatEnum | None:
        """Infer FileFormatEnum from file extension."""
        lower_name = file_name.lower()
        if lower_name.endswith(".tar.gz") or lower_name.endswith(".tgz"):
            return FileFormatEnum.gz

        ext = lower_name.rsplit(".", 1)[-1] if "." in lower_name else ""
        mapping = {
            "mrc": FileFormatEnum.mrc,
            "mrcs": FileFormatEnum.mrcs,
            "tif": FileFormatEnum.tiff,
            "tiff": FileFormatEnum.tiff,
            "h5": FileFormatEnum.h5,
            "hdf5": FileFormatEnum.hdf5,
            "star": FileFormatEnum.star,
            "pdb": FileFormatEnum.pdb,
            "cif": FileFormatEnum.mmcif,
            "mmcif": FileFormatEnum.mmcif,
            "mtz": FileFormatEnum.mtz,
            "cbf": FileFormatEnum.cbf,
            "img": FileFormatEnum.img,
            "dat": FileFormatEnum.ascii,
            "txt": FileFormatEnum.ascii,
            "csv": FileFormatEnum.csv,
            "json": FileFormatEnum.json,
            "zip": FileFormatEnum.zip,
            "gz": FileFormatEnum.gz,
            "tar": FileFormatEnum.tar,
        }
        return mapping.get(ext)

    def _infer_sample_type(self, sample_value: str) -> SampleTypeEnum:
        """Infer SampleTypeEnum from sample text."""
        text = sample_value.lower()
        if any(token in text for token in ("virus", "phage", "virion")):
            return SampleTypeEnum.virus
        if any(token in text for token in ("organelle", "mito", "chloroplast")):
            return SampleTypeEnum.organelle
        if any(token in text for token in ("complex", "holo", "assembly")):
            return SampleTypeEnum.complex
        return SampleTypeEnum.protein

    def _infer_technique(
        self,
        sample_key: str,
        sample_value: str,
        resource: dict[str, Any] | None,
        files: list[dict[str, Any]],
    ) -> TechniqueEnum:
        """Infer TechniqueEnum from transaction metadata."""
        resource_name = ""
        if resource:
            resource_name = " ".join(
                str(resource.get(key) or "") for key in ("name", "display_name")
            )

        file_text = " ".join(str(file.get("path") or "") for file in files)
        text = " ".join([sample_key, sample_value,
                        resource_name, file_text]).lower()

        mass_spec_patterns = (
            r"\borbitrap\b",
            r"\blumos\b",
            r"\bmass(?:\s|-)?spec(?:trometry)?\b",
            r"\blc[-\s]?ms\b",
            r"\bgc[-\s]?ms\b",
            r"\bms/?ms\b",
            r"\bms2\b",
            r"\bms\b",
        )
        if any(re.search(pattern, text) for pattern in mass_spec_patterns):
            return TechniqueEnum.mass_spectrometry
        if "sans" in text:
            return TechniqueEnum.sans
        if "saxs" in text:
            return TechniqueEnum.saxs
        if any(token in text for token in ("xanes", "exafs", "xas")):
            return TechniqueEnum.xas
        if any(token in text for token in ("krios", "arctica", "aquilos", "cryo", "pncc", "epu", "atlas")):
            return TechniqueEnum.cryo_em

        # Most publicly visible sample-search transactions at EMSL are cryo-EM.
        return TechniqueEnum.cryo_em

    def _infer_instrument_category(self, resource_name: str) -> InstrumentCategoryEnum:
        """Infer InstrumentCategoryEnum from resource name."""
        text = resource_name.lower()
        if any(token in text for token in ("krios", "arctica", "aquilos", "cryo", "tem")):
            return InstrumentCategoryEnum.ELECTRON_MICROSCOPE
        if any(token in text for token in ("orbitrap", "lumos", "mass spect", "lc-ms", "ftir", "raman")):
            return InstrumentCategoryEnum.SPECTROMETER
        return InstrumentCategoryEnum.ELECTRON_MICROSCOPE

    def _infer_acquisition_software(self, files: list[dict[str, Any]]) -> str | None:
        """Infer acquisition software from transaction file paths."""
        paths = " ".join(str(file.get("path") or "").lower() for file in files)
        if "epu" in paths:
            return "EPU"
        if "serialem" in paths:
            return "SerialEM"
        if "leginon" in paths:
            return "Leginon"
        return None

    def _build_resource_description(self, resource: dict[str, Any]) -> str | None:
        """Create compact description from resource metadata."""
        parts = [
            str(resource.get("location")) if resource.get("location") else None,
            str(resource.get("available_hours"))
            if resource.get("available_hours")
            else None,
        ]
        kept = [part for part in parts if part]
        return " | ".join(kept) if kept else None

    def _build_epu_quantity_values(
        self,
        epu: dict[str, Any] | None,
    ) -> dict[str, Any]:
        """
        Convert raw EPU metadata dict (from _parse_epu_session_xml) into a dict
        of QuantityValue objects and plain strings suitable for ExperimentRun fields.

        Fields with raw dict form {"numeric_value": ..., "unit": ...} are wrapped
        in QuantityValue. String fields (e.g., acquisition_software_version) are
        passed through as-is. Unknown/private keys (prefixed with _) are dropped.
        """
        if not epu:
            return {}
        result: dict[str, Any] = {}
        for key, val in epu.items():
            if key.startswith("_"):
                continue
            if isinstance(val, dict) and "numeric_value" in val:
                try:
                    result[key] = QuantityValue(
                        numeric_value=val["numeric_value"],
                        unit=val.get("unit") or "",
                    )
                except Exception:
                    pass
            elif isinstance(val, str):
                result[key] = val
        return result

    def _normalize_doi(self, value: Any) -> str | None:
        """Normalize award DOI values into a DOI URL."""
        if value is None:
            return None
        doi = str(value).strip()
        if not doi:
            return None
        if doi.startswith("http://") or doi.startswith("https://"):
            return doi
        doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
        return f"https://doi.org/{doi}"

    def _slugify(self, text: str) -> str:
        """Create a stable slug for CURIE-friendly local identifiers."""
        slug = re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")
        return slug or "unknown"
