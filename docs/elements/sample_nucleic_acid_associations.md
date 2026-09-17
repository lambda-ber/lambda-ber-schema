

# Slot: sample_nucleic_acid_associations 


_Links between samples and the nucleic acids they contain (M:N with role, copy number, structural form, source)_





URI: [lambda:sample_nucleic_acid_associations](http://w3id.org/lambda/sample_nucleic_acid_associations)
Alias: sample_nucleic_acid_associations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |






## Properties

* Range: [SampleNucleicAcidAssociation](SampleNucleicAcidAssociation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:sample_nucleic_acid_associations |
| native | lambda:sample_nucleic_acid_associations |




## LinkML Source

<details>
```yaml
name: sample_nucleic_acid_associations
description: Links between samples and the nucleic acids they contain (M:N with role,
  copy number, structural form, source)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: sample_nucleic_acid_associations
owner: Dataset
domain_of:
- Dataset
range: SampleNucleicAcidAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>