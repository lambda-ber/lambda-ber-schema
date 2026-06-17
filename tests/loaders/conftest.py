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


# A real published SSRL MX distribution package (LAMBDA RO-Crate), copied verbatim from a released
# distribution (the PDB 9MS4 Xa_EXLX1 expansin deposition). It is a fully profile-conformant crate
# (inline @context, official runParameters/instrumentName terms, approved facility/technique termCodes)
# and is already free of internal filesystem paths. Slimmed to just ro-crate-metadata.json — the loader
# reads only the crate (run definition, stats, and file refs are all embedded), not the tar/mtz/provenance.
_SSRL_MX_PACKAGE = FIXTURES_DIR / "ssrl" / "package"


@pytest.fixture
def ssrl_mx_package_path() -> Path:
    """Path to the published SSRL MX distribution package (RO-Crate) fixture."""
    return _SSRL_MX_PACKAGE


@pytest.fixture
def ssrl_mx_loader():
    """A crate-driven SSRLMXLoader."""
    from lambda_ber_schema.loaders import SSRLMXLoader
    return SSRLMXLoader()


@pytest.fixture
def ssrl_mx_dataset(ssrl_mx_loader, ssrl_mx_package_path):
    """The Dataset produced by loading the package fixture."""
    return ssrl_mx_loader.load(str(ssrl_mx_package_path)).dataset
