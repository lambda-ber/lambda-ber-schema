

# Slot: undulator_gap 


_Undulator gap setting in millimeters_





URI: [lambdaber:undulator_gap](https://w3id.org/lambda-ber-schema/undulator_gap)
Alias: undulator_gap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Float](Float.md)




## Comments

* Primary undulator gap for beamlines with insertion devices

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:undulator_gap |
| native | lambdaber:undulator_gap |
| exact | ispyb:DataCollection.undulatorGap1 |




## LinkML Source

<details>
```yaml
name: undulator_gap
description: Undulator gap setting in millimeters
comments:
- Primary undulator gap for beamlines with insertion devices
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:DataCollection.undulatorGap1
rank: 1000
alias: undulator_gap
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
unit:
  ucum_code: mm

```
</details>