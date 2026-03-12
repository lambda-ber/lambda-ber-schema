"""
Command-line interface for lambda-ber-schema.

Provides ETL commands for loading data from external structural biology repositories.
"""

import json
from pathlib import Path
from typing import Annotated

import requests
import typer
import yaml

import logging

from lambda_ber_schema.loaders import (
    BatchLoader,
    EMSLLoader,
    PDBLoader,
    ResponseCache,
    SASBDBLoader,
    SimpleScatteringLoader,
)

app = typer.Typer(
    name="lambda-ber-schema",
    help="CLI for lambda-ber-schema: multimodal structural biology data",
    no_args_is_help=True,
)

etl_app = typer.Typer(
    help="ETL commands for loading data from external sources")
app.add_typer(etl_app, name="etl")


def _serialize_dataset(dataset, format: str) -> str:
    """Serialize dataset to requested format."""
    normalized_format = format.lower()
    if normalized_format not in {"json", "yaml"}:
        typer.echo(
            f"Invalid format: {format}. Supported formats are: json, yaml",
            err=True,
        )
        raise typer.Exit(1)

    # Convert Pydantic model to dict, excluding None values
    data = dataset.model_dump(exclude_none=True, mode="json")

    if normalized_format == "json":
        return json.dumps(data, indent=2)
    return yaml.dump(data, default_flow_style=False, sort_keys=False)


def _load_with_error_handling(loader, identifier: str):
    """Load a dataset with friendly error messages and exit codes."""
    try:
        return loader.load(identifier)
    except requests.HTTPError as exc:
        status = getattr(exc.response, "status_code", None)
        status_msg = f" (HTTP {status})" if status is not None else ""
        typer.echo(
            f"Error: failed to fetch {identifier} from {loader.source_name}{status_msg}",
            err=True,
        )
        raise typer.Exit(1) from exc
    except ValueError as exc:
        typer.echo(
            f"Error: {identifier} not found or invalid for {loader.source_name}",
            err=True,
        )
        raise typer.Exit(2) from exc
    except Exception as exc:
        typer.echo(
            f"Error: unexpected failure loading {identifier} from {loader.source_name}",
            err=True,
        )
        raise typer.Exit(1) from exc


@etl_app.command("sasbdb")
def etl_sasbdb(
    entry: Annotated[
        str,
        typer.Option("--entry", "-e",
                     help="SASBDB entry code (e.g., SASDA52)"),
    ],
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o",
                     help="Output file path (stdout if not specified)"),
    ] = None,
    format: Annotated[
        str,
        typer.Option("--format", "-f", help="Output format: yaml or json"),
    ] = "yaml",
    cache: Annotated[
        bool,
        typer.Option("--cache/--no-cache",
                     help="Enable/disable response caching"),
    ] = False,
    cache_dir: Annotated[
        Path | None,
        typer.Option("--cache-dir", help="Cache directory (default: .cache)"),
    ] = None,
) -> None:
    """
    Load data from SASBDB (Small Angle Scattering Biological Data Bank).

    Examples:

        lambda-ber-schema etl sasbdb --entry SASDA52

        lambda-ber-schema etl sasbdb --entry SASDA52 --output data.yaml

        lambda-ber-schema etl sasbdb --entry SASDA52 --format json --cache
    """
    # Set up loader with optional cache
    response_cache = ResponseCache(
        cache_dir=cache_dir or Path(".cache"),
        enabled=cache,
    )
    loader = SASBDBLoader(cache=response_cache)

    # Load the entry
    typer.echo(f"Loading SASBDB entry: {entry}", err=True)
    result = _load_with_error_handling(loader, entry)

    # Report warnings
    if result.warnings:
        for warning in result.warnings:
            typer.echo(f"Warning: {warning}", err=True)

    # Serialize output
    output_str = _serialize_dataset(result.dataset, format)

    if output:
        output.write_text(output_str)
        typer.echo(f"Wrote output to: {output}", err=True)
    else:
        typer.echo(output_str)


