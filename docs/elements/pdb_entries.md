

# Slot: pdb_entries 



URI: [lambda:pdb_entries](http://w3id.org/lambda/pdb_entries)
Alias: pdb_entries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConformationalState](ConformationalState.md) | Individual conformational state |  no  |
| [NucleicAcid](NucleicAcid.md) | A nucleic acid as a molecular entity: one DNA, RNA or hybrid strand, with its... |  no  |
| [Protein](Protein.md) | A protein as a biological entity: its sequence, source organism, gene, and th... |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |






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
- NucleicAcid
- ConformationalState
- AggregatedProteinView
range: string

```
</details>