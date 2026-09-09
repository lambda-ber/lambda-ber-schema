

# Slot: workflow_person_associations 


_Links between workflow runs and people (M:N with role)_





URI: [lambda:workflow_person_associations](http://w3id.org/lambda/workflow_person_associations)
Alias: workflow_person_associations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |






## Properties

* Range: [WorkflowPersonAssociation](WorkflowPersonAssociation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:workflow_person_associations |
| native | lambda:workflow_person_associations |




## LinkML Source

<details>
```yaml
name: workflow_person_associations
description: Links between workflow runs and people (M:N with role)
from_schema: http://w3id.org/lambda/
rank: 1000
alias: workflow_person_associations
owner: Dataset
domain_of:
- Dataset
range: WorkflowPersonAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>