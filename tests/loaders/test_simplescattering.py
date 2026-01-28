"""Tests for Simple Scattering loader."""

import pytest

from lambda_ber_schema.loaders.simplescattering import SimpleScatteringLoader
from lambda_ber_schema.pydantic import (
    Dataset,
    SAXSInstrument,
    TechniqueEnum,
)


@pytest.fixture
def loader(mocker, simplescattering_xsbhevph_html):
    """Create loader with mocked HTTP client."""
    loader = SimpleScatteringLoader()
    mocker.patch.object(
        loader, "_fetch_dataset_page", return_value=simplescattering_xsbhevph_html
    )
    return loader


class TestSimpleScatteringLoader:
    """Tests for SimpleScatteringLoader."""

    def test_load_returns_loader_result(self, loader):
        """Test that load() returns a LoaderResult."""
        result = loader.load("xsbhevph")
        assert result is not None
        assert result.dataset is not None
        assert isinstance(result.dataset, Dataset)

    def test_dataset_has_correct_id(self, loader):
        """Test dataset ID is prefixed."""
        result = loader.load("xsbhevph")
        assert result.dataset.id == "simplescattering:xsbhevph"

    def test_dataset_has_title(self, loader):
        """Test dataset title is extracted from HTML."""
        result = loader.load("xsbhevph")
        assert "GluRS" in result.dataset.title

    def test_sample_has_required_fields(self, loader):
        """Test Sample has all required fields."""
        result = loader.load("xsbhevph")
        assert len(result.dataset.samples) == 1
        sample = result.dataset.samples[0]
        assert sample.sample_code == "SS-XSBHEVPH"
        assert sample.sample_type == "protein"

    def test_sample_has_concentration(self, loader):
        """Test Sample has concentration extracted."""
        result = loader.load("xsbhevph")
        sample = result.dataset.samples[0]
        assert sample.concentration is not None
        assert sample.concentration.numeric_value == 3.5
        assert sample.concentration.unit == "mg/mL"

    def test_sample_has_buffer_composition(self, loader):
        """Test Sample has buffer composition."""
        result = loader.load("xsbhevph")
        sample = result.dataset.samples[0]
        assert sample.buffer_composition is not None
        # pH should be extracted
        assert sample.buffer_composition.ph is not None
        assert sample.buffer_composition.ph.numeric_value == 6.5

    def test_instrument_is_saxs_instrument(self, loader):
        """Test Instrument is SAXSInstrument for SIBYLS."""
        result = loader.load("xsbhevph")
        assert len(result.dataset.instruments) == 1
        instrument = result.dataset.instruments[0]
        assert isinstance(instrument, SAXSInstrument)
        assert instrument.title is not None
        assert "SIBYLS" in instrument.title
        assert instrument.instrument_code == "ALS-SIBYLS-BL12.3.1"

    def test_experiment_run_has_saxs_technique(self, loader):
        """Test ExperimentRun uses SAXS technique."""
        result = loader.load("xsbhevph")
        assert len(result.dataset.experiment_runs) == 1
        exp = result.dataset.experiment_runs[0]
        assert exp.technique == TechniqueEnum.saxs

    def test_experiment_run_has_wavelength(self, loader):
        """Test ExperimentRun has wavelength extracted."""
        result = loader.load("xsbhevph")
        exp = result.dataset.experiment_runs[0]
        assert exp.wavelength is not None
        assert exp.wavelength.unit == "Angstroms"

    def test_experiment_run_has_detector_distance(self, loader):
        """Test ExperimentRun has detector distance extracted."""
        result = loader.load("xsbhevph")
        exp = result.dataset.experiment_runs[0]
        assert exp.detector_distance is not None
        assert exp.detector_distance.unit == "mm"

    def test_data_files_created(self, loader):
        """Test DataFiles are created from download links."""
        result = loader.load("xsbhevph")
        files = result.dataset.data_files
        # Should have at least one file
        assert len(files) >= 1
        # Each file should have unique ID
        ids = [f.id for f in files]
        assert len(ids) == len(set(ids)), "File IDs should be unique"

    def test_data_files_have_filenames(self, loader):
        """Test DataFiles have proper filenames."""
        result = loader.load("xsbhevph")
        for f in result.dataset.data_files:
            assert f.file_name is not None
            assert len(f.file_name) > 0

    def test_association_tables_created(self, loader):
        """Test association tables link entities."""
        result = loader.load("xsbhevph")
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

    def test_raw_data_includes_html(self, loader):
        """Test raw_data contains original HTML."""
        result = loader.load("xsbhevph")
        assert result.raw_data is not None
        assert "html" in result.raw_data
        assert "metadata" in result.raw_data


@pytest.mark.integration
@pytest.mark.slow
class TestSimpleScatteringLoaderIntegration:
    """Integration tests that hit the real Simple Scattering website."""

    def test_load_real_dataset(self):
        """Test loading a real Simple Scattering dataset."""
        loader = SimpleScatteringLoader()
        result = loader.load("xsbhevph")

        assert result.dataset is not None
        assert result.dataset.id == "simplescattering:xsbhevph"

    def test_list_entries(self):
        """Test listing datasets from Simple Scattering."""
        loader = SimpleScatteringLoader()
        entries = loader.list_entries(limit=5)

        assert len(entries) == 5
        # Each entry should be a string code
        assert all(isinstance(e, str) for e in entries)
