"""Conformance tests for the LAMBDA Core RO-Crate profile.

Three layers, matching the validation model in ``lambda_rocrate_core.yaml``:

1. **Document shape** - each crate validates against ``ROCrateMetadataDocument``.
2. **Per-entity** - each ``@graph`` entity is dispatched on its ``@type`` and validated against
   the matching profile class. These classes are closed, so an undeclared term fails here. This
   is the layer that actually bites.
3. **Graph rules** - the cross-entity constraints neither JSON Schema nor per-entity validation
   can state, because they are about relationships between entities rather than the shape of any
   one of them. They live here as plain functions; lifting them into a shipped conformance
   checker is a separate, deliberate step.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

jsonschema = pytest.importorskip("jsonschema")

REPO = Path(__file__).resolve().parent.parent
SCHEMA = REPO / "src" / "lambda_ber_schema" / "schema" / "lambda_rocrate_core.yaml"
CRATES = REPO / "tests" / "data" / "rocrate"

DOCUMENT_CLASS = "ROCrateMetadataDocument"


# --------------------------------------------------------------------------------------
# schema loading
# --------------------------------------------------------------------------------------


@pytest.fixture(scope="session")
def json_schema() -> dict:
    """The generated JSON Schema, built once - generation parses the whole imported schema."""
    from linkml.generators.jsonschemagen import JsonSchemaGenerator

    return json.loads(
        JsonSchemaGenerator(str(SCHEMA), top_class=DOCUMENT_CLASS).serialize()
    )


def _validator(json_schema: dict, class_name: str):
    """A validator for one profile class, reusing the document schema's ``$defs``."""
    assert class_name in json_schema["$defs"], f"{class_name} is not in the generated schema"
    return jsonschema.Draft201909Validator(
        {"$ref": f"#/$defs/{class_name}", "$defs": json_schema["$defs"]}
    )


def _flatten(error) -> list:
    """Descend into ``anyOf``/``oneOf`` sub-errors.

    LinkML wraps every optional object slot in ``anyOf: [<class>, null]``, so a violation inside
    one reports only "is not valid under any of the given schemas" at the top. The useful message -
    which property is missing - is in ``error.context``.
    """
    if not error.context:
        return [error]
    return [sub for child in error.context for sub in _flatten(child)]


def _errors(validator, instance) -> list[str]:
    return [
        f"{'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
        for top in validator.iter_errors(instance)
        for e in _flatten(top)
    ]


# --------------------------------------------------------------------------------------
# @type dispatch - the rule a reader applies to decide what an entity is
# --------------------------------------------------------------------------------------

#: Checked in order: the first matching type wins, so the specific ``lambda:`` types are
#: consulted before the generic RO-Crate ones an entity also carries.
DISPATCH: list[tuple[str, str]] = [
    ("lambda:Dataset", "CrateRoot"),
    ("lambda:Experiment", "CrateRoot"),  # deprecated SSRL 0.2 spelling
    ("lambda:Sample", "SampleEntity"),
    ("lambda:Instrument", "InstrumentEntity"),
    ("lambda:ExperimentRun", "ExperimentRunAction"),
    ("lambda:WorkflowRun", "WorkflowRunAction"),
    ("CreateAction", "WorkflowRunAction"),
    ("Person", "PersonEntity"),
    ("Organization", "OrganizationEntity"),
    ("SoftwareApplication", "SoftwareApplicationEntity"),
    ("DefinedTerm", "DefinedTermEntity"),
    ("PropertyValue", "PropertyValueEntity"),
    ("File", "CrateFile"),
    # Not an RO-Crate term - see FILE_TYPE_RULE below. Dispatched so the real defect is reported
    # instead of a bare "unclassifiable entity".
    ("DataFile", "CrateFile"),
    ("Dataset", "CrateDatasetPart"),
    ("CreativeWork", "RelatedWork"),
]


def entity_types(entity: dict) -> list[str]:
    raw = entity.get("@type", [])
    return [raw] if isinstance(raw, str) else list(raw)


