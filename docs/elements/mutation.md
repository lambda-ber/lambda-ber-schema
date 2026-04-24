

# Slot: mutation 


_Mutation in standard notation (e.g., 'A123V')_





URI: [lambda:mutation](http://w3id.org/lambda/mutation)
Alias: mutation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[A-Z][0-9]+[A-Z]$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:mutation |
| native | lambda:mutation |




## LinkML Source

<details>
```yaml
name: mutation
description: Mutation in standard notation (e.g., 'A123V')
from_schema: http://w3id.org/lambda/
rank: 1000
alias: mutation
owner: MutationEffect
domain_of:
- MutationEffect
range: string
required: true
pattern: ^[A-Z][0-9]+[A-Z]$

```
</details>