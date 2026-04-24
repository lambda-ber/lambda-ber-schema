

# Slot: goniometer_type 


_Type of goniometer_





URI: [lambda:goniometer_type](http://w3id.org/lambda/goniometer_type)
Alias: goniometer_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:goniometer_type |
| native | lambda:goniometer_type |
| exact | mmCIF:_diffrn_measurement.device |




## LinkML Source

<details>
```yaml
name: goniometer_type
description: Type of goniometer
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_diffrn_measurement.device
rank: 1000
alias: goniometer_type
owner: XRayInstrument
domain_of:
- XRayInstrument
range: string

```
</details>