

# Slot: humidity_percentage 


_Chamber humidity during vitrification (range: 0-100), typically specified as a percentage. Data providers may specify as decimal fraction by including the unit in the QuantityValue._





URI: [lambdaber:humidity_percentage](https://w3id.org/lambda-ber-schema/humidity_percentage)
Alias: humidity_percentage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMPreparation](CryoEMPreparation.md) | Cryo-EM specific sample preparation |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:humidity_percentage |
| native | lambdaber:humidity_percentage |




## LinkML Source

<details>
```yaml
name: humidity_percentage
description: 'Chamber humidity during vitrification (range: 0-100), typically specified
  as a percentage. Data providers may specify as decimal fraction by including the
  unit in the QuantityValue.'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: humidity_percentage
owner: CryoEMPreparation
domain_of:
- CryoEMPreparation
range: QuantityValue
inlined: true

```
</details>