

# Slot: rnacentral_id 


_RNAcentral identifier as a Bioregistry CURIE (rnacentral:URS0000759CF4), optionally with the taxon suffix (rnacentral:URS0000759CF4_9606). For non-coding RNAs. Normally identical to id when set._





URI: [lambda:rnacentral_id](http://w3id.org/lambda/rnacentral_id)
Alias: rnacentral_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | A nucleic acid as a molecular entity: one DNA, RNA or hybrid strand, with its... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^rnacentral:URS[0-9A-F]{10}(_[0-9]+)?$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:rnacentral_id |
| native | lambda:rnacentral_id |




## LinkML Source

<details>
```yaml
name: rnacentral_id
description: RNAcentral identifier as a Bioregistry CURIE (rnacentral:URS0000759CF4),
  optionally with the taxon suffix (rnacentral:URS0000759CF4_9606). For non-coding
  RNAs. Normally identical to id when set.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: rnacentral_id
owner: NucleicAcid
domain_of:
- NucleicAcid
range: uriorcurie
pattern: ^rnacentral:URS[0-9A-F]{10}(_[0-9]+)?$

```
</details>