def classify(entity: dict) -> str | None:
    """Which profile class an entity should be validated against.

    The metadata descriptor is the entity whose ``@id`` is exactly ``ro-crate-metadata.json`` -
    or, for a detached crate, an absolute URI ending in it *and* carrying ``about``. A nested
    crate's descriptor lives at a path like ``saxs/ro-crate-metadata.json`` and is a plain ``File``
    of the enclosing crate, not the enclosing crate's own descriptor.
    """
    at_id = str(entity.get("@id", ""))
    if at_id == "ro-crate-metadata.json" or (
        at_id.endswith("ro-crate-metadata.json") and "about" in entity
    ):
        return "MetadataDescriptor"
    types = entity_types(entity)
    for type_token, class_name in DISPATCH:
        if type_token in types:
            return class_name
    return None


# --------------------------------------------------------------------------------------
# crate discovery
# --------------------------------------------------------------------------------------


def _crates(subdir: str) -> list[Path]:
    return sorted((CRATES / subdir).glob("*.json"))


VALID = _crates("valid")
INVALID = _crates("invalid")
LEGACY = _crates("legacy")


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def graph(crate: dict) -> list[dict]:
    return crate.get("@graph", [])


def root_of(crate: dict) -> dict | None:
    return next((e for e in graph(crate) if classify(e) == "CrateRoot"), None)


# --------------------------------------------------------------------------------------
# graph-level rules
# --------------------------------------------------------------------------------------


def _refs(value) -> list[str]:
    """Every ``@id`` reachable from a property value, however it is nested."""
    if isinstance(value, dict):
        if "@id" in value and len(value) == 1:
            return [value["@id"]]
        return [r for v in value.values() for r in _refs(v)]
    if isinstance(value, list):
        return [r for v in value for r in _refs(v)]
    return []


def compact_keys(entity: dict) -> dict:
    """Strip a profile prefix from any key whose bare form is not already present.

    The per-entity layer compacts against the class schema, which knows exactly which properties
    exist. The graph rules have no class in hand, so they compact by prefix alone - enough, because
    they only read a handful of well-known terms. Without this a crate writing ``lambdax:missing``
    would look as though it declared nothing, which is precisely backwards.
    """
    out = {}
    for key, value in entity.items():
        bare = next((key[len(p):] for p in ("lambda:", "lambdarc:", "lambdax:")
                     if key.startswith(p)), None)
        out[bare if (bare and bare not in entity) else key] = value
    return out


