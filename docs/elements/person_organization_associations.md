

# Slot: person_organization_associations 


_Links between people and organizations (M:N with role and dates)_





URI: [lambda:person_organization_associations](http://w3id.org/lambda/person_organization_associations)
Alias: person_organization_associations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |






## Properties

* Range: [PersonOrganizationAssociation](PersonOrganizationAssociation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:person_organization_associations |
| native | lambda:person_organization_associations |




## LinkML Source

<details>
```yaml
name: person_organization_associations
description: Links between people and organizations (M:N with role and dates)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: person_organization_associations
owner: Dataset
domain_of:
- Dataset
range: PersonOrganizationAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>