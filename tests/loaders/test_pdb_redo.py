"""Tests for the PDB-REDO loader."""

import copy
import json

import pytest
import requests

from lambda_ber_schema.loaders.batch import BatchLoader
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.loaders.pdb import PDBLoader
from lambda_ber_schema.loaders.pdb_redo import PDBREDOLoader
from lambda_ber_schema.pydantic import Dataset


@pytest.fixture
def pdb_loader(mocker, pdb_1hho_entry_response, pdb_1hho_polymer_entities):
    """The wrapped PDB loader, answering from the 1HHO fixtures."""
    loader = PDBLoader()
    mocker.patch.object(loader, "_fetch_entry", return_value=pdb_1hho_entry_response)
    mocker.patch.object(
        loader, "_fetch_polymer_entities", return_value=pdb_1hho_polymer_entities
    )
    return loader


def _redo_loader(mocker, pdb_loader, properties, versions) -> PDBREDOLoader:
    loader = PDBREDOLoader(pdb_loader=pdb_loader)
    mocker.patch.object(loader, "_fetch_data", return_value=properties)
    mocker.patch.object(loader, "_fetch_versions", return_value=versions)
    return loader


@pytest.fixture
def loader(mocker, pdb_loader, pdb_redo_1hho_data, pdb_redo_1hho_versions):
    return _redo_loader(
        mocker, pdb_loader, pdb_redo_1hho_data["properties"], pdb_redo_1hho_versions
    )


@pytest.fixture
def result(loader):
    return loader.load("1hho")


def _redo_run(dataset: Dataset):
    [run] = [w for w in dataset.workflow_runs if w.software_name == "PDB-REDO"]
    return run


def _response(mocker, status_code: int, payload: dict | None = None):
    response = mocker.Mock()
    response.status_code = status_code
    response.json.return_value = payload
    response.raise_for_status = mocker.Mock(
        side_effect=requests.HTTPError(f"{status_code}") if status_code >= 400 else None
    )
    return response


def _not_found(mocker):
    """How pdb-redo.eu answers for an entry it does not hold: 500, not 404."""
    return _response(mocker, 500, {"error": "Not Found"})


