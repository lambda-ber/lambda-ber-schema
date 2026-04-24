

# Slot: ligand_id 


_Ligand identifier (ChEMBL, ChEBI, PubChem)_





URI: [lambda:ligand_id](http://w3id.org/lambda/ligand_id)
Alias: ligand_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LigandInteraction](LigandInteraction.md) | Small molecule/ligand interactions with proteins |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ligand_id |
| native | lambda:ligand_id |




## LinkML Source

<details>
```yaml
name: ligand_id
description: Ligand identifier (ChEMBL, ChEBI, PubChem)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: ligand_id
owner: LigandInteraction
domain_of:
- LigandInteraction
range: uriorcurie
required: true

```
</details>