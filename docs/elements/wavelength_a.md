

# Slot: wavelength_a 


_X-ray wavelength, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:wavelength_a](http://w3id.org/lambda/wavelength_a)
Alias: wavelength_a

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* wavelength


## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:wavelength_a |
| native | lambda:wavelength_a |
| exact | mmCIF:_diffrn_radiation_wavelength.wavelength |




## LinkML Source

<details>
```yaml
name: wavelength_a
description: X-ray wavelength, typically specified in Angstroms. Data providers may
  specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
aliases:
- wavelength
exact_mappings:
- mmCIF:_diffrn_radiation_wavelength.wavelength
rank: 1000
alias: wavelength_a
owner: DataCollectionStrategy
domain_of:
- DataCollectionStrategy
range: QuantityValue
inlined: true

```
</details>