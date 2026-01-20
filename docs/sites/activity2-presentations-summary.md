# Activity 2 Presentation Slides Summary

Summary of presentations from `assets/external/Activity 2/Presentation Slides/`

---

## 1. LAMBDA-Activity-2.pptx

**Overview**: Introduction to LAMBDA Activity 2 data standardization goals and approach.

### Key Points

- **Data Standardization Goals**:
  - Map standards landscape
  - Devise ETL strategy
  - Create and populate lakehouse-ready schema for studies, samples, sample processing, workflow runs, metadata, and annotations

- **Standards Mapping**:
  - Collecting data elements from each facility
  - Aligning with other BER projects (e.g., NMDC, BRIDGE)
  - Mapping to existing standards: NEXUS, mmCIF, EMPIAR

- **Contributions Received**:
  - EMSL_CryoEM_Schema_Share.docx (Krios Cryo-EM Workflows)
  - BNL mappings between mmCIF/PDB and NSLS-II metadata fields
  - MX_metadata_template.xlsx (macromolecular crystallography)

- **High-Level Schema (Proposed)**:
  - Study / Project
  - Sample Preparation
  - Sample
  - Instrument
  - Experiment Run
  - Workflow Execution
  - Data Object

- **AI-Assisted Schema Development**:
  - Schema agent helps with metadata mapping
  - GitHub-based schema management with LinkML YAML files
  - Automated QA/QC validates every PR
  - Auto-rendered as website: https://lambda-ber.github.io/lambda-ber-schema

- **Ontology Reuse**: Leveraging existing ontologies for semantic interoperability

---

## 2. EMSL_cryoEM_metadata_overview_2025_12_19.pdf

**Authors**: August George, James Evans (PNNL)
**Date**: December 5, 2025

### PNNL/EMSL Cryo-EM Workflows

Four main workflow types with LAMBDA priorities:

| Priority | Technique | Resolution | Size Limits |
|----------|-----------|------------|-------------|
| #1 | Single Particle Imaging (SPA) | 1.5-20 Å | >50 kDa |
| #2 | Protein Micro-ED | 1.5-5 Å | 3D crystal <1μm |
| #2 | Small Molecule Micro-ED | 0.5-5 Å | 3D crystal <1μm |
| #3 | Tomography (Whole Cells/Tissue) | 5-40 Å | <750nm thick |

### Data Flow

1. Sample Shipment/Synthesis/Culturing Onsite
2. Protein/RNA/DNA/Cell
3. Cryo-EM Vitrification (Sample Preparation)
4. Krios Instrument (Data Collection)
5. KriosGPU Server (Local Processing)
6. EMSL TAHOMA (Connector)
7. EMSL Science Central
8. EMSL AURORA (Raw & Processed Data Archival)
9. BER Lakehouse
10. External Repositories (EMDB/PDB)
11. Journal Publication

### Metadata Categories

- **High-level project metadata** for EMSL archive (program info, assessments, notes)
- **Sample synthesis/generation metadata**
- **Cryo-EM sample prep metadata**
- **Data collection workflow metadata**:
  - EPU software: Session (.dm), Grid Square (.dm), Foil Hole (.xml)
  - serialEM software: Record (.mdoc)
- **Data reduction/processing metadata**: Cryosparc, Relion, Phenix
- **Data archival metadata**: Session summary YAML
- **Publication and repository metadata**

### Mapping Statistics (First Pass)

| Category | Count | Percentage |
|----------|-------|------------|
| Direct Mappings | 20 | 55.6% |
| Transformations/Conversions | 7 | 19.4% |
| Gaps/Unmapped | 9 | 25.0% |
| **Total PNNL Fields** | 36 | 100% |

### Key Issues Identified

- Unit conversions: Pixel size (Angstroms vs micrometers)
- Type coercions: camera_binning requires integer; PNNL has float values
- Unmapped fields: processing_scheme, nominal_camera_length, tilting_mode, fiducial_size, ice_contamination, ice_quality, particle_concentration

### Discussion Points

- Overall organization: Sample protein or cell as top level?
- Units standardization (angstroms vs micrometers vs meters)
- Nominal vs calibrated values
- Technique vs instrument as higher level organizing principle
- Binning factor: allow float?
- Topaz-specific DL model naming

---

## 3. BioSANS_Task2Lambda_Presentation.pptx

**Author**: Alan Hicks (Computational Instrument Scientist, ORNL NScD)
**Date**: November 21, 2025

### Bio-SANS Instrument Overview

- **Monochromation**: 6-25 Å
- **Collimation**: 8 M1 Guides (2m each)
- **Detection**: 3He Linear Position Sensitive Detectors (LPSD) - 256 Pixels
  - Main: ~1m x 1.0m (192 tubes)
  - Mid-range: ~1m x 0.4m (64 tubes)
  - Wing: ~1m x 0.9m (160 tubes)

### Data Collection

