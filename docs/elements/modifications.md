

# Slot: modifications 



URI: [lambda:modifications](http://w3id.org/lambda/modifications)
Alias: modifications

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MolecularComposition](MolecularComposition.md) | Molecular composition of a sample |  no  |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |
| [SampleNucleicAcidAssociation](SampleNucleicAcidAssociation.md) | M:N link between Sample and NucleicAcid |  no  |






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
- SampleNucleicAcidAssociation
range: string

```
</details>