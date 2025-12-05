

# Class: ExperimentalConditions 


_Environmental and experimental conditions_





URI: [lambdaber:ExperimentalConditions](https://w3id.org/lambda-ber-schema/ExperimentalConditions)





```mermaid
 classDiagram
    class ExperimentalConditions
    click ExperimentalConditions href "../ExperimentalConditions/"
      AttributeGroup <|-- ExperimentalConditions
        click AttributeGroup href "../AttributeGroup/"
      
      ExperimentalConditions : atmosphere
        
      ExperimentalConditions : beam_energy
        
      ExperimentalConditions : description
        
      ExperimentalConditions : exposure_time
        
      ExperimentalConditions : humidity
        
      ExperimentalConditions : pressure
        
      ExperimentalConditions : temperature
        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * **ExperimentalConditions**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [temperature](temperature.md) | 0..1 <br/> [Float](Float.md) | Temperature in Celsius | direct |
| [humidity](humidity.md) | 0..1 <br/> [Float](Float.md) | Humidity percentage | direct |
| [pressure](pressure.md) | 0..1 <br/> [Float](Float.md) | Pressure in kPa | direct |
| [atmosphere](atmosphere.md) | 0..1 <br/> [String](String.md) | Atmosphere composition | direct |
| [beam_energy](beam_energy.md) | 0..1 <br/> [Float](Float.md) | Beam energy in keV | direct |
| [exposure_time](exposure_time.md) | 0..1 <br/> [Float](Float.md) | Exposure time in seconds | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | [experimental_conditions](experimental_conditions.md) | range | [ExperimentalConditions](ExperimentalConditions.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:ExperimentalConditions |
| native | lambdaber:ExperimentalConditions |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExperimentalConditions
description: Environmental and experimental conditions
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeGroup
attributes:
  temperature:
    name: temperature
    description: Temperature in Celsius
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - StorageConditions
    - ExperimentalConditions
    - MeasurementConditions
    range: float
  humidity:
    name: humidity
    description: Humidity percentage
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ExperimentalConditions
    range: float
  pressure:
    name: pressure
    description: Pressure in kPa
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - ExperimentalConditions
    range: float
  atmosphere:
    name: atmosphere
    description: Atmosphere composition
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - StorageConditions
    - ExperimentalConditions
  beam_energy:
    name: beam_energy
    description: Beam energy in keV
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - XRFImage
    - ExperimentalConditions
    range: float
  exposure_time:
    name: exposure_time
    description: Exposure time in seconds
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - Image
    - ExperimentalConditions
    range: float

```
</details>

### Induced

<details>
```yaml
name: ExperimentalConditions
description: Environmental and experimental conditions
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeGroup
attributes:
  temperature:
    name: temperature
    description: Temperature in Celsius
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: temperature
    owner: ExperimentalConditions
    domain_of:
    - StorageConditions
    - ExperimentalConditions
    - MeasurementConditions
    range: float
  humidity:
    name: humidity
    description: Humidity percentage
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: humidity
    owner: ExperimentalConditions
    domain_of:
    - ExperimentalConditions
    range: float
  pressure:
    name: pressure
    description: Pressure in kPa
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: pressure
    owner: ExperimentalConditions
    domain_of:
    - ExperimentalConditions
    range: float
  atmosphere:
    name: atmosphere
    description: Atmosphere composition
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: atmosphere
    owner: ExperimentalConditions
    domain_of:
    - StorageConditions
    - ExperimentalConditions
    range: string
  beam_energy:
    name: beam_energy
    description: Beam energy in keV
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: beam_energy
    owner: ExperimentalConditions
    domain_of:
    - XRFImage
    - ExperimentalConditions
    range: float
  exposure_time:
    name: exposure_time
    description: Exposure time in seconds
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: exposure_time
    owner: ExperimentalConditions
    domain_of:
    - Image
    - ExperimentalConditions
    range: float
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: description
    owner: ExperimentalConditions
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>