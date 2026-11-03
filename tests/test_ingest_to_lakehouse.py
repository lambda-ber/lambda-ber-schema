"""Tests for scripts/ingest_to_lakehouse.py. No live lakehouse calls."""

import importlib.util
import json
import typing
from pathlib import Path

import pandas as pd
import pytest
import yaml
from pydantic import BaseModel

from lambda_ber_schema.pydantic import Dataset

REPO_ROOT = Path(__file__).resolve().parent.parent
VALID_DIR = REPO_ROOT / "tests" / "data" / "valid"

_spec = importlib.util.spec_from_file_location(
    "ingest_to_lakehouse", REPO_ROOT / "scripts" / "ingest_to_lakehouse.py"
)
ingest = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ingest)

# Iceberg metadata-table names, which Polaris rejects as table names.
ICEBERG_METADATA_TABLES = {
    "all_data_files", "all_delete_files", "all_entries", "all_files", "all_manifests",
    "data_files", "delete_files", "entries", "files", "history", "manifests",
    "metadata_log_entries", "partitions", "position_deletes", "refs", "snapshots",
}


def _is_model(annotation) -> bool:
    """True for a pydantic model, or a union of them such as the instrument subclasses."""
    members = typing.get_args(annotation) or (annotation,)
    return all(isinstance(m, type) and issubclass(m, BaseModel) for m in members)


def _pydantic_entity_fields() -> set[str]:
    """Names of `Dataset` fields typed as a list of pydantic models."""
    fields = set()
    for name, field in Dataset.model_fields.items():
        for arg in typing.get_args(field.annotation):
            if typing.get_origin(arg) is list and _is_model(typing.get_args(arg)[0]):
                fields.add(name)
    return fields


def test_entity_slots_match_dataset_model():
    assert set(ingest.get_entity_slots()) == _pydantic_entity_fields()


def test_entity_slots_exclude_non_class_slots():
    assert not {"keywords", "id", "title"} & set(ingest.get_entity_slots())


@pytest.mark.parametrize("slot", [
    "proteins", "nucleic_acids", "small_molecules", "sample_components",
    "sample_component_interactions", "sample_protein_associations",
    "sample_nucleic_acid_associations", "persons", "organizations",
    "study_person_associations", "experiment_person_associations",
    "workflow_person_associations", "study_organization_associations",
    "person_organization_associations",
])
def test_previously_dropped_slots_are_covered(slot):
    assert slot in ingest.get_entity_slots()


def test_silver_table_names_avoid_iceberg_metadata_tables():
    names = {ingest.SLOT_TO_SILVER_NAME.get(s, s) for s in ingest.get_entity_slots()}
    assert not names & ICEBERG_METADATA_TABLES


def test_shared_slots_are_entity_slots():
    assert set(ingest.SHARED_ENTITY_SLOTS) <= set(ingest.get_entity_slots())


def test_identical_rows_collapse_ignoring_source_entry_id():
    rows = [
        {"source_entry_id": "a", "id": "uniprot:P1", "title": "x"},
        {"source_entry_id": "b", "id": "uniprot:P1", "title": "x"},
        {"source_entry_id": "b", "id": "uniprot:P2", "title": "y"},
    ]
    deduped, conflicts = ingest.dedupe_shared_rows("proteins", rows)
    assert deduped == [{"id": "uniprot:P1", "title": "x"}, {"id": "uniprot:P2", "title": "y"}]
    assert conflicts == []


def test_conflicting_rows_keep_first_and_are_reported():
    rows = [
        {"source_entry_id": "a", "id": "i1", "description": "Pilatus 2M"},
        {"source_entry_id": "b", "id": "i1", "description": "Pilatus 1M"},
        {"source_entry_id": "c", "id": "i1", "description": "Pilatus 1M", "manufacturer": "m"},
    ]
    deduped, conflicts = ingest.dedupe_shared_rows("instruments", rows)
    assert deduped == [{"id": "i1", "description": "Pilatus 2M"}]
    assert len(conflicts) == 1
    assert conflicts[0]["key"] == "i1"
    assert conflicts[0]["rows"] == 2
    assert conflicts[0]["fields"]["description"] == ["Pilatus 2M", "Pilatus 1M"]
    assert conflicts[0]["fields"]["manufacturer"] == [None, "m"]


def test_proteins_take_most_common_values_with_fields_paired():
    rows = [
        {"source_entry_id": "a", "id": "p", "protein_name": "BSA, dimer", "title": "BSA, dimer",
         "amino_acid_sequence": "AAAA", "sequence_length": 4},
        {"source_entry_id": "b", "id": "p", "protein_name": "BSA", "title": "BSA",
         "amino_acid_sequence": "CC", "sequence_length": 2},
        {"source_entry_id": "c", "id": "p", "protein_name": "BSA", "title": "BSA",
         "amino_acid_sequence": "CC", "sequence_length": 2},
    ]
    deduped, conflicts = ingest.dedupe_shared_rows("proteins", rows)
    assert deduped == [{"id": "p", "protein_name": "BSA", "title": "BSA",
                        "amino_acid_sequence": "CC", "sequence_length": 2}]
    assert set(conflicts[0]["fields"]["protein_name"]) == {"BSA", "BSA, dimer"}


