

# Slot: symmetry 


_Symmetry applied (C1, Cn, Dn, T, O, I)_





URI: [lambda:symmetry](http://w3id.org/lambda/symmetry)
Alias: symmetry

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RefinementParameters](RefinementParameters.md) | Parameters specific to 3D refinement workflows |  no  |






## Properties

* Range: [SymmetryEnum](SymmetryEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:symmetry |
| native | lambda:symmetry |
| exact | mmCIF:_em_3d_reconstruction.symmetry_type |




## LinkML Source

<details>
```yaml
name: symmetry
description: Symmetry applied (C1, Cn, Dn, T, O, I)
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_3d_reconstruction.symmetry_type
rank: 1000
alias: symmetry
owner: RefinementParameters
domain_of:
- RefinementParameters
range: SymmetryEnum

```
</details>