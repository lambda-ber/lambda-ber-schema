

# Slot: transmission 


_X-ray beam transmission as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue._





URI: [lambdaber:transmission](https://w3id.org/lambda-ber-schema/transmission)
Alias: transmission

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* Percentage of full beam intensity used

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:transmission |
| native | lambdaber:transmission |
| exact | ispyb:DataCollection.transmission |




## LinkML Source

<details>
```yaml
name: transmission
description: X-ray beam transmission as a percentage (0-100). Data providers may specify
  as a decimal fraction or percentage by including the unit in the QuantityValue.
comments:
- Percentage of full beam intensity used
from_schema: https://w3id.org/lambda-ber-schema/
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