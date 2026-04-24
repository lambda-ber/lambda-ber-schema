

# Slot: resolution_low 


_Low resolution limit, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:resolution_low](http://w3id.org/lambda/resolution_low)
Alias: resolution_low

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
| self | lambda:resolution_low |
| native | lambda:resolution_low |
| exact | nsls2:Resolution_Low_A, mmCIF:_reflns.d_resolution_low, ispyb:AutoProcScalingStatistics.resolutionLimitLow |




## LinkML Source

<details>
```yaml
name: resolution_low
description: Low resolution limit, typically specified in Angstroms (Å). Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Resolution_Low_A
- mmCIF:_reflns.d_resolution_low
- ispyb:AutoProcScalingStatistics.resolutionLimitLow
rank: 1000
alias: resolution_low
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>