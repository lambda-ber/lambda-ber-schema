

# Slot: processing_level 


_Processing level (0=raw, 1=corrected, 2=derived, 3=model)_





URI: [lambdaber:processing_level](https://w3id.org/lambda-ber-schema/processing_level)
Alias: processing_level

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 0

* Maximum Value: 4




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:processing_level |
| native | lambdaber:processing_level |




## LinkML Source

<details>
```yaml
name: processing_level
description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: processing_level
owner: WorkflowRun
domain_of:
- WorkflowRun
range: integer
minimum_value: 0
maximum_value: 4

```
</details>