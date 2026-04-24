

# Slot: attribute 


_The attribute being represented._





URI: [lambda:attribute](http://w3id.org/lambda/attribute)
Alias: attribute

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |  no  |
| [TextValue](TextValue.md) | A value described using a text string, optionally with a controlled vocabular... |  no  |
| [AttributeValue](AttributeValue.md) | The value for any attribute of an entity |  no  |
| [DateTimeValue](DateTimeValue.md) | A date or date and time value |  no  |






## Properties

* Range: [Attribute](Attribute.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:attribute |
| native | lambda:attribute |




## LinkML Source

<details>
```yaml
name: attribute
description: The attribute being represented.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: attribute
domain_of:
- AttributeValue
range: Attribute
required: true

```
</details>