

# Class: ComputeResources 


_Computational resources used_





URI: [lambda:ComputeResources](http://w3id.org/lambda/ComputeResources)





```mermaid
 classDiagram
    class ComputeResources
    click ComputeResources href "../ComputeResources/"
      AttributeGroup <|-- ComputeResources
        click AttributeGroup href "../AttributeGroup/"
      
      ComputeResources : cpu_hours
        
          
    
        
        
        ComputeResources --> "0..1" QuantityValue : cpu_hours
        click QuantityValue href "../QuantityValue/"
    

        
      ComputeResources : description
        
      ComputeResources : gpu_hours
        
          
    
        
        
        ComputeResources --> "0..1" QuantityValue : gpu_hours
        click QuantityValue href "../QuantityValue/"
    

        
      ComputeResources : memory_gb
        
          
    
        
        
        ComputeResources --> "0..1" QuantityValue : memory_gb
        click QuantityValue href "../QuantityValue/"
    

        
      ComputeResources : storage_gb
        
          
    
        
        
        ComputeResources --> "0..1" QuantityValue : storage_gb
        click QuantityValue href "../QuantityValue/"
    

        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * **ComputeResources**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cpu_hours](cpu_hours.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | CPU hours used, measured in hours | direct |
| [gpu_hours](gpu_hours.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | GPU hours used, measured in hours | direct |
| [memory_gb](memory_gb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Maximum memory used, typically specified in gigabytes (GB) | direct |
| [storage_gb](storage_gb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Storage used, typically specified in gigabytes (GB) | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | [compute_resources](compute_resources.md) | range | [ComputeResources](ComputeResources.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ComputeResources |
| native | lambda:ComputeResources |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComputeResources
description: Computational resources used
from_schema: http://w3id.org/lambda/
is_a: AttributeGroup
attributes:
  cpu_hours:
    name: cpu_hours
    description: CPU hours used, measured in hours. Data providers may specify alternative
      time units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - ComputeResources
    range: QuantityValue
    inlined: true
  gpu_hours:
    name: gpu_hours
    description: GPU hours used, measured in hours. Data providers may specify alternative
      time units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - ComputeResources
    range: QuantityValue
    inlined: true
  memory_gb:
    name: memory_gb
    description: Maximum memory used, typically specified in gigabytes (GB). Data
      providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - ComputeResources
    range: QuantityValue
    inlined: true
  storage_gb:
    name: storage_gb
    description: Storage used, typically specified in gigabytes (GB). Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - ComputeResources
    range: QuantityValue
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: ComputeResources
description: Computational resources used
from_schema: http://w3id.org/lambda/
is_a: AttributeGroup
attributes:
  cpu_hours:
    name: cpu_hours
    description: CPU hours used, measured in hours. Data providers may specify alternative
      time units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: cpu_hours
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: QuantityValue
    inlined: true
  gpu_hours:
    name: gpu_hours
    description: GPU hours used, measured in hours. Data providers may specify alternative
      time units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: gpu_hours
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: QuantityValue
    inlined: true
  memory_gb:
    name: memory_gb
    description: Maximum memory used, typically specified in gigabytes (GB). Data
      providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: memory_gb
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: QuantityValue
    inlined: true
  storage_gb:
    name: storage_gb
    description: Storage used, typically specified in gigabytes (GB). Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: storage_gb
    owner: ComputeResources
    domain_of:
    - ComputeResources
    range: QuantityValue
    inlined: true
  description:
    name: description
    from_schema: http://w3id.org/lambda/
    alias: description
    owner: ComputeResources
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>