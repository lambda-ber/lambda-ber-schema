# Enum: SampleRoleEnum 




_Role of a sample in a study_



URI: [lambda:SampleRoleEnum](http://w3id.org/lambda/SampleRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| target | None | Primary sample under investigation |
| control | None | Control sample for comparison |
| reference | None | Reference standard or calibrant |
| blank | None | Buffer blank or negative control |




## Slots

| Name | Description |
| ---  | --- |
| [role](role.md) | Role of sample in study (e |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: SampleRoleEnum
description: Role of a sample in a study
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  target:
    text: target
    description: Primary sample under investigation
  control:
    text: control
    description: Control sample for comparison
  reference:
    text: reference
    description: Reference standard or calibrant
  blank:
    text: blank
    description: Buffer blank or negative control

```
</details>