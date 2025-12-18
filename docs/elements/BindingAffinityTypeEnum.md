# Enum: BindingAffinityTypeEnum 




_Types of binding affinity measurements_



URI: [lambdaber:BindingAffinityTypeEnum](https://w3id.org/lambda-ber-schema/BindingAffinityTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| kd | None | Dissociation constant |
| ki | None | Inhibition constant |
| ic50 | None | Half maximal inhibitory concentration |
| ec50 | None | Half maximal effective concentration |
| ka | None | Association constant |
| km | None | Michaelis constant |




## Slots

| Name | Description |
| ---  | --- |
| [binding_affinity_type](binding_affinity_type.md) | Type of binding measurement (Kd, Ki, IC50) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: BindingAffinityTypeEnum
description: Types of binding affinity measurements
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  kd:
    text: kd
    description: Dissociation constant
  ki:
    text: ki
    description: Inhibition constant
  ic50:
    text: ic50
    description: Half maximal inhibitory concentration
  ec50:
    text: ec50
    description: Half maximal effective concentration
  ka:
    text: ka
    description: Association constant
  km:
    text: km
    description: Michaelis constant

```
</details>