

# Slot: attribute 


_The attribute being represented._





URI: [lambdaber:attribute](https://w3id.org/lambda-ber-schema/attribute)
Alias: attribute

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DateTimeValue](DateTimeValue.md) | A date or date and time value |  no  |
| [AttributeValue](AttributeValue.md) | The value for any attribute of an entity |  no  |
| [TextValue](TextValue.md) | A value described using a text string, optionally with a controlled vocabular... |  no  |
| [QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |  no  |






## Properties

* Range: [Attribute](Attribute.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:attribute |
| native | lambdaber:attribute |




## LinkML Source

<details>
```yaml
name: attribute
description: The attribute being represented.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: attribute
domain_of:
- AttributeValue
range: Attribute
required: true

```
</details>