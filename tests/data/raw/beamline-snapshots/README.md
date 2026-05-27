# Beamline Snapshots

Real DCSS state snapshots from SSRL MX beamlines, converted to JSON.

| File | Beamline | Sample | Notes |
|------|----------|--------|-------|
| `SA_x4_1_00001.json` | BL12-2 | SA_x4 (Ss_EXLX1 expansin) | Has sidecar metadata + processing results |
| `A48Br_1_00001.json` | BL9-2 | A48Br | Older snapshot, no current_port |
| `A78_x107_1_00001.json` | BL12-2 | A78_x107 | |
| `XA_x16_1_00001.json` | BL12-1 | XA_x16 | |

## Source

Generated from raw `.txt` snapshots in the `dcss-dump-json` project using:

```
python3 convert.py tests/fixtures/<NAME>_1_00001.txt -o <NAME>_1_00001.json
```

The raw `.txt` files are DCSS state dumps written by `saveSystemSnapshot` alongside
each collected dataset. The `convert.py` tool parses them using per-beamline
device type registries (`<beamline>.dat`).

## Usage

```
lambda-ber-schema etl ssrl-mx --snapshot tests/data/raw/beamline-snapshots/SA_x4_1_00001.json
```
