

# Slot: exposure_time_per_frame 


_Exposure time per frame in milliseconds_





URI: [lambda:exposure_time_per_frame](http://w3id.org/lambda/exposure_time_per_frame)
Alias: exposure_time_per_frame

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:exposure_time_per_frame |
| native | lambda:exposure_time_per_frame |
| exact | mmCIF:_em_image_recording.average_exposure_time |




## LinkML Source

<details>
```yaml
name: exposure_time_per_frame
description: Exposure time per frame in milliseconds
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_image_recording.average_exposure_time
rank: 1000
alias: exposure_time_per_frame
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>