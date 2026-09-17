"""Conformance tests for the LAMBDA Core RO-Crate profile.

The checker itself lives in ``lambda_ber_schema.rocrate.validation`` and is what
``lambda-ber-schema rocrate validate`` runs. These tests drive it over the fixtures in
``tests/data/rocrate/`` and pin the things a user-facing checker must not drift on: that the
shipped schema matches the source, that the graph rules read real profile terms, that every
negative fixture fails for the reason it was written to fail, and that the legacy SSRL crate's
gaps are exactly the known ones.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from lambda_ber_schema.rocrate import validation as v
from lambda_ber_schema.rocrate.validation import (
    GRAPH_RULE_TERMS,
    classify,
    entity_types,
    entity_violations,
    graph_rule_violations,
    root_of,
    validate_crate,
    validate_path,
)

REPO = Path(__file__).resolve().parent.parent
CRATES = REPO / "tests" / "data" / "rocrate"
GENERATED_SCHEMA = REPO / "assets" / "rocrate" / "jsonschema" / "lambda_rocrate_core.schema.json"


# --------------------------------------------------------------------------------------
# schema loading
# --------------------------------------------------------------------------------------


@pytest.fixture(scope="session")
def json_schema() -> dict:
    """The JSON Schema built fresh from the YAML, once.

    Built rather than loaded so that the tests check the *source* profile. Whether the shipped
    copies agree with it is a separate test below. ``scope="session"`` is load-bearing: generation
    traverses the whole of ``lambda_ber_schema`` through the import, which takes seconds.
    """
    return v.generate_schema()


def _crates(subdir: str) -> list[Path]:
    return sorted((CRATES / subdir).glob("*.json"))


VALID = _crates("valid")
INVALID = _crates("invalid")
LEGACY = _crates("legacy")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------------------
# layer 1 - document shape
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("path", VALID + LEGACY, ids=lambda p: p.name)
def test_document_shape(json_schema, path):
    """Every crate, including the legacy one, is a well-formed RO-Crate metadata document."""
    errors = v.document_violations(json_schema, load(path))
    assert not errors, f"{path.name} is not a valid crate document:\n" + "\n".join(errors)


def test_shipped_schema_matches_source(json_schema):
    """The copies in ``assets/`` and inside the package are what the YAML currently generates.

    Guards the ``gen-rocrate`` step twice over: gen-project roots the JSON Schema at the imported
    schema's ``tree_root``, so if the ``--top-class`` regeneration is ever dropped from the
    Makefile the published artifact would silently describe ``Dataset`` instead of a crate; and
    the packaged copy is what a plain install validates against, so a stale one means users and
    tests disagree about what conforms.
    """
    for shipped in (GENERATED_SCHEMA, v.packaged_schema_path()):
        assert shipped.exists(), f"{shipped} is missing; run `make gen-rocrate`"
        schema = json.loads(shipped.read_text(encoding="utf-8"))
        assert set(schema["properties"]) == {"@context", "@graph"}, (
            f"{shipped} is not rooted at the crate document - "
            "was gen-json-schema --top-class dropped?"
        )
        assert schema == json_schema, f"{shipped} is stale; run `make gen-rocrate`"


def test_load_schema_defaults_to_packaged_copy():
    if not v.packaged_schema_path().exists():
        pytest.skip("run `make gen-rocrate` first")
    assert v.DOCUMENT_CLASS in v.load_schema()["$defs"]


# --------------------------------------------------------------------------------------
# layer 2 - per-entity
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_entities_conform(json_schema, path):
    problems = entity_violations(json_schema, load(path))
    assert not problems, f"{path.name} has non-conformant entities:\n" + "\n".join(problems)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_every_entity_is_classifiable(path):
    """A reader must be able to tell what each entity is from its @type alone."""
    unclassified = [e.get("@id") for e in v.graph(load(path)) if classify(e) is None]
    assert not unclassified, f"{path.name}: unclassifiable entities {unclassified}"


def test_classify_descriptor_branches():
    """All three descriptor cases: ordinary, detached (absolute URI + about), nested (a File)."""
    assert classify({"@id": "ro-crate-metadata.json"}) == "MetadataDescriptor"
    assert classify({"@id": "https://x/ro-crate-metadata.json", "about": {}}) == "MetadataDescriptor"
    assert classify({"@id": "saxs/ro-crate-metadata.json", "@type": "File"}) == "CrateFile"


# --------------------------------------------------------------------------------------
# layer 3 - graph rules
# --------------------------------------------------------------------------------------


def test_graph_rule_keys_are_profile_terms(json_schema):
    """Every key the graph rules read must be a real property of the class they read it from.

    A crate writing a slot's canonical snake_case name rather than its alias is already rejected by
    the per-entity layer, whose classes are closed - so there is no path by which a wrong spelling
    quietly passes. What this guards is the opposite direction: the profile renaming a term out from
    under a rule that would then check nothing and report nothing.
    """
    for class_name, keys in GRAPH_RULE_TERMS.items():
        properties = set(json_schema["$defs"][class_name]["properties"])
        stranded = sorted(set(keys) - properties)
        assert not stranded, (
            f"{class_name}: graph rules read {stranded}, which the profile no longer declares - "
            "the rule is now inert"
        )


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_graph_rules(path):
    problems = graph_rule_violations(load(path))
    assert not problems, f"{path.name} breaks graph rules:\n" + "\n".join(problems)


def test_root_must_declare_profile_conformance():
    """A crate that does not claim the profile cannot be checked against it (rule 7)."""
    crate = load(CRATES / "valid" / "minimal-manifest.json")
    root = root_of(crate)
    root["conformsTo"] = [{"@id": "https://w3id.org/ro/crate/1.2"}]
    problems = graph_rule_violations(crate)
    assert any("names no LAMBDA Core profile" in p for p in problems), problems
    assert not any("names no RO-Crate version" in p for p in problems), problems

    root["conformsTo"] = [{"@id": "https://w3id.org/lambda/profile/core/0.3.1"}]
    problems = graph_rule_violations(crate)
    assert any("names no RO-Crate version" in p for p in problems), problems


# --------------------------------------------------------------------------------------
# negative cases - each fixture isolates one rule
# --------------------------------------------------------------------------------------

#: fixture name -> a fragment that must appear in the reported failure, so a test that passes
#: for the wrong reason is caught.
EXPECTED_FAILURE = {
    "no-checksum.json": "sha256",
    "no-license.json": "omits 'license'",
    "datafile-type-token.json": "not an RO-Crate term",
    "designation-no-association.json": "prov:qualifiedAssociation",
    "estimator-no-admissibility.json": "admissibility",
    "missing-no-reason.json": "reason",
    "bare-technique-terms.json": "ccHalf",
    "dangling-about.json": "not in the graph",
    "dangling-haspart.json": "no entity in the graph",
    "dangling-inline-ref.json": "promised_but_absent",
    "dangling-protein-part.json": "hasBioChemEntityPart",
    "protein-no-accession.json": "no uniprot_id and no declared absence",
    "nucleic-acid-no-identity.json": "nucleic acid with no rnacentral_id",
}


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.name)
def test_invalid_crates_are_rejected(json_schema, path):
    crate = load(path)
    problems = entity_violations(json_schema, crate) + graph_rule_violations(crate)
    assert problems, f"{path.name} was accepted but should not have been"

    expected = EXPECTED_FAILURE[path.name]
    assert any(expected in p for p in problems), (
        f"{path.name} failed, but not for the expected reason ({expected!r}):\n"
        + "\n".join(problems)
    )


def test_every_invalid_fixture_is_accounted_for():
    assert {p.name for p in INVALID} == set(EXPECTED_FAILURE), (
        "an invalid fixture has no expected-failure entry, so it could pass for any reason"
    )


# --------------------------------------------------------------------------------------
# legacy SSRL crates - pinning the known gaps rather than pretending they conform
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("path", LEGACY, ids=lambda p: p.name)
def test_legacy_crate_uses_the_deprecated_vocabulary(path):
    """The 0.2 spelling still classifies. This is the alias layer doing its job."""
    crate = load(path)
    root = root_of(crate)
    assert root is not None, f"{path.name}: 0.2 root did not classify as CrateRoot"
    assert "lambda:Experiment" in entity_types(root), "expected the deprecated 0.2 root type"
    assert all(classify(e) is not None for e in v.graph(crate)), (
        "some 0.2 entity has no profile class"
    )


#: What stops the published SSRL 0.2 crate from conforming to Core 0.3.2. Each is a real,
#: actionable gap rather than a naming difference - the naming differences are handled by the
#: alias layer and do not appear here. If one of these disappears, this test fails and the
#: entry should be removed.
LEGACY_KNOWN_GAPS = {
    "ssrl-mx-XA_x16-core-0.2.json": [
        "omits 'license' without declaring it",  # not merely absent - absent and unstated
        "'lambda:unitCell'",  # MX quantities as bare properties, not nested in resultSummary
        "no metadata pointer",  # RawUnit and DerivedProduct point nowhere for fuller metadata
        "names no RO-Crate version",  # conformsTo names the 0.2 profiles and nothing else
    ],
}


@pytest.mark.parametrize("path", LEGACY, ids=lambda p: p.name)
def test_legacy_crate_gaps_are_exactly_the_known_ones(json_schema, path):
    crate = load(path)
    problems = entity_violations(json_schema, crate) + graph_rule_violations(crate)
    report = "\n".join(problems)
    for gap in LEGACY_KNOWN_GAPS[path.name]:
        assert gap in report, (
            f"{path.name}: expected known gap {gap!r} is no longer reported - "
            "if the crate was fixed upstream, drop it from LEGACY_KNOWN_GAPS"
        )


# --------------------------------------------------------------------------------------
# the user-facing surface - validate_crate / validate_path / the CLI
# --------------------------------------------------------------------------------------


def test_validate_crate_report_layers(json_schema):
    crate = load(CRATES / "invalid" / "datafile-type-token.json")
    report = validate_crate(crate, json_schema, source="x")
    assert not report.ok
    assert report.by_layer("graph"), "the DataFile token is a graph-rule finding"
    assert {f.layer for f in report.findings} <= set(v.LAYERS)
    assert report.to_dict()["conformant"] is False


def test_validate_crate_rejects_unknown_layer(json_schema):
    with pytest.raises(ValueError):
        validate_crate({}, json_schema, layers=("shape",))


def test_validate_crate_only_graph_needs_no_schema():
    """Layer 3 is pure Python over the graph, so it must not require the JSON Schema."""
    report = validate_crate(load(CRATES / "invalid" / "no-license.json"), None, layers=("graph",))
    assert any("omits 'license'" in f.message for f in report.findings)


def test_validate_path_accepts_a_crate_directory(json_schema, tmp_path):
    crate_dir = tmp_path / "crate"
    crate_dir.mkdir()
    (crate_dir / v.METADATA_FILE).write_text((CRATES / "valid" / "minimal-manifest.json").read_text(encoding="utf-8"))
    assert validate_path(crate_dir, json_schema).ok
    with pytest.raises(FileNotFoundError):
        validate_path(tmp_path, json_schema)


def test_validate_path_reports_bad_json(json_schema, tmp_path):
    bad = tmp_path / "ro-crate-metadata.json"
    bad.write_text("{not json")
    report = validate_path(bad, json_schema)
    assert not report.ok
    assert "not valid JSON" in report.findings[0].message


def test_validate_path_reads_utf8_regardless_of_locale(json_schema, tmp_path, monkeypatch):
    """RO-Crate mandates UTF-8; the platform default encoding must not get a say."""
    crate = load(CRATES / "valid" / "minimal-manifest.json")
    root_of(crate)["name"] = "Glutamyl-tRNA synthetase \u00e0 la SIBYLS \u2014 \u03b2 sheet"
    path = tmp_path / v.METADATA_FILE
    path.write_bytes(json.dumps(crate, ensure_ascii=False).encode("utf-8"))
    monkeypatch.setattr(Path, "read_text", _ascii_only_read_text)
    assert validate_path(path, json_schema).ok


def _ascii_only_read_text(self, encoding=None, errors=None):
    """Stand-in for a platform whose default text encoding is not UTF-8."""
    with open(self, encoding=encoding or "ascii", errors=errors) as fh:
        return fh.read()


def test_validate_path_raises_on_unreadable_file(json_schema, tmp_path):
    """A file that exists but cannot be read is a path problem, not a crate finding."""
    import os

    if os.geteuid() == 0:
        pytest.skip("root can read anything")
    locked = tmp_path / v.METADATA_FILE
    locked.write_text("{}")
    locked.chmod(0)
    try:
        with pytest.raises(PermissionError):
            validate_path(locked, json_schema)
    finally:
        locked.chmod(0o644)


@pytest.fixture(scope="module")
def cli():
    from lambda_ber_schema.cli import app

    runner = CliRunner()
    return lambda *args: runner.invoke(app, ["rocrate", "validate", *args])


@pytest.mark.skipif(not v.packaged_schema_path().exists(), reason="run `make gen-rocrate` first")
class TestCLI:
    def test_valid_crates_exit_zero(self, cli):
        result = cli(*(str(p) for p in VALID))
        assert result.exit_code == 0, result.output
        assert result.output.count("conformant") == len(VALID)

    def test_invalid_crate_exits_one_and_names_the_rule(self, cli):
        result = cli(str(CRATES / "invalid" / "no-license.json"))
        assert result.exit_code == 1, result.output
        assert "[graph]" in result.output
        assert "omits 'license'" in result.output

    def test_missing_file_exits_two(self, cli):
        result = cli("does-not-exist.json")
        assert result.exit_code == 2, result.output

    def test_json_output(self, cli):
        result = cli("--json", "--layer", "graph", str(CRATES / "invalid" / "dangling-about.json"))
        assert result.exit_code == 1, result.output
        [report] = json.loads(result.output)
        assert report["conformant"] is False
        assert all(f["layer"] == "graph" for f in report["findings"])

    def test_json_output_is_one_array_over_many_crates(self, cli):
        """Several crates and all three layers still come out as one parseable document."""
        result = cli("--json", str(VALID[0]), str(CRATES / "invalid" / "no-license.json"))
        assert result.exit_code == 1, result.output
        reports = json.loads(result.output)
        assert [r["conformant"] for r in reports] == [True, False]
        assert reports[0]["source"] == str(VALID[0])

    def test_unreadable_file_exits_two(self, cli, tmp_path):
        import os

        if os.geteuid() == 0:
            pytest.skip("root can read anything")
        locked = tmp_path / v.METADATA_FILE
        locked.write_text("{}")
        locked.chmod(0)
        try:
            result = cli(str(locked))
        finally:
            locked.chmod(0o644)
        assert result.exit_code == 2, result.output

    def test_quiet_prints_nothing(self, cli):
        result = cli("--quiet", str(CRATES / "invalid" / "no-license.json"))
        assert result.exit_code == 1
        assert result.output == ""

    def test_explicit_schema(self, cli):
        result = cli("--schema", str(GENERATED_SCHEMA), str(VALID[0]))
        assert result.exit_code == 0, result.output

    def test_unknown_layer_exits_two(self, cli):
        result = cli("--layer", "shape", str(VALID[0]))
        assert result.exit_code == 2
