

# Slot: method 


_Crystallization method used_





URI: [nsls2:Method](https://github.com/NSLS2/BER-LAMBDA/Method)
Alias: method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |  no  |






## Properties

* Range: [CrystallizationMethodEnum](CrystallizationMethodEnum.md)




## Comments

* Maps to NSLS2 spreadsheet: Method

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Method |
| native | lambdaber:method |




## LinkML Source

<details>
```yaml
name: method
description: Crystallization method used
comments:
- 'Maps to NSLS2 spreadsheet: Method'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Method
alias: method
owner: CrystallizationConditions
domain_of:
- CrystallizationConditions
range: CrystallizationMethodEnum

```
</details>