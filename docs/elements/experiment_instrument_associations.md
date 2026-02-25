

# Slot: experiment_instrument_associations 


_Links between experiments and instruments (M:N)_





URI: [lambdaber:experiment_instrument_associations](https://w3id.org/lambda-ber-schema/experiment_instrument_associations)
Alias: experiment_instrument_associations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |






## Properties

* Range: [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:experiment_instrument_associations |
| native | lambdaber:experiment_instrument_associations |




## LinkML Source

<details>
```yaml
name: experiment_instrument_associations
description: Links between experiments and instruments (M:N)
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: experiment_instrument_associations
owner: Dataset
domain_of:
- Dataset
range: ExperimentInstrumentAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>