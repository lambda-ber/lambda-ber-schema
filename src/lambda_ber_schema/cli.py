"""
Command-line interface for lambda-ber-schema.

Provides ETL commands for loading data from external structural biology repositories.
"""

import json
from pathlib import Path
from typing import Annotated

import typer
import yaml

from lambda_ber_schema.loaders import PDBLoader, ResponseCache, SASBDBLoader, SimpleScatteringLoader

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
    result = loader.load(entry)

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
    result = loader.load(dataset)

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
    result = loader.load(entry)

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


@etl_app.command("list")
def etl_list(
    source: Annotated[
        str,
        typer.Argument(help="Data source: pdb, sasbdb, simplescattering"),
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
    else:
        typer.echo(
            f"Unknown source: {source}. Available: pdb, sasbdb, simplescattering", err=True)
        raise typer.Exit(1)

    typer.echo(f"Found {len(entries)} entries:")
    for code in entries:
        typer.echo(f"  {code}")


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
