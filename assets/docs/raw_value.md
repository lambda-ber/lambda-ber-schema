

# Slot: raw_value 


_The value that was specified in raw form, i.e. a string. E.g. "2 Angstroms" or "2-4 micrometers"_





URI: [lambdaber:raw_value](https://w3id.org/lambda-ber-schema/raw_value)
Alias: raw_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DateTimeValue](DateTimeValue.md) | A date or date and time value |  no  |
| [AttributeValue](AttributeValue.md) | The value for any attribute of an entity |  no  |
| [TextValue](TextValue.md) | A value described using a text string, optionally with a controlled vocabular... |  no  |
| [QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |  yes  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:raw_value |
| native | lambdaber:raw_value |
| undefined | nmdc:raw_value |




## LinkML Source

<details>
```yaml
name: raw_value
description: The value that was specified in raw form, i.e. a string. E.g. "2 Angstroms"
  or "2-4 micrometers"
from_schema: https://w3id.org/lambda-ber-schema/
mappings:
- nmdc:raw_value
rank: 1000
alias: raw_value
domain_of:
- AttributeValue
range: string

```
</details>