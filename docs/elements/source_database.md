

# Slot: source_database 


_Source database or resource that provided this annotation_





URI: [lambdaber:source_database](https://w3id.org/lambda-ber-schema/source_database)
Alias: source_database

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |






## Properties

* Range: [AnnotationSourceEnum](AnnotationSourceEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:source_database |
| native | lambdaber:source_database |




## LinkML Source

<details>
```yaml
name: source_database
description: Source database or resource that provided this annotation
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: source_database
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: AnnotationSourceEnum

```
</details>