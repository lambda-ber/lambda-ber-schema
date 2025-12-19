

# Slot: value 


_The value, as a text string._





URI: [lambdaber:value](https://w3id.org/lambda-ber-schema/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DateTimeValue](DateTimeValue.md) | A date or date and time value |  no  |
| [TextValue](TextValue.md) | A value described using a text string, optionally with a controlled vocabular... |  no  |
| [BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:value |
| native | lambdaber:value |




## LinkML Source

<details>
```yaml
name: value
description: The value, as a text string.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: value
domain_of:
- TextValue
- DateTimeValue
- BiophysicalProperty
range: string

```
</details>