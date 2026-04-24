

# Slot: ethane_temperature 


_Ethane temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:ethane_temperature](http://w3id.org/lambda/ethane_temperature)
Alias: ethane_temperature

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
| self | lambda:ethane_temperature |
| native | lambda:ethane_temperature |
| exact | mmCIF:_em_vitrification.cryogen_name |




## LinkML Source

<details>
```yaml
name: ethane_temperature
description: Ethane temperature, typically specified in degrees Celsius. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_vitrification.cryogen_name
rank: 1000
alias: ethane_temperature
owner: CryoEMPreparation
domain_of:
- CryoEMPreparation
range: QuantityValue
inlined: true

```
</details>