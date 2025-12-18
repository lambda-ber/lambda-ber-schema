

# Slot: detector_distance 


_Distance from sample to detector_





URI: [lambdaber:detector_distance](https://w3id.org/lambda-ber-schema/detector_distance)
Alias: detector_distance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:detector_distance |
| native | lambdaber:detector_distance |
| exact | nsls2:Detector_distance, imgCIF:_diffrn_measurement.sample_detector_distance, mmCIF:_diffrn_detector.distance, ispyb:DataCollection.detectorDistance |




## LinkML Source

<details>
```yaml
name: detector_distance
description: Distance from sample to detector
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Detector_distance
- imgCIF:_diffrn_measurement.sample_detector_distance
- mmCIF:_diffrn_detector.distance
- ispyb:DataCollection.detectorDistance
rank: 1000
alias: detector_distance
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
unit:
  ucum_code: mm

```
</details>