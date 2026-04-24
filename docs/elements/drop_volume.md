

# Slot: drop_volume 


_Total drop volume, typically specified in nanoliters. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:drop_volume](http://w3id.org/lambda/drop_volume)
Alias: drop_volume

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:drop_volume |
| native | lambda:drop_volume |
| exact | nsls2:Drop_Volume |




## LinkML Source

<details>
```yaml
name: drop_volume
description: Total drop volume, typically specified in nanoliters. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Drop_Volume
rank: 1000
alias: drop_volume
owner: CrystallizationConditions
domain_of:
- CrystallizationConditions
range: QuantityValue
inlined: true

```
</details>