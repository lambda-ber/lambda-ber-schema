

# Slot: blot_time 


_Blotting time, typically specified in seconds (range: 0.5-10.0). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:blot_time](http://w3id.org/lambda/blot_time)
Alias: blot_time

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
| self | lambda:blot_time |
| native | lambda:blot_time |
| exact | mmCIF:_em_vitrification.time_resolved_state |




## LinkML Source

<details>
```yaml
name: blot_time
description: 'Blotting time, typically specified in seconds (range: 0.5-10.0). Data
  providers may specify alternative units by including the unit in the QuantityValue.'
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_vitrification.time_resolved_state
rank: 1000
alias: blot_time
owner: CryoEMPreparation
domain_of:
- CryoEMPreparation
range: QuantityValue
inlined: true

```
</details>