"""Tests for the SSRL MX loader."""

from pathlib import Path

import pytest

from lambda_ber_schema.loaders import SSRLMXLoader
from lambda_ber_schema.pydantic import (
    Dataset,
    ExperimentRun,
    FacilityEnum,
    Sample,
    SampleTypeEnum,
    TechniqueEnum,
    WorkflowRun,
    WorkflowTypeEnum,
    XRayInstrument,
)


class TestSSRLMXLoader:
    """Tests for the SSRL MX loader."""

    def test_load_returns_loader_result(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that load returns a LoaderResult."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        assert result is not None
        assert isinstance(result.dataset, Dataset)
        assert result.source_url is not None

    def test_dataset_has_correct_id(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that the dataset ID is correctly formed."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        assert result.dataset.id.startswith("ssrl-mx:BL12-2/")
        assert "SA_x4_1_00001" in result.dataset.id

    def test_instrument_created(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that the instrument is created from detector info."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        assert len(result.dataset.instruments) == 1
        instrument = result.dataset.instruments[0]
        assert isinstance(instrument, XRayInstrument)
        assert instrument.instrument_code == "BL12-2"
        assert instrument.beamline_id == "BL12-2"
        assert instrument.detector_model == "EIGER16M"
        assert instrument.detector_manufacturer == "Dectris"
        assert instrument.facility_name == FacilityEnum.Stanford_Synchrotron_Radiation_Lightsource

    def test_sample_created(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that the sample is created from crystalStatus with metadata enrichment."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        assert len(result.dataset.samples) == 1
        sample = result.dataset.samples[0]
        assert isinstance(sample, Sample)
        assert sample.sample_code == "SA_x4"  # current_port
        assert sample.sample_type == SampleTypeEnum.protein
        # Enriched from sidecar metadata (run1.directory matches metadata key)
        assert sample.protein_name == "Ss_EXLX1"
        assert sample.organism == "NCBITaxon:909626"  # Streptomyces dysideae
        assert "Organism: Streptomyces dysideae" in sample.description
        assert "UniProt: A0A101UQ08" in sample.description
        assert "PDB: 9MS5" in sample.description

    def test_only_collecting_runs_included(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that only runs with status='collecting' are included."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        # Fixture has run1 with status="collecting", others are "inactive"
        assert len(result.dataset.experiment_runs) == 1
        run = result.dataset.experiment_runs[0]
        assert run.experiment_code == "DCSS-run1"

    def test_experiment_run_has_correct_fields(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that ExperimentRun has correct field values."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        run = result.dataset.experiment_runs[0]
        assert isinstance(run, ExperimentRun)
        assert run.technique == TechniqueEnum.xray_crystallography

        # Check wavelength conversion (energy 12658 eV -> ~0.9795 A)
        assert run.wavelength is not None
        assert 0.97 < run.wavelength.numeric_value < 0.99
        assert run.wavelength.unit == "Angstroms"

        # Check detector distance
        assert run.detector_distance is not None
        assert run.detector_distance.numeric_value == 200.0
        assert run.detector_distance.unit == "mm"

        # Check oscillation angle
        assert run.oscillation_angle is not None
        assert run.oscillation_angle.numeric_value == 0.2
        assert run.oscillation_angle.unit == "degrees"

        # Check start angle
        assert run.start_angle is not None
        assert run.start_angle.numeric_value == 40.0

        # Check number of images (end_frame - start_frame + 1 = 1350 - 1 + 1 = 1350)
        assert run.number_of_images is not None
        assert run.number_of_images.numeric_value == 1350

        # Check transmission
        assert run.transmission is not None
        assert run.transmission.numeric_value == 90.0

        # Check raw data location
        assert run.raw_data_location == "/data/csmith/Collect/PNNL/SA/xtal4"

        # Check resolution from sidecar metadata
        assert run.quality_metrics is not None
        assert run.quality_metrics.resolution is not None
        assert run.quality_metrics.resolution.numeric_value == 1.45
        assert run.quality_metrics.resolution.unit == "Angstroms"

    def test_energy_to_wavelength_conversion(self):
        """Test the energy to wavelength conversion."""
        loader = SSRLMXLoader()

        # At 12658 eV, wavelength should be ~0.9795 A
        wavelength = loader._energy_to_wavelength(12658.0)
        assert abs(wavelength - 0.9795) < 0.001

        # At 10000 eV, wavelength should be ~1.24 A
        wavelength = loader._energy_to_wavelength(10000.0)
        assert abs(wavelength - 1.2398) < 0.001

    def test_study_created(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that a Study is created using the UUID and title from sidecar metadata."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        assert len(result.dataset.studies) == 1
        study = result.dataset.studies[0]
        # Each snapshot has its own Study UUID; SA_x4 (9MS5) gets this one
        assert study.id == "ssrl-mx:study/5c2cdf5a-c0e9-41e9-80ba-b5ef87a080c2"
        assert study.title == "Crystal structure of an expansin (Ss_EXLX1) from Streptomyces sp."
        assert study.keywords == [
            "bacterial expansin",
            "carbohydrate-binding",
            "cellulose-loosening",
            "sugar binding protein",
        ]

    def test_study_falls_back_when_no_metadata(self, tmp_path: Path):
        """Test that Study id falls back to snapshot-derived form without metadata."""
        import json as _json
        snapshot = {
            "beamlineID": {"value": "BL12-2", "_type": "string"},
            "detectorType": {"value": "EIGER16M", "_type": "string"},
            "crystalStatus": {"current_port": "X", "sampleID": 1, "_type": "string"},
            "run0": {
                "status": "collecting", "directory": "/data/unknown", "energy1_eV": 12000,
                "distance_mm": 200, "delta": 0.1, "start_angle_deg": 0,
                "start_frame": 1, "end_frame": 10, "file_root": "X", "exposure_time_s": 0.1,
                "_type": "string",
            },
        }
        snapshot_path = tmp_path / "snap.json"
        snapshot_path.write_text(_json.dumps(snapshot))
        loader = SSRLMXLoader(metadata_file=tmp_path / "missing.json", processing_results_file=tmp_path / "missing.json")
        result = loader.load(str(snapshot_path))
        study = result.dataset.studies[0]
        assert study.id.endswith("/study")
        assert "BL12-2" in study.title

    def test_associations_created(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that association tables are created correctly."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        ds = result.dataset

        # Study-sample associations
        assert ds.study_sample_associations is not None
        assert len(ds.study_sample_associations) == 1

        # Study-experiment associations (one per collecting run)
        assert ds.study_experiment_associations is not None
        assert len(ds.study_experiment_associations) == 1

        # Experiment-sample associations
        assert ds.experiment_sample_associations is not None
        assert len(ds.experiment_sample_associations) == 1

        # Experiment-instrument associations
        assert ds.experiment_instrument_associations is not None
        assert len(ds.experiment_instrument_associations) == 1

    def test_raw_data_returned(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that raw data is included in result."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        assert result.raw_data is not None
        assert "detectorType" in result.raw_data
        assert "crystalStatus" in result.raw_data

    def test_file_not_found_raises(self):
        """Test that loading non-existent file raises FileNotFoundError."""
        loader = SSRLMXLoader()

        with pytest.raises(FileNotFoundError):
            loader.load("/nonexistent/path/snapshot.json")

    def test_list_entries_returns_empty_for_missing_dir(self):
        """Test that list_entries returns empty list for missing directory."""
        loader = SSRLMXLoader()
        entries = loader.list_entries(directory="/nonexistent/path")
        assert entries == []

    def test_beamline_id_from_snapshot(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that beamline ID is always extracted from the snapshot."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        # Snapshot's beamlineID field carries the canonical beamline name.
        assert "BL12-2" in result.dataset.id

    def test_load_raises_when_snapshot_lacks_beamlineID(self, tmp_path: Path):
        """Loader refuses to invent a beamline if the snapshot doesn't declare one."""
        import json as _json
        snap = tmp_path / "broken.json"
        snap.write_text(_json.dumps({
            "detectorType": {"value": "EIGER16M", "_type": "string"},
            "crystalStatus": {"current_port": "X", "_type": "string"},
        }))
        with pytest.raises(ValueError, match="beamlineID"):
            SSRLMXLoader().load(str(snap))

    def test_experimental_conditions_includes_exposure_time(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that experimental conditions include exposure time."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        run = result.dataset.experiment_runs[0]
        assert run.experimental_conditions is not None
        assert run.experimental_conditions.exposure_time is not None
        assert run.experimental_conditions.exposure_time.numeric_value == 0.2
        assert run.experimental_conditions.exposure_time.unit == "seconds"

    def test_workflow_run_created_from_processing_results(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that WorkflowRun is created when processing results exist."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        # Fixture run1.directory matches processing_results.json key
        assert result.dataset.workflow_runs is not None
        assert len(result.dataset.workflow_runs) == 1

        workflow = result.dataset.workflow_runs[0]
        assert isinstance(workflow, WorkflowRun)
        assert workflow.workflow_type == WorkflowTypeEnum.scaling
        assert workflow.software_name == "autoproc"
        assert workflow.software_version == "1.0.5"

    def test_workflow_run_has_space_group(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that WorkflowRun has space group from processing results."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        workflow = result.dataset.workflow_runs[0]
        assert workflow.space_group == "P 21 21 21"

    def test_workflow_run_has_unit_cell(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that WorkflowRun has unit cell parameters from processing results."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        workflow = result.dataset.workflow_runs[0]

        assert workflow.unit_cell_a is not None
        assert workflow.unit_cell_a.numeric_value == 45.91
        assert workflow.unit_cell_a.unit == "Angstroms"

        assert workflow.unit_cell_b is not None
        assert workflow.unit_cell_b.numeric_value == 60.79

        assert workflow.unit_cell_c is not None
        assert workflow.unit_cell_c.numeric_value == 65.14

        assert workflow.unit_cell_alpha is not None
        assert workflow.unit_cell_alpha.numeric_value == 90.0
        assert workflow.unit_cell_alpha.unit == "degrees"

    def test_workflow_run_has_resolution(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that WorkflowRun has resolution from processing results."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        workflow = result.dataset.workflow_runs[0]
        assert workflow.refinement_resolution_a is not None
        assert workflow.refinement_resolution_a.numeric_value == 1.45
        assert workflow.refinement_resolution_a.unit == "Angstroms"

    def test_workflow_run_has_indexer_scaler(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that WorkflowRun has indexer and scaler info."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        workflow = result.dataset.workflow_runs[0]
        assert workflow.indexer_module == "XDS"
        assert workflow.scaler_module == "AIMLESS"

    def test_workflow_run_has_processing_parameters(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that WorkflowRun has processing parameters summary."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        workflow = result.dataset.workflow_runs[0]
        assert workflow.processing_parameters is not None
        # Should contain summary statistics
        assert "Rmerge=" in workflow.processing_parameters
        assert "CC1/2=" in workflow.processing_parameters

    def test_data_file_emitted_from_output_files(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """The aimless.mtz declared in processing_results.json becomes a DataFile."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        assert result.dataset.data_files is not None
        assert len(result.dataset.data_files) == 1

        mtz = result.dataset.data_files[0]
        assert mtz.file_name == "aimless.mtz"
        assert mtz.file_format == "mtz"
        assert mtz.file_path == "/data/csmith/Collect/PNNL/SA/xtal4/autoproc/SA_x4_1/aimless.mtz"
        assert mtz.checksum == "82dbdc66990d4f384a4ee97214e6d1dbc2c65213e7d4b2f304b1ac9f21f69dd2"
        assert mtz.file_size_bytes.numeric_value == 6293260
        assert mtz.file_role == "final"
        assert mtz.data_type == "diffraction"
        # Canonical LIMS retrieval URL: a tar bundle of all output files for
        # this experiment. Points at /dev/lims for now (prod /lims is locked
        # to existing features pending an upgrade). The /bundle/ collection
        # holds archives; individual canonical files (when the LIMS adds them)
        # will live under /files/ with the same dataset name. The dataset name
        # is the DCSS file_root ("SA_x4") -- the sample-level identifier. The
        # experiment UUID disambiguates multiple runs of the same sample.
        assert mtz.storage_uri == (
            "https://smb.slac.stanford.edu/dev/lims/lambda/experiment/"
            "3a1d5d30-559b-4074-8433-e13db2920b48/bundle/SA_x4.tar"
        )

    def test_workflow_output_association_links_mtz_to_workflow(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Each DataFile is linked back to its WorkflowRun via an output association."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        assoc_list = result.dataset.workflow_output_associations
        assert assoc_list is not None
        assert len(assoc_list) == 1

        assoc = assoc_list[0]
        wf = result.dataset.workflow_runs[0]
        df = result.dataset.data_files[0]
        assert assoc.workflow_id == wf.id
        assert assoc.file_id == df.id
        assert assoc.output_type == "processed_data"

    def test_experiment_id_from_metadata_uuid(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that ExperimentRun.id uses the UUID from sidecar metadata when present."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        run = result.dataset.experiment_runs[0]
        # SA_x4 metadata has experiment_id "3a1d5d30-559b-4074-8433-e13db2920b48"
        assert run.id == "ssrl-mx:experiment/3a1d5d30-559b-4074-8433-e13db2920b48"

        # Associations should reference the UUID-based id
        assoc = result.dataset.experiment_sample_associations[0]
        assert assoc.experiment_id == run.id

    def test_workflow_associations_created(self, ssrl_mx_snapshot_path: Path, ssrl_mx_loader):
        """Test that workflow association tables are created."""
        result = ssrl_mx_loader.load(str(ssrl_mx_snapshot_path))

        ds = result.dataset

        # Study-workflow associations
        assert ds.study_workflow_associations is not None
        assert len(ds.study_workflow_associations) == 1
        assert ds.study_workflow_associations[0].study_id == ds.studies[0].id
        assert ds.study_workflow_associations[0].workflow_id == ds.workflow_runs[0].id

        # Workflow-experiment associations
        assert ds.workflow_experiment_associations is not None
        assert len(ds.workflow_experiment_associations) == 1
        assert ds.workflow_experiment_associations[0].workflow_id == ds.workflow_runs[0].id
        assert ds.workflow_experiment_associations[0].experiment_id == ds.experiment_runs[0].id


class TestSSRLMXLoaderNoCollectingRuns:
    """Test behavior when no runs are collecting."""

    def test_warning_when_no_collecting_runs(self, tmp_path: Path):
        """Test that a warning is issued when no runs are collecting."""
        # Create a snapshot with all inactive runs
        snapshot = {
            "beamlineID": {"value": "BL12-2", "_type": "string"},
            "detectorType": {"value": "EIGER16M", "_type": "string"},
            "crystalStatus": {
                "current_port": "SA_x1",
                "sampleID": 12345,
                "_type": "string",
            },
            "run0": {"status": "inactive", "_type": "string"},
            "run1": {"status": "inactive", "_type": "string"},
        }

        import json
        snapshot_path = tmp_path / "test_snapshot.json"
        snapshot_path.write_text(json.dumps(snapshot))

        loader = SSRLMXLoader()
        result = loader.load(str(snapshot_path))

        assert any("No actively collecting runs" in w for w in result.warnings)
        assert len(result.dataset.experiment_runs) == 0


class TestSSRLMXLoaderMultiRunMetadata:
    """Regression tests for snapshots with multiple collecting runs."""

    def test_metadata_uuid_only_applies_to_matching_run(self, tmp_path: Path):
        """A first-run metadata UUID must not overwrite later collecting runs."""
        import json

        snapshot = {
            "beamlineID": {"value": "BL12-2", "_type": "string"},
            "detectorType": {"value": "EIGER16M", "_type": "string"},
            "crystalStatus": {"current_port": "SA_x1", "sampleID": 12345, "_type": "string"},
            "run0": {
                "status": "collecting",
                "directory": "/data/run0",
                "energy1_eV": 12000,
                "distance_mm": 200,
                "delta": 0.1,
                "start_angle_deg": 0,
                "start_frame": 1,
                "end_frame": 10,
                "file_root": "SA_x1",
                "exposure_time_s": 0.1,
            },
            "run1": {
                "status": "collecting",
                "directory": "/data/run1",
                "energy1_eV": 12000,
                "distance_mm": 210,
                "delta": 0.2,
                "start_angle_deg": 10,
                "start_frame": 11,
                "end_frame": 20,
                "file_root": "SA_x2",
                "exposure_time_s": 0.2,
            },
        }
        metadata = {
            "/data/run0": {
                "experiment_id": "11111111-1111-1111-1111-111111111111",
                "resolution_angstrom": 1.5,
            }
        }

        snapshot_path = tmp_path / "test_snapshot.json"
        metadata_path = tmp_path / "sample_metadata.json"
        snapshot_path.write_text(json.dumps(snapshot))
        metadata_path.write_text(json.dumps(metadata))

        loader = SSRLMXLoader(metadata_file=metadata_path)
        result = loader.load(str(snapshot_path))

        experiment_ids = [experiment.id for experiment in result.dataset.experiment_runs]
        assert experiment_ids == [
            "ssrl-mx:experiment/11111111-1111-1111-1111-111111111111",
            "ssrl-mx:BL12-2/test_snapshot/run1",
        ]

    def test_workflow_only_links_to_processed_run(self, tmp_path: Path):
        """Processing from the first run must not be attached to every collecting run."""
        import json

        snapshot = {
            "beamlineID": {"value": "BL12-2", "_type": "string"},
            "detectorType": {"value": "EIGER16M", "_type": "string"},
            "crystalStatus": {"current_port": "SA_x1", "sampleID": 12345, "_type": "string"},
            "run0": {
                "status": "collecting",
                "directory": "/data/run0",
                "energy1_eV": 12000,
                "distance_mm": 200,
                "delta": 0.1,
                "start_angle_deg": 0,
                "start_frame": 1,
                "end_frame": 10,
                "file_root": "SA_x1",
                "exposure_time_s": 0.1,
            },
            "run1": {
                "status": "collecting",
                "directory": "/data/run1",
                "energy1_eV": 12000,
                "distance_mm": 210,
                "delta": 0.2,
                "start_angle_deg": 10,
                "start_frame": 11,
                "end_frame": 20,
                "file_root": "SA_x2",
                "exposure_time_s": 0.2,
            },
        }
        processing = {
            "/data/run0": {
                "pipeline": "autoproc",
                "output_files": [],
            }
        }

        snapshot_path = tmp_path / "test_snapshot.json"
        processing_path = tmp_path / "processing_results.json"
        snapshot_path.write_text(json.dumps(snapshot))
        processing_path.write_text(json.dumps(processing))

        loader = SSRLMXLoader(processing_results_file=processing_path)
        result = loader.load(str(snapshot_path))

        associations = result.dataset.workflow_experiment_associations
        assert associations is not None
        assert len(associations) == 1
        assert associations[0].experiment_id == "ssrl-mx:BL12-2/test_snapshot/run0"


class TestSSRLMXLoaderWithoutMetadata:
    """Test behavior when no sidecar metadata file exists."""

    def test_load_without_metadata_file(self, tmp_path: Path):
        """Test that loader works without a metadata file."""
        # Create a snapshot
        snapshot = {
            "beamlineID": {"value": "BL12-2", "_type": "string"},
            "detectorType": {"value": "EIGER16M", "_type": "string"},
            "crystalStatus": {
                "current_port": "TEST_x1",
                "protein": "TestProtein",
                "sampleID": 99999,
                "_type": "string",
            },
            "run0": {
                "status": "collecting",
                "directory": "/data/nonexistent/path",
                "energy1_eV": 12000,
                "distance_mm": 300,
                "delta": 0.1,
                "start_angle_deg": 0,
                "start_frame": 1,
                "end_frame": 100,
                "file_root": "test",
                "exposure_time_s": 0.1,
                "_type": "string",
            },
        }

        import json
        snapshot_path = tmp_path / "test_snapshot.json"
        snapshot_path.write_text(json.dumps(snapshot))

        # Use non-existent metadata and processing files
        loader = SSRLMXLoader(
            metadata_file=tmp_path / "nonexistent_metadata.json",
            processing_results_file=tmp_path / "nonexistent_processing.json",
        )
        result = loader.load(str(snapshot_path))

        # Should still work, using DCSS data directly
        sample = result.dataset.samples[0]
        assert sample.protein_name == "TestProtein"  # From crystalStatus
        assert sample.organism is None  # No metadata

        # No resolution without metadata
        run = result.dataset.experiment_runs[0]
        assert run.quality_metrics is None

        # No workflow runs without processing results
        assert result.dataset.workflow_runs is None
        assert result.dataset.study_workflow_associations is None
        assert result.dataset.workflow_experiment_associations is None
