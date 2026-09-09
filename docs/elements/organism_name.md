

# Slot: organism_name 


_Scientific name of the source organism. For display, and for sources that give a name but no taxonomy identifier._





URI: [lambda:organism_name](http://w3id.org/lambda/organism_name)
Alias: organism_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a biological entity: its sequence, source organism, gene, and th... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:organism_name |
| native | lambda:organism_name |
| exact | mmCIF:_entity_src_gen.pdbx_gene_src_scientific_name |




## LinkML Source

<details>
```yaml
name: organism_name
description: Scientific name of the source organism. For display, and for sources
  that give a name but no taxonomy identifier.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_entity_src_gen.pdbx_gene_src_scientific_name
rank: 1000
alias: organism_name
owner: Protein
domain_of:
- Protein
range: string

```
</details>