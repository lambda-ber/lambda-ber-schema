

# Slot: synchrotron_mode 


_Synchrotron storage ring fill mode_





URI: [lambda:synchrotron_mode](http://w3id.org/lambda/synchrotron_mode)
Alias: synchrotron_mode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [String](String.md)




## Comments

* e.g., 'Top-up', 'Decay', 'Hybrid'

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:synchrotron_mode |
| native | lambda:synchrotron_mode |
| exact | ispyb:DataCollection.synchrotronMode |




## LinkML Source

<details>
```yaml
name: synchrotron_mode
description: Synchrotron storage ring fill mode
comments:
- e.g., 'Top-up', 'Decay', 'Hybrid'
from_schema: http://w3id.org/lambda/
exact_mappings:
- ispyb:DataCollection.synchrotronMode
rank: 1000
alias: synchrotron_mode
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string

```
</details>