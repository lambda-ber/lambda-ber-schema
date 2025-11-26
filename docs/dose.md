

# Slot: dose 



URI: [lambdaber:dose](https://w3id.org/lambda-ber-schema/dose)
Alias: dose

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:dose |
| native | lambdaber:dose |




## LinkML Source

<details>
```yaml
name: dose
alias: dose
domain_of:
- Image
- Micrograph
range: string

```
</details>