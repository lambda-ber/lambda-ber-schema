

# Slot: observed_molecular_weight 



URI: [lambda:observed_molecular_weight](http://w3id.org/lambda/observed_molecular_weight)
Alias: observed_molecular_weight

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |
| [SampleNucleicAcidAssociation](SampleNucleicAcidAssociation.md) | M:N link between Sample and NucleicAcid |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:observed_molecular_weight |
| native | lambda:observed_molecular_weight |




## LinkML Source

<details>
```yaml
name: observed_molecular_weight
alias: observed_molecular_weight
domain_of:
- SampleProteinAssociation
- SampleNucleicAcidAssociation
range: string

```
</details>