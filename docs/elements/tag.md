

# Slot: tag 


_Affinity tag (e.g., His6, GST, MBP)_





URI: [lambda:tag](http://w3id.org/lambda/tag)
Alias: tag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:tag |
| native | lambda:tag |
| exact | nsls2:Tag |




## LinkML Source

<details>
```yaml
name: tag
description: Affinity tag (e.g., His6, GST, MBP)
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Tag
rank: 1000
alias: tag
owner: Sample
domain_of:
- Sample
range: string

```
</details>