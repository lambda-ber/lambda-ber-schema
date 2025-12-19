

# Slot: completeness_percent 


_Data completeness as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue._





URI: [lambdaber:completeness_percent](https://w3id.org/lambda-ber-schema/completeness_percent)
Alias: completeness_percent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:completeness_percent |
| native | lambdaber:completeness_percent |
| exact | nsls2:Completeness, mmCIF:_reflns.percent_possible_obs, ispyb:AutoProcScalingStatistics.completeness |




## LinkML Source

<details>
```yaml
name: completeness_percent
description: Data completeness as a percentage (0-100). Data providers may specify
  as a decimal fraction or percentage by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Completeness
- mmCIF:_reflns.percent_possible_obs
- ispyb:AutoProcScalingStatistics.completeness
rank: 1000
alias: completeness_percent
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>