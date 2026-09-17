

# Slot: chain_ids 



URI: [lambda:chain_ids](http://w3id.org/lambda/chain_ids)
Alias: chain_ids

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
| self | lambda:chain_ids |
| native | lambda:chain_ids |




## LinkML Source

<details>
```yaml
name: chain_ids
alias: chain_ids
domain_of:
- SampleProteinAssociation
- SampleNucleicAcidAssociation
range: string

```
</details>