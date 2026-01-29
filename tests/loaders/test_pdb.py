"""Tests for PDB loader."""

import pytest

from lambda_ber_schema.loaders.pdb import PDBLoader
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.pydantic import (
    Dataset,
    TechniqueEnum,
    XRayInstrument,
)


@pytest.fixture
def loader(mocker, pdb_1hho_entry_response, pdb_1hho_polymer_entities):
    """Create loader with mocked HTTP client."""
    loader = PDBLoader()
    mocker.patch.object(loader, "_fetch_entry",
                        return_value=pdb_1hho_entry_response)
    mocker.patch.object(
        loader, "_fetch_polymer_entities", return_value=pdb_1hho_polymer_entities
    )
    return loader


class TestPDBLoader:
    """Tests for PDBLoader."""

    def test_load_returns_loader_result(self, loader):
        """Test that load() returns a LoaderResult."""
        result = loader.load("1HHO")
        assert result is not None
        assert result.dataset is not None
        assert isinstance(result.dataset, Dataset)

    def test_dataset_has_correct_id(self, loader):
        """Test dataset ID is prefixed and uppercase."""
        result = loader.load("1hho")
        assert result.dataset.id == "pdb:1HHO"

    def test_dataset_has_title(self, loader):
        """Test dataset title is extracted from struct."""
        result = loader.load("1HHO")
        assert "OXYHAEMOGLOBIN" in result.dataset.title

    def test_samples_created_from_polymer_entities(self, loader):
        """Test Sample objects are created from polymer entities."""
        result = loader.load("1HHO")
        assert len(result.dataset.samples) == 2  # Alpha and Beta chains

        # Check first sample (alpha chain)
        alpha = result.dataset.samples[0]
        assert alpha.sample_code == "PDB-1HHO-1"
        assert alpha.sample_type == "protein"
        assert "ALPHA" in alpha.protein_name

    def test_sample_has_organism(self, loader):
        """Test Sample has organism from source organism."""
        result = loader.load("1HHO")
        sample = result.dataset.samples[0]
        assert sample.organism == "Homo sapiens"

    def test_sample_has_molecular_weight(self, loader):
        """Test Sample has molecular weight from entity."""
        result = loader.load("1HHO")
        sample = result.dataset.samples[0]
        assert sample.molecular_weight is not None
        assert sample.molecular_weight.numeric_value > 10  # ~15 kDa
        assert sample.molecular_weight.unit == "kDa"

    def test_instrument_is_xray_instrument(self, loader):
        """Test Instrument is XRayInstrument."""
        result = loader.load("1HHO")
        assert len(result.dataset.instruments) == 1
        instrument = result.dataset.instruments[0]
        assert isinstance(instrument, XRayInstrument)

    def test_experiment_run_has_xray_technique(self, loader):
        """Test ExperimentRun uses X-ray crystallography technique."""
        result = loader.load("1HHO")
        assert len(result.dataset.experiment_runs) == 1
        exp = result.dataset.experiment_runs[0]
        assert exp.technique == TechniqueEnum.xray_crystallography

    def test_experiment_run_has_quality_metrics(self, loader):
        """Test ExperimentRun has quality metrics."""
        result = loader.load("1HHO")
        exp = result.dataset.experiment_runs[0]

        assert exp.quality_metrics is not None
        # Resolution
        assert exp.quality_metrics.resolution is not None
        assert exp.quality_metrics.resolution.numeric_value == 2.1
        assert exp.quality_metrics.resolution.unit == "Angstroms"

        # Space group
        assert exp.quality_metrics.space_group == "P 41 21 2"

    def test_experiment_run_has_unit_cell(self, loader):
        """Test ExperimentRun has unit cell parameters."""
        result = loader.load("1HHO")
        exp = result.dataset.experiment_runs[0]

        assert exp.quality_metrics.unit_cell_a is not None
        assert exp.quality_metrics.unit_cell_a.numeric_value == 53.7
        assert exp.quality_metrics.unit_cell_a.unit == "Angstroms"

    def test_experiment_run_has_r_work(self, loader):
        """Test ExperimentRun has R-work from refinement."""
        result = loader.load("1HHO")
        exp = result.dataset.experiment_runs[0]

        assert exp.quality_metrics.r_work is not None
        assert exp.quality_metrics.r_work.numeric_value == 0.223

    def test_experiment_run_has_date(self, loader):
        """Test ExperimentRun has deposition date."""
        result = loader.load("1HHO")
        exp = result.dataset.experiment_runs[0]
        assert exp.experiment_date == "1983-06-10"

    def test_workflow_runs_created(self, loader):
        """Test WorkflowRuns are created for refinement."""
        result = loader.load("1HHO")
        workflows = result.dataset.workflow_runs

        assert len(workflows) >= 1
        refine = workflows[0]
        assert refine.workflow_type == "refinement"

    def test_data_files_created(self, loader):
        """Test DataFiles are created for PDB files."""
        result = loader.load("1HHO")
        files = result.dataset.data_files

        assert len(files) >= 2
        # Should have PDB format
        pdb_file = next((f for f in files if f.file_format == "pdb"), None)
        assert pdb_file is not None
        assert pdb_file.file_name == "1hho.pdb"

        # Should have mmCIF format
        cif_file = next((f for f in files if f.file_format == "mmcif"), None)
        assert cif_file is not None

    def test_association_tables_created(self, loader):
        """Test association tables link entities."""
        result = loader.load("1HHO")
        ds = result.dataset

        # Study-Sample associations (2 samples)
        assert ds.study_sample_associations is not None
        assert len(ds.study_sample_associations) == 2

        # Study-Experiment association
        assert ds.study_experiment_associations is not None
        assert len(ds.study_experiment_associations) == 1

        # Experiment-Sample associations (2 samples)
        assert ds.experiment_sample_associations is not None
        assert len(ds.experiment_sample_associations) == 2

        # Experiment-Instrument association
        assert ds.experiment_instrument_associations is not None
        assert len(ds.experiment_instrument_associations) == 1

    def test_raw_data_contains_entry_and_entities(self, loader):
        """Test raw_data contains entry and polymer entity data."""
        result = loader.load("1HHO")
        assert result.raw_data is not None
        assert "entry" in result.raw_data
        assert "polymer_entities" in result.raw_data

    def test_list_entries_uses_cache(self, mocker, tmp_path):
        """Test list_entries caches responses when enabled."""
        response = mocker.Mock()
        response.status_code = 200
        response.text = '{"result_set":[{"identifier":"1ABC"},{"identifier":"2DEF"}]}'
        response.raise_for_status = mocker.Mock()
        post_mock = mocker.patch(
            "lambda_ber_schema.loaders.pdb.requests.post",
            return_value=response,
        )

        cache = ResponseCache(cache_dir=tmp_path, enabled=True)
        loader = PDBLoader(cache=cache)

        first = loader.list_entries(limit=2)
        second = loader.list_entries(limit=2)

        assert first == ["1ABC", "2DEF"]
        assert second == ["1ABC", "2DEF"]
        assert post_mock.call_count == 1


@pytest.mark.integration
@pytest.mark.slow
class TestPDBLoaderIntegration:
    """Integration tests that hit the real PDB API."""

    def test_load_real_entry(self):
        """Test loading a real PDB entry."""
        loader = PDBLoader()
        result = loader.load("1HHO")

        assert result.dataset is not None
        assert result.dataset.id == "pdb:1HHO"

    def test_load_cryo_em_entry(self):
        """Test loading a cryo-EM PDB entry."""
        loader = PDBLoader()
        # EMD-23908 / PDB 7MLZ - SARS-CoV-2 spike protein
        result = loader.load("7MLZ")

        assert result.dataset is not None
        exp = result.dataset.experiment_runs[0]
        assert exp.technique == TechniqueEnum.cryo_em

    def test_list_entries(self):
        """Test listing entries from PDB."""
        loader = PDBLoader()
        entries = loader.list_entries(limit=5)

        assert len(entries) == 5
        # Each entry should be a 4-character code
        assert all(len(e) == 4 for e in entries)

    def test_list_entries_by_method(self):
        """Test listing entries filtered by method."""
        loader = PDBLoader()
        entries = loader.list_entries(experimental_method="X-RAY", limit=5)

        assert len(entries) == 5
