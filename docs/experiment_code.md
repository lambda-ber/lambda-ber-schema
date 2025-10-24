

# Slot: experiment_code 


_Human-friendly laboratory or facility identifier for the experiment (e.g., 'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and cross-referencing within laboratory systems._





URI: [lambdaber:experiment_code](https://w3id.org/lambda-ber-schema/experiment_code)
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


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:experiment_code |
| native | lambdaber:experiment_code |




## LinkML Source

<details>
```yaml
name: experiment_code
description: Human-friendly laboratory or facility identifier for the experiment (e.g.,
  'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and
  cross-referencing within laboratory systems.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: experiment_code
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string
required: true

```
</details>