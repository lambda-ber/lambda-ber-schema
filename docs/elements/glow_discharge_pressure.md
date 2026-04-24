

# Slot: glow_discharge_pressure 


_Glow discharge pressure, typically specified in millibars. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:glow_discharge_pressure](http://w3id.org/lambda/glow_discharge_pressure)
Alias: glow_discharge_pressure

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
| self | lambda:glow_discharge_pressure |
| native | lambda:glow_discharge_pressure |
| exact | mmCIF:_em_sample_support.pretreatment_pressure |




## LinkML Source

<details>
```yaml
name: glow_discharge_pressure
description: Glow discharge pressure, typically specified in millibars. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_sample_support.pretreatment_pressure
rank: 1000
alias: glow_discharge_pressure
owner: CryoEMPreparation
domain_of:
- CryoEMPreparation
range: QuantityValue
inlined: true

```
</details>