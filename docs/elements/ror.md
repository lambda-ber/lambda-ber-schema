

# Slot: ror 


_Research Organization Registry (ROR) identifier for the organization_





URI: [lambda:ror](http://w3id.org/lambda/ror)
Alias: ror

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | An institution, facility, laboratory or funding body - a national laboratory,... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^https://ror\.org/\w+$`




## Comments

* The preferred way to identify an organization
* Every FacilityEnum permissible value already carries its ROR as the term's meaning
* Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ror |
| native | lambda:ror |




## LinkML Source

<details>
```yaml
name: ror
description: Research Organization Registry (ROR) identifier for the organization
comments:
- The preferred way to identify an organization
- Every FacilityEnum permissible value already carries its ROR as the term's meaning
- 'Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)'
from_schema: http://w3id.org/lambda/
rank: 1000
alias: ror
owner: Organization
domain_of:
- Organization
range: uriorcurie
pattern: ^https://ror\.org/\w+$

```
</details>