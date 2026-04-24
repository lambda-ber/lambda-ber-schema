

# Slot: detector_model 



URI: [lambda:detector_model](http://w3id.org/lambda/detector_model)
Alias: detector_model

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:detector_model |
| native | lambda:detector_model |




## LinkML Source

<details>
```yaml
name: detector_model
alias: detector_model
domain_of:
- CryoEMInstrument
- XRayInstrument
- XRFImage
range: string

```
</details>