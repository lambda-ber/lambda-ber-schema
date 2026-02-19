# ============== ETL Data Ingestion Recipes ==============
# Use these recipes to load structural biology data from external sources.
#
# IMPORTANT: Clean operations preserve the API cache by default.
# Only `*-realclean` targets delete the cache (requires manual confirmation).

# Variables (RUN inherited from project.justfile)
pdb_dump_dir := "data/pdb_dump"
sasbdb_dump_dir := "data/sasbdb_dump"

# ============================================================================
# PDB (Protein Data Bank) Ingestion
# ============================================================================

# Load a single PDB entry (e.g., just pdb-load 1HHO)
[group('etl')]
pdb-load entry:
    uv run lambda-ber-schema etl pdb --entry {{entry}}

# List recent PDB entries
[group('etl')]
pdb-list:
    uv run lambda-ber-schema etl list pdb --limit 20

# Start full PDB dump (background, 2 req/sec) - ~46 hours without cache
[group('etl')]
pdb-dump-start:
    mkdir -p {{pdb_dump_dir}}
    @echo "Starting PDB dump to {{pdb_dump_dir}}"
    @echo "Monitor: just pdb-dump-status"
    @echo "Stop: just pdb-dump-stop"
    nohup uv run lambda-ber-schema etl dump-pdb --output-dir {{pdb_dump_dir}} --rate 2 > {{pdb_dump_dir}}/output.log 2>&1 &

# Start PDB dump fast (5 req/sec) - use when cache exists
[group('etl')]
pdb-dump-start-fast:
    mkdir -p {{pdb_dump_dir}}
    @echo "Starting fast PDB dump (using cache)"
    nohup uv run lambda-ber-schema etl dump-pdb --output-dir {{pdb_dump_dir}} --rate 5 > {{pdb_dump_dir}}/output.log 2>&1 &

# Check PDB dump status
[group('etl')]
pdb-dump-status:
    #!/usr/bin/env bash
    if pgrep -f "dump-pdb" > /dev/null; then echo "✓ Running"; else echo "✗ Not running"; fi
    tail -5 {{pdb_dump_dir}}/output.log 2>/dev/null || true
    if [ -f {{pdb_dump_dir}}/progress.json ]; then
      python3 -c "import json; d=json.load(open('{{pdb_dump_dir}}/progress.json')); print(f'Completed: {len(d[\"completed\"])} | Failed: {len(d[\"failed\"])}')"
    fi

# Stop PDB dump
[group('etl')]
pdb-dump-stop:
    pkill -f "dump-pdb" && echo "Stopped" || echo "Not running"

# Retry failed PDB entries
[group('etl')]
pdb-dump-retry:
    uv run lambda-ber-schema etl dump-pdb --output-dir {{pdb_dump_dir}} --retry-failed

# Show PDB cache info
[group('etl')]
pdb-cache-info:
    @du -sh {{pdb_dump_dir}}/.cache 2>/dev/null || echo "No cache"
    @find {{pdb_dump_dir}}/.cache -type f 2>/dev/null | wc -l | xargs echo "Files:" || true

# ============================================================================
# PDB Clean Targets - SAFE BY DEFAULT (preserves cache)
# ============================================================================

# Clean PDB output files (preserves cache + progress)
[group('etl-clean')]
pdb-clean:
    @echo "Cleaning output files (preserving cache + progress)"
    find {{pdb_dump_dir}} -maxdepth 1 -name "*.yaml" -type f -delete 2>/dev/null || true
    rm -f {{pdb_dump_dir}}/batch.log {{pdb_dump_dir}}/errors.log {{pdb_dump_dir}}/output.log

# Clean PDB output + reset progress (preserves cache)
[group('etl-clean')]
pdb-clean-progress:
    @echo "Cleaning output + progress (preserving cache)"
    find {{pdb_dump_dir}} -maxdepth 1 -name "*.yaml" -type f -delete 2>/dev/null || true
    rm -f {{pdb_dump_dir}}/progress.json {{pdb_dump_dir}}/batch.log {{pdb_dump_dir}}/errors.log {{pdb_dump_dir}}/output.log

# DANGEROUS: Delete everything including PDB cache
[group('etl-clean')]
pdb-realclean:
    @echo "⚠️  WARNING: This deletes the API cache (~24GB)"
    @echo "Re-fetching all PDB data takes ~46 hours!"
    @echo ""
    @echo "To confirm, manually run:"
    @echo "  rm -rf {{pdb_dump_dir}} && mkdir -p {{pdb_dump_dir}}"

