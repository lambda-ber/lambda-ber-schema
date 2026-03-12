

# Slot: maximum_numeric_value 


_The maximum value part, expressed as a number, of the quantity value when the value covers a range._





URI: [lambdaber:maximum_numeric_value](https://w3id.org/lambda-ber-schema/maximum_numeric_value)
Alias: maximum_numeric_value


## Inheritance

* [numeric_value](numeric_value.md)
    * **maximum_numeric_value**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:maximum_numeric_value |
| native | lambdaber:maximum_numeric_value |
| undefined | nmdc:maximum_numeric_value |




## LinkML Source

<details>
```yaml
name: maximum_numeric_value
description: The maximum value part, expressed as a number, of the quantity value
  when the value covers a range.
from_schema: https://w3id.org/lambda-ber-schema/
mappings:
- nmdc:maximum_numeric_value
rank: 1000
is_a: numeric_value
alias: maximum_numeric_value
domain_of:
- QuantityValue
range: float

```
</details>