# Enum: OrganizationRoleEnum 




_Capacity in which an organization is attached to a study, or a person to an organization. One vocabulary rather than one per association, matching PersonRoleEnum: these are roles in a relationship, and the same organization is often attached in more than one way._



URI: [lambda:OrganizationRoleEnum](http://w3id.org/lambda/OrganizationRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| host_institution | None | Institution where the work was carried out |
| operating_institution | None | Institution that operates the facility used |
| funder | None | Funded the work; pair with an award number on the association |
| collaborating_institution | None | Contributed to the work without hosting it |
| depositor | None | Deposited the data to an archive or repository |
| primary_affiliation | None | A person's main institutional affiliation |
| secondary_affiliation | None | A further current affiliation held by a person |
| former_affiliation | None | An affiliation a person held previously |








## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: OrganizationRoleEnum
description: 'Capacity in which an organization is attached to a study, or a person
  to an organization. One vocabulary rather than one per association, matching PersonRoleEnum:
  these are roles in a relationship, and the same organization is often attached in
  more than one way.'
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  host_institution:
    text: host_institution
    description: Institution where the work was carried out
  operating_institution:
    text: operating_institution
    description: Institution that operates the facility used
  funder:
    text: funder
    description: Funded the work; pair with an award number on the association
  collaborating_institution:
    text: collaborating_institution
    description: Contributed to the work without hosting it
  depositor:
    text: depositor
    description: Deposited the data to an archive or repository
  primary_affiliation:
    text: primary_affiliation
    description: A person's main institutional affiliation
  secondary_affiliation:
    text: secondary_affiliation
    description: A further current affiliation held by a person
  former_affiliation:
    text: former_affiliation
    description: An affiliation a person held previously

```
</details>