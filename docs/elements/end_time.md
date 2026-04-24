

# Slot: end_time 


_Data collection end timestamp_





URI: [lambda:end_time](http://w3id.org/lambda/end_time)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:end_time |
| native | lambda:end_time |
| exact | ispyb:DataCollection.endTime |




## LinkML Source

<details>
```yaml
name: end_time
description: Data collection end timestamp
from_schema: http://w3id.org/lambda/
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