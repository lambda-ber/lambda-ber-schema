

# Slot: ligand_interactions 



URI: [lambdaber:ligand_interactions](https://w3id.org/lambda-ber-schema/ligand_interactions)
Alias: ligand_interactions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:ligand_interactions |
| native | lambdaber:ligand_interactions |




## LinkML Source

<details>
```yaml
name: ligand_interactions
alias: ligand_interactions
domain_of:
- Sample
- FunctionalSite
- AggregatedProteinView
range: string

```
</details>