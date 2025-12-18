# lambda-ber-schema and proteindiffraction.org (IRRMC) Alignment Analysis

> **Note**: This document was generated using Claude (Anthropic's AI assistant) through automated analysis of documentation and web sources. While efforts have been made to ensure accuracy, there may be errors or outdated information. Please verify critical details with official proteindiffraction.org documentation.

## Overview

This document provides a detailed analysis of the alignment between the lambda-ber-schema schema and proteindiffraction.org (IRRMC - Integrated Resource for Reproducibility in Macromolecular Crystallography), examining how lambda-ber-schema can integrate with and complement IRRMC's role as an archive for raw X-ray diffraction data supporting reproducibility in crystallographic research.

## Introduction to proteindiffraction.org

### What is IRRMC?

proteindiffraction.org hosts the Integrated Resource for Reproducibility in Macromolecular Crystallography (IRRMC), a comprehensive repository designed to archive raw diffraction data with associated metadata from macromolecular crystallography experiments. Key characteristics:

- **Purpose**: Archive raw diffraction images enabling structure reprocessing and validation
- **Content**: 6,700+ projects, 10,800+ datasets (as of 2024)
- **Sources**: Structural Genomics centers (CSGID, SSGCID, JCSG, MCSG, SGC) and individual research labs
- **Access**: Freely available under Creative Commons CC0 (public domain)
- **Goal**: Enable reproducibility through access to original experimental data

### Data Sources

IRRMC aggregates data from major structural biology initiatives:

1. **Structural Genomics Centers**
   - CSGID (Center for Structural Genomics of Infectious Diseases)
   - SSGCID (Seattle Structural Genomics Center for Infectious Disease)
   - JCSG (Joint Center for Structural Genomics)
   - MCSG (Midwest Center for Structural Genomics)
   - SGC (Structural Genomics Consortium)

2. **Individual Research Laboratories**
   - Academic institutions worldwide
   - Industrial research groups
   - Synchrotron user programs

### Current Status (2024-2025)

- **Version**: 2.0 with improved metadata extraction
- **Architecture**: Redesigned for automated publishing process
- **Standards**: Moving toward FAIR data principles (Findable, Accessible, Interoperable, Re-usable)
- **Integration**: Links to PDB structures via DOIs

## IRRMC Data Model

### Entry Structure

Each proteindiffraction.org dataset entry contains:

```
Project
├── Dataset(s)
│   ├── Raw diffraction images (typically ~10GB compressed)
│   ├── Metadata
│   │   ├── Title/Description
│   │   ├── First Author/Organization
│   │   ├── UniProt ID (protein identifier)
│   │   ├── Resolution (Å)
│   │   ├── R/Rfree values
│   │   └── DOI
│   └── External Links
│       ├── PDB structure
│       ├── Validation reports
│       └── Institutional repositories
└── Download Package (compressed archive)
```

### Metadata Fields

Based on the browse interface, IRRMC captures:

| Field | Description | lambda-ber-schema Equivalent |
|-------|-------------|------------------------------|
| Title | Crystal structure description | Study.title |
| First Author | Research group/PI | Study.contributors |
| UniProt ID | Protein database link | Sample.uniprot_id |
| Resolution | Diffraction quality (Å) | WorkflowRun.resolution |
| R/Rfree | Model reliability statistics | WorkflowRun.r_work, r_free |
| DOI | Persistent identifier | DataFile.doi |
| PDB ID | Deposited structure | external_ids.pdb_id |

### Download Packages

Raw data is distributed as compressed archives:
- Typical size: 139 MB to 9.3 GB per dataset
- Format: Compressed diffraction image collections
- Contents: CBF, IMG, or HDF5 format images

## lambda-ber-schema-IRRMC Alignment

### Structural Mapping

| IRRMC Concept | lambda-ber-schema Equivalent | Alignment Notes |
|---------------|------------------------------|-----------------|
| **Project** | **Dataset/Study** | Complete experimental collection |
| **Dataset** | **ExperimentRun + DataFiles** | Single data collection session |
| **Raw Images** | **DataFile (type: diffraction)** | ✅ Diffraction image files |
| **Metadata** | **ExperimentRun attributes** | Collection parameters |
| **Structure** | **WorkflowRun output** | Processing results |
| **UniProt Link** | **Sample.uniprot_id** | ✅ Protein identification |
| **PDB Link** | **external_ids** | ✅ Cross-references |

### Metadata Alignment

#### Data Collection Parameters

**IRRMC Metadata (implicit in raw data):**
- Wavelength
- Detector distance
- Oscillation angle
- Beam center
- Number of images

**lambda-ber-schema Equivalent:**
```yaml
ExperimentRun:
  technique: xray_crystallography
  wavelength: 0.9795
  detector_distance: 200.0
  oscillation_angle: 0.2
  beam_center_x: 1024.5
  beam_center_y: 1024.5
  number_of_images: 1800
  beamline: "FMX"
```

#### Quality Metrics

**IRRMC Metadata:**
- Resolution
- R-factor / R-free

**lambda-ber-schema Equivalent:**
```yaml
WorkflowRun:
  workflow_type: refinement
  resolution: 1.85
  r_work: 0.165
  r_free: 0.198
  space_group: "P43212"
```

#### Sample Information

**IRRMC Metadata:**
- UniProt ID
- Protein name (from title)
- Organism (from title)

**lambda-ber-schema Equivalent:**
```yaml
Sample:
  sample_code: "lysozyme_001"
  protein_name: "Lysozyme C"
  uniprot_id: "P00698"
  source_organism: "Gallus gallus"
```

## Key Differences and Complementarities

### 1. Data Focus

**IRRMC**: Raw data archival
- Primary focus on diffraction images
- Enables complete reprocessing
- Supports reproducibility verification

**lambda-ber-schema**: Workflow context
- Tracks complete experimental history
- Links sample preparation to final structure
- Captures processing parameter evolution

### 2. Metadata Depth

**IRRMC**: Minimal essential metadata
- Enough to identify and locate data
- Links to PDB for full details
- Automated extraction where possible

**lambda-ber-schema**: Comprehensive metadata
- Detailed experimental conditions
- Buffer compositions, crystallization conditions
- Quality metrics at each stage

### 3. Scope

**IRRMC**: X-ray crystallography specific
- Specialized for MX data
- Deep domain expertise
- Established community resource

**lambda-ber-schema**: Multi-technique
- Unified model across techniques
- Supports cryo-EM, SAXS, spectroscopy
- Integrative structural biology

## Integration Strategies

### lambda-ber-schema Reference to IRRMC

```yaml
# Reference proteindiffraction.org dataset
DataFile:
  file_name: "diffraction_images.tar.gz"
  file_format: cbf
  data_type: diffraction
  external_ids:
    proteindiffraction_project: "SSGCID-bael-8c0e8cf36da2"
  download_url: "https://proteindiffraction.org/project/SSGCID-bael-8c0e8cf36da2"
```

### IRRMC Data Import to lambda-ber-schema

```python
def import_from_proteindiffraction(project_id):
    """Import IRRMC project metadata into lambda-ber-schema"""

    # Fetch project metadata
    metadata = fetch_irrmc_metadata(project_id)

    study = {
        "title": metadata["title"],
        "external_ids": {
            "proteindiffraction_id": project_id,
            "pdb_id": metadata.get("pdb_id"),
            "uniprot_id": metadata.get("uniprot_id")
        },
        "samples": [{
            "sample_code": f"sample_{project_id}",
            "protein_name": extract_protein_name(metadata["title"]),
            "uniprot_id": metadata.get("uniprot_id")
        }],
        "data_files": [{
            "file_name": f"{project_id}_diffraction.tar.gz",
            "file_format": "cbf",
            "data_type": "diffraction",
            "file_size_bytes": metadata.get("download_size")
        }],
        "workflow_runs": [{
            "workflow_type": "refinement",
            "resolution": metadata.get("resolution"),
            "r_work": metadata.get("r_factor"),
            "r_free": metadata.get("r_free")
        }]
    }

    return study
```

### Enrichment Strategy

lambda-ber-schema can enrich IRRMC data with:

1. **Sample Preparation Details**
   ```yaml
   XRayPreparation:
     crystallization_conditions:
       method: vapor_diffusion_hanging_drop
       precipitant: "30% PEG 4000"
       ph: 7.5
       temperature: 18.0
   ```

2. **Processing Provenance**
   ```yaml
   WorkflowRun:
     - workflow_type: indexing
       software_name: "DIALS"
       software_version: "3.18.0"
     - workflow_type: integration
       software_name: "DIALS"
     - workflow_type: scaling
       software_name: "AIMLESS"
     - workflow_type: phasing
       software_name: "PHASER"
       phasing_method: molecular_replacement
   ```

3. **Quality Assessment**
   ```yaml
   WorkflowRun:
     quality_metrics:
       completeness: 99.5
       multiplicity: 6.8
       r_merge: 0.082
       i_sigma: 15.2
       cc_half: 0.998
   ```

## Reproducibility Support

### The SBDG Finding

The Structural Biology Data Grid (SBDG) analysis revealed that "18% of deposited datasets could not be automatically reprocessed with current software" due to metadata and format inconsistencies (Iudin et al., 2016).

### How lambda-ber-schema Addresses This

1. **Complete Metadata Capture**
   - All parameters needed for reprocessing
   - Controlled vocabularies reduce ambiguity
   - Required fields ensure completeness

2. **Processing History**
   - Track which software versions were used
   - Document parameter choices
   - Enable exact reproduction

3. **Format Mappings**
   - imgCIF mappings for image metadata
   - mmCIF mappings for structure data
   - NSLS2 mappings for beamline metadata

## Recommended Workflow

### 1. Data Collection
```
Synchrotron beamline / Home source
         ↓
Collect diffraction images
         ↓
Record metadata in lambda-ber-schema (ExperimentRun)
```

### 2. Processing
```
Process with DIALS/XDS/etc.
         ↓
Track each step in lambda-ber-schema (WorkflowRun)
         ↓
Capture quality metrics
```

### 3. Archival
```
Deposit raw images to proteindiffraction.org
         ↓
Deposit structure to PDB
         ↓
Update lambda-ber-schema with accession IDs
```

### 4. Publication
```
lambda-ber-schema: Complete workflow record
proteindiffraction.org: Raw data archive
PDB: Final structure
         ↓
All cross-linked for reproducibility
```

## Best Practices

### For Data Producers

1. **Document Early**: Use lambda-ber-schema during data collection
2. **Archive Raw Data**: Submit to proteindiffraction.org
3. **Link Everything**: Maintain cross-references between resources
4. **Include Processing**: Document software and parameters

### For Data Consumers

1. **Check Raw Data**: Verify proteindiffraction.org links exist
2. **Review Metadata**: Understand collection parameters
3. **Reprocess If Needed**: Use archived raw data
4. **Cite Properly**: Acknowledge data sources

## Future Opportunities

### Technical Developments

1. **Automated Extraction**
   - Parse CBF/imgCIF headers automatically
   - Extract metadata from proteindiffraction.org
   - Populate lambda-ber-schema programmatically

2. **Validation Integration**
   - Compare processed results with deposited structures
   - Flag inconsistencies for review
   - Enable systematic quality assessment

3. **Search and Discovery**
   - Query across both resources
   - Find raw data for reprocessing
   - Identify similar experiments

### Community Benefits

- Enhanced reproducibility in crystallography
- Better training data for AI/ML models
- Improved method development and validation
- Comprehensive provenance for regulatory contexts

## Comparison with Related Resources

| Resource | Focus | Raw Data | Metadata Depth | Scope |
|----------|-------|----------|----------------|-------|
| proteindiffraction.org | Raw diffraction images | ✅ Primary | Basic | MX only |
| PDB | Deposited structures | ❌ | Comprehensive | Multi-technique |
| lambda-ber-schema | Workflow tracking | Reference | Comprehensive | Multi-technique |
| Zenodo | General archival | ✅ | Variable | Any |

## Conclusion

proteindiffraction.org (IRRMC) and lambda-ber-schema form a **complementary ecosystem** for crystallographic data management:

- **IRRMC** provides critical infrastructure for raw data archiving with:
  - Petabyte-scale diffraction image storage
  - CC0 licensing for unrestricted reuse
  - Links to deposited PDB structures
  - Support for reproducibility verification

- **lambda-ber-schema** adds comprehensive workflow context through:
  - Sample-to-structure tracking
  - Detailed metadata with controlled vocabularies
  - Processing provenance documentation
  - Multi-technique integration capability

The optimal strategy involves:
1. Using lambda-ber-schema for complete experimental documentation
2. Archiving raw diffraction data to proteindiffraction.org
3. Maintaining bidirectional links between resources
4. Leveraging both systems' strengths for reproducible crystallography

This integration addresses the data quality challenges identified in the SBDG study by ensuring both raw data (IRRMC) and comprehensive metadata (lambda-ber-schema) are preserved, enabling true reproducibility in macromolecular crystallography.

## References and Further Reading

- proteindiffraction.org: https://proteindiffraction.org/
- IRRMC About Page: https://proteindiffraction.org/about/
- Grabowski et al. (2016) "A public database of macromolecular diffraction experiments" Acta Cryst. D72, 1181-1193
- Iudin et al. (2016) "Data publication with the structural biology data grid supports live analysis" Nature Communications 7, 10882
- Minor et al. (2016) "Safeguarding structural data repositories against bad apples" Structure 24(2), 216-220
