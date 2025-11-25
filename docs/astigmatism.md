

# Slot: astigmatism 


_Astigmatism value in Angstroms_





URI: [lambdaber:astigmatism](https://w3id.org/lambda-ber-schema/astigmatism)
Alias: astigmatism

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  yes  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:astigmatism |
| native | lambdaber:astigmatism |




## LinkML Source

<details>
```yaml
name: astigmatism
description: Astigmatism value in Angstroms
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: astigmatism
owner: Image2D
domain_of:
- Image2D
range: float

```
</details>