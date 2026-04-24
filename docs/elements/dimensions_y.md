

# Slot: dimensions_y 


_Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:dimensions_y](http://w3id.org/lambda/dimensions_y)
Alias: dimensions_y

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
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
| self | lambda:dimensions_y |
| native | lambda:dimensions_y |




## LinkML Source

<details>
```yaml
name: dimensions_y
description: Image height, typically specified in pixels. Data providers may specify
  alternative units by including the unit in the QuantityValue.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: dimensions_y
owner: Image
domain_of:
- Image
range: QuantityValue
inlined: true

```
</details>