# ============================================================================
# SASBDB (Small Angle Scattering) Ingestion
# ============================================================================

# Load a single SASBDB entry (e.g., just sasbdb-load SASDA52)
[group('etl')]
sasbdb-load entry:
    uv run lambda-ber-schema etl sasbdb --entry {{entry}}

# List SASBDB entries
[group('etl')]
sasbdb-list:
    uv run lambda-ber-schema etl list sasbdb --limit 20

# Start full SASBDB dump (background, 2 req/sec) - ~2k entries, ~30 min
[group('etl')]
sasbdb-dump-start:
    mkdir -p {{sasbdb_dump_dir}}
    @echo "Starting SASBDB dump to {{sasbdb_dump_dir}}"
    @echo "Monitor: just sasbdb-dump-status"
    @echo "Stop: just sasbdb-dump-stop"
    nohup uv run lambda-ber-schema etl dump-sasbdb --output-dir {{sasbdb_dump_dir}} --rate 2 > {{sasbdb_dump_dir}}/output.log 2>&1 &

# Start SASBDB dump fast (5 req/sec) - use when cache exists
[group('etl')]
sasbdb-dump-start-fast:
    mkdir -p {{sasbdb_dump_dir}}
    @echo "Starting fast SASBDB dump (using cache)"
    nohup uv run lambda-ber-schema etl dump-sasbdb --output-dir {{sasbdb_dump_dir}} --rate 5 > {{sasbdb_dump_dir}}/output.log 2>&1 &

# Check SASBDB dump status
[group('etl')]
sasbdb-dump-status:
    #!/usr/bin/env bash
    if pgrep -f "dump-sasbdb" > /dev/null; then echo "✓ Running"; else echo "✗ Not running"; fi
    tail -5 {{sasbdb_dump_dir}}/output.log 2>/dev/null || true
    if [ -f {{sasbdb_dump_dir}}/progress.json ]; then
      python3 -c "import json; d=json.load(open('{{sasbdb_dump_dir}}/progress.json')); print(f'Completed: {len(d[\"completed\"])} | Failed: {len(d[\"failed\"])}')"
    fi

# Stop SASBDB dump
[group('etl')]
sasbdb-dump-stop:
    pkill -f "dump-sasbdb" && echo "Stopped" || echo "Not running"

# Retry failed SASBDB entries
[group('etl')]
sasbdb-dump-retry:
    uv run lambda-ber-schema etl dump-sasbdb --output-dir {{sasbdb_dump_dir}} --retry-failed

# Show SASBDB cache info
[group('etl')]
sasbdb-cache-info:
    @du -sh {{sasbdb_dump_dir}}/.cache 2>/dev/null || echo "No cache"
    @find {{sasbdb_dump_dir}}/.cache -type f 2>/dev/null | wc -l | xargs echo "Files:" || true

# ============================================================================
# SASBDB Clean Targets - SAFE BY DEFAULT (preserves cache)
# ============================================================================

# Clean SASBDB output files (preserves cache + progress)
[group('etl-clean')]
sasbdb-clean:
    @echo "Cleaning output files (preserving cache + progress)"
    find {{sasbdb_dump_dir}} -maxdepth 1 -name "*.yaml" -type f -delete 2>/dev/null || true
    rm -f {{sasbdb_dump_dir}}/batch.log {{sasbdb_dump_dir}}/errors.log {{sasbdb_dump_dir}}/output.log

# Clean SASBDB output + reset progress (preserves cache)
[group('etl-clean')]
sasbdb-clean-progress:
    @echo "Cleaning output + progress (preserving cache)"
    find {{sasbdb_dump_dir}} -maxdepth 1 -name "*.yaml" -type f -delete 2>/dev/null || true
    rm -f {{sasbdb_dump_dir}}/progress.json {{sasbdb_dump_dir}}/batch.log {{sasbdb_dump_dir}}/errors.log {{sasbdb_dump_dir}}/output.log

# DANGEROUS: Delete everything including SASBDB cache
[group('etl-clean')]
sasbdb-realclean:
    @echo "⚠️  WARNING: This deletes the API cache"
    @echo ""
    @echo "To confirm, manually run:"
    @echo "  rm -rf {{sasbdb_dump_dir}} && mkdir -p {{sasbdb_dump_dir}}"
