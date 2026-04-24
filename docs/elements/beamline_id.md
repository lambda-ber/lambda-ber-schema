

# Slot: beamline_id 


_Beamline identifier at synchrotron/neutron facility_





URI: [lambda:beamline_id](http://w3id.org/lambda/beamline_id)
Alias: beamline_id

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




## Comments

* Use facility-specific naming convention
* Examples: '12.3.1' (ALS), '17-ID-1' (NSLS-II), 'I04' (Diamond)

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:beamline_id |
| native | lambda:beamline_id |
| exact | mmCIF:_diffrn_source.pdbx_synchrotron_beamline |




## LinkML Source

<details>
```yaml
name: beamline_id
description: Beamline identifier at synchrotron/neutron facility
comments:
- Use facility-specific naming convention
- 'Examples: ''12.3.1'' (ALS), ''17-ID-1'' (NSLS-II), ''I04'' (Diamond)'
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_diffrn_source.pdbx_synchrotron_beamline
rank: 1000
alias: beamline_id
owner: Instrument
domain_of:
- Instrument
range: string

```
</details>