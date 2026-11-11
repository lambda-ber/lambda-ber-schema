# Enum: FileFormatEnum 




_File formats_



URI: [lambda:FileFormatEnum](http://w3id.org/lambda/FileFormatEnum)

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
| cbf_zst | None | Zstandard-compressed CBF format |
| img | None | Generic diffraction image format |
| h5 | None | HDF5 format (alternative extension) |
| ascii | None | ASCII text format |
| thermo_raw | None | Thermo Fisher RAW format |
| zip | None | ZIP compressed archive |
| tar | None | TAR archive format |
| mrcs | None | MRC stack format for particle stacks |
| eer | None | EER format for electron counting |
| cs | None | CryoSPARC format |
| json | None | JSON data format |
| csv | None | Comma-separated values format |
| ccp4 | None | CCP4 map format |
| gz | None | Gzip compressed format |
| nmr_star | None | NMR-STAR format for NMR data (chemical shifts, restraints, sample conditions)... |
| yaml | None | YAML text format (e |
| mdoc | None | SerialEM autodoc metadata sidecar ( |
| nav | None | SerialEM navigator file ( |
| dm4 | None | Gatan DigitalMicrograph 4 image format ( |
| mol2 | None | Tripos MOL2 format for parameterized small molecules |
| sdf | None | Structure-Data File format for chemical structures |
| frcmod | None | Amber force field modification file |
| prmtop | None | Amber topology (parameter/topology) file |
| inpcrd | None | Amber initial coordinates file |
| rst7 | None | Amber restart file (ASCII coordinates/velocities) |
| netcdf | None | NetCDF trajectory format (Amber mdcrd binary) |
| dcd | None | DCD trajectory format (CHARMM/NAMD) |
| xtc | None | XTC compressed trajectory format (GROMACS) |
| trr | None | TRR full-precision trajectory format (GROMACS) |
| gro | None | GROMACS coordinate file format |
| top | None | GROMACS topology file format |
| tpr | None | GROMACS portable binary run input (topology and simulation parameters) |
| itp | None | GROMACS include topology file |
| mdp | None | GROMACS molecular dynamics parameter file |
| cpt | None | GROMACS checkpoint file |
| edr | None | GROMACS binary energy file |
| mdc | None | MDCompress compressed molecular dynamics trajectory |
| toml | None | TOML configuration or metadata file |
| png | None | Portable Network Graphics image |
| lib | None | Amber residue library file |




## Slots

| Name | Description |
| ---  | --- |
| [file_format](file_format.md) | File format |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: FileFormatEnum
description: File formats
from_schema: http://w3id.org/lambda/
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
  cbf_zst:
    text: cbf_zst
    description: Zstandard-compressed CBF format
  img:
    text: img
    description: Generic diffraction image format
  h5:
    text: h5
    description: HDF5 format (alternative extension)
  ascii:
    text: ascii
    description: ASCII text format
  thermo_raw:
    text: thermo_raw
    description: Thermo Fisher RAW format
  zip:
    text: zip
    description: ZIP compressed archive
  tar:
    text: tar
    description: TAR archive format
  mrcs:
    text: mrcs
    description: MRC stack format for particle stacks
  eer:
    text: eer
    description: EER format for electron counting
  cs:
    text: cs
    description: CryoSPARC format
  json:
    text: json
    description: JSON data format
  csv:
    text: csv
    description: Comma-separated values format
  ccp4:
    text: ccp4
    description: CCP4 map format
  gz:
    text: gz
    description: Gzip compressed format
  nmr_star:
    text: nmr_star
    description: NMR-STAR format for NMR data (chemical shifts, restraints, sample
      conditions), as distributed by BMRB
  yaml:
    text: yaml
    description: YAML text format (e.g., a facility acquisition protocol sheet)
  mdoc:
    text: mdoc
    description: 'SerialEM autodoc metadata sidecar (.mdoc): per-image or per-tile
      acquisition parameters for an MRC or TIFF file'
  nav:
    text: nav
    description: 'SerialEM navigator file (.nav): acquisition targets with stage coordinates
      and the maps they were picked from'
  dm4:
    text: dm4
    description: Gatan DigitalMicrograph 4 image format (.dm4), commonly used for
      K2/K3 gain references
  mol2:
    text: mol2
    description: Tripos MOL2 format for parameterized small molecules
  sdf:
    text: sdf
    description: Structure-Data File format for chemical structures
  frcmod:
    text: frcmod
    description: Amber force field modification file
  prmtop:
    text: prmtop
    description: Amber topology (parameter/topology) file
  inpcrd:
    text: inpcrd
    description: Amber initial coordinates file
  rst7:
    text: rst7
    description: Amber restart file (ASCII coordinates/velocities)
  netcdf:
    text: netcdf
    description: NetCDF trajectory format (Amber mdcrd binary)
    comments:
    - Standard binary trajectory format for Amber MD simulations
  dcd:
    text: dcd
    description: DCD trajectory format (CHARMM/NAMD)
  xtc:
    text: xtc
    description: XTC compressed trajectory format (GROMACS)
  trr:
    text: trr
    description: TRR full-precision trajectory format (GROMACS)
  gro:
    text: gro
    description: GROMACS coordinate file format
  top:
    text: top
    description: GROMACS topology file format
  tpr:
    text: tpr
    description: GROMACS portable binary run input (topology and simulation parameters)
  itp:
    text: itp
    description: GROMACS include topology file
  mdp:
    text: mdp
    description: GROMACS molecular dynamics parameter file
  cpt:
    text: cpt
    description: GROMACS checkpoint file
  edr:
    text: edr
    description: GROMACS binary energy file
  mdc:
    text: mdc
    description: MDCompress compressed molecular dynamics trajectory
  toml:
    text: toml
    description: TOML configuration or metadata file
  png:
    text: png
    description: Portable Network Graphics image
  lib:
    text: lib
    description: Amber residue library file

```
</details>