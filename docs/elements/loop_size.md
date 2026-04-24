

# Slot: loop_size 


_Loop size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:loop_size](http://w3id.org/lambda/loop_size)
Alias: loop_size

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:loop_size |
| native | lambda:loop_size |
| exact | nsls2:Loop_Size |




## LinkML Source

<details>
```yaml
name: loop_size
description: Loop size, typically specified in micrometers. Data providers may specify
  alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Loop_Size
rank: 1000
alias: loop_size
owner: XRayPreparation
domain_of:
- XRayPreparation
range: QuantityValue
inlined: true

```
</details>