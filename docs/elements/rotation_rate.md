

# Slot: rotation_rate 


_Continuous rotation rate during data collection (e.g., for MicroED). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:rotation_rate](http://w3id.org/lambda/rotation_rate)
Alias: rotation_rate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* For the extent of a continuous-rotation sweep, use the rotation-method slots shared with the diffraction techniques: start_angle, sweep_start, sweep_end, total_rotation, and oscillation_angle.

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:rotation_rate |
| native | lambda:rotation_rate |




## LinkML Source

<details>
```yaml
name: rotation_rate
description: Continuous rotation rate during data collection (e.g., for MicroED).
  Data providers may specify alternative units by including the unit in the QuantityValue.
comments:
- 'For the extent of a continuous-rotation sweep, use the rotation-method slots shared
  with the diffraction techniques: start_angle, sweep_start, sweep_end, total_rotation,
  and oscillation_angle.'
from_schema: http://w3id.org/lambda/
rank: 1000
alias: rotation_rate
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>