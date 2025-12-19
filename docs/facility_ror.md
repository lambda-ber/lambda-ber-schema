

# Slot: facility_ror 


_Research Organization Registry (ROR) identifier for the facility_





URI: [lambdaber:facility_ror](https://w3id.org/lambda-ber-schema/facility_ror)
Alias: facility_ror

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^https://ror\.org/\w+$`




## Comments

* Persistent identifier for the facility organization
* Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:facility_ror |
| native | lambdaber:facility_ror |




## LinkML Source

<details>
```yaml
name: facility_ror
description: Research Organization Registry (ROR) identifier for the facility
comments:
- Persistent identifier for the facility organization
- 'Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: facility_ror
owner: Instrument
domain_of:
- Instrument
range: uriorcurie
pattern: ^https://ror\.org/\w+$

```
</details>