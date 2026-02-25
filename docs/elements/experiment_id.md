

# Slot: experiment_id 



URI: [lambdaber:experiment_id](https://w3id.org/lambda-ber-schema/experiment_id)
Alias: experiment_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md) | M:N link between WorkflowRun and source ExperimentRuns |  no  |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |
| [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | M:N link between ExperimentRun and Instrument |  no  |
| [StudyExperimentAssociation](StudyExperimentAssociation.md) | M:N link between Study and ExperimentRun |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:experiment_id |
| native | lambdaber:experiment_id |




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