

# Slot: stage_tilt 


_Fixed stage tilt angle for a single-orientation acquisition, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:stage_tilt](http://w3id.org/lambda/stage_tilt)
Alias: stage_tilt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* For a tilt series, use tilt_angle_min, tilt_angle_max, and tilt_angle_increment rather than this slot.

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:stage_tilt |
| native | lambda:stage_tilt |




## LinkML Source

<details>
```yaml
name: stage_tilt
description: Fixed stage tilt angle for a single-orientation acquisition, typically
  specified in degrees. Data providers may specify alternative units by including
  the unit in the QuantityValue.
comments:
- For a tilt series, use tilt_angle_min, tilt_angle_max, and tilt_angle_increment
  rather than this slot.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: stage_tilt
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>