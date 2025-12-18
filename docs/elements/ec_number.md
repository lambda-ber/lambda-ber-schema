

# Slot: ec_number 


_Enzyme Commission number for catalytic sites_





URI: [lambdaber:ec_number](https://w3id.org/lambda-ber-schema/ec_number)
Alias: ec_number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:ec_number |
| native | lambdaber:ec_number |




## LinkML Source

<details>
```yaml
name: ec_number
description: Enzyme Commission number for catalytic sites
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: ec_number
owner: FunctionalSite
domain_of:
- FunctionalSite
range: string
pattern: ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$

```
</details>