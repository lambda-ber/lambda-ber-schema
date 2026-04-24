

# Slot: monochromator_type 


_Type of monochromator_





URI: [lambda:monochromator_type](http://w3id.org/lambda/monochromator_type)
Alias: monochromator_type

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
| self | lambda:monochromator_type |
| native | lambda:monochromator_type |
| exact | mmCIF:_diffrn_source.monochromator |




## LinkML Source

<details>
```yaml
name: monochromator_type
description: Type of monochromator
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_diffrn_source.monochromator
rank: 1000
alias: monochromator_type
owner: XRayInstrument
domain_of:
- XRayInstrument
range: string

```
</details>