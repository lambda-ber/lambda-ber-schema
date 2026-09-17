

# Slot: nucleic_acid_name 


_Name as the depositor or database gives it (e.g., 'tRNA-Phe', 'Dickerson dodecamer', 'sgRNA targeting EMX1'). Recommended, not required, so that a record seeded from an accession alone can be enriched later._





URI: [lambda:nucleic_acid_name](http://w3id.org/lambda/nucleic_acid_name)
Alias: nucleic_acid_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | A nucleic acid as a molecular entity: one DNA, RNA or hybrid strand, with its... |  no  |






## Properties

* Range: [String](String.md)

* Recommended: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:nucleic_acid_name |
| native | lambda:nucleic_acid_name |
| related | mmCIF:_entity.pdbx_description |




## LinkML Source

<details>
```yaml
name: nucleic_acid_name
description: Name as the depositor or database gives it (e.g., 'tRNA-Phe', 'Dickerson
  dodecamer', 'sgRNA targeting EMX1'). Recommended, not required, so that a record
  seeded from an accession alone can be enriched later.
from_schema: http://w3id.org/lambda/
related_mappings:
- mmCIF:_entity.pdbx_description
rank: 1000
alias: nucleic_acid_name
owner: NucleicAcid
domain_of:
- NucleicAcid
range: string
recommended: true

```
</details>