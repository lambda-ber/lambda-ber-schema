# NSLS2-BER-LAMBDA Integration

## Overview

This document describes the integration of metadata mappings from the NSLS2-BER-LAMBDA project into lambda-ber-schema. The integration extends the schema to comprehensively support X-ray crystallography workflows with detailed mappings to CBF diffraction images, PDB/mmCIF depositions, and Excel metadata templates.

## Integration Summary

### 1. Namespace Addition

Added `nsls2` prefix to the schema:
- **Prefix**: `nsls2`
- **Expansion**: `https://github.com/NSLS2/BER-LAMBDA/`
- **Purpose**: Provides semantic URIs for NSLS2 metadata field mappings

### 2. Extended Classes

#### ExperimentRun Extensions

Added X-ray crystallography-specific data collection fields with NSLS2 mappings:

| Field | Type | Maps to CBF | Maps to PDB | NSLS2 Slot URI |
|-------|------|-------------|-------------|----------------|
| `wavelength` | float | `Wavelength` | `_diffrn_radiation_wavelength.wavelength` | `nsls2:Wavelength` |
| `oscillation_angle` | float | `Angle_increment` | `_diffrn_scan.angle_increment` | `nsls2:Angle_increment` |
| `start_angle` | float | `Start_angle` | - | `nsls2:Start_angle` |
| `number_of_images` | integer | - | - | `nsls2:Number_of_images` |
| `beam_center_x` | float | `Beam_xy` (x) | `_diffrn_detector.beam_center_x` | `nsls2:Beam_xy_x` |
| `beam_center_y` | float | `Beam_xy` (y) | `_diffrn_detector.beam_center_y` | `nsls2:Beam_xy_y` |
| `detector_distance` | float | `Detector_distance` | `_diffrn_detector.distance` | `nsls2:Detector_distance` |
| `pixel_size_x` | float | `Pixel_size` | - | `nsls2:Pixel_size_x` |
| `pixel_size_y` | float | `Pixel_size` | - | `nsls2:Pixel_size_y` |
| `total_rotation` | float | - | - | `nsls2:Total_rotation_deg` |
| `beamline` | string | - | `_diffrn_source.beamline` | `nsls2:Beamline` |

#### WorkflowRun Extensions

Added crystallographic data processing and refinement fields:

**Data Processing Fields** (NSLS2 Data_Processing mapping):
- Unit cell parameters: `space_group`, `unit_cell_a`, `unit_cell_b`, `unit_cell_c`, `unit_cell_alpha`, `unit_cell_beta`, `unit_cell_gamma`
- Resolution limits: `resolution_high`, `resolution_low`
- Quality metrics: `rmerge`, `rpim`, `cc_half`, `completeness_percent`, `i_over_sigma`, `wilson_b_factor`, `multiplicity`

**Refinement Fields** (NSLS2 Refinement mapping):
- R-factors: `rwork`, `rfree`
- Geometry validation: `rmsd_bonds`, `rmsd_angles`
- Ramachandran statistics: `ramachandran_favored`, `ramachandran_outliers`
- Model quality: `clashscore`

#### Sample Extensions

Added NSLS2 Sample metadata fields:
- `protein_name` - Name of the protein (nsls2:Protein_Name)
- `construct` - Construct description (nsls2:Construct)
- `tag` - Affinity tag (nsls2:Tag)
- `mutations` - Mutations present (nsls2:Mutations)
- `expression_system` - Expression system used (nsls2:Expression_System)
- `ligand` - Bound ligand/small molecule (nsls2:Ligand)

#### XRayInstrument Extensions

Added detector and beamline identification:
- `detector_type` - Type of X-ray detector (nsls2:Detector)
- `beamline_id` - Beamline identifier (nsls2:Beamline)

#### XRayPreparation Extensions

Added mounting details:
- `loop_size` - Loop size in micrometers (nsls2:Loop_Size)
- `mounting_temperature` - Temperature during mounting (nsls2:Temperature)
- `mounting_method` - Crystal mounting method (nsls2:Mount_Type)

### 3. New Classes

#### CrystallizationConditions

A dedicated class for crystal growth conditions (NSLS2 Crystallization mapping):

