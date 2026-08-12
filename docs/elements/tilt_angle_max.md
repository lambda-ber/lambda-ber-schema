

# Slot: tilt_angle_max 


_Highest (most positive) tilt angle in the tilt series, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:tilt_angle_max](http://w3id.org/lambda/tilt_angle_max)
Alias: tilt_angle_max

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:tilt_angle_max |
| native | lambda:tilt_angle_max |
| exact | mmCIF:_em_imaging.tilt_angle_max, mmCIF:_em_tomography.axis1_max_angle |




## LinkML Source

<details>
```yaml
name: tilt_angle_max
description: Highest (most positive) tilt angle in the tilt series, typically specified
  in degrees. Data providers may specify alternative units by including the unit in
  the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_imaging.tilt_angle_max
- mmCIF:_em_tomography.axis1_max_angle
rank: 1000
alias: tilt_angle_max
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>