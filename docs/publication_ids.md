

# Slot: publication_ids 


_IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix._





URI: [lambdaber:publication_ids](https://w3id.org/lambda-ber-schema/publication_ids)
Alias: publication_ids

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:publication_ids |
| native | lambdaber:publication_ids |




## LinkML Source

<details>
```yaml
name: publication_ids
description: IDs of one or more publications supporting this annotation. Use PubMed
  IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: publication_ids
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string
multivalued: true
pattern: ^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$

```
</details>