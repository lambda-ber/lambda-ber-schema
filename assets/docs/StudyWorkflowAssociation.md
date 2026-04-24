
# Class: StudyWorkflowAssociation

M:N link between Study and WorkflowRun

URI: [lambda:StudyWorkflowAssociation](http://w3id.org/lambda/StudyWorkflowAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[WorkflowRun]<workflow_id%201..1-%20[StudyWorkflowAssociation],[Study]<study_id%201..1-%20[StudyWorkflowAssociation],[Dataset]++-%20study_workflow_associations%200..*>[StudyWorkflowAssociation],[Study],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[WorkflowRun]<workflow_id%201..1-%20[StudyWorkflowAssociation],[Study]<study_id%201..1-%20[StudyWorkflowAssociation],[Dataset]++-%20study_workflow_associations%200..*>[StudyWorkflowAssociation],[Study],[Dataset])

## Referenced by Class

 *  **None** *[➞study_workflow_associations](dataset__study_workflow_associations.md)*  <sub>0..\*</sub>  **[StudyWorkflowAssociation](StudyWorkflowAssociation.md)**

## Attributes


### Own

 * [➞study_id](studyWorkflowAssociation__study_id.md)  <sub>1..1</sub>
     * Description: Reference to the study
     * Range: [Study](Study.md)
 * [➞workflow_id](studyWorkflowAssociation__workflow_id.md)  <sub>1..1</sub>
     * Description: Reference to the workflow run
     * Range: [WorkflowRun](WorkflowRun.md)
