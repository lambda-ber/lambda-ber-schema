# MDRepo metadata import pilot

The `MDRepoLoader` imports public molecular dynamics metadata into LAMBDA without
downloading trajectories, structures, or other simulation payloads. The pilot uses
three real API snapshots retrieved on 2026-11-06:

| Case | MDRepo entry | Protein | Ligand records | Replicates reported | File records |
| --- | --- | --- | ---: | ---: | ---: |
| Apo | [MDR00020971](https://mdrepo.org/explore/MDR00020971) | Tau-tubulin kinase 2, Q6IQ55 | 0 | 1 | 29 |
| Ligand complex | [MDR00021021](https://mdrepo.org/explore/MDR00021021) | JAK3, P52333 | 1 | 1 | 30 |
| Ensemble | [MDR00079393](https://mdrepo.org/explore/MDR00079393) | Aldose reductase, P15121 | 2 (ZST and NAP) | 5 | 16 |

## Run the import

```bash
# Fetch one entry's metadata and retain the original JSON alongside the dataset.
uv run lambda-ber-schema etl mdrepo --entry MDR00021021 \
  --output dataset.yaml --raw-output mdrepo-source.json

# Convert an archived response without network access.
uv run lambda-ber-schema etl mdrepo \
  --metadata tests/loaders/fixtures/mdrepo/MDR00021021.json \
  --output dataset.yaml

# Rebuild all three checked-in examples from their snapshots.
uv run python scripts/import_mdrepo_pilot.py

# Explicitly refresh those snapshots from the public API and rebuild the examples.
uv run python scripts/import_mdrepo_pilot.py --refresh
```

The examples are `tests/data/valid/Dataset-mdrepo-{apo,ligand,ensemble}.yaml`.
`tests/loaders/fixtures/mdrepo/manifest.json` records source URLs, retrieval timestamps,
SHA-256 hashes of the archived JSON, counts, and conversion warnings. These hashes
verify the metadata snapshots; they do not verify any remote payload.

Programmatic access follows the other repository loaders:

```python
from lambda_ber_schema.loaders import MDRepoLoader

loader = MDRepoLoader()
result = loader.load("MDR00021021")
dataset = result.dataset
source_json = result.raw_data
warnings = result.warnings

# Bounded public search, using MDRepo filter names.
entries = loader.list_entries(limit=10, matched_uniprot="P52333", has_ligand=True)
```

## Mapping and provenance

| Source information | LAMBDA representation |
| --- | --- |
| Collection | Study, with sample, experiment and workflow associations |
| Molecular system | Sample, explicitly described as a computational system |
| Simulation entry | ExperimentRun with technique `molecular_dynamics`, linked to one `md_production` WorkflowRun |
| Canonical UniProt identity and sequence | Protein with a `uniprot:` CURIE |
| Simulated sequence, chain order, terminal caps and alignments | JSON in ProteinConstruct and SampleComponent descriptions; sample association carries canonical residue range and copy count |
| Ligand structure | SmallMolecule with SMILES, InChI and InChIKey, linked through SampleComponent |
| Engine, temperature, timestep, water model | MDSimulationParameters, when supplied as structured values |
| Source force field text, replica count, publications, contributor, commands and other source parameters | JSON in WorkflowRun.processing_parameters |
| Uploaded and processed file inventories | DataFile with format, size, source group, and original source metadata |
| Uploaded topology/parameter input and trajectory output | WorkflowInputAssociation and WorkflowOutputAssociation |

The importer uses existing `lambda:` IDs for source-local objects. It never assigns
a UniProt canonical sequence from a simulated mutant sequence. In the ensemble
example those sequences differ; both are retained. Chains mapping to one canonical
protein are grouped for copy count, while their `chain_order` values are retained
even when labels repeat. Several distinct simulated sequences for one protein are
preserved on the component without choosing one construct. A polymer without a single
valid UniProt match gets a local protein identity and a warning.

MDRepo's `sampling_frequency` is a saved-frame interval in **nanoseconds**, despite
its name. The importer converts it to integration steps only when the timestep is
positive and the result integral. JAK3's 0.01 ns interval and 2 fs timestep become
5,000 steps. Duration maps to `duration_ns` only for an explicitly single-replicate
entry. The ensemble's 19.5 ns source duration is retained as source metadata: its
description specifies five replicas each covering 3.9 ns. The importer does not
create five fictitious workflow runs or assign the aggregate duration to each one.

The file-format enum adds `tpr`, `itp`, `mdp`, `cpt`, `edr`, `mdc`, `toml` and `png`.
Text files use the existing `ascii` value; `.tgz` and `.tar.gz` use `gz`, retaining
their full filenames. Every file in these three snapshots is represented.

## Deliberate limits

- `Sample` is currently defined for physical samples. Using it for the computational
  molecular system follows the existing MD example, but a dedicated computational-system
  model would make that distinction structural.
- MDRepo's force-field field can combine protein and ligand models. It remains intact
  in source parameters rather than being assigned to one model by guessing from text.
- Missing structured values remain missing. JAK3's description mentions TIP3P while
  `water_type` is null. Source descriptions are retained for later curation.
- Ligand names alone do not establish CCD identifiers, and co-occurrence does not
  establish binding. The pilot uses local ligand IDs and creates no interaction assertions.
- MDRepo supplies MD5 file hashes; `DataFile.checksum` specifies SHA-256. MD5 values
  remain explicitly named in file descriptions. No remote payload checksum is claimed.
- Processed derivatives have no exposed processing-run history. They remain linked to
  the simulation through `related_entity`, without invented producing workflows or
  executable download URLs. Unclear input/output roles remain unassigned.
- This pilot maps protein chains. Other polymer types and unrecognized file formats
  produce warnings and remain in the complete source JSON. RMSD/RMSF arrays likewise
  remain in source JSON; their file inventories are represented where present.

## Validation and sources

`uv run pytest tests/loaders/test_mdrepo.py` checks real fixtures, identity separation,
units, ensemble duration, copy counts, foreign keys, source preservation, API requests
and offline CLI behavior. `make test` regenerates schema assets and validates the
examples through LinkML, including JSON and RDF serialization and RO-Crate checks.

Source interfaces: [MDRepo API documentation](https://mdrepo.org/api/schema/swagger-ui/),
[FAQ and CC BY 4.0 contribution terms](https://mdrepo.org/faq), and
[nightly metadata archive](https://static.mdrepo.org/metadata/mdrepo-metadata-latest.tar.gz).
The pilot only requests three JSON endpoints; it does not download the full archive.
