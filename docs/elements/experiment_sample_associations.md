

# Slot: experiment_sample_associations 


_Links between experiments and samples (M:N with role)_





URI: [lambda:experiment_sample_associations](http://w3id.org/lambda/experiment_sample_associations)
Alias: experiment_sample_associations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |






## Properties

* Range: [ExperimentSampleAssociation](ExperimentSampleAssociation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:experiment_sample_associations |
| native | lambda:experiment_sample_associations |




## LinkML Source

<details>
```yaml
name: experiment_sample_associations
description: Links between experiments and samples (M:N with role)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: experiment_sample_associations
owner: Dataset
domain_of:
- Dataset
range: ExperimentSampleAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>