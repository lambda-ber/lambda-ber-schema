# SimpleScattering GluRS Dataset Analysis

## Dataset Overview

**Source**: SimpleScattering.com  
**Dataset ID**: xsbhevph  
**URL**: https://simplescattering.com/open_dataset/xsbhevph  
**Title**: SEC-SAXS-MALS of Pseudomonas aeruginosa GluRS  

## Scientific Context

This dataset represents a comprehensive structural characterization of Glutamyl-tRNA synthetase (GluRS) from *Pseudomonas aeruginosa* using an integrated approach:

1. **SEC-SAXS**: Size Exclusion Chromatography coupled with Small Angle X-ray Scattering
2. **MALS**: Multi-Angle Light Scattering  
3. **Crystallography**: Complementary crystal structure (PDB: 8VC5)

**Scientific Goal**: Determine the oligomerization state of GluRS in solution

## Data Structure

### Raw Data
- **660 SEC-SAXS frames**: Individual scattering profiles collected during SEC elution
  - Format: ASCII text files with Q, I(Q), and Error columns
  - File pattern: `GluRS_1_00001.dat` to `GluRS_1_00660.dat`
  - Size: ~35 KB per frame
  - Total: 10.8 MB compressed

### Processed Data
- **Averaged profile**: `A_S_GluRS_1_5.dat` (107 KB)
  - Merged data from peak fractions
  - Q range: 0.0109 to 0.4729 Å⁻¹
  - 913 data points

### Structural Data
- **Crystal structure**: `8vc5.pdb` (1.3 MB)
  - Zinc-bound form of GluRS
  - Resolution data from crystallography
  - Deposited: 2023-12-13

## Technical Parameters

### Beamline Configuration
- **Facility**: Advanced Light Source (ALS)
- **Beamline**: SIBYLS BL12.3.1
- **Wavelength**: 1.127 Å (11 keV)
- **Detector**: Pilatus 3 2M
- **Sample-to-detector distance**: 2.1 m

### Data Collection
- **Technique**: SEC-SAXS with inline MALS
- **Frames**: 660 during elution
- **Q range**: 0.0109 - 0.4729 Å⁻¹
- **Temperature**: 20°C (standard)

## lambda-ber-schema Representation

### Key Design Decisions

1. **Dataset Structure**
   ```yaml
   Dataset
   └── Study: GluRS oligomerization
       ├── Sample: PA-GluRS protein
       ├── SamplePreparations: expression, purification, SEC-SAXS prep
       ├── ExperimentRun: SEC-SAXS-MALS collection
       ├── WorkflowRuns: SAXS processing, MALS analysis
       ├── DataFiles: frames, averaged data, structure, archive
       └── Images: chromatogram, Guinier plot
   ```

2. **Sample Tracking**
   - Linked UniProt ID (Q9XCL6) for sequence reference
   - Expression system details (E. coli BL21(DE3))
   - Buffer composition for reproducibility
   - Concentration and preparation methods

3. **Multi-technique Integration**
   - SEC-SAXS-MALS represented as single experiment run
   - Technique set to 'saxs' (primary method)
   - MALS processing as separate workflow
   - Crystal structure linked as complementary data

4. **Data Provenance**
   - All 660 frames referenced (example shown)
   - Processing parameters captured
   - Software versions documented
   - Compute resources tracked

### Schema Extensions Required

1. **FileFormatEnum**: Added `zip` for compressed archives
2. **Existing enums covered**:
   - `sec_saxs` collection mode (already added)
   - `saxs_analysis` workflow type (already added)
   - `ascii` file format (already added)

### Metadata Preservation

The lambda-ber-schema annotation preserves all critical metadata:
- Experimental conditions (wavelength, detector, distance)
- Processing parameters (Q range, buffer subtraction)
- Quality metrics (estimated Rg ~32.5 Å, I(0) ~45)
- Data lineage (raw frames → averaged profile)

## Comparison with Native Format

### SimpleScattering Format
- Web-based presentation
- Minimal structured metadata
- Files as separate downloads
- No formal schema

### lambda-ber-schema Advantages
1. **Structured metadata**: Machine-readable YAML/JSON
2. **Complete provenance**: Sample → Data → Analysis
3. **Validation**: LinkML schema ensures data integrity
4. **Integration ready**: Can combine with other techniques
5. **FAIR compliant**: Findable, Accessible, Interoperable, Reusable

## Use Cases Enabled

1. **Data Integration**
   - Combine SEC-SAXS with crystallography
   - Cross-reference with other GluRS studies
   - Meta-analysis across synthetases

2. **Reproducibility**
   - Complete experimental parameters
   - Processing workflow documented
   - Software versions tracked

3. **Machine Learning**
   - Structured data for training
   - Quality metrics for filtering
   - Multi-modal feature extraction

4. **Data Discovery**
   - Searchable by protein, technique, facility
   - Queryable quality metrics
   - Linked to public databases

## Recommendations

1. **For Data Providers**
   - Include buffer subtraction details
   - Provide Rg and Dmax values
   - Link to publications when available
   - Include MALS molecular weight results

2. **For Schema Development**
   - Consider adding MALS-specific fields
   - Add SEC parameters (column, flow rate)
   - Include data quality indicators
   - Support for time-resolved data

3. **For Users**
   - Validate oligomeric state claims
   - Compare solution vs crystal structures
   - Check for aggregation in SEC profile
   - Verify Guinier region linearity

## Conclusion

The SimpleScattering GluRS dataset demonstrates lambda-ber-schema's capability to:
- Capture complex multi-technique experiments
- Preserve all scientific metadata
- Enable data integration and reuse
- Support FAIR data principles

This annotation serves as a template for representing SEC-SAXS-MALS datasets from various sources in a standardized, interoperable format.