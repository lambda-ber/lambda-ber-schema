"""Tests for version injection mechanism.

These tests verify that the dynamic versioning setup correctly injects
the version from git tags into both the package metadata and the schema YAML.
"""

import re
import subprocess
import zipfile
from pathlib import Path

import pytest

try:
    import tomllib
except ImportError:
    import tomli as tomllib  # Python < 3.11 fallback

# Path to the schema file
SCHEMA_PATH = Path(__file__).parent.parent / "src" / \
    "lambda_ber_schema" / "schema" / "lambda_ber_schema.yaml"
PROJECT_ROOT = Path(__file__).parent.parent

# The marker comment that identifies the version line for injection
VERSION_MARKER = "# Managed by uv-dynamic-versioning"

# Regex pattern that matches how the version line should look in the schema
VERSION_LINE_PATTERN = re.compile(
    r'^version:\s*"([^"]*)"\s*# Managed by uv-dynamic-versioning', re.MULTILINE)


def test_schema_has_version_field():
    """Test that the schema YAML has a version field with the marker comment."""
    content = SCHEMA_PATH.read_text()

    # Check that version field exists
    assert "version:" in content, "Schema YAML must have a 'version:' field"

    # Check that it has the marker comment for dynamic versioning
    assert VERSION_MARKER in content, (
        f"Schema YAML version line must contain '{VERSION_MARKER}' marker"
    )


def test_version_line_format():
    """Test that the version line matches the expected format for injection."""
    content = SCHEMA_PATH.read_text()
    lines = content.split("\n")

    version_line = None
    for line in lines:
        if "version:" in line and VERSION_MARKER in line:
            version_line = line
            break

    assert version_line is not None, "Could not find version line with marker"

    # The version line should match the pattern that uv-dynamic-versioning expects
    match = VERSION_LINE_PATTERN.match(version_line)
    assert match is not None, (
        f"Version line format is incorrect.\n"
        f"Expected format: version: \"X.Y.Z\" {VERSION_MARKER}\n"
        f"Got: {version_line}"
    )


def test_version_is_early_in_schema():
    """Test that version appears early in the schema (within first 10 lines)."""
    content = SCHEMA_PATH.read_text()
    lines = content.split("\n")[:10]

    found_version = any("version:" in line for line in lines)
    assert found_version, (
        "Version field should appear in the first 10 lines of the schema. "
        "This ensures it's a top-level schema attribute, not nested."
    )


def test_pyproject_pattern_matches_schema():
    """Test that the regex pattern in pyproject.toml can match the schema version line."""
    # Read the pattern from pyproject.toml using proper TOML parsing
    pyproject_path = PROJECT_ROOT / "pyproject.toml"

    with open(pyproject_path, "rb") as f:
        pyproject = tomllib.load(f)

    # Get the pattern from the parsed TOML (backslashes are already unescaped)
    pattern_str = pyproject["tool"]["hatch"]["build"]["hooks"]["version"]["pattern"]

    # Compile the pattern
    pattern = re.compile(pattern_str, re.MULTILINE)

    # Read the schema and try to match
    schema_content = SCHEMA_PATH.read_text()

    match = pattern.search(schema_content)
    assert match is not None, (
        f"The pattern in pyproject.toml does not match the version line in the schema.\n"
        f"Pattern: {pattern_str}\n"
        f"This will cause version injection to fail during builds."
    )

    # Verify the pattern captures a version group
    assert "version" in match.groupdict(), (
        "Pattern must capture a group named 'version' for injection to work"
    )


@pytest.mark.slow
def test_build_injects_version():
    """Test that running 'uv build' injects a version into the built package.

    This is a slower integration test that actually runs the build process.
    """
    # Run uv build
    result = subprocess.run(
        ["uv", "build"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Build failed: {result.stderr}"

    # Find the built wheel
    dist_dir = PROJECT_ROOT / "dist"
    wheels = list(dist_dir.glob("*.whl"))
    assert len(wheels) > 0, "No wheel files found after build"

    # Get the most recent wheel
    wheel_path = max(wheels, key=lambda p: p.stat().st_mtime)

    # Extract and check the schema from the wheel
    with zipfile.ZipFile(wheel_path, "r") as zf:
        # Find the schema file in the wheel
        schema_files = [n for n in zf.namelist(
        ) if n.endswith("lambda_ber_schema.yaml")]
        assert len(
            schema_files) == 1, f"Expected 1 schema file in wheel, found: {schema_files}"

        schema_content = zf.read(schema_files[0]).decode("utf-8")

    # Check that the version was injected (not 0.0.0)
    match = VERSION_LINE_PATTERN.search(schema_content)
    assert match is not None, "Version line not found in built schema"

    version = match.group(1)

    # The version should not be the placeholder
    assert version != "0.0.0", (
        "Version in built package is still 0.0.0 - injection may have failed"
    )

    # Version should look like a valid PEP 440 version
    # Could be "1.2.3" or "1.2.3.post5.dev0+abc1234" for dev builds
    assert re.match(r"^\d+\.\d+", version), (
        f"Version '{version}' doesn't look like a valid version number"
    )


def test_schema_version_field_is_string():
    """Test that the version is quoted as a string in YAML.

    YAML can interpret bare versions like 1.0 as floats, which causes issues.
    The version should always be quoted.
    """
    content = SCHEMA_PATH.read_text()

    # Find the version line
    for line in content.split("\n"):
        if line.startswith("version:"):
            # Check that the value is quoted
            assert '"' in line or "'" in line, (
                "Version value should be quoted in YAML to prevent type coercion. "
                f"Got: {line}"
            )
            break
