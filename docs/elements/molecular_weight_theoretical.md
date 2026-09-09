

# Slot: molecular_weight_theoretical 


_Mass computed from the canonical sequence, typically in kDa. A mass measured for a given preparation belongs on SampleProteinAssociation.observed_molecular_weight._





URI: [lambda:molecular_weight_theoretical](http://w3id.org/lambda/molecular_weight_theoretical)
Alias: molecular_weight_theoretical

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a biological entity: its sequence, source organism, gene, and th... |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:molecular_weight_theoretical |
| native | lambda:molecular_weight_theoretical |
| related | mmCIF:_entity.formula_weight |




## LinkML Source

<details>
```yaml
name: molecular_weight_theoretical
description: Mass computed from the canonical sequence, typically in kDa. A mass measured
  for a given preparation belongs on SampleProteinAssociation.observed_molecular_weight.
from_schema: http://w3id.org/lambda/
related_mappings:
- mmCIF:_entity.formula_weight
rank: 1000
alias: molecular_weight_theoretical
owner: Protein
domain_of:
- Protein
range: QuantityValue
inlined: true

```
</details>