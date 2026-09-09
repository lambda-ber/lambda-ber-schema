

# Slot: copy_number 


_Copies of this protein per assembly in the sample (e.g., 4 for a homotetramer, 2 for each chain of an alpha2-beta2 heterotetramer). Omit when unknown rather than assuming 1._





URI: [lambda:copy_number](http://w3id.org/lambda/copy_number)
Alias: copy_number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleProteinAssociation](SampleProteinAssociation.md) | M:N link between Sample and Protein |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:copy_number |
| native | lambda:copy_number |
| exact | mmCIF:_entity.pdbx_number_of_molecules |




## LinkML Source

<details>
```yaml
name: copy_number
description: Copies of this protein per assembly in the sample (e.g., 4 for a homotetramer,
  2 for each chain of an alpha2-beta2 heterotetramer). Omit when unknown rather than
  assuming 1.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_entity.pdbx_number_of_molecules
rank: 1000
alias: copy_number
owner: SampleProteinAssociation
domain_of:
- SampleProteinAssociation
range: integer

```
</details>