

# Slot: model_file_path 


_Path to deep learning model file if using a local or custom trained model file. Use this instead of model_name when pointing to a specific file on disk. Either model_name or model_file_path should be provided when using deep learning methods._





URI: [lambdaber:model_file_path](https://w3id.org/lambda-ber-schema/model_file_path)
Alias: model_file_path

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ParticlePickingParameters](ParticlePickingParameters.md) | Parameters specific to particle picking workflows |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:model_file_path |
| native | lambdaber:model_file_path |




## LinkML Source

<details>
```yaml
name: model_file_path
description: Path to deep learning model file if using a local or custom trained model
  file. Use this instead of model_name when pointing to a specific file on disk. Either
  model_name or model_file_path should be provided when using deep learning methods.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: model_file_path
owner: ParticlePickingParameters
domain_of:
- ParticlePickingParameters
range: string

```
</details>