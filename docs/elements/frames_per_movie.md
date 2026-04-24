

# Slot: frames_per_movie 


_Number of frames per movie_





URI: [lambda:frames_per_movie](http://w3id.org/lambda/frames_per_movie)
Alias: frames_per_movie

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
| self | lambda:frames_per_movie |
| native | lambda:frames_per_movie |
| exact | mmCIF:_em_image_recording.num_frames_per_image |




## LinkML Source

<details>
```yaml
name: frames_per_movie
description: Number of frames per movie
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_image_recording.num_frames_per_image
rank: 1000
alias: frames_per_movie
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>