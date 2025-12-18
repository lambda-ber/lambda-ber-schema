

# Slot: i_over_sigma 


_Mean I/sigma(I) - signal to noise ratio_





URI: [lambdaber:i_over_sigma](https://w3id.org/lambda-ber-schema/i_over_sigma)
Alias: i_over_sigma

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
| self | lambdaber:i_over_sigma |
| native | lambdaber:i_over_sigma |
| exact | nsls2:I_over_sigma, mmCIF:_reflns.pdbx_netI_over_sigmaI, ispyb:AutoProcScalingStatistics.meanIOverSigI |




## LinkML Source

<details>
```yaml
name: i_over_sigma
description: Mean I/sigma(I) - signal to noise ratio
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:I_over_sigma
- mmCIF:_reflns.pdbx_netI_over_sigmaI
- ispyb:AutoProcScalingStatistics.meanIOverSigI
rank: 1000
alias: i_over_sigma
owner: WorkflowRun
domain_of:
- WorkflowRun
range: float

```
</details>