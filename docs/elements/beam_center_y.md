

# Slot: beam_center_y 


_Beam center Y coordinate, typically specified in pixels ([px]). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:beam_center_y](http://w3id.org/lambda/beam_center_y)
Alias: beam_center_y

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
| self | lambda:beam_center_y |
| native | lambda:beam_center_y |
| exact | nsls2:Beam_xy_y, imgCIF:_diffrn_detector.beam_centre_y, mmCIF:_diffrn_detector.beam_center_y, ispyb:DataCollection.yBeam |




## LinkML Source

<details>
```yaml
name: beam_center_y
description: Beam center Y coordinate, typically specified in pixels ([px]). Data
  providers may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
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
range: QuantityValue
inlined: true

```
</details>