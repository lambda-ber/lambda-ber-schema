

# Slot: facility_name 


_Name of the research facility where the instrument is located_





URI: [lambdaber:facility_name](https://w3id.org/lambda-ber-schema/facility_name)
Alias: facility_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |






## Properties

* Range: [FacilityEnum](FacilityEnum.md)




## Comments

* Select from the standardized list of major synchrotron facilities
* Leave empty for laboratory-based instruments

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:facility_name |
| native | lambdaber:facility_name |




## LinkML Source

<details>
```yaml
name: facility_name
description: Name of the research facility where the instrument is located
comments:
- Select from the standardized list of major synchrotron facilities
- Leave empty for laboratory-based instruments
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: facility_name
owner: Instrument
domain_of:
- Instrument
range: FacilityEnum

```
</details>