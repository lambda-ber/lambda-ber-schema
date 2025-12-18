

# Slot: flux_end 


_Photon flux at end of data collection in photons/second_





URI: [lambdaber:flux_end](https://w3id.org/lambda-ber-schema/flux_end)
Alias: flux_end

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:flux_end |
| native | lambdaber:flux_end |
| exact | ispyb:DataCollection.flux_end |




## LinkML Source

<details>
```yaml
name: flux_end
description: Photon flux at end of data collection in photons/second
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:DataCollection.flux_end
rank: 1000
alias: flux_end
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
unit:
  ucum_code: '{photons}/s'

```
</details>