@etl_app.command("simplescattering")
def etl_simplescattering(
    dataset: Annotated[
        str,
        typer.Option("--dataset", "-d",
                     help="Simple Scattering dataset code (e.g., xsbhevph)"),
    ],
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o",
                     help="Output file path (stdout if not specified)"),
    ] = None,
    format: Annotated[
        str,
        typer.Option("--format", "-f", help="Output format: yaml or json"),
    ] = "yaml",
    cache: Annotated[
        bool,
        typer.Option("--cache/--no-cache",
                     help="Enable/disable response caching"),
    ] = False,
    cache_dir: Annotated[
        Path | None,
        typer.Option("--cache-dir", help="Cache directory (default: .cache)"),
    ] = None,
) -> None:
    """
    Load data from Simple Scattering (SEC-SAXS from SIBYLS beamline).

    Examples:

        lambda-ber-schema etl simplescattering --dataset xsbhevph

        lambda-ber-schema etl simplescattering --dataset xsbhevph --output data.yaml

        lambda-ber-schema etl simplescattering --dataset xsbhevph --format json --cache
    """
    # Set up loader with optional cache
    response_cache = ResponseCache(
        cache_dir=cache_dir or Path(".cache"),
        enabled=cache,
    )
    loader = SimpleScatteringLoader(cache=response_cache)

    # Load the dataset
    typer.echo(f"Loading Simple Scattering dataset: {dataset}", err=True)
    result = _load_with_error_handling(loader, dataset)

    # Report warnings
    if result.warnings:
        for warning in result.warnings:
            typer.echo(f"Warning: {warning}", err=True)

    # Serialize output
    output_str = _serialize_dataset(result.dataset, format)

    if output:
        output.write_text(output_str)
        typer.echo(f"Wrote output to: {output}", err=True)
    else:
        typer.echo(output_str)


@etl_app.command("pdb")
def etl_pdb(
    entry: Annotated[
        str,
        typer.Option("--entry", "-e", help="PDB entry ID (e.g., 1HHO, 7S4S)"),
    ],
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o",
                     help="Output file path (stdout if not specified)"),
    ] = None,
    format: Annotated[
        str,
        typer.Option("--format", "-f", help="Output format: yaml or json"),
    ] = "yaml",
    cache: Annotated[
        bool,
        typer.Option("--cache/--no-cache",
                     help="Enable/disable response caching"),
    ] = False,
    cache_dir: Annotated[
        Path | None,
        typer.Option("--cache-dir", help="Cache directory (default: .cache)"),
    ] = None,
) -> None:
    """
    Load data from PDB (Protein Data Bank).

    Examples:

        lambda-ber-schema etl pdb --entry 1HHO

        lambda-ber-schema etl pdb --entry 7S4S --output data.yaml

        lambda-ber-schema etl pdb --entry 1HHO --format json --cache
    """
    # Set up loader with optional cache
    response_cache = ResponseCache(
        cache_dir=cache_dir or Path(".cache"),
        enabled=cache,
    )
    loader = PDBLoader(cache=response_cache)

    # Load the entry
    typer.echo(f"Loading PDB entry: {entry}", err=True)
    result = _load_with_error_handling(loader, entry)

    # Report warnings
    if result.warnings:
        for warning in result.warnings:
            typer.echo(f"Warning: {warning}", err=True)

    # Serialize output
    output_str = _serialize_dataset(result.dataset, format)

    if output:
        output.write_text(output_str)
        typer.echo(f"Wrote output to: {output}", err=True)
    else:
        typer.echo(output_str)


