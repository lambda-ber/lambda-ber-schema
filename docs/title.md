

# Slot: title 


_A human-readable name or title for this entity_





URI: [dcterms:title](http://purl.org/dc/terms/title)
Alias: title

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [Dataset](Dataset.md) | A collection of studies |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [OntologyTerm](OntologyTerm.md) | A term from a controlled vocabulary or ontology |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [Study](Study.md) | A focused research investigation that groups related samples, experiments, an... |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:title |
| native | lambdaber:title |




## LinkML Source

<details>
```yaml
name: title
description: A human-readable name or title for this entity
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: dcterms:title
alias: title
owner: NamedThing
domain_of:
- NamedThing
range: string

```
</details>