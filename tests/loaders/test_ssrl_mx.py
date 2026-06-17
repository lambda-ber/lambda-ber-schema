"""Tests for the SSRL MX loader (crate-driven).

The loader consumes a published distribution package (LAMBDA RO-Crate) and maps its semantic graph into
the lambda-ber schema. The fixture at ``tests/loaders/fixtures/ssrl/package/`` is a **real** released
distribution's crate (the PDB 9MS4 Xa_EXLX1 expansin deposition), copied verbatim — a fully
profile-conformant v0.2 crate (inline @context, runParameters/instrumentName, approved termCodes).
"""

import pytest

from lambda_ber_schema.loaders import SSRLMXLoader
from lambda_ber_schema.loaders.base import LoaderResult


class TestSSRLMXLoaderCrate:
    def test_load_returns_loader_result(self, ssrl_mx_loader, ssrl_mx_package_path):
        result = ssrl_mx_loader.load(str(ssrl_mx_package_path))
        assert isinstance(result, LoaderResult)
        assert result.dataset is not None
        assert result.source_url.endswith("ro-crate-metadata.json")

    def test_load_accepts_dir_or_crate_file(self, ssrl_mx_loader, ssrl_mx_package_path):
        from_dir = ssrl_mx_loader.load(str(ssrl_mx_package_path)).dataset
        from_file = ssrl_mx_loader.load(str(ssrl_mx_package_path / "ro-crate-metadata.json")).dataset
        assert from_dir.id == from_file.id

    def test_dataset_id_from_study_uuid(self, ssrl_mx_dataset):
        assert ssrl_mx_dataset.id == "ssrl-mx:4d7d9700-94b2-44be-a540-494bbb6658a6"

    def test_study_mapped_from_root(self, ssrl_mx_dataset):
        study = ssrl_mx_dataset.studies[0]
        assert study.id == "ssrl-mx:study/4d7d9700-94b2-44be-a540-494bbb6658a6"
        assert study.title == "Xa_EXLX1 expansin (XA_x16, BL12-1)"
        assert "bacterial expansin" in study.keywords

    def test_instrument_from_beamline(self, ssrl_mx_dataset):
        inst = ssrl_mx_dataset.instruments[0]
        assert inst.beamline_id == "BL12-1"
        assert inst.instrument_code == "BL12-1"
        assert inst.facility_name is not None

    def test_sample_from_raw_unit(self, ssrl_mx_dataset):
        sample = ssrl_mx_dataset.samples[0]
        assert sample.sample_code == "90000002"
        assert sample.protein_name == "Xa_EXLX1"
        assert sample.organism == "NCBITaxon:56458"
        # description rolls up the study-level lambda fields
        assert "expansin" in (sample.description or "")
        assert "9MS4" in (sample.description or "")

    def test_experiment_from_run_definition(self, ssrl_mx_dataset):
        exp = ssrl_mx_dataset.experiment_runs[0]
        assert exp.id.startswith("ssrl-mx:experiment/")
        assert exp.technique is not None
        # acquisition params come from the crate's camelCase runParameters
        assert abs(exp.wavelength.numeric_value - 0.9795) < 0.001
        assert exp.detector_distance.numeric_value == 350
        assert exp.oscillation_angle.numeric_value == 0.2
        assert exp.number_of_images.numeric_value == 1800
        assert exp.transmission.numeric_value == 77.88
        assert exp.experimental_conditions.exposure_time.numeric_value == 0.2
        # widened run definition: energy + sweep extent (total_rotation derived from start/end angle)
        assert abs(exp.energy.numeric_value - 12658.4) < 0.1
        assert exp.sweep_start.numeric_value == 90
        assert exp.sweep_end.numeric_value == 450
        assert exp.total_rotation.numeric_value == 360

    def test_workflow_stats_from_crate(self, ssrl_mx_dataset):
        wf = ssrl_mx_dataset.workflow_runs[0]
        assert wf.id.startswith("ssrl-mx:workflow/")
        assert wf.space_group == "C 1 2 1"
        assert wf.unit_cell_a.numeric_value == 201.205
        assert wf.unit_cell_gamma.numeric_value == 90
        assert wf.refinement_resolution_a.numeric_value == 2.3
        assert wf.software_name  # mapped from the SoftwareApplication
        assert wf.software_version == "0.7.13"
        assert "CC1/2=0.995" in (wf.processing_parameters or "")

    def test_data_file_is_the_mtz_only(self, ssrl_mx_dataset):
        # Only genuine data products (the MTZ) become typed DataFiles; provenance/aux JSON/HTML do not.
        files = ssrl_mx_dataset.data_files or []
        assert len(files) == 1
        mtz = files[0]
        assert mtz.file_name == "XA_x16_autoproc.mtz"
        assert str(mtz.file_format) == "mtz"
        assert mtz.file_role == "final"
        assert mtz.checksum  # sha256 carried from the crate File entity

    def test_associations(self, ssrl_mx_dataset):
        d = ssrl_mx_dataset
        assert len(d.study_sample_associations) == 1
        assert len(d.study_experiment_associations) == 1
        assert len(d.experiment_sample_associations) == 1
        assert len(d.experiment_instrument_associations) == 1
        assert len(d.study_workflow_associations) == 1
        assert len(d.workflow_experiment_associations) == 1
        assert len(d.workflow_output_associations) == 1  # one DataFile output
        # the experiment-sample link resolves the RawUnit the workflow consumed
        assert d.experiment_sample_associations[0].sample_id == d.samples[0].id

    def test_no_warnings_for_complete_package(self, ssrl_mx_loader, ssrl_mx_package_path):
        assert ssrl_mx_loader.load(str(ssrl_mx_package_path)).warnings == []


