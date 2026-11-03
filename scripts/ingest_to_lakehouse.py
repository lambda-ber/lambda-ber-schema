#!/usr/bin/env python3
"""
Dump SASBDB and SimpleScattering entries, convert to per-entity-class Parquet,
and upload to the lakehouse object store.

Pipeline phases (each can be skipped independently):
  1. dump     - run `lambda-ber-schema etl dump-{source}` to populate {dump_dir}/*.yaml
  2. convert  - parse YAMLs into one Parquet per entity class in {staging_dir}
  3. upload   - push every Parquet (and the generated ingest config) to MinIO
  4. ingest   - optional: invoke data_lakehouse_ingest.ingest() against the config

Output object layout:
  s3a://{bucket}/tenant-general-warehouse/{tenant}/datasets/{source}/{slot}.parquet
  s3a://{bucket}/tenant-general-warehouse/{tenant}/datasets/{source}/{source}_ingest_config.json
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import subprocess
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
import pyarrow.parquet as pq
import yaml

LOG = logging.getLogger("ingest_to_lakehouse")

REPO_ROOT = Path(__file__).resolve().parent.parent
SUPPORTED_SOURCES = ("sasbdb", "simplescattering", "ssrl-mx")

# Normalize source names for use in S3 paths and SQL identifiers (hyphens
# are invalid in Spark/Iceberg database names).
SOURCE_TO_DATASET_NAME: dict[str, str] = {
    "ssrl-mx": "ssrl_mx",
}

SCHEMA_PATH = REPO_ROOT / "src" / "lambda_ber_schema" / "schema" / "lambda_ber_schema.yaml"

# Slot names whose silver-table name must differ from the bronze slot name.
# `data_files` collides with the reserved Iceberg metadata-table name and
# trips Polaris's path resolver (IllegalStateException:
# invalid_path_key_for_passthrough_resolved_path), so we expose it as
# `dataset_files` in the silver catalog. Bronze parquet keeps the slot name.
SLOT_TO_SILVER_NAME: dict[str, str] = {
    "data_files": "dataset_files",
}

# Entities that many entries refer to, so each per-entry YAML carries a copy.
# These collapse to one row per key; every other table stays entry-scoped.
SHARED_ENTITY_SLOTS: tuple[str, ...] = (
    "instruments",
    "proteins",
    "nucleic_acids",
    "small_molecules",
    "persons",
    "organizations",
)

# Key fields tried in order when de-duplicating a shared entity row.
SHARED_ENTITY_KEYS: dict[str, tuple[str, ...]] = {
    "instruments": ("id", "instrument_code"),
}

# Protein fields a source may record per entry (mutants and constructs share a
# UniProt ID). Each is copied to sample_protein_associations as entry_{field}, and
# the shared row takes the most common values. Fields in a group stay paired.
PROTEIN_DETAIL_FIELDS: tuple[str, ...] = (
    "protein_name",
    "organism_name",
    "amino_acid_sequence",
    "sequence_length",
)
MOST_COMMON_FIELD_GROUPS: dict[str, tuple[tuple[str, ...], ...]] = {
    "proteins": (
        ("protein_name", "title"),
        ("organism_name",),
        ("amino_acid_sequence", "sequence_length"),
    ),
}


@lru_cache(maxsize=1)
def get_entity_slots() -> tuple[str, ...]:
    """Return every multivalued, class-ranged `Dataset` slot, in schema order.

    Each one aggregates to one Parquet. Needs linkml_runtime, so run the convert
    phase under `uv run`; upload and ingest can reuse its output with --skip-convert.
    """
    from linkml_runtime import SchemaView

    view = SchemaView(str(SCHEMA_PATH))
    classes = view.all_classes()
    return tuple(
        slot.name
        for slot in view.class_induced_slots("Dataset")
        if slot.multivalued and slot.range in classes
    )


# ---------------------------------------------------------------------------
# Phase 1: dump
# ---------------------------------------------------------------------------

def run_dump(source: str, dump_dir: Path, rate: float, workers: int,
             limit: int | None, allow_failures: bool) -> None:
    """Invoke the lambda-ber-schema dump CLI for `source` and block until done."""
    dump_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "uv", "run", "lambda-ber-schema", "etl", f"dump-{source}",
        "--output-dir", str(dump_dir),
        "--rate", str(rate),
        "--workers", str(workers),
    ]
    if limit is not None:
        cmd.extend(["--limit", str(limit)])

    LOG.info("Running dump: %s", " ".join(cmd))
    result = subprocess.run(cmd, cwd=REPO_ROOT, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"dump-{source} exited with {result.returncode}")

    progress_path = dump_dir / "progress.json"
    if progress_path.exists():
        progress = json.loads(progress_path.read_text())
        completed = len(progress.get("completed", []))
        failed = progress.get("failed", {}) or {}
        LOG.info("Dump complete: completed=%d failed=%d", completed, len(failed))
        if failed and not allow_failures:
            sample = list(failed.items())[:3]
            raise RuntimeError(
                f"{len(failed)} entries failed (e.g. {sample}); "
                "rerun with --allow-failures to continue."
            )


def run_dump_ssrl_mx(
    snapshots_dir: Path,
    dump_dir: Path,
    limit: int | None,
    metadata_file: Path | None,
    processing_file: Path | None,
) -> None:
    """Invoke dump-ssrl-mx (filesystem-only, no rate limiting).

    Unlike the HTTP-based sources, SSRL MX is a pure filesystem ETL: the
    CLI reads snapshot JSON files from ``snapshots_dir`` and writes converted
    Dataset YAMLs to ``dump_dir``. No network, no rate limiting.
    """
    snapshots = sorted(snapshots_dir.glob("*.json"))
    snapshot_count = len(snapshots)
    if limit is not None:
        snapshot_count = min(snapshot_count, limit)
    LOG.info(
        "SSRL MX dump: %d snapshot(s) from %s (metadata=%s, processing=%s)",
        snapshot_count, snapshots_dir,
        metadata_file or "none", processing_file or "none",
    )

    dump_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "uv", "run", "lambda-ber-schema", "etl", "dump-ssrl-mx",
        "--snapshots-dir", str(snapshots_dir),
        "--output-dir", str(dump_dir),
    ]
    if metadata_file is not None:
        cmd.extend(["--metadata", str(metadata_file)])
    if processing_file is not None:
        cmd.extend(["--processing", str(processing_file)])
    if limit is not None:
        cmd.extend(["--limit", str(limit)])

    LOG.info("Running dump: %s", " ".join(cmd))
    result = subprocess.run(cmd, cwd=REPO_ROOT, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"dump-ssrl-mx exited with {result.returncode}")

    output_count = len(list(dump_dir.glob("*.yaml")))
    LOG.info("Dump complete: %d YAML file(s) in %s", output_count, dump_dir)


# ---------------------------------------------------------------------------
# Phase 2: YAML -> Parquet
# ---------------------------------------------------------------------------

def _flatten_value(value: Any) -> Any:
    """Return a Parquet-friendly scalar or a JSON string for nested types."""
    if isinstance(value, (dict, list)):
        return json.dumps(value, default=str, sort_keys=True)
    return value


def _flatten_row(row: dict, source_entry_id: str | None) -> dict:
    flat = {"source_entry_id": source_entry_id}
    for key, val in row.items():
        flat[key] = _flatten_value(val)
    return flat


def _iter_yaml_docs(dump_dir: Path) -> Iterable[tuple[Path, dict]]:
    for path in sorted(dump_dir.glob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            LOG.warning("Skipping unparseable YAML %s: %s", path, exc)
            continue
        if not isinstance(doc, dict):
            LOG.warning("Skipping non-mapping YAML %s", path)
            continue
        yield path, doc


def _shared_entity_key(slot: str, row: dict) -> str | None:
    for field in SHARED_ENTITY_KEYS.get(slot, ("id",)):
        if row.get(field) is not None:
            return row[field]
    return None


def copy_protein_details_to_associations(rows_by_slot: dict[str, list[dict]]) -> None:
    """Add each entry's own protein details to its sample_protein_associations rows.

    The entry_* columns are not schema slots. They keep what de-duplicating the
    proteins table would otherwise lose.
    """
    by_entry_and_id = {
        (row.get("source_entry_id"), row.get("id")): row
        for row in rows_by_slot.get("proteins", [])
    }
    for association in rows_by_slot.get("sample_protein_associations", []):
        protein = by_entry_and_id.get(
            (association.get("source_entry_id"), association.get("protein_id")), {}
        )
        for field in PROTEIN_DETAIL_FIELDS:
            if protein.get(field) is not None:
                association[f"entry_{field}"] = protein[field]


def _apply_most_common_values(slot: str, kept: dict, group_rows: list[dict]) -> None:
    """Set each field group on `kept` to its most common values; ties go to the first seen."""
    for fields in MOST_COMMON_FIELD_GROUPS.get(slot, ()):
        values = Counter(
            tuple(row.get(f) for f in fields)
            for row in group_rows
            if any(row.get(f) is not None for f in fields)
        )
        if values:
            kept.update(zip(fields, values.most_common(1)[0][0]))


def dedupe_shared_rows(slot: str, rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Collapse `rows` to one per key, keeping the first seen.

    Slots in MOST_COMMON_FIELD_GROUPS then take the most common values for those fields.

    `source_entry_id` is dropped: a collapsed row belongs to many entries, and the
    association tables lead back to them. Rows sharing a key but differing in any
    other field are returned as conflicts. Rows with no key are kept as they are.

    Returns (deduped_rows, conflicts).
    """
    first_by_key: dict[str, dict] = {}
    rows_by_key: dict[str, list[dict]] = {}
    conflict_by_key: dict[str, dict] = {}
    deduped: list[dict] = []
    for row in rows:
        entry_id = row.get("source_entry_id")
        fields = {k: v for k, v in row.items() if k != "source_entry_id"}
        key = _shared_entity_key(slot, fields)
        if key is None:
            LOG.warning("%s: row from %s has no key; keeping it as is", slot, entry_id)
            deduped.append(fields)
            continue
        rows_by_key.setdefault(key, []).append(fields)
        kept = first_by_key.get(key)
        if kept is None:
            first_by_key[key] = dict(fields)
            deduped.append(first_by_key[key])
            continue
        differing = sorted(
            f for f in kept.keys() | fields.keys() if kept.get(f) != fields.get(f)
        )
        if differing:
            conflict = conflict_by_key.setdefault(
                key, {"slot": slot, "key": key, "fields": {}, "rows": 0}
            )
            conflict["rows"] += 1
            for field in differing:
                values = conflict["fields"].setdefault(field, [kept.get(field)])
                if fields.get(field) not in values:
                    values.append(fields.get(field))
    for key in conflict_by_key:
        _apply_most_common_values(slot, first_by_key[key], rows_by_key[key])
    return deduped, list(conflict_by_key.values())


