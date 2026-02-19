"""Tests for batch loading utilities."""

import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor as StdThreadPoolExecutor

import pytest

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.loaders.batch import BatchLoader
from lambda_ber_schema.pydantic import Dataset


class DummyLoader(BaseLoader):
    """Test loader with controllable behavior."""

    source_name = "dummy"
    base_url = "https://example.org"

    def __init__(
        self,
        entries: list[str],
        failures: dict[str, Exception] | None = None,
        delay_seconds: float = 0.0,
    ):
        self._entries = entries
        self._failures = failures or {}
        self.delay_seconds = delay_seconds
        self.load_calls: list[str] = []
        self.thread_ids: set[int] = set()
        self.list_entries_calls: list[dict] = []

    def load(self, identifier: str) -> LoaderResult:
        self.load_calls.append(identifier)
        self.thread_ids.add(threading.get_ident())
        if self.delay_seconds:
            time.sleep(self.delay_seconds)

        if identifier in self._failures:
            raise self._failures[identifier]

        return LoaderResult(dataset=Dataset(id=f"dummy:{identifier}"))

    def list_entries(self, **filters) -> list[str]:
        self.list_entries_calls.append(filters)
        limit = filters.get("limit")
        if limit is None:
            return list(self._entries)
        return list(self._entries[:limit])


class FlakyLoader(BaseLoader):
    """Test loader that fails first attempt, succeeds on retry."""

    source_name = "dummy"
    base_url = "https://example.org"

    def __init__(self, entries: list[str], flaky_entry: str):
        self._entries = entries
        self.flaky_entry = flaky_entry
        self.attempts: dict[str, int] = {}

    def load(self, identifier: str) -> LoaderResult:
        attempt = self.attempts.get(identifier, 0) + 1
        self.attempts[identifier] = attempt
        if identifier == self.flaky_entry and attempt == 1:
            raise RuntimeError("temporary failure")
        return LoaderResult(dataset=Dataset(id=f"dummy:{identifier}"))

    def list_entries(self, **filters) -> list[str]:
        limit = filters.get("limit")
        if limit is None:
            return list(self._entries)
        return list(self._entries[:limit])


