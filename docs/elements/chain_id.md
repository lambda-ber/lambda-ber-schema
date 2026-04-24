

# Slot: chain_id 


_Chain identifier in the PDB structure_





URI: [lambda:chain_id](http://w3id.org/lambda/chain_id)
Alias: chain_id

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

* Regex pattern: `^[A-Za-z0-9]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:chain_id |
| native | lambda:chain_id |




## LinkML Source

<details>
```yaml
name: chain_id
description: Chain identifier in the PDB structure
from_schema: http://w3id.org/lambda/
rank: 1000
alias: chain_id
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string
pattern: ^[A-Za-z0-9]+$

```
</details>