

# Slot: mounting_temperature 


_Temperature during mounting, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:mounting_temperature](http://w3id.org/lambda/mounting_temperature)
Alias: mounting_temperature

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:mounting_temperature |
| native | lambda:mounting_temperature |
| exact | nsls2:Temperature |




## LinkML Source

<details>
```yaml
name: mounting_temperature
description: Temperature during mounting, typically specified in Kelvin. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Temperature
rank: 1000
alias: mounting_temperature
owner: XRayPreparation
domain_of:
- XRayPreparation
range: QuantityValue
inlined: true

```
</details>