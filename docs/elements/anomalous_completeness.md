

# Slot: anomalous_completeness 


_Completeness of anomalous data as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue._





URI: [lambdaber:anomalous_completeness](https://w3id.org/lambda-ber-schema/anomalous_completeness)
Alias: anomalous_completeness

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* Completeness of Bijvoet pairs

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:anomalous_completeness |
| native | lambdaber:anomalous_completeness |
| exact | ispyb:AutoProcScalingStatistics.anomalousCompleteness |




## LinkML Source

<details>
```yaml
name: anomalous_completeness
description: Completeness of anomalous data as a percentage (0-100). Data providers
  may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
comments:
- Completeness of Bijvoet pairs
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:AutoProcScalingStatistics.anomalousCompleteness
rank: 1000
alias: anomalous_completeness
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>