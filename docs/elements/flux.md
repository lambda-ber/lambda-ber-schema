

# Slot: flux 



URI: [lambda:flux](http://w3id.org/lambda/flux)
Alias: flux

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [SANSSource](SANSSource.md) | Beam source parameters for a SANS instrument |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:flux |
| native | lambda:flux |




## LinkML Source

<details>
```yaml
name: flux
alias: flux
domain_of:
- SANSSource
- ExperimentRun
- XRFImage
range: string

```
</details>