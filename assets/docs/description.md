

# Slot: description 



URI: [lambdaber:description](https://w3id.org/lambda-ber-schema/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [Dataset](Dataset.md) | A collection of studies |  no  |
| [DatabaseCrossReference](DatabaseCrossReference.md) | Cross-references to external databases |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [OntologyTerm](OntologyTerm.md) | A term from a controlled vocabulary or ontology |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [StorageConditions](StorageConditions.md) | Storage conditions for samples |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |
| [BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [QualityMetrics](QualityMetrics.md) | Quality metrics for experiments |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |  no  |
| [FSCCurve](FSCCurve.md) | Fourier Shell Correlation curve data |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) | Base class for technique-specific preparation details |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [ImageFeature](ImageFeature.md) | Semantic annotations describing features identified in images using controlle... |  no  |
| [ComputeResources](ComputeResources.md) | Computational resources used |  no  |
| [CTFEstimationParameters](CTFEstimationParameters.md) | Parameters specific to CTF estimation workflows |  no  |
| [MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |  no  |
| [AttributeGroup](AttributeGroup.md) | A grouping of related data attributes that form a logical unit |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [ConformationalState](ConformationalState.md) | Individual conformational state |  no  |
| [Study](Study.md) | A focused research investigation that groups related samples, experiments, an... |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [CryoEMPreparation](CryoEMPreparation.md) | Cryo-EM specific sample preparation |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [ExperimentalConditions](ExperimentalConditions.md) | Environmental and experimental conditions |  no  |
| [BufferComposition](BufferComposition.md) | Buffer composition for sample storage |  no  |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |
| [LigandInteraction](LigandInteraction.md) | Small molecule/ligand interactions with proteins |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |
| [MotionCorrectionParameters](MotionCorrectionParameters.md) | Parameters specific to motion correction workflows |  no  |
| [ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [ParticlePickingParameters](ParticlePickingParameters.md) | Parameters specific to particle picking workflows |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [SAXSPreparation](SAXSPreparation.md) | SAXS/WAXS specific preparation |  no  |
| [RefinementParameters](RefinementParameters.md) | Parameters specific to 3D refinement workflows |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [MolecularComposition](MolecularComposition.md) | Molecular composition of a sample |  no  |






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