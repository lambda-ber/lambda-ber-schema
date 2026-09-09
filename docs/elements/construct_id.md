

# Slot: construct_id 



URI: [lambda:construct_id](http://w3id.org/lambda/construct_id)
Alias: construct_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |
| [ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:construct_id |
| native | lambda:construct_id |




## LinkML Source

<details>
```yaml
name: construct_id
alias: construct_id
domain_of:
- ProteinConstruct
- SampleProteinAssociation
range: string

```
</details>