

# Slot: spotsize 


_Electron beam spot size setting_





URI: [lambda:spotsize](http://w3id.org/lambda/spotsize)
Alias: spotsize

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
| self | lambda:spotsize |
| native | lambda:spotsize |
| exact | mmCIF:_em_imaging.detector_spot_size |




## LinkML Source

<details>
```yaml
name: spotsize
description: Electron beam spot size setting
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_imaging.detector_spot_size
rank: 1000
alias: spotsize
owner: CryoEMInstrument
domain_of:
- CryoEMInstrument
range: QuantityValue
inlined: true

```
</details>