

# Slot: processing_level 


_Processing level (0=raw, 1=corrected, 2=derived, 3=model)_





URI: [lambda:processing_level](http://w3id.org/lambda/processing_level)
Alias: processing_level

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:processing_level |
| native | lambda:processing_level |




## LinkML Source

<details>
```yaml
name: processing_level
description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: processing_level
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>