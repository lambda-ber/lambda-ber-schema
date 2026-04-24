

# Slot: model_source 


_Source or software associated with the model (e.g., 'topaz', 'cryolo', 'warp', 'custom', 'pretrained'). Helps track model provenance and should be provided alongside model_name or model_file_path to document which software/framework the model is for._





URI: [lambda:model_source](http://w3id.org/lambda/model_source)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:model_source |
| native | lambda:model_source |




## LinkML Source

<details>
```yaml
name: model_source
description: Source or software associated with the model (e.g., 'topaz', 'cryolo',
  'warp', 'custom', 'pretrained'). Helps track model provenance and should be provided
  alongside model_name or model_file_path to document which software/framework the
  model is for.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: model_source
owner: ParticlePickingParameters
domain_of:
- ParticlePickingParameters
range: string

```
</details>