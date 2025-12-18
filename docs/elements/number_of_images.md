

# Slot: number_of_images 


_Total number of diffraction images collected_





URI: [lambdaber:number_of_images](https://w3id.org/lambda-ber-schema/number_of_images)
Alias: number_of_images

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Integer](Integer.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:number_of_images |
| native | lambdaber:number_of_images |
| exact | nsls2:Number_of_images, imgCIF:_diffrn_scan.frames, ispyb:DataCollection.numberOfImages |




## LinkML Source

<details>
```yaml
name: number_of_images
description: Total number of diffraction images collected
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Number_of_images
- imgCIF:_diffrn_scan.frames
- ispyb:DataCollection.numberOfImages
rank: 1000
alias: number_of_images
owner: ExperimentRun
domain_of:
- ExperimentRun
range: integer

```
</details>