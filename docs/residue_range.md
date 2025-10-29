

# Slot: residue_range 


_Range of residues (e.g., '1-100', '25,27,30-35')_





URI: [lambdaber:residue_range](https://w3id.org/lambda-ber-schema/residue_range)
Alias: residue_range

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:residue_range |
| native | lambdaber:residue_range |




## LinkML Source

<details>
```yaml
name: residue_range
description: Range of residues (e.g., '1-100', '25,27,30-35')
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: residue_range
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string

```
</details>