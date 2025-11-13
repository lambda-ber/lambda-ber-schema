# Raw Data Files

This directory contains raw or source data files used for testing and validation of the lambda-ber-schema, particularly for demonstrating metadata extraction and mapping from real experimental data.

## Files

### 9B7F.cif

**Source**: NSLS2-BER-LAMBDA repository (`BNL/data/MX/Bin2Sum2Hcomp24_pdb/9B7F.cif`)

**Format**: mmCIF (Macromolecular Crystallographic Information File)

**Description**: Crystal structure deposited in the Protein Data Bank (PDB entry 9B7F). This structure was collected at NSLS-II and serves as a reference example for demonstrating NSLS2-BER-LAMBDA metadata integration with lambda-ber-schema.

**Key Metadata**:
- **Space Group**: P 43 21 2
- **Unit Cell**: a=78.895 Å, b=78.895 Å, c=36.955 Å (tetragonal)
- **Resolution**: 1.64 Å
- **Wavelength**: 1.65 Å
- **Detector**: DECTRIS EIGER X 9M
- **Collection Date**: 2023-11-15
- **R-work**: 0.1592 (15.92%)
- **R-free**: 0.1975 (19.75%)
- **Completeness**: 88.9%
- **Reflections**: 13,089 observed

**Contact**: Jean Jakoncic (jjakoncic@bnl.gov) - NSLS-II beamline scientist

**Related Files**:
- Example dataset: `examples/Dataset-nsls2-9B7F.yaml` - lambda-ber-schema representation of this structure's metadata
- Integration documentation: `docs/nsls2-integration.md`

## Purpose

These raw files serve multiple purposes:

1. **Validation**: Verify that lambda-ber-schema can accurately represent real experimental data
2. **Metadata Extraction**: Test tools that extract metadata from CBF/mmCIF files into lambda-ber-schema format
3. **Mapping Verification**: Confirm that NSLS2 metadata field mappings are correct and complete
4. **Examples**: Provide real-world examples for users implementing converters or parsers
5. **Testing**: Support automated testing of metadata extraction pipelines

## Usage

### Extract Metadata with Python

```python
from gemmi import cif

# Parse mmCIF file
doc = cif.read("tests/data/raw/9B7F.cif")
block = doc.sole_block()

# Extract key metadata
wavelength = block.find_value("_diffrn_radiation_wavelength.wavelength")
space_group = block.find_value("_symmetry.space_group_name_H-M")
resolution = block.find_value("_reflns.d_resolution_high")
rwork = block.find_value("_refine.ls_R_factor_R_work")

print(f"Wavelength: {wavelength} Å")
print(f"Space Group: {space_group}")
print(f"Resolution: {resolution} Å")
print(f"R-work: {rwork}")
```

### Map to lambda-ber-schema

See `examples/Dataset-nsls2-9B7F.yaml` for a complete example of how this mmCIF data is represented in lambda-ber-schema format with full NSLS2 field mappings.

## Data Provenance

All data in this directory comes from publicly available sources or collaborating facilities:

- **9B7F.cif**: Public PDB entry, also available from NSLS2-BER-LAMBDA repository
- Original data collected at NSLS-II (National Synchrotron Light Source II), Brookhaven National Laboratory

## License

mmCIF files from the Protein Data Bank are available under CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. See https://www.rcsb.org/pages/usage-policy for details.

## Adding New Raw Data

When adding new raw data files to this directory:

1. Document the source and provenance
2. Include key metadata summary
3. Add contact information if available
4. Create corresponding example in `examples/` directory
5. Update this README
6. Ensure proper licensing/permissions for public repository

## References

- PDB Entry 9B7F: https://www.rcsb.org/structure/9B7F
- NSLS2-BER-LAMBDA: https://github.com/NSLS2/BER-LAMBDA
- mmCIF Format: https://mmcif.wwpdb.org/
- NSLS-II: https://www.bnl.gov/ps/
