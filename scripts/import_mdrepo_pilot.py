"""Rebuild the three MDRepo examples offline, or refresh their public API snapshots.

Run from the repository: uv run python scripts/import_mdrepo_pilot.py [--refresh]
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

from lambda_ber_schema.loaders import MDRepoLoader

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/loaders/fixtures/mdrepo"
ENTRIES = {"MDR00020971": "apo", "MDR00021021": "ligand", "MDR00079393": "ensemble"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Fetch metadata only from the public API")
    args = parser.parse_args()
    loader = MDRepoLoader()
    manifest_path = FIXTURES / "manifest.json"
    previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    manifest = {"source": "MDRepo", "license": "CC-BY-4.0", "payloads_downloaded": False, "entries": []}
    for slug, case in ENTRIES.items():
        path = FIXTURES / f"{slug}.json"
        if args.refresh:
            result = loader.load(slug)
            path.write_text(json.dumps(result.raw_data, indent=2) + "\n")
            fetched = datetime.now(timezone.utc).isoformat()
        else:
            result = loader.convert(json.loads(path.read_text()))
            fetched = next((e["retrieved_at"] for e in previous.get("entries", []) if e["id"] == slug), None)
        data = result.dataset.model_dump(mode="json", exclude_none=True)
        output = ROOT / f"tests/data/valid/Dataset-mdrepo-{case}.yaml"
        output.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
        manifest["entries"].append({
            "id": slug, "case": case, "retrieved_at": fetched,
            "source_url": result.source_url,
            "api_url": f"{loader.base_url}/simulation_view/{int(slug[3:])}",
            "snapshot_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "output": str(output.relative_to(ROOT)),
            "counts": {key: len(data.get(key, [])) for key in (
                "proteins", "small_molecules", "sample_components", "workflow_runs", "data_files")},
            "warnings": result.warnings,
        })
        print(f"{slug}: {len(data['data_files'])} file records -> {output.relative_to(ROOT)}")
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
