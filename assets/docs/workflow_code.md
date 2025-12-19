

# Slot: workflow_code 


_Human-friendly identifier for the computational workflow run (e.g., 'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing pipelines and computational provenance._





URI: [lambdaber:workflow_code](https://w3id.org/lambda-ber-schema/workflow_code)
Alias: workflow_code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:workflow_code |
| native | lambdaber:workflow_code |




## LinkML Source

<details>
```yaml
name: workflow_code
description: Human-friendly identifier for the computational workflow run (e.g., 'MOTION-CORR-RUN-001',
  'RELION-REFINE-240815'). Used for tracking processing pipelines and computational
  provenance.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: workflow_code
owner: WorkflowRun
domain_of:
- WorkflowRun
range: string
required: true

```
</details>