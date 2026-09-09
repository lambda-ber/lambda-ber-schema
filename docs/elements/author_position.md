

# Slot: author_position 


_Position in the author list, where authorship order is meaningful. 1 is first author. Absent when the source does not state an order; do not invent one._





URI: [lambda:author_position](http://w3id.org/lambda/author_position)
Alias: author_position

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyPersonAssociation](StudyPersonAssociation.md) | M:N link between Study and Person with role metadata |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:author_position |
| native | lambda:author_position |




## LinkML Source

<details>
```yaml
name: author_position
description: Position in the author list, where authorship order is meaningful. 1
  is first author. Absent when the source does not state an order; do not invent one.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: author_position
owner: StudyPersonAssociation
domain_of:
- StudyPersonAssociation
range: integer

```
</details>