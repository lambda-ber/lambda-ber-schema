

# Slot: tag 


_Affinity tag (e.g., His6, GST, MBP)_





URI: [nsls2:Tag](https://github.com/NSLS2/BER-LAMBDA/Tag)
Alias: tag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [String](String.md)




## Comments

* Maps to NSLS2 spreadsheet: Tag

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Tag |
| native | lambdaber:tag |




## LinkML Source

<details>
```yaml
name: tag
description: Affinity tag (e.g., His6, GST, MBP)
comments:
- 'Maps to NSLS2 spreadsheet: Tag'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Tag
alias: tag
owner: Sample
domain_of:
- Sample
range: string

```
</details>