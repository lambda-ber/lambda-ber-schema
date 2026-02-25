

# Slot: study_id 



URI: [lambdaber:study_id](https://w3id.org/lambda-ber-schema/study_id)
Alias: study_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyExperimentAssociation](StudyExperimentAssociation.md) | M:N link between Study and ExperimentRun |  no  |
| [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | M:N link between Study and WorkflowRun |  no  |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:study_id |
| native | lambdaber:study_id |




## LinkML Source

<details>
```yaml
name: study_id
alias: study_id
domain_of:
- StudySampleAssociation
- StudyExperimentAssociation
- StudyWorkflowAssociation
range: string

```
</details>