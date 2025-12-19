# Enum: IlluminationTypeEnum 




_Types of illumination for optical microscopy_



URI: [lambdaber:IlluminationTypeEnum](https://w3id.org/lambda-ber-schema/IlluminationTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| brightfield | None | Brightfield illumination |
| darkfield | None | Darkfield illumination |
| phase_contrast | None | Phase contrast microscopy |
| dic | None | Differential interference contrast (DIC/Nomarski) |
| fluorescence | None | Fluorescence illumination |
| confocal | None | Confocal laser scanning |
| polarized | None | Polarized light microscopy |
| oblique | None | Oblique illumination |




## Slots

| Name | Description |
| ---  | --- |
| [illumination_type](illumination_type.md) | Type of illumination (brightfield, darkfield, phase contrast, DIC) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: IlluminationTypeEnum
description: Types of illumination for optical microscopy
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  brightfield:
    text: brightfield
    description: Brightfield illumination
  darkfield:
    text: darkfield
    description: Darkfield illumination
  phase_contrast:
    text: phase_contrast
    description: Phase contrast microscopy
  dic:
    text: dic
    description: Differential interference contrast (DIC/Nomarski)
  fluorescence:
    text: fluorescence
    description: Fluorescence illumination
  confocal:
    text: confocal
    description: Confocal laser scanning
  polarized:
    text: polarized
    description: Polarized light microscopy
  oblique:
    text: oblique
    description: Oblique illumination

```
</details>