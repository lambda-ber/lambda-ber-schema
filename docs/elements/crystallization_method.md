

# Slot: crystallization_method 


_Method used for crystallization_





URI: [lambda:crystallization_method](http://w3id.org/lambda/crystallization_method)
Alias: crystallization_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |  no  |






## Properties

* Range: [CrystallizationMethodEnum](CrystallizationMethodEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:crystallization_method |
| native | lambda:crystallization_method |
| exact | mmCIF:_exptl_crystal_grow.method |




## LinkML Source

<details>
```yaml
name: crystallization_method
description: Method used for crystallization
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_exptl_crystal_grow.method
rank: 1000
alias: crystallization_method
owner: XRayPreparation
domain_of:
- XRayPreparation
range: CrystallizationMethodEnum

```
</details>