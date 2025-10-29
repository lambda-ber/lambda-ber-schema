# Enum: SecondaryStructureEnum 




_Secondary structure types_



URI: [lambdaber:SecondaryStructureEnum](https://w3id.org/lambda-ber-schema/SecondaryStructureEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| helix | None | Helix structure |
| sheet | None | Beta sheet |
| turn | None | Turn |
| coil | None | Random coil |
| helix_310 | None | 3-10 helix |
| helix_pi | None | Pi helix |
| bend | None | Bend |
| bridge | None | Beta bridge |




## Slots

| Name | Description |
| ---  | --- |
| [secondary_structure](secondary_structure.md) | Secondary structure assignment |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: SecondaryStructureEnum
description: Secondary structure types
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  helix:
    text: helix
    description: Helix structure
  sheet:
    text: sheet
    description: Beta sheet
  turn:
    text: turn
    description: Turn
  coil:
    text: coil
    description: Random coil
  helix_310:
    text: helix_310
    description: 3-10 helix
  helix_pi:
    text: helix_pi
    description: Pi helix
  bend:
    text: bend
    description: Bend
  bridge:
    text: bridge
    description: Beta bridge

```
</details>