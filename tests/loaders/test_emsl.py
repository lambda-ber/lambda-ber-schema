"""Tests for EMSL loader."""

import pytest

from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.loaders.emsl import EMSLLoader
from lambda_ber_schema.pydantic import (
    Dataset,
    FileFormatEnum,
    TechniqueEnum,
)


@pytest.fixture
def emsl_search_response() -> dict:
    """Representative sample-search payload from EMSL API."""
    return {
        "total_count": 2,
        "transactions": [
            {
                "transaction_id": 3736677,
                "sample_key": "pncc.short_sample_name",
                "sample_value": "T-A-apo_5_021226_data",
                "submitter_id": 48279,
                "instrument_id": 34290,
                "project_id": "160724",
                "created": "2026-02-15T15:46:44",
                "similarity_score": None,
            },
            {
                "transaction_id": 3736600,
                "sample_key": "pncc.short_sample_name",
                "sample_value": "T-A-apo_5_021226_atlas",
                "submitter_id": 48279,
                "instrument_id": 34290,
                "project_id": "160724",
                "created": "2026-02-15T08:51:33",
                "similarity_score": None,
            },
        ],
        "search_mode": "like",
        "limit": 20,
        "offset": 0,
    }


@pytest.fixture
def emsl_project() -> dict:
    """Representative project details payload."""
    return {
        "id": "160724",
        "title": "Single particle cryo-EM analysis of human PARP enzymes",
        "abstract": "Project abstract text",
        "project_type": "General Access",
        "award_doi": None,
        "active": True,
        "accepted": True,
    }


@pytest.fixture
def emsl_resource() -> dict:
    """Representative resource payload."""
    return {
        "id": 34290,
        "name": "PNCC Krios 1",
        "active": True,
        "location": "EMSL/1095",
        "display_name": "PNCC Krios 1 (34290)",
        "available_hours": "24/7",
    }


@pytest.fixture
def emsl_transaction_files() -> list[dict]:
    """Representative transaction file listing payload."""
    return [
        {
            "file_id": 64895567,
            "size": 146741698560,
            "name": "87ffc243efcf23cc97850c900d93d62a25087827.data.1.tar",
            "path": "160724/T-A-apo_5_021226_data/epu_session",
            "transaction_id": 3736677,
        },
        {
            "file_id": 64895568,
            "size": 155176284160,
            "name": "notes.txt",
            "path": "160724/T-A-apo_5_021226_data/epu_session",
            "transaction_id": 3736677,
        },
    ]


@pytest.fixture
def loader(mocker, emsl_search_response, emsl_project, emsl_resource, emsl_transaction_files):
    """Create loader with mocked HTTP-facing helper methods."""
    loader = EMSLLoader()
    mocker.patch.object(
        loader,
        "_search_transactions",
        return_value=emsl_search_response,
    )
    mocker.patch.object(loader, "_fetch_project", return_value=emsl_project)
    mocker.patch.object(loader, "_fetch_resource", return_value=emsl_resource)
    mocker.patch.object(
        loader,
        "_fetch_transaction_files",
        return_value=emsl_transaction_files,
    )
    return loader