def graph_rule_violations(crate: dict) -> list[str]:
    """Cross-entity conformance rules. Returns a list of human-readable violations."""
    problems: list[str] = []
    entities = [compact_keys(e) for e in graph(crate)]
    ids = {e.get("@id") for e in entities}

    descriptor = next(
        (e for e in entities if str(e.get("@id", "")).endswith("ro-crate-metadata.json")), None
    )
    if descriptor is None:
        problems.append("no metadata descriptor entity")
    else:
        for target in _refs(descriptor.get("about")):
            if target not in ids:
                problems.append(f"descriptor is about {target!r}, which is not in the graph")

    root = root_of({"@graph": entities})
    if root is None:
        problems.append("no root data entity typed lambda:Dataset")

    # every promised part must actually be described
    for entity in entities:
        for target in _refs(entity.get("hasPart")):
            if target not in ids:
                problems.append(
                    f"{entity.get('@id')!r} hasPart {target!r}, which has no entity in the graph"
                )

    # a dataset part must say where its fuller metadata lives, or declare that it has none
    for entity in entities:
        if classify(entity) != "CrateDatasetPart":
            continue
        nested = any(str(t).endswith("ro-crate-metadata.json") for t in _refs(entity.get("hasPart")))
        mechanisms = [
            bool(entity.get("conformsTo")) and nested,
            bool(entity.get("schemaRecord")),
            bool(entity.get("identifier")) and bool(entity.get("url")),
        ]
        if not any(mechanisms) and not entity.get("missing"):
            problems.append(
                f"{entity.get('@id')!r} is a dataset part with no metadata pointer "
                "and no declared absence"
            )

    # file entities must carry RO-Crate's own type token
    for entity in entities:
        types = entity_types(entity)
        if "DataFile" in types and "File" not in types:
            problems.append(
                f"{entity.get('@id')!r} is typed 'DataFile', which is not an RO-Crate term and "
                "resolves to nothing; use 'File'"
            )

    # newly-optional root fields must still be declared when absent
    root_entity = root
    if root_entity is not None:
        declared = {d.get("field") for d in (root_entity.get("missing") or [])}
        for field in ("license", "datePublished"):
            if field not in root_entity and field not in declared:
                problems.append(
                    f"root omits {field!r} without declaring it in missing - "
                    "absence is stated, never implied"
                )

    # an absence blocks a tier unless it genuinely does not apply
    for entity in entities:
        for declaration in entity.get("missing", []) or []:
            if declaration.get("reason") != "not-applicable" and not declaration.get("blocks"):
                problems.append(
                    f"{entity.get('@id')!r} declares {declaration.get('field')!r} missing "
                    "without saying which tier it blocks"
                )

    # a field cannot be both present and declared absent
    for entity in entities:
        for declaration in entity.get("missing", []) or []:
            field = declaration.get("field")
            if field in entity:
                problems.append(
                    f"{entity.get('@id')!r} declares {field!r} missing while also carrying it"
                )

    return problems


# --------------------------------------------------------------------------------------
# layer 1 - document shape
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("path", VALID + LEGACY, ids=lambda p: p.name)
def test_document_shape(json_schema, path):
    """Every crate, including the legacy one, is a well-formed RO-Crate metadata document."""
    errors = _errors(jsonschema.Draft201909Validator(json_schema), load(path))
    assert not errors, f"{path.name} is not a valid crate document:\n" + "\n".join(errors)


GENERATED_SCHEMA = REPO / "assets" / "rocrate" / "jsonschema" / "lambda_rocrate_core.schema.json"


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_generated_artifact_agrees(path):
    """The *shipped* JSON Schema accepts the fixtures, not just one built on the fly.

    Guards the ``gen-rocrate`` step: gen-project roots the JSON Schema at the imported schema's
    ``tree_root``, so if the ``--top-class`` regeneration is ever dropped from the Makefile the
    published artifact would silently describe ``Dataset`` instead of a crate.
    """
    if not GENERATED_SCHEMA.exists():
        pytest.skip("run `make gen-rocrate` first")
    schema = json.loads(GENERATED_SCHEMA.read_text())
    assert list(schema["properties"]) == ["@context", "@graph"], (
        "the generated schema is not rooted at the crate document - "
        "was gen-json-schema --top-class dropped?"
    )
    errors = _errors(jsonschema.Draft201909Validator(schema), load(path))
    assert not errors, f"{path.name} rejected by the generated artifact:\n" + "\n".join(errors)


# --------------------------------------------------------------------------------------
# layer 2 - per-entity
# --------------------------------------------------------------------------------------


PROFILE_PREFIXES = ("lambda:", "lambdarc:")


def _is_array(prop_schema: dict) -> bool:
    declared = prop_schema.get("type")
    return declared == "array" or (isinstance(declared, list) and "array" in declared)


