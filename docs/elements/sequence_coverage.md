

# Slot: sequence_coverage 



URI: [lambda:sequence_coverage](http://w3id.org/lambda/sequence_coverage)
Alias: sequence_coverage

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
| self | lambda:sequence_coverage |
| native | lambda:sequence_coverage |




## LinkML Source

<details>
```yaml
name: sequence_coverage
alias: sequence_coverage
domain_of:
- SampleProteinAssociation
- SampleNucleicAcidAssociation
range: string

```
</details>