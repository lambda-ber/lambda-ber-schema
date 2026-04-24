

# Slot: raw_value 


_The value that was specified in raw form, i.e. a string. E.g. "2 Angstroms" or "2-4 micrometers"_





URI: [lambda:raw_value](http://w3id.org/lambda/raw_value)
Alias: raw_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |  yes  |
| [TextValue](TextValue.md) | A value described using a text string, optionally with a controlled vocabular... |  no  |
| [AttributeValue](AttributeValue.md) | The value for any attribute of an entity |  no  |
| [DateTimeValue](DateTimeValue.md) | A date or date and time value |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:raw_value |
| native | lambda:raw_value |
| undefined | nmdc:raw_value |




## LinkML Source

<details>
```yaml
name: raw_value
description: The value that was specified in raw form, i.e. a string. E.g. "2 Angstroms"
  or "2-4 micrometers"
from_schema: http://w3id.org/lambda/
mappings:
- nmdc:raw_value
rank: 1000
alias: raw_value
domain_of:
- AttributeValue
range: string

```
</details>