

# Slot: protein_id 



URI: [lambdaber:protein_id](https://w3id.org/lambda-ber-schema/protein_id)
Alias: protein_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:protein_id |
| native | lambdaber:protein_id |




## LinkML Source

<details>
```yaml
name: protein_id
alias: protein_id
domain_of:
- ProteinAnnotation
- ConformationalEnsemble
range: string

```
</details>