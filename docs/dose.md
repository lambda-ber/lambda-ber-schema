

# Slot: dose 


_Electron dose in e-/Å²_





URI: [lambdaber:dose](https://w3id.org/lambda-ber-schema/dose)
Alias: dose

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:dose |
| native | lambdaber:dose |




## LinkML Source

<details>
```yaml
name: dose
description: Electron dose in e-/Å²
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: dose
owner: Image
domain_of:
- Image
range: float

```
</details>