# Enum: DetectorModeEnum 




_Operating modes for detectors during data collection_



URI: [lambda:DetectorModeEnum](http://w3id.org/lambda/DetectorModeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| counting | None | Electron/photon counting mode |
| integrating | None | Integrating mode (analog) |
| super_resolution | None | Super-resolution mode with oversampling |
| linear | None | Linear response mode |
| correlated_double_sampling | None | Correlated double sampling mode |




## Slots

| Name | Description |
| ---  | --- |
| [detector_mode](detector_mode.md) | Supported or default detector operating mode |





## Comments

* Particularly relevant for cryo-EM direct electron detectors

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: DetectorModeEnum
description: Operating modes for detectors during data collection
comments:
- Particularly relevant for cryo-EM direct electron detectors
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  counting:
    text: counting
    description: Electron/photon counting mode
    comments:
    - Individual electron/photon events are counted
  integrating:
    text: integrating
    description: Integrating mode (analog)
    comments:
    - Charge accumulation over exposure time
  super_resolution:
    text: super_resolution
    description: Super-resolution mode with oversampling
    comments:
    - Cryo-EM mode with smaller effective pixel size via oversampling
  linear:
    text: linear
    description: Linear response mode
  correlated_double_sampling:
    text: correlated_double_sampling
    description: Correlated double sampling mode

```
</details>