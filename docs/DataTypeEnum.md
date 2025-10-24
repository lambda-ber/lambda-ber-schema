# Enum: DataTypeEnum 




_Types of data_



URI: [lambdaber:DataTypeEnum](https://w3id.org/lambda-ber-schema/DataTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| micrograph | None | Electron micrograph |
| diffraction | None | Diffraction pattern |
| scattering | None | Scattering data |
| particles | None | Particle stack |
| volume | None | 3D volume |
| model | None | Atomic model |
| metadata | None | Metadata file |
| raw_data | None | Raw experimental data |
| processed_data | None | Processed data |




## Slots

| Name | Description |
| ---  | --- |
| [data_type](data_type.md) | Type of data in the file |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: DataTypeEnum
description: Types of data
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  micrograph:
    text: micrograph
    description: Electron micrograph
  diffraction:
    text: diffraction
    description: Diffraction pattern
  scattering:
    text: scattering
    description: Scattering data
  particles:
    text: particles
    description: Particle stack
  volume:
    text: volume
    description: 3D volume
  model:
    text: model
    description: Atomic model
  metadata:
    text: metadata
    description: Metadata file
  raw_data:
    text: raw_data
    description: Raw experimental data
  processed_data:
    text: processed_data
    description: Processed data

```
</details>