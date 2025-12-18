

# Slot: sig_anomalous 


_Mean anomalous difference signal_





URI: [lambdaber:sig_anomalous](https://w3id.org/lambda-ber-schema/sig_anomalous)
Alias: sig_anomalous

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* Mean |F(+) - F(-)|/sigma

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:sig_anomalous |
| native | lambdaber:sig_anomalous |
| exact | ispyb:AutoProcScalingStatistics.sigAno |




## LinkML Source

<details>
```yaml
name: sig_anomalous
description: Mean anomalous difference signal
comments:
- Mean |F(+) - F(-)|/sigma
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:AutoProcScalingStatistics.sigAno
rank: 1000
alias: sig_anomalous
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float

```
</details>