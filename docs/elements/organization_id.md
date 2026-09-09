

# Slot: organization_id 



URI: [lambda:organization_id](http://w3id.org/lambda/organization_id)
Alias: organization_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyOrganizationAssociation](StudyOrganizationAssociation.md) | M:N link between Study and Organization with role metadata - the host institu... |  no  |
| [PersonOrganizationAssociation](PersonOrganizationAssociation.md) | M:N link between Person and Organization with role metadata |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:organization_id |
| native | lambda:organization_id |




## LinkML Source

<details>
```yaml
name: organization_id
alias: organization_id
domain_of:
- StudyOrganizationAssociation
- PersonOrganizationAssociation
range: string

```
</details>