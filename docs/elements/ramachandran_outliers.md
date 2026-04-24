

# Slot: ramachandran_outliers 


_Percentage of Ramachandran outliers (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue._





URI: [lambda:ramachandran_outliers](http://w3id.org/lambda/ramachandran_outliers)
Alias: ramachandran_outliers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ramachandran_outliers |
| native | lambda:ramachandran_outliers |
| exact | nsls2:Ramachandran_Outliers, mmCIF:_pdbx_struct_quality.ramachandran_outliers |




## LinkML Source

<details>
```yaml
name: ramachandran_outliers
description: Percentage of Ramachandran outliers (0-100). Data providers may specify
  as a decimal fraction or percentage by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Ramachandran_Outliers
- mmCIF:_pdbx_struct_quality.ramachandran_outliers
rank: 1000
alias: ramachandran_outliers
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>