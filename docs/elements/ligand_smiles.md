

# Slot: ligand_smiles 


_SMILES representation of the ligand_





URI: [lambda:ligand_smiles](http://w3id.org/lambda/ligand_smiles)
Alias: ligand_smiles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LigandInteraction](LigandInteraction.md) | Small molecule/ligand interactions with proteins |  no  |






## Properties

* Range: [SmilesString](SmilesString.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ligand_smiles |
| native | lambda:ligand_smiles |




## LinkML Source

<details>
```yaml
name: ligand_smiles
description: SMILES representation of the ligand
from_schema: http://w3id.org/lambda/
rank: 1000
alias: ligand_smiles
owner: LigandInteraction
domain_of:
- LigandInteraction
range: smiles_string

```
</details>