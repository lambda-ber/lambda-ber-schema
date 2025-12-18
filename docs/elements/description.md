

# Slot: description 



URI: [lambdaber:description](https://w3id.org/lambda-ber-schema/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |
| [OntologyTerm](OntologyTerm.md) | A term from a controlled vocabulary or ontology |  no  |
| [ExperimentalConditions](ExperimentalConditions.md) | Environmental and experimental conditions |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [QualityMetrics](QualityMetrics.md) | Quality metrics for experiments |  no  |
| [RefinementParameters](RefinementParameters.md) | Parameters specific to 3D refinement workflows |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [SAXSPreparation](SAXSPreparation.md) | SAXS/WAXS specific preparation |  no  |
| [ImageFeature](ImageFeature.md) | Semantic annotations describing features identified in images using controlle... |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [LigandInteraction](LigandInteraction.md) | Small molecule/ligand interactions with proteins |  no  |
| [ConformationalState](ConformationalState.md) | Individual conformational state |  no  |
| [DatabaseCrossReference](DatabaseCrossReference.md) | Cross-references to external databases |  no  |
| [Study](Study.md) | A focused research investigation that groups related samples, experiments, an... |  no  |
| [Dataset](Dataset.md) | A collection of studies |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [BufferComposition](BufferComposition.md) | Buffer composition for sample storage |  no  |
| [ComputeResources](ComputeResources.md) | Computational resources used |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [MotionCorrectionParameters](MotionCorrectionParameters.md) | Parameters specific to motion correction workflows |  no  |
| [ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |  no  |
| [AttributeGroup](AttributeGroup.md) | A grouping of related data attributes that form a logical unit |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [StorageConditions](StorageConditions.md) | Storage conditions for samples |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |
| [FSCCurve](FSCCurve.md) | Fourier Shell Correlation curve data |  no  |
| [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) | Base class for technique-specific preparation details |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [CTFEstimationParameters](CTFEstimationParameters.md) | Parameters specific to CTF estimation workflows |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [ParticlePickingParameters](ParticlePickingParameters.md) | Parameters specific to particle picking workflows |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [MolecularComposition](MolecularComposition.md) | Molecular composition of a sample |  no  |
| [CryoEMPreparation](CryoEMPreparation.md) | Cryo-EM specific sample preparation |  no  |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |






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