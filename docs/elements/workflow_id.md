

# Slot: workflow_id 



URI: [lambda:workflow_id](http://w3id.org/lambda/workflow_id)
Alias: workflow_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md) | M:N link between WorkflowRun and source ExperimentRuns |  no  |
| [WorkflowInputAssociation](WorkflowInputAssociation.md) | Links input DataFiles to WorkflowRun |  no  |
| [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | M:N link between Study and WorkflowRun |  no  |
| [WorkflowOutputAssociation](WorkflowOutputAssociation.md) | Links output DataFiles to WorkflowRun |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:workflow_id |
| native | lambda:workflow_id |




## LinkML Source

<details>
```yaml
name: workflow_id
alias: workflow_id
domain_of:
- StudyWorkflowAssociation
- WorkflowExperimentAssociation
- WorkflowInputAssociation
- WorkflowOutputAssociation
range: string

```
</details>