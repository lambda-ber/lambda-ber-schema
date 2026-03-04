

# Slot: sample_id 



URI: [lambdaber:sample_id](https://w3id.org/lambda-ber-schema/sample_id)
Alias: sample_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:sample_id |
| native | lambdaber:sample_id |




## LinkML Source

<details>
```yaml
name: sample_id
alias: sample_id
domain_of:
- SamplePreparation
- StudySampleAssociation
- ExperimentSampleAssociation
range: string

```
</details>