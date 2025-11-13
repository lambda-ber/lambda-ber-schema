

# Slot: description 



URI: [lambdaber:description](https://w3id.org/lambda-ber-schema/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [BufferComposition](BufferComposition.md) | Buffer composition for sample storage |  no  |
| [ComputeResources](ComputeResources.md) | Computational resources used |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [SAXSPreparation](SAXSPreparation.md) | SAXS/WAXS specific preparation |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [OntologyTerm](OntologyTerm.md) |  |  no  |
| [ImageFeature](ImageFeature.md) | Semantic annotations describing features identified in images using controlle... |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [DatabaseCrossReference](DatabaseCrossReference.md) | Cross-references to external databases |  no  |
| [BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |  no  |
| [StorageConditions](StorageConditions.md) | Storage conditions for samples |  no  |
| [CryoEMPreparation](CryoEMPreparation.md) | Cryo-EM specific sample preparation |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [Study](Study.md) | A focused research investigation that groups related samples, experiments, an... |  no  |
| [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) | Base class for technique-specific preparation details |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [LigandInteraction](LigandInteraction.md) | Small molecule/ligand interactions with proteins |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [AttributeGroup](AttributeGroup.md) | A grouping of related data attributes that form a logical unit |  no  |
| [QualityMetrics](QualityMetrics.md) | Quality metrics for experiments |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Dataset](Dataset.md) | A collection of studies |  no  |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [MolecularComposition](MolecularComposition.md) | Molecular composition of a sample |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [ConformationalState](ConformationalState.md) | Individual conformational state |  no  |
| [ExperimentalConditions](ExperimentalConditions.md) | Environmental and experimental conditions |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:description |
| native | lambdaber:description |




## LinkML Source

<details>
```yaml
name: description
alias: description
domain_of:
- NamedThing
- AttributeGroup
range: string

```
</details>