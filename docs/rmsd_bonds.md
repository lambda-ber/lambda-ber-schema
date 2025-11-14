

# Slot: rmsd_bonds 


_RMSD from ideal bond lengths_





URI: [lambdaber:rmsd_bonds](https://w3id.org/lambda-ber-schema/rmsd_bonds)
Alias: rmsd_bonds

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
| self | lambdaber:rmsd_bonds |
| native | lambdaber:rmsd_bonds |
| exact | nsls2:RMSD_bonds, mmCIF:_refine.ls_d_res_high |




## LinkML Source

<details>
```yaml
name: rmsd_bonds
description: RMSD from ideal bond lengths
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:RMSD_bonds
- mmCIF:_refine.ls_d_res_high
rank: 1000
alias: rmsd_bonds
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float
unit:
  ucum_code: Ao

```
</details>