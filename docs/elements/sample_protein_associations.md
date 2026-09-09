

# Slot: sample_protein_associations 


_Links between samples and the proteins they contain (M:N with role, copy number, construct)_





URI: [lambda:sample_protein_associations](http://w3id.org/lambda/sample_protein_associations)
Alias: sample_protein_associations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |






## Properties

* Range: [SampleProteinAssociation](SampleProteinAssociation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:sample_protein_associations |
| native | lambda:sample_protein_associations |




## LinkML Source

<details>
```yaml
name: sample_protein_associations
description: Links between samples and the proteins they contain (M:N with role, copy
  number, construct)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: sample_protein_associations
owner: Dataset
domain_of:
- Dataset
range: SampleProteinAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>