

# Slot: rmsd_angles 


_RMSD from ideal bond angles, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:rmsd_angles](http://w3id.org/lambda/rmsd_angles)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:rmsd_angles |
| native | lambda:rmsd_angles |
| exact | nsls2:RMSD_angles, mmCIF:_refine.pdbx_ls_sigma_I |




## LinkML Source

<details>
```yaml
name: rmsd_angles
description: RMSD from ideal bond angles, typically specified in degrees. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:RMSD_angles
- mmCIF:_refine.pdbx_ls_sigma_I
rank: 1000
alias: rmsd_angles
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>