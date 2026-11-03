#!/usr/bin/env python3
"""
Report join-key coverage and integrity for lakehouse databases written by
ingest_to_lakehouse.py, and compare them with the databases they would replace.

Read-only: runs SELECT and SHOW statements. Writes {out_dir}/coverage.json and
{out_dir}/coverage.md.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PDB_ENTRIES = "kescience.pdb.pdb_entries"
PDB_UNIPROT_MAPPING = "kescience.pdb.pdb_uniprot_mapping"

# (association table, its column, referenced table)
ASSOCIATION_REFERENCES = (
    ("sample_protein_associations", "sample_id", "samples"),
    ("sample_protein_associations", "protein_id", "proteins"),
    ("experiment_instrument_associations", "experiment_id", "experiment_runs"),
    ("experiment_instrument_associations", "instrument_id", "instruments"),
    ("experiment_sample_associations", "sample_id", "samples"),
    ("study_sample_associations", "sample_id", "samples"),
)

# (shared table, association table, its column pointing at the shared table)
SHARED_REFERENCES = (
    ("proteins", "sample_protein_associations", "protein_id"),
    ("instruments", "experiment_instrument_associations", "instrument_id"),
    ("nucleic_acids", "sample_nucleic_acid_associations", "nucleic_acid_id"),
)


def _scalar(spark, sql: str) -> int:
    return spark.sql(sql).collect()[0][0] or 0


def _table_counts(spark, namespace: str) -> dict[str, int]:
    tables = sorted(r["tableName"] for r in spark.sql(f"SHOW TABLES IN {namespace}").collect())
    return {t: _scalar(spark, f"SELECT COUNT(*) FROM {namespace}.{t}") for t in tables}


def _fraction(part: int, whole: int) -> float | None:
    return round(part / whole, 4) if whole else None


def protein_coverage(spark, ns: str, tables: dict[str, int]) -> dict:
    """Coverage of samples and proteins by UniProt CURIEs and by kescience.pdb."""
    samples = tables.get("samples", 0)
    result = {"samples": samples, "proteins": tables.get("proteins", 0)}
    if "proteins" not in tables or "sample_protein_associations" not in tables:
        result.update(samples_with_uniprot_protein=0, samples_with_uniprot_protein_fraction=_fraction(0, samples))
        return result

    uniprot = f"(SELECT id, regexp_replace(id, '^uniprot:', '') AS acc FROM {ns}.proteins WHERE id LIKE 'uniprot:%')"
    mapped = f"(SELECT DISTINCT uniprot_accession AS acc FROM {PDB_UNIPROT_MAPPING})"
    linked = _scalar(spark, f"""
        SELECT COUNT(DISTINCT a.sample_id) FROM {ns}.sample_protein_associations a
        JOIN {uniprot} p ON a.protein_id = p.id""")
    linked_pdb = _scalar(spark, f"""
        SELECT COUNT(DISTINCT a.sample_id) FROM {ns}.sample_protein_associations a
        JOIN {uniprot} p ON a.protein_id = p.id JOIN {mapped} m ON p.acc = m.acc""")
    curies = _scalar(spark, f"SELECT COUNT(*) FROM {uniprot}")
    curies_pdb = _scalar(spark, f"SELECT COUNT(*) FROM {uniprot} p JOIN {mapped} m ON p.acc = m.acc")
    result.update(
        samples_with_uniprot_protein=linked,
        samples_with_uniprot_protein_fraction=_fraction(linked, samples),
        samples_with_uniprot_protein_in_pdb_mapping=linked_pdb,
        samples_with_uniprot_protein_in_pdb_mapping_fraction=_fraction(linked_pdb, samples),
        proteins_with_uniprot_curie=curies,
        proteins_with_uniprot_curie_in_pdb_mapping=curies_pdb,
        proteins_with_uniprot_curie_in_pdb_mapping_fraction=_fraction(curies_pdb, curies),
    )
    return result


def cross_reference_coverage(spark, ns: str, tables: dict[str, int]) -> dict:
    """Count samples.database_cross_references by database and how many resolve."""
    if "samples" not in tables:
        return {}
    columns = spark.table(f"{ns}.samples").columns
    if "database_cross_references" not in columns:
        return {"total": 0, "by_database": {}}

    xrefs = f"""(SELECT lower(x.database_name) AS db, x.database_id AS acc FROM (
        SELECT explode(from_json(database_cross_references,
            'array<struct<database_name:string,database_id:string>>')) AS x
        FROM {ns}.samples WHERE database_cross_references IS NOT NULL))"""
    by_database = {
        r["db"]: r["n"]
        for r in spark.sql(f"SELECT db, COUNT(*) AS n FROM {xrefs} GROUP BY db").collect()
    }
    result = {"total": sum(by_database.values()), "by_database": by_database}
    if "proteins" in tables:
        result["uniprot_in_proteins_table"] = _scalar(spark, f"""
            SELECT COUNT(*) FROM {xrefs} x JOIN {ns}.proteins p
            ON concat('uniprot:', x.acc) = p.id WHERE x.db = 'uniprot'""")
    result["uniprot_in_pdb_mapping"] = _scalar(spark, f"""
        SELECT COUNT(*) FROM {xrefs} x JOIN
        (SELECT DISTINCT uniprot_accession AS acc FROM {PDB_UNIPROT_MAPPING}) m
        ON x.acc = m.acc WHERE x.db = 'uniprot'""")
    result["pdb_in_pdb_entries"] = _scalar(spark, f"""
        SELECT COUNT(*) FROM {xrefs} x JOIN {PDB_ENTRIES} e
        ON upper(x.acc) = upper(e.pdb_id) WHERE x.db IN ('pdb', 'wwpdb', 'rcsb')""")
    return result


def integrity(spark, ns: str, tables: dict[str, int]) -> dict:
    """Dangling association values, shared rows nothing refers to, and repeated ids."""
    dangling = {}
    for assoc, column, target in ASSOCIATION_REFERENCES:
        if assoc in tables and target in tables:
            dangling[f"{assoc}.{column}->{target}"] = _scalar(spark, f"""
                SELECT COUNT(*) FROM {ns}.{assoc} a LEFT ANTI JOIN {ns}.{target} t
                ON a.{column} = t.id""")
    unreferenced = {}
    for shared, assoc, column in SHARED_REFERENCES:
        if shared in tables:
            if assoc not in tables:
                unreferenced[shared] = tables[shared]
                continue
            unreferenced[shared] = _scalar(spark, f"""
                SELECT COUNT(*) FROM {ns}.{shared} s LEFT ANTI JOIN {ns}.{assoc} a
                ON s.id = a.{column}""")
    repeated = {
        t: _scalar(spark, f"SELECT COUNT(*) - COUNT(DISTINCT id) FROM {ns}.{t}")
        for t in ("instruments", "proteins", "nucleic_acids", "small_molecules", "persons", "organizations")
        if t in tables
    }
    return {"dangling": dangling, "unreferenced_shared_rows": unreferenced, "repeated_ids": repeated}


def compare_entries(spark, current: str, new: str) -> dict:
    """Compare the entries behind samples in the current and new databases."""
    query = "SELECT DISTINCT source_entry_id AS e FROM {}.samples"
    old, fresh = query.format(current), query.format(new)
    return {
        "entries_current": _scalar(spark, f"SELECT COUNT(*) FROM ({old})"),
        "entries_new": _scalar(spark, f"SELECT COUNT(*) FROM ({fresh})"),
        "entries_only_in_current": sorted(
            r["e"] for r in spark.sql(f"SELECT e FROM ({old}) EXCEPT SELECT e FROM ({fresh})").collect()
        ),
        "entries_only_in_new": _scalar(spark, f"SELECT COUNT(*) FROM (SELECT e FROM ({fresh}) EXCEPT SELECT e FROM ({old}))"),
    }


def report_database(spark, tenant: str, dataset: str, suffix: str) -> dict:
    current, new = f"{tenant}.{dataset}", f"{tenant}.{dataset}{suffix}"
    current_tables = _table_counts(spark, current)
    new_tables = _table_counts(spark, new)
    return {
        "current": current,
        "new": new,
        "tables": {
            t: {"current": current_tables.get(t), "new": new_tables.get(t)}
            for t in sorted(current_tables.keys() | new_tables.keys())
        },
        "entries": compare_entries(spark, current, new),
        "proteins": protein_coverage(spark, new, new_tables),
        "cross_references": cross_reference_coverage(spark, new, new_tables),
        "integrity": integrity(spark, new, new_tables),
    }


def render_markdown(results: dict[str, dict]) -> str:
    lines = ["# Join-key coverage", ""]
    lines += [
        "| Database | Samples | With UniProt-linked protein | ...also in `pdb_uniprot_mapping` | Proteins | UniProt CURIEs |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for r in results.values():
        p = r["proteins"]
        lines.append(
            f"| `{r['new']}` | {p['samples']} "
            f"| {p['samples_with_uniprot_protein']} ({p['samples_with_uniprot_protein_fraction']}) "
            f"| {p.get('samples_with_uniprot_protein_in_pdb_mapping', 0)} "
            f"({p.get('samples_with_uniprot_protein_in_pdb_mapping_fraction')}) "
            f"| {p['proteins']} | {p.get('proteins_with_uniprot_curie', 0)} |"
        )
    lines += [
        "",
        "| Database | Cross-references | UniProt | ...in proteins table | ...in `pdb_uniprot_mapping` | PDB in `pdb_entries` |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for r in results.values():
        x = r["cross_references"]
        lines.append(
            f"| `{r['new']}` | {x.get('total', 0)} | {x.get('by_database', {}).get('uniprot', 0)} "
            f"| {x.get('uniprot_in_proteins_table', 0)} | {x.get('uniprot_in_pdb_mapping', 0)} "
            f"| {x.get('pdb_in_pdb_entries', 0)} |"
        )
    for r in results.values():
        lines += ["", f"## `{r['new']}` compared with `{r['current']}`", ""]
        lines += ["| Table | Current | New |", "|---|---:|---:|"]
        lines += [f"| {t} | {c['current']} | {c['new']} |" for t, c in r["tables"].items()]
        e = r["entries"]
        lines += [
            "",
            f"Entries: {e['entries_current']} current, {e['entries_new']} new, "
            f"{e['entries_only_in_new']} only in new, "
            f"{len(e['entries_only_in_current'])} only in current {e['entries_only_in_current'][:20]}.",
            "",
            f"Integrity: {json.dumps(r['integrity'])}",
        ]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--datasets", required=True, help="Comma-separated current database names")
    p.add_argument("--suffix", required=True, help="Suffix of the new databases, e.g. _202611")
    p.add_argument("--tenant", default="lambda")
    p.add_argument("--out-dir", type=Path, required=True)
    args = p.parse_args(argv)

    from berdl_notebook_utils.setup_spark_session import get_spark_session

    spark = get_spark_session()
    results = {
        d: report_database(spark, args.tenant, d, args.suffix)
        for d in args.datasets.split(",")
    }
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "coverage.json").write_text(json.dumps(results, indent=2))
    markdown = render_markdown(results)
    (args.out_dir / "coverage.md").write_text(markdown)
    print(markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
