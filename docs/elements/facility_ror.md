

# Slot: facility_ror 


_Research Organization Registry (ROR) identifier for the facility_





URI: [lambda:facility_ror](http://w3id.org/lambda/facility_ror)
Alias: facility_ror

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

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^https://ror\.org/\w+$`




## Comments

* Persistent identifier for the facility organization
* Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:facility_ror |
| native | lambda:facility_ror |




## LinkML Source

<details>
```yaml
name: facility_ror
description: Research Organization Registry (ROR) identifier for the facility
comments:
- Persistent identifier for the facility organization
- 'Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)'
from_schema: http://w3id.org/lambda/
rank: 1000
alias: facility_ror
owner: Instrument
domain_of:
- Instrument
range: uriorcurie
pattern: ^https://ror\.org/\w+$

```
</details>