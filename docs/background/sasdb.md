# SASDB: Small Angle Scattering Biological Data Bank

## Overview

SASDB (Small Angle Scattering Biological Data Bank) is a curated repository for biological small-angle scattering data, serving as the primary archive for experimental data from both Small-Angle X-ray Scattering (SAXS) and Small-Angle Neutron Scattering (SANS) experiments. Launched in 2014 by the Biological Small Angle Scattering Group at EMBL Hamburg, SASDB addresses the urgent need for a global repository of experimental scattering data as recommended by the wwPDB small angle scattering task force.

**Website**: https://www.sasbdb.org  
**Current Status**: Over 1,000 entries containing more than 1,600 models (as of 2019)  
**Growth Rate**: Approximately 32 entries deposited per month from worldwide contributors

## Purpose and Scope

SASDB was designed to:
- Store and organize small-angle scattering experimental data with associated metadata
- Provide freely accessible structural information on biological macromolecules in solution
- Support structural biology research with resolution of 1-2 nm
- Enable data exchange between repositories through federated database principles
- Ensure reproducibility and validation of SAS experiments

## Database Architecture

### Technical Implementation

- **Database Type**: Relational MySQL database
- **Web Framework**: Django 1.6 (Python 2.7)
- **Visualization Tools**: 
  - Gnuplot for data plots
  - PyMOL for model visualization
  - JSmol for interactive 3D structure viewing
- **Search Engine**: Elasticsearch
- **Data Format**: Primary support for sasCIF format with conversion tools

### Entry Identification System

Each SASDB entry has a unique identifier following the format: **SASXXXN**
- S-A-S: Fixed prefix
- XXX: Three alphanumeric characters
- N: Single digit

Example: SASDAB5, SASDGV5

## Data Model and Structure

### Core Components

Each SASDB entry is organized around an experimental SAS dataset linked to comprehensive metadata:

#### 1. Sample Information
- **Sample Details**:
  - Macromolecule name and type
  - Expected molecular weight
  - Organism source
  - Polymer type classification
  - Biological sequence (when available)
  - UniProt links for protein identification

- **Buffer Composition**:
  - Chemical composition
  - pH conditions
  - Salt concentrations
  - Additives and stabilizers

- **Storage Conditions**:
  - Temperature
  - Storage duration
  - Preservation methods

#### 2. Experimental Parameters
- **Instrument Specifications**:
  - Instrument code and facility
  - Detector type and configuration
  - X-ray source or neutron source details
  - Beam characteristics

- **Data Collection**:
  - Experiment date and duration
  - Temperature during measurement
  - Exposure time
  - Sample concentration
  - Collection mode (batch, SEC-SAXS, etc.)

- **Quality Metrics**:
  - Signal-to-noise ratio
  - Resolution range (q-range)
  - Data completeness

#### 3. Derived Structural Parameters
- **Guinier Analysis**:
  - Forward scattering I(0)
  - Radius of gyration (Rg)
  - Guinier plot with linear fit
  - Quality of fit parameters

- **Real-Space Analysis**:
  - Pair distance distribution function P(r)
  - Maximum particle dimension (Dmax)
  - Porod volume
  - Molecular weight estimates

- **Additional Plots**:
  - Kratky plot (dimensionless)
  - Porod plot
  - Scattering profile visualization

#### 4. Models and Fits
- **Model Types**:
  - Ab initio shape reconstructions
  - Hybrid models (combining SAS with other techniques)
  - Atomic models from crystallography or NMR
  - Ensemble models

- **Fit Quality**:
  - Chi-squared values
  - Reduced chi-squared
  - P-values for statistical significance
  - Visual fit overlays

#### 5. External References
- **Database Links**:
  - PubMed for publications
  - UniProt for protein sequences
  - PDB for atomic structures
  - Related SASDB entries

- **Publication Information**:
  - Journal reference
  - Authors
  - DOI
  - Project information (for unpublished data)

### Data Organization Hierarchy

```
Dataset
├── Study/Project
│   ├── Multiple SASDB Entries
│   │   ├── Experimental Data (scattering curve)
│   │   ├── Metadata Set 1 (experimental conditions)
│   │   ├── Metadata Set 2 (models and fits)
│   │   └── External Links
│   └── Publication/Project Info
└── Related Entries (grouped by study)
```

## Data Standards and Formats

### sasCIF Format

SASDB adopted sasCIF (small-angle scattering Crystallographic Information File) as its primary data exchange format. This ASCII-based format extends the general CIF framework used in crystallography.

#### sasCIF Features:
- **Comprehensive Data Storage**: Includes scattering curves, distance distributions, models, and fits in a single file
- **Metadata Categories**: Sample properties, solvent conditions, experimental parameters, publication records
- **2D Data Support**: Area-detector data can be included using imgCIF dictionary
- **Standardization**: Follows wwPDB SAStf recommendations for data presentation and exchange

#### sasCIFtools Suite:
- **cif2fit**: Extracts calculated scattering and fit statistics
- **cif2sub**: Extracts metadata to text files
- **cif2all**: Comprehensive extraction of all data types
- **Conversion tools**: Support for various legacy formats

### Data Validation

SASDB implements a multi-tier validation system:

1. **Manual Curation**: Expert review by database curators
2. **Consistency Checks**:
   - Structural parameter validation
   - Rg calculation quality
   - Signal-to-noise assessment
   - Model fit quality evaluation
3. **Future Plans**: Automated validation pipeline development

## API and Programmatic Access

### REST API

SASDB provides RESTful web services for programmatic data access:

