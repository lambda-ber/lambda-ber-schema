"""Real MDRepo metadata fixtures and scientific/provenance regression checks."""

import copy
import hashlib
import json
from pathlib import Path

import pytest
import responses
import yaml
from typer.testing import CliRunner

from lambda_ber_schema.cli import app
from lambda_ber_schema.loaders import MDRepoLoader

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).parent / "fixtures/mdrepo"
CASES = [("MDR00020971", "apo", 29), ("MDR00021021", "ligand", 30), ("MDR00079393", "ensemble", 16)]


def source(slug="MDR00021021"):
    return json.loads((FIXTURES / f"{slug}.json").read_text())


@pytest.mark.parametrize("slug,case,file_count", CASES)
def test_real_examples_are_reproducible_and_linked(slug, case, file_count):
    raw = source(slug)
    before = copy.deepcopy(raw)
    result = MDRepoLoader().convert(raw)
    assert raw == before
    data = result.dataset.model_dump(mode="json", exclude_none=True)
    assert data == yaml.safe_load((ROOT / f"tests/data/valid/Dataset-mdrepo-{case}.yaml").read_text())
    assert len(data["data_files"]) == file_count == len(raw["uploaded_files"]) + len(raw["processed_files"])
    assert result.raw_data == raw
    assert all(f.checksum is None and f.storage_uri is None and f.file_path is None for f in result.dataset.data_files)
    assert all(json.loads(f.description)["md5_hash"] for f in result.dataset.data_files)
    targets = {
        "study_id": "studies", "sample_id": "samples", "protein_id": "proteins",
        "construct_id": "protein_constructs", "small_molecule_id": "small_molecules",
        "experiment_id": "experiment_runs", "workflow_id": "workflow_runs", "file_id": "data_files",
    }
    for table, rows in data.items():
        if not isinstance(rows, list):
            continue
        for row in rows:
            if not isinstance(row, dict):
                continue
            for key, target in targets.items():
                if key in row and not (table == "protein_constructs" and key == "construct_id"):
                    assert row[key] in {entity["id"] for entity in data.get(target, [])}, (table, row)
    assert not result.dataset.sample_component_interactions  # Co-occurrence does not prove binding.
    assert result.dataset.workflow_runs[0].started_at is None


def test_apo_ligands_and_units():
    apo = MDRepoLoader().convert(source("MDR00020971")).dataset
    assert not apo.small_molecules
    ds = MDRepoLoader().convert(source()).dataset
    assert ds.proteins[0].id == "uniprot:P52333"
    assert ds.small_molecules[0].inchikey == "AGTYRXOJPORGGM-LLVKDONJSA-N"
    assert ds.small_molecules[0].pdb_ligand_id is None  # Name alone does not establish CCD identity.
    params = ds.workflow_runs[0].md_simulation_params
    assert params.duration_ns.numeric_value == 500
    assert params.timestep.numeric_value == 2
    assert params.trajectory_output_interval.numeric_value == 5000
    assert params.trajectory_output_interval.unit == "steps"
    assert params.water_model is None  # Source prose mentions TIP3P; the structured field is null.
    assert params.protein_force_field is None
    assert json.loads(ds.workflow_runs[0].processing_parameters)["forcefield"] == "CHARMM36"
    assert ds.sample_protein_associations[0].residue_range == "813-1100"  # Alignment, not PDB numbering.


def test_mutant_sequence_and_ensemble_provenance():
    raw = source("MDR00079393")
    result = MDRepoLoader().convert(raw)
    ds = result.dataset
    canonical = ds.proteins[0].amino_acid_sequence
    simulated = raw["chains"][0]["polymer"]["sequence"]
    assert canonical == raw["uniprot"][0]["sequence"] != simulated
    assert json.loads(ds.protein_constructs[0].description)[0]["polymer"]["sequence"] == simulated
    assert len(ds.workflow_runs) == 1
    workflow = ds.workflow_runs[0]
    assert json.loads(workflow.processing_parameters)["num_replicates"] == 5
    assert json.loads(workflow.processing_parameters)["duration"] == 19.5
    assert workflow.md_simulation_params.duration_ns is None
    assert any("replicates" in w for w in result.warnings)
    # A processed file is not claimed to have been produced directly by AMBER.
    assert all("/uploaded_files/" in assoc.file_id for assoc in ds.workflow_output_associations)


