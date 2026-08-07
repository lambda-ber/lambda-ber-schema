

# Slot: number_of_tilt_images 


_Number of images collected in the tilt series_





URI: [lambda:number_of_tilt_images](http://w3id.org/lambda/number_of_tilt_images)
Alias: number_of_tilt_images

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* For a symmetric series this is usually (tilt_angle_max - tilt_angle_min) / tilt_angle_increment + 1, but record the actual count since tilts are often skipped or discarded.

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:number_of_tilt_images |
| native | lambda:number_of_tilt_images |




## LinkML Source

<details>
```yaml
name: number_of_tilt_images
description: Number of images collected in the tilt series
comments:
- For a symmetric series this is usually (tilt_angle_max - tilt_angle_min) / tilt_angle_increment
  + 1, but record the actual count since tilts are often skipped or discarded.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: number_of_tilt_images
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>