

# Slot: role 



URI: [lambda:role](http://w3id.org/lambda/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |
| [PersonOrganizationAssociation](PersonOrganizationAssociation.md) | M:N link between Person and Organization with role metadata |  no  |
| [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | M:N link between ExperimentRun and Instrument |  no  |
| [StudyPersonAssociation](StudyPersonAssociation.md) | M:N link between Study and Person with role metadata |  no  |
| [StudyOrganizationAssociation](StudyOrganizationAssociation.md) | M:N link between Study and Organization with role metadata - the host institu... |  no  |
| [ExperimentPersonAssociation](ExperimentPersonAssociation.md) | M:N link between ExperimentRun and Person with role metadata - who actually c... |  no  |
| [WorkflowPersonAssociation](WorkflowPersonAssociation.md) | M:N link between WorkflowRun and Person with role metadata - who ran the proc... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:role |
| native | lambda:role |




## LinkML Source

<details>
```yaml
name: role
alias: role
domain_of:
- StudySampleAssociation
- ExperimentSampleAssociation
- SampleProteinAssociation
- ExperimentInstrumentAssociation
- StudyPersonAssociation
- ExperimentPersonAssociation
- WorkflowPersonAssociation
- StudyOrganizationAssociation
- PersonOrganizationAssociation
range: string

```
</details>