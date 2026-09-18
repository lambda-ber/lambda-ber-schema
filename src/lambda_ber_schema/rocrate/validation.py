"""Conformance checking for the LAMBDA Core RO-Crate profile.

Three layers, matching the validation model in ``lambda_rocrate_core.yaml`` and section 12 of the
profile document:

1. **Document shape** - the crate validates against ``ROCrateMetadataDocument``.
2. **Per-entity** - each ``@graph`` entity is dispatched on its ``@type`` and validated against
   the matching profile class. These classes are closed, so an undeclared term fails here. This
   is the layer that actually bites.
3. **Graph rules** - the cross-entity constraints neither JSON Schema nor per-entity validation
   can state, because they are about relationships between entities rather than the shape of any
   one of them. They are plain functions over the parsed graph.

``linkml-validate`` cannot do this job: it iterates a data source as a collection of instances, so
a single JSON object is walked key by key, and ``--legacy-mode`` routes through ``gen-python``,
which cannot represent the ``@``-keyword aliases. Hence this module.

The entry points are :func:`validate_crate` for a parsed document and :func:`validate_path` for a
file or crate directory. Both return a :class:`ValidationReport`. The CLI
(``lambda-ber-schema rocrate validate``) is a thin wrapper over :func:`validate_path`.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from importlib import resources
from pathlib import Path
from typing import Iterable

import jsonschema

DOCUMENT_CLASS = "ROCrateMetadataDocument"

#: The file name RO-Crate reserves for the metadata document.
METADATA_FILE = "ro-crate-metadata.json"

#: Name of the generated JSON Schema, both in ``assets/rocrate/jsonschema/`` and inside the package.
SCHEMA_FILE = "lambda_rocrate_core.schema.json"

LAYERS = ("document", "entity", "graph")

PROFILE_PREFIXES = ("lambda:", "lambdarc:", "lambdax:")

#: RO-Crate's context resolves the bare schema.org terms, so crates rarely write these - but
#: nothing forbids it, and a crate writing "sdo:license" must not read as having omitted a licence.
SCHEMA_ORG_PREFIXES = ("sdo:", "schema:")


# --------------------------------------------------------------------------------------
# schema loading
# --------------------------------------------------------------------------------------


class SchemaNotAvailable(RuntimeError):
    """No usable JSON Schema for the profile could be found or built."""


def packaged_schema_path() -> Path:
    """Where the generated JSON Schema lives inside the installed package.

    ``make gen-rocrate`` copies it here so that a plain install can validate without the
    ``linkml`` generators, which are a development dependency only.
    """
    return Path(str(resources.files("lambda_ber_schema") / "schema" / SCHEMA_FILE))


def profile_yaml_path() -> Path:
    return Path(str(resources.files("lambda_ber_schema") / "schema" / "lambda_rocrate_core.yaml"))


def generate_schema() -> dict:
    """Build the document schema from the LinkML source. Needs ``linkml`` installed.

    This parses and traverses the whole of ``lambda_ber_schema`` through the import, which takes
    seconds. Callers should build once and reuse.
    """
    try:
        from linkml.generators.jsonschemagen import JsonSchemaGenerator
    except ImportError as exc:  # pragma: no cover - depends on the install
        raise SchemaNotAvailable(
            "the packaged JSON Schema is missing and `linkml` is not installed to rebuild it; "
            "run `make gen-rocrate` in a checkout, or pass an explicit schema path"
        ) from exc
    return json.loads(
        JsonSchemaGenerator(str(profile_yaml_path()), top_class=DOCUMENT_CLASS).serialize()
    )


def load_schema(path: str | Path | None = None) -> dict:
    """The JSON Schema for the profile, resolved in order of preference.

    1. ``path``, when given.
    2. The copy shipped inside the package.
    3. Generated on the fly from the YAML, when ``linkml`` is importable.
    """
    if path is not None:
        schema = json.loads(Path(path).read_text(encoding="utf-8"))
    elif packaged_schema_path().exists():
        schema = json.loads(packaged_schema_path().read_text(encoding="utf-8"))
    else:
        schema = generate_schema()
    if set(schema.get("properties", {})) != {"@context", "@graph"}:
        raise SchemaNotAvailable(
            "the JSON Schema is not rooted at the crate document; it must be generated with "
            f"--top-class {DOCUMENT_CLASS}"
        )
    if DOCUMENT_CLASS not in schema.get("$defs", {}):
        raise SchemaNotAvailable(f"{DOCUMENT_CLASS} is not in the JSON Schema's $defs")
    return schema


# --------------------------------------------------------------------------------------
# jsonschema plumbing
# --------------------------------------------------------------------------------------


def _validator(json_schema: dict, class_name: str):
    """A validator for one profile class, reusing the document schema's ``$defs``."""
    if class_name not in json_schema["$defs"]:
        raise SchemaNotAvailable(f"{class_name} is not in the generated schema")
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
    ("lambda:Protein", "ProteinEntity"),
    ("lambda:NucleicAcid", "NucleicAcidEntity"),
    ("lambda:SmallMolecule", "SmallMoleculeEntity"),
    ("lambda:SampleComponentInteraction", "ComponentInteractionEntity"),
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
    # Not an RO-Crate term; the graph rules reject it. Dispatched anyway so that such an entity is
    # still shape-checked as a file and the report names the real defect, rather than degenerating
    # to "unclassifiable entity". An entity that is both wrongly typed and malformed therefore
    # yields both findings - which is the useful outcome, since fixing only the type token would
    # leave the other defect to be discovered on the next round.
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
    if at_id == METADATA_FILE or (at_id.endswith(METADATA_FILE) and "about" in entity):
        return "MetadataDescriptor"
    types = entity_types(entity)
    for type_token, class_name in DISPATCH:
        if type_token in types:
            return class_name
    return None


