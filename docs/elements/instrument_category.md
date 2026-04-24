

# Slot: instrument_category 


_Category distinguishing beamlines from laboratory equipment_





URI: [lambda:instrument_category](http://w3id.org/lambda/instrument_category)
Alias: instrument_category

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

* Range: [InstrumentCategoryEnum](InstrumentCategoryEnum.md)




## Comments

* Use SYNCHROTRON_BEAMLINE for synchrotron beamlines
* Use ELECTRON_MICROSCOPE for cryo-EM instruments

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:instrument_category |
| native | lambda:instrument_category |




## LinkML Source

<details>
```yaml
name: instrument_category
description: Category distinguishing beamlines from laboratory equipment
comments:
- Use SYNCHROTRON_BEAMLINE for synchrotron beamlines
- Use ELECTRON_MICROSCOPE for cryo-EM instruments
from_schema: http://w3id.org/lambda/
rank: 1000
alias: instrument_category
owner: Instrument
domain_of:
- Instrument
range: InstrumentCategoryEnum

```
</details>