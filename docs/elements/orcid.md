

# Slot: orcid 


_ORCID identifier for the person_





URI: [lambda:orcid](http://w3id.org/lambda/orcid)
Alias: orcid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person involved in producing, processing or publishing data - a principal i... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$`




## Comments

* Persistent identifier for the individual; the preferred way to identify a person
* Example: https://orcid.org/0000-0002-1885-1511

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:orcid |
| native | lambda:orcid |




## LinkML Source

<details>
```yaml
name: orcid
description: ORCID identifier for the person
comments:
- Persistent identifier for the individual; the preferred way to identify a person
- 'Example: https://orcid.org/0000-0002-1885-1511'
from_schema: http://w3id.org/lambda/
rank: 1000
alias: orcid
owner: Person
domain_of:
- Person
range: uriorcurie
pattern: ^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]$

```
</details>