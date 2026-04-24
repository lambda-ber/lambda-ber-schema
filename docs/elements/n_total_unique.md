

# Slot: n_total_unique 


_Total number of unique reflections_





URI: [lambda:n_total_unique](http://w3id.org/lambda/n_total_unique)
Alias: n_total_unique

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
| self | lambda:n_total_unique |
| native | lambda:n_total_unique |
| exact | mmCIF:_reflns.number_obs |




## LinkML Source

<details>
```yaml
name: n_total_unique
description: Total number of unique reflections
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_reflns.number_obs
rank: 1000
alias: n_total_unique
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>