| Field | Type | Maps to | NSLS2 Slot URI |
|-------|------|---------|----------------|
| `method` | CrystallizationMethodEnum | Spreadsheet: Method | `nsls2:Method` |
| `crystallization_conditions` | string | Spreadsheet: Conditions | `nsls2:Conditions` |
| `drop_volume` | float | Spreadsheet: Drop_Volume | `nsls2:Drop_Volume` |
| `protein_concentration` | float | Spreadsheet: Protein_Concentration | `nsls2:Protein_Concentration` |
| `crystal_size_um` | string | Spreadsheet: Crystal_Size | `nsls2:Crystal_Size` |
| `cryo_protectant` | string | Spreadsheet: Cryo_Protectant | `nsls2:Cryo_Protectant` |
| `crystal_id` | string | Spreadsheet: Crystal_ID | `nsls2:Crystal_ID` |

### 4. Enumeration Extensions

#### DetectorTypeEnum

Added X-ray crystallography detector types:
- `eiger` - Dectris EIGER detector (hybrid photon counting)
- `pilatus` - Dectris PILATUS detector
- `rayonix` - Rayonix CCD detector
- `adsc` - ADSC CCD detector
- `mar` - MAR CCD or imaging plate detector

#### FileFormatEnum

Added crystallography file formats:
- `cbf_zst` - Zstandard-compressed CBF format
- `img` - Generic diffraction image format
- `h5` - HDF5 format (alternative extension)
- `gz` - Gzip compressed format

## NSLS2 Metadata Category Mappings

The integration provides comprehensive mappings for all 11 NSLS2 metadata categories:

### 1. Project → Study
- Project_ID, PI, Institution → Study-level metadata

### 2. Sample → Sample
- Sample_Name, Protein_Name, Construct, Tag, Mutations
- Expression_System, Buffer, Ligand

### 3. Crystallization → CrystallizationConditions
- Method, Conditions, Drop_Volume, Protein_Concentration
- Crystal_Size, Cryo_Protectant, Crystal_ID

### 4. Mounting → XRayPreparation
- Loop_Size, Temperature, Mount_Type

### 5. Data_Collection → ExperimentRun
- Wavelength, Detector, Detector_distance, Beam_xy
- Exposure_time, Oscillation, Number_of_images, Start_angle
- Temperature, Beamline

### 6. Data_Processing → WorkflowRun
- Space_Group, Unit_Cell (a,b,c,α,β,γ)
- Resolution_High, Resolution_Low
- Completeness, Multiplicity, I/σ(I)
- CC½, Rmerge, Rpim, Wilson_B

### 7. PDB_Headers → Study/Sample metadata
- Standard PDB header information

### 8. Scaling → WorkflowRun (workflow_type: scaling)
- Program, Version, Anomalous flag

### 9. Refinement → WorkflowRun (workflow_type: refinement)
- Program, Resolution, Rwork/Rfree
- RMSD_bonds, RMSD_angles
- Ramachandran statistics, Clashscore

### 10. Deposition → WorkflowRun
- PDB_ID, deposited_to_pdb

### 11. Files → DataFile
- Raw_Data_Path, Processed_Data_Path, PDB_File, MTZ_File

## Example Usage

A comprehensive example dataset based on PDB entry 9B7F is provided in `examples/Dataset-nsls2-9B7F.yaml`. This example demonstrates:

1. **Complete X-ray crystallography workflow** from crystallization to structure deposition
2. **NSLS-II FMX beamline** instrument configuration with EIGER detector
3. **Full data collection parameters** with wavelength, oscillation, beam center, etc.
4. **Multi-stage processing pipeline**:
   - Data integration (XDS)
   - Scaling (AIMLESS)
   - Phasing (Phaser - molecular replacement)
   - Refinement (PHENIX.REFINE)
5. **Quality metrics** at each stage with space group, unit cell, R-factors, validation statistics

### Key Features Demonstrated

