

# Slot: experiment_id 



URI: [lambda:experiment_id](http://w3id.org/lambda/experiment_id)
Alias: experiment_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyExperimentAssociation](StudyExperimentAssociation.md) | M:N link between Study and ExperimentRun |  no  |
| [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md) | M:N link between WorkflowRun and source ExperimentRuns |  no  |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |
| [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | M:N link between ExperimentRun and Instrument |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:experiment_id |
| native | lambda:experiment_id |




## LinkML Source

<details>
```yaml
name: experiment_id
alias: experiment_id
domain_of:
- StudyExperimentAssociation
- ExperimentSampleAssociation
- ExperimentInstrumentAssociation
- WorkflowExperimentAssociation
range: string

```
</details>