class TestBatchLoader:
    """Tests for BatchLoader."""

    def test_load_all_writes_outputs_and_summary(self, tmp_path):
        """load_all should process entries and write output files."""
        loader = DummyLoader(entries=["A1", "B2"])
        batch = BatchLoader(
            loader=loader,
            output_dir=tmp_path,
            requests_per_second=1000.0,
            max_workers=1,
        )

        summary = batch.load_all(format="json")

        assert summary["total_entries"] == 2
        assert summary["successful"] == 2
        assert summary["failed"] == 0
        assert (tmp_path / "a1.json").exists()
        assert (tmp_path / "b2.json").exists()

        progress = json.loads((tmp_path / "progress.json").read_text())
        assert set(progress["completed"]) == {"A1", "B2"}

    def test_load_all_concurrent_path_processes_entries(self, tmp_path):
        """Concurrent path should process all entries and surface failures."""
        entries = [f"E{i}" for i in range(8)]
        loader = DummyLoader(
            entries=entries,
            failures={"E3": RuntimeError("boom")},
            delay_seconds=0.02,
        )
        batch = BatchLoader(
            loader=loader,
            output_dir=tmp_path,
            requests_per_second=1000.0,
            max_workers=4,
        )

        summary = batch.load_all(format="yaml")

        assert summary["total_entries"] == 8
        assert summary["successful"] == 7
        assert summary["failed"] == 1
        assert len(loader.thread_ids) >= 2
        assert batch.progress.failed_entry_ids() == ["E3"]
        assert (tmp_path / "errors.log").exists()
        assert "E3: RuntimeError: boom" in (
            tmp_path / "errors.log").read_text()

    def test_load_all_concurrent_limits_in_flight_futures(self, mocker, tmp_path):
        """Concurrent mode should keep in-flight futures bounded."""
        entries = [f"E{i}" for i in range(40)]
        loader = DummyLoader(entries=entries, delay_seconds=0.02)

        class TrackingExecutor(StdThreadPoolExecutor):
            instances: list["TrackingExecutor"] = []

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self._tracking_lock = threading.Lock()
                self.in_flight = 0
                self.max_in_flight = 0
                TrackingExecutor.instances.append(self)

            def submit(self, *args, **kwargs):
                future = super().submit(*args, **kwargs)
                with self._tracking_lock:
                    self.in_flight += 1
                    self.max_in_flight = max(
                        self.max_in_flight, self.in_flight)

                def _decrement(_future):
                    with self._tracking_lock:
                        self.in_flight -= 1

                future.add_done_callback(_decrement)
                return future

        mocker.patch(
            "lambda_ber_schema.loaders.batch.ThreadPoolExecutor", TrackingExecutor
        )

        batch = BatchLoader(
            loader=loader,
            output_dir=tmp_path,
            requests_per_second=1000.0,
            max_workers=2,
        )
        summary = batch.load_all(format="yaml")

        assert summary["total_entries"] == 40
        assert summary["successful"] == 40
        assert summary["failed"] == 0
        assert TrackingExecutor.instances
        assert TrackingExecutor.instances[0].max_in_flight <= 4

    def test_load_all_concurrent_rate_limits_submission(self, mocker, tmp_path):
        """Concurrent mode should apply request-interval throttling on submit."""
        sleep_calls: list[float] = []

        def fake_sleep(seconds: float) -> None:
            sleep_calls.append(seconds)

        mocker.patch("lambda_ber_schema.loaders.batch.time.sleep",
                     side_effect=fake_sleep)

        loader = DummyLoader(entries=["A1", "B2", "C3"])
        batch = BatchLoader(
            loader=loader,
            output_dir=tmp_path,
            requests_per_second=0.5,  # 2 seconds per request
            max_workers=2,
        )
        summary = batch.load_all(format="yaml")

        assert summary["total_entries"] == 3
        assert summary["successful"] == 3
        assert summary["failed"] == 0
        assert any(seconds > 0 for seconds in sleep_calls)

    def test_load_all_resume_skips_completed_from_progress(self, tmp_path):
        """Entries already in progress file should not be reloaded."""
        progress_file = tmp_path / "progress.json"
        progress_file.write_text(
            json.dumps(
                {
                    "completed": ["DONE"],
                    "failed": {},
                    "started_at": "2025-01-01T00:00:00",
                    "updated_at": "2025-01-01T00:00:00",
                }
            )
        )

        loader = DummyLoader(entries=["DONE", "TODO"])
        batch = BatchLoader(
            loader=loader,
            output_dir=tmp_path,
            requests_per_second=1000.0,
            max_workers=1,
        )

        summary = batch.load_all(format="yaml")

        assert loader.load_calls == ["TODO"]
        assert summary["total_entries"] == 2
        assert summary["successful"] == 2
        assert summary["failed"] == 0
        assert (tmp_path / "todo.yaml").exists()

    def test_load_all_marks_entry_complete_when_output_file_exists(self, tmp_path):
        """Existing output files should be treated as completed work."""
        (tmp_path / "exists.yaml").write_text("id: dummy:EXISTS\n")
        loader = DummyLoader(entries=["EXISTS", "NEW"])
        batch = BatchLoader(
            loader=loader,
            output_dir=tmp_path,
            requests_per_second=1000.0,
            max_workers=1,
        )

        summary = batch.load_all(format="yaml")

        assert loader.load_calls == ["NEW"]
        assert summary["successful"] == 2
        assert batch.progress.is_done("EXISTS")
        assert batch.progress.is_done("NEW")

    def test_retry_failed_retries_and_clears_failures(self, tmp_path):
        """retry_failed should retry failed entries and clear recovered failures."""
        loader = FlakyLoader(entries=["FLAKY"], flaky_entry="FLAKY")
        batch = BatchLoader(
            loader=loader,
            output_dir=tmp_path,
            requests_per_second=1000.0,
            max_workers=1,
        )

        initial_summary = batch.load_all(format="yaml")
        retry_summary = batch.retry_failed(format="yaml")

        assert initial_summary["failed"] == 1
        assert retry_summary == {
            "retried": 1,
            "now_successful": 1,
            "still_failed": 0,
        }
        assert batch.progress.failed_entry_ids() == []
        assert (tmp_path / "flaky.yaml").exists()

    def test_requests_per_second_validation(self, tmp_path):
        """requests_per_second must be positive."""
        loader = DummyLoader(entries=["A1"])

        with pytest.raises(ValueError, match="greater than 0"):
            BatchLoader(loader=loader, output_dir=tmp_path /
                        "zero", requests_per_second=0)

        with pytest.raises(ValueError, match="greater than 0"):
            BatchLoader(loader=loader, output_dir=tmp_path /
                        "negative", requests_per_second=-1)
