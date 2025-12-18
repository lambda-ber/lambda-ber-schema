

# Slot: beam_center_y 


_Beam center Y coordinate_





URI: [lambdaber:beam_center_y](https://w3id.org/lambda-ber-schema/beam_center_y)
Alias: beam_center_y

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
| self | lambdaber:beam_center_y |
| native | lambdaber:beam_center_y |
| exact | nsls2:Beam_xy_y, imgCIF:_diffrn_detector.beam_centre_y, mmCIF:_diffrn_detector.beam_center_y, ispyb:DataCollection.yBeam |




## LinkML Source

<details>
```yaml
name: beam_center_y
description: Beam center Y coordinate
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Beam_xy_y
- imgCIF:_diffrn_detector.beam_centre_y
- mmCIF:_diffrn_detector.beam_center_y
- ispyb:DataCollection.yBeam
rank: 1000
alias: beam_center_y
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
unit:
  ucum_code: '[px]'

```
</details>