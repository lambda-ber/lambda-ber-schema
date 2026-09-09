

# Slot: sequence_coverage 


_Fraction of the canonical sequence present in this sample (range: 0-1)_





URI: [lambda:sequence_coverage](http://w3id.org/lambda/sequence_coverage)
Alias: sequence_coverage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |






## Properties

* Range: [Float](Float.md)

* Minimum Value: 0

* Maximum Value: 1




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:sequence_coverage |
| native | lambda:sequence_coverage |




## LinkML Source

<details>
```yaml
name: sequence_coverage
description: 'Fraction of the canonical sequence present in this sample (range: 0-1)'
from_schema: http://w3id.org/lambda/
rank: 1000
alias: sequence_coverage
owner: SampleProteinAssociation
domain_of:
- SampleProteinAssociation
range: float
minimum_value: 0
maximum_value: 1

```
</details>