@etl_app.command("emsl")
def etl_emsl(
    sample: Annotated[
        str,
        typer.Option(
            "--sample",
            "-s",
            help="Sample query text for EMSL transaction search (e.g., apo)",
        ),
    ],
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o",
                     help="Output file path (stdout if not specified)"),
    ] = None,
    format: Annotated[
        str,
        typer.Option("--format", "-f", help="Output format: yaml or json"),
    ] = "yaml",
    cache: Annotated[
        bool,
        typer.Option("--cache/--no-cache",
                     help="Enable/disable response caching"),
    ] = False,
    cache_dir: Annotated[
        Path | None,
        typer.Option("--cache-dir", help="Cache directory (default: .cache)"),
    ] = None,
    transaction_id: Annotated[
        int | None,
        typer.Option(
            "--transaction-id",
            "-t",
            help="Optional transaction ID to select from search results",
        ),
    ] = None,
    search_mode: Annotated[
        str,
        typer.Option(
            "--search-mode",
            help="Search mode: like, regex, or fuzzy",
        ),
    ] = "like",
    key_filter: Annotated[
        str | None,
        typer.Option(
            "--key-filter",
            help="Optional sample-key filter (e.g., pncc, short_sample_name)",
        ),
    ] = "pncc",
    exact_match: Annotated[
        bool,
        typer.Option(
            "--exact-match/--partial-match",
            help="Require exact sample match",
        ),
    ] = False,
    similarity_threshold: Annotated[
        float | None,
        typer.Option(
            "--similarity-threshold",
            help="Fuzzy matching threshold (0.0-1.0, fuzzy mode only)",
        ),
    ] = None,
    limit: Annotated[
        int,
        typer.Option(
            "--limit",
            "-n",
            help="Maximum transactions to consider in sample search",
        ),
    ] = 20,
) -> None:
    """
    Load data from the EMSL public API using sample-search transactions.

    Examples:

        lambda-ber-schema etl emsl --sample apo

        lambda-ber-schema etl emsl --sample apo --transaction-id 3736677

        lambda-ber-schema etl emsl --sample apo --format json --cache
    """
    response_cache = ResponseCache(
        cache_dir=cache_dir or Path(".cache"),
        enabled=cache,
    )
    loader = EMSLLoader(cache=response_cache)

    typer.echo(f"Loading EMSL sample query: {sample}", err=True)
    try:
        result = loader.load_by_sample(
            sample_name=sample,
            transaction_id=transaction_id,
            search_mode=search_mode,
            key_filter=key_filter,
            exact_match=exact_match,
            similarity_threshold=similarity_threshold,
            limit=limit,
        )
    except requests.HTTPError as exc:
        status = getattr(exc.response, "status_code", None)
        status_msg = f" (HTTP {status})" if status is not None else ""
        typer.echo(
            f"Error: failed to fetch EMSL data for sample '{sample}'{status_msg}",
            err=True,
        )
        raise typer.Exit(1) from exc
    except ValueError as exc:
        typer.echo(
            f"Error: {exc}",
            err=True,
        )
        raise typer.Exit(2) from exc
    except Exception as exc:
        typer.echo(
            f"Error: unexpected failure loading EMSL sample '{sample}'",
            err=True,
        )
        raise typer.Exit(1) from exc

    if result.warnings:
        for warning in result.warnings:
            typer.echo(f"Warning: {warning}", err=True)

    output_str = _serialize_dataset(result.dataset, format)

    if output:
        output.write_text(output_str)
        typer.echo(f"Wrote output to: {output}", err=True)
    else:
        typer.echo(output_str)


