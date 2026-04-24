

# Slot: imaging_mode 


_Imaging mode for electron microscopy_





URI: [lambda:imaging_mode](http://w3id.org/lambda/imaging_mode)
Alias: imaging_mode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [ImagingModeEnum](ImagingModeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:imaging_mode |
| native | lambda:imaging_mode |
| exact | mmCIF:_em_imaging.mode |




## LinkML Source

<details>
```yaml
name: imaging_mode
description: Imaging mode for electron microscopy
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_imaging.mode
rank: 1000
alias: imaging_mode
owner: CryoEMInstrument
domain_of:
- CryoEMInstrument
range: ImagingModeEnum

```
</details>