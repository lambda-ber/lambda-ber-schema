

# Slot: resolution_at_corner 


_Resolution at corner of detector, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:resolution_at_corner](https://w3id.org/lambda-ber-schema/resolution_at_corner)
Alias: resolution_at_corner

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:resolution_at_corner |
| native | lambdaber:resolution_at_corner |
| exact | ispyb:DataCollection.resolutionAtCorner |




## LinkML Source

<details>
```yaml
name: resolution_at_corner
description: Resolution at corner of detector, typically specified in Angstroms (Å).
  Data providers may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:DataCollection.resolutionAtCorner
rank: 1000
alias: resolution_at_corner
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>