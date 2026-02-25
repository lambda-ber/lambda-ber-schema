# Enum: ExperimentSampleRoleEnum 




_Role of a sample in an experiment_



URI: [lambdaber:ExperimentSampleRoleEnum](https://w3id.org/lambda-ber-schema/ExperimentSampleRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| target | None | Primary target of measurement |
| buffer_blank | None | Buffer-only measurement for subtraction |
| standard | None | Calibration or reference standard |
| size_marker | None | Molecular weight marker |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: ExperimentSampleRoleEnum
description: Role of a sample in an experiment
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  target:
    text: target
    description: Primary target of measurement
  buffer_blank:
    text: buffer_blank
    description: Buffer-only measurement for subtraction
  standard:
    text: standard
    description: Calibration or reference standard
  size_marker:
    text: size_marker
    description: Molecular weight marker

```
</details>