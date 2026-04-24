

# Slot: study_id 



URI: [lambda:study_id](http://w3id.org/lambda/study_id)
Alias: study_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | M:N link between Study and WorkflowRun |  no  |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |
| [StudyExperimentAssociation](StudyExperimentAssociation.md) | M:N link between Study and ExperimentRun |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:study_id |
| native | lambda:study_id |




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