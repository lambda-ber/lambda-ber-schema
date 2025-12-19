

# Slot: dimensions_x 


_Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:dimensions_x](https://w3id.org/lambda-ber-schema/dimensions_x)
Alias: dimensions_x

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
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
| self | lambdaber:dimensions_x |
| native | lambdaber:dimensions_x |




## LinkML Source

<details>
```yaml
name: dimensions_x
description: Image width, typically specified in pixels. Data providers may specify
  alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: dimensions_x
owner: Image
domain_of:
- Image
range: QuantityValue
inlined: true

```
</details>