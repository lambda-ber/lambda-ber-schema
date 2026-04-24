

# Slot: flux_end 


_Photon flux at end of data collection, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:flux_end](http://w3id.org/lambda/flux_end)
Alias: flux_end

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:flux_end |
| native | lambda:flux_end |
| exact | ispyb:DataCollection.flux_end |




## LinkML Source

<details>
```yaml
name: flux_end
description: Photon flux at end of data collection, typically specified in photons
  per second. Data providers may specify alternative units by including the unit in
  the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- ispyb:DataCollection.flux_end
rank: 1000
alias: flux_end
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>