

# Slot: affiliation_ror 


_Research Organization Registry (ROR) identifier for the affiliated institution_





URI: [lambda:affiliation_ror](http://w3id.org/lambda/affiliation_ror)
Alias: affiliation_ror

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person involved in producing, processing or publishing data - a principal i... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^https://ror\.org/\w+$`




## Comments

* Free-text convenience, retained for sources that publish only an affiliation string. Where the institution can be resolved, prefer an Organization record linked by PersonOrganizationAssociation, which can carry more than one affiliation and date them.

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:affiliation_ror |
| native | lambda:affiliation_ror |




## LinkML Source

<details>
```yaml
name: affiliation_ror
description: Research Organization Registry (ROR) identifier for the affiliated institution
comments:
- Free-text convenience, retained for sources that publish only an affiliation string.
  Where the institution can be resolved, prefer an Organization record linked by PersonOrganizationAssociation,
  which can carry more than one affiliation and date them.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: affiliation_ror
owner: Person
domain_of:
- Person
range: uriorcurie
pattern: ^https://ror\.org/\w+$

```
</details>