def graph(crate: dict) -> list[dict]:
    raw = crate.get("@graph", [])
    return [e for e in raw if isinstance(e, dict)] if isinstance(raw, list) else []


def root_of(crate: dict) -> dict | None:
    return next((e for e in graph(crate) if classify(e) == "CrateRoot"), None)


# --------------------------------------------------------------------------------------
# layer 1 - document shape
# --------------------------------------------------------------------------------------


def document_violations(json_schema: dict, crate: dict) -> list[str]:
    """Is this a well-formed RO-Crate metadata document at all?"""
    return _errors(jsonschema.Draft201909Validator(json_schema), crate)


# --------------------------------------------------------------------------------------
# layer 2 - per-entity
# --------------------------------------------------------------------------------------


def _is_array(prop_schema: dict) -> bool:
    declared = prop_schema.get("type")
    return declared == "array" or (isinstance(declared, list) and "array" in declared)


def _class_schema(prop_schema: dict, defs: dict) -> dict:
    """Resolve a property schema to the class it describes, through $ref and anyOf wrapping."""
    if not isinstance(prop_schema, dict):
        return {}
    if "$ref" in prop_schema:
        return defs.get(prop_schema["$ref"].rsplit("/", 1)[-1], {})
    for alternative in prop_schema.get("anyOf", []):
        resolved = _class_schema(alternative, defs)
        if resolved.get("properties"):
            return resolved
    return prop_schema if prop_schema.get("properties") else {}


def normalize(entity: dict, class_schema: dict, defs: dict | None = None) -> dict:
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
    defs = defs if defs is not None else {}

    # Two prefixed spellings of one term (``lambda:x`` and ``lambdax:x``) compact to the same key
    # and the later one wins. Such an entity is malformed either way; layer 2 will report the
    # surviving value if it is wrong, and nothing here tries to guess which one was meant.
    compacted: dict = {}
    for key, value in entity.items():
        bare = next(
            (key[len(p):] for p in PROFILE_PREFIXES + SCHEMA_ORG_PREFIXES if key.startswith(p)),
            None,
        )
        target = bare if (bare in properties and bare not in entity) else key
        compacted[target] = value

    expanded: dict = {}
    for key, value in compacted.items():
        prop = properties.get(key, {})
        if _is_array(prop) and not isinstance(value, list):
            value = [value]
        # recurse into nested value objects: a PROV association buried in a designation is as
        # entitled to JSON-LD's shorthand as a top-level property is, and nothing about the rule
        # says it stops at depth one
        child = _class_schema(prop.get("items", prop) if _is_array(prop) else prop, defs)
        if child.get("properties"):
            if isinstance(value, list):
                value = [normalize(v, child, defs) if isinstance(v, dict) else v for v in value]
            elif isinstance(value, dict):
                value = normalize(value, child, defs)
        expanded[key] = value
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
        class_schema = json_schema["$defs"].get(class_name)
        if class_schema is None:
            raise SchemaNotAvailable(
                f"the JSON Schema defines no {class_name} class, which this checker needs; "
                "it was generated from a different version of the profile than the checker "
                "expects, so regenerate it with `make gen-rocrate` or drop --schema"
            )
        for error in _errors(
            _validator(json_schema, class_name),
            normalize(entity, class_schema, json_schema["$defs"]),
        ):
            problems.append(f"{entity.get('@id')!r} as {class_name}: {error}")
    return problems