def convert_yamls_to_parquet(dump_dir: Path, staging_dir: Path) -> list[str]:
    """Aggregate per-entry YAMLs into one Parquet per non-empty entity slot.

    Shared entity slots collapse to one row per key; what that discards is logged
    and written to {staging_dir}/dedupe_conflicts.json.

    Returns the list of slot names that produced a Parquet file.
    """
    staging_dir.mkdir(parents=True, exist_ok=True)
    entity_slots = get_entity_slots()
    rows_by_slot: dict[str, list[dict]] = {slot: [] for slot in entity_slots}

    yaml_count = 0
    for _, doc in _iter_yaml_docs(dump_dir):
        yaml_count += 1
        entry_id = doc.get("id")
        for slot in entity_slots:
            for raw_row in (doc.get(slot) or []):
                if not isinstance(raw_row, dict):
                    continue
                rows_by_slot[slot].append(_flatten_row(raw_row, entry_id))

    LOG.info("Parsed %d YAML files from %s", yaml_count, dump_dir)

    copy_protein_details_to_associations(rows_by_slot)

    all_conflicts: list[dict] = []
    for slot in SHARED_ENTITY_SLOTS:
        before = len(rows_by_slot[slot])
        rows_by_slot[slot], conflicts = dedupe_shared_rows(slot, rows_by_slot[slot])
        all_conflicts.extend(conflicts)
        if before:
            LOG.info("De-duplicated %s: %d -> %d rows, %d key(s) with conflicts",
                     slot, before, len(rows_by_slot[slot]), len(conflicts))
        for conflict in conflicts[:5]:
            LOG.warning("%s %s: collapsed to one row; %d row(s) differ in %s",
                        slot, conflict["key"], conflict["rows"], sorted(conflict["fields"]))
    (staging_dir / "dedupe_conflicts.json").write_text(json.dumps(all_conflicts, indent=2))

    written: list[str] = []
    for slot, rows in rows_by_slot.items():
        if not rows:
            continue
        df = pd.DataFrame.from_records(rows)
        out_path = staging_dir / f"{slot}.parquet"
        df.to_parquet(out_path, index=False)
        written.append(slot)
        LOG.info("Wrote %s (%d rows, %d cols)", out_path.name, len(df), len(df.columns))

    return written


