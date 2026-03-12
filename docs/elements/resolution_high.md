

# Slot: resolution_high 


_High resolution limit, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:resolution_high](https://w3id.org/lambda-ber-schema/resolution_high)
Alias: resolution_high

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
| self | lambdaber:resolution_high |
| native | lambdaber:resolution_high |
| exact | nsls2:Resolution_High_A, mmCIF:_reflns.d_resolution_high, ispyb:AutoProcScalingStatistics.resolutionLimitHigh |




## LinkML Source

<details>
```yaml
name: resolution_high
description: High resolution limit, typically specified in Angstroms (Å). Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Resolution_High_A
- mmCIF:_reflns.d_resolution_high
- ispyb:AutoProcScalingStatistics.resolutionLimitHigh
rank: 1000
alias: resolution_high
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>