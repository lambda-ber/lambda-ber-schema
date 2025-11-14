

# Slot: protein_concentration 


_Protein concentration for crystallization in mg/mL_





URI: [nsls2:Protein_Concentration](https://github.com/NSLS2/BER-LAMBDA/Protein_Concentration)
Alias: protein_concentration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* Maps to NSLS2 spreadsheet: Protein_Concentration

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Protein_Concentration |
| native | lambdaber:protein_concentration |




## LinkML Source

<details>
```yaml
name: protein_concentration
description: Protein concentration for crystallization in mg/mL
comments:
- 'Maps to NSLS2 spreadsheet: Protein_Concentration'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Protein_Concentration
alias: protein_concentration
owner: CrystallizationConditions
domain_of:
- CrystallizationConditions
range: float

```
</details>