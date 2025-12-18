

# Slot: construct 


_Construct description (e.g., domain boundaries, truncations)_





URI: [nsls2:Construct](https://github.com/NSLS2/BER-LAMBDA/Construct)
Alias: construct

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [String](String.md)




## Comments

* Maps to NSLS2 spreadsheet: Construct

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Construct |
| native | lambdaber:construct |




## LinkML Source

<details>
```yaml
name: construct
description: Construct description (e.g., domain boundaries, truncations)
comments:
- 'Maps to NSLS2 spreadsheet: Construct'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Construct
alias: construct
owner: Sample
domain_of:
- Sample
range: string

```
</details>