

# Slot: wilson_b_factor 


_Wilson B-factor, typically specified in Angstroms squared (Ų). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:wilson_b_factor](https://w3id.org/lambda-ber-schema/wilson_b_factor)
Alias: wilson_b_factor

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
| self | lambdaber:wilson_b_factor |
| native | lambdaber:wilson_b_factor |
| exact | nsls2:Wilson_B, mmCIF:_reflns.B_iso_Wilson_estimate |




## LinkML Source

<details>
```yaml
name: wilson_b_factor
description: Wilson B-factor, typically specified in Angstroms squared (Ų). Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Wilson_B
- mmCIF:_reflns.B_iso_Wilson_estimate
rank: 1000
alias: wilson_b_factor
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>