# Enum: OutputTypeEnum 




_Types of outputs from computational workflows_



URI: [lambda:OutputTypeEnum](http://w3id.org/lambda/OutputTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| map | None | Density map or reconstructed volume |
| model | None | Atomic model or coordinates |
| particles | None | Particle stack or extracted particles |
| micrographs | None | Motion-corrected micrographs |
| ctf_estimates | None | CTF estimation results |
| metadata | None | Metadata or parameter files |
| statistics | None | Processing statistics or quality metrics |
| processed_data | None | Processed or derived data files |
| log | None | Processing log files |




## Slots

| Name | Description |
| ---  | --- |
| [output_type](output_type.md) | Type of output from the workflow |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: OutputTypeEnum
description: Types of outputs from computational workflows
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  map:
    text: map
    description: Density map or reconstructed volume
  model:
    text: model
    description: Atomic model or coordinates
  particles:
    text: particles
    description: Particle stack or extracted particles
  micrographs:
    text: micrographs
    description: Motion-corrected micrographs
  ctf_estimates:
    text: ctf_estimates
    description: CTF estimation results
  metadata:
    text: metadata
    description: Metadata or parameter files
  statistics:
    text: statistics
    description: Processing statistics or quality metrics
  processed_data:
    text: processed_data
    description: Processed or derived data files
  log:
    text: log
    description: Processing log files

```
</details>