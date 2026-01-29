"""Tests for CLI commands."""

import json

import pytest
from typer.testing import CliRunner

from lambda_ber_schema.cli import app

runner = CliRunner()


class TestCLI:
    """Tests for CLI commands."""

    def test_help(self):
        """Test CLI help output."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "lambda-ber-schema" in result.output

    def test_version(self):
        """Test version command."""
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert "lambda-ber-schema" in result.output

    def test_etl_help(self):
        """Test ETL subcommand help."""
        result = runner.invoke(app, ["etl", "--help"])
        assert result.exit_code == 0
        assert "sasbdb" in result.output
        assert "simplescattering" in result.output
        assert "pdb" in result.output
        assert "list" in result.output

    def test_etl_sasbdb_help(self):
        """Test SASBDB ETL command help."""
        result = runner.invoke(app, ["etl", "sasbdb", "--help"])
        assert result.exit_code == 0
        assert "SASBDB entry code" in result.output

    def test_etl_simplescattering_help(self):
        """Test Simple Scattering ETL command help."""
        result = runner.invoke(app, ["etl", "simplescattering", "--help"])
        assert result.exit_code == 0
        assert "Simple Scattering dataset code" in result.output

    def test_etl_pdb_help(self):
        """Test PDB ETL command help."""
        result = runner.invoke(app, ["etl", "pdb", "--help"])
        assert result.exit_code == 0
        assert "PDB entry ID" in result.output


@pytest.mark.integration
@pytest.mark.slow
class TestCLIIntegration:
    """Integration tests for CLI that hit real APIs."""

    def test_etl_sasbdb(self, tmp_path):
        """Test SASBDB ETL command."""
        output_file = tmp_path / "output.yaml"
        result = runner.invoke(
            app,
            ["etl", "sasbdb", "--entry", "SASDA52",
                "--output", str(output_file)],
        )
        assert result.exit_code == 0
        assert output_file.exists()

        # Check output contains expected content
        content = output_file.read_text()
        assert "sasbdb:SASDA52" in content
        assert "Alcohol dehydrogenase" in content

    def test_etl_sasbdb_json_format(self, tmp_path):
        """Test SASBDB ETL with JSON output."""
        output_file = tmp_path / "output.json"
        result = runner.invoke(
            app,
            [
                "etl",
                "sasbdb",
                "--entry",
                "SASDA52",
                "--output",
                str(output_file),
                "--format",
                "json",
            ],
        )
        assert result.exit_code == 0

        # Verify valid JSON
        data = json.loads(output_file.read_text())
        assert data["id"] == "sasbdb:SASDA52"

    def test_etl_list_sasbdb(self):
        """Test listing SASBDB entries."""
        result = runner.invoke(app, ["etl", "list", "sasbdb", "--limit", "3"])
        assert result.exit_code == 0
        assert "Found 3 entries" in result.output

    def test_etl_simplescattering(self, tmp_path):
        """Test Simple Scattering ETL command."""
        output_file = tmp_path / "output.yaml"
        result = runner.invoke(
            app,
            [
                "etl",
                "simplescattering",
                "--dataset",
                "xsbhevph",
                "--output",
                str(output_file),
            ],
        )
        assert result.exit_code == 0
        assert output_file.exists()

        # Check output contains expected content
        content = output_file.read_text()
        assert "simplescattering:xsbhevph" in content
        assert "GluRS" in content

    def test_etl_list_simplescattering(self):
        """Test listing Simple Scattering entries."""
        result = runner.invoke(
            app, ["etl", "list", "simplescattering", "--limit", "3"]
        )
        assert result.exit_code == 0
        assert "Found 3 entries" in result.output

    def test_etl_pdb(self, tmp_path):
        """Test PDB ETL command."""
        output_file = tmp_path / "output.yaml"
        result = runner.invoke(
            app,
            ["etl", "pdb", "--entry", "1HHO", "--output", str(output_file)],
        )
        assert result.exit_code == 0
        assert output_file.exists()

        # Check output contains expected content
        content = output_file.read_text()
        assert "pdb:1HHO" in content
        assert "OXYHAEMOGLOBIN" in content.upper()

    def test_etl_list_pdb(self):
        """Test listing PDB entries."""
        result = runner.invoke(app, ["etl", "list", "pdb", "--limit", "3"])
        assert result.exit_code == 0
        assert "Found 3 entries" in result.output
