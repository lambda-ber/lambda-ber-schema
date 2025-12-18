

# Slot: omim_id 


_OMIM database identifier_





URI: [lambdaber:omim_id](https://w3id.org/lambda-ber-schema/omim_id)
Alias: omim_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[0-9]{6}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:omim_id |
| native | lambdaber:omim_id |




## LinkML Source

<details>
```yaml
name: omim_id
description: OMIM database identifier
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: omim_id
owner: MutationEffect
domain_of:
- MutationEffect
range: string
pattern: ^[0-9]{6}$

```
</details>