# ---------------------------------------------------------------------------
# Phase 2b: ingest-config generation
# ---------------------------------------------------------------------------

def _arrow_type_to_sql(arrow_type) -> str:
    """Map a pyarrow type to the SQL types data_lakehouse_ingest expects."""
    import pyarrow as pa

    if pa.types.is_int32(arrow_type) or pa.types.is_int16(arrow_type) or pa.types.is_int8(arrow_type):
        return "INT"
    if pa.types.is_int64(arrow_type) or pa.types.is_uint32(arrow_type) or pa.types.is_uint64(arrow_type):
        return "BIGINT"
    if pa.types.is_floating(arrow_type):
        return "DOUBLE" if pa.types.is_float64(arrow_type) else "FLOAT"
    if pa.types.is_boolean(arrow_type):
        return "BOOLEAN"
    if pa.types.is_timestamp(arrow_type):
        return "TIMESTAMP"
    if pa.types.is_date(arrow_type):
        return "DATE"
    return "STRING"


def _parquet_schema_to_sql(parquet_path: Path) -> str:
    schema = pq.read_schema(parquet_path)
    return ", ".join(f"{f.name} {_arrow_type_to_sql(f.type)}" for f in schema)


def build_ingest_config(
    source: str,
    tenant: str,
    bucket: str,
    staging_dir: Path,
    slots: list[str],
    dataset_suffix: str = "",
) -> dict:
    dataset_name = target_dataset_name(source, dataset_suffix)
    bronze_base = f"s3a://{bucket}/tenant-general-warehouse/{tenant}/datasets/{dataset_name}/"
    return {
        "tenant": tenant,
        "dataset": dataset_name,
        "paths": {
            "data_plane": f"s3a://{bucket}/tenant-general-warehouse/{tenant}/",
            "bronze_base": bronze_base,
            "silver_base": f"s3a://{bucket}/tenant-sql-warehouse/{tenant}/{tenant}_{dataset_name}.db",
        },
        "defaults": {"parquet": {"inferSchema": False}},
        "tables": [
            {
                "name": SLOT_TO_SILVER_NAME.get(slot, slot),
                "enabled": True,
                "partition_by": None,
                "mode": "overwrite",
                "schema_sql": _parquet_schema_to_sql(staging_dir / f"{slot}.parquet"),
                "bronze_path": f"{bronze_base}{slot}.parquet",
            }
            for slot in slots
        ],
    }


