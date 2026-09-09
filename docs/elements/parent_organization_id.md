

# Slot: parent_organization_id 


_The organization this one belongs to - a light source's national laboratory, a department's university. Self-referential, as Sample.parent_sample_id is._





URI: [lambda:parent_organization_id](http://w3id.org/lambda/parent_organization_id)
Alias: parent_organization_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | An institution, facility, laboratory or funding body - a national laboratory,... |  no  |






## Properties

* Range: [Organization](Organization.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:parent_organization_id |
| native | lambda:parent_organization_id |




## LinkML Source

<details>
```yaml
name: parent_organization_id
description: The organization this one belongs to - a light source's national laboratory,
  a department's university. Self-referential, as Sample.parent_sample_id is.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: parent_organization_id
owner: Organization
domain_of:
- Organization
range: Organization

```
</details>