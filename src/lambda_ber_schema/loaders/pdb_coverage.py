"""
Account for every field the RCSB Data API returns.

``pdb_rcsb_fields.json`` lists every leaf field RCSB's JSON schemas allow on the records
the PDB loader fetches; ``pdb_field_map.yaml`` gives each one a disposition. This module
reads both, says which rule governs a field, and reports, for any set of fetched records,
which fields were classified how and whether any were not classified at all.

The loader also uses it: fields marked ``metric`` are emitted generically, as
additional_metrics or additional_properties, by :func:`extra_values`.

Example:
    >>> fmap = field_map()
    >>> fmap.rule("entry", "refine[].ls_R_factor_R_work").disposition
    'to'
    >>> fmap.rule("entry", "refine[].B_iso_max").disposition
    'metric'
    >>> fmap.rule("entry", "pdbx_audit_revision_history[].revision_date").disposition
    'bookkeeping'
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass, field
from functools import lru_cache
from importlib import resources
from typing import Any, Iterator

import yaml

#: The dispositions a rule may give, in the order a report lists them.
DISPOSITIONS = (
    "to",
    "metric",
    "derived",
    "reference",
    "linked_file",
    "join",
    "bookkeeping",
    "out_of_scope",
)

#: Kinds of RCSB record, as named in both data files.
KINDS = (
    "entry",
    "polymer_entity",
    "nonpolymer_entity",
    "branched_entity",
    "chemcomp",
    "assembly",
    "interface",
)

#: Leading path components that are RCSB's own derived categories rather than mmCIF categories.
_RCSB_PREFIXES = ("rcsb_", "ma_", "ihm_")


@dataclass(frozen=True)
class Rule:
    """The rule in the field map that governs one field."""

    kind: str
    key: str
    disposition: str
    target: str
    transformed: str | None = None


@dataclass
class FieldMap:
    """The field map, indexed for longest-prefix lookup."""

    rules: dict[str, dict[str, Rule]]

    def rule(self, kind: str, path: str) -> Rule | None:
        """
        The rule for a field: the longest key that is the path or a prefix of it.

        A key is a prefix of a path when the path continues it with "." or "[]".
        """
        kind_rules = self.rules.get(kind, {})
        candidate = path
        while True:
            if candidate in kind_rules:
                return kind_rules[candidate]
            cut = max(candidate.rfind("."), candidate.rfind("[]"))
            if cut <= 0:
                return None
            candidate = candidate[:cut]


@lru_cache(maxsize=1)
def field_map() -> FieldMap:
    """Load pdb_field_map.yaml."""
    text = resources.files("lambda_ber_schema.loaders").joinpath("pdb_field_map.yaml").read_text()
    raw = yaml.safe_load(text)
    rules: dict[str, dict[str, Rule]] = {}
    for kind, entries in raw.items():
        if kind not in KINDS:
            raise ValueError(f"pdb_field_map.yaml: unknown record kind {kind!r}")
        kind_rules: dict[str, Rule] = {}
        for key, body in entries.items():
            dispositions = [d for d in DISPOSITIONS if d in body]
            if len(dispositions) != 1:
                raise ValueError(
                    f"pdb_field_map.yaml: {kind}.{key} needs exactly one of {DISPOSITIONS}"
                )
            extra = set(body) - set(DISPOSITIONS) - {"as"}
            if extra or ("as" in body and dispositions[0] != "to"):
                raise ValueError(f"pdb_field_map.yaml: {kind}.{key} has unexpected keys {extra}")
            disposition = dispositions[0]
            kind_rules[key] = Rule(
                kind=kind,
                key=key,
                disposition=disposition,
                target=str(body[disposition]),
                transformed=body.get("as"),
            )
        rules[kind] = kind_rules
    return FieldMap(rules=rules)


@lru_cache(maxsize=1)
def rcsb_fields() -> dict[str, dict[str, dict[str, str]]]:
    """Every leaf field RCSB's schemas allow, by kind, with its JSON type and RCSB unit."""
    text = resources.files("lambda_ber_schema.loaders").joinpath("pdb_rcsb_fields.json").read_text()
    return json.loads(text)["kinds"]


def leaf_values(record: Any, prefix: str = "") -> Iterator[tuple[str, Any]]:
    """
    Walk a record to its scalar leaves, yielding (path, value) with "[]" marking list steps.

    Example:
        >>> list(leaf_values({"a": [{"b": 1}, {"b": 2}], "c": "x"}))
        [('a[].b', 1), ('a[].b', 2), ('c', 'x')]
    """
    if isinstance(record, dict):
        for key, value in record.items():
            yield from leaf_values(value, f"{prefix}.{key}" if prefix else key)
    elif isinstance(record, list):
        for value in record:
            yield from leaf_values(value, f"{prefix}[]")
    elif record is not None:
        yield prefix, record