class TestSSRLMXTermCompat:
    """The loader reads the official profile terms (runParameters / root instrumentName) and also falls
    back to the older lambda:runDefinition / per-product lambda:beamline so existing packages still load.
    """

    def _crate(self, run_key, inst_on_root):
        wf = {
            "@id": "urn:uuid:11111111-1111-4111-8111-111111111111",
            "@type": "CreateAction",
            "workflowRunId": "11111111-1111-4111-8111-111111111111",
            "name": "proc",
            "instrument": {"@id": "#sw"},
            "object": [{"@id": "#ru"}],
            "result": [{"@id": "#prod"}],
            "endTime": "2025-01-01T00:00:00Z",
            run_key: {"wavelengthAngstrom": 0.98, "detectorDistanceMm": 150},
        }
        prod = {"@id": "#prod", "@type": ["Dataset", "lambda:DerivedProduct"],
                "name": "p", "productId": "p", "description": "d", "hasPart": []}
        if not inst_on_root:
            prod["lambda:beamline"] = "BL9-2"
        root = {"@id": "./", "@type": ["Dataset", "lambda:Experiment"],
                "identifier": {"@type": "PropertyValue", "propertyID": "UUID",
                               "value": "22222222-2222-4222-8222-222222222222"},
                "name": "t"}
        if inst_on_root:
            root["instrumentName"] = "BL12-2"
        return {"@graph": [root, {"@id": "#sw", "@type": "SoftwareApplication", "name": "x"},
                                 {"@id": "#ru", "@type": ["Dataset", "lambda:RawUnit"],
                                  "name": "r", "rawUnitId": "r", "description": "d"}, prod, wf]}

    def _load(self, tmp_path, crate):
        import json
        (tmp_path / "ro-crate-metadata.json").write_text(json.dumps(crate))
        return SSRLMXLoader().load(str(tmp_path)).dataset

    def test_new_terms(self, tmp_path):
        d = self._load(tmp_path, self._crate("runParameters", inst_on_root=True))
        assert d.experiment_runs[0].wavelength.numeric_value == 0.98
        assert d.instruments[0].beamline_id == "BL12-2"

    def test_legacy_terms(self, tmp_path):
        d = self._load(tmp_path, self._crate("lambda:runDefinition", inst_on_root=False))
        assert d.experiment_runs[0].wavelength.numeric_value == 0.98
        assert d.instruments[0].beamline_id == "BL9-2"


class TestSSRLMXLoaderErrors:
    def test_missing_crate_raises(self, ssrl_mx_loader, tmp_path):
        with pytest.raises(FileNotFoundError):
            ssrl_mx_loader.load(str(tmp_path / "nope"))

    def test_crate_without_root_raises(self, ssrl_mx_loader, tmp_path):
        (tmp_path / "ro-crate-metadata.json").write_text('{"@graph": []}')
        with pytest.raises(ValueError):
            ssrl_mx_loader.load(str(tmp_path))


class TestSSRLMXListEntries:
    def test_list_single_package(self, ssrl_mx_loader, ssrl_mx_package_path):
        entries = ssrl_mx_loader.list_entries(ssrl_mx_package_path)
        assert entries == [str(ssrl_mx_package_path)]

    def test_list_packages_dir(self, ssrl_mx_loader, ssrl_mx_package_path):
        entries = ssrl_mx_loader.list_entries(ssrl_mx_package_path.parent)
        assert str(ssrl_mx_package_path) in entries

    def test_list_none_returns_empty(self, ssrl_mx_loader):
        assert ssrl_mx_loader.list_entries(None) == []
