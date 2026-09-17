

# Slot: nucleic_acid_type 


_Chemical type of the polymer: DNA, RNA, a DNA/RNA hybrid, or an analogue_





URI: [lambda:nucleic_acid_type](http://w3id.org/lambda/nucleic_acid_type)
Alias: nucleic_acid_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | A nucleic acid as a molecular entity: one DNA, RNA or hybrid strand, with its... |  no  |






## Properties

* Range: [NucleicAcidTypeEnum](NucleicAcidTypeEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:nucleic_acid_type |
| native | lambda:nucleic_acid_type |
| exact | mmCIF:_entity_poly.type |




## LinkML Source

<details>
```yaml
name: nucleic_acid_type
description: 'Chemical type of the polymer: DNA, RNA, a DNA/RNA hybrid, or an analogue'
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_entity_poly.type
rank: 1000
alias: nucleic_acid_type
owner: NucleicAcid
domain_of:
- NucleicAcid
range: NucleicAcidTypeEnum
required: true

```
</details>