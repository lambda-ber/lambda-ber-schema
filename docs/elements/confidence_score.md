

# Slot: confidence_score 


_Confidence score for the annotation (range: 0-1)_





URI: [lambda:confidence_score](http://w3id.org/lambda/confidence_score)
Alias: confidence_score

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |






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
| self | lambda:confidence_score |
| native | lambda:confidence_score |




## LinkML Source

<details>
```yaml
name: confidence_score
description: 'Confidence score for the annotation (range: 0-1)'
from_schema: http://w3id.org/lambda/
rank: 1000
alias: confidence_score
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: float
minimum_value: 0
maximum_value: 1

```
</details>