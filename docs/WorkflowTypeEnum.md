# Enum: WorkflowTypeEnum 




_Types of processing workflows_



URI: [lambdaber:WorkflowTypeEnum](https://w3id.org/lambda-ber-schema/WorkflowTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| motion_correction | None | Motion correction for cryo-EM |
| ctf_estimation | None | CTF estimation |
| particle_picking | None | Particle picking |
| classification_2d | None | 2D classification |
| classification_3d | None | 3D classification |
| refinement | None | 3D refinement |
| model_building | None | Atomic model building |
| phasing | None | Phase determination |
| integration | None | Data integration |
| scaling | None | Data scaling |
| saxs_analysis | None | SAXS data analysis |
| em_2d_classification | None | EM 2D classification |
| mass_spec_deconvolution | None | Mass spectrometry deconvolution |
| particle_extraction | None | Particle extraction from micrographs |
| ab_initio | None | Ab initio 3D reconstruction |
| postprocessing | None | Map post-processing and sharpening |
| map_validation | None | 3D map validation |
| model_refinement | None | Atomic model refinement |
| model_validation | None | Model validation and quality assessment |




## Slots

| Name | Description |
| ---  | --- |
| [workflow_type](workflow_type.md) | Type of processing workflow |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: WorkflowTypeEnum
description: Types of processing workflows
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  motion_correction:
    text: motion_correction
    description: Motion correction for cryo-EM
  ctf_estimation:
    text: ctf_estimation
    description: CTF estimation
  particle_picking:
    text: particle_picking
    description: Particle picking
  classification_2d:
    text: classification_2d
    description: 2D classification
  classification_3d:
    text: classification_3d
    description: 3D classification
  refinement:
    text: refinement
    description: 3D refinement
  model_building:
    text: model_building
    description: Atomic model building
  phasing:
    text: phasing
    description: Phase determination
  integration:
    text: integration
    description: Data integration
  scaling:
    text: scaling
    description: Data scaling
  saxs_analysis:
    text: saxs_analysis
    description: SAXS data analysis
  em_2d_classification:
    text: em_2d_classification
    description: EM 2D classification
  mass_spec_deconvolution:
    text: mass_spec_deconvolution
    description: Mass spectrometry deconvolution
  particle_extraction:
    text: particle_extraction
    description: Particle extraction from micrographs
  ab_initio:
    text: ab_initio
    description: Ab initio 3D reconstruction
  postprocessing:
    text: postprocessing
    description: Map post-processing and sharpening
  map_validation:
    text: map_validation
    description: 3D map validation
  model_refinement:
    text: model_refinement
    description: Atomic model refinement
  model_validation:
    text: model_validation
    description: Model validation and quality assessment

```
</details>