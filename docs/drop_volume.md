

# Slot: drop_volume 


_Total drop volume in nanoliters_





URI: [nsls2:Drop_Volume](https://github.com/NSLS2/BER-LAMBDA/Drop_Volume)
Alias: drop_volume

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* Maps to NSLS2 spreadsheet: Drop_Volume

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Drop_Volume |
| native | lambdaber:drop_volume |




## LinkML Source

<details>
```yaml
name: drop_volume
description: Total drop volume in nanoliters
comments:
- 'Maps to NSLS2 spreadsheet: Drop_Volume'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Drop_Volume
alias: drop_volume
owner: CrystallizationConditions
domain_of:
- CrystallizationConditions
range: float

```
</details>