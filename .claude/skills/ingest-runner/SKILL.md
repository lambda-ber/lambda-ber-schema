---
name: ingest-runner
description: Run ETL data ingestion pipelines for structural biology sources (PDB, SASBDB, SimpleScattering, EMSL, SSRL MX snapshots, ANL LAMBDA). Use when asked to load, dump, or ingest data from an external source such as the Protein Data Bank or the Argonne LIMS. Handles batch operations, progress monitoring, cache management, API keys, and safe cleanup.
---

# Ingest Runner

Run ETL pipelines to load structural biology data from external databases into lambda-ber-schema format.

## Available Sources

| Source | Command | Data | Needs |
|--------|---------|------|-------|
| PDB | `just pdb-*` | Protein Data Bank (~248k structures) | nothing |
| SASBDB | `just sasbdb-*` | Small Angle Scattering (~2k entries) | nothing |
| SimpleScattering | `just simplescattering-*` | SAXS datasets from simplescattering.com | nothing |
| EMSL | `just emsl-load`, `just emsl-list` | EMSL datasets by sample query | JWT token (`--token`) |
| SSRL MX | `just ssrlmx-*` | Beamline snapshot directories on disk | snapshot files, no API |
| ANL LAMBDA | `just anllambda-*` | Argonne SBC MX experiments and the LIMS export | API key (see below) |

PDB, SASBDB, SimpleScattering and ANL LAMBDA share the batch dump machinery
described here (`*-dump-start`, `*-dump-status`, `*-clean*`). EMSL and SSRL MX
have single-shot recipes only.

## Quick Reference

```bash
# Single entry
just pdb-load 1HHO
just sasbdb-load SASDA52
just simplescattering-load xsbhevph
just anllambda-load e22fc16d-4e38-43f3-ad9b-50eea6b8ac69
just anllambda-lims          # the whole LIMS export as one Dataset

# Full dump (runs in background)
just pdb-dump-start          # PDB: 2 req/sec, ~46 hours without cache
just sasbdb-dump-start       # SASBDB: 2 req/sec, ~42 min (~5k entries)
just simplescattering-dump-start
just anllambda-dump-start    # ANL: 2 req/sec, ~50 experiments with images

# Fast mode (use when cache exists)
just pdb-dump-start-fast               # 5 req/sec
just sasbdb-dump-start-fast            # 5 req/sec
just simplescattering-dump-start-fast  # 5 req/sec

# Monitor
just pdb-dump-status
just sasbdb-dump-status
just anllambda-dump-status

# Stop
just pdb-dump-stop
just sasbdb-dump-stop
just anllambda-dump-stop
```

## ANL LAMBDA

