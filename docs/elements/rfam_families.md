

# Slot: rfam_families 


_Rfam families the RNA belongs to, as CURIEs (rfam:RF00005 for tRNA)_





URI: [lambda:rfam_families](http://w3id.org/lambda/rfam_families)
Alias: rfam_families

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | A nucleic acid as a molecular entity: one DNA, RNA or hybrid strand, with its... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Multivalued: True

* Regex pattern: `^rfam:RF[0-9]{5}$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:rfam_families |
| native | lambda:rfam_families |




## LinkML Source

<details>
```yaml
name: rfam_families
description: Rfam families the RNA belongs to, as CURIEs (rfam:RF00005 for tRNA)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: rfam_families
owner: NucleicAcid
domain_of:
- NucleicAcid
range: uriorcurie
multivalued: true
pattern: ^rfam:RF[0-9]{5}$

```
</details>