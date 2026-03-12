

# Slot: experiment_sample_associations 


_Links between experiments and samples (M:N with role)_





URI: [lambdaber:experiment_sample_associations](https://w3id.org/lambda-ber-schema/experiment_sample_associations)
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


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:experiment_sample_associations |
| native | lambdaber:experiment_sample_associations |




## LinkML Source

<details>
```yaml
name: experiment_sample_associations
description: Links between experiments and samples (M:N with role)
from_schema: https://w3id.org/lambda-ber-schema/
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