def normalize(entity: dict, class_schema: dict) -> dict:
    """Put an entity into the form the profile defines validation against.

    Two normalizations, both of them things a JSON-LD processor does and neither of them a
    change of meaning:

    * **Term compaction.** ``"lambda:protein_name"`` and a context-mapped ``"protein_name"``
      expand to the same IRI, so a crate may spell a term either way - and real crates mix the two
      within a single entity. The prefixed spelling is compacted to the profile's own term.
    * **Set expansion.** JSON-LD permits a single value where a set is expected. Any property the
      profile declares as multivalued is wrapped, so ``"instrument": {"@id": "#x"}`` and
      ``"instrument": [{"@id": "#x"}]`` are treated alike.

    The class's own generated schema is the authority for which properties are multivalued, so
    this stays correct as the profile evolves.
    """
    properties = class_schema.get("properties", {})

    compacted: dict = {}
    for key, value in entity.items():
        bare = next(
            (key[len(p):] for p in PROFILE_PREFIXES if key.startswith(p)),
            None,
        )
        target = bare if (bare in properties and bare not in entity) else key
        compacted[target] = value

    expanded = {
        key: [value]
        if (_is_array(properties.get(key, {})) and not isinstance(value, list))
        else value
        for key, value in compacted.items()
    }
    return _expand_types(expanded)


def _expand_types(value):
    """Wrap every bare-string ``@type`` at any depth.

    JSON-LD's shorthand is not a top-level-only rule: a nested PROV agent is as entitled to write
    ``"@type": "prov:SoftwareAgent"`` as a graph entity is. This needs no schema knowledge, because
    ``@type`` is always a set.
    """
    if isinstance(value, dict):
        return {
            k: [v] if (k == "@type" and isinstance(v, str)) else _expand_types(v)
            for k, v in value.items()
        }
    if isinstance(value, list):
        return [_expand_types(v) for v in value]
    return value


def entity_violations(json_schema: dict, crate: dict) -> list[str]:
    problems: list[str] = []
    for raw in graph(crate):
        # classification only reads @type and @id, so a cheap pre-expansion is enough for it
        entity = raw if isinstance(raw.get("@type"), list) else {**raw, "@type": entity_types(raw)}
        class_name = classify(entity)
        if class_name is None:
            problems.append(
                f"{entity.get('@id')!r} has no profile class for @type {entity_types(entity)}"
            )
            continue
        class_schema = json_schema["$defs"][class_name]
        for error in _errors(
            _validator(json_schema, class_name), normalize(entity, class_schema)
        ):
            problems.append(f"{entity.get('@id')!r} as {class_name}: {error}")
    return problems


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_entities_conform(json_schema, path):
    problems = entity_violations(json_schema, load(path))
    assert not problems, f"{path.name} has non-conformant entities:\n" + "\n".join(problems)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_every_entity_is_classifiable(path):
    """A reader must be able to tell what each entity is from its @type alone."""
    unclassified = [e.get("@id") for e in graph(load(path)) if classify(e) is None]
    assert not unclassified, f"{path.name}: unclassifiable entities {unclassified}"


# --------------------------------------------------------------------------------------
# layer 3 - graph rules
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_graph_rules(path):
    problems = graph_rule_violations(load(path))
    assert not problems, f"{path.name} breaks graph rules:\n" + "\n".join(problems)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_root_declares_profile_conformance(path):
    """A crate that does not claim the profile cannot be checked against it."""
    root = root_of(load(path))
    claimed = _refs(root.get("conformsTo"))
    assert any("lambda/profile/core" in c for c in claimed), (
        f"{path.name}: root conformsTo {claimed} names no LAMBDA Core profile"
    )
    assert any("ro/crate" in c for c in claimed), (
        f"{path.name}: root conformsTo {claimed} names no RO-Crate version"
    )


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
    assert all(classify(e) is not None for e in graph(crate)), (
        "some 0.2 entity has no profile class"
    )


#: What stops the published SSRL 0.2 crate from conforming to Core 0.3.0. Each is a real,
#: actionable gap rather than a naming difference - the naming differences are handled by the
#: alias layer and do not appear here. If one of these disappears, this test fails and the
#: entry should be removed.
LEGACY_KNOWN_GAPS = {
    "ssrl-mx-XA_x16-core-0.2.json": [
        "omits 'license' without declaring it",  # not merely absent - absent and unstated
        "'lambda:unitCell'",  # MX quantities as bare properties, not nested in resultSummary
        "no metadata pointer",  # RawUnit and DerivedProduct point nowhere for fuller metadata
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
