

# Slot: crystal_id 


_Identifier for the specific crystal used_





URI: [nsls2:Crystal_ID](https://github.com/NSLS2/BER-LAMBDA/Crystal_ID)
Alias: crystal_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |  no  |






## Properties

* Range: [String](String.md)




## Comments

* Maps to NSLS2 spreadsheet: Crystal_ID

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Crystal_ID |
| native | lambdaber:crystal_id |




## LinkML Source

<details>
```yaml
name: crystal_id
description: Identifier for the specific crystal used
comments:
- 'Maps to NSLS2 spreadsheet: Crystal_ID'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Crystal_ID
alias: crystal_id
owner: CrystallizationConditions
domain_of:
- CrystallizationConditions
range: string

```
</details>