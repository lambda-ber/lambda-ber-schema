

# Slot: n_total_observations 


_Total number of observations (before merging)_





URI: [lambda:n_total_observations](http://w3id.org/lambda/n_total_observations)
Alias: n_total_observations

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
| self | lambda:n_total_observations |
| native | lambda:n_total_observations |
| exact | mmCIF:_reflns.number_all |




## LinkML Source

<details>
```yaml
name: n_total_observations
description: Total number of observations (before merging)
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_reflns.number_all
rank: 1000
alias: n_total_observations
owner: WorkflowRun
domain_of:
- WorkflowRun
range: QuantityValue
inlined: true

```
</details>