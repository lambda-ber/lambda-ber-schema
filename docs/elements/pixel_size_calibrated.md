

# Slot: pixel_size_calibrated 


_Calibrated pixel size for this experiment, typically specified in Angstroms (Å) per pixel. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:pixel_size_calibrated](http://w3id.org/lambda/pixel_size_calibrated)
Alias: pixel_size_calibrated

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* For cryo-EM: depends on magnification (Å/pixel)
* For X-ray: typically mm/pixel or µm/pixel
* Physical pixel size is hardware spec stored in Instrument

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:pixel_size_calibrated |
| native | lambda:pixel_size_calibrated |
| exact | mmCIF:_em_image_recording.calibrated_pixel_size |




## LinkML Source

<details>
```yaml
name: pixel_size_calibrated
description: Calibrated pixel size for this experiment, typically specified in Angstroms
  (Å) per pixel. Data providers may specify alternative units by including the unit
  in the QuantityValue.
comments:
- 'For cryo-EM: depends on magnification (Å/pixel)'
- 'For X-ray: typically mm/pixel or µm/pixel'
- Physical pixel size is hardware spec stored in Instrument
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_image_recording.calibrated_pixel_size
rank: 1000
alias: pixel_size_calibrated
owner: DataCollectionStrategy
domain_of:
- DataCollectionStrategy
range: QuantityValue
inlined: true

```
</details>