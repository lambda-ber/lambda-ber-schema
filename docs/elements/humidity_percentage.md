

# Slot: humidity_percentage 


_Chamber humidity during vitrification (range: 0-100), typically specified as a percentage. Data providers may specify as decimal fraction by including the unit in the QuantityValue._





URI: [lambda:humidity_percentage](http://w3id.org/lambda/humidity_percentage)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:humidity_percentage |
| native | lambda:humidity_percentage |
| exact | mmCIF:_em_vitrification.chamber_humidity |




## LinkML Source

<details>
```yaml
name: humidity_percentage
description: 'Chamber humidity during vitrification (range: 0-100), typically specified
  as a percentage. Data providers may specify as decimal fraction by including the
  unit in the QuantityValue.'
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_vitrification.chamber_humidity
rank: 1000
alias: humidity_percentage
owner: CryoEMPreparation
domain_of:
- CryoEMPreparation
range: QuantityValue
inlined: true

```
</details>