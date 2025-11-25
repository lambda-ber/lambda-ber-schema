

# Slot: detector_technology 



URI: [lambdaber:detector_technology](https://w3id.org/lambda-ber-schema/detector_technology)
Alias: detector_technology

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
| self | lambdaber:detector_technology |
| native | lambdaber:detector_technology |




## LinkML Source

<details>
```yaml
name: detector_technology
alias: detector_technology
domain_of:
- CryoEMInstrument
- XRayInstrument
- XRFImage
range: string

```
</details>