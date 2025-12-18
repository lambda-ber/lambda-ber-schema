

# Slot: mounting_temperature 


_Temperature during mounting in Kelvin_





URI: [nsls2:Temperature](https://github.com/NSLS2/BER-LAMBDA/Temperature)
Alias: mounting_temperature

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* Maps to NSLS2 spreadsheet: Temperature

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nsls2:Temperature |
| native | lambdaber:mounting_temperature |




## LinkML Source

<details>
```yaml
name: mounting_temperature
description: Temperature during mounting in Kelvin
comments:
- 'Maps to NSLS2 spreadsheet: Temperature'
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
slot_uri: nsls2:Temperature
alias: mounting_temperature
owner: XRayPreparation
domain_of:
- XRayPreparation
range: float

```
</details>