

# Slot: experiment_code 


_Human-friendly laboratory or facility identifier for the experiment (e.g., 'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and cross-referencing within laboratory systems._





URI: [lambda:experiment_code](http://w3id.org/lambda/experiment_code)
Alias: experiment_code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:experiment_code |
| native | lambda:experiment_code |




## LinkML Source

<details>
```yaml
name: experiment_code
description: Human-friendly laboratory or facility identifier for the experiment (e.g.,
  'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and
  cross-referencing within laboratory systems.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: experiment_code
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string
required: true

```
</details>