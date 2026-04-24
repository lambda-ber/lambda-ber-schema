

# Slot: evidence_type 


_Type of evidence supporting this annotation_





URI: [lambda:evidence_type](http://w3id.org/lambda/evidence_type)
Alias: evidence_type

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

* Range: [EvidenceTypeEnum](EvidenceTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:evidence_type |
| native | lambda:evidence_type |




## LinkML Source

<details>
```yaml
name: evidence_type
description: Type of evidence supporting this annotation
from_schema: http://w3id.org/lambda/
rank: 1000
alias: evidence_type
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: EvidenceTypeEnum

```
</details>