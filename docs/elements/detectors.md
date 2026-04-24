

# Slot: detectors 


_List of detectors associated with the instrument_





URI: [lambda:detectors](http://w3id.org/lambda/detectors)
Alias: detectors

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SANSInstrument](SANSInstrument.md) | Small-angle neutron scattering (SANS) instrument specifications |  no  |






## Properties

* Range: [SANSDetector](SANSDetector.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:detectors |
| native | lambda:detectors |




## LinkML Source

<details>
```yaml
name: detectors
description: List of detectors associated with the instrument
from_schema: http://w3id.org/lambda/
rank: 1000
alias: detectors
owner: SANSInstrument
domain_of:
- SANSInstrument
range: SANSDetector
multivalued: true
inlined: true
inlined_as_list: true

```
</details>