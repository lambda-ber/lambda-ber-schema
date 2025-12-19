

# Slot: numeric_value 


_The numerical part of a quantity value, expressed as a number._





URI: [lambdaber:numeric_value](https://w3id.org/lambda-ber-schema/numeric_value)
Alias: numeric_value


## Inheritance

* **numeric_value**
    * [minimum_numeric_value](minimum_numeric_value.md)
    * [maximum_numeric_value](maximum_numeric_value.md)






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |  yes  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:numeric_value |
| native | lambdaber:numeric_value |
| undefined | nmdc:numeric_value, qud:quantityValue, schema:value |




## LinkML Source

<details>
```yaml
name: numeric_value
description: The numerical part of a quantity value, expressed as a number.
from_schema: https://w3id.org/lambda-ber-schema/
mappings:
- nmdc:numeric_value
- qud:quantityValue
- schema:value
rank: 1000
alias: numeric_value
domain_of:
- QuantityValue
range: float

```
</details>