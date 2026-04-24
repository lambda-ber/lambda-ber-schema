

# Slot: source_database 


_Source database or resource that provided this annotation_





URI: [lambda:source_database](http://w3id.org/lambda/source_database)
Alias: source_database

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

* Range: [AnnotationSourceEnum](AnnotationSourceEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:source_database |
| native | lambda:source_database |




## LinkML Source

<details>
```yaml
name: source_database
description: Source database or resource that provided this annotation
from_schema: http://w3id.org/lambda/
rank: 1000
alias: source_database
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: AnnotationSourceEnum

```
</details>