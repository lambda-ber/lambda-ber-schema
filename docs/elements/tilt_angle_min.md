

# Slot: tilt_angle_min 


_Lowest (most negative) tilt angle in the tilt series, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:tilt_angle_min](http://w3id.org/lambda/tilt_angle_min)
Alias: tilt_angle_min

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
| self | lambda:tilt_angle_min |
| native | lambda:tilt_angle_min |
| exact | mmCIF:_em_imaging.tilt_angle_min, mmCIF:_em_tomography.axis1_min_angle |




## LinkML Source

<details>
```yaml
name: tilt_angle_min
description: Lowest (most negative) tilt angle in the tilt series, typically specified
  in degrees. Data providers may specify alternative units by including the unit in
  the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_imaging.tilt_angle_min
- mmCIF:_em_tomography.axis1_min_angle
rank: 1000
alias: tilt_angle_min
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>