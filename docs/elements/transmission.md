

# Slot: transmission 


_X-ray beam transmission as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue._





URI: [lambda:transmission](http://w3id.org/lambda/transmission)
Alias: transmission

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* attenuation
* transmission_percent


## Comments

* Percentage of full beam intensity used

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:transmission |
| native | lambda:transmission |
| exact | ispyb:DataCollection.transmission |




## LinkML Source

<details>
```yaml
name: transmission
description: X-ray beam transmission as a percentage (0-100). Data providers may specify
  as a decimal fraction or percentage by including the unit in the QuantityValue.
comments:
- Percentage of full beam intensity used
from_schema: http://w3id.org/lambda/
aliases:
- attenuation
- transmission_percent
exact_mappings:
- ispyb:DataCollection.transmission
rank: 1000
alias: transmission
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>