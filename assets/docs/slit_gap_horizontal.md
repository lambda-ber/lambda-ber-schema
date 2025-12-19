

# Slot: slit_gap_horizontal 


_Horizontal slit gap aperture, typically specified in micrometers (µm). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:slit_gap_horizontal](https://w3id.org/lambda-ber-schema/slit_gap_horizontal)
Alias: slit_gap_horizontal

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
| self | lambdaber:slit_gap_horizontal |
| native | lambdaber:slit_gap_horizontal |
| exact | ispyb:DataCollection.slitGapHorizontal |




## LinkML Source

<details>
```yaml
name: slit_gap_horizontal
description: Horizontal slit gap aperture, typically specified in micrometers (µm).
  Data providers may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:DataCollection.slitGapHorizontal
rank: 1000
alias: slit_gap_horizontal
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>