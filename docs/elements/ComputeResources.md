

# Class: ComputeResources 


_Computational resources used_





URI: [lambdaber:ComputeResources](https://w3id.org/lambda-ber-schema/ComputeResources)





```mermaid
 classDiagram
    class ComputeResources
    click ComputeResources href "../ComputeResources/"
      AttributeGroup <|-- ComputeResources
        click AttributeGroup href "../AttributeGroup/"
      
      ComputeResources : cpu_hours
        
      ComputeResources : description
        
      ComputeResources : gpu_hours
        
      ComputeResources : memory_gb
        
      ComputeResources : storage_gb
        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * **ComputeResources**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cpu_hours](cpu_hours.md) | 0..1 <br/> [Float](Float.md) | CPU hours used | direct |
| [gpu_hours](gpu_hours.md) | 0..1 <br/> [Float](Float.md) | GPU hours used | direct |
| [memory_gb](memory_gb.md) | 0..1 <br/> [Float](Float.md) | Maximum memory used in GB | direct |
| [storage_gb](storage_gb.md) | 0..1 <br/> [Float](Float.md) | Storage used in GB | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | [compute_resources](compute_resources.md) | range | [ComputeResources](ComputeResources.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:ComputeResources |
| native | lambdaber:ComputeResources |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComputeResources
description: Computational resources used
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeGroup
attributes:
  cpu_hours:
    name: cpu_hours
    description: CPU hours used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ComputeResources
    range: float
  gpu_hours:
    name: gpu_hours
    description: GPU hours used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ComputeResources
    range: float
  memory_gb:
    name: memory_gb
    description: Maximum memory used in GB
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ComputeResources
    range: float
  storage_gb:
    name: storage_gb
    description: Storage used in GB
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ComputeResources
    range: float

```
</details>

### Induced

<details>
```yaml
name: ComputeResources
description: Computational resources used
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeGroup
attributes:
  cpu_hours:
    name: cpu_hours
    description: CPU hours used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: cpu_hours
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: float
  gpu_hours:
    name: gpu_hours
    description: GPU hours used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: gpu_hours
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: float
  memory_gb:
    name: memory_gb
    description: Maximum memory used in GB
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: memory_gb
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: float
  storage_gb:
    name: storage_gb
    description: Storage used in GB
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: storage_gb
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: float
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: description
    owner: ComputeResources
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>