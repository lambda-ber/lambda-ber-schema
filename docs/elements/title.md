

# Slot: title 


_A human-readable name or title for this entity_





URI: [dcterms:title](http://purl.org/dc/terms/title)
Alias: title

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |  no  |
| [SANSInstrument](SANSInstrument.md) | Small-angle neutron scattering (SANS) instrument specifications |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [OntologyTerm](OntologyTerm.md) | A term from a controlled vocabulary or ontology |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |
| [Study](Study.md) | A logical grouping of related experiments investigating a research question |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:title |
| native | lambda:title |




## LinkML Source

<details>
```yaml
name: title
description: A human-readable name or title for this entity
from_schema: http://w3id.org/lambda/
rank: 1000
slot_uri: dcterms:title
alias: title
owner: NamedThing
domain_of:
- NamedThing
range: string

```
</details>