

# Slot: beam_center_x 


_Beam center X coordinate, typically specified in pixels ([px]). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:beam_center_x](http://w3id.org/lambda/beam_center_x)
Alias: beam_center_x

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
| self | lambda:beam_center_x |
| native | lambda:beam_center_x |
| exact | nsls2:Beam_xy_x, imgCIF:_diffrn_detector.beam_centre_x, mmCIF:_diffrn_detector.beam_center_x, ispyb:DataCollection.xBeam |




## LinkML Source

<details>
```yaml
name: beam_center_x
description: Beam center X coordinate, typically specified in pixels ([px]). Data
  providers may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Beam_xy_x
- imgCIF:_diffrn_detector.beam_centre_x
- mmCIF:_diffrn_detector.beam_center_x
- ispyb:DataCollection.xBeam
rank: 1000
alias: beam_center_x
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>