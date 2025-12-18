

# Slot: start_time 


_Data collection start timestamp_





URI: [lambdaber:start_time](https://w3id.org/lambda-ber-schema/start_time)
Alias: start_time

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
| self | lambdaber:start_time |
| native | lambdaber:start_time |
| exact | ispyb:DataCollection.startTime |




## LinkML Source

<details>
```yaml
name: start_time
description: Data collection start timestamp
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:DataCollection.startTime
rank: 1000
alias: start_time
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string

```
</details>