---
name: ingest-runner
description: Run ETL data ingestion pipelines for structural biology databases (PDB, SASBDB). Use when asked to load, dump, or ingest data from external sources like Protein Data Bank. Handles batch operations, progress monitoring, cache management, and safe cleanup.
---

# Ingest Runner

Run ETL pipelines to load structural biology data from external databases into lambda-ber-schema format.

## Available Sources

| Source | Command | Data |
|--------|---------|------|
| PDB | `just pdb-*` | Protein Data Bank (~248k structures) |
| SASBDB | `just sasbdb-*` | Small Angle Scattering (~2k entries) |

## Quick Reference

```bash
# Single entry
just pdb-load 1HHO
just sasbdb-load SASDA52

# Full dump (runs in background)
just pdb-dump-start          # PDB: 2 req/sec, ~46 hours without cache
just sasbdb-dump-start       # SASBDB: 2 req/sec, ~42 min (~5k entries)

# Fast mode (use when cache exists)
just pdb-dump-start-fast     # 5 req/sec
just sasbdb-dump-start-fast  # 5 req/sec

# Monitor
just pdb-dump-status
just sasbdb-dump-status

# Stop
just pdb-dump-stop
just sasbdb-dump-stop
```

## Batch Dump Workflow

### Start a dump

```bash
just pdb-dump-start      # PDB (~248k entries, ~46 hours)
just sasbdb-dump-start   # SASBDB (~5k entries, ~42 min)
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
```

### Resume after interruption

Just run start again - it skips completed entries:

```bash
just pdb-dump-start
just sasbdb-dump-start
```

### Retry failed entries

```bash
just pdb-dump-retry
just sasbdb-dump-retry
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

Where `{source}` is `pdb` or `sasbdb`.

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

Each entry produces a YAML file with:
- Sample info with UniProt cross-references
- Experiment run with quality metrics
- Instrument details
- Workflow runs (refinement)
- Data files (PDB, mmCIF, structure factors)

Example:
```yaml
samples:
  - id: pdb:1HHO/sample/1
    sample_type: protein
    protein_name: Hemoglobin subunit alpha
    organism: Homo sapiens
    database_cross_references:
      - database_name: uniprot
        database_id: P69905
        database_url: https://www.uniprot.org/uniprotkb/P69905
```

## Troubleshooting

### Dump not progressing

Check if process is running:
```bash
pgrep -f "dump-pdb"
pgrep -f "dump-sasbdb"
```

Check log for errors:
```bash
tail -50 data/pdb_dump/output.log
tail -50 data/sasbdb_dump/output.log
```

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
