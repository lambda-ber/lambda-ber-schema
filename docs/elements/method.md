

# Slot: method 


_Crystallization method used_





URI: [lambda:method](http://w3id.org/lambda/method)
Alias: method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |  no  |






## Properties

* Range: [CrystallizationMethodEnum](CrystallizationMethodEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:method |
| native | lambda:method |
| exact | nsls2:Method, mmCIF:_exptl_crystal_grow.method |




## LinkML Source

<details>
```yaml
name: method
description: Crystallization method used
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Method
- mmCIF:_exptl_crystal_grow.method
rank: 1000
alias: method
owner: CrystallizationConditions
domain_of:
- CrystallizationConditions
range: CrystallizationMethodEnum

```
</details>