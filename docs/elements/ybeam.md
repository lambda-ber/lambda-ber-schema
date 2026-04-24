

# Slot: ybeam 


_Beam center Y coordinate in pixels_





URI: [lambda:ybeam](http://w3id.org/lambda/ybeam)
Alias: ybeam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamCenterPixels](BeamCenterPixels.md) | Combined beam center coordinates in detector pixel units |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* y
* beam_center_y_px


## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ybeam |
| native | lambda:ybeam |
| exact | nsls2:Beam_xy_y, imgCIF:_diffrn_detector.beam_center_y, mmCIF:_diffrn_detector.beam_center_y, ispyb:DataCollection.yBeam |




## LinkML Source

<details>
```yaml
name: ybeam
description: Beam center Y coordinate in pixels
from_schema: http://w3id.org/lambda/
aliases:
- y
- beam_center_y_px
exact_mappings:
- nsls2:Beam_xy_y
- imgCIF:_diffrn_detector.beam_center_y
- mmCIF:_diffrn_detector.beam_center_y
- ispyb:DataCollection.yBeam
rank: 1000
alias: ybeam
owner: BeamCenterPixels
domain_of:
- BeamCenterPixels
range: QuantityValue
inlined: true

```
</details>