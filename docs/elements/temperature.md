

# Slot: temperature 



URI: [lambdaber:temperature](https://w3id.org/lambda-ber-schema/temperature)
Alias: temperature

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |  no  |
| [StorageConditions](StorageConditions.md) | Storage conditions for samples |  no  |
| [ExperimentalConditions](ExperimentalConditions.md) | Environmental and experimental conditions |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:temperature |
| native | lambdaber:temperature |




## LinkML Source

<details>
```yaml
name: temperature
alias: temperature
domain_of:
- StorageConditions
- ExperimentalConditions
- MeasurementConditions
range: string

```
</details>