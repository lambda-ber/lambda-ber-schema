# Enum: CollectionModeEnum 




_Data collection modes_



URI: [lambdaber:CollectionModeEnum](https://w3id.org/lambda-ber-schema/CollectionModeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| counting | None | Counting mode |
| super_resolution | None | Super-resolution mode |
| continuous | None | Continuous collection |
| oscillation | None | Oscillation method |
| still | None | Still images |
| batch | None | Batch mode collection |
| sec_saxs | None | SEC-SAXS collection mode |
| single_particle | None | Single particle analysis mode |




## Slots

| Name | Description |
| ---  | --- |
| [collection_mode](collection_mode.md) | Mode of data collection |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: CollectionModeEnum
description: Data collection modes
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  counting:
    text: counting
    description: Counting mode
  super_resolution:
    text: super_resolution
    description: Super-resolution mode
  continuous:
    text: continuous
    description: Continuous collection
  oscillation:
    text: oscillation
    description: Oscillation method
  still:
    text: still
    description: Still images
  batch:
    text: batch
    description: Batch mode collection
  sec_saxs:
    text: sec_saxs
    description: SEC-SAXS collection mode
  single_particle:
    text: single_particle
    description: Single particle analysis mode

```
</details>