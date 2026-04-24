
# Class: Dataset

Root container holding flat entity collections and association tables. Follows relational database design patterns for structural biology data.

URI: [lambda:Dataset](http://w3id.org/lambda/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[WorkflowOutputAssociation],[WorkflowInputAssociation],[WorkflowExperimentAssociation],[StudyWorkflowAssociation],[StudySampleAssociation],[StudyExperimentAssociation],[Study],[SamplePreparation],[Sample],[ProteinConstruct],[NamedThing],[Instrument],[Image],[ExperimentSampleAssociation],[ExperimentRun],[ExperimentInstrumentAssociation],[WorkflowOutputAssociation]<workflow_output_associations%200..*-++[Dataset&#124;keywords:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[WorkflowInputAssociation]<workflow_input_associations%200..*-++[Dataset],[WorkflowExperimentAssociation]<workflow_experiment_associations%200..*-++[Dataset],[ExperimentInstrumentAssociation]<experiment_instrument_associations%200..*-++[Dataset],[ExperimentSampleAssociation]<experiment_sample_associations%200..*-++[Dataset],[StudyWorkflowAssociation]<study_workflow_associations%200..*-++[Dataset],[StudyExperimentAssociation]<study_experiment_associations%200..*-++[Dataset],[StudySampleAssociation]<study_sample_associations%200..*-++[Dataset],[Image]<images%200..*-++[Dataset],[DataFile]<data_files%200..*-++[Dataset],[WorkflowRun]<workflow_runs%200..*-++[Dataset],[ExperimentRun]<experiment_runs%200..*-++[Dataset],[SamplePreparation]<sample_preparations%200..*-++[Dataset],[Sample]<samples%200..*-++[Dataset],[ProteinConstruct]<protein_constructs%200..*-++[Dataset],[Instrument]<instruments%200..*-++[Dataset],[Study]<studies%200..*-++[Dataset],[NamedThing]^-[Dataset],[DataFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[WorkflowOutputAssociation],[WorkflowInputAssociation],[WorkflowExperimentAssociation],[StudyWorkflowAssociation],[StudySampleAssociation],[StudyExperimentAssociation],[Study],[SamplePreparation],[Sample],[ProteinConstruct],[NamedThing],[Instrument],[Image],[ExperimentSampleAssociation],[ExperimentRun],[ExperimentInstrumentAssociation],[WorkflowOutputAssociation]<workflow_output_associations%200..*-++[Dataset&#124;keywords:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[WorkflowInputAssociation]<workflow_input_associations%200..*-++[Dataset],[WorkflowExperimentAssociation]<workflow_experiment_associations%200..*-++[Dataset],[ExperimentInstrumentAssociation]<experiment_instrument_associations%200..*-++[Dataset],[ExperimentSampleAssociation]<experiment_sample_associations%200..*-++[Dataset],[StudyWorkflowAssociation]<study_workflow_associations%200..*-++[Dataset],[StudyExperimentAssociation]<study_experiment_associations%200..*-++[Dataset],[StudySampleAssociation]<study_sample_associations%200..*-++[Dataset],[Image]<images%200..*-++[Dataset],[DataFile]<data_files%200..*-++[Dataset],[WorkflowRun]<workflow_runs%200..*-++[Dataset],[ExperimentRun]<experiment_runs%200..*-++[Dataset],[SamplePreparation]<sample_preparations%200..*-++[Dataset],[Sample]<samples%200..*-++[Dataset],[ProteinConstruct]<protein_constructs%200..*-++[Dataset],[Instrument]<instruments%200..*-++[Dataset],[Study]<studies%200..*-++[Dataset],[NamedThing]^-[Dataset],[DataFile])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Attributes


### Own

 * [➞keywords](dataset__keywords.md)  <sub>0..\*</sub>
     * Description: Keywords or tags describing the dataset for search and categorization
     * Range: [String](types/String.md)
 * [➞studies](dataset__studies.md)  <sub>0..\*</sub>
     * Description: All studies in this dataset
     * Range: [Study](Study.md)
 * [➞instruments](dataset__instruments.md)  <sub>0..\*</sub>
     * Description: All instruments used across studies
     * Range: [Instrument](Instrument.md)
 * [➞protein_constructs](dataset__protein_constructs.md)  <sub>0..\*</sub>
     * Description: All protein constructs
     * Range: [ProteinConstruct](ProteinConstruct.md)
 * [➞samples](dataset__samples.md)  <sub>0..\*</sub>
     * Description: All samples across all studies
     * Range: [Sample](Sample.md)
 * [➞sample_preparations](dataset__sample_preparations.md)  <sub>0..\*</sub>
     * Description: All sample preparations
     * Range: [SamplePreparation](SamplePreparation.md)
 * [➞experiment_runs](dataset__experiment_runs.md)  <sub>0..\*</sub>
     * Description: All experiment runs (data collection sessions)
     * Range: [ExperimentRun](ExperimentRun.md)
 * [➞workflow_runs](dataset__workflow_runs.md)  <sub>0..\*</sub>
     * Description: All workflow runs (computational processing)
     * Range: [WorkflowRun](WorkflowRun.md)
 * [➞data_files](dataset__data_files.md)  <sub>0..\*</sub>
     * Description: All data files
     * Range: [DataFile](DataFile.md)
 * [➞images](dataset__images.md)  <sub>0..\*</sub>
     * Description: All images
     * Range: [Image](Image.md)
 * [➞study_sample_associations](dataset__study_sample_associations.md)  <sub>0..\*</sub>
     * Description: Links between studies and samples (M:N)
     * Range: [StudySampleAssociation](StudySampleAssociation.md)
 * [➞study_experiment_associations](dataset__study_experiment_associations.md)  <sub>0..\*</sub>
     * Description: Links between studies and experiments (M:N)
     * Range: [StudyExperimentAssociation](StudyExperimentAssociation.md)
 * [➞study_workflow_associations](dataset__study_workflow_associations.md)  <sub>0..\*</sub>
     * Description: Links between studies and workflows (M:N)
     * Range: [StudyWorkflowAssociation](StudyWorkflowAssociation.md)
 * [➞experiment_sample_associations](dataset__experiment_sample_associations.md)  <sub>0..\*</sub>
     * Description: Links between experiments and samples (M:N with role)
     * Range: [ExperimentSampleAssociation](ExperimentSampleAssociation.md)
 * [➞experiment_instrument_associations](dataset__experiment_instrument_associations.md)  <sub>0..\*</sub>
     * Description: Links between experiments and instruments (M:N)
     * Range: [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md)
 * [➞workflow_experiment_associations](dataset__workflow_experiment_associations.md)  <sub>0..\*</sub>
     * Description: Links between workflows and source experiments (M:N)
     * Range: [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md)
 * [➞workflow_input_associations](dataset__workflow_input_associations.md)  <sub>0..\*</sub>
     * Description: Links between workflows and input files
     * Range: [WorkflowInputAssociation](WorkflowInputAssociation.md)
 * [➞workflow_output_associations](dataset__workflow_output_associations.md)  <sub>0..\*</sub>
     * Description: Links between workflows and output files
     * Range: [WorkflowOutputAssociation](WorkflowOutputAssociation.md)

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
