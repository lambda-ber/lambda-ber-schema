

# Slot: camera_binning 


_Camera binning factor. This must be a positive float value (e.g., 1, 1.5, 2, 3)._





URI: [lambdaber:camera_binning](https://w3id.org/lambda-ber-schema/camera_binning)
Alias: camera_binning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Float](Float.md)

* Minimum Value: 0




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:camera_binning |
| native | lambdaber:camera_binning |




## LinkML Source

<details>
```yaml
name: camera_binning
description: Camera binning factor. This must be a positive float value (e.g., 1,
  1.5, 2, 3).
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: camera_binning
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
minimum_value: 0.01

```
</details>