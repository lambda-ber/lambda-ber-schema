

# Slot: beamline 


_Beamline identifier (e.g., FMX, AMX, 12.3.1)_





URI: [lambda:beamline](http://w3id.org/lambda/beamline)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:beamline |
| native | lambda:beamline |
| exact | nsls2:Beamline, mmCIF:_diffrn_source.pdbx_synchrotron_beamline, ispyb:BLSession.beamLineName |




## LinkML Source

<details>
```yaml
name: beamline
description: Beamline identifier (e.g., FMX, AMX, 12.3.1)
from_schema: http://w3id.org/lambda/
exact_mappings:
- nsls2:Beamline
- mmCIF:_diffrn_source.pdbx_synchrotron_beamline
- ispyb:BLSession.beamLineName
rank: 1000
alias: beamline
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string

```
</details>