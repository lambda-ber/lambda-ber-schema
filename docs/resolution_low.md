

# Slot: resolution_low 


_Low resolution limit_





URI: [lambdaber:resolution_low](https://w3id.org/lambda-ber-schema/resolution_low)
Alias: resolution_low

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
| self | lambdaber:resolution_low |
| native | lambdaber:resolution_low |
| exact | nsls2:Resolution_Low_A, mmCIF:_reflns.d_resolution_low |




## LinkML Source

<details>
```yaml
name: resolution_low
description: Low resolution limit
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Resolution_Low_A
- mmCIF:_reflns.d_resolution_low
rank: 1000
alias: resolution_low
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float
unit:
  ucum_code: Ao

```
</details>