# --------------------------------------------------------------------------------------
# layer 3 - graph rules
# --------------------------------------------------------------------------------------


def refs(value) -> list[str]:
    """Every ``@id`` reachable from a property value, however it is nested.

    An ``@id`` counts whether or not it stands alone. An inline reference carrying a label
    alongside its identifier is still a reference, and a dangling one must not pass silently.
    """
    if isinstance(value, dict):
        here = [value["@id"]] if isinstance(value.get("@id"), str) else []
        return here + [r for key, sub in value.items() if key != "@id" for r in refs(sub)]
    if isinstance(value, list):
        return [r for v in value for r in refs(v)]
    return []


#: The JSON keys the graph rules read, per class, spelled as the profile spells them.
#: Hardcoded strings in a rule that only ever *adds* findings fail silently when they drift: rename
#: an alias in the schema and the check keeps passing everything, which reads exactly like success.
#: The test suite checks these against the generated schema so that drift turns into a red test.
GRAPH_RULE_TERMS: dict[str, tuple[str, ...]] = {
    "CrateRoot": ("license", "datePublished", "missing", "hasPart", "conformsTo"),
    "CrateDatasetPart": ("conformsTo", "schemaRecord", "identifier", "url", "hasPart", "missing"),
    "MetadataDescriptor": ("about",),
    "SampleEntity": ("hasBioChemEntityPart",),
    "ProteinEntity": ("uniprot_id", "missing"),
    "NucleicAcidEntity": ("rnacentral_id", "sequence_accession", "nucleotide_sequence", "missing"),
    "SmallMoleculeEntity": ("chebi_id", "pdb_ligand_id", "inChIKey", "smiles", "missing"),
    "ComponentInteractionEntity": ("sample_id", "subject_id", "object_id"),
}

#: What identifies a nucleic acid entity: a registry accession, or the sequence itself.
NUCLEIC_ACID_IDENTITY = ("rnacentral_id", "sequence_accession", "nucleotide_sequence")

#: What identifies a small molecule entity: a registry accession, or the structure itself.
SMALL_MOLECULE_IDENTITY = ("chebi_id", "pdb_ligand_id", "inChIKey", "smiles")

#: Fragments the root's ``conformsTo`` must name (rule 7 in the profile).
PROFILE_CONFORMANCE_FRAGMENT = "lambda/profile/core"
ROCRATE_CONFORMANCE_FRAGMENT = "ro/crate"


def compact_keys(entity: dict) -> dict:
    """Strip a profile prefix from any key whose bare form is not already present.

    The per-entity layer compacts against the class schema, which knows exactly which properties
    exist. The graph rules have no class in hand, so they compact by prefix alone - enough, because
    they only read a handful of well-known terms. Without this a crate writing ``lambdax:missing``
    would look as though it declared nothing, which is precisely backwards.
    """
    out = {}
    for key, value in entity.items():
        bare = next((key[len(p):] for p in PROFILE_PREFIXES + SCHEMA_ORG_PREFIXES
                     if key.startswith(p)), None)
        out[bare if (bare and bare not in entity) else key] = value
    return out


def _missing_declarations(entity: dict) -> list[dict]:
    declared = entity.get("missing") or []
    return [d for d in declared if isinstance(d, dict)] if isinstance(declared, list) else []


