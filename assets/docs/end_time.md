

# Slot: end_time 


_Data collection end timestamp_





URI: [lambdaber:end_time](https://w3id.org/lambda-ber-schema/end_time)
Alias: end_time

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
| self | lambdaber:end_time |
| native | lambdaber:end_time |
| exact | ispyb:DataCollection.endTime |




## LinkML Source

<details>
```yaml
name: end_time
description: Data collection end timestamp
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:DataCollection.endTime
rank: 1000
alias: end_time
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string

```
</details>