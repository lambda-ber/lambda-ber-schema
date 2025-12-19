

# Class: DateTimeValue 


_A date or date and time value._





URI: [nmdc:DateTimeValue](https://w3id.org/nmdc/DateTimeValue)





```mermaid
 classDiagram
    class DateTimeValue
    click DateTimeValue href "../DateTimeValue/"
      AttributeValue <|-- DateTimeValue
        click AttributeValue href "../AttributeValue/"
      
      DateTimeValue : attribute
        
          
    
        
        
        DateTimeValue --> "0..1" Attribute : attribute
        click Attribute href "../Attribute/"
    

        
      DateTimeValue : raw_value
        
      DateTimeValue : value
        
      
```





## Inheritance
* [AttributeValue](AttributeValue.md)
    * **DateTimeValue**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [value](value.md) | 1 <br/> [String](String.md) | The date or date/time value, expressed in ISO 8601-compatible form | direct |
| [attribute](attribute.md) | 0..1 <br/> [Attribute](Attribute.md) | The attribute being represented | [AttributeValue](AttributeValue.md) |
| [raw_value](raw_value.md) | 0..1 <br/> [String](String.md) | Unnormalized atomic string representation, suggested syntax {number} {unit} | [AttributeValue](AttributeValue.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:DateTimeValue |
| native | lambdaber:DateTimeValue |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DateTimeValue
description: A date or date and time value.
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeValue
attributes:
  value:
    name: value
    description: The date or date/time value, expressed in ISO 8601-compatible form.
      Dates should be expressed as YYYY-MM-DD; times should be expressed as HH:MM:SS
      with optional milliseconds and an indication of the timezone.
    examples:
    - value: '2025-11-09'
    - value: '2025-09-16T22:48:54Z'
    from_schema: https://w3id.org/lambda-ber-schema/types
    domain_of:
    - TextValue
    - DateTimeValue
    - BiophysicalProperty
    range: string
    required: true
class_uri: nmdc:DateTimeValue

```
</details>

### Induced

<details>
```yaml
name: DateTimeValue
description: A date or date and time value.
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeValue
attributes:
  value:
    name: value
    description: The date or date/time value, expressed in ISO 8601-compatible form.
      Dates should be expressed as YYYY-MM-DD; times should be expressed as HH:MM:SS
      with optional milliseconds and an indication of the timezone.
    examples:
    - value: '2025-11-09'
    - value: '2025-09-16T22:48:54Z'
    from_schema: https://w3id.org/lambda-ber-schema/types
    alias: value
    owner: DateTimeValue
    domain_of:
    - TextValue
    - DateTimeValue
    - BiophysicalProperty
    range: string
    required: true
  attribute:
    name: attribute
    description: The attribute being represented.
    from_schema: https://w3id.org/lambda-ber-schema/types
    alias: attribute
    owner: DateTimeValue
    domain_of:
    - AttributeValue
    range: Attribute
  raw_value:
    name: raw_value
    description: Unnormalized atomic string representation, suggested syntax {number}
      {unit}
    from_schema: https://w3id.org/lambda-ber-schema/types
    alias: raw_value
    owner: DateTimeValue
    domain_of:
    - AttributeValue
    range: string
class_uri: nmdc:DateTimeValue

```
</details>