def graph_rule_violations(crate: dict) -> list[str]:
    """Cross-entity conformance rules. Returns a list of human-readable violations."""
    problems: list[str] = []
    entities = [compact_keys(e) for e in graph(crate)]
    ids = {e.get("@id") for e in entities}

    descriptor = next(
        (e for e in entities if str(e.get("@id", "")).endswith(METADATA_FILE)), None
    )
    if descriptor is None:
        problems.append("no metadata descriptor entity")
    else:
        for target in refs(descriptor.get("about")):
            if target not in ids:
                problems.append(f"descriptor is about {target!r}, which is not in the graph")

    root = root_of({"@graph": entities})
    if root is None:
        problems.append("no root data entity typed lambda:Dataset")

    # every promised part must actually be described
    for entity in entities:
        for target in refs(entity.get("hasPart")):
            if target not in ids:
                problems.append(
                    f"{entity.get('@id')!r} hasPart {target!r}, which has no entity in the graph"
                )

    # a specimen's proteins must be described, not merely pointed at
    for entity in entities:
        for target in refs(entity.get("hasBioChemEntityPart")):
            if target not in ids:
                problems.append(
                    f"{entity.get('@id')!r} hasBioChemEntityPart {target!r}, "
                    "which has no entity in the graph"
                )

    # a protein without an accession says so
    for entity in entities:
        if classify(entity) != "ProteinEntity":
            continue
        declared = {d.get("field") for d in _missing_declarations(entity)}
        if "uniprot_id" not in entity and "uniprot_id" not in declared:
            problems.append(
                f"{entity.get('@id')!r} is a protein with no uniprot_id and no declared absence - "
                "absence is stated, never implied"
            )

    # a nucleic acid without an accession or a sequence says so
    for entity in entities:
        if classify(entity) != "NucleicAcidEntity":
            continue
        declared = {d.get("field") for d in _missing_declarations(entity)}
        if not any(k in entity or k in declared for k in NUCLEIC_ACID_IDENTITY):
            problems.append(
                f"{entity.get('@id')!r} is a nucleic acid with no rnacentral_id, "
                "sequence_accession or nucleotide_sequence and no declared absence - "
                "absence is stated, never implied"
            )

    # a small molecule without an accession or a structure says so
    for entity in entities:
        if classify(entity) != "SmallMoleculeEntity":
            continue
        declared = {d.get("field") for d in _missing_declarations(entity)}
        if not any(k in entity or k in declared for k in SMALL_MOLECULE_IDENTITY):
            problems.append(
                f"{entity.get('@id')!r} is a small molecule with no chebi_id, pdb_ligand_id, "
                "inChIKey or smiles and no declared absence - absence is stated, never implied"
            )

    # an interaction is between two things its sample actually contains
    by_id = {e.get("@id"): e for e in entities}
    for entity in entities:
        if classify(entity) != "ComponentInteractionEntity":
            continue
        sample_ids = refs(entity.get("sample_id"))
        sample_ref = sample_ids[0] if sample_ids else None
        sample = by_id.get(sample_ref)
        if sample is None or classify(sample) != "SampleEntity":
            problems.append(
                f"{entity.get('@id')!r} is an interaction whose sample_id {sample_ref!r} "
                "is not a sample in the graph"
            )
            continue
        parts = set(refs(sample.get("hasBioChemEntityPart")))
        for key in ("subject_id", "object_id"):
            for target in refs(entity.get(key)):
                if target not in ids:
                    problems.append(
                        f"{entity.get('@id')!r} {key} {target!r}, which has no entity in the graph"
                    )
                elif target not in parts:
                    problems.append(
                        f"{entity.get('@id')!r} {key} {target!r}, which sample "
                        f"{sample.get('@id')!r} does not list in hasBioChemEntityPart"
                    )

    # a dataset part must say where its fuller metadata lives, or declare that it has none
    for entity in entities:
        if classify(entity) != "CrateDatasetPart":
            continue
        nested = any(str(t).endswith(METADATA_FILE) for t in refs(entity.get("hasPart")))
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

    if root is not None:
        # newly-optional root fields must still be declared when absent
        declared = {d.get("field") for d in _missing_declarations(root)}
        for field_name in ("license", "datePublished"):
            if field_name not in root and field_name not in declared:
                problems.append(
                    f"root omits {field_name!r} without declaring it in missing - "
                    "absence is stated, never implied"
                )

        # a crate that does not claim the profile cannot be checked against it
        claimed = refs(root.get("conformsTo"))
        if not any(PROFILE_CONFORMANCE_FRAGMENT in c for c in claimed):
            problems.append(f"root conformsTo {claimed} names no LAMBDA Core profile")
        if not any(ROCRATE_CONFORMANCE_FRAGMENT in c for c in claimed):
            problems.append(f"root conformsTo {claimed} names no RO-Crate version")

    # an absence blocks a tier unless it genuinely does not apply
    for entity in entities:
        for declaration in _missing_declarations(entity):
            if declaration.get("reason") != "not-applicable" and not declaration.get("blocks"):
                problems.append(
                    f"{entity.get('@id')!r} declares {declaration.get('field')!r} missing "
                    "without saying which tier it blocks"
                )

    # a field cannot be both present and declared absent
    for entity in entities:
        for declaration in _missing_declarations(entity):
            field_name = declaration.get("field")
            if field_name in entity:
                problems.append(
                    f"{entity.get('@id')!r} declares {field_name!r} missing while also carrying it"
                )

    return problems


