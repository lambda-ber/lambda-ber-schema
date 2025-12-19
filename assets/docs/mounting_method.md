

# Slot: mounting_method 


_Crystal mounting method_





URI: [nsls2:Mount_Type](https://github.com/NSLS2/BER-LAMBDA/Mount_Type)
Alias: mounting_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |






## Properties

* Range: [String](String.md)




## Comments

* Maps to NSLS2 spreadsheet: Mount_Type

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Mount_Type |
| native | lambdaber:mounting_method |




## LinkML Source

<details>
```yaml
name: mounting_method
description: Crystal mounting method
comments:
- 'Maps to NSLS2 spreadsheet: Mount_Type'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Mount_Type
alias: mounting_method
owner: XRayPreparation
domain_of:
- XRayPreparation
range: string

```
</details>