

# Slot: pixel_size_y 


_Pixel size Y dimension_





URI: [lambdaber:pixel_size_y](https://w3id.org/lambda-ber-schema/pixel_size_y)
Alias: pixel_size_y

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* imgCIF: _array_element_size.size[2]

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:pixel_size_y |
| native | lambdaber:pixel_size_y |
| exact | nsls2:Pixel_size_y, imgCIF:_array_element_size.size |




## LinkML Source

<details>
```yaml
name: pixel_size_y
description: Pixel size Y dimension
comments:
- 'imgCIF: _array_element_size.size[2]'
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Pixel_size_y
- imgCIF:_array_element_size.size
rank: 1000
alias: pixel_size_y
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
unit:
  ucum_code: um

```
</details>