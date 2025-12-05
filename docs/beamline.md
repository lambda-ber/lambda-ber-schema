

# Slot: beamline 


_Beamline identifier (e.g., FMX, AMX, 12.3.1)_





URI: [lambdaber:beamline](https://w3id.org/lambda-ber-schema/beamline)
Alias: beamline

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:beamline |
| native | lambdaber:beamline |
| exact | nsls2:Beamline, mmCIF:_diffrn_source.pdbx_synchrotron_beamline |




## LinkML Source

<details>
```yaml
name: beamline
description: Beamline identifier (e.g., FMX, AMX, 12.3.1)
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Beamline
- mmCIF:_diffrn_source.pdbx_synchrotron_beamline
rank: 1000
alias: beamline
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string

```
</details>