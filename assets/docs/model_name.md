

# Slot: model_name 


_Name or identifier of the deep learning model (e.g., 'resnet16', 'resnet8', 'cryolo_general'). Use this for standard pretrained models. Either model_name or model_file_path should be provided when using deep learning methods._





URI: [lambdaber:model_name](https://w3id.org/lambda-ber-schema/model_name)
Alias: model_name

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
| self | lambdaber:model_name |
| native | lambdaber:model_name |




## LinkML Source

<details>
```yaml
name: model_name
description: Name or identifier of the deep learning model (e.g., 'resnet16', 'resnet8',
  'cryolo_general'). Use this for standard pretrained models. Either model_name or
  model_file_path should be provided when using deep learning methods.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: model_name
owner: ParticlePickingParameters
domain_of:
- ParticlePickingParameters
range: string

```
</details>