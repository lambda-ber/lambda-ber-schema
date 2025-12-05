
# Class: Study

A focused research investigation that groups related samples, experiments, and data collection around a specific biological question or hypothesis

URI: [lambdaber:Study](https://w3id.org/lambda-ber-schema/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[AggregatedProteinView]<aggregated_protein_views%200..*-++[Study&#124;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image]<images%200..*-++[Study],[DataFile]<data_files%200..*-++[Study],[WorkflowRun]<workflow_runs%200..*-++[Study],[ExperimentRun]<instrument_runs%200..*-++[Study],[SamplePreparation]<sample_preparations%200..*-++[Study],[Sample]<samples%200..*-++[Study],[ProteinConstruct]<protein_constructs%200..*-++[Study],[Dataset]++-%20studies%200..*>[Study],[NamedThing]^-[Study],[SamplePreparation],[Sample],[ProteinConstruct],[NamedThing],[Image],[ExperimentRun],[Dataset],[DataFile],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[AggregatedProteinView]<aggregated_protein_views%200..*-++[Study&#124;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image]<images%200..*-++[Study],[DataFile]<data_files%200..*-++[Study],[WorkflowRun]<workflow_runs%200..*-++[Study],[ExperimentRun]<instrument_runs%200..*-++[Study],[SamplePreparation]<sample_preparations%200..*-++[Study],[Sample]<samples%200..*-++[Study],[ProteinConstruct]<protein_constructs%200..*-++[Study],[Dataset]++-%20studies%200..*>[Study],[NamedThing]^-[Study],[SamplePreparation],[Sample],[ProteinConstruct],[NamedThing],[Image],[ExperimentRun],[Dataset],[DataFile],[AggregatedProteinView])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞studies](dataset__studies.md)*  <sub>0..\*</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [➞protein_constructs](study__protein_constructs.md)  <sub>0..\*</sub>
     * Description: Protein constructs and cloning information
     * Range: [ProteinConstruct](ProteinConstruct.md)
 * [➞samples](study__samples.md)  <sub>0..\*</sub>
     * Description: Experimental samples used in this study, including biological samples 
     * Range: [Sample](Sample.md)
 * [➞sample_preparations](study__sample_preparations.md)  <sub>0..\*</sub>
     * Description: Sample preparation procedures performed in this study
     * Range: [SamplePreparation](SamplePreparation.md)
 * [➞instrument_runs](study__instrument_runs.md)  <sub>0..\*</sub>
     * Description: Experimental data collection runs performed in this study
     * Range: [ExperimentRun](ExperimentRun.md)
 * [➞workflow_runs](study__workflow_runs.md)  <sub>0..\*</sub>
     * Description: Computational workflow executions for data processing in this study
     * Range: [WorkflowRun](WorkflowRun.md)
 * [➞data_files](study__data_files.md)  <sub>0..\*</sub>
     * Description: Data files generated or used in this study
     * Range: [DataFile](DataFile.md)
 * [➞images](study__images.md)  <sub>0..\*</sub>
     * Description: Images acquired or generated in this study
     * Range: [Image](Image.md)
 * [➞aggregated_protein_views](study__aggregated_protein_views.md)  <sub>0..\*</sub>
     * Description: Aggregated functional and structural annotations for proteins in this study
     * Range: [AggregatedProteinView](AggregatedProteinView.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
