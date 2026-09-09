

# Slot: award_number 


_Grant or award number, where the organization is a funder. Distinct from Study.proposal_id, which is the facility's beamtime allocation rather than the funding that paid for the science._





URI: [lambda:award_number](http://w3id.org/lambda/award_number)
Alias: award_number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyOrganizationAssociation](StudyOrganizationAssociation.md) | M:N link between Study and Organization with role metadata - the host institu... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:award_number |
| native | lambda:award_number |




## LinkML Source

<details>
```yaml
name: award_number
description: Grant or award number, where the organization is a funder. Distinct from
  Study.proposal_id, which is the facility's beamtime allocation rather than the funding
  that paid for the science.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: award_number
owner: StudyOrganizationAssociation
domain_of:
- StudyOrganizationAssociation
range: string

```
</details>