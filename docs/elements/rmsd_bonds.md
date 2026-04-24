

# Slot: rmsd_bonds 


_RMSD from ideal bond lengths, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:rmsd_bonds](http://w3id.org/lambda/rmsd_bonds)
Alias: rmsd_bonds

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
| self | lambda:rmsd_bonds |
| native | lambda:rmsd_bonds |
| exact | nsls2:RMSD_bonds, mmCIF:_refine.pdbx_ls_sigma_F |




## LinkML Source

<details>
```yaml
name: rmsd_bonds
description: RMSD from ideal bond lengths, typically specified in Angstroms (Å). Data
  providers may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:RMSD_bonds
- mmCIF:_refine.pdbx_ls_sigma_F
rank: 1000
alias: rmsd_bonds
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>