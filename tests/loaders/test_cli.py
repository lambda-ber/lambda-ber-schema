"""Tests for CLI commands."""

import json
import logging

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
        assert "emsl" in result.output
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

    def test_etl_emsl_help(self):
        """Test EMSL ETL command help."""
        result = runner.invoke(app, ["etl", "emsl", "--help"])
        assert result.exit_code == 0
        assert "--sample" in result.output

    def test_etl_dump_pdb_calls_load_all_with_filters(self, mocker, tmp_path):
        """Test dump-pdb invokes BatchLoader.load_all with expected options."""
        calls: dict[str, object] = {}

        class FakeBatchLoader:
            def __init__(self, loader, output_dir, requests_per_second, max_workers):
                calls["loader"] = loader
                calls["output_dir"] = output_dir
                calls["requests_per_second"] = requests_per_second
                calls["max_workers"] = max_workers

            def load_all(self, format="yaml", limit=None, **filters):
                calls["load_all"] = {
                    "format": format,
                    "limit": limit,
                    "filters": filters,
                }
                return {"total_entries": 5, "successful": 5, "failed": 0}

        class FakePDBLoader:
            pass

        def fake_file_handler(path):
            assert path.parent.exists()
            calls["batch_log_path"] = path
            return logging.NullHandler()

        mocker.patch("lambda_ber_schema.cli.PDBLoader", FakePDBLoader)
        mocker.patch("lambda_ber_schema.cli.BatchLoader", FakeBatchLoader)
        mocker.patch("lambda_ber_schema.cli.logging.FileHandler",
                     side_effect=fake_file_handler)
        mocker.patch("lambda_ber_schema.cli.logging.basicConfig")

        output_dir = tmp_path / "new" / "pdb_dump"
        result = runner.invoke(
            app,
            [
                "etl",
                "dump-pdb",
                "--output-dir",
                str(output_dir),
                "--format",
                "json",
                "--method",
                "EM",
                "--limit",
                "5",
                "--rate",
                "3.5",
                "--workers",
                "2",
            ],
        )

        assert result.exit_code == 0
        assert output_dir.exists()
        assert calls["output_dir"] == output_dir
        assert calls["requests_per_second"] == 3.5
        assert calls["max_workers"] == 2
        assert calls["batch_log_path"] == output_dir / "batch.log"
        assert calls["load_all"] == {
            "format": "json",
            "limit": 5,
            "filters": {"experimental_method": "EM"},
        }

    def test_etl_dump_pdb_retry_failed_path(self, mocker, tmp_path):
        """Test dump-pdb --retry-failed invokes retry path, not load_all."""
        calls: dict[str, object] = {}

        class FakeBatchLoader:
            def __init__(self, loader, output_dir, requests_per_second, max_workers):
                calls["output_dir"] = output_dir

            def retry_failed(self, format="yaml"):
                calls["retry_failed"] = format
                return {"retried": 2, "now_successful": 2, "still_failed": 0}

            def load_all(self, format="yaml", limit=None, **filters):
                calls["load_all_called"] = True
                return {}

        class FakePDBLoader:
            pass

        mocker.patch("lambda_ber_schema.cli.PDBLoader", FakePDBLoader)
        mocker.patch("lambda_ber_schema.cli.BatchLoader", FakeBatchLoader)
        mocker.patch("lambda_ber_schema.cli.logging.FileHandler",
                     return_value=logging.NullHandler())
        mocker.patch("lambda_ber_schema.cli.logging.basicConfig")

        output_dir = tmp_path / "retry" / "pdb_dump"
        result = runner.invoke(
            app,
            [
                "etl",
                "dump-pdb",
                "--output-dir",
                str(output_dir),
                "--retry-failed",
                "--format",
                "json",
            ],
        )

        assert result.exit_code == 0
        assert calls["retry_failed"] == "json"
        assert "load_all_called" not in calls

    def test_etl_dump_sasbdb_calls_load_all_with_filters(self, mocker, tmp_path):
        """Test dump-sasbdb invokes BatchLoader.load_all with expected options."""
        calls: dict[str, object] = {}

        class FakeBatchLoader:
            def __init__(self, loader, output_dir, requests_per_second, max_workers):
                calls["output_dir"] = output_dir
                calls["requests_per_second"] = requests_per_second
                calls["max_workers"] = max_workers

            def load_all(self, format="yaml", limit=None, **filters):
                calls["load_all"] = {
                    "format": format,
                    "limit": limit,
                    "filters": filters,
                }
                return {"total_entries": 4, "successful": 4, "failed": 0}

        class FakeSASBDBLoader:
            pass

        def fake_file_handler(path):
            assert path.parent.exists()
            calls["batch_log_path"] = path
            return logging.NullHandler()

        mocker.patch("lambda_ber_schema.cli.SASBDBLoader", FakeSASBDBLoader)
        mocker.patch("lambda_ber_schema.cli.BatchLoader", FakeBatchLoader)
        mocker.patch("lambda_ber_schema.cli.logging.FileHandler",
                     side_effect=fake_file_handler)
        mocker.patch("lambda_ber_schema.cli.logging.basicConfig")

        output_dir = tmp_path / "new" / "sasbdb_dump"
        result = runner.invoke(
            app,
            [
                "etl",
                "dump-sasbdb",
                "--output-dir",
                str(output_dir),
                "--format",
                "yaml",
                "--type",
                "protein",
                "--limit",
                "4",
                "--rate",
                "4.0",
                "--workers",
                "3",
            ],
        )

        assert result.exit_code == 0
        assert output_dir.exists()
        assert calls["batch_log_path"] == output_dir / "batch.log"
        assert calls["requests_per_second"] == 4.0
        assert calls["max_workers"] == 3
        assert calls["load_all"] == {
            "format": "yaml",
            "limit": 4,
            "filters": {"molecular_type": "protein"},
        }

    def test_etl_emsl_calls_loader_with_expected_args(self, mocker, tmp_path):
        """Test EMSL ETL command routes options into EMSLLoader.load_by_sample."""
        calls: dict[str, object] = {}

        class FakeLoader:
            def __init__(self, cache):
                calls["cache"] = cache

            def load_by_sample(
                self,
                sample_name,
                transaction_id=None,
                search_mode="like",
                key_filter=None,
                exact_match=False,
                similarity_threshold=None,
                limit=20,
            ):
                calls["load_by_sample"] = {
                    "sample_name": sample_name,
                    "transaction_id": transaction_id,
                    "search_mode": search_mode,
                    "key_filter": key_filter,
                    "exact_match": exact_match,
                    "similarity_threshold": similarity_threshold,
                    "limit": limit,
                }

                class _Result:
                    warnings = []

                    class _Dataset:
                        @staticmethod
                        def model_dump(exclude_none=True, mode="json"):
                            return {"id": "emsl:transaction_3736677"}

                    dataset = _Dataset()

                return _Result()

        mocker.patch("lambda_ber_schema.cli.EMSLLoader", FakeLoader)

        output_file = tmp_path / "emsl.yaml"
        result = runner.invoke(
            app,
            [
                "etl",
                "emsl",
                "--sample",
                "apo",
                "--transaction-id",
                "3736677",
                "--search-mode",
                "like",
                "--key-filter",
                "pncc",
                "--exact-match",
                "--limit",
                "10",
                "--output",
                str(output_file),
            ],
        )

        assert result.exit_code == 0
        assert output_file.exists()
        assert calls["load_by_sample"] == {
            "sample_name": "apo",
            "transaction_id": 3736677,
            "search_mode": "like",
            "key_filter": "pncc",
            "exact_match": True,
            "similarity_threshold": None,
            "limit": 10,
        }

    def test_etl_list_emsl_requires_sample(self):
        """EMSL listing should require --sample."""
        result = runner.invoke(app, ["etl", "list", "emsl"])
        assert result.exit_code == 1
        assert "--sample is required" in result.output

    def test_etl_list_emsl_routes_sample_filter(self, mocker):
        """Test etl list emsl calls loader.list_entries(sample_name=...)."""
        calls: dict[str, object] = {}

        class FakeLoader:
            def list_entries(self, sample_name=None, limit=None):
                calls["list_entries"] = {"sample_name": sample_name, "limit": limit}
                return ["3736677", "3736600"]

        mocker.patch("lambda_ber_schema.cli.EMSLLoader", FakeLoader)

        result = runner.invoke(
            app,
            ["etl", "list", "emsl", "--sample", "apo", "--limit", "2"],
        )
        assert result.exit_code == 0
        assert "Found 2 entries" in result.output
        assert calls["list_entries"] == {"sample_name": "apo", "limit": 2}


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
