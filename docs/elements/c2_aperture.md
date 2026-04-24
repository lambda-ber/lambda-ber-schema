

# Slot: c2_aperture 


_C2 aperture size in micrometers_





URI: [lambda:c2_aperture](http://w3id.org/lambda/c2_aperture)
Alias: c2_aperture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:c2_aperture |
| native | lambda:c2_aperture |
| exact | mmCIF:_em_imaging.c2_aperture_diameter |




## LinkML Source

<details>
```yaml
name: c2_aperture
description: C2 aperture size in micrometers
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_imaging.c2_aperture_diameter
rank: 1000
alias: c2_aperture
owner: CryoEMInstrument
domain_of:
- CryoEMInstrument
range: QuantityValue
inlined: true

```
</details>