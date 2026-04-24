

# Slot: total_rotation 


_Total rotation range collected, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:total_rotation](http://w3id.org/lambda/total_rotation)
Alias: total_rotation

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
| self | lambda:total_rotation |
| native | lambda:total_rotation |
| exact | nsls2:Total_rotation_deg, imgCIF:_diffrn_scan_axis.angle_range |




## LinkML Source

<details>
```yaml
name: total_rotation
description: Total rotation range collected, typically specified in degrees. Data
  providers may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Total_rotation_deg
- imgCIF:_diffrn_scan_axis.angle_range
rank: 1000
alias: total_rotation
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>