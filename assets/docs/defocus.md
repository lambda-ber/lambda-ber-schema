

# Slot: defocus 


_Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:defocus](https://w3id.org/lambda-ber-schema/defocus)
Alias: defocus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  yes  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:defocus |
| native | lambdaber:defocus |




## LinkML Source

<details>
```yaml
name: defocus
description: Defocus value, typically specified in micrometers. Data providers may
  specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: defocus
owner: Image2D
domain_of:
- Image2D
range: QuantityValue
inlined: true

```
</details>