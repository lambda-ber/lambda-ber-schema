

# Slot: ramachandran_favored 


_Percentage of residues in favored Ramachandran regions_





URI: [lambdaber:ramachandran_favored](https://w3id.org/lambda-ber-schema/ramachandran_favored)
Alias: ramachandran_favored

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:ramachandran_favored |
| native | lambdaber:ramachandran_favored |
| exact | nsls2:Ramachandran_Favored, mmCIF:_refine.pdbx_overall_ESU_R |




## LinkML Source

<details>
```yaml
name: ramachandran_favored
description: Percentage of residues in favored Ramachandran regions
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Ramachandran_Favored
- mmCIF:_refine.pdbx_overall_ESU_R
rank: 1000
alias: ramachandran_favored
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float
unit:
  ucum_code: '%'

```
</details>