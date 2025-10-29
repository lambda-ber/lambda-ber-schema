# Enum: ExpressionSystemEnum 




_Expression systems for recombinant protein production_



URI: [lambdaber:ExpressionSystemEnum](https://w3id.org/lambda-ber-schema/ExpressionSystemEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| bacteria | None | Bacterial expression (e |
| yeast | None | Yeast expression (e |
| insect | None | Insect cell expression (e |
| mammalian | None | Mammalian cell expression (e |
| cell_free | None | Cell-free expression system |




## Slots

| Name | Description |
| ---  | --- |
| [expression_system](expression_system.md) | Expression system used for recombinant protein production |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: ExpressionSystemEnum
description: Expression systems for recombinant protein production
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  bacteria:
    text: bacteria
    description: Bacterial expression (e.g., E. coli)
  yeast:
    text: yeast
    description: Yeast expression (e.g., S. cerevisiae, P. pastoris)
  insect:
    text: insect
    description: Insect cell expression (e.g., Sf9, High Five)
  mammalian:
    text: mammalian
    description: Mammalian cell expression (e.g., HEK293, CHO)
  cell_free:
    text: cell_free
    description: Cell-free expression system

```
</details>