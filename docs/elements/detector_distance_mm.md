

# Slot: detector_distance_mm 


_Detector distance, typically specified in millimeters. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:detector_distance_mm](http://w3id.org/lambda/detector_distance_mm)
Alias: detector_distance_mm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* detector_distance


## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:detector_distance_mm |
| native | lambda:detector_distance_mm |
| exact | mmCIF:_diffrn_detector.distance |




## LinkML Source

<details>
```yaml
name: detector_distance_mm
description: Detector distance, typically specified in millimeters. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
aliases:
- detector_distance
exact_mappings:
- mmCIF:_diffrn_detector.distance
rank: 1000
alias: detector_distance_mm
owner: DataCollectionStrategy
domain_of:
- DataCollectionStrategy
range: QuantityValue
inlined: true

```
</details>