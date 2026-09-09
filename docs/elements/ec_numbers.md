

# Slot: ec_numbers 


_Enzyme Commission numbers, where the protein is an enzyme (e.g., 1.1.1.1)_





URI: [lambda:ec_numbers](http://w3id.org/lambda/ec_numbers)
Alias: ec_numbers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a biological entity: its sequence, source organism, gene, and th... |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^([0-9]+|-)\.([0-9]+|-)\.([0-9]+|-)\.([0-9]+|n[0-9]*|-)$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ec_numbers |
| native | lambda:ec_numbers |
| exact | mmCIF:_entity.pdbx_ec |




## LinkML Source

<details>
```yaml
name: ec_numbers
description: Enzyme Commission numbers, where the protein is an enzyme (e.g., 1.1.1.1)
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_entity.pdbx_ec
rank: 1000
alias: ec_numbers
owner: Protein
domain_of:
- Protein
range: string
multivalued: true
pattern: ^([0-9]+|-)\.([0-9]+|-)\.([0-9]+|-)\.([0-9]+|n[0-9]*|-)$

```
</details>