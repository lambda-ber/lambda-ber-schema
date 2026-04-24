

# Slot: total_rotation_deg 


_Total rotation range, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:total_rotation_deg](http://w3id.org/lambda/total_rotation_deg)
Alias: total_rotation_deg

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:total_rotation_deg |
| native | lambda:total_rotation_deg |
| exact | mmCIF:_diffrn_scan_axis.angle_range |




## LinkML Source

<details>
```yaml
name: total_rotation_deg
description: Total rotation range, typically specified in degrees. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_diffrn_scan_axis.angle_range
rank: 1000
alias: total_rotation_deg
owner: DataCollectionStrategy
domain_of:
- DataCollectionStrategy
range: QuantityValue
inlined: true

```
</details>