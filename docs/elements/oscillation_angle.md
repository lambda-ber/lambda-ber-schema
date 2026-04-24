

# Slot: oscillation_angle 


_Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:oscillation_angle](http://w3id.org/lambda/oscillation_angle)
Alias: oscillation_angle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* oscillation_width
* oscillation_per_image_deg


## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:oscillation_angle |
| native | lambda:oscillation_angle |
| exact | nsls2:Angle_increment, imgCIF:_diffrn_scan_axis.angle_increment, mmCIF:_diffrn_scan.angle_increment, ispyb:DataCollection.axisRange |




## LinkML Source

<details>
```yaml
name: oscillation_angle
description: Oscillation angle per image, typically specified in degrees. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
aliases:
- oscillation_width
- oscillation_per_image_deg
exact_mappings:
- nsls2:Angle_increment
- imgCIF:_diffrn_scan_axis.angle_increment
- mmCIF:_diffrn_scan.angle_increment
- ispyb:DataCollection.axisRange
rank: 1000
alias: oscillation_angle
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>