

# Slot: instrument_id 


_Reference to the instrument_





URI: [lambdaber:instrument_id](https://w3id.org/lambda-ber-schema/instrument_id)
Alias: instrument_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | M:N link between ExperimentRun and Instrument |  no  |






## Properties

* Range: [Instrument](Instrument.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:instrument_id |
| native | lambdaber:instrument_id |




## LinkML Source

<details>
```yaml
name: instrument_id
description: Reference to the instrument
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: instrument_id
owner: ExperimentInstrumentAssociation
domain_of:
- ExperimentInstrumentAssociation
range: Instrument
required: true

```
</details>