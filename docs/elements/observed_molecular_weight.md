

# Slot: observed_molecular_weight 


_Mass as measured for this preparation (mass spectrometry, SEC-MALS, SAXS), typically in kDa. The sequence-derived mass lives on Protein.molecular_weight_theoretical._





URI: [lambda:observed_molecular_weight](http://w3id.org/lambda/observed_molecular_weight)
Alias: observed_molecular_weight

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:observed_molecular_weight |
| native | lambda:observed_molecular_weight |




## LinkML Source

<details>
```yaml
name: observed_molecular_weight
description: Mass as measured for this preparation (mass spectrometry, SEC-MALS, SAXS),
  typically in kDa. The sequence-derived mass lives on Protein.molecular_weight_theoretical.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: observed_molecular_weight
owner: SampleProteinAssociation
domain_of:
- SampleProteinAssociation
range: QuantityValue
inlined: true

```
</details>