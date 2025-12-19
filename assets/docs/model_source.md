

# Slot: model_source 


_Source or software associated with the model (e.g., 'topaz', 'cryolo', 'warp', 'custom', 'pretrained'). Helps track model provenance and should be provided alongside model_name or model_file_path to document which software/framework the model is for._





URI: [lambdaber:model_source](https://w3id.org/lambda-ber-schema/model_source)
Alias: model_source

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
| self | lambdaber:model_source |
| native | lambdaber:model_source |




## LinkML Source

<details>
```yaml
name: model_source
description: Source or software associated with the model (e.g., 'topaz', 'cryolo',
  'warp', 'custom', 'pretrained'). Helps track model provenance and should be provided
  alongside model_name or model_file_path to document which software/framework the
  model is for.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: model_source
owner: ParticlePickingParameters
domain_of:
- ParticlePickingParameters
range: string

```
</details>