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


_SSRL_MX_SNAPSHOT = (
    Path(__file__).parent.parent / "data" / "raw" / "beamline-snapshots" / "SA_x4_1_00001.json"
)
_SSRL_MX_SIDECAR_DIR = FIXTURES_DIR / "ssrl"


@pytest.fixture
def ssrl_mx_snapshot() -> dict:
    """Load real SSRL MX snapshot (SA_x4 from BL12-2) as a dict."""
    return json.loads(_SSRL_MX_SNAPSHOT.read_text())


@pytest.fixture
def ssrl_mx_snapshot_path() -> Path:
    """Return path to real SSRL MX snapshot (SA_x4 from BL12-2)."""
    return _SSRL_MX_SNAPSHOT


@pytest.fixture
def ssrl_mx_sample_metadata_path() -> Path:
    """Sidecar: sample metadata (UUIDs, protein names, study info)."""
    return _SSRL_MX_SIDECAR_DIR / "sample_metadata.json"


@pytest.fixture
def ssrl_mx_processing_results_path() -> Path:
    """Sidecar: autoproc/aimless processing results + output files."""
    return _SSRL_MX_SIDECAR_DIR / "processing_results.json"


@pytest.fixture
def ssrl_mx_loader(ssrl_mx_sample_metadata_path, ssrl_mx_processing_results_path):
    """A pre-wired SSRLMXLoader pointing at the committed test sidecars."""
    from lambda_ber_schema.loaders import SSRLMXLoader
    return SSRLMXLoader(
        metadata_file=ssrl_mx_sample_metadata_path,
        processing_results_file=ssrl_mx_processing_results_path,
    )