The Structural Biology Center at Argonne serves its LIMS through the LAMBDA API
(https://sg.bio.anl.gov/lambda). Every call needs an API key, exchanged for an
hour-long session token. The key is read from, in order:

1. `--api-key` on the command line (avoid: it lands in shell history)
2. `ANL_LAMBDA_API_KEY` environment variable
3. `--api-key-file PATH`
4. `ANL_LAMBDA_API_KEY_FILE` environment variable
5. `./anl_lambda_token` in the working directory (gitignored)

Keep the key in `./anl_lambda_token`. Never commit it, never paste it into a
command, never echo it into a log. The session token is never written to the
response cache.

Two views of the same database are served:

| View | Command | Output |
|------|---------|--------|
| One MX experiment | `just anllambda-load UUID` | one Dataset: sample, protein, constructs, three preparations, run, frames, structure |
| Every MX experiment with images | `just anllambda-dump-start` | one YAML per experiment in `data/anl_lambda_dump/` |
| Whole LIMS export | `just anllambda-lims` | `data/anl_lambda_dump/lims_dataset.yaml`, a single Dataset |

Find uuids with `just anllambda-list` or `just anllambda-list kinase` (protein
name, partial match). The CLI also takes `--pi-name`.

Ids from both views join: the same experiment, sample, preparation and workflow
rows carry the same `anl-lambda:` ids whichever way they were loaded.

Two flags matter for batch runs:

- `--no-files` skips the per-frame DataFile rows. The default fetches every
  diffraction frame; an experiment with thousands of frames takes a while.
- The loader prints warnings for things it repaired or could not: repeated
  workflow rows, a species label with nowhere to go, culture volumes the LIMS
  records in mL but labels in L, target columns that disagree in length. Read
  them; they are the honest part of the output.

Errors: a 401 on the key exchange means the key is bad. A 404 means the uuid is
unknown or not visible to this key. Both exit with code 2 from the CLI; other
HTTP failures exit 1.

## Batch Dump Workflow

### Start a dump

```bash
just pdb-dump-start              # PDB (~248k entries, ~46 hours)
just sasbdb-dump-start           # SASBDB (~5k entries, ~42 min)
just simplescattering-dump-start
just anllambda-dump-start        # ANL LAMBDA (~50 experiments)
```

Creates in `data/{source}_dump/`:
- `*.yaml` - One file per entry
- `.cache/` - Cached API responses (preserve this!)
- `progress.json` - Tracks completed/failed entries
- `output.log` - Runtime log

### Monitor progress

```bash
just pdb-dump-status
just sasbdb-dump-status
just simplescattering-dump-status
just anllambda-dump-status
```

### Resume after interruption

Just run start again - it skips completed entries:

```bash
just pdb-dump-start
just sasbdb-dump-start
just anllambda-dump-start
```

### Retry failed entries

```bash
just pdb-dump-retry
just sasbdb-dump-retry
just simplescattering-dump-retry
just anllambda-dump-retry
```

## Cache System

API responses are cached in `.cache/` directories. This is critical for:
- Resuming interrupted dumps
- Re-processing with updated code
- Avoiding redundant API calls

Cache TTL: 7 days for batch operations.

### Check cache

```bash
just pdb-cache-info
```

## Clean Operations

**IMPORTANT:** Default clean operations preserve the cache.

| Command | Deletes | Preserves |
|---------|---------|-----------|
| `just {source}-clean` | Output YAML files | Cache + progress |
| `just {source}-clean-progress` | Output + progress | Cache |
| `just {source}-realclean` | Prints warning only | Everything |

Where `{source}` is `pdb`, `sasbdb`, `simplescattering` or `anllambda`.
SSRL MX has `ssrlmx-clean` and `ssrlmx-realclean` only; it keeps no cache.

### Re-process with updated code

```bash
just sasbdb-dump-stop
just sasbdb-clean-progress   # Keeps cache!
just sasbdb-dump-start-fast  # Uses cached responses
```

### Full reset (dangerous)

Only do this if cache is corrupted or you need fresh data:

```bash
just sasbdb-dump-stop
rm -rf data/sasbdb_dump && mkdir -p data/sasbdb_dump
just sasbdb-dump-start
```

## Output Format

A PDB entry becomes one Dataset holding the deposited specimen as a single Sample, with a
SampleComponent per entity (proteins, nucleic acids, ligands, ions, glycans) and
SampleComponentInteraction rows for the contacts RCSB reports: which chain binds which
(from the assembly's interfaces) and which chain each ligand or glycan sits on. Around it:

- Protein rows keyed by UniProt CURIE, or `pdb:<entry>/protein/<entity>` for chains with no
  UniProt entry (antibodies, nanobodies, designed proteins); ProteinConstruct rows with the
  deposited sequence; SmallMolecule rows from the Chemical Component Dictionary
- Expression, crystallization and EM grid preparations
- One ExperimentRun per diffraction experiment, EM imaging session, NMR experiment or
  scattering experiment, each with its instrument (XRay, CryoEM, NMR or SAXS)
- WorkflowRuns for each processing stage the entry records (data reduction, scaling with
  resolution shells, phasing, refinement, CTF, particle picking, reconstruction, model
  fitting, validation), with their software
- People, funders, publications, archive cross-references (EMDB, BMRB, ...)
- Data files: coordinates, structure factors, NMR restraints and shifts, EMDB maps,
  the validation report, raw data sets the entry cites

Where every field RCSB returns goes is set in
`src/lambda_ber_schema/loaders/pdb_field_map.yaml`; `tests/loaders/test_pdb_coverage.py`
fails if any field is unclassified or a field marked as carried is missing from the output.
Values with no named slot go to `additional_metrics` / `additional_properties`, keyed by
their mmCIF item (`mmCIF:_refine.B_iso_max`).

Example:
```yaml
sample_components:
  - id: pdb:7ZYI/component/6
    title: GLYCOCHENODEOXYCHOLIC ACID
    sample_id: pdb:7ZYI/sample
    component_type: small_molecule
    small_molecule_id: CHEBI:36274
    role: ligand
    copy_number: 2
sample_component_interactions:
  - sample_id: pdb:7ZYI/sample
    subject_id: pdb:7ZYI/component/6
    object_id: pdb:7ZYI/component/1
    interaction_type: binds
    interaction_status: observed
```

## Troubleshooting

### Dump not progressing

Check if process is running:
```bash
pgrep -f "dump-pdb"
pgrep -f "dump-sasbdb"
pgrep -f "dump-simplescattering"
pgrep -f "dump-anl-lambda"
```

Check log for errors:
```bash
tail -50 data/pdb_dump/output.log
tail -50 data/sasbdb_dump/output.log
tail -50 data/anl_lambda_dump/output.log
```

### ANL LAMBDA says there is no API key

The CLI names every place it looked. Put the key in `./anl_lambda_token` in the
directory you run from, or export `ANL_LAMBDA_API_KEY`. Do not pass the key on
the command line to work around it.

### Rate limiting

If getting 429 errors, reduce rate:
```bash
just sasbdb-dump-stop
# Edit etl.justfile to use --rate 1
just sasbdb-dump-start
```

### Cache too old

Cache entries expire after 7 days. If data is stale:
```bash
just sasbdb-realclean  # Follow instructions
```
