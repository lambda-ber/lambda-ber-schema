

# Slot: source_type 



URI: [lambdaber:source_type](https://w3id.org/lambda-ber-schema/source_type)
Alias: source_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:source_type |
| native | lambdaber:source_type |




## LinkML Source

<details>
```yaml
name: source_type
alias: source_type
domain_of:
- XRayInstrument
- BeamlineInstrument
- XRFImage
range: string

```
</details>