- **Base URL**: https://www.sasbdb.org/rest-api/
- **Documentation**: https://www.sasbdb.org/rest-api/docs/
- **Response Formats**: JSON, XML
- **Authentication**: Not required for public data access

### API Features:
- Entry retrieval by SASDB ID
- Metadata queries
- Bulk data download
- Search functionality
- Format conversion services

### Identifier Format:
Local identifiers must match the regular expression: `^[Ss][Aa][Ss][A-Za-z0-9]{3}[0-9]$`

## Data Access and Usage

### Access Methods

1. **Web Interface**: 
   - Browse and search without registration
   - Download individual entries
   - Interactive visualization tools
   - Advanced search filters

2. **Programmatic Access**:
   - REST API for automated retrieval
   - Bulk download capabilities
   - sasCIF format export/import

3. **Data Submission**:
   - Registration required (email and password)
   - Online submission interface
   - Validation before acceptance
   - Embargo options for unpublished data

### Usage Policies

- **License**: All data free of copyright restrictions
- **Commercial Use**: Permitted
- **Attribution**: Required to original authors
- **Data Reuse**: Encouraged for meta-analyses and method development

## Visualization and Analysis Tools

### Integrated Visualization

SASDB provides several visualization modes for data analysis:

1. **Scattering Profiles**:
   - Linear/log and log/log scales
   - Interactive zooming and panning
   - Overlay of experimental and calculated data

2. **Analysis Plots**:
   - **Guinier Plot**: Low-q region analysis for Rg and I(0)
   - **Kratky Plot**: Assessment of folding state and flexibility
   - **Porod Plot**: High-q region analysis
   - **P(r) Distribution**: Real-space representation

3. **3D Model Viewing**:
   - JSmol integration for interactive manipulation
   - PyMOL-generated static images
   - Overlay of multiple models
   - Surface and volume representations

### Data Quality Indicators

Visual and numerical indicators help users assess data quality:
- Guinier region linearity
- Systematic deviations in fits
- Resolution estimates
- Aggregation indicators

## Integration with Structural Biology Ecosystem

### wwPDB Compliance

SASDB aligns with Worldwide Protein Data Bank (wwPDB) recommendations:
- Standardized data formats (sasCIF)
- Consistent metadata requirements
- Quality assessment protocols
- Federated database architecture

### Complementary Databases

SASDB interfaces with multiple structural biology resources:
- **PDB**: Atomic structure validation against SAS data
- **UniProt**: Sequence and functional annotations
- **BMRB**: NMR data correlation
- **EMDB**: EM density map comparisons

### Hybrid Modeling Support

SASDB facilitates integrative structural biology by storing:
- Multi-technique datasets
- Hybrid models combining SAS with crystallography/NMR/EM
- Ensemble models from multiple conformations
- Time-resolved SAS data

## Current Limitations and Future Developments

### Current Limitations

1. **Manual Curation Bottleneck**: Growing submission rate challenges manual review
2. **Format Diversity**: Need for more automated format conversion
3. **Metadata Completeness**: Variable quality of deposited metadata
4. **Search Capabilities**: Limited semantic search functionality

### Planned Improvements

1. **Automated Validation Pipeline**: 
   - Machine learning for quality assessment
   - Automated consistency checks
   - Real-time validation feedback

2. **Enhanced Search**:
   - Semantic search capabilities
   - Structure-based similarity searches
   - Advanced filtering options

3. **Format Standardization**:
   - Full sasCIF implementation
   - Automated conversion services
   - Legacy format support

4. **Federation System**:
   - Integration with regional databases
   - Synchronized data exchange
   - Distributed validation

## Use Cases and Applications

### Research Applications

1. **Structure Validation**: Compare crystal structures with solution behavior
2. **Conformational Analysis**: Study protein flexibility and dynamics
3. **Complex Formation**: Analyze protein-protein interactions
4. **Method Development**: Benchmark new SAS analysis methods
5. **Meta-Analysis**: Large-scale studies across multiple datasets

### Educational Resources

SASDB serves as a teaching resource for:
- SAS data interpretation
- Quality assessment training
- Method comparison studies
- Best practices in data deposition

## Best Practices for Data Deposition

### Required Information

Minimum metadata requirements for deposition:
1. Experimental data (scattering curve)
2. Sample identification and concentration
3. Buffer composition
4. Data collection parameters
5. Basic structural parameters (Rg, I(0), Dmax)

### Recommended Information

For comprehensive entries:
1. P(r) distribution
2. Guinier and Kratky plots
3. Models (if available)
4. Raw data (if available)
5. Detailed experimental protocols
6. Quality assessment metrics

### Data Preparation

Before submission:
1. Verify data quality and consistency
2. Calculate standard structural parameters
3. Prepare models in accepted formats
4. Compile complete metadata
5. Check external database links

## Conclusion

SASDB represents a critical infrastructure component for the structural biology community, providing standardized storage, validation, and dissemination of small-angle scattering data. Its comprehensive metadata model, visualization capabilities, and integration with the broader structural biology ecosystem make it an essential resource for researchers using SAS techniques. As the database continues to grow and evolve, automated validation and enhanced search capabilities will further increase its utility for both data producers and consumers in the field of structural biology.

## References and Further Reading

- SASBDB Website: https://www.sasbdb.org
- Valentini et al. (2015) "SASBDB, a repository for biological small-angle scattering data" Nucleic Acids Research 43(D1):D357-D363
- Kikhney et al. (2020) "SASBDB: Towards an automatically curated and validated repository for biological scattering data" Protein Science 29(1):66-75
- wwPDB SAS Task Force Report: Guidelines for SAS data deposition
- sasCIF Format Specification: Extension for small-angle scattering data