- Uses EPICS (Experimental Physics and Industrial Control System)
- ~4800 objects stored in HDF5 file
- 20-50 PVs necessary for critical information
- Data catalogued to ONCat (ORNL Neutron Catalog)
- Metadata + 2D raw data saved to NeXus HDF format

### Key Metadata Fields

- Wavelength, wavelength spread (dλ/λ)
- Sample to detector distance
- Detector angles and positions
- Beam trap coordinates
- Source/sample aperture parameters
- Sample title, temperature, environment

### ONCat Features

- IPTS project-based organization
- View PVs and entries from metadata
- pyoncat API access
- Authorization layer for user data protection
- Option to publish data with DOI

### Data Processing Pipeline

1. **Reduction** (drtSANS + MANTID):
   - Input: Raw NeXus HDF, calibration runs, instrument parameters
   - Output: 1D/2D data in canSAS format, reduction log (HDF)

2. **Buffer Subtraction, Analysis, Modeling**:
   - Software: Bio-SANS Interactive WebGUI, BioXTas RAW, SasView, ATSAS
   - Guinier analysis, PDDF/P(r), Ab initio modeling, sasmodels fitting

### Integration with lambda-ber-schema

Mapping Bio-SANS workflow to schema classes:

| Schema Element | Bio-SANS Data |
|----------------|---------------|
| Sample | Protein/cell, buffer composition, contrast/SLD |
| Sample Preparation | Gene synthesis, expression, purification, %D2O |
| Instrument | Bio-SANS description, detectors, neutron source |
| Experiment Run | Duration, counts, RunID, ProjectID, configuration |
| Workflow Runs | drtSANS reduction, analysis workflows |
| Data Products | NeXus HDF5 2D raw, 1D/2D processed, buffer-subtracted |

### Example Dataset

**Title**: "The N-terminal domain of COMPANION OF CELLULOSE SYNTHASE1 promotes microtubule array formation in Arabidopsis"
**DOI**: https://doi.org/10.1093/plphys/kiaf392
**Instruments**: Bio-SANS, LiX NSLS-II, Rigaku SAXS, smFRET, Confocal microscopy

Multiple studies with different research questions sharing samples and preparations.

---

## 4. NSLS2 - AMX-FMX data organization.pptx

**Author**: Venkateswaran "Shekar" Shekar (Computational Scientist, BNL, NSLS-II)
**Date**: December 5, 2025

### AMX/FMX Beamlines

- FMX: https://www.bnl.gov/nsls2/beamlines/beamline.php?r=17-ID-2
- AMX: https://www.bnl.gov/nsls2/beamlines/beamline.php?r=17-ID-1

### Data Flow

Sample Preparation → Data Collection → Data Reduction → Data Analysis

### Data Collection

- **Software**: Life Science Data Collection (backed by Bluesky)
- **Database**: MongoDB for sample and collection information
- **Collection Modes**: Manual, fully automated, hybrid

### Sample Information Captured

- Sample metadata
- Collection parameters
- Raw data locations

### Data Directory Structure

Standard directory tree containing:
- Raw diffraction data
- Processed data
- Data collection logs
- Processing logs

**Processing Pipelines**: Autoproc, FastDP

### Data Transfer Methods

- Globus
- SFTP
- Tiled (in progress): tiled-demo.nsls2.bnl.gov
  - Structured access regardless of format
  - Search and chunkwise data access
  - Uses HTTPS/secure websockets

### Fragment Screening Project

- **mxplate**: https://github.com/NSLS2/mxplate/
- Tracks provenance of samples through long experiment lifecycles
- Manages high-throughput experiment plans

### RECAP - Reproducible Experiment Capture and Provenance

**GitHub**: https://github.com/NSLS2/recap/

Key features:
- Experiment data management framework
- Unifies experiment stages under scalable provenance backbone
- Complete audit trail (who, when, what settings)
- Models physical and digital artifacts with relationships
- SQL database with stable API

### Core Concepts

**Templates vs Instances**:
- Templates: Reusable definitions (versioned, can evolve)
- Instances: Concrete implementations in the lab

**Benefits**:
- Repeatability: Single template spawns many runs
- Versioning: Templates evolve while past instances remain frozen
- Separation of concerns: Scientists design templates; automation executes instances

**Resource Tracking**:
- ResourceTemplates define types, children, properties
- Resources are instantiated and trackable through workflows

---

## Cross-Cutting Themes

1. **Schema Alignment**: All facilities working toward common high-level schema (Study → Sample → Instrument → Experiment → Workflow → Data)

2. **Metadata Gaps**: Each facility has unique fields not yet mapped to common schema

3. **Provenance Tracking**: Strong emphasis on tracking sample preparation through final data products

4. **Existing Standards**: Leveraging NEXUS/HDF5, mmCIF, canSAS formats

5. **Data Access**: Mix of facility-specific catalogs (ONCat, MongoDB) with emerging unified access (Tiled, BER Lakehouse)
