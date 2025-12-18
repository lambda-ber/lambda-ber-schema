

# Slot: chain_id 


_Chain identifier in the PDB structure_





URI: [lambdaber:chain_id](https://w3id.org/lambda-ber-schema/chain_id)
Alias: chain_id

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

* Range: [String](String.md)

* Regex pattern: `^[A-Za-z0-9]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:chain_id |
| native | lambdaber:chain_id |




## LinkML Source

<details>
```yaml
name: chain_id
description: Chain identifier in the PDB structure
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: chain_id
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string
pattern: ^[A-Za-z0-9]+$

```
</details>