def attribute_id(path: str) -> str:
    """
    The CURIE naming a source field: an mmCIF item where the field is one, else an RCSB attribute.

    Example:
        >>> attribute_id("refine[].B_iso_max")
        'mmCIF:_refine.B_iso_max'
        >>> attribute_id("rcsb_polymer_entity_name_com[].name")
        'rcsb:rcsb_polymer_entity_name_com.name'
    """
    plain = path.replace("[]", "")
    category, _, item = plain.partition(".")
    if category.startswith(_RCSB_PREFIXES) or not item:
        return f"rcsb:{plain}"
    return f"mmCIF:_{category}.{item}"


#: RCSB's unit names, as the schema's QuantityValue writes units elsewhere in this project.
RCSB_UNITS = {
    "angstroms": "Angstroms",
    "angstroms_squared": "Angstroms^2",
    "angstroms_cubed": "Angstroms^3",
    "angstroms_cubed_per_dalton": "Angstroms^3/Da",
    "degrees": "degrees",
    "kelvins": "K",
    "kilovolts": "kV",
    "millimetres": "mm",
    "microns": "micrometers",
    "nanometres": "nanometers",
    "seconds": "s",
    "electrons_angstrom_squared": "e-/Angstrom^2",
    "milliradians": "mrad",
    "megahertz": "MHz",
    "kilodaltons": "kDa",
    "daltons": "Da",
    "percent": "percent",
}


def unit_for(kind: str, path: str) -> str:
    """
    The unit RCSB's schema gives a field, in this project's spelling.

    RCSB leaves many fields without a unit, counts and ratios but also some lengths, so a
    missing unit is written 'unspecified' rather than guessed.
    """
    spec = rcsb_fields().get(kind, {}).get(path, {})
    unit = spec.get("units")
    if not unit:
        return "unspecified"
    return RCSB_UNITS.get(unit, unit)


def extra_values(kind: str, record: dict[str, Any], prefix: str) -> tuple[list[dict], list[dict]]:
    """
    The fields of one record that the field map marks ``metric``, ready for the schema.

    ``record`` is one row of the category at ``prefix`` (a path such as ``refine[]`` or
    ``pdbx_vrpt_summary``). Numbers come back as QuantityValue dicts, everything else as
    TextValue dicts, each with an attribute naming its source item. Lists of scalars are
    joined with ", " so a wavelength list stays one value.

    Example:
        >>> metrics, props = extra_values("entry", {"B_iso_max": 80.5, "details": "x"}, "refine[]")
        >>> metrics[0]["numeric_value"], metrics[0]["unit"], metrics[0]["attribute"]["id"]
        (80.5, 'Angstroms^2', 'mmCIF:_refine.B_iso_max')
        >>> props
        []
    """
    fmap = field_map()
    metrics: list[dict] = []
    properties: list[dict] = []
    grouped: dict[str, list[Any]] = {}
    for sub_path, value in leaf_values(record):
        grouped.setdefault(sub_path, []).append(value)
    for sub_path, values in grouped.items():
        path = f"{prefix}.{sub_path}" if prefix else sub_path
        rule = fmap.rule(kind, path)
        if rule is None or rule.disposition != "metric":
            continue
        attribute = {"id": attribute_id(path), "label": path.replace("[]", "")}
        numbers = [v for v in values if isinstance(v, (int, float)) and not isinstance(v, bool)]
        if len(values) == 1 and len(numbers) == 1:
            metrics.append(
                {"attribute": attribute, "numeric_value": numbers[0], "unit": unit_for(kind, path)}
            )
        else:
            text = ", ".join(str(v) for v in values)
            properties.append({"attribute": attribute, "value": text})
    return metrics, properties


@dataclass
class CoverageReport:
    """How the fields present in some fetched records were classified."""

    counts: Counter = field(default_factory=Counter)
    unclassified: dict[str, set[str]] = field(default_factory=dict)

    @property
    def complete(self) -> bool:
        return not self.unclassified


def coverage(records: dict[str, list[dict[str, Any]]]) -> CoverageReport:
    """
    Classify every field present in a set of records, by kind.

    ``records`` maps a kind to the records of that kind, as the loader's
    ``LoaderResult.raw_data`` holds them.
    """
    fmap = field_map()
    report = CoverageReport()
    for kind, kind_records in records.items():
        seen: set[str] = set()
        for record in kind_records:
            for path, _ in leaf_values(record):
                seen.add(path)
        for path in seen:
            rule = fmap.rule(kind, path)
            if rule is None:
                report.unclassified.setdefault(kind, set()).add(path)
            else:
                report.counts[rule.disposition] += 1
    return report


def universe_report() -> CoverageReport:
    """Classify every field RCSB's schemas allow, present in a given entry or not."""
    fmap = field_map()
    report = CoverageReport()
    for kind, fields in rcsb_fields().items():
        for path in fields:
            rule = fmap.rule(kind, path)
            if rule is None:
                report.unclassified.setdefault(kind, set()).add(path)
            else:
                report.counts[rule.disposition] += 1
    return report
