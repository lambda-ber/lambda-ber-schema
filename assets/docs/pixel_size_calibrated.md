

# Slot: pixel_size_calibrated 


_Calibrated pixel size for this experiment, typically specified in Angstroms (Å) per pixel. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:pixel_size_calibrated](https://w3id.org/lambda-ber-schema/pixel_size_calibrated)
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


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:pixel_size_calibrated |
| native | lambdaber:pixel_size_calibrated |




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
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: pixel_size_calibrated
owner: DataCollectionStrategy
domain_of:
- DataCollectionStrategy
range: QuantityValue
inlined: true

```
</details>