# Enum: ParticleConcentrationEnum 




_Assessment of particle concentration on a cryo-EM grid_



URI: [lambda:ParticleConcentrationEnum](http://w3id.org/lambda/ParticleConcentrationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| optimal | None | Particle concentration is suitable for data collection |
| too_low | None | Particle concentration is too low for efficient data collection |
| too_high | None | Particle concentration is too high, causing overlapping particles |




## Slots

| Name | Description |
| ---  | --- |
| [particle_concentration](particle_concentration.md) | Assessment of particle concentration on the cryo-EM grid |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: ParticleConcentrationEnum
description: Assessment of particle concentration on a cryo-EM grid
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  optimal:
    text: optimal
    description: Particle concentration is suitable for data collection
  too_low:
    text: too_low
    description: Particle concentration is too low for efficient data collection
  too_high:
    text: too_high
    description: Particle concentration is too high, causing overlapping particles

```
</details>