"""
Every field the RCSB Data API returns is accounted for, and what the field map says is carried is.

The field map (src/lambda_ber_schema/loaders/pdb_field_map.yaml) gives each field a disposition.
These tests hold it to three promises:

1. Nothing is unclassified, whether among the fields RCSB's schemas allow or the fields the
   captured entries actually contain.
2. Every target the map names is a real slot of a real class.
3. Every value the map says is carried, without an "as:" transformation, appears verbatim in
   the loader's output for the captured entries. A field cannot be marked carried and then
   quietly dropped.
"""

import math
import re

import pytest
from linkml_runtime import SchemaView

from lambda_ber_schema.loaders.base import dataset_to_dict
from lambda_ber_schema.loaders.pdb_coverage import (
    coverage,
    field_map,
    leaf_values,
    universe_report,
)

from .conftest import PDB_FIXTURE_ENTRIES

SCHEMA = "src/lambda_ber_schema/schema/lambda_ber_schema.yaml"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(SCHEMA)


@pytest.fixture(scope="module")
def loaded(request) -> dict:
    """Every fixture entry loaded once: entry id -> LoaderResult."""
    from lambda_ber_schema.loaders.pdb import PDBLoader

    from .conftest import read_pdb_fixture

    class FixturePDBLoader(PDBLoader):
        def _get(self, path, cache_key=None):
            return read_pdb_fixture(path)

    loader = FixturePDBLoader()
    return {entry: loader.load(entry) for entry in PDB_FIXTURE_ENTRIES}


def test_every_rcsb_field_has_a_disposition():
    report = universe_report()
    assert report.complete, f"Fields with no rule in pdb_field_map.yaml: {report.unclassified}"


@pytest.mark.parametrize("entry", PDB_FIXTURE_ENTRIES)
def test_every_fetched_field_has_a_disposition(loaded, entry):
    report = coverage(loaded[entry].raw_data)
    assert report.complete, f"{entry}: fields with no rule in pdb_field_map.yaml: {report.unclassified}"


def test_targets_are_schema_slots(schema_view):
    classes = set(schema_view.all_classes())
    problems = []
    for kind, rules in field_map().rules.items():
        for rule in rules.values():
            if rule.disposition == "to":
                cls, _, slot = rule.target.partition(".")
                if cls not in classes:
                    problems.append(f"{kind} {rule.key}: no class {cls}")
                elif slot not in schema_view.class_slots(cls):
                    problems.append(f"{kind} {rule.key}: {cls} has no slot {slot}")
            elif rule.disposition == "metric":
                cls = rule.target.split("[")[0]
                if cls not in classes:
                    problems.append(f"{kind} {rule.key}: no class {cls}")
                elif "additional_metrics" not in schema_view.class_slots(cls):
                    problems.append(f"{kind} {rule.key}: {cls} cannot hold additional metrics")
    assert not problems, "\n".join(problems)


def _output_values(result) -> tuple[list[float], list[str]]:
    """Every number and every string anywhere in the loader's output."""
    data = dataset_to_dict(result.dataset)
    numbers: list[float] = []
    strings: list[str] = []
    for _, value in leaf_values(data):
        if isinstance(value, bool):
            continue
        if isinstance(value, (int, float)):
            numbers.append(float(value))
        else:
            strings.append(str(value))
    return numbers, strings


def _appears(value, numbers: list[float], strings: list[str]) -> bool:
    """
    Whether a source value shows up in the output.

    Numbers match numerically, also when the source wrote them as text. Text matches case-blind,
    as a whole output string, as one item of a list the loader joined with ", " or "; ", or,
    from three characters up, inside a longer output string.
    """
    if isinstance(value, bool):
        return True
    number = value if isinstance(value, (int, float)) else None
    if isinstance(value, str):
        try:
            number = float(value)
        except ValueError:
            pass
    if number is not None:
        if any(math.isclose(float(number), n, rel_tol=1e-9, abs_tol=1e-12) for n in numbers):
            return True
        pattern = re.compile(rf"(?<![\d.]){re.escape(str(value).strip())}(?![\d])")
        return any(pattern.search(s) for s in strings)
    text = str(value).strip().lower()
    if not text:
        return True
    lowered = [s.strip().lower() for s in strings]
    if text in lowered:
        return True
    for s in lowered:
        if text in {t.strip() for t in s.replace("; ", ", ").split(", ")}:
            return True
    return len(text) >= 3 and any(text in s for s in lowered)


@pytest.mark.parametrize("entry", PDB_FIXTURE_ENTRIES)
def test_carried_values_appear_in_output(loaded, entry):
    result = loaded[entry]
    numbers, strings = _output_values(result)
    fmap = field_map()
    missing = []
    for kind, records in result.raw_data.items():
        for record in records:
            for path, value in leaf_values(record):
                rule = fmap.rule(kind, path)
                if rule is None or rule.disposition not in ("to", "metric") or rule.transformed:
                    continue
                if not _appears(value, numbers, strings):
                    missing.append(f"{kind} {path} = {str(value)[:60]!r} ({rule.disposition} {rule.target})")
    missing = sorted(set(missing))
    assert not missing, f"{entry}: {len(missing)} carried values missing from the output:\n" + "\n".join(missing)


def test_cli_reports_coverage(mocker):
    from typer.testing import CliRunner

    from lambda_ber_schema.cli import app

    from .conftest import read_pdb_fixture

    mocker.patch("lambda_ber_schema.loaders.pdb.PDBLoader._get", lambda self, path, cache_key=None: read_pdb_fixture(path))
    result = CliRunner().invoke(app, ["etl", "pdb-coverage", "--entry", "7ZYI"])
    assert result.exit_code == 0, result.output
    assert "unclassified: 0" in result.output
