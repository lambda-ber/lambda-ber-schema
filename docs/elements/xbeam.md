

# Slot: xbeam 


_Beam center X coordinate in pixels_





URI: [lambda:xbeam](http://w3id.org/lambda/xbeam)
Alias: xbeam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamCenterPixels](BeamCenterPixels.md) | Combined beam center coordinates in detector pixel units |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* x
* beam_center_x_px


## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:xbeam |
| native | lambda:xbeam |
| exact | nsls2:Beam_xy_x, imgCIF:_diffrn_detector.beam_center_x, mmCIF:_diffrn_detector.beam_center_x, ispyb:DataCollection.xBeam |




## LinkML Source

<details>
```yaml
name: xbeam
description: Beam center X coordinate in pixels
from_schema: http://w3id.org/lambda/
aliases:
- x
- beam_center_x_px
exact_mappings:
- nsls2:Beam_xy_x
- imgCIF:_diffrn_detector.beam_center_x
- mmCIF:_diffrn_detector.beam_center_x
- ispyb:DataCollection.xBeam
rank: 1000
alias: xbeam
owner: BeamCenterPixels
domain_of:
- BeamCenterPixels
range: QuantityValue
inlined: true

```
</details>