# Lambda-BER Schema Overview

The [lambda-ber-schema](https://w3id.org/lambda-ber-schema/) is a comprehensive schema for representing multimodal structural biology imaging data, from atomic-resolution structures to tissue-level organization.

## Design Philosophy

The schema follows a **relational design** with:
- Flat entity collections stored at the Dataset level
- Explicit association tables for many-to-many relationships
- SQL-friendly structure that maps cleanly to normalized databases

## Schema Structure

```
Dataset (root container)
├── Entity Tables (flat collections)
│   ├── studies
│   ├── samples
│   ├── sample_preparations
│   ├── instruments
│   ├── experiment_runs
│   ├── workflow_runs
│   ├── data_files
│   └── images
│
└── Association Tables (M:N relationships)
    ├── study_sample_associations
    ├── study_experiment_associations
    ├── study_workflow_associations
    ├── experiment_sample_associations
    ├── experiment_instrument_associations
    ├── workflow_experiment_associations
    ├── workflow_input_associations
    └── workflow_output_associations
```

## Core Classes

### Container

| Class | Description |
|-------|-------------|
| [Dataset](https://w3id.org/lambda-ber-schema/Dataset) | Root container holding all entity collections and association tables |

### Logical Groupings

| Class | Description |
|-------|-------------|
| [Study](https://w3id.org/lambda-ber-schema/Study) | Lightweight grouping of related experiments investigating a research question |

### Biological Materials

| Class | Description |
|-------|-------------|
| [Sample](https://w3id.org/lambda-ber-schema/Sample) | Biological specimens (proteins, nucleic acids, complexes, cells, tissues) |
| [ProteinConstruct](https://w3id.org/lambda-ber-schema/ProteinConstruct) | Detailed protein construct information including expression system |
| [SamplePreparation](https://w3id.org/lambda-ber-schema/SamplePreparation) | How samples were prepared for specific techniques |

### Instrumentation

| Class | Description |
|-------|-------------|
| [Instrument](https://w3id.org/lambda-ber-schema/Instrument) | Base class for all instruments |
| [CryoEMInstrument](https://w3id.org/lambda-ber-schema/CryoEMInstrument) | Cryo-electron microscopes (e.g., Titan Krios) |
| [XRayInstrument](https://w3id.org/lambda-ber-schema/XRayInstrument) | X-ray diffractometers and synchrotron beamlines |
| [SAXSInstrument](https://w3id.org/lambda-ber-schema/SAXSInstrument) | Small-angle X-ray scattering instruments |
| [BeamlineInstrument](https://w3id.org/lambda-ber-schema/BeamlineInstrument) | Synchrotron beamline specifications |

### Data Collection

| Class | Description |
|-------|-------------|
| [ExperimentRun](https://w3id.org/lambda-ber-schema/ExperimentRun) | Individual data collection sessions with quality metrics |

### Data Processing

| Class | Description |
|-------|-------------|
| [WorkflowRun](https://w3id.org/lambda-ber-schema/WorkflowRun) | Computational processing steps (motion correction, reconstruction, refinement) |

### Data Products

| Class | Description |
|-------|-------------|
| [DataFile](https://w3id.org/lambda-ber-schema/DataFile) | Any files generated or used, with checksums for integrity |
| [Image](https://w3id.org/lambda-ber-schema/Image) | Base class for all imaging data |
| [Micrograph](https://w3id.org/lambda-ber-schema/Micrograph) | 2D electron microscopy images |
| [Movie](https://w3id.org/lambda-ber-schema/Movie) | Cryo-EM movie stacks |
| [FTIRImage](https://w3id.org/lambda-ber-schema/FTIRImage) | Infrared spectroscopy molecular composition maps |
| [FluorescenceImage](https://w3id.org/lambda-ber-schema/FluorescenceImage) | Fluorophore-labeled cellular imaging |
| [OpticalImage](https://w3id.org/lambda-ber-schema/OpticalImage) | Brightfield/phase contrast microscopy |
| [XRFImage](https://w3id.org/lambda-ber-schema/XRFImage) | X-ray fluorescence elemental distribution maps |

## Association Tables

Association tables model many-to-many relationships and can carry relationship metadata:

| Class | Links | Metadata |
|-------|-------|----------|
| [StudySampleAssociation](https://w3id.org/lambda-ber-schema/StudySampleAssociation) | Study ↔ Sample | role (target, control, reference) |
| [StudyExperimentAssociation](https://w3id.org/lambda-ber-schema/StudyExperimentAssociation) | Study ↔ ExperimentRun | |
| [StudyWorkflowAssociation](https://w3id.org/lambda-ber-schema/StudyWorkflowAssociation) | Study ↔ WorkflowRun | |
| [ExperimentSampleAssociation](https://w3id.org/lambda-ber-schema/ExperimentSampleAssociation) | ExperimentRun ↔ Sample | role, preparation used |
| [ExperimentInstrumentAssociation](https://w3id.org/lambda-ber-schema/ExperimentInstrumentAssociation) | ExperimentRun ↔ Instrument | role (primary, detector) |
| [WorkflowExperimentAssociation](https://w3id.org/lambda-ber-schema/WorkflowExperimentAssociation) | WorkflowRun ↔ ExperimentRun | |
| [WorkflowInputAssociation](https://w3id.org/lambda-ber-schema/WorkflowInputAssociation) | WorkflowRun ↔ DataFile | input type |
| [WorkflowOutputAssociation](https://w3id.org/lambda-ber-schema/WorkflowOutputAssociation) | WorkflowRun ↔ DataFile | output type |

## Supporting Classes

### Sample Metadata

| Class | Description |
|-------|-------------|
| [MolecularComposition](https://w3id.org/lambda-ber-schema/MolecularComposition) | Sequences, modifications, ligands |
| [BufferComposition](https://w3id.org/lambda-ber-schema/BufferComposition) | pH, salts, additives |
| [StorageConditions](https://w3id.org/lambda-ber-schema/StorageConditions) | Temperature, duration, method |

### Preparation Details

| Class | Description |
|-------|-------------|
| [CryoEMPreparation](https://w3id.org/lambda-ber-schema/CryoEMPreparation) | Grid type, vitrification parameters |
| [CrystallizationConditions](https://w3id.org/lambda-ber-schema/CrystallizationConditions) | Crystal growth conditions |
| [XRayPreparation](https://w3id.org/lambda-ber-schema/XRayPreparation) | X-ray specific preparation |
| [SAXSPreparation](https://w3id.org/lambda-ber-schema/SAXSPreparation) | SAXS/WAXS preparation |

### Quality & Processing

| Class | Description |
|-------|-------------|
| [QualityMetrics](https://w3id.org/lambda-ber-schema/QualityMetrics) | Resolution, R-factors, validation scores |
| [ComputeResources](https://w3id.org/lambda-ber-schema/ComputeResources) | CPU/GPU hours, memory usage |
| [ExperimentalConditions](https://w3id.org/lambda-ber-schema/ExperimentalConditions) | Temperature, humidity during collection |
| [DataCollectionStrategy](https://w3id.org/lambda-ber-schema/DataCollectionStrategy) | Collection parameters and strategy |

## Key Enumerations

### Sample & Preparation

| Enum | Examples |
|------|----------|
| [SampleTypeEnum](https://w3id.org/lambda-ber-schema/SampleTypeEnum) | protein, nucleic_acid, complex, cell, tissue |
| [PreparationTypeEnum](https://w3id.org/lambda-ber-schema/PreparationTypeEnum) | cryo_em_grid, crystallization, saxs_sample |
| [GridTypeEnum](https://w3id.org/lambda-ber-schema/GridTypeEnum) | holey_carbon, continuous_carbon, graphene |
| [VitrificationMethodEnum](https://w3id.org/lambda-ber-schema/VitrificationMethodEnum) | plunge_freezing, focused_ion_beam |

### Techniques & Methods

| Enum | Examples |
|------|----------|
| [TechniqueEnum](https://w3id.org/lambda-ber-schema/TechniqueEnum) | cryo_em, xray_crystallography, saxs, sans, cryo_et |
| [WorkflowTypeEnum](https://w3id.org/lambda-ber-schema/WorkflowTypeEnum) | motion_correction, ctf_estimation, refinement, model_building |
| [PhasingMethodEnum](https://w3id.org/lambda-ber-schema/PhasingMethodEnum) | molecular_replacement, sad, mad, direct_methods |

### Instruments & Detectors

| Enum | Examples |
|------|----------|
| [DetectorTypeEnum](https://w3id.org/lambda-ber-schema/DetectorTypeEnum) | direct_electron, ccd, cmos |
| [XRaySourceTypeEnum](https://w3id.org/lambda-ber-schema/XRaySourceTypeEnum) | synchrotron, rotating_anode, sealed_tube |
| [BeamlineEnum](https://w3id.org/lambda-ber-schema/BeamlineEnum) | ALS beamlines (8.2.1, 8.2.2, 8.3.1, 12.3.1, etc.) |

### Data & Files

| Enum | Examples |
|------|----------|
| [FileFormatEnum](https://w3id.org/lambda-ber-schema/FileFormatEnum) | mrc, pdb, mmcif, hdf5, tiff |
| [DataTypeEnum](https://w3id.org/lambda-ber-schema/DataTypeEnum) | micrograph, particles, volume, model |

## Supported Techniques

The schema supports a wide range of structural biology techniques:

| Category | Techniques |
|----------|------------|
| **Electron Microscopy** | Cryo-EM single particle, cryo-ET, electron crystallography |
| **X-ray Methods** | Crystallography, SAXS, WAXS, XRF |
| **Neutron Methods** | SANS |
| **Light Microscopy** | Fluorescence, confocal, super-resolution |
| **Spectroscopy** | FTIR imaging, Raman |

## Example: Cryo-EM Study

```yaml
id: dataset:cryo-em-example
title: Structure of Human Ribosome
studies:
  - id: study:ribosome-cryo-em
    title: Cryo-EM analysis of human ribosome
samples:
  - id: sample:ribosome-prep
    sample_code: RIBO-2024-001
    sample_type: complex
    concentration:
      numeric_value: 2.5
      unit: mg/mL
instruments:
  - id: instrument:titan-krios
    instrument_code: TITAN-KRIOS-1
experiment_runs:
  - id: exp:data-collection-1
    experiment_code: RIBO-DC-001
    technique: cryo_em
workflow_runs:
  - id: wf:reconstruction
    workflow_code: RIBO-RECON-001
    workflow_type: refinement
    software_name: RELION
# Association tables link entities
experiment_sample_associations:
  - experiment_id: exp:data-collection-1
    sample_id: sample:ribosome-prep
experiment_instrument_associations:
  - experiment_id: exp:data-collection-1
    instrument_id: instrument:titan-krios
```

## External Links

- **Schema Repository**: [github.com/lambda-ber/lambda-ber-schema](https://github.com/lambda-ber/lambda-ber-schema)
- **W3ID Namespace**: [w3id.org/lambda-ber-schema](https://w3id.org/lambda-ber-schema/)
- **LinkML**: [linkml.io](https://linkml.io/)
