

# Slot: current_status 


_Current operational status_





URI: [lambdaber:current_status](https://w3id.org/lambda-ber-schema/current_status)
Alias: current_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [InstrumentStatusEnum](InstrumentStatusEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:current_status |
| native | lambdaber:current_status |




## LinkML Source

<details>
```yaml
name: current_status
description: Current operational status
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: current_status
owner: Instrument
domain_of:
- Instrument
range: InstrumentStatusEnum

```
</details>