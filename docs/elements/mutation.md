

# Slot: mutation 


_Mutation in standard notation (e.g., 'A123V')_





URI: [lambdaber:mutation](https://w3id.org/lambda-ber-schema/mutation)
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


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:mutation |
| native | lambdaber:mutation |




## LinkML Source

<details>
```yaml
name: mutation
description: Mutation in standard notation (e.g., 'A123V')
from_schema: https://w3id.org/lambda-ber-schema/
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