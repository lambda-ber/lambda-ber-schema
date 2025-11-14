

# Slot: total_rotation 


_Total rotation range collected_





URI: [lambdaber:total_rotation](https://w3id.org/lambda-ber-schema/total_rotation)
Alias: total_rotation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:total_rotation |
| native | lambdaber:total_rotation |
| exact | nsls2:Total_rotation_deg, imgCIF:_diffrn_scan_axis.angle_range |




## LinkML Source

<details>
```yaml
name: total_rotation
description: Total rotation range collected
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Total_rotation_deg
- imgCIF:_diffrn_scan_axis.angle_range
rank: 1000
alias: total_rotation
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
unit:
  ucum_code: deg

```
</details>