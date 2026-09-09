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
- [Proteins](Protein.md): The protein as a biological entity - sequence, source organism, gene,
  and the functional and structural annotations that hold for it in every preparation. Identified
  by UniProt accession as a CURIE (`uniprot:P69905`) wherever one exists. One record serves every
  sample that contains the protein; what varies between preparations lives on the sample and on
  the sample-protein association.

- [Samples](Sample.md): The physical specimens being studied (proteins, nucleic acids, complexes,
  cells, tissues). Each sample records the preparation-specific facts - buffer conditions,
  concentration, storage, purity - and links to the proteins it contains through
  [SampleProteinAssociation](SampleProteinAssociation.md).

- [Protein Constructs](ProteinConstruct.md): How a protein was cloned and expressed - vector,
  tags, cleavage sites, codon optimization. A construct realizes one protein and may feed many samples.

- [Sample Preparations](SamplePreparation.md): How samples were prepared for specific techniques.
  This includes cryo-EM grid preparation (vitrification parameters), crystallization conditions for
  X-ray studies, or staining protocols for fluorescence microscopy.

**Data Collection**
- [Instruments](Instrument.md): The equipment used, from Titan Krios microscopes to synchrotron
  beamlines. Each instrument type ([CryoEMInstrument](CryoEMInstrument.md),
  [XRayInstrument](XRayInstrument.md), [SANSInstrument](SANSInstrument.md),
  [SAXSInstrument](SAXSInstrument.md)) has specific parameters like accelerating voltage,
  detector type, or beam energy.

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

**People and organizations**
- [Persons](Person.md): People involved in producing, processing or publishing the data - principal
  investigators, beamline operators, analysts, curators. Identified by ORCID where available. Which
  work a person is attached to, and in what capacity, is carried by the person association tables,
  so one record serves every role a person holds across the dataset.

- [Organizations](Organization.md): Institutions, facilities and funding bodies, identified by ROR.
  The structured home for organizational identity that would otherwise live as free text on
  instruments, on people, and in FacilityEnum's annotations - so a parent institution is stated
  once rather than restated by everything that refers to it.

### Association Tables

Many-to-many relationships are represented via explicit association tables, which can carry
relationship metadata (e.g., the role of a sample in an experiment):

- **StudySampleAssociation**: Links samples to studies (with role: target, control, reference)
- **StudyExperimentAssociation**: Links experiments to studies
- **StudyWorkflowAssociation**: Links workflows to studies
- **ExperimentSampleAssociation**: Links samples to experiments (with role and preparation used)
- **SampleProteinAssociation**: Links proteins to samples (with role, copy number, residue range,
  modifications, observed mass, and the construct used)
- **ExperimentInstrumentAssociation**: Links instruments to experiments (with role: primary, detector)
- **WorkflowExperimentAssociation**: Links source experiments to workflows
- **WorkflowInputAssociation**: Links input files to workflows
- **WorkflowOutputAssociation**: Links output files to workflows
- **StudyPersonAssociation**: Links people to studies (with role, author position, corresponding flag)
- **ExperimentPersonAssociation**: Links people to experiment runs (with role: operator, local contact)
- **WorkflowPersonAssociation**: Links people to workflow runs (with role: analyst, reviewer)
- **StudyOrganizationAssociation**: Links organizations to studies (with role and award number)
- **PersonOrganizationAssociation**: Links people to organizations (with role and affiliation dates)

This relational design enables:
- **Sample reuse**: The same sample can be used in multiple studies and experiments
- **Protein reuse**: The same protein is described once and linked from every sample that contains it
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


URI: http://w3id.org/lambda/