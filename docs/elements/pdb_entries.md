

# Slot: pdb_entries 



URI: [lambda:pdb_entries](http://w3id.org/lambda/pdb_entries)
Alias: pdb_entries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a biological entity: its sequence, source organism, gene, and th... |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [ConformationalState](ConformationalState.md) | Individual conformational state |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:pdb_entries |
| native | lambda:pdb_entries |




## LinkML Source

<details>
```yaml
name: pdb_entries
alias: pdb_entries
domain_of:
- Protein
- ConformationalState
- AggregatedProteinView
range: string

```
</details>