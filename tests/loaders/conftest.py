"""Shared fixtures for loader tests."""

import json
from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def sasbdb_sasda52_response() -> dict:
    """Load mocked SASBDB SASDA52 API response."""
    fixture_path = FIXTURES_DIR / "sasbdb_SASDA52.json"
    return json.loads(fixture_path.read_text())


@pytest.fixture
def simplescattering_xsbhevph_html() -> str:
    """Load mocked Simple Scattering HTML response."""
    fixture_path = FIXTURES_DIR / "simplescattering_xsbhevph.html"
    return fixture_path.read_text()


@pytest.fixture
def pdb_1hho_entry_response() -> dict:
    """Load mocked PDB 1HHO entry API response."""
    fixture_path = FIXTURES_DIR / "pdb_1HHO_entry.json"
    return json.loads(fixture_path.read_text())


@pytest.fixture
def pdb_1hho_polymer_entities() -> list[dict]:
    """Load mocked PDB 1HHO polymer entity responses."""
    entity1 = json.loads((FIXTURES_DIR / "pdb_1HHO_entity1.json").read_text())
    entity2 = json.loads((FIXTURES_DIR / "pdb_1HHO_entity2.json").read_text())
    return [entity1, entity2]
