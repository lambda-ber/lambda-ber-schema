

# Slot: beam_center_x 


_Beam center X coordinate_





URI: [lambdaber:beam_center_x](https://w3id.org/lambda-ber-schema/beam_center_x)
Alias: beam_center_x

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
| self | lambdaber:beam_center_x |
| native | lambdaber:beam_center_x |
| exact | nsls2:Beam_xy_x, imgCIF:_diffrn_detector.beam_centre_x, mmCIF:_diffrn_detector.beam_center_x |




## LinkML Source

<details>
```yaml
name: beam_center_x
description: Beam center X coordinate
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Beam_xy_x
- imgCIF:_diffrn_detector.beam_centre_x
- mmCIF:_diffrn_detector.beam_center_x
rank: 1000
alias: beam_center_x
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
unit:
  ucum_code: '[px]'

```
</details>