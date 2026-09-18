# TomoBabel / CETS metadata examples

Companion files for the [TomoBabel / CETS background page](../tomobabel-cets.md), inspected on 2026-09-17.

| File | Origin and scope |
| --- | --- |
| [minimal-cets.yaml](minimal-cets.yaml) | Authored synthetic CETS Dataset, validated against core commit `0c8c4e3c7a2885f29caba551ffcaacde45c00101`. Includes an image, coordinate frames, a point annotation, and a particle-map reference. File paths are fictional. Uses a corner origin, not the centered rigid-converter profile. |
| [empiar-12104-tomogram.excerpt.yaml](empiar-12104-tomogram.excerpt.yaml) | Selected fields from an upstream CETS JSON example. Source values are unchanged; the referenced tilt series is omitted. Includes a real public MRC URL. The full historical source lacks 50 tilt-image IDs required by current core. |
| [portal-10445.excerpt.yaml](portal-10445.excerpt.yaml) | Selected fields from recorded portal converter input. This is not a CETS document. Includes real image URLs and a GO membrane annotation. The selected image and annotation metadata describe different sampling grids. |
| [provenance.yaml](provenance.yaml) | Exact repository revisions, source URLs, source and excerpt checksums, and transformation descriptions. |
| [validation.txt](validation.txt) | Results of local metadata checks against the pinned CETS model. |

The excerpts are reading aids, not complete submission or conformance fixtures. No volume arrays were downloaded for this page. The upstream JSON files remain linked from the provenance manifest; authorship and broader experimental context should be obtained from those sources and their associated archives.

## Reading the synthetic example

The image has 4 Å sampling and a corner-origin physical frame. Its point at `[40, 80, 24]` Å therefore corresponds to array coordinates `[10, 20, 6]`. The particle map's `coord_index: 0` refers to that first point. Its name deliberately makes no biological identification.

The example was validated with the patched Pydantic `Dataset` model from `cets_data_model.models.models`, then serialized to JSON and loaded again. YAML parsing or Pydantic acceptance does not check all referenced files, graph relationships, or spatial conventions. The real-data excerpts must not be mistaken for independently validated, complete CETS documents.

## Reproducing the local example checks

From the LAMBDA repository root, create an isolated environment with the model revision and validation packages used for the checks. The distribution version is `cets_data_model==0.1.0`; the Git commit identifies the precise model snapshot. These commands use the committed patched model, so model generation is unnecessary.

```sh
uv venv --python 3.12.9 /tmp/cets-example-check
uv pip install --python /tmp/cets-example-check/bin/python \
  'cets_data_model @ git+https://github.com/TomoBabel/cets-data-models.git@0c8c4e3c7a2885f29caba551ffcaacde45c00101' \
  'pydantic==2.13.5' 'PyYAML==6.0.3'
```

Run the following to check all local YAML examples and their recorded checksums, then validate the synthetic Dataset and its JSON round-trip:

```sh
/tmp/cets-example-check/bin/python - <<'PY'
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path

import yaml
from cets_data_model.models.models import Dataset

root = Path('src/docs/background/tomobabel-cets-examples')
manifest = yaml.safe_load((root / 'provenance.yaml').read_text())
for name, expected in manifest['validation']['packages'].items():
    assert version(name) == expected, (name, version(name), expected)
for entry in manifest['examples']:
    payload = (root / entry['local']).read_bytes()
    assert len(payload) == entry['bytes'], entry['local']
    assert sha256(payload).hexdigest() == entry['sha256'], entry['local']
    yaml.safe_load(payload)
data = yaml.safe_load((root / 'minimal-cets.yaml').read_text())
model = Dataset.model_validate(data)
reloaded = Dataset.model_validate_json(model.model_dump_json())
assert model.model_dump() == reloaded.model_dump()
print('Local YAML/checksum checks and synthetic Dataset JSON round-trip: passed')
PY
```

This reproduces the local example checks in [validation.txt](validation.txt). The historical source comparisons and structural probes in that file are separate investigation results; the command above does not fetch their upstream fixtures or run those probes. The pinned source URLs and checksums are recorded in [provenance.yaml](provenance.yaml).
