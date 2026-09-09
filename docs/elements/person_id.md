

# Slot: person_id 



URI: [lambda:person_id](http://w3id.org/lambda/person_id)
Alias: person_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyPersonAssociation](StudyPersonAssociation.md) | M:N link between Study and Person with role metadata |  no  |
| [ExperimentPersonAssociation](ExperimentPersonAssociation.md) | M:N link between ExperimentRun and Person with role metadata - who actually c... |  no  |
| [WorkflowPersonAssociation](WorkflowPersonAssociation.md) | M:N link between WorkflowRun and Person with role metadata - who ran the proc... |  no  |
| [PersonOrganizationAssociation](PersonOrganizationAssociation.md) | M:N link between Person and Organization with role metadata |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:person_id |
| native | lambda:person_id |




## LinkML Source

<details>
```yaml
name: person_id
alias: person_id
domain_of:
- StudyPersonAssociation
- ExperimentPersonAssociation
- WorkflowPersonAssociation
- PersonOrganizationAssociation
range: string

```
</details>