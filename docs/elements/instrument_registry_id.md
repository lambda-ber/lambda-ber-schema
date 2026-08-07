

# Slot: instrument_registry_id 


_Controlled-vocabulary identifier linking this instrument to its canonical entry in a registry enum appropriate to the instrument type. For beamlines, use a value from BeamlineEnum; additional instrument-type registries may be referenced here as they are introduced._





URI: [lambda:instrument_registry_id](http://w3id.org/lambda/instrument_registry_id)
Alias: instrument_registry_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [SANSInstrument](SANSInstrument.md) | Small-angle neutron scattering (SANS) instrument specifications |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |






## Properties

* Range: [String](String.md)&nbsp;or&nbsp;<br />[BeamlineEnum](BeamlineEnum.md)




## Comments

* Use this to link an instrument record to a known, validated registry entry, enabling schema-level validation against typos
* instrument_code is a free-text local label; instrument_registry_id is the schema-level controlled identity
* beamline_id captures the facility-local string ID (e.g., '19-ID'); instrument_registry_id captures the enum identity (e.g., APS_SBCCAT_19ID)
* Distinct from the instrument_id foreign-key slot used in association tables, which references an Instrument object

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:instrument_registry_id |
| native | lambda:instrument_registry_id |




## LinkML Source

<details>
```yaml
name: instrument_registry_id
description: Controlled-vocabulary identifier linking this instrument to its canonical
  entry in a registry enum appropriate to the instrument type. For beamlines, use
  a value from BeamlineEnum; additional instrument-type registries may be referenced
  here as they are introduced.
comments:
- Use this to link an instrument record to a known, validated registry entry, enabling
  schema-level validation against typos
- instrument_code is a free-text local label; instrument_registry_id is the schema-level
  controlled identity
- beamline_id captures the facility-local string ID (e.g., '19-ID'); instrument_registry_id
  captures the enum identity (e.g., APS_SBCCAT_19ID)
- Distinct from the instrument_id foreign-key slot used in association tables, which
  references an Instrument object
from_schema: http://w3id.org/lambda/
rank: 1000
alias: instrument_registry_id
owner: Instrument
domain_of:
- Instrument
range: string
any_of:
- range: BeamlineEnum

```
</details>