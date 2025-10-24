# Enum: DetectorTypeEnum 




_Types of detectors for cryo-EM_



URI: [lambdaber:DetectorTypeEnum](https://w3id.org/lambda-ber-schema/DetectorTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| direct_electron | None | Direct electron detector |
| ccd | None | CCD camera |
| cmos | None | CMOS detector |
| hybrid_pixel | None | Hybrid pixel detector |




## Slots

| Name | Description |
| ---  | --- |
| [detector_type](detector_type.md) | Type of detector |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: DetectorTypeEnum
description: Types of detectors for cryo-EM
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  direct_electron:
    text: direct_electron
    description: Direct electron detector
  ccd:
    text: ccd
    description: CCD camera
  cmos:
    text: cmos
    description: CMOS detector
  hybrid_pixel:
    text: hybrid_pixel
    description: Hybrid pixel detector

```
</details>