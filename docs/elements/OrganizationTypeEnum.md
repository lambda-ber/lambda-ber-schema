# Enum: OrganizationTypeEnum 




_Kind of organization. Distinct from FacilityTypeEnum, which says what kind of *facility* something is - the Advanced Light Source is a SYNCHROTRON facility and part of a national_laboratory, and both statements are worth keeping._



URI: [lambda:OrganizationTypeEnum](http://w3id.org/lambda/OrganizationTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| national_laboratory | None | National laboratory, e |
| university | None | University or college |
| research_institute | None | Independent or institute-level research organization |
| government_agency | None | Government department or agency |
| funding_agency | None | Body that funds research |
| company | None | Commercial organization |
| hospital | None | Hospital or clinical research centre |
| consortium | None | Collaboration or consortium of member organizations |
| other | None | Organization that fits none of the above |




## Slots

| Name | Description |
| ---  | --- |
| [organization_type](organization_type.md) | What kind of organization this is |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: OrganizationTypeEnum
description: Kind of organization. Distinct from FacilityTypeEnum, which says what
  kind of *facility* something is - the Advanced Light Source is a SYNCHROTRON facility
  and part of a national_laboratory, and both statements are worth keeping.
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  national_laboratory:
    text: national_laboratory
    description: National laboratory, e.g. a DOE national lab
  university:
    text: university
    description: University or college
  research_institute:
    text: research_institute
    description: Independent or institute-level research organization
  government_agency:
    text: government_agency
    description: Government department or agency
  funding_agency:
    text: funding_agency
    description: Body that funds research
  company:
    text: company
    description: Commercial organization
  hospital:
    text: hospital
    description: Hospital or clinical research centre
  consortium:
    text: consortium
    description: Collaboration or consortium of member organizations
  other:
    text: other
    description: Organization that fits none of the above

```
</details>