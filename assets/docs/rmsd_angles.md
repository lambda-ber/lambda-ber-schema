

# Slot: rmsd_angles 


_RMSD from ideal bond angles, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:rmsd_angles](https://w3id.org/lambda-ber-schema/rmsd_angles)
Alias: rmsd_angles

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
| self | lambdaber:rmsd_angles |
| native | lambdaber:rmsd_angles |
| exact | nsls2:RMSD_angles, mmCIF:_refine.ls_d_res_low |




## LinkML Source

<details>
```yaml
name: rmsd_angles
description: RMSD from ideal bond angles, typically specified in degrees. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:RMSD_angles
- mmCIF:_refine.ls_d_res_low
rank: 1000
alias: rmsd_angles
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>