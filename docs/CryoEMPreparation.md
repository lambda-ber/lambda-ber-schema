

# Class: CryoEMPreparation 


_Cryo-EM specific sample preparation_





URI: [lambdaber:CryoEMPreparation](https://w3id.org/lambda-ber-schema/CryoEMPreparation)





```mermaid
 classDiagram
    class CryoEMPreparation
    click CryoEMPreparation href "../CryoEMPreparation/"
      TechniqueSpecificPreparation <|-- CryoEMPreparation
        click TechniqueSpecificPreparation href "../TechniqueSpecificPreparation/"
      
      CryoEMPreparation : blot_force
        
      CryoEMPreparation : blot_time
        
      CryoEMPreparation : chamber_temperature
        
      CryoEMPreparation : description
        
      CryoEMPreparation : grid_type
        
          
    
        
        
        CryoEMPreparation --> "0..1" GridTypeEnum : grid_type
        click GridTypeEnum href "../GridTypeEnum/"
    

        
      CryoEMPreparation : hole_size
        
      CryoEMPreparation : humidity_percentage
        
      CryoEMPreparation : plasma_treatment
        
      CryoEMPreparation : support_film
        
      CryoEMPreparation : vitrification_method
        
          
    
        
        
        CryoEMPreparation --> "0..1" VitrificationMethodEnum : vitrification_method
        click VitrificationMethodEnum href "../VitrificationMethodEnum/"
    

        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md)
        * **CryoEMPreparation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [grid_type](grid_type.md) | 0..1 <br/> [GridTypeEnum](GridTypeEnum.md) | Type of EM grid used | direct |
| [support_film](support_film.md) | 0..1 <br/> [String](String.md) | Support film type | direct |
| [hole_size](hole_size.md) | 0..1 <br/> [Float](Float.md) | Hole size in micrometers | direct |
| [vitrification_method](vitrification_method.md) | 0..1 <br/> [VitrificationMethodEnum](VitrificationMethodEnum.md) | Method used for vitrification | direct |
| [blot_time](blot_time.md) | 0..1 <br/> [Float](Float.md) | Blotting time in seconds | direct |
| [blot_force](blot_force.md) | 0..1 <br/> [Integer](Integer.md) | Blotting force setting | direct |
| [humidity_percentage](humidity_percentage.md) | 0..1 <br/> [Float](Float.md) | Chamber humidity during vitrification | direct |
| [chamber_temperature](chamber_temperature.md) | 0..1 <br/> [Float](Float.md) | Chamber temperature in Celsius | direct |
| [plasma_treatment](plasma_treatment.md) | 0..1 <br/> [String](String.md) | Plasma treatment details | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:CryoEMPreparation |
| native | lambdaber:CryoEMPreparation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CryoEMPreparation
description: Cryo-EM specific sample preparation
from_schema: https://w3id.org/lambda-ber-schema/
is_a: TechniqueSpecificPreparation
attributes:
  grid_type:
    name: grid_type
    description: Type of EM grid used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation
    range: GridTypeEnum
  support_film:
    name: support_film
    description: Support film type
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation
    range: string
  hole_size:
    name: hole_size
    description: Hole size in micrometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation
    range: float
    minimum_value: 0.5
    maximum_value: 5.0
  vitrification_method:
    name: vitrification_method
    description: Method used for vitrification
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation
    range: VitrificationMethodEnum
  blot_time:
    name: blot_time
    description: Blotting time in seconds
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation
    range: float
    minimum_value: 0.5
    maximum_value: 10.0
  blot_force:
    name: blot_force
    description: Blotting force setting
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation
    range: integer
  humidity_percentage:
    name: humidity_percentage
    description: Chamber humidity during vitrification
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation
    range: float
    minimum_value: 0
    maximum_value: 100
  chamber_temperature:
    name: chamber_temperature
    description: Chamber temperature in Celsius
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation
    range: float
  plasma_treatment:
    name: plasma_treatment
    description: Plasma treatment details
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - CryoEMPreparation

```
</details>

### Induced

<details>
```yaml
name: CryoEMPreparation
description: Cryo-EM specific sample preparation
from_schema: https://w3id.org/lambda-ber-schema/
is_a: TechniqueSpecificPreparation
attributes:
  grid_type:
    name: grid_type
    description: Type of EM grid used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: grid_type
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: GridTypeEnum
  support_film:
    name: support_film
    description: Support film type
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: support_film
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: string
  hole_size:
    name: hole_size
    description: Hole size in micrometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: hole_size
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: float
    minimum_value: 0.5
    maximum_value: 5.0
  vitrification_method:
    name: vitrification_method
    description: Method used for vitrification
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: vitrification_method
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: VitrificationMethodEnum
  blot_time:
    name: blot_time
    description: Blotting time in seconds
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: blot_time
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: float
    minimum_value: 0.5
    maximum_value: 10.0
  blot_force:
    name: blot_force
    description: Blotting force setting
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: blot_force
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: integer
  humidity_percentage:
    name: humidity_percentage
    description: Chamber humidity during vitrification
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: humidity_percentage
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: float
    minimum_value: 0
    maximum_value: 100
  chamber_temperature:
    name: chamber_temperature
    description: Chamber temperature in Celsius
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: chamber_temperature
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: float
  plasma_treatment:
    name: plasma_treatment
    description: Plasma treatment details
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: plasma_treatment
    owner: CryoEMPreparation
    domain_of:
    - CryoEMPreparation
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: description
    owner: CryoEMPreparation
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>