def write_ingest_config(config: dict, staging_dir: Path, source: str) -> Path:
    path = staging_dir / f"{source}_ingest_config.json"
    path.write_text(json.dumps(config, indent=2))
    LOG.info("Wrote ingest config: %s", path)
    return path


# ---------------------------------------------------------------------------
# Phase 3: upload to MinIO
# ---------------------------------------------------------------------------

def get_minio_client():
    """Get a MinIO/S3 client via BERDL helpers (credentials handled internally)."""
    from berdl_notebook_utils.clients import get_minio_client as _berdl_minio_client
    client = _berdl_minio_client()
    LOG.info("MinIO client ready")
    return client


def ensure_target_is_new(
    minio_client,
    spark,
    bucket: str,
    tenant: str,
    dataset_name: str,
) -> None:
    """Refuse to overwrite an existing load: bronze objects or silver tables.

    Pass None for a client whose side of the target this run does not write.
    """
    if minio_client is not None:
        prefix = f"tenant-general-warehouse/{tenant}/datasets/{dataset_name}/"
        if next(iter(minio_client.list_objects(bucket, prefix=prefix, recursive=True)), None):
            raise RuntimeError(
                f"s3a://{bucket}/{prefix} already has objects. Choose a new --dataset-suffix, "
                "or pass --replace-existing to overwrite them."
            )
    if spark is not None:
        namespace = f"{tenant}.{dataset_name}"
        if spark.catalog.databaseExists(namespace) and spark.sql(f"SHOW TABLES IN {namespace}").count():
            raise RuntimeError(
                f"{namespace} already has tables. Choose a new --dataset-suffix, "
                "or pass --replace-existing to overwrite them."
            )


