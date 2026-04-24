

# Slot: instrument_id 


_Reference to the instrument_





URI: [lambda:instrument_id](http://w3id.org/lambda/instrument_id)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:instrument_id |
| native | lambda:instrument_id |




## LinkML Source

<details>
```yaml
name: instrument_id
description: Reference to the instrument
from_schema: http://w3id.org/lambda/
rank: 1000
alias: instrument_id
owner: ExperimentInstrumentAssociation
domain_of:
- ExperimentInstrumentAssociation
range: Instrument
required: true

```
</details>