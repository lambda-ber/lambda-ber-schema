

# Slot: annotation_method 


_Computational or experimental method used_





URI: [lambdaber:annotation_method](https://w3id.org/lambda-ber-schema/annotation_method)
Alias: annotation_method

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

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:annotation_method |
| native | lambdaber:annotation_method |




## LinkML Source

<details>
```yaml
name: annotation_method
description: Computational or experimental method used
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: annotation_method
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string

```
</details>