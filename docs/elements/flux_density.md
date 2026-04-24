

# Slot: flux_density 


_Photon flux density in photons/s/mm²_





URI: [lambda:flux_density](http://w3id.org/lambda/flux_density)
Alias: flux_density

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:flux_density |
| native | lambda:flux_density |
| exact | mmCIF:_diffrn_source.pdbx_flux |




## LinkML Source

<details>
```yaml
name: flux_density
description: Photon flux density in photons/s/mm²
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_diffrn_source.pdbx_flux
rank: 1000
alias: flux_density
owner: XRayInstrument
domain_of:
- XRayInstrument
range: QuantityValue
inlined: true

```
</details>