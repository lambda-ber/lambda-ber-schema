
# Class: ExperimentSampleAssociation

M:N link between ExperimentRun and Sample with role metadata

URI: [lambda:ExperimentSampleAssociation](http://w3id.org/lambda/ExperimentSampleAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SamplePreparation],[Sample],[SamplePreparation]<preparation_id%200..1-%20[ExperimentSampleAssociation&#124;role:ExperimentSampleRoleEnum%20%3F],[Sample]<sample_id%201..1-%20[ExperimentSampleAssociation],[ExperimentRun]<experiment_id%201..1-%20[ExperimentSampleAssociation],[Dataset]++-%20experiment_sample_associations%200..*>[ExperimentSampleAssociation],[ExperimentRun],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[SamplePreparation],[Sample],[SamplePreparation]<preparation_id%200..1-%20[ExperimentSampleAssociation&#124;role:ExperimentSampleRoleEnum%20%3F],[Sample]<sample_id%201..1-%20[ExperimentSampleAssociation],[ExperimentRun]<experiment_id%201..1-%20[ExperimentSampleAssociation],[Dataset]++-%20experiment_sample_associations%200..*>[ExperimentSampleAssociation],[ExperimentRun],[Dataset])

## Referenced by Class

 *  **None** *[➞experiment_sample_associations](dataset__experiment_sample_associations.md)*  <sub>0..\*</sub>  **[ExperimentSampleAssociation](ExperimentSampleAssociation.md)**

## Attributes


### Own

 * [➞experiment_id](experimentSampleAssociation__experiment_id.md)  <sub>1..1</sub>
     * Description: Reference to the experiment run
     * Range: [ExperimentRun](ExperimentRun.md)
 * [➞sample_id](experimentSampleAssociation__sample_id.md)  <sub>1..1</sub>
     * Description: Reference to the sample
     * Range: [Sample](Sample.md)
 * [➞role](experimentSampleAssociation__role.md)  <sub>0..1</sub>
     * Description: Role of sample in experiment
     * Range: [ExperimentSampleRoleEnum](ExperimentSampleRoleEnum.md)
 * [➞preparation_id](experimentSampleAssociation__preparation_id.md)  <sub>0..1</sub>
     * Description: Specific preparation used for this sample in this experiment
     * Range: [SamplePreparation](SamplePreparation.md)
