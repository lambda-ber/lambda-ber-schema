

# Slot: source_type 



URI: [lambda:source_type](http://w3id.org/lambda/source_type)
Alias: source_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [SANSSource](SANSSource.md) | Beam source parameters for a SANS instrument |  no  |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:source_type |
| native | lambda:source_type |




## LinkML Source

<details>
```yaml
name: source_type
alias: source_type
domain_of:
- XRayInstrument
- SANSSource
- BeamlineInstrument
- XRFImage
range: string

```
</details>