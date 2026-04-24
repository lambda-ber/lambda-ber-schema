
# Class: WorkflowExperimentAssociation

M:N link between WorkflowRun and source ExperimentRuns

URI: [lambda:WorkflowExperimentAssociation](http://w3id.org/lambda/WorkflowExperimentAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[ExperimentRun]<experiment_id%201..1-%20[WorkflowExperimentAssociation],[WorkflowRun]<workflow_id%201..1-%20[WorkflowExperimentAssociation],[Dataset]++-%20workflow_experiment_associations%200..*>[WorkflowExperimentAssociation],[ExperimentRun],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[ExperimentRun]<experiment_id%201..1-%20[WorkflowExperimentAssociation],[WorkflowRun]<workflow_id%201..1-%20[WorkflowExperimentAssociation],[Dataset]++-%20workflow_experiment_associations%200..*>[WorkflowExperimentAssociation],[ExperimentRun],[Dataset])

## Referenced by Class

 *  **None** *[➞workflow_experiment_associations](dataset__workflow_experiment_associations.md)*  <sub>0..\*</sub>  **[WorkflowExperimentAssociation](WorkflowExperimentAssociation.md)**

## Attributes


### Own

 * [➞workflow_id](workflowExperimentAssociation__workflow_id.md)  <sub>1..1</sub>
     * Description: Reference to the workflow run
     * Range: [WorkflowRun](WorkflowRun.md)
 * [➞experiment_id](workflowExperimentAssociation__experiment_id.md)  <sub>1..1</sub>
     * Description: Reference to the source experiment run
     * Range: [ExperimentRun](ExperimentRun.md)