```yaml
instrument_runs:
  - experiment_code: "FMX-2024-11-9B7F"
    technique: xray_crystallography
    # NSLS2 Data_Collection fields with mappings
    wavelength: 1.653123  # nsls2:Wavelength → CBF + PDB
    oscillation_angle: 0.4  # nsls2:Angle_increment
    beam_center_x: 785.50  # nsls2:Beam_xy_x
    beam_center_y: 783.40  # nsls2:Beam_xy_y
    detector_distance: 100.003  # nsls2:Detector_distance
    beamline: "FMX"  # nsls2:Beamline

workflow_runs:
  - workflow_type: refinement
    # NSLS2 Data_Processing + Refinement fields
    space_group: "P 21 21 21"  # nsls2:Space_Group
    unit_cell_a: 52.3  # nsls2:Unit_Cell_a
    resolution_high: 1.8  # nsls2:Resolution_High_A
    rwork: 0.178  # nsls2:Rwork
    rfree: 0.203  # nsls2:Rfree
    ramachandran_favored: 97.5  # nsls2:Ramachandran_Favored
    clashscore: 4.5  # nsls2:Clashscore
```

## Validation

All extensions have been validated:
- ✅ Schema successfully regenerates with `make gen-project`
- ✅ New example validates with `linkml-validate`
- ✅ All existing examples continue to validate
- ✅ Full test suite passes with `make test`

## Benefits

1. **Bidirectional mapping**: NSLS2 metadata can be extracted from CBF/PDB files and mapped to lambda-ber-schema, or lambda-ber-schema data can be exported in NSLS2 formats

2. **Semantic annotations**: All new fields include `slot_uri` mappings to the nsls2 namespace and comments documenting CBF/PDB field mappings

3. **Backward compatible**: All changes are additive; existing schema usage remains unchanged

4. **Comprehensive coverage**: Supports complete X-ray crystallography pipeline from sample preparation through structure deposition

5. **Standards-compliant**: Aligns with PDB mmCIF standards and CBF format specifications

## Integration with NSLS2-BER-LAMBDA

The NSLS2-BER-LAMBDA repository can now use lambda-ber-schema as its output format:

```python
# Pseudocode integration
from lambda_ber_schema import Dataset, ExperimentRun, WorkflowRun
from nsls2_lambda.metadata import parse_cbf, parse_cif, parse_spreadsheet

# Extract metadata from NSLS2 sources
cbf_metadata = parse_cbf("lyso_7500eV.cbf.zst")
pdb_metadata = parse_cif("9B7F.cif")
spreadsheet_metadata = parse_spreadsheet("mx_metadata_template.xlsx")

# Create lambda-ber-schema objects
experiment = ExperimentRun(
    experiment_code="FMX-2024-001",
    wavelength=cbf_metadata['Wavelength'],
    beam_center_x=cbf_metadata['Beam_xy'][0],
    detector_distance=cbf_metadata['Detector_distance'],
    # ... map all fields
)

workflow = WorkflowRun(
    workflow_code="REFINEMENT-001",
    space_group=pdb_metadata['_symmetry.space_group_name_h-m'],
    unit_cell_a=pdb_metadata['_cell.length_a'],
    rwork=pdb_metadata['_refine.ls_R_factor_R_work'],
    # ... map all fields
)

# Validate and export
dataset = Dataset(studies=[Study(instrument_runs=[experiment], workflow_runs=[workflow])])
dataset.validate()  # LinkML validation
dataset.export("dataset.yaml")  # or .json, .ttl, etc.
```

## Future Enhancements

Potential future additions:
1. Add more beamline-specific fields (energy scans, MAD phasing data)
2. Extend to support micro-ED (microcrystal electron diffraction)
3. Add serial crystallography (SSX, SFX) specific fields
4. Create automated converters between NSLS2 spreadsheets and lambda-ber-schema
5. Integration with PDB deposition APIs

## References

- NSLS2-BER-LAMBDA: https://github.com/NSLS2/BER-LAMBDA
- lambda-ber-schema: https://w3id.org/lambda-ber-schema/
- PDB mmCIF dictionary: https://mmcif.wwpdb.org/
- CBF/imgCIF specification: https://www.iucr.org/resources/cif/spec/version1.1
- NSLS-II FMX beamline: https://www.bnl.gov/ps/fmx.php

## Contact

For questions about this integration:
- lambda-ber-schema: See repository documentation
- NSLS2-BER-LAMBDA: Contact Shekar V (vshekar1@bnl.gov)
- NSLS-II beamlines: Contact Jean Jakoncic (jjakoncic@bnl.gov)
