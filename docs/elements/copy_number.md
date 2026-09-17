

# Slot: copy_number 



URI: [lambda:copy_number](http://w3id.org/lambda/copy_number)
Alias: copy_number

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
| self | lambda:copy_number |
| native | lambda:copy_number |




## LinkML Source

<details>
```yaml
name: copy_number
alias: copy_number
domain_of:
- SampleProteinAssociation
- SampleNucleicAcidAssociation
range: string

```
</details>