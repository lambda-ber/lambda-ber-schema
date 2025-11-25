

# Slot: wavelength 


_X-ray wavelength_





URI: [lambdaber:wavelength](https://w3id.org/lambda-ber-schema/wavelength)
Alias: wavelength

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:wavelength |
| native | lambdaber:wavelength |
| exact | nsls2:Wavelength, imgCIF:_diffrn_radiation_wavelength.wavelength, mmCIF:_diffrn_radiation_wavelength.wavelength |




## LinkML Source

<details>
```yaml
name: wavelength
description: X-ray wavelength
from_schema: https://w3id.org/lambda-ber-schema/
exact_mappings:
- nsls2:Wavelength
- imgCIF:_diffrn_radiation_wavelength.wavelength
- mmCIF:_diffrn_radiation_wavelength.wavelength
rank: 1000
alias: wavelength
owner: ExperimentRun
domain_of:
- ExperimentRun
range: float
unit:
  ucum_code: Ao

```
</details>