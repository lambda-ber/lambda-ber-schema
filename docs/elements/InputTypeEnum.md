# Enum: InputTypeEnum 




_Type of input for a workflow_



URI: [lambda:InputTypeEnum](http://w3id.org/lambda/InputTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| raw_data | None | Raw experimental data |
| reference | None | Reference data (e |
| parameters | None | Processing parameters file |
| mask | None | Mask or selection file |




## Slots

| Name | Description |
| ---  | --- |
| [input_type](input_type.md) | Type of input for the workflow |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: InputTypeEnum
description: Type of input for a workflow
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  raw_data:
    text: raw_data
    description: Raw experimental data
  reference:
    text: reference
    description: Reference data (e.g., PDB model, database)
  parameters:
    text: parameters
    description: Processing parameters file
  mask:
    text: mask
    description: Mask or selection file

```
</details>