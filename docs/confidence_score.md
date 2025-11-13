

# Slot: confidence_score 


_Confidence score for the annotation (0-1)_





URI: [lambdaber:confidence_score](https://w3id.org/lambda-ber-schema/confidence_score)
Alias: confidence_score

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |






## Properties

* Range: [Float](Float.md)

* Minimum Value: 0

* Maximum Value: 1




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:confidence_score |
| native | lambdaber:confidence_score |




## LinkML Source

<details>
```yaml
name: confidence_score
description: Confidence score for the annotation (0-1)
from_schema: https://w3id.org/lambda-ber-schema/
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