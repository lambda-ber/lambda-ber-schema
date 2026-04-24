

# Slot: oscillation_per_image_deg 


_Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:oscillation_per_image_deg](http://w3id.org/lambda/oscillation_per_image_deg)
Alias: oscillation_per_image_deg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* oscillation_width


## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:oscillation_per_image_deg |
| native | lambda:oscillation_per_image_deg |
| exact | mmCIF:_diffrn_scan.angle_increment |




## LinkML Source

<details>
```yaml
name: oscillation_per_image_deg
description: Oscillation angle per image, typically specified in degrees. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
aliases:
- oscillation_width
exact_mappings:
- mmCIF:_diffrn_scan.angle_increment
rank: 1000
alias: oscillation_per_image_deg
owner: DataCollectionStrategy
domain_of:
- DataCollectionStrategy
range: QuantityValue
inlined: true

```
</details>