@etl_app.command("list")
def etl_list(
    source: Annotated[
        str,
        typer.Argument(help="Data source: pdb, sasbdb, simplescattering, emsl"),
    ],
    molecular_type: Annotated[
        str | None,
        typer.Option("--type", "-t",
                     help="Molecular type filter (sasbdb only)"),
    ] = None,
    method: Annotated[
        str | None,
        typer.Option(
            "--method", "-m", help="Experimental method filter (pdb only: X-RAY, EM, NMR)"),
    ] = None,
    sample: Annotated[
        str | None,
        typer.Option("--sample", "-s", help="Sample query (emsl only)"),
    ] = None,
    limit: Annotated[
        int,
        typer.Option("--limit", "-n",
                     help="Maximum number of entries to list"),
    ] = 20,
) -> None:
    """
    List available entries from a data source.

    Examples:

        lambda-ber-schema etl list sasbdb

        lambda-ber-schema etl list sasbdb --type protein --limit 10

        lambda-ber-schema etl list simplescattering --limit 5

        lambda-ber-schema etl list pdb --method X-RAY --limit 10

        lambda-ber-schema etl list emsl --sample apo --limit 10
    """
    source_lower = source.lower()

    if source_lower == "sasbdb":
        loader = SASBDBLoader()
        entries = loader.list_entries(
            molecular_type=molecular_type, limit=limit)
    elif source_lower == "simplescattering":
        loader = SimpleScatteringLoader()
        entries = loader.list_entries(limit=limit)
    elif source_lower == "pdb":
        loader = PDBLoader()
        entries = loader.list_entries(experimental_method=method, limit=limit)
    elif source_lower == "emsl":
        if not sample:
            typer.echo(
                "Error: --sample is required when listing EMSL entries",
                err=True,
            )
            raise typer.Exit(1)
        loader = EMSLLoader()
        entries = loader.list_entries(sample_name=sample, limit=limit)
    else:
        typer.echo(
            f"Unknown source: {source}. Available: pdb, sasbdb, simplescattering, emsl", err=True)
        raise typer.Exit(1)

    typer.echo(f"Found {len(entries)} entries:")
    for code in entries:
        typer.echo(f"  {code}")