def upload_files(
    minio_client,
    bucket: str,
    tenant: str,
    source: str,
    staging_dir: Path,
    slots: list[str],
    config_path: Path,
    dataset_suffix: str = "",
) -> None:
    dataset_name = target_dataset_name(source, dataset_suffix)
    prefix = f"tenant-general-warehouse/{tenant}/datasets/{dataset_name}"
    for slot in slots:
        local = staging_dir / f"{slot}.parquet"
        obj = f"{prefix}/{slot}.parquet"
        LOG.info("Uploading -> s3a://%s/%s", bucket, obj)
        minio_client.fput_object(bucket, obj, str(local),
                                 content_type="application/octet-stream")

    obj = f"{prefix}/{config_path.name}"
    LOG.info("Uploading -> s3a://%s/%s", bucket, obj)
    minio_client.fput_object(bucket, obj, str(config_path),
                             content_type="application/json")


# ---------------------------------------------------------------------------
# Phase 4: optional ingest
# ---------------------------------------------------------------------------

def run_ingest(config_s3_path: str, minio_client) -> Any:
    """Invoke data_lakehouse_ingest with the uploaded config (needs a Spark session)."""
    from data_lakehouse_ingest import ingest
    from data_lakehouse_ingest.orchestrator.init_utils import init_logger

    spark = _build_spark_session()
    return ingest(
        config=config_s3_path,
        spark=spark,
        logger=init_logger(None),
        minio_client=minio_client,
    )


def run_direct_ingest(
    config: dict,
    staging_dir: Path,
    slots: list[str],
) -> dict[str, int]:
    """Create Iceberg tables directly via Spark SQL.

    This bypasses data_lakehouse_ingest. Creates the namespace with the
    governance-aware flow, then reads each Parquet from the bronze S3 path and
    writes it as a managed table. Any table of the same name is dropped first,
    so callers guard existing targets with ensure_target_is_new().
    """
    from berdl_notebook_utils.spark.database import create_namespace_if_not_exists

    spark = _build_spark_session()

    tenant = config["tenant"]
    dataset_name = config["dataset"]

    ns = create_namespace_if_not_exists(
        spark, namespace=dataset_name, tenant_name=tenant, iceberg=True,
    )
    LOG.info("Using namespace: %s", ns)
    spark.sql(f"USE {ns}")

    bronze_base = config["paths"]["bronze_base"]
    results: dict[str, int] = {}
    for slot in slots:
        table_name = SLOT_TO_SILVER_NAME.get(slot, slot)
        parquet_path = f"{bronze_base}{slot}.parquet"
        LOG.info("Loading %s -> %s.%s", parquet_path, ns, table_name)
        spark.sql(f"DROP TABLE IF EXISTS {ns}.{table_name}")
        df = spark.read.parquet(parquet_path)
        df.write.mode("overwrite").saveAsTable(f"{ns}.{table_name}")
        count = spark.sql(f"SELECT COUNT(*) AS cnt FROM {ns}.{table_name}").collect()[0]["cnt"]
        results[table_name] = count
        LOG.info("  %s: %d rows", table_name, count)

    return results


