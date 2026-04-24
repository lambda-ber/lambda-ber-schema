
# Class: WorkflowOutputAssociation

Links output DataFiles to WorkflowRun

URI: [lambda:WorkflowOutputAssociation](http://w3id.org/lambda/WorkflowOutputAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[DataFile]<file_id%201..1-%20[WorkflowOutputAssociation&#124;output_type:OutputTypeEnum%20%3F],[WorkflowRun]<workflow_id%201..1-%20[WorkflowOutputAssociation],[Dataset]++-%20workflow_output_associations%200..*>[WorkflowOutputAssociation],[Dataset],[DataFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[DataFile]<file_id%201..1-%20[WorkflowOutputAssociation&#124;output_type:OutputTypeEnum%20%3F],[WorkflowRun]<workflow_id%201..1-%20[WorkflowOutputAssociation],[Dataset]++-%20workflow_output_associations%200..*>[WorkflowOutputAssociation],[Dataset],[DataFile])

## Referenced by Class

 *  **None** *[➞workflow_output_associations](dataset__workflow_output_associations.md)*  <sub>0..\*</sub>  **[WorkflowOutputAssociation](WorkflowOutputAssociation.md)**

## Attributes


### Own

 * [➞workflow_id](workflowOutputAssociation__workflow_id.md)  <sub>1..1</sub>
     * Description: Reference to the workflow run
     * Range: [WorkflowRun](WorkflowRun.md)
 * [➞file_id](workflowOutputAssociation__file_id.md)  <sub>1..1</sub>
     * Description: Reference to the output data file
     * Range: [DataFile](DataFile.md)
 * [➞output_type](workflowOutputAssociation__output_type.md)  <sub>0..1</sub>
     * Description: Type of output from the workflow
     * Range: [OutputTypeEnum](OutputTypeEnum.md)
