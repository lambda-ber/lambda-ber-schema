

# Slot: molecular_weight 


_Molecular weight, typically specified in kilodaltons (kDa). Data providers may specify alternative units (e.g., Daltons, g/mol) by including the unit in the QuantityValue._





URI: [lambdaber:molecular_weight](https://w3id.org/lambda-ber-schema/molecular_weight)
Alias: molecular_weight

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:molecular_weight |
| native | lambdaber:molecular_weight |




## LinkML Source

<details>
```yaml
name: molecular_weight
description: Molecular weight, typically specified in kilodaltons (kDa). Data providers
  may specify alternative units (e.g., Daltons, g/mol) by including the unit in the
  QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: molecular_weight
owner: Sample
domain_of:
- Sample
range: QuantityValue
inlined: true

```
</details>