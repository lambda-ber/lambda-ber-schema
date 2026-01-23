"""Tests for SASBDB loader."""

import pytest

from lambda_ber_schema.loaders.sasbdb import SASBDBLoader
from lambda_ber_schema.pydantic import (
    Dataset,
    ExperimentRun,
    Sample,
    SAXSInstrument,
    TechniqueEnum,
    WorkflowRun,
)


@pytest.fixture
def loader(mocker, sasbdb_sasda52_response):
    """Create loader with mocked HTTP client."""
    loader = SASBDBLoader()
    mocker.patch.object(
        loader, "_fetch_entry", return_value=sasbdb_sasda52_response
    )
    return loader


class TestSASBDBLoader:
    """Tests for SASBDBLoader."""

    def test_load_returns_loader_result(self, loader):
        """Test that load() returns a LoaderResult."""
        result = loader.load("SASDA52")
        assert result is not None
        assert result.dataset is not None
        assert isinstance(result.dataset, Dataset)

    def test_dataset_has_correct_id(self, loader):
        """Test dataset ID is prefixed."""
        result = loader.load("SASDA52")
        assert result.dataset.id == "sasbdb:SASDA52"

    def test_dataset_has_title(self, loader):
        """Test dataset title is extracted."""
        result = loader.load("SASDA52")
        assert result.dataset.title == "Standard proteins"

    def test_sample_has_required_fields(self, loader):
        """Test Sample has all required fields."""
        result = loader.load("SASDA52")
        assert len(result.dataset.samples) == 1
        sample = result.dataset.samples[0]
        assert sample.sample_code == "SASBDB-SASDA52"
        assert sample.sample_type == "protein"

    def test_sample_has_protein_info(self, loader):
        """Test Sample contains protein information."""
        result = loader.load("SASDA52")
        sample = result.dataset.samples[0]
        assert sample.protein_name == "Alcohol dehydrogenase 1"
        assert sample.organism == "Saccharomyces cerevisiae"

    def test_sample_has_quantity_values(self, loader):
        """Test Sample uses QuantityValue for numeric fields."""
        result = loader.load("SASDA52")
        sample = result.dataset.samples[0]

        assert sample.molecular_weight is not None
        assert sample.molecular_weight.numeric_value == 147.4
        assert sample.molecular_weight.unit == "kDa"

        assert sample.concentration is not None
        assert sample.concentration.numeric_value == 24.89

    def test_sample_has_buffer_composition(self, loader):
        """Test Sample has buffer composition."""
        result = loader.load("SASDA52")
        sample = result.dataset.samples[0]

        assert sample.buffer_composition is not None
        assert sample.buffer_composition.ph is not None
        assert sample.buffer_composition.ph.numeric_value == 7.4
        assert sample.buffer_composition.components == ["PBS"]

    def test_instrument_is_saxs_instrument(self, loader):
        """Test Instrument is SAXSInstrument."""
        result = loader.load("SASDA52")
        assert len(result.dataset.instruments) == 1
        instrument = result.dataset.instruments[0]
        assert isinstance(instrument, SAXSInstrument)
        assert instrument.instrument_code is not None

    def test_experiment_run_has_saxs_technique(self, loader):
        """Test ExperimentRun uses SAXS technique."""
        result = loader.load("SASDA52")
        assert len(result.dataset.experiment_runs) == 1
        exp = result.dataset.experiment_runs[0]
        assert exp.technique == TechniqueEnum.saxs

    def test_experiment_run_has_quality_metrics(self, loader):
        """Test ExperimentRun has quality metrics."""
        result = loader.load("SASDA52")
        exp = result.dataset.experiment_runs[0]

        assert exp.quality_metrics is not None
        assert exp.quality_metrics.rg is not None
        assert exp.quality_metrics.rg.numeric_value == 3.16
        assert exp.quality_metrics.i_zero is not None
        assert exp.quality_metrics.i_zero.numeric_value == 76.55

    def test_experiment_run_has_wavelength_and_distance(self, loader):
        """Test ExperimentRun has wavelength and detector distance."""
        result = loader.load("SASDA52")
        exp = result.dataset.experiment_runs[0]

        assert exp.wavelength is not None
        # SASBDB wavelength is 0.15 nm, converted to 1.5 Angstroms
        assert exp.wavelength.numeric_value == 1.5
        assert exp.wavelength.unit == "Angstroms"

        assert exp.detector_distance is not None
        assert exp.detector_distance.unit == "mm"

    def test_workflow_runs_created(self, loader):
        """Test WorkflowRuns are created for analysis."""
        result = loader.load("SASDA52")
        workflows = result.dataset.workflow_runs

        assert len(workflows) >= 1
        # Should have PDDF analysis
        pddf = next((w for w in workflows if "pddf" in w.id), None)
        assert pddf is not None
        assert pddf.software_name == "ATSAS GNOM"

    def test_data_files_created(self, loader):
        """Test DataFiles are created."""
        result = loader.load("SASDA52")
        files = result.dataset.data_files

        assert len(files) >= 1
        # Should have intensities file
        intensities = next((f for f in files if "intensities" in f.id), None)
        assert intensities is not None
        assert intensities.file_name == "SASDA52.dat"
        assert intensities.file_format == "ascii"

    def test_association_tables_created(self, loader):
        """Test association tables link entities."""
        result = loader.load("SASDA52")
        ds = result.dataset

        # Study-Sample association
        assert ds.study_sample_associations is not None
        assert len(ds.study_sample_associations) == 1

        # Study-Experiment association
        assert ds.study_experiment_associations is not None
        assert len(ds.study_experiment_associations) == 1

        # Experiment-Sample association
        assert ds.experiment_sample_associations is not None
        assert len(ds.experiment_sample_associations) == 1

        # Experiment-Instrument association
        assert ds.experiment_instrument_associations is not None
        assert len(ds.experiment_instrument_associations) == 1


@pytest.mark.integration
@pytest.mark.slow
class TestSASBDBLoaderIntegration:
    """Integration tests that hit the real SASBDB API."""

    def test_load_real_entry(self):
        """Test loading a real SASBDB entry."""
        loader = SASBDBLoader()
        result = loader.load("SASDA52")

        assert result.dataset is not None
        assert result.dataset.id == "sasbdb:SASDA52"
        assert len(result.warnings) == 0

    def test_list_entries(self):
        """Test listing entries from SASBDB."""
        loader = SASBDBLoader()
        entries = loader.list_entries(limit=5)

        assert len(entries) == 5
        # Each entry should be a string code
        assert all(isinstance(e, str) for e in entries)
