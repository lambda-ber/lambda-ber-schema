

# Slot: ligand 


_Ligand or small molecule bound to sample_





URI: [lambda:ligand](http://w3id.org/lambda/ligand)
Alias: ligand

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ligand |
| native | lambda:ligand |
| exact | nsls2:Ligand |




## LinkML Source

<details>
```yaml
name: ligand
description: Ligand or small molecule bound to sample
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Ligand
rank: 1000
alias: ligand
owner: Sample
domain_of:
- Sample
range: string

```
</details>