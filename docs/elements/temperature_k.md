

# Slot: temperature_k 


_Data collection temperature, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:temperature_k](http://w3id.org/lambda/temperature_k)
Alias: temperature_k

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:temperature_k |
| native | lambda:temperature_k |
| exact | mmCIF:_diffrn.ambient_temp |




## LinkML Source

<details>
```yaml
name: temperature_k
description: Data collection temperature, typically specified in Kelvin. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_diffrn.ambient_temp
rank: 1000
alias: temperature_k
owner: DataCollectionStrategy
domain_of:
- DataCollectionStrategy
range: QuantityValue
inlined: true

```
</details>