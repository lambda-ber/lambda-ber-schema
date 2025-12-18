

# Slot: anomalous_multiplicity 


_Multiplicity of anomalous data_





URI: [lambdaber:anomalous_multiplicity](https://w3id.org/lambda-ber-schema/anomalous_multiplicity)
Alias: anomalous_multiplicity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* Redundancy of Bijvoet pairs

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:anomalous_multiplicity |
| native | lambdaber:anomalous_multiplicity |
| exact | ispyb:AutoProcScalingStatistics.anomalousMultiplicity |




## LinkML Source

<details>
```yaml
name: anomalous_multiplicity
description: Multiplicity of anomalous data
comments:
- Redundancy of Bijvoet pairs
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:AutoProcScalingStatistics.anomalousMultiplicity
rank: 1000
alias: anomalous_multiplicity
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float

```
</details>