

# Slot: instrument_category 


_Category distinguishing beamlines from laboratory equipment_





URI: [lambdaber:instrument_category](https://w3id.org/lambda-ber-schema/instrument_category)
Alias: instrument_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [InstrumentCategoryEnum](InstrumentCategoryEnum.md)




## Comments

* Use SYNCHROTRON_BEAMLINE for synchrotron beamlines
* Use ELECTRON_MICROSCOPE for cryo-EM instruments

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:instrument_category |
| native | lambdaber:instrument_category |




## LinkML Source

<details>
```yaml
name: instrument_category
description: Category distinguishing beamlines from laboratory equipment
comments:
- Use SYNCHROTRON_BEAMLINE for synchrotron beamlines
- Use ELECTRON_MICROSCOPE for cryo-EM instruments
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: instrument_category
owner: Instrument
domain_of:
- Instrument
range: InstrumentCategoryEnum

```
</details>