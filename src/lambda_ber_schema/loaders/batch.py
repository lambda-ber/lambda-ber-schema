"""
Batch loading utilities for large-scale ETL operations.

Provides robust batch loading with:
- Rate limiting
- Progress tracking
- Resume capability
- Error logging
- Concurrent processing
"""

import json
import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.loaders.cache import ResponseCache

logger = logging.getLogger(__name__)


class BatchProgress:
    """
    Tracks batch loading progress with persistence.

    Enables resuming interrupted batch jobs.
    """

    def __init__(self, progress_file: Path):
        self.progress_file = progress_file
        self.completed: set[str] = set()
        self.failed: dict[str, str] = {}  # entry_id -> error message
        self.started_at: str | None = None
        self._lock = threading.RLock()
        self.load()

    def load(self) -> None:
        """Load progress from file."""
        if self.progress_file.exists():
            data = json.loads(self.progress_file.read_text())
            with self._lock:
                self.completed = set(data.get("completed", []))
                self.failed = data.get("failed", {})
                self.started_at = data.get("started_at")

    def save(self) -> None:
        """Save progress to file."""
        with self._lock:
            completed = list(self.completed)
            failed = dict(self.failed)
            started_at = self.started_at

        data = {
            "completed": completed,
            "failed": failed,
            "started_at": started_at,
            "updated_at": datetime.now().isoformat(),
        }
        self.progress_file.write_text(json.dumps(data, indent=2))

    def mark_completed(self, entry_id: str) -> None:
        """Mark entry as completed."""
        with self._lock:
            self.completed.add(entry_id)
            # Remove from failed if it was there
            self.failed.pop(entry_id, None)

    def mark_failed(self, entry_id: str, error: str) -> None:
        """Mark entry as failed with error message."""
        with self._lock:
            self.failed[entry_id] = error

    def is_done(self, entry_id: str) -> bool:
        """Check if entry is already completed."""
        with self._lock:
            return entry_id in self.completed

    def completed_count(self) -> int:
        """Get number of completed entries."""
        with self._lock:
            return len(self.completed)

    def failed_entry_ids(self) -> list[str]:
        """Get failed entry IDs snapshot."""
        with self._lock:
            return list(self.failed.keys())


