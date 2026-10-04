"""Shared fixtures for loader tests."""

import gzip
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


#: Real RCSB Data API responses, one gzipped file per record, named after the request path:
#: entry_7ZYI, polymer_entity_7ZYI_1, chemcomp_CHO, interface_7ZYI_1_2 and so on.
PDB_FIXTURES_DIR = FIXTURES_DIR / "pdb"

#: The entries captured, chosen so that between them every kind of PDB entry is exercised.
PDB_FIXTURE_ENTRIES = (
    "7ZYI",  # cryo-EM single particle, membrane protein, Fab, nanobody, ligands
    "6LU7",  # X-ray, synchrotron, peptide-like covalent inhibitor
    "6BOC",  # X-ray, LCP crystallization, grants, ORCIDs, binding affinity
    "1AAY",  # X-ray, protein-DNA complex
    "1HHO",  # X-ray, 1980s entry, heme
    "1D3Z",  # solution NMR
    "6VXX",  # cryo-EM, glycosylated
    "6MB3",  # cryo-EM with sub-assemblies
    "6TUQ",  # cryo-EM helical
    "4BZJ",  # cryo-EM subtomogram averaging
    "6UOU",  # MicroED
    "7S4R",  # serial femtosecond crystallography
    "6D4L",  # joint X-ray and neutron
    "1W2R",  # solution scattering
    "2C8I",  # negative stain and cryo-EM, virus
    "1WKX",  # protein from a natural source
)


def read_pdb_fixture(path: str) -> dict | None:
    """The fixture for a Data API path such as 'core/entry/7ZYI', or None if not captured."""
    parts = path.split("/")[1:]
    name = parts[0] + ("_" + "_".join(parts[1:]) if len(parts) > 1 else "")
    fixture = PDB_FIXTURES_DIR / f"{name}.json.gz"
    if not fixture.exists():
        return None
    return json.loads(gzip.decompress(fixture.read_bytes()))


@pytest.fixture
def pdb_loader():
    """A PDBLoader that answers from the captured fixtures instead of the network."""
    from lambda_ber_schema.loaders.pdb import PDBLoader

    class FixturePDBLoader(PDBLoader):
        def _get(self, path, cache_key=None):
            return read_pdb_fixture(path)

    return FixturePDBLoader()


@pytest.fixture
def sasbdb_sasdv63_response() -> dict:
    """Load mocked SASBDB SASDV63 API response (B2 SINE RNA, a single RNA molecule)."""
    return json.loads((FIXTURES_DIR / "sasbdb_SASDV63.json").read_text())


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
