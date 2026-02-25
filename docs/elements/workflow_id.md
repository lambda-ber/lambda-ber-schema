

# Slot: workflow_id 



URI: [lambdaber:workflow_id](https://w3id.org/lambda-ber-schema/workflow_id)
Alias: workflow_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowOutputAssociation](WorkflowOutputAssociation.md) | Links output DataFiles to WorkflowRun |  no  |
| [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md) | M:N link between WorkflowRun and source ExperimentRuns |  no  |
| [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | M:N link between Study and WorkflowRun |  no  |
| [WorkflowInputAssociation](WorkflowInputAssociation.md) | Links input DataFiles to WorkflowRun |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:workflow_id |
| native | lambdaber:workflow_id |




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