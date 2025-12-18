

# Slot: ramachandran_outliers 


_Percentage of Ramachandran outliers_





URI: [lambdaber:ramachandran_outliers](https://w3id.org/lambda-ber-schema/ramachandran_outliers)
Alias: ramachandran_outliers

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
| self | lambdaber:ramachandran_outliers |
| native | lambdaber:ramachandran_outliers |
| exact | nsls2:Ramachandran_Outliers, mmCIF:_refine.pdbx_overall_ESU_R_Free |




## LinkML Source

<details>
```yaml
name: ramachandran_outliers
description: Percentage of Ramachandran outliers
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Ramachandran_Outliers
- mmCIF:_refine.pdbx_overall_ESU_R_Free
rank: 1000
alias: ramachandran_outliers
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float
unit:
  ucum_code: '%'

```
</details>