class TestPDBREDOLoader:
    def test_dataset_is_named_for_pdb_redo(self, result):
        assert result.dataset.id == "pdb-redo:1HHO"
        assert result.dataset.title.startswith("PDB-REDO 1HHO: STRUCTURE OF HUMAN OXYHAEMOGLOBIN")
        assert result.source_url == "https://pdb-redo.eu/db/1hho"

    def test_pdb_rows_keep_their_ids(self, result, pdb_loader):
        """The crystal, molecules and experiment are the PDB entry's, so they join a PDB load."""
        pdb = pdb_loader.load("1HHO").dataset
        redo = result.dataset

        def ids(rows):
            return [row.id for row in rows or []]

        assert ids(redo.samples) == ids(pdb.samples)
        assert ids(redo.proteins) == ids(pdb.proteins)
        assert ids(redo.instruments) == ids(pdb.instruments)
        assert ids(redo.experiment_runs) == ids(pdb.experiment_runs)
        assert ids(redo.studies) == ids(pdb.studies)
        # The deposited refinement and the PDB files stay, with PDB-REDO's added after them
        assert ids(redo.workflow_runs)[: len(pdb.workflow_runs)] == ids(pdb.workflow_runs)
        assert ids(redo.data_files)[: len(pdb.data_files)] == ids(pdb.data_files)

    def test_run_records_the_final_model(self, result):
        run = _redo_run(result.dataset)
        assert run.id == "pdb-redo:1HHO/workflow/re-refinement"
        assert run.workflow_type == "model_refinement"
        assert run.software_version == "8.21"
        assert run.rwork.numeric_value == 0.2038
        assert run.rfree.numeric_value == 0.265
        assert run.clashscore.numeric_value == 8.59
        assert run.refinement_resolution_a.numeric_value == 2.1
        assert run.wilson_b_factor.numeric_value == 43.33
        assert run.space_group == "P 41 21 2"
        assert run.completed_at == "2026-08-21"
        assert run.deposited_to_pdb is False
        assert run.validation_report_path == "https://pdb-redo.eu/db/1hho/wf/pdbout.txt"
        assert "refmac 5.8.0431" in run.additional_software
        # Tools versions.json lists as unused are left out
        assert "ctruncate" not in run.additional_software

    def test_pdb_redo_supplies_an_r_free_the_deposition_lacks(self, result):
        """1HHO was deposited in 1983 without a test set; PDB-REDO chose one."""
        [experiment] = result.dataset.experiment_runs
        assert experiment.quality_metrics.r_work.numeric_value == 0.223
        assert experiment.quality_metrics.r_free is None
        assert _redo_run(result.dataset).rfree is not None

    def test_description_sets_the_final_r_free_against_the_unbiased_estimate(self, result):
        """Recalculated, 1HHO's R-free reads 0.2272; PDB-REDO's unbiased estimate is 0.2703."""
        description = _redo_run(result.dataset).description
        assert "R 0.2262 -> 0.2038" in description
        assert "R-free 0.2272 (estimated unbiased 0.2703) -> 0.265" in description

    def test_notes_compare_deposited_and_final(self, result):
        notes = _redo_run(result.dataset).processing_notes
        assert "Deposited header: R 0.223, R-free n/a." in notes
        assert "R-free 0.2272 (estimated unbiased R-free 0.2703), R-free Z-score 5.9." in notes
        assert "Re-refined and rebuilt: R 0.2038, R-free 0.265." in notes
        assert "MolProbity clashscore 29.75 -> 8.59" in notes
        assert "Ramachandran Z-score -5.588 -> -2.23" in notes
        assert "peptides flipped 0" in notes
        # versions.json says which PDB revision PDB-REDO worked from
        assert "Started from PDB model revision 2.3 and reflections revision 1_2." in notes

    def test_run_reads_the_deposited_model_and_structure_factors(self, result):
        ds = result.dataset
        run = _redo_run(ds)
        inputs = {
            (a.file_id, a.input_type) for a in ds.workflow_input_associations
            if a.workflow_id == run.id
        }
        assert inputs == {
            ("pdb:1HHO/file/mmcif", "structure_prior"),
            ("pdb:1HHO/file/sf", "raw_data"),
        }
        file_ids = {f.id for f in ds.data_files}
        assert all(file_id in file_ids for file_id, _ in inputs)

    def test_run_writes_the_pdb_redo_files(self, result):
        ds = result.dataset
        run = _redo_run(ds)
        files = {f.id: f for f in ds.data_files}
        outputs = {
            a.file_id: a.output_type for a in ds.workflow_output_associations
            if a.workflow_id == run.id
        }
        assert set(outputs) == {
            f"pdb-redo:1HHO/file/{key}"
            for key in (
                "final_cif", "final_pdb", "final_mtz", "besttls_cif", "besttls_mtz",
                "data", "versions", "archive",
            )
        }
        assert set(outputs) <= set(files)
        final = files["pdb-redo:1HHO/file/final_cif"]
        assert final.file_path == "https://pdb-redo.eu/db/1hho/1hho_final.cif"
        assert final.file_format == "mmcif"
        assert final.file_role == "final"
        assert outputs[final.id] == "model"
        assert files["pdb-redo:1HHO/file/besttls_cif"].file_role == "intermediate"
        archive = files["pdb-redo:1HHO/file/archive"]
        assert (archive.file_name, archive.file_path) == (
            "1hho.zip", "https://pdb-redo.eu/db/1hho/zipped"
        )

    def test_run_belongs_to_the_pdb_experiment(self, result):
        ds = result.dataset
        run = _redo_run(ds)
        assert [
            a.experiment_id for a in ds.workflow_experiment_associations
            if a.workflow_id == run.id
        ] == ["pdb:1HHO/experiment"]

    def test_no_pdb_format_file_for_a_model_too_big_for_it(
        self, mocker, pdb_loader, pdb_redo_1hho_data, pdb_redo_1hho_versions
    ):
        properties = copy.deepcopy(pdb_redo_1hho_data["properties"])
        properties["NOPDB"] = True
        ds = _redo_loader(mocker, pdb_loader, properties, pdb_redo_1hho_versions).load(
            "1HHO"
        ).dataset
        file_ids = {f.id for f in ds.data_files}
        assert "pdb-redo:1HHO/file/final_pdb" not in file_ids
        assert "pdb-redo:1HHO/file/final_cif" in file_ids
        assert "pdb-redo:1HHO/file/final_pdb" not in {
            a.file_id for a in ds.workflow_output_associations
        }

    def test_without_versions_json_the_version_comes_from_data_json(
        self, mocker, pdb_loader, pdb_redo_1hho_data
    ):
        loader = PDBREDOLoader(pdb_loader=pdb_loader)
        mocker.patch.object(
            loader, "_fetch_data", return_value=pdb_redo_1hho_data["properties"]
        )
        mocker.patch(
            "lambda_ber_schema.loaders.pdb_redo.requests.get",
            return_value=_not_found(mocker),
        )
        result = loader.load("1HHO")
        run = _redo_run(result.dataset)
        assert run.software_version == "8.21"
        assert run.additional_software is None
        assert "Started from" not in run.processing_notes
        assert any("versions.json" in w for w in result.warnings)

    def test_entry_not_in_pdb_redo_fails_before_the_pdb_is_asked(self, mocker):
        pdb_loader = mocker.Mock()
        get = mocker.patch(
            "lambda_ber_schema.loaders.pdb_redo.requests.get",
            return_value=_not_found(mocker),
        )
        loader = PDBREDOLoader(pdb_loader=pdb_loader)
        with pytest.raises(ValueError, match="7MLZ is not in the PDB-REDO databank"):
            loader.load("7mlz")
        assert get.call_args.args[0] == "https://pdb-redo.eu/db/7mlz/data.json"
        pdb_loader.load.assert_not_called()

    def test_a_plain_404_also_means_not_in_pdb_redo(self, mocker):
        mocker.patch(
            "lambda_ber_schema.loaders.pdb_redo.requests.get",
            return_value=_response(mocker, 404),
        )
        with pytest.raises(ValueError, match="not in the PDB-REDO databank"):
            PDBREDOLoader(pdb_loader=mocker.Mock()).load("1ABC")

    def test_a_server_failure_is_not_mistaken_for_a_missing_entry(self, mocker):
        mocker.patch(
            "lambda_ber_schema.loaders.pdb_redo.requests.get",
            return_value=_response(mocker, 500, {"error": "Internal Server Error"}),
        )
        with pytest.raises(requests.HTTPError):
            PDBREDOLoader(pdb_loader=mocker.Mock()).load("1CBS")

    def test_cache_keeps_the_summary_not_the_residue_angles(
        self, mocker, tmp_path, pdb_redo_1hho_data
    ):
        payload = {**pdb_redo_1hho_data, "rama-angles": [{"chains": ["many residues"]}]}
        get = mocker.patch(
            "lambda_ber_schema.loaders.pdb_redo.requests.get",
            return_value=_response(mocker, 200, payload),
        )
        cache = ResponseCache(cache_dir=tmp_path, enabled=True)
        loader = PDBREDOLoader(cache=cache, pdb_loader=mocker.Mock())

        first = loader._fetch_data("1HHO")
        second = loader._fetch_data("1HHO")

        assert first == second == pdb_redo_1hho_data["properties"]
        assert get.call_count == 1
        [cached] = list(tmp_path.glob("*.json"))
        assert "rama-angles" not in json.loads(cached.read_text())

    def test_dataset_round_trips_through_the_model(self, result):
        ds = result.dataset
        again = Dataset(**ds.model_dump(exclude_none=True, mode="json"))
        assert again.model_dump(exclude_none=True, mode="json") == ds.model_dump(
            exclude_none=True, mode="json"
        )

    def test_list_entries_lists_xray_pdb_entries(self, mocker):
        pdb_loader = mocker.Mock()
        pdb_loader.list_entries.return_value = ["1CBS", "1HHO"]
        loader = PDBREDOLoader(pdb_loader=pdb_loader)
        assert loader.list_entries(limit=2, experimental_method="EM") == ["1CBS", "1HHO"]
        pdb_loader.list_entries.assert_called_once_with(experimental_method="X-RAY", limit=2)

    def test_batch_listing_pages_through_xray_entries(self, mocker, tmp_path):
        batch = BatchLoader(PDBREDOLoader(pdb_loader=mocker.Mock()), output_dir=tmp_path)
        pages = mocker.patch.object(batch, "_get_all_pdb_entries", return_value=["1CBS"])
        assert batch._get_all_entries(limit=3, experimental_method="EM") == ["1CBS"]
        pages.assert_called_once_with(limit=3, experimental_method="X-RAY")


@pytest.mark.integration
class TestPDBREDOLoaderIntegration:
    """Hits pdb-redo.eu and the RCSB API."""

    def test_load_real_entry(self):
        result = PDBREDOLoader().load("1CBS")
        ds = result.dataset
        assert ds.id == "pdb-redo:1CBS"
        run = _redo_run(ds)
        assert run.rfree is not None and run.rwork is not None
        assert {a.file_id for a in ds.workflow_input_associations} == {
            "pdb:1CBS/file/mmcif", "pdb:1CBS/file/sf",
        }

    def test_cryo_em_entry_is_not_in_pdb_redo(self):
        with pytest.raises(ValueError, match="not in the PDB-REDO databank"):
            PDBREDOLoader().load("7MLZ")
