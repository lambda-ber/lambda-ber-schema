

# Slot: cc_anomalous 


_Anomalous correlation coefficient_





URI: [lambdaber:cc_anomalous](https://w3id.org/lambda-ber-schema/cc_anomalous)
Alias: cc_anomalous

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* Correlation coefficient between Bijvoet pairs

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:cc_anomalous |
| native | lambdaber:cc_anomalous |
| exact | ispyb:AutoProcScalingStatistics.ccAno |




## LinkML Source

<details>
```yaml
name: cc_anomalous
description: Anomalous correlation coefficient
comments:
- Correlation coefficient between Bijvoet pairs
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:AutoProcScalingStatistics.ccAno
rank: 1000
alias: cc_anomalous
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float

```
</details>