

# Slot: id 


_Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration._





URI: [lambdaber:id](https://w3id.org/lambda-ber-schema/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [Study](Study.md) | A focused research investigation that groups related samples, experiments, an... |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [Dataset](Dataset.md) | A collection of studies |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |  no  |
| [OntologyTerm](OntologyTerm.md) |  |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |






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