def test_missing_values_do_not_outvote_recorded_ones():
    rows = [
        {"source_entry_id": "a", "id": "p"},
        {"source_entry_id": "b", "id": "p"},
        {"source_entry_id": "c", "id": "p", "organism_name": "Homo sapiens"},
    ]
    deduped, _ = ingest.dedupe_shared_rows("proteins", rows)
    assert deduped[0]["organism_name"] == "Homo sapiens"


def test_entry_protein_details_are_copied_to_associations():
    rows_by_slot = {
        "proteins": [
            {"source_entry_id": "a", "id": "p", "protein_name": "tau", "amino_acid_sequence": "AAA"},
            {"source_entry_id": "b", "id": "p", "protein_name": "tau fragment"},
        ],
        "sample_protein_associations": [
            {"source_entry_id": "a", "sample_id": "s1", "protein_id": "p"},
            {"source_entry_id": "b", "sample_id": "s2", "protein_id": "p"},
            {"source_entry_id": "c", "sample_id": "s3", "protein_id": "other"},
        ],
    }
    ingest.copy_protein_details_to_associations(rows_by_slot)
    first, second, third = rows_by_slot["sample_protein_associations"]
    assert first["entry_protein_name"] == "tau"
    assert first["entry_amino_acid_sequence"] == "AAA"
    assert second["entry_protein_name"] == "tau fragment"
    assert "entry_amino_acid_sequence" not in second
    assert "entry_protein_name" not in third


def test_instrument_code_is_the_fallback_key():
    rows = [
        {"source_entry_id": "a", "instrument_code": "X33"},
        {"source_entry_id": "b", "instrument_code": "X33"},
    ]
    deduped, _ = ingest.dedupe_shared_rows("instruments", rows)
    assert deduped == [{"instrument_code": "X33"}]


def test_rows_without_a_key_are_kept():
    rows = [{"source_entry_id": "a", "title": "x"}, {"source_entry_id": "b", "title": "x"}]
    deduped, conflicts = ingest.dedupe_shared_rows("proteins", rows)
    assert len(deduped) == 2
    assert conflicts == []


def test_convert_dedupes_shared_tables_only(tmp_path):
    dump_dir = tmp_path / "dump"
    dump_dir.mkdir()
    doc = yaml.safe_load((VALID_DIR / "Dataset-cas9-nucleic-acid-entities.yaml").read_text())
    assert doc.get("proteins") and doc.get("samples")
    for name in ("one", "two"):
        (dump_dir / f"{name}.yaml").write_text(yaml.safe_dump({**doc, "id": f"test:{name}"}))

    staging = tmp_path / "staging"
    slots = ingest.convert_yamls_to_parquet(dump_dir, staging)

    assert "proteins" in slots
    proteins = pd.read_parquet(staging / "proteins.parquet")
    assert proteins["id"].is_unique
    assert len(proteins) == len(doc["proteins"])
    assert "source_entry_id" not in proteins.columns

    samples = pd.read_parquet(staging / "samples.parquet")
    assert len(samples) == 2 * len(doc["samples"])
    assert set(samples["source_entry_id"]) == {"test:one", "test:two"}
    assert json.loads((staging / "dedupe_conflicts.json").read_text()) == []


class _FakeMinio:
    def __init__(self, objects):
        self.objects = objects

    def list_objects(self, bucket, prefix, recursive):
        return iter(self.objects)


class _FakeCatalog:
    def __init__(self, exists):
        self.exists = exists

    def databaseExists(self, name):
        return self.exists


class _FakeSpark:
    def __init__(self, exists, table_count=0):
        self.catalog = _FakeCatalog(exists)
        self.table_count = table_count

    def sql(self, statement):
        assert statement.startswith("SHOW TABLES IN"), statement
        count = self.table_count

        class _Result:
            def count(self):
                return count

        return _Result()


def test_guard_refuses_existing_bronze_objects():
    with pytest.raises(RuntimeError, match="already has objects"):
        ingest.ensure_target_is_new(_FakeMinio(["obj"]), None, "b", "lambda", "sasbdb")


def test_guard_refuses_existing_silver_tables():
    with pytest.raises(RuntimeError, match="already has tables"):
        ingest.ensure_target_is_new(None, _FakeSpark(True, 3), "b", "lambda", "sasbdb")


def test_guard_allows_new_target():
    ingest.ensure_target_is_new(_FakeMinio([]), _FakeSpark(False), "b", "lambda", "sasbdb_202611")
    ingest.ensure_target_is_new(_FakeMinio([]), _FakeSpark(True, 0), "b", "lambda", "sasbdb_202611")


def test_suffix_changes_bronze_and_namespace_but_not_source_name(tmp_path):
    (tmp_path / "samples.parquet").write_bytes(b"")
    pd.DataFrame({"id": ["x"]}).to_parquet(tmp_path / "samples.parquet")
    config = ingest.build_ingest_config(
        "ssrl-mx", "lambda", "cdm-lake", tmp_path, ["samples"], dataset_suffix="_202611"
    )
    assert config["dataset"] == "ssrl_mx_202611"
    assert config["paths"]["bronze_base"].endswith("/datasets/ssrl_mx_202611/")
    assert config["tables"][0]["bronze_path"].endswith("/datasets/ssrl_mx_202611/samples.parquet")
