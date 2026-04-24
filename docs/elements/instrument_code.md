

# Slot: instrument_code 


_Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking._





URI: [lambda:instrument_code](http://w3id.org/lambda/instrument_code)
Alias: instrument_code

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

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:instrument_code |
| native | lambda:instrument_code |




## LinkML Source

<details>
```yaml
name: instrument_code
description: Human-friendly facility or laboratory identifier for the instrument (e.g.,
  'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and
  equipment tracking.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: instrument_code
owner: Instrument
domain_of:
- Instrument
range: string
required: true

```
</details>