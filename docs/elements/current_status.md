

# Slot: current_status 


_Current operational status_





URI: [lambda:current_status](http://w3id.org/lambda/current_status)
Alias: current_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [SANSInstrument](SANSInstrument.md) | Small-angle neutron scattering (SANS) instrument specifications |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |






## Properties

* Range: [InstrumentStatusEnum](InstrumentStatusEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:current_status |
| native | lambda:current_status |




## LinkML Source

<details>
```yaml
name: current_status
description: Current operational status
from_schema: http://w3id.org/lambda/
rank: 1000
alias: current_status
owner: Instrument
domain_of:
- Instrument
range: InstrumentStatusEnum

```
</details>