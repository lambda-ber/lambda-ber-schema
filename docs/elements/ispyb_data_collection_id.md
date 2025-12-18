

# Slot: ispyb_data_collection_id 


_ISPyB DataCollection.dataCollectionId for traceability_





URI: [lambdaber:ispyb_data_collection_id](https://w3id.org/lambda-ber-schema/ispyb_data_collection_id)
Alias: ispyb_data_collection_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Integer](Integer.md)




## Comments

* Use to link back to ISPyB records

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:ispyb_data_collection_id |
| native | lambdaber:ispyb_data_collection_id |
| exact | ispyb:DataCollection.dataCollectionId |




## LinkML Source

<details>
```yaml
name: ispyb_data_collection_id
description: ISPyB DataCollection.dataCollectionId for traceability
comments:
- Use to link back to ISPyB records
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- ispyb:DataCollection.dataCollectionId
rank: 1000
alias: ispyb_data_collection_id
owner: ExperimentRun
domain_of:
- ExperimentRun
range: integer

```
</details>