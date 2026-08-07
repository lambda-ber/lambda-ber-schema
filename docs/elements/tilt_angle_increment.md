

# Slot: tilt_angle_increment 


_Tilt angle increment between successive tilt steps. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:tilt_angle_increment](http://w3id.org/lambda/tilt_angle_increment)
Alias: tilt_angle_increment

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
| self | lambda:tilt_angle_increment |
| native | lambda:tilt_angle_increment |
| exact | mmCIF:_em_tomography.axis1_angle_increment |




## LinkML Source

<details>
```yaml
name: tilt_angle_increment
description: Tilt angle increment between successive tilt steps. Data providers may
  specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_tomography.axis1_angle_increment
rank: 1000
alias: tilt_angle_increment
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>