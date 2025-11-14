

# Slot: completeness_percent 


_Data completeness percentage_





URI: [lambdaber:completeness_percent](https://w3id.org/lambda-ber-schema/completeness_percent)
Alias: completeness_percent

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
| self | lambdaber:completeness_percent |
| native | lambdaber:completeness_percent |
| exact | nsls2:Completeness, mmCIF:_reflns.percent_possible_obs |




## LinkML Source

<details>
```yaml
name: completeness_percent
description: Data completeness percentage
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Completeness
- mmCIF:_reflns.percent_possible_obs
rank: 1000
alias: completeness_percent
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float
unit:
  ucum_code: '%'

```
</details>