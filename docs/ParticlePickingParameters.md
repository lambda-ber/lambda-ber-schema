

# Class: ParticlePickingParameters 


_Parameters specific to particle picking workflows_





URI: [lambdaber:ParticlePickingParameters](https://w3id.org/lambda-ber-schema/ParticlePickingParameters)





```mermaid
 classDiagram
    class ParticlePickingParameters
    click ParticlePickingParameters href "../ParticlePickingParameters/"
      AttributeGroup <|-- ParticlePickingParameters
        click AttributeGroup href "../AttributeGroup/"
      
      ParticlePickingParameters : box_size
        
      ParticlePickingParameters : description
        
      ParticlePickingParameters : model_file
        
      ParticlePickingParameters : ncc_score
        
      ParticlePickingParameters : picking_method
        
      ParticlePickingParameters : power_score
        
      ParticlePickingParameters : threshold
        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * **ParticlePickingParameters**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [picking_method](picking_method.md) | 0..1 <br/> [String](String.md) | Method used (manual, template_matching, deep_learning, LoG, Topaz, other) | direct |
| [box_size](box_size.md) | 0..1 <br/> [Integer](Integer.md) | Particle box size in pixels | direct |
| [threshold](threshold.md) | 0..1 <br/> [Float](Float.md) | Picking threshold | direct |
| [power_score](power_score.md) | 0..1 <br/> [Float](Float.md) | Power score threshold | direct |
| [ncc_score](ncc_score.md) | 0..1 <br/> [Float](Float.md) | Normalized cross-correlation score threshold | direct |
| [model_file](model_file.md) | 0..1 <br/> [String](String.md) | Path to deep learning model file if used | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | [particle_picking_params](particle_picking_params.md) | range | [ParticlePickingParameters](ParticlePickingParameters.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:ParticlePickingParameters |
| native | lambdaber:ParticlePickingParameters |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ParticlePickingParameters
description: Parameters specific to particle picking workflows
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeGroup
attributes:
  picking_method:
    name: picking_method
    description: Method used (manual, template_matching, deep_learning, LoG, Topaz,
      other)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ParticlePickingParameters
    range: string
  box_size:
    name: box_size
    description: Particle box size in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ParticlePickingParameters
    - RefinementParameters
    range: integer
  threshold:
    name: threshold
    description: Picking threshold
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ParticlePickingParameters
    range: float
  power_score:
    name: power_score
    description: Power score threshold
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ParticlePickingParameters
    range: float
  ncc_score:
    name: ncc_score
    description: Normalized cross-correlation score threshold
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ParticlePickingParameters
    range: float
  model_file:
    name: model_file
    description: Path to deep learning model file if used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ParticlePickingParameters
    range: string

```
</details>

### Induced

<details>
```yaml
name: ParticlePickingParameters
description: Parameters specific to particle picking workflows
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeGroup
attributes:
  picking_method:
    name: picking_method
    description: Method used (manual, template_matching, deep_learning, LoG, Topaz,
      other)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: picking_method
    owner: ParticlePickingParameters
    domain_of:
    - ParticlePickingParameters
    range: string
  box_size:
    name: box_size
    description: Particle box size in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: box_size
    owner: ParticlePickingParameters
    domain_of:
    - ParticlePickingParameters
    - RefinementParameters
    range: integer
  threshold:
    name: threshold
    description: Picking threshold
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: threshold
    owner: ParticlePickingParameters
    domain_of:
    - ParticlePickingParameters
    range: float
  power_score:
    name: power_score
    description: Power score threshold
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: power_score
    owner: ParticlePickingParameters
    domain_of:
    - ParticlePickingParameters
    range: float
  ncc_score:
    name: ncc_score
    description: Normalized cross-correlation score threshold
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: ncc_score
    owner: ParticlePickingParameters
    domain_of:
    - ParticlePickingParameters
    range: float
  model_file:
    name: model_file
    description: Path to deep learning model file if used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: model_file
    owner: ParticlePickingParameters
    domain_of:
    - ParticlePickingParameters
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: description
    owner: ParticlePickingParameters
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>