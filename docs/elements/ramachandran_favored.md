

# Slot: ramachandran_favored 


_Percentage of residues in favored Ramachandran regions (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue._





URI: [lambda:ramachandran_favored](http://w3id.org/lambda/ramachandran_favored)
Alias: ramachandran_favored

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
| self | lambda:ramachandran_favored |
| native | lambda:ramachandran_favored |
| exact | nsls2:Ramachandran_Favored, mmCIF:_pdbx_struct_quality.ramachandran_favored |




## LinkML Source

<details>
```yaml
name: ramachandran_favored
description: Percentage of residues in favored Ramachandran regions (0-100). Data
  providers may specify as a decimal fraction or percentage by including the unit
  in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Ramachandran_Favored
- mmCIF:_pdbx_struct_quality.ramachandran_favored
rank: 1000
alias: ramachandran_favored
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>