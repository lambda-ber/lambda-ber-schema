

# Slot: pdb_entry 


_PDB identifier_





URI: [lambda:pdb_entry](http://w3id.org/lambda/pdb_entry)
Alias: pdb_entry

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

* Regex pattern: `^[0-9][A-Za-z0-9]{3}$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:pdb_entry |
| native | lambda:pdb_entry |




## LinkML Source

<details>
```yaml
name: pdb_entry
description: PDB identifier
from_schema: http://w3id.org/lambda/
rank: 1000
alias: pdb_entry
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string
pattern: ^[0-9][A-Za-z0-9]{3}$

```
</details>