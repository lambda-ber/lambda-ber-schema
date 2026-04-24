

# Slot: sample_code 


_Human-friendly laboratory identifier or facility code for the sample (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference and tracking within laboratory workflows._





URI: [lambda:sample_code](http://w3id.org/lambda/sample_code)
Alias: sample_code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:sample_code |
| native | lambda:sample_code |




## LinkML Source

<details>
```yaml
name: sample_code
description: Human-friendly laboratory identifier or facility code for the sample
  (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference and
  tracking within laboratory workflows.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: sample_code
owner: Sample
domain_of:
- Sample
range: string
required: true

```
</details>