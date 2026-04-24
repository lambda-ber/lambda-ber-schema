

# Slot: concentration 


_Sample concentration, typically specified in mg/mL or µM. Data providers may specify alternative units (e.g., molar, g/L) by including the unit in the QuantityValue._





URI: [lambda:concentration](http://w3id.org/lambda/concentration)
Alias: concentration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:concentration |
| native | lambda:concentration |




## LinkML Source

<details>
```yaml
name: concentration
description: Sample concentration, typically specified in mg/mL or µM. Data providers
  may specify alternative units (e.g., molar, g/L) by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: concentration
owner: Sample
domain_of:
- Sample
range: QuantityValue
inlined: true

```
</details>