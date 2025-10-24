# Enum: FileFormatEnum 




_File formats_



URI: [lambdaber:FileFormatEnum](https://w3id.org/lambda-ber-schema/FileFormatEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| mrc | None | MRC format for EM data |
| tiff | None | TIFF image format |
| hdf5 | None | HDF5 hierarchical data format |
| star | None | STAR format for metadata |
| pdb | None | PDB coordinate format |
| mmcif | None | mmCIF format |
| mtz | None | MTZ reflection format |
| cbf | None | Crystallographic Binary Format |
| ascii | None | ASCII text format |
| thermo_raw | None | Thermo Fisher RAW format |
| zip | None | ZIP compressed archive |




## Slots

| Name | Description |
| ---  | --- |
| [file_format](file_format.md) | File format |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: FileFormatEnum
description: File formats
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  mrc:
    text: mrc
    description: MRC format for EM data
  tiff:
    text: tiff
    description: TIFF image format
  hdf5:
    text: hdf5
    description: HDF5 hierarchical data format
  star:
    text: star
    description: STAR format for metadata
  pdb:
    text: pdb
    description: PDB coordinate format
  mmcif:
    text: mmcif
    description: mmCIF format
  mtz:
    text: mtz
    description: MTZ reflection format
  cbf:
    text: cbf
    description: Crystallographic Binary Format
  ascii:
    text: ascii
    description: ASCII text format
  thermo_raw:
    text: thermo_raw
    description: Thermo Fisher RAW format
  zip:
    text: zip
    description: ZIP compressed archive

```
</details>