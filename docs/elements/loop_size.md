

# Slot: loop_size 


_Loop size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [nsls2:Loop_Size](https://github.com/NSLS2/BER-LAMBDA/Loop_Size)
Alias: loop_size

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* Maps to NSLS2 spreadsheet: Loop_Size

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Loop_Size |
| native | lambdaber:loop_size |




## LinkML Source

<details>
```yaml
name: loop_size
description: Loop size, typically specified in micrometers. Data providers may specify
  alternative units by including the unit in the QuantityValue.
comments:
- 'Maps to NSLS2 spreadsheet: Loop_Size'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Loop_Size
alias: loop_size
owner: XRayPreparation
domain_of:
- XRayPreparation
range: QuantityValue
inlined: true

```
</details>