

# Slot: output_binning 


_Output binning factor. This must be a positive float value (e.g., 1, 1.5, 2, 3)._





URI: [lambdaber:output_binning](https://w3id.org/lambda-ber-schema/output_binning)
Alias: output_binning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MotionCorrectionParameters](MotionCorrectionParameters.md) | Parameters specific to motion correction workflows |  no  |






## Properties

* Range: [Float](Float.md)

* Minimum Value: 0




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:output_binning |
| native | lambdaber:output_binning |




## LinkML Source

<details>
```yaml
name: output_binning
description: Output binning factor. This must be a positive float value (e.g., 1,
  1.5, 2, 3).
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: output_binning
owner: MotionCorrectionParameters
domain_of:
- MotionCorrectionParameters
range: float
minimum_value: 0.01

```
</details>