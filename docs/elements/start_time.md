

# Slot: start_time 


_Data collection start timestamp_





URI: [lambda:start_time](http://w3id.org/lambda/start_time)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:start_time |
| native | lambda:start_time |
| exact | ispyb:DataCollection.startTime |




## LinkML Source

<details>
```yaml
name: start_time
description: Data collection start timestamp
from_schema: http://w3id.org/lambda/
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