# --------------------------------------------------------------------------------------
# the whole thing
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Finding:
    layer: str
    message: str

    def __str__(self) -> str:
        return f"[{self.layer}] {self.message}"


@dataclass
class ValidationReport:
    source: str
    findings: list[Finding] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.findings

    def by_layer(self, layer: str) -> list[Finding]:
        return [f for f in self.findings if f.layer == layer]

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "conformant": self.ok,
            "findings": [{"layer": f.layer, "message": f.message} for f in self.findings],
        }


def validate_crate(
    crate: dict,
    json_schema: dict | None = None,
    *,
    source: str = "<crate>",
    layers: Iterable[str] = LAYERS,
) -> ValidationReport:
    """Run the requested layers over a parsed ``ro-crate-metadata.json``.

    Layers run independently. A document that fails layer 1 still gets layers 2 and 3, because
    the layer 1 message is often the least specific of the three and a user wants the real
    defect named.
    """
    wanted = set(layers)
    unknown = wanted - set(LAYERS)
    if unknown:
        raise ValueError(f"unknown layers {sorted(unknown)}; choose from {LAYERS}")
    if json_schema is None and wanted & {"document", "entity"}:
        json_schema = load_schema()

    report = ValidationReport(source=source)
    if not isinstance(crate, dict):
        report.findings.append(Finding("document", "the document is not a JSON object"))
        return report
    if "document" in wanted:
        report.findings += [Finding("document", m) for m in document_violations(json_schema, crate)]
    if "entity" in wanted:
        report.findings += [Finding("entity", m) for m in entity_violations(json_schema, crate)]
    if "graph" in wanted:
        report.findings += [Finding("graph", m) for m in graph_rule_violations(crate)]
    return report


def resolve_metadata_path(path: str | Path) -> Path:
    """Accept either the metadata file or the crate directory that holds it."""
    p = Path(path)
    if p.is_dir():
        candidate = p / METADATA_FILE
        if not candidate.exists():
            raise FileNotFoundError(f"{p} is a directory with no {METADATA_FILE} inside it")
        return candidate
    if not p.exists():
        raise FileNotFoundError(f"{p} does not exist")
    return p


def validate_path(
    path: str | Path,
    json_schema: dict | None = None,
    *,
    layers: Iterable[str] = LAYERS,
) -> ValidationReport:
    """Validate a crate on disk. ``path`` may be the metadata file or the crate directory.

    Raises ``OSError`` (``FileNotFoundError``, ``PermissionError``, ...) when the file cannot be
    reached or read: that is a problem with the path, not with the crate. A file that is read
    but is not JSON comes back as a report with one document-layer finding.
    """
    metadata = resolve_metadata_path(path)
    try:
        crate = json.loads(metadata.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        return ValidationReport(
            source=str(metadata),
            findings=[Finding("document", f"not valid JSON: {exc}")],
        )
    return validate_crate(crate, json_schema, source=str(metadata), layers=layers)
