

# Slot: id 


_Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration._





URI: [lambdaber:id](https://w3id.org/lambda-ber-schema/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [OntologyTerm](OntologyTerm.md) |  |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [Study](Study.md) | A focused research investigation that groups related samples, experiments, an... |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Dataset](Dataset.md) | A collection of studies |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:id |
| native | lambdaber:id |




## LinkML Source

<details>
```yaml
name: id
description: Globally unique identifier as an IRI or CURIE for machine processing
  and external references. Used for linking data across systems and semantic web integration.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
identifier: true
alias: id
owner: NamedThing
domain_of:
- NamedThing
range: uriorcurie
required: true

```
</details>