

# Slot: flux_photons_per_s 


_Photon flux, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:flux_photons_per_s](http://w3id.org/lambda/flux_photons_per_s)
Alias: flux_photons_per_s

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:flux_photons_per_s |
| native | lambda:flux_photons_per_s |
| exact | mmCIF:_diffrn_source.pdbx_flux |




## LinkML Source

<details>
```yaml
name: flux_photons_per_s
description: Photon flux, typically specified in photons per second. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_diffrn_source.pdbx_flux
rank: 1000
alias: flux_photons_per_s
owner: DataCollectionStrategy
domain_of:
- DataCollectionStrategy
range: QuantityValue
inlined: true

```
</details>