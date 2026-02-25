# lambda-ber-schema 

lambda-ber-schema is a comprehensive schema for representing multimodal structural biology imaging data, 
from atomic-resolution structures to tissue-level organization. It supports diverse experimental 
techniques including cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and 
spectroscopic imaging.

## Schema Organization

The schema follows a **relational design** with flat entity collections and explicit association
tables for many-to-many relationships. This maps cleanly to SQL databases while supporting
flexible data reuse across studies.

The top-level entity is a [Dataset](Dataset.md), which serves as a container for related research.
A dataset might represent all data from a specific grant, collaboration, or publication.

### Entity Tables

All entities are stored in flat collections at the Dataset level:

**Biological Materials**
- [Samples](Sample.md): The biological specimens being studied (proteins, nucleic acids, complexes,
  cells, tissues). Each sample includes detailed molecular composition, buffer conditions, and
  storage information. For example, a purified protein with its sequence, concentration, and buffer pH.

- [Sample Preparations](SamplePreparation.md): How samples were prepared for specific techniques.
  This includes cryo-EM grid preparation (vitrification parameters), crystallization conditions for
  X-ray studies, or staining protocols for fluorescence microscopy.

**Data Collection**
- [Instruments](Instrument.md): The equipment used, from Titan Krios microscopes to synchrotron
  beamlines. Each instrument type ([CryoEMInstrument](CryoEMInstrument.md),
  [XRayInstrument](XRayInstrument.md), [SAXSInstrument](SAXSInstrument.md)) has specific parameters
  like accelerating voltage, detector type, or beam energy.

- [Experiment Runs](ExperimentRun.md): Individual data collection sessions. An experiment run
  captures when, how, and under what conditions data was collected, including quality metrics
  like resolution and completeness.

**Data Processing**
- [Workflow Runs](WorkflowRun.md): Computational processing steps applied to raw data. This includes
  motion correction for cryo-EM movies, 3D reconstruction, model building, or phase determination
  for crystallography. Each workflow tracks the software used, parameters, and computational resources.

**Data Products**
- [Data Files](DataFile.md): Any files generated or used, from raw data to final models. Each file
  is tracked with checksums for data integrity and typed (micrograph, particles, volume, model).

- [Images](Image.md): Specialized classes for different imaging modalities:
  - [Image2D](Image2D.md): Micrographs, diffraction patterns
  - [Image3D](Image3D.md): 3D reconstructions, tomograms
  - [FTIRImage](FTIRImage.md): Molecular composition maps from infrared spectroscopy
  - [FluorescenceImage](FluorescenceImage.md): Fluorophore-labeled cellular components
  - [OpticalImage](OpticalImage.md): Brightfield/phase contrast microscopy
  - [XRFImage](XRFImage.md): Elemental distribution maps

**Logical Groupings**
- [Studies](Study.md): Lightweight groupings representing focused investigations of specific
  biological questions. For example, a study might investigate "Heat stress response in Arabidopsis"
  or "Structure of the human ribosome under different conditions."

### Association Tables

Many-to-many relationships are represented via explicit association tables, which can carry
relationship metadata (e.g., the role of a sample in an experiment):

- **StudySampleAssociation**: Links samples to studies (with role: target, control, reference)
- **StudyExperimentAssociation**: Links experiments to studies
- **StudyWorkflowAssociation**: Links workflows to studies
- **ExperimentSampleAssociation**: Links samples to experiments (with role and preparation used)
- **ExperimentInstrumentAssociation**: Links instruments to experiments (with role: primary, detector)
- **WorkflowExperimentAssociation**: Links source experiments to workflows
- **WorkflowInputAssociation**: Links input files to workflows
- **WorkflowOutputAssociation**: Links output files to workflows

This relational design enables:
- **Sample reuse**: The same sample can be used in multiple studies and experiments
- **Multi-instrument experiments**: An experiment can use multiple instruments with different roles
- **Integrative workflows**: A workflow can combine data from multiple experiments

## Example Usage

A typical cryo-EM study of a protein complex would include:
1. Sample records for the purified complex with molecular weight and buffer composition
2. Grid preparation details with vitrification parameters
3. Microscope specifications and data collection parameters
4. Processing workflows from motion correction through 3D refinement
5. Final reconstructed volumes and fitted atomic models

A multimodal plant imaging study might combine:
1. Whole plant optical imaging for morphology
2. XRF imaging to map nutrient distribution
3. FTIR spectroscopy to identify stress-related molecular changes
4. Fluorescence microscopy to track specific protein responses
5. Cryo-EM of isolated organelles for ultrastructural details

## Key Features

- **Relational design**: Flat entity tables with explicit association tables for M:N relationships
- **SQL-friendly**: Maps directly to normalized database tables
- **Technique-agnostic core**: The same schema handles data from any structural biology method
- **Rich metadata**: Comprehensive tracking from sample to structure
- **Workflow provenance**: Complete computational reproducibility
- **Multimodal support**: Seamlessly integrate data across scales and techniques
- **Standards-compliant**: Follows FAIR principles and integrates with existing ontologies


URI: https://w3id.org/lambda-ber-schema/