def test_duplicate_chain_labels_do_not_collapse_copies():
    raw = source()
    second = copy.deepcopy(raw["chains"][0])
    second["chain_order"] = 2
    raw["chains"].append(second)
    ds = MDRepoLoader().convert(raw).dataset
    assert len(ds.proteins) == 1
    assert ds.sample_protein_associations[0].copy_number == 2
    protein_component = next(c for c in ds.sample_components if c.protein_id)
    assert protein_component.copy_number == 2
    assert [c["chain_order"] for c in json.loads(protein_component.description)] == [1, 2]


def test_no_single_uniprot_match_does_not_claim_canonical_identity():
    raw = source()
    raw["chains"][0]["polymer"]["uniprots"] = []
    result = MDRepoLoader().convert(raw)
    protein = result.dataset.proteins[0]
    assert protein.id.startswith("lambda:mdrepo/")
    assert protein.uniprot_id is None
    assert protein.amino_acid_sequence == raw["chains"][0]["polymer"]["sequence"]
    assert result.dataset.sample_protein_associations[0].residue_range is None


def test_unknown_format_is_reported_and_source_retained():
    raw = source()
    raw["uploaded_files"][0]["filename"] = "unknown.xyz123"
    result = MDRepoLoader().convert(raw)
    assert any("unknown.xyz123" in w for w in result.warnings)
    assert result.raw_data == raw


@pytest.mark.parametrize("value", [None, 0, 3])
def test_missing_or_nonintegral_step_interval_is_not_invented(value):
    raw = source()
    raw["integration_timestep_fs"] = value
    result = MDRepoLoader().convert(raw)
    assert result.dataset.workflow_runs[0].md_simulation_params.trajectory_output_interval is None
    assert any("interval" in w for w in result.warnings)


@pytest.mark.parametrize("value", [-1, float("nan"), float("inf"), True])
def test_bad_quantities_rejected(value):
    raw = source()
    raw["duration"] = value
    with pytest.raises(ValueError):
        MDRepoLoader().convert(raw)


@responses.activate
def test_numeric_endpoint_and_no_payload_requests():
    url = f"{MDRepoLoader.base_url}/simulation_view/21021"
    responses.get(url, json=source())
    assert MDRepoLoader().load("mdr00021021").dataset.proteins[0].id == "uniprot:P52333"
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url


@pytest.mark.parametrize("value", ["", "../21021", "MDR-1", "0", "https://mdrepo.org/21021"])
def test_bad_identifiers_rejected_before_network(value):
    with pytest.raises(ValueError):
        MDRepoLoader().load(value)


@responses.activate
def test_list_pagination_keeps_filters_and_limit():
    url = f"{MDRepoLoader.base_url}/simulation_list"
    responses.get(url, json={"results": [{"slug": "MDR00020971"}], "next": "next-page"})
    responses.get(url, json={"results": [{"slug": "MDR00021021"}], "next": None})
    assert MDRepoLoader().list_entries(limit=2, has_ligand=True) == ["MDR00020971", "MDR00021021"]
    assert "offset=1" in responses.calls[1].request.url
    assert "has_ligand=True" in responses.calls[1].request.url
    assert MDRepoLoader().list_entries(limit=0) == []


def test_offline_cli_and_preserved_source(tmp_path):
    output, raw_output = tmp_path / "data.json", tmp_path / "raw.json"
    result = CliRunner().invoke(app, ["etl", "mdrepo", "--metadata", str(FIXTURES / "MDR00021021.json"),
                                     "--format", "json", "--output", str(output), "--raw-output", str(raw_output)])
    assert result.exit_code == 0, result.output
    assert json.loads(output.read_text())["proteins"][0]["id"] == "uniprot:P52333"
    assert json.loads(raw_output.read_text()) == source()


def test_cli_rejects_ambiguous_inputs_and_overwriting_source(tmp_path):
    runner = CliRunner()
    assert runner.invoke(app, ["etl", "mdrepo"]).exit_code == 2
    path = tmp_path / "source.json"
    path.write_text(json.dumps(source()))
    for args in (["--metadata", str(path), "--entry", "21021"],
                 ["--metadata", str(path), "--output", str(path)]):
        assert runner.invoke(app, ["etl", "mdrepo", *args]).exit_code == 2
    assert json.loads(path.read_text()) == source()


def test_snapshot_checksums():
    manifest = json.loads((FIXTURES / "manifest.json").read_text())
    for entry in manifest["entries"]:
        assert entry["retrieved_at"]
        assert hashlib.sha256((FIXTURES / f"{entry['id']}.json").read_bytes()).hexdigest() == entry["snapshot_sha256"]
