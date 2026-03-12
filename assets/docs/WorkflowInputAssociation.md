
# Class: WorkflowInputAssociation

Links input DataFiles to WorkflowRun

URI: [lambda:WorkflowInputAssociation](http://w3id.org/lambda/WorkflowInputAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[DataFile]<file_id%201..1-%20[WorkflowInputAssociation&#124;input_type:InputTypeEnum%20%3F],[WorkflowRun]<workflow_id%201..1-%20[WorkflowInputAssociation],[Dataset]++-%20workflow_input_associations%200..*>[WorkflowInputAssociation],[Dataset],[DataFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun],[DataFile]<file_id%201..1-%20[WorkflowInputAssociation&#124;input_type:InputTypeEnum%20%3F],[WorkflowRun]<workflow_id%201..1-%20[WorkflowInputAssociation],[Dataset]++-%20workflow_input_associations%200..*>[WorkflowInputAssociation],[Dataset],[DataFile])

## Referenced by Class

 *  **None** *[➞workflow_input_associations](dataset__workflow_input_associations.md)*  <sub>0..\*</sub>  **[WorkflowInputAssociation](WorkflowInputAssociation.md)**

## Attributes


### Own

 * [➞workflow_id](workflowInputAssociation__workflow_id.md)  <sub>1..1</sub>
     * Description: Reference to the workflow run
     * Range: [WorkflowRun](WorkflowRun.md)
 * [➞file_id](workflowInputAssociation__file_id.md)  <sub>1..1</sub>
     * Description: Reference to the input data file
     * Range: [DataFile](DataFile.md)
 * [➞input_type](workflowInputAssociation__input_type.md)  <sub>0..1</sub>
     * Description: Type of input for the workflow
     * Range: [InputTypeEnum](InputTypeEnum.md)
