

# Slot: sample_id 



URI: [lambda:sample_id](http://w3id.org/lambda/sample_id)
Alias: sample_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:sample_id |
| native | lambda:sample_id |




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