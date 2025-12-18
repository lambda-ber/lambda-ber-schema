

# Slot: pixel_size_physical_um 


_Physical pixel size of the detector in micrometers_





URI: [lambdaber:pixel_size_physical_um](https://w3id.org/lambda-ber-schema/pixel_size_physical_um)
Alias: pixel_size_physical_um

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* Hardware specification, independent of magnification
* Calibrated pixel size (Å/pixel) depends on magnification and is stored in ExperimentRun

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:pixel_size_physical_um |
| native | lambdaber:pixel_size_physical_um |




## LinkML Source

<details>
```yaml
name: pixel_size_physical_um
description: Physical pixel size of the detector in micrometers
comments:
- Hardware specification, independent of magnification
- Calibrated pixel size (Å/pixel) depends on magnification and is stored in ExperimentRun
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: pixel_size_physical_um
owner: CryoEMInstrument
domain_of:
- CryoEMInstrument
range: float

```
</details>