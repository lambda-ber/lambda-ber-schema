

# Slot: workflow_experiment_associations 


_Links between workflows and source experiments (M:N)_





URI: [lambda:workflow_experiment_associations](http://w3id.org/lambda/workflow_experiment_associations)
Alias: workflow_experiment_associations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |






## Properties

* Range: [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:workflow_experiment_associations |
| native | lambda:workflow_experiment_associations |




## LinkML Source

<details>
```yaml
name: workflow_experiment_associations
description: Links between workflows and source experiments (M:N)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: workflow_experiment_associations
owner: Dataset
domain_of:
- Dataset
range: WorkflowExperimentAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>