

# Slot: value 


_The value, as a text string._





URI: [lambda:value](http://w3id.org/lambda/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |  no  |
| [TextValue](TextValue.md) | A value described using a text string, optionally with a controlled vocabular... |  no  |
| [DateTimeValue](DateTimeValue.md) | A date or date and time value |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:value |
| native | lambda:value |




## LinkML Source

<details>
```yaml
name: value
description: The value, as a text string.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: value
domain_of:
- TextValue
- DateTimeValue
- BiophysicalProperty
range: string

```
</details>