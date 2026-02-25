

# Slot: oscillation_angle 


_Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:oscillation_angle](https://w3id.org/lambda-ber-schema/oscillation_angle)
Alias: oscillation_angle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:oscillation_angle |
| native | lambdaber:oscillation_angle |
| exact | nsls2:Angle_increment, imgCIF:_diffrn_scan_axis.angle_increment, mmCIF:_diffrn_scan.angle_increment, ispyb:DataCollection.axisRange |




## LinkML Source

<details>
```yaml
name: oscillation_angle
description: Oscillation angle per image, typically specified in degrees. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
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