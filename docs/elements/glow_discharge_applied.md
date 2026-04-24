

# Slot: glow_discharge_applied 


_Whether glow discharge treatment was applied_





URI: [lambda:glow_discharge_applied](http://w3id.org/lambda/glow_discharge_applied)
Alias: glow_discharge_applied

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMPreparation](CryoEMPreparation.md) | Cryo-EM specific sample preparation |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:glow_discharge_applied |
| native | lambda:glow_discharge_applied |
| exact | mmCIF:_em_sample_support.pretreatment_type |




## LinkML Source

<details>
```yaml
name: glow_discharge_applied
description: Whether glow discharge treatment was applied
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_sample_support.pretreatment_type
rank: 1000
alias: glow_discharge_applied
owner: CryoEMPreparation
domain_of:
- CryoEMPreparation
range: boolean

```
</details>