

# Slot: facility_organization_id 


_The Organization that operates this instrument's facility. An instrument sits at exactly one facility, so this is a direct reference rather than an association table - the same shape as Sample.parent_sample_id._





URI: [lambda:facility_organization_id](http://w3id.org/lambda/facility_organization_id)
Alias: facility_organization_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [SANSInstrument](SANSInstrument.md) | Small-angle neutron scattering (SANS) instrument specifications |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |






## Properties

* Range: [Organization](Organization.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:facility_organization_id |
| native | lambda:facility_organization_id |




## LinkML Source

<details>
```yaml
name: facility_organization_id
description: The Organization that operates this instrument's facility. An instrument
  sits at exactly one facility, so this is a direct reference rather than an association
  table - the same shape as Sample.parent_sample_id.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: facility_organization_id
owner: Instrument
domain_of:
- Instrument
range: Organization

```
</details>