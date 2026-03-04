

# Slot: role 



URI: [lambdaber:role](https://w3id.org/lambda-ber-schema/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |
| [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | M:N link between ExperimentRun and Instrument |  no  |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:role |
| native | lambdaber:role |




## LinkML Source

<details>
```yaml
name: role
alias: role
domain_of:
- StudySampleAssociation
- ExperimentSampleAssociation
- ExperimentInstrumentAssociation
range: string

```
</details>