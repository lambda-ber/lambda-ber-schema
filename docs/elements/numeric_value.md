

# Slot: numeric_value 


_The numerical part of a quantity value, expressed as a number._





URI: [lambda:numeric_value](http://w3id.org/lambda/numeric_value)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:numeric_value |
| native | lambda:numeric_value |
| undefined | nmdc:numeric_value, qud:quantityValue, schema:value |




## LinkML Source

<details>
```yaml
name: numeric_value
description: The numerical part of a quantity value, expressed as a number.
from_schema: http://w3id.org/lambda/
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