class TestEMSLLoader:
    """Tests for EMSLLoader."""

    def test_load_returns_loader_result(self, loader):
        """load() should return a populated LoaderResult."""
        result = loader.load("apo")
        assert result is not None
        assert isinstance(result.dataset, Dataset)

    def test_load_by_sample_selects_most_recent_even_if_unsorted(self, mocker):
        """Default selection should sort by created timestamp before picking latest."""
        unsorted_search = {
            "transactions": [
                {
                    "transaction_id": 3736600,
                    "sample_key": "pncc.short_sample_name",
                    "sample_value": "older_tx",
                    "submitter_id": 1,
                    "instrument_id": 10,
                    "project_id": "160724",
                    "created": "2026-02-15T08:51:33",
                    "similarity_score": None,
                },
                {
                    "transaction_id": 3736677,
                    "sample_key": "pncc.short_sample_name",
                    "sample_value": "newer_tx",
                    "submitter_id": 1,
                    "instrument_id": 10,
                    "project_id": "160724",
                    "created": "2026-02-15T15:46:44",
                    "similarity_score": None,
                },
            ]
        }
        project = {"id": "160724", "title": "Project"}
        resource = {"id": 10, "name": "PNCC Krios 1", "active": True}
        files = [{"file_id": 1, "size": 100,
                  "name": "data.1.tar", "path": "160724/newer_tx"}]

        loader = EMSLLoader()
        mocker.patch.object(loader, "_search_transactions",
                            return_value=unsorted_search)
        mocker.patch.object(loader, "_fetch_project", return_value=project)
        mocker.patch.object(loader, "_fetch_resource", return_value=resource)
        mocker.patch.object(
            loader, "_fetch_transaction_files", return_value=files)

        result = loader.load("apo")
        assert result.dataset.id == "emsl:transaction_3736677"
        assert any(
            "using most recent transaction 3736677" in w for w in result.warnings)

    def test_sort_transactions_handles_mixed_naive_and_aware_timestamps(self):
        """Sorting should work when created timestamps mix naive and timezone-aware values."""
        loader = EMSLLoader()
        transactions = [
            {"transaction_id": 1, "created": "2026-02-15T15:46:44"},
            {"transaction_id": 2, "created": "2026-02-15T15:46:45Z"},
            {"transaction_id": 3, "created": "2026-02-15T15:46:46+00:00"},
        ]

        sorted_transactions = loader._sort_transactions(transactions)
        assert [tx["transaction_id"] for tx in sorted_transactions] == [3, 2, 1]

    def test_dataset_has_expected_id_and_title(self, loader):
        """Dataset should use transaction-based identifier and project-derived title."""
        result = loader.load("apo")
        assert result.dataset.id == "emsl:transaction_3736677"
        assert "PARP" in result.dataset.title

    def test_load_by_sample_source_url_matches_endpoint(self, loader):
        """Sample-load provenance should match the by_sample_name endpoint."""
        result = loader.load("apo")
        assert result.source_url == "https://api.emsl.pnnl.gov/external/datasets/by_sample_name"

    def test_experiment_has_cryo_em_technique(self, loader):
        """Technique should be inferred from PNCC/Krios context."""
        result = loader.load("apo")
        exp = result.dataset.experiment_runs[0]
        assert exp.technique == TechniqueEnum.cryo_em
        assert exp.experiment_code == "EMSL-TX-3736677"
        assert exp.operator_id == "48279"
        assert exp.acquisition_software == "EPU"

    def test_infer_technique_avoids_ms_substring_false_positive(self):
        """Plain words containing 'ms' should not trigger mass spectrometry."""
        loader = EMSLLoader()
        technique = loader._infer_technique(
            sample_key="example.key",
            sample_value="emsl_sample",
            resource=None,
            files=[],
        )
        assert technique == TechniqueEnum.cryo_em

    def test_infer_technique_detects_lc_ms(self):
        """Canonical LC-MS text should map to mass spectrometry."""
        loader = EMSLLoader()
        technique = loader._infer_technique(
            sample_key="example.key",
            sample_value="lc-ms profiling run",
            resource=None,
            files=[],
        )
        assert technique == TechniqueEnum.mass_spectrometry

    def test_instrument_and_associations_created(self, loader):
        """Instrument should be resolved and linked to experiment."""
        result = loader.load("apo")
        ds = result.dataset

        assert len(ds.instruments) == 1
        instrument = ds.instruments[0]
        assert "Krios" in (instrument.title or "")
        assert str(instrument.facility_name) == "EMSL"

        assert ds.experiment_instrument_associations is not None
        assert len(ds.experiment_instrument_associations) == 1

    def test_data_files_include_tar_and_ascii(self, loader):
        """Transaction files should map to supported file formats."""
        result = loader.load("apo")
        files = result.dataset.data_files
        assert len(files) == 2
        assert files[0].file_format == FileFormatEnum.tar
        assert files[1].file_format == FileFormatEnum.ascii

    def test_load_transaction_path_works(self, mocker, emsl_project, emsl_transaction_files):
        """tx:<id> should use transaction_info pathway."""
        loader = EMSLLoader()
        mocker.patch.object(
            loader,
            "_fetch_transaction_files",
            return_value=emsl_transaction_files,
        )
        mocker.patch.object(loader, "_fetch_project",
                            return_value=emsl_project)

        result = loader.load("tx:3736677")
        assert result.dataset.id == "emsl:transaction_3736677"
        assert result.source_url == (
            "https://api.emsl.pnnl.gov/external/datasets/transaction_info/3736677"
        )
        assert any(
            "Transaction loaded without sample-search context" in w for w in result.warnings)

    def test_load_bare_transaction_id_path_works(self, mocker, emsl_project, emsl_transaction_files):
        """Bare numeric identifier should route to transaction_info pathway."""
        loader = EMSLLoader()
        mocker.patch.object(
            loader,
            "_fetch_transaction_files",
            return_value=emsl_transaction_files,
        )
        mocker.patch.object(loader, "_fetch_project",
                            return_value=emsl_project)

        result = loader.load("3736677")
        assert result.dataset.id == "emsl:transaction_3736677"
        assert result.source_url == (
            "https://api.emsl.pnnl.gov/external/datasets/transaction_info/3736677"
        )
        assert any(
            "Transaction loaded without sample-search context" in w for w in result.warnings)

    def test_list_entries_by_sample(self, loader):
        """list_entries should return transaction IDs."""
        entries = loader.list_entries(sample_name="apo", limit=5)
        assert entries == ["3736677", "3736600"]

    def test_list_entries_requires_sample(self):
        """list_entries without sample should return empty list."""
        loader = EMSLLoader()
        assert loader.list_entries() == []

    def test_list_entries_uses_cache(self, mocker, tmp_path, emsl_search_response):
        """Sample search responses should be cached when enabled."""
        response = mocker.Mock()
        response.raise_for_status = mocker.Mock()
        response.json.return_value = emsl_search_response

        post_mock = mocker.patch(
            "lambda_ber_schema.loaders.emsl.requests.post",
            return_value=response,
        )

        cache = ResponseCache(cache_dir=tmp_path, enabled=True)
        loader = EMSLLoader(cache=cache)

        first = loader.list_entries(sample_name="apo", limit=2)
        second = loader.list_entries(sample_name="apo", limit=2)

        assert first == ["3736677", "3736600"]
        assert second == ["3736677", "3736600"]
        assert post_mock.call_count == 1
