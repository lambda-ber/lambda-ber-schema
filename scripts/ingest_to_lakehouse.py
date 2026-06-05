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
import subprocess
import sys
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

# Dataset-level slots that aggregate to one Parquet each (lambda_ber_schema.yaml:185-244).
# Slot names whose silver-table name must differ from the bronze slot name.
# `data_files` collides with the reserved Iceberg metadata-table name and
# trips Polaris's path resolver (IllegalStateException:
# invalid_path_key_for_passthrough_resolved_path), so we expose it as
# `dataset_files` in the silver catalog. Bronze parquet keeps the slot name.
SLOT_TO_SILVER_NAME: dict[str, str] = {
    "data_files": "dataset_files",
}

ENTITY_SLOTS: tuple[str, ...] = (
    "studies",
    "instruments",
    "protein_constructs",
    "samples",
    "sample_preparations",
    "experiment_runs",
    "workflow_runs",
    "data_files",
    "images",
    "study_sample_associations",
    "study_experiment_associations",
    "study_workflow_associations",
    "experiment_sample_associations",
    "experiment_instrument_associations",
    "workflow_experiment_associations",
    "workflow_input_associations",
    "workflow_output_associations",
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
    """Invoke dump-ssrl-mx (filesystem-only, no rate limiting)."""
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


def convert_yamls_to_parquet(dump_dir: Path, staging_dir: Path) -> list[str]:
    """Aggregate per-entry YAMLs into one Parquet per non-empty entity slot.

    Returns the list of slot names that produced a Parquet file.
    """
    staging_dir.mkdir(parents=True, exist_ok=True)
    rows_by_slot: dict[str, list[dict]] = {slot: [] for slot in ENTITY_SLOTS}

    yaml_count = 0
    for _, doc in _iter_yaml_docs(dump_dir):
        yaml_count += 1
        entry_id = doc.get("id")
        for slot in ENTITY_SLOTS:
            for raw_row in (doc.get(slot) or []):
                if not isinstance(raw_row, dict):
                    continue
                rows_by_slot[slot].append(_flatten_row(raw_row, entry_id))

    LOG.info("Parsed %d YAML files from %s", yaml_count, dump_dir)

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
) -> dict:
    dataset_name = SOURCE_TO_DATASET_NAME.get(source, source)
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


def upload_files(
    minio_client,
    bucket: str,
    tenant: str,
    source: str,
    staging_dir: Path,
    slots: list[str],
    config_path: Path,
) -> None:
    dataset_name = SOURCE_TO_DATASET_NAME.get(source, source)
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
    """Create tables directly via Spark SQL (Delta/Hive flow).

    This bypasses data_lakehouse_ingest and works when the Iceberg catalog
    flow is unavailable. Creates the namespace with the governance-aware
    Delta/Hive flow, then reads each Parquet from the bronze S3 path and
    writes it as a managed table.
    """
    from berdl_notebook_utils.spark.database import create_namespace_if_not_exists

    spark = _build_spark_session()

    tenant = config["tenant"]
    dataset_name = config["dataset"]

    ns = create_namespace_if_not_exists(
        spark, namespace=dataset_name, tenant_name=tenant, iceberg=False,
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

def process_source(source: str, args: argparse.Namespace, minio_client) -> None:
    dataset_name = SOURCE_TO_DATASET_NAME.get(source, source)
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
    )
    config_path = write_ingest_config(config, staging_dir, source)

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
        )
    else:
        LOG.info("Skipping upload phase for %s", source)

    if args.direct_ingest:
        LOG.info("Running direct ingest (Delta/Hive flow) for %s", source)
        report = run_direct_ingest(config, staging_dir, slots)
        LOG.info("Direct ingest complete: %s", report)
    elif args.run_ingest:
        cfg_s3 = (
            f"s3a://{args.bucket}/tenant-general-warehouse/{args.tenant}"
            f"/datasets/{dataset_name}/{config_path.name}"
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
    p.add_argument("--skip-dump", action="store_true")
    p.add_argument("--skip-convert", action="store_true")
    p.add_argument("--skip-upload", action="store_true")
    p.add_argument("--run-ingest", action="store_true",
                   help="After upload, invoke data_lakehouse_ingest.ingest()")
    p.add_argument("--direct-ingest", action="store_true",
                   help="After upload, create tables directly via Spark SQL (Delta/Hive flow)")
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

    minio_client = None
    if not args.skip_upload or args.run_ingest:
        minio_client = get_minio_client()

    for source in sources:
        process_source(source, args, minio_client)

    LOG.info("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
