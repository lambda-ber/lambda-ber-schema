# lambda-ber-schema and EMPIAR Alignment Analysis

> **Note**: This document was generated using Claude (Anthropic's AI assistant) through automated analysis of documentation and web sources. While efforts have been made to ensure accuracy, there may be errors or outdated information. Please verify critical details with official EMPIAR documentation.

## Overview

This document provides a detailed analysis of the alignment between the lambda-ber-schema schema and EMPIAR (Electron Microscopy Public Image Archive), examining how lambda-ber-schema can integrate with and complement EMPIAR's role as the global repository for raw electron microscopy and related imaging data.

## Introduction to EMPIAR

### What is EMPIAR?

EMPIAR is the global public archive for raw electron microscopy images and related imaging data. Key characteristics:

- **Purpose**: Archive raw EM images underpinning 3D reconstructions
- **Content**: 2,385 entries, >6.24 PiB of data (as of 2025)
- **Scope**: Beyond EM - includes volume EM, X-ray tomography, CLEM
- **Access**: REST API, Aspera/Globus downloads, CC0 licensing
- **Integration**: Cross-references with EMDB, PDB, BioImage Archive

### Data Types Supported

EMPIAR has evolved beyond traditional cryo-EM to support:

1. **Single Particle Cryo-EM**
   - Movie stacks (multiframe micrographs)
   - Single frame micrographs
   - Particle stacks
   - Class averages

2. **Electron Tomography**
   - Tilt series
   - Tomograms
   - Subtomograms

3. **Volume EM Techniques**
   - FIB-SEM (Focused Ion Beam SEM)
   - SBF-SEM (Serial Block Face SEM)
   - Array tomography datasets

4. **X-ray Microscopy**
   - Soft X-ray tomography
   - Hard X-ray tomography
   - Cryo-soft X-ray data

5. **Correlative Microscopy**
   - CLEM (Correlative Light and Electron Microscopy)
   - Multimodal datasets
   - Aligned image stacks

### Current Status (2024-2025)

- **Growth**: Exponential data growth reaching petabyte scale
- **Expansion**: Support for volume EM and X-ray techniques
- **Integration**: Improved workflow uploads from Scipion
- **Standards**: JSON schema-based metadata model
- **Automation**: Header extraction from common formats

## EMPIAR Data Model

### JSON Schema Structure

EMPIAR uses a structured JSON schema for deposition metadata:

```json
{
  "admin": {
    "title": "Dataset title",
    "authors": [...],
    "references": [...]
  },
  "imagesets": [
    {
      "name": "Micrographs",
      "category": "T1",  // T1=single frame, T2=multiframe
      "format": "MRC",
      "dimensions": {
        "width": 5760,
        "height": 4092
      },
      "pixel_spacing": 0.85,
      "num_images": 8500
    }
  ],
  "specimen": {
    "cs": 2.7,
    "electron_dose": 40.0,
    "gain_reference": "..."
  }
}
```

### Image Categories

| Code | Category | lambda-ber-schema Equivalent |
|------|----------|---------------------|
| T1 | Micrographs - single frame | Image2D (single exposure) |
| T2 | Micrographs - multiframe | DataFile (movie stack) |
| T9 | Tilt series | DataFile (collection) |
| T10 | Class averages | DataFile (processed) |
| T13 | Reconstructed volumes | Image3D |
| T14 | Subtomograms | DataFile (extracted) |
| OT | Other | DataFile (generic) |

## lambda-ber-schema-EMPIAR Alignment

### Structural Mapping

| EMPIAR Concept | lambda-ber-schema Equivalent | Alignment Notes |
|----------------|---------------------|-----------------|
| **Entry** | **Study/Dataset** | Complete experimental dataset |
| **Imagesets** | **DataFile collections** | ✅ Groups of related images |
| **Admin metadata** | **Dataset attributes** | Title, authors, references |
| **Specimen info** | **Sample + ExperimentRun** | ✅ Sample and collection parameters |
| **Image metadata** | **Image attributes** | Dimensions, pixel size, format |
| **File hierarchy** | **DataFile.file_path** | Directory structure preservation |
| **Cross-references** | **external_ids** | ✅ EMDB, PDB, BioStudies links |

### Metadata Alignment

#### Sample and Specimen

**EMPIAR Specimen:**
```json
{
  "specimen": {
    "cs": 2.7,
    "electron_dose": 40.0,
    "gain_reference": "gain.mrc"
  }
}
```

**lambda-ber-schema Equivalent:**
```yaml
CryoEMInstrument:
  cs_corrector: true  # Cs value implies corrector
  
ExperimentRun:
  data_collection_strategy:
    total_dose: 40.0
    
DataFile:
  file_name: "gain.mrc"
  data_type: calibration
```

#### Imageset Organization

**EMPIAR Imagesets:**
```json
{
  "imagesets": [{
    "name": "Movies",
    "category": "T2",
    "format": "MRC",
    "num_images": 8500,
    "frames_per_image": 40
  }]
}
```

**lambda-ber-schema Equivalent:**
```yaml
DataFile:
  file_name: "movies.tar"
  file_format: mrc
  data_type: micrograph
  metadata:
    empiar_category: "T2"
    image_count: 8500
    frames_per_image: 40
```

## Key Differences and Complementarities

### 1. Raw Data Focus

**EMPIAR**: Specialized for raw data
- Optimized for large file storage
- Direct download infrastructure
- Minimal processing metadata

**lambda-ber-schema**: Workflow context
- Tracks processing history
- Links raw to processed data
- Captures parameter evolution

### 2. Multi-modal Support

**EMPIAR**: Expanding modality coverage
- Volume EM (FIB-SEM, SBF-SEM)
- X-ray tomography
- CLEM datasets

**lambda-ber-schema**: Unified multi-modal schema
- Native support for FTIR, fluorescence
- Integrated workflow across techniques
- Common metadata model

### 3. Access Patterns

**EMPIAR**: Bulk data access
- Aspera/Globus for large transfers
- REST API for metadata
- Volume Browser for visualization

**lambda-ber-schema**: Metadata-centric access
- Query by workflow stage
- Sample lineage tracking
- Processing parameter search

## Integration Strategies

### lambda-ber-schema → EMPIAR Deposition

```python
def prepare_empiar_deposition(study):
    """Generate EMPIAR JSON from lambda-ber-schema study"""
    empiar_json = {
        "admin": {
            "title": study.title,
            "authors": extract_authors(study),
            "references": extract_publications(study)
        },
        "imagesets": [],
        "specimen": {}
    }
    
    # Map DataFiles to imagesets
    for data_file in study.data_files:
        if data_file.data_type in ['micrograph', 'tilt_series']:
            imageset = {
                "name": data_file.file_name,
                "category": map_to_empiar_category(data_file),
                "format": data_file.file_format.upper(),
                "num_images": data_file.metadata.get('image_count')
            }
            empiar_json["imagesets"].append(imageset)
    
    # Extract specimen parameters
    for exp_run in study.experiment_runs:
        if exp_run.technique == 'cryo_em':
            empiar_json["specimen"]["electron_dose"] = exp_run.data_collection_strategy.total_dose
    
    return empiar_json
```

### EMPIAR → lambda-ber-schema Import

```yaml
# lambda-ber-schema representation of EMPIAR entry
Study:
  title: "Imported from EMPIAR-12345"
  
  data_files:
    - file_name: "micrographs/"
      file_format: mrc
      data_type: micrograph
      file_size_bytes: 5400000000000
      external_ids:
        empiar_id: "EMPIAR-12345"
      metadata:
        empiar_category: "T2"
        image_count: 8500
        download_method: "aspera"
        
  experiment_runs:
    - technique: cryo_em
      quality_metrics:
        completeness: 100  # All raw data present
```

## Advanced Integration Features

### 1. Volume EM Support

lambda-ber-schema can track volume EM workflows:

```yaml
ExperimentRun:
  technique: volume_em
  metadata:
    modality: "FIB-SEM"
    slice_thickness: 5.0  # nm
    volume_dimensions: [1000, 1000, 500]  # voxels
    
DataFile:
  data_type: volume_em_stack
  external_ids:
    empiar_id: "EMPIAR-11000"
```

### 2. Correlative Microscopy

Track CLEM experiments:

```yaml
Study:
  title: "Correlative light and electron microscopy"
  
  experiment_runs:
    - technique: fluorescence
      instrument_id: "light_microscope_001"
    - technique: cryo_em
      instrument_id: "titan_krios_001"
      
  data_files:
    - data_type: clem_registration
      metadata:
        alignment_method: "CLEM-Reg"
        modalities: ["fluorescence", "cryo_em"]
```

### 3. X-ray Tomography

Support for soft X-ray data:

```yaml
ExperimentRun:
  technique: soft_xray_tomography
  instrument_id: "synchrotron_beamline"
  
DataFile:
  data_type: xray_tomogram
  external_ids:
    empiar_id: "EMPIAR-11500"
```

## REST API Integration

### Accessing EMPIAR from lambda-ber-schema

```python
import requests

class EMPIARConnector:
    """Connect lambda-ber-schema to EMPIAR REST API"""
    
    BASE_URL = "https://www.ebi.ac.uk/empiar/api"
    
    def get_entry_metadata(self, empiar_id):
        """Retrieve EMPIAR entry metadata"""
        response = requests.get(f"{self.BASE_URL}/entry/{empiar_id}")
        return response.json()
    
    def check_entry_status(self, empiar_id):
        """Verify entry release status"""
        response = requests.get(
            f"{self.BASE_URL}/entry_status/{empiar_id}"
        )
        return response.json()
    
    def get_emdb_linked_entries(self, emdb_id):
        """Find EMPIAR entries for EMDB map"""
        response = requests.get(
            f"{self.BASE_URL}/search/emdb_id/{emdb_id}"
        )
        return response.json()
```

## Recommended Workflow

### 1. Data Collection Phase
```
lambda-ber-schema: Track samples, instruments, parameters
         ↓
   Collect raw data (movies, micrographs)
         ↓
   Store locally with lambda-ber-schema metadata
```

### 2. Processing Phase
```
lambda-ber-schema: Document processing workflows
         ↓
   Generate processed data
         ↓
   Track quality metrics
```

### 3. Deposition Preparation
```
lambda-ber-schema: Organize raw data for EMPIAR
         ↓
   Generate EMPIAR JSON metadata
         ↓
   Prepare data hierarchy
```

### 4. Archive Submission
```
EMPIAR: Deposit raw data
EMDB: Deposit 3D maps
PDB: Deposit atomic models
         ↓
   Update lambda-ber-schema with accession IDs
```

### 5. Public Access
```
lambda-ber-schema: Maintain complete workflow record
EMPIAR: Serve raw data to community
         ↓
   Enable reprocessing and validation
```

## Future Opportunities

### Technical Developments

1. **Automated Deposition**
   - Direct EMPIAR submission from lambda-ber-schema
   - Metadata validation before submission
   - Status tracking integration

2. **Enhanced Metadata**
   - Richer processing provenance
   - Multi-modal experiment description
   - Sample preparation details

3. **Data Mining**
   - Cross-archive queries
   - Workflow pattern analysis
   - Quality metric aggregation

### Emerging Modalities

Support for new EMPIAR data types:
- Time-resolved EM
- In situ structural biology
- Microcrystal electron diffraction
- Correlative super-resolution data

## Best Practices

### For Data Producers

1. **Plan Early**: Structure data for EMPIAR compatibility
2. **Track Metadata**: Use lambda-ber-schema for comprehensive documentation
3. **Organize Hierarchically**: Maintain logical file organization
4. **Include Calibration**: Don't forget gain references, defects

### For Data Consumers

1. **Check References**: Verify EMPIAR-EMDB-PDB links
2. **Review Metadata**: Understand collection parameters
3. **Use APIs**: Programmatic access for large studies
4. **Cite Properly**: Acknowledge data sources

## Validation and Quality

### EMPIAR Requirements

- Minimum metadata for reprocessing
- Standard file formats (MRC, TIFF, DM4)
- Organized directory structure
- Clear imageset categorization

### lambda-ber-schema Enhancements

```yaml
DataFile:
  validation:
    empiar_compliant: true
    format_valid: true
    metadata_complete: true
  quality_checks:
    - image_integrity
    - header_consistency
    - gain_reference_present
```

## Conclusion

lambda-ber-schema and EMPIAR form a **powerful complementary ecosystem** for electron microscopy data management:

- **EMPIAR** provides the definitive archive for raw EM data with:
  - Petabyte-scale storage infrastructure
  - Global accessibility
  - Expanding modality support
  - Community standard compliance

- **lambda-ber-schema** adds comprehensive workflow context through:
  - Sample-to-structure tracking
  - Multi-technique integration
  - Processing provenance
  - Flexible metadata capture

The optimal strategy involves:
1. Using lambda-ber-schema for active research and workflow management
2. Depositing raw data to EMPIAR for long-term preservation
3. Maintaining bidirectional links for complete provenance
4. Leveraging both systems' strengths throughout the research lifecycle

This integration ensures that both the experimental process (lambda-ber-schema) and the raw data products (EMPIAR) are properly documented, preserved, and made accessible to the global scientific community, enabling reproducibility, reanalysis, and methodological advancement in structural biology.