def _build_spark_session():
    try:
        from berdl_notebook_utils.setup_spark_session import get_spark_session
    except ImportError as exc:
        raise RuntimeError(
            "berdl_notebook_utils.setup_spark_session.get_spark_session is required for --run-ingest"
        ) from exc
    return get_spark_session()


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def target_dataset_name(source: str, dataset_suffix: str = "") -> str:
    """Return the name used for the bronze prefix and silver namespace."""
    return SOURCE_TO_DATASET_NAME.get(source, source) + dataset_suffix


def process_source(source: str, args: argparse.Namespace, minio_client) -> None:
    dataset_name = SOURCE_TO_DATASET_NAME.get(source, source)
    target_name = target_dataset_name(source, args.dataset_suffix)
    dump_dir = args.dump_dir or (REPO_ROOT / "data" / f"{dataset_name}_dump")
    staging_dir = args.staging_dir or (REPO_ROOT / "data" / f"{dataset_name}_parquet")
    dump_dir = Path(dump_dir)
    staging_dir = Path(staging_dir)

    LOG.info("=== %s: dump_dir=%s staging_dir=%s ===", source, dump_dir, staging_dir)

    if not args.skip_dump:
        if source == "ssrl-mx":
            if args.snapshots_dir is None:
                raise RuntimeError(
                    "--snapshots-dir is required for ssrl-mx source"
                )
            run_dump_ssrl_mx(
                snapshots_dir=args.snapshots_dir,
                dump_dir=dump_dir,
                limit=args.limit,
                metadata_file=args.metadata_file,
                processing_file=args.processing_file,
            )
        else:
            run_dump(
                source=source,
                dump_dir=dump_dir,
                rate=args.rate,
                workers=args.workers,
                limit=args.limit,
                allow_failures=args.allow_failures,
            )
    else:
        LOG.info("Skipping dump phase for %s", source)

    if not args.skip_convert:
        slots = convert_yamls_to_parquet(dump_dir, staging_dir)
    else:
        slots = sorted(p.stem for p in staging_dir.glob("*.parquet"))
        LOG.info("Skipping convert; reusing %d existing Parquet files", len(slots))

    if not slots:
        LOG.warning("No Parquet files produced for %s; nothing to upload.", source)
        return

    config = build_ingest_config(
        source=source,
        tenant=args.tenant,
        bucket=args.bucket,
        staging_dir=staging_dir,
        slots=slots,
        dataset_suffix=args.dataset_suffix,
    )
    config_path = write_ingest_config(config, staging_dir, source)

    if not args.replace_existing:
        ensure_target_is_new(
            minio_client=None if args.skip_upload else minio_client,
            spark=_build_spark_session() if (args.direct_ingest or args.run_ingest) else None,
            bucket=args.bucket,
            tenant=args.tenant,
            dataset_name=target_name,
        )

    if not args.skip_upload:
        if minio_client is None:
            raise RuntimeError("MinIO client unavailable but upload phase is enabled")
        upload_files(
            minio_client=minio_client,
            bucket=args.bucket,
            tenant=args.tenant,
            source=source,
            staging_dir=staging_dir,
            slots=slots,
            config_path=config_path,
            dataset_suffix=args.dataset_suffix,
        )
    else:
        LOG.info("Skipping upload phase for %s", source)

    if args.direct_ingest:
        LOG.info("Running direct ingest for %s", source)
        report = run_direct_ingest(config, staging_dir, slots)
        LOG.info("Direct ingest complete: %s", report)
    elif args.run_ingest:
        cfg_s3 = (
            f"s3a://{args.bucket}/tenant-general-warehouse/{args.tenant}"
            f"/datasets/{target_name}/{config_path.name}"
        )
        LOG.info("Running data_lakehouse_ingest with config: %s", cfg_s3)
        report = run_ingest(cfg_s3, minio_client)
        LOG.info("Ingest report: %s", report)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--sources", default="sasbdb,simplescattering",
                   help="Comma-separated sources (default: sasbdb,simplescattering)")
    p.add_argument("--dump-dir", type=Path, default=None,
                   help="Override dump directory (default: data/{source}_dump per source)")
    p.add_argument("--staging-dir", type=Path, default=None,
                   help="Override Parquet staging directory (default: data/{source}_parquet)")
    p.add_argument("--rate", type=float, default=2.0,
                   help="Requests per second for dump (default: 2.0)")
    p.add_argument("--workers", type=int, default=1,
                   help="Concurrent workers for dump (default: 1)")
    p.add_argument("--limit", type=int, default=None,
                   help="Max entries per source (default: all)")
    p.add_argument("--tenant", default="lambda", help="Tenant name (default: lambda)")
    p.add_argument("--bucket", default="cdm-lake", help="Object-store bucket (default: cdm-lake)")
    p.add_argument("--dataset-suffix", default="",
                   help="Append to the bronze prefix and silver namespace, to load beside "
                        "the current tables (e.g. _202611 writes lambda.sasbdb_202611)")
    p.add_argument("--replace-existing", action="store_true",
                   help="Allow overwriting a bronze prefix or silver tables that already exist")
    p.add_argument("--skip-dump", action="store_true")
    p.add_argument("--skip-convert", action="store_true")
    p.add_argument("--skip-upload", action="store_true")
    p.add_argument("--run-ingest", action="store_true",
                   help="After upload, invoke data_lakehouse_ingest.ingest()")
    p.add_argument("--direct-ingest", action="store_true",
                   help="After upload, create Iceberg tables directly via Spark SQL")
    p.add_argument("--allow-failures", action="store_true",
                   help="Continue even if the dump phase reports failed entries")
    p.add_argument("--snapshots-dir", type=Path, default=None,
                   help="Directory with DCSS snapshot .json files (ssrl-mx only)")
    p.add_argument("--metadata-file", type=Path, default=None,
                   help="Sample metadata sidecar JSON (ssrl-mx only)")
    p.add_argument("--processing-file", type=Path, default=None,
                   help="Processing results sidecar JSON (ssrl-mx only)")
    p.add_argument("--log-level", default="INFO")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=args.log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    sources = [s.strip().lower() for s in args.sources.split(",") if s.strip()]
    unknown = [s for s in sources if s not in SUPPORTED_SOURCES]
    if unknown:
        raise SystemExit(f"Unsupported sources: {unknown}. Supported: {SUPPORTED_SOURCES}")

    if (len(sources) > 1) and (args.dump_dir or args.staging_dir):
        raise SystemExit(
            "--dump-dir / --staging-dir only make sense with a single --sources entry."
        )

    if args.snapshots_dir and "ssrl-mx" not in sources:
        raise SystemExit("--snapshots-dir is only valid with --sources=ssrl-mx")
    if "ssrl-mx" in sources and not args.skip_dump and not args.snapshots_dir:
        raise SystemExit("--snapshots-dir is required when dumping ssrl-mx")

    if args.dataset_suffix and not re.fullmatch(r"[a-z0-9_]+", args.dataset_suffix):
        raise SystemExit("--dataset-suffix may only contain lowercase letters, digits and _")

    minio_client = None
    if not args.skip_upload or args.run_ingest:
        minio_client = get_minio_client()

    for source in sources:
        process_source(source, args, minio_client)

    LOG.info("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
