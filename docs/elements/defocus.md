

# Slot: defocus 


_Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:defocus](http://w3id.org/lambda/defocus)
Alias: defocus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:defocus |
| native | lambda:defocus |




## LinkML Source

<details>
```yaml
name: defocus
description: Defocus value, typically specified in micrometers. Data providers may
  specify alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: defocus
owner: Image2D
domain_of:
- Image2D
range: QuantityValue
inlined: true

```
</details>