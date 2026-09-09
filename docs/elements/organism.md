

# Slot: organism 



URI: [lambda:organism](http://w3id.org/lambda/organism)
Alias: organism

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A physical biological sample used in structural biology experiments |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [Protein](Protein.md) | A protein as a biological entity: its sequence, source organism, gene, and th... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:organism |
| native | lambda:organism |




## LinkML Source

<details>
```yaml
name: organism
alias: organism
domain_of:
- Sample
- Protein
- AggregatedProteinView
range: string

```
</details>