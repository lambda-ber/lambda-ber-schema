

# Slot: ligand 


_Ligand or small molecule bound to sample_





URI: [nsls2:Ligand](https://github.com/NSLS2/BER-LAMBDA/Ligand)
Alias: ligand

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [String](String.md)




## Comments

* Maps to NSLS2 spreadsheet: Ligand

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Ligand |
| native | lambdaber:ligand |




## LinkML Source

<details>
```yaml
name: ligand
description: Ligand or small molecule bound to sample
comments:
- 'Maps to NSLS2 spreadsheet: Ligand'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Ligand
alias: ligand
owner: Sample
domain_of:
- Sample
range: string

```
</details>