class BatchLoader:
    """
    Batch loader for large-scale ETL operations.

    Features:
    - Rate limiting to respect API limits
    - Resume from interrupted runs
    - Progress reporting
    - Error logging and retry
    - Optional concurrent loading

    Example:
        >>> from lambda_ber_schema.loaders import PDBLoader
        >>> loader = PDBLoader()
        >>> batch = BatchLoader(loader, output_dir=Path("pdb_dump"))
        >>> batch.load_all(format="yaml")
    """

    def __init__(
        self,
        loader: BaseLoader,
        output_dir: Path,
        cache_dir: Path | None = None,
        requests_per_second: float = 2.0,
        max_workers: int = 1,
    ):
        """
        Initialize batch loader.

        Args:
            loader: The source-specific loader to use
            output_dir: Directory to save loaded data
            cache_dir: Optional directory for API response caching
            requests_per_second: Rate limit (default 2 req/sec for RCSB)
            max_workers: Number of concurrent workers (1 = sequential)
        """
        self.loader = loader
        self.output_dir = output_dir
        self.cache_dir = cache_dir or output_dir / ".cache"

        if requests_per_second <= 0:
            raise ValueError("requests_per_second must be greater than 0")

        self.requests_per_second = requests_per_second
        self.max_workers = max_workers
        self.request_interval = 1.0 / requests_per_second

        # Setup directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Progress tracking
        self.progress = BatchProgress(self.output_dir / "progress.json")

        # Setup caching with extended TTL for batch operations (7 days)
        if hasattr(self.loader, "cache"):
            self.loader.cache = ResponseCache(
                cache_dir=self.cache_dir,
                enabled=True,
                ttl=timedelta(days=7),
            )

        # Error log
        self.error_log = self.output_dir / "errors.log"

    def _get_all_entries(self, limit: int | None = None, **filters: Any) -> list[str]:
        """
        Get all entry IDs from the source.

        Uses pagination to get all entries, not just first page.

        Args:
            limit: Optional maximum number of entries to fetch
            **filters: Source-specific filters
        """
        logger.info("Fetching entry IDs from %s...", self.loader.source_name)

        # For PDB, use the RCSB search API with pagination
        if self.loader.source_name == "pdb":
            return self._get_all_pdb_entries(limit=limit, **filters)

        # For other loaders, use their list_entries method
        if hasattr(self.loader, "list_entries"):
            entries = self.loader.list_entries(limit=limit, **filters)
            logger.info("Found %d entries", len(entries))
            return entries

        raise NotImplementedError(
            f"Loader {self.loader.source_name} does not support listing entries"
        )

    def _get_all_pdb_entries(
        self, limit: int | None = None, **filters: Any
    ) -> list[str]:
        """Get all PDB entry IDs using the RCSB search API."""
        import requests

        all_entries: list[str] = []
        batch_size = 10000  # RCSB allows up to 10000 per page
        start = 0

        while True:
            # Build search query (simplified version for all entries)
            search_request = {
                "query": {"type": "terminal", "service": "text"},
                "return_type": "entry",
                "request_options": {
                    "paginate": {"start": start, "rows": batch_size},
                    "sort": [
                        {"sort_by": "rcsb_accession_info.deposit_date",
                            "direction": "desc"}
                    ],
                },
            }

            # Apply filters if provided
            if filters.get("experimental_method"):
                method_map = {
                    "X-RAY": "X-RAY DIFFRACTION",
                    "XRAY": "X-RAY DIFFRACTION",
                    "EM": "ELECTRON MICROSCOPY",
                    "CRYO-EM": "ELECTRON MICROSCOPY",
                    "NMR": "SOLUTION NMR",
                }
                method = filters["experimental_method"].upper()
                method_value = method_map.get(method, method)
                search_request["query"] = {
                    "type": "terminal",
                    "service": "text",
                    "parameters": {
                        "attribute": "exptl.method",
                        "operator": "exact_match",
                        "value": method_value,
                    },
                }

            response = requests.post(
                "https://search.rcsb.org/rcsbsearch/v2/query",
                json=search_request,
                timeout=60,
            )
            response.raise_for_status()

            if response.status_code == 204 or not response.text:
                break

            result = response.json()
            entries = [hit["identifier"]
                       for hit in result.get("result_set", [])]
            all_entries.extend(entries)

            total_count = result.get("total_count", 0)
            logger.info("  Fetched %d/%d entries...",
                        len(all_entries), total_count)

            # Stop if we've hit the limit or reached the end
            if limit and len(all_entries) >= limit:
                all_entries = all_entries[:limit]
                break

            if len(entries) < batch_size or len(all_entries) >= total_count:
                break

            start += batch_size
            time.sleep(0.5)  # Be nice to the search API

        logger.info("Found %d entries", len(all_entries))
        return all_entries

    def _serialize(self, result: LoaderResult, format: str) -> str:
        """Serialize dataset to requested format."""
        data = result.dataset.model_dump(exclude_none=True, mode="json")

        if format == "json":
            return json.dumps(data, indent=2)
        else:  # yaml
            return yaml.dump(data, default_flow_style=False, sort_keys=False)

    def _load_single(self, entry_id: str, format: str) -> tuple[str, bool, str | None]:
        """
        Load a single entry.

        Returns:
            Tuple of (entry_id, success, error_message)
        """
        if self.progress.is_done(entry_id):
            return (entry_id, True, None)

        # Determine output path
        ext = "json" if format == "json" else "yaml"
        output_file = self.output_dir / f"{entry_id.lower()}.{ext}"

        # Skip if file exists (another form of resume)
        if output_file.exists():
            self.progress.mark_completed(entry_id)
            return (entry_id, True, None)

        try:
            result = self.loader.load(entry_id)
            output_str = self._serialize(result, format)
            output_file.write_text(output_str)

            # Log warnings
            if result.warnings:
                logger.warning("%s: %s", entry_id, "; ".join(result.warnings))

            return (entry_id, True, None)

        except Exception as e:
            error_msg = f"{type(e).__name__}: {e}"
            return (entry_id, False, error_msg)

    def load_all(
        self,
        format: str = "yaml",
        limit: int | None = None,
        **filters: Any,
    ) -> dict[str, Any]:
        """
        Load all entries from the source.

        Args:
            format: Output format ("yaml" or "json")
            limit: Optional limit on number of entries to load
            **filters: Source-specific filters (e.g., experimental_method="X-RAY")

        Returns:
            Summary dict with statistics
        """
        # Initialize progress
        if not self.progress.started_at:
            self.progress.started_at = datetime.now().isoformat()

        # Get entry IDs (with optional limit to avoid fetching all 200k+ when only needing a few)
        all_entries = self._get_all_entries(limit=limit, **filters)

        # Filter out already completed
        pending = [e for e in all_entries if not self.progress.is_done(e)]
        logger.info(
            "Loading %d entries (%d already completed)",
            len(pending),
            len(all_entries) - len(pending),
        )

        # Statistics
        success_count = self.progress.completed_count()
        fail_count = 0
        start_time = time.time()

        # Process entries
        if self.max_workers > 1:
            # Concurrent loading
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {
                    executor.submit(self._load_single, entry_id, format): entry_id
                    for entry_id in pending
                }

                for future in as_completed(futures):
                    entry_id, success, error = future.result()

                    if success:
                        self.progress.mark_completed(entry_id)
                        success_count += 1
                    else:
                        self.progress.mark_failed(
                            entry_id, error or "Unknown error")
                        fail_count += 1
                        with open(self.error_log, "a") as f:
                            f.write(
                                f"{datetime.now().isoformat()} {entry_id}: {error}\n")

                    # Progress report every 100 entries
                    total_done = success_count + fail_count
                    if total_done % 100 == 0:
                        elapsed = time.time() - start_time
                        rate = total_done / elapsed if elapsed > 0 else 0
                        remaining = len(all_entries) - total_done
                        eta = remaining / rate if rate > 0 else 0
                        logger.info(
                            "Progress: %d/%d (%.1f/sec, ETA: %.0f min)",
                            total_done,
                            len(all_entries),
                            rate,
                            eta / 60,
                        )
                        self.progress.save()

        else:
            # Sequential loading with rate limiting
            for i, entry_id in enumerate(pending):
                entry_id, success, error = self._load_single(entry_id, format)

                if success:
                    self.progress.mark_completed(entry_id)
                    success_count += 1
                else:
                    self.progress.mark_failed(
                        entry_id, error or "Unknown error")
                    fail_count += 1
                    with open(self.error_log, "a") as f:
                        f.write(
                            f"{datetime.now().isoformat()} {entry_id}: {error}\n")

                # Progress report every 100 entries
                total_done = success_count + fail_count - \
                    self.progress.completed_count() + len(pending)
                if (i + 1) % 100 == 0:
                    elapsed = time.time() - start_time
                    rate = (i + 1) / elapsed if elapsed > 0 else 0
                    remaining = len(pending) - (i + 1)
                    eta = remaining / rate if rate > 0 else 0
                    logger.info(
                        "Progress: %d/%d (%.1f/sec, ETA: %.0f min)",
                        i + 1,
                        len(pending),
                        rate,
                        eta / 60,
                    )
                    self.progress.save()

                # Rate limiting
                time.sleep(self.request_interval)

        # Final save
        self.progress.save()

        elapsed = time.time() - start_time
        summary = {
            "total_entries": len(all_entries),
            "successful": success_count,
            "failed": fail_count,
            "elapsed_seconds": elapsed,
            "entries_per_second": len(pending) / elapsed if elapsed > 0 else 0,
        }

        logger.info("Batch loading complete: %s", summary)
        return summary

    def retry_failed(self, format: str = "yaml") -> dict[str, Any]:
        """
        Retry previously failed entries.

        Returns:
            Summary dict with statistics
        """
        failed_entries = self.progress.failed_entry_ids()
        logger.info("Retrying %d failed entries", len(failed_entries))

        success_count = 0
        still_failed = 0

        for entry_id in failed_entries:
            entry_id, success, error = self._load_single(entry_id, format)

            if success:
                self.progress.mark_completed(entry_id)
                success_count += 1
            else:
                self.progress.mark_failed(entry_id, error or "Unknown error")
                still_failed += 1

            time.sleep(self.request_interval)

        self.progress.save()

        return {
            "retried": len(failed_entries),
            "now_successful": success_count,
            "still_failed": still_failed,
        }