@etl_app.command("dump-pdb")
def etl_dump_pdb(
    output_dir: Annotated[
        Path,
        typer.Option("--output-dir", "-o",
                     help="Directory to save output files"),
    ],
    format: Annotated[
        str,
        typer.Option("--format", "-f", help="Output format: yaml or json"),
    ] = "yaml",
    method: Annotated[
        str | None,
        typer.Option("--method", "-m",
                     help="Filter by method (X-RAY, EM, NMR)"),
    ] = None,
    limit: Annotated[
        int | None,
        typer.Option("--limit", "-n",
                     help="Maximum entries to load (default: all)"),
    ] = None,
    rate: Annotated[
        float,
        typer.Option("--rate", "-r",
                     help="Requests per second (default: 2.0)"),
    ] = 2.0,
    workers: Annotated[
        int,
        typer.Option("--workers", "-w",
                     help="Concurrent workers (default: 1)"),
    ] = 1,
    retry_failed: Annotated[
        bool,
        typer.Option("--retry-failed", help="Retry previously failed entries"),
    ] = False,
) -> None:
    """
    Dump all PDB entries to a directory.

    Creates one file per entry in the output directory. Supports resume -
    if interrupted, run again to continue from where it left off.

    Examples:

        # Load all PDB entries (will take many hours)
        lambda-ber-schema etl dump-pdb --output-dir ./pdb_dump

        # Load only X-ray structures
        lambda-ber-schema etl dump-pdb --output-dir ./pdb_xray --method X-RAY

        # Load first 100 entries for testing
        lambda-ber-schema etl dump-pdb --output-dir ./pdb_test --limit 100

        # Resume after interruption
        lambda-ber-schema etl dump-pdb --output-dir ./pdb_dump

        # Retry failed entries
        lambda-ber-schema etl dump-pdb --output-dir ./pdb_dump --retry-failed
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(output_dir / "batch.log"),
        ],
    )

    # Create loader
    loader = PDBLoader()
    batch = BatchLoader(
        loader=loader,
        output_dir=output_dir,
        requests_per_second=rate,
        max_workers=workers,
    )

    if retry_failed:
        typer.echo("Retrying failed entries...", err=True)
        result = batch.retry_failed(format=format)
        typer.echo(f"Retry complete: {result}", err=True)
    else:
        # Build filters
        filters = {}
        if method:
            filters["experimental_method"] = method

        typer.echo(f"Starting PDB dump to {output_dir}...", err=True)
        typer.echo(f"Rate limit: {rate} req/sec, Workers: {workers}", err=True)
        if limit:
            typer.echo(f"Limit: {limit} entries", err=True)
        if method:
            typer.echo(f"Filter: method={method}", err=True)

        result = batch.load_all(format=format, limit=limit, **filters)
        typer.echo(f"Complete: {result}", err=True)


@etl_app.command("dump-sasbdb")
def etl_dump_sasbdb(
    output_dir: Annotated[
        Path,
        typer.Option("--output-dir", "-o",
                     help="Directory to save output files"),
    ],
    format: Annotated[
        str,
        typer.Option("--format", "-f", help="Output format: yaml or json"),
    ] = "yaml",
    molecular_type: Annotated[
        str | None,
        typer.Option(
            "--type", "-t", help="Filter by molecular type (protein, rna, dna, heterocomplex)"),
    ] = None,
    limit: Annotated[
        int | None,
        typer.Option("--limit", "-n",
                     help="Maximum entries to load (default: all)"),
    ] = None,
    rate: Annotated[
        float,
        typer.Option("--rate", "-r",
                     help="Requests per second (default: 2.0)"),
    ] = 2.0,
    workers: Annotated[
        int,
        typer.Option("--workers", "-w",
                     help="Concurrent workers (default: 1)"),
    ] = 1,
    retry_failed: Annotated[
        bool,
        typer.Option("--retry-failed", help="Retry previously failed entries"),
    ] = False,
) -> None:
    """
    Dump all SASBDB entries to a directory.

    Creates one file per entry in the output directory. Supports resume -
    if interrupted, run again to continue from where it left off.

    Examples:

        # Load all SASBDB entries (~2k entries, ~30 min)
        lambda-ber-schema etl dump-sasbdb --output-dir ./sasbdb_dump

        # Load only protein entries
        lambda-ber-schema etl dump-sasbdb --output-dir ./sasbdb_protein --type protein

        # Load first 50 entries for testing
        lambda-ber-schema etl dump-sasbdb --output-dir ./sasbdb_test --limit 50

        # Resume after interruption
        lambda-ber-schema etl dump-sasbdb --output-dir ./sasbdb_dump

        # Retry failed entries
        lambda-ber-schema etl dump-sasbdb --output-dir ./sasbdb_dump --retry-failed
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(output_dir / "batch.log"),
        ],
    )

    # Create loader
    loader = SASBDBLoader()
    batch = BatchLoader(
        loader=loader,
        output_dir=output_dir,
        requests_per_second=rate,
        max_workers=workers,
    )

    if retry_failed:
        typer.echo("Retrying failed entries...", err=True)
        result = batch.retry_failed(format=format)
        typer.echo(f"Retry complete: {result}", err=True)
    else:
        # Build filters
        filters = {}
        if molecular_type:
            filters["molecular_type"] = molecular_type

        typer.echo(f"Starting SASBDB dump to {output_dir}...", err=True)
        typer.echo(f"Rate limit: {rate} req/sec, Workers: {workers}", err=True)
        if limit:
            typer.echo(f"Limit: {limit} entries", err=True)
        if molecular_type:
            typer.echo(f"Filter: type={molecular_type}", err=True)

        result = batch.load_all(format=format, limit=limit, **filters)
        typer.echo(f"Complete: {result}", err=True)


@app.command()
def version() -> None:
    """Show version information."""
    try:
        from importlib.metadata import version as get_version

        v = get_version("lambda-ber-schema")
    except Exception:
        v = "unknown"

    typer.echo(f"lambda-ber-schema {v}")


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
