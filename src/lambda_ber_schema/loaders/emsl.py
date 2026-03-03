"""
EMSL (Environmental Molecular Sciences Laboratory) loader.

API Documentation:
  - https://api.emsl.pnnl.gov/external/
  - https://api.emsl.pnnl.gov/external/swagger.json
"""

import json
import re
from typing import Any
from urllib.parse import quote

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

    def __init__(
        self,
        cache: ResponseCache | None = None,
        default_key_filter: str | None = "pncc",
        max_files: int = 200,
    ):
        self.cache = cache or ResponseCache(enabled=False)
        self.default_key_filter = default_key_filter
        self.max_files = max_files

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
                raise ValueError(f"Invalid transaction identifier: {identifier}")
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
            raise ValueError(f"No EMSL transactions found for sample query: {sample_name}")

        selected: dict[str, Any] | None = None
        if transaction_id is not None:
            tx_id = str(transaction_id)
            selected = next(
                (tx for tx in transactions if str(tx.get("transaction_id")) == tx_id),
                None,
            )
            if selected is None:
                raise ValueError(
                    f"Transaction {transaction_id} was not found in sample search results"
                )
        else:
            selected = transactions[0]
            if len(transactions) > 1:
                warnings.append(
                    f"Multiple transactions matched '{sample_name}'; "
                    f"using most recent transaction {selected.get('transaction_id')}"
                )

        result = self._build_dataset_from_transaction(selected, warnings)
        result.source_url = f"{self.base_url}/datasets/by_sample/{quote(sample_name)}"
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
        sample_value = path_parts[1] if len(path_parts) > 1 else f"transaction-{transaction_id}"

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
            try:
                return {"payload": response.json()}
            except ValueError as exc:
                raise ValueError(
                    "EMSL API returned non-JSON response for sample search"
                ) from exc

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
            return {"payload": response.json()}

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
            payload = response.json()
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
            return {"payload": response.json()}

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
        sample_value = str(transaction.get("sample_value") or f"transaction-{tx_id}")
        created = transaction.get("created")
        submitter_id = transaction.get("submitter_id")

        project: dict[str, Any] | None = None
        if project_id:
            try:
                project = self._fetch_project(project_id)
            except requests.HTTPError:
                warnings.append(f"Could not resolve project metadata for project_id={project_id}")

        resource: dict[str, Any] | None = None
        if instrument_id is not None:
            try:
                resource = self._fetch_resource(instrument_id)
            except requests.HTTPError:
                warnings.append(
                    f"Could not resolve instrument metadata for instrument_id={instrument_id}"
                )
            if resource is None:
                warnings.append(f"No public resource metadata for instrument_id={instrument_id}")

        files = transaction_files
        if files is None:
            files = self._fetch_transaction_files(tx_id)
        if not files:
            warnings.append(f"No file metadata returned for transaction {tx_id}")

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
            keywords=[k for k in ["EMSL", project.get("project_type") if project else None] if k],
        )

        sample = Sample(
            id=sample_id,
            sample_code=sample_value,
            sample_type=self._infer_sample_type(sample_value),
            title=sample_value,
            description=f"Source key: {sample_key}",
        )

        technique = self._infer_technique(sample_key, sample_value, resource, files)
        experiment = ExperimentRun(
            id=experiment_id,
            experiment_code=f"EMSL-TX-{tx_id}",
            experiment_date=created,
            operator_id=str(submitter_id) if submitter_id is not None else None,
            technique=technique,
            raw_data_location=(files[0].get("path") if files else None),
            processing_status=ProcessingStatusEnum.collected,
            acquisition_software=self._infer_acquisition_software(files),
        )

        instruments: list[Instrument] = []
        experiment_instrument_associations: list[ExperimentInstrumentAssociation] = []
        if resource:
            resource_id = resource.get("id", instrument_id)
            resource_name = str(resource.get("name") or f"Resource {resource_id}")
            instrument = Instrument(
                id=f"emsl:resource_{resource_id}",
                instrument_code=f"EMSL-{self._slugify(resource_name)}-{resource_id}",
                title=str(resource.get("display_name") or resource_name),
                description=self._build_resource_description(resource),
                facility_name=FacilityEnum.Environmental_Molecular_Sciences_Laboratory,
                facility_ror="https://ror.org/05h992307",
                instrument_category=self._infer_instrument_category(resource_name),
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
                StudyExperimentAssociation(study_id=study.id, experiment_id=experiment.id)
            ],
            experiment_sample_associations=[
                ExperimentSampleAssociation(
                    experiment_id=experiment.id,
                    sample_id=sample.id,
                )
            ],
            experiment_instrument_associations=experiment_instrument_associations,
        )

        doi = self._normalize_doi(project.get("award_doi") if project else None)
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
                warnings.append("Skipped file with missing name in transaction_info payload")
                continue

            file_format = self._infer_file_format(name)
            if file_format is None:
                warnings.append(f"Skipped file with unsupported format: {name}")
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
        text = " ".join([sample_key, sample_value, resource_name, file_text]).lower()

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
