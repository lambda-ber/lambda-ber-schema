

# Slot: residue_range 


_Range of residues (e.g., '1-100', '25,27,30-35')_





URI: [lambda:residue_range](http://w3id.org/lambda/residue_range)
Alias: residue_range

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

* Range: [String](String.md)

* Regex pattern: `^[0-9,\-]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:residue_range |
| native | lambda:residue_range |




## LinkML Source

<details>
```yaml
name: residue_range
description: Range of residues (e.g., '1-100', '25,27,30-35')
from_schema: http://w3id.org/lambda/
rank: 1000
alias: residue_range
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string
pattern: ^[0-9,\-]+$

```
</details>