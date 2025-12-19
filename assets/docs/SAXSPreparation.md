

# Class: SAXSPreparation 


_SAXS/WAXS specific preparation_





URI: [lambdaber:SAXSPreparation](https://w3id.org/lambda-ber-schema/SAXSPreparation)





```mermaid
 classDiagram
    class SAXSPreparation
    click SAXSPreparation href "../SAXSPreparation/"
      TechniqueSpecificPreparation <|-- SAXSPreparation
        click TechniqueSpecificPreparation href "../TechniqueSpecificPreparation/"
      
      SAXSPreparation : buffer_matching_protocol
        
      SAXSPreparation : cell_path_length
        
          
    
        
        
        SAXSPreparation --> "0..1" QuantityValue : cell_path_length
        click QuantityValue href "../QuantityValue/"
    

        
      SAXSPreparation : concentration_series
        
          
    
        
        
        SAXSPreparation --> "0..1" QuantityValue : concentration_series
        click QuantityValue href "../QuantityValue/"
    

        
      SAXSPreparation : description
        
      SAXSPreparation : sample_cell_type
        
      SAXSPreparation : temperature_control
        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md)
        * **SAXSPreparation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [concentration_series](concentration_series.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration values for series measurements | direct |
| [buffer_matching_protocol](buffer_matching_protocol.md) | 0..1 <br/> [String](String.md) | Protocol for buffer matching | direct |
| [sample_cell_type](sample_cell_type.md) | 0..1 <br/> [String](String.md) | Type of sample cell used | direct |
| [cell_path_length](cell_path_length.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Path length, typically specified in millimeters (mm) | direct |
| [temperature_control](temperature_control.md) | 0..1 <br/> [String](String.md) | Temperature control settings | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:SAXSPreparation |
| native | lambdaber:SAXSPreparation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SAXSPreparation
description: SAXS/WAXS specific preparation
from_schema: https://w3id.org/lambda-ber-schema/
is_a: TechniqueSpecificPreparation
attributes:
  concentration_series:
    name: concentration_series
    description: Concentration values for series measurements
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - SAXSPreparation
    range: QuantityValue
    inlined: true
  buffer_matching_protocol:
    name: buffer_matching_protocol
    description: Protocol for buffer matching
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - SAXSPreparation
  sample_cell_type:
    name: sample_cell_type
    description: Type of sample cell used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - SAXSPreparation
  cell_path_length:
    name: cell_path_length
    description: Path length, typically specified in millimeters (mm). Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - SAXSPreparation
    range: QuantityValue
    inlined: true
  temperature_control:
    name: temperature_control
    description: Temperature control settings
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - SAXSPreparation

```
</details>

### Induced

<details>
```yaml
name: SAXSPreparation
description: SAXS/WAXS specific preparation
from_schema: https://w3id.org/lambda-ber-schema/
is_a: TechniqueSpecificPreparation
attributes:
  concentration_series:
    name: concentration_series
    description: Concentration values for series measurements
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: concentration_series
    owner: SAXSPreparation
    domain_of:
    - SAXSPreparation
    range: QuantityValue
    inlined: true
  buffer_matching_protocol:
    name: buffer_matching_protocol
    description: Protocol for buffer matching
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: buffer_matching_protocol
    owner: SAXSPreparation
    domain_of:
    - SAXSPreparation
    range: string
  sample_cell_type:
    name: sample_cell_type
    description: Type of sample cell used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: sample_cell_type
    owner: SAXSPreparation
    domain_of:
    - SAXSPreparation
    range: string
  cell_path_length:
    name: cell_path_length
    description: Path length, typically specified in millimeters (mm). Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: cell_path_length
    owner: SAXSPreparation
    domain_of:
    - SAXSPreparation
    range: QuantityValue
    inlined: true
  temperature_control:
    name: temperature_control
    description: Temperature control settings
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: temperature_control
    owner: SAXSPreparation
    domain_of:
    - SAXSPreparation
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: description
    owner: SAXSPreparation
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>