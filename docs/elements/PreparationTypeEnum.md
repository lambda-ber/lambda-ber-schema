# Enum: PreparationTypeEnum 




_Types of sample preparation_



URI: [lambdaber:PreparationTypeEnum](https://w3id.org/lambda-ber-schema/PreparationTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| cryo_em | None | Cryo-EM preparation |
| xray_crystallography | None | X-ray crystallography preparation |
| saxs | None | SAXS/WAXS preparation |
| sans | None | SANS preparation |
| protein_expression | None | Protein expression in host cells |
| protein_purification | None | Protein purification |
| negative_stain | None | Negative stain EM preparation |




## Slots

| Name | Description |
| ---  | --- |
| [preparation_type](preparation_type.md) | Type of sample preparation |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: PreparationTypeEnum
description: Types of sample preparation
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  cryo_em:
    text: cryo_em
    description: Cryo-EM preparation
  xray_crystallography:
    text: xray_crystallography
    description: X-ray crystallography preparation
  saxs:
    text: saxs
    description: SAXS/WAXS preparation
  sans:
    text: sans
    description: SANS preparation
  protein_expression:
    text: protein_expression
    description: Protein expression in host cells
  protein_purification:
    text: protein_purification
    description: Protein purification
  negative_stain:
    text: negative_stain
    description: Negative stain EM preparation

```
</details>