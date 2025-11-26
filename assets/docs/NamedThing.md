
# Class: NamedThing

A named thing

URI: [lambdaber:NamedThing](https://w3id.org/lambda-ber-schema/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[Study],[SamplePreparation],[Sample],[ProteinConstruct],[ProteinAnnotation],[OntologyTerm],[NamedThing&#124;id:uriorcurie;title:string%20%3F;description:string%20%3F]^-[WorkflowRun],[NamedThing]^-[Study],[NamedThing]^-[SamplePreparation],[NamedThing]^-[Sample],[NamedThing]^-[ProteinConstruct],[NamedThing]^-[ProteinAnnotation],[NamedThing]^-[OntologyTerm],[NamedThing]^-[MeasurementConditions],[NamedThing]^-[Instrument],[NamedThing]^-[Image],[NamedThing]^-[ExperimentRun],[NamedThing]^-[Dataset],[NamedThing]^-[DataFile],[NamedThing]^-[ConformationalEnsemble],[NamedThing]^-[AggregatedProteinView],[MeasurementConditions],[Instrument],[Image],[ExperimentRun],[Dataset],[DataFile],[ConformationalEnsemble],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[Study],[SamplePreparation],[Sample],[ProteinConstruct],[ProteinAnnotation],[OntologyTerm],[NamedThing&#124;id:uriorcurie;title:string%20%3F;description:string%20%3F]^-[WorkflowRun],[NamedThing]^-[Study],[NamedThing]^-[SamplePreparation],[NamedThing]^-[Sample],[NamedThing]^-[ProteinConstruct],[NamedThing]^-[ProteinAnnotation],[NamedThing]^-[OntologyTerm],[NamedThing]^-[MeasurementConditions],[NamedThing]^-[Instrument],[NamedThing]^-[Image],[NamedThing]^-[ExperimentRun],[NamedThing]^-[Dataset],[NamedThing]^-[DataFile],[NamedThing]^-[ConformationalEnsemble],[NamedThing]^-[AggregatedProteinView],[MeasurementConditions],[Instrument],[Image],[ExperimentRun],[Dataset],[DataFile],[ConformationalEnsemble],[AggregatedProteinView])

## Children

 * [AggregatedProteinView](AggregatedProteinView.md) - Aggregated view of all structural and functional data for a protein
 * [ConformationalEnsemble](ConformationalEnsemble.md) - Ensemble of conformational states for a protein
 * [DataFile](DataFile.md) - A data file generated or used in the study
 * [Dataset](Dataset.md) - A collection of studies
 * [ExperimentRun](ExperimentRun.md) - An experimental data collection session
 * [Image](Image.md) - An image file from structural biology experiments
 * [Instrument](Instrument.md) - An instrument used to collect data
 * [MeasurementConditions](MeasurementConditions.md) - Conditions under which biophysical measurements were made
 * [OntologyTerm](OntologyTerm.md) - A term from a controlled vocabulary or ontology
 * [ProteinAnnotation](ProteinAnnotation.md) - Base class for all protein-related functional and structural annotations
 * [ProteinConstruct](ProteinConstruct.md) - Detailed information about a protein construct including cloning and sequence design
 * [Sample](Sample.md) - A biological sample used in structural biology experiments
 * [SamplePreparation](SamplePreparation.md) - A process that prepares a sample for imaging
 * [Study](Study.md) - A focused research investigation that groups related samples, experiments, and data collection around a specific biological question or hypothesis
 * [WorkflowRun](WorkflowRun.md) - A computational processing workflow execution

## Referenced by Class


## Attributes


### Own

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
