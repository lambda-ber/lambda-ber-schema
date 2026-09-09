

# Slot: modifications 



URI: [lambda:modifications](http://w3id.org/lambda/modifications)
Alias: modifications

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |
| [MolecularComposition](MolecularComposition.md) | Molecular composition of a sample |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:modifications |
| native | lambda:modifications |




## LinkML Source

<details>
```yaml
name: modifications
alias: modifications
domain_of:
- MolecularComposition
- SampleProteinAssociation
range: string

```
</details>