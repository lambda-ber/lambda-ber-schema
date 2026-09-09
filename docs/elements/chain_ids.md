

# Slot: chain_ids 


_Chain identifiers this protein occupies in the deposited structure, where the sample is a PDB entity_





URI: [lambda:chain_ids](http://w3id.org/lambda/chain_ids)
Alias: chain_ids

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:chain_ids |
| native | lambda:chain_ids |
| exact | mmCIF:_entity_poly.pdbx_strand_id |




## LinkML Source

<details>
```yaml
name: chain_ids
description: Chain identifiers this protein occupies in the deposited structure, where
  the sample is a PDB entity
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_entity_poly.pdbx_strand_id
rank: 1000
alias: chain_ids
owner: SampleProteinAssociation
domain_of:
- SampleProteinAssociation
range: string
multivalued: true

```
</details>