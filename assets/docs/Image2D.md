
# Class: Image2D

A 2D image (micrograph, diffraction pattern)

URI: [lambdaber:Image2D](https://w3id.org/lambda-ber-schema/Image2D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[XRFImage],[QuantityValue],[OpticalImage],[Movie],[Micrograph],[QuantityValue]<astigmatism%200..1-++[Image2D&#124;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<defocus%200..1-++[Image2D],[Image2D]^-[XRFImage],[Image2D]^-[OpticalImage],[Image2D]^-[Movie],[Image2D]^-[Micrograph],[Image2D]^-[FluorescenceImage],[Image]^-[Image2D],[Image],[FluorescenceImage])](https://yuml.me/diagram/nofunky;dir:TB/class/[XRFImage],[QuantityValue],[OpticalImage],[Movie],[Micrograph],[QuantityValue]<astigmatism%200..1-++[Image2D&#124;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<defocus%200..1-++[Image2D],[Image2D]^-[XRFImage],[Image2D]^-[OpticalImage],[Image2D]^-[Movie],[Image2D]^-[Micrograph],[Image2D]^-[FluorescenceImage],[Image]^-[Image2D],[Image],[FluorescenceImage])

## Parents

 *  is_a: [Image](Image.md) - An image file from structural biology experiments

## Children

 * [FluorescenceImage](FluorescenceImage.md) - Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
 * [Micrograph](Micrograph.md) - Motion-corrected micrograph derived from movie
 * [Movie](Movie.md) - Raw cryo-EM movie with frame-by-frame metadata for motion correction
 * [OpticalImage](OpticalImage.md) - Visible light optical microscopy or photography image
 * [XRFImage](XRFImage.md) - X-ray fluorescence (XRF) image showing elemental distribution

## Referenced by Class


## Attributes


### Own

 * [➞defocus](image2D__defocus.md)  <sub>0..1</sub>
     * Description: Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞astigmatism](image2D__astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from Image:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
 * [➞file_name](image__file_name.md)  <sub>1..1</sub>
     * Description: Image file name
     * Range: [String](types/String.md)
 * [➞acquisition_date](image__acquisition_date.md)  <sub>0..1</sub>
     * Description: Date image was acquired
     * Range: [String](types/String.md)
 * [➞pixel_size](image__pixel_size.md)  <sub>0..1</sub>
     * Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞dimensions_x](image__dimensions_x.md)  <sub>0..1</sub>
     * Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞dimensions_y](image__dimensions_y.md)  <sub>0..1</sub>
     * Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞exposure_time](image__exposure_time.md)  <sub>0..1</sub>
     * Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞dose](image__dose.md)  <sub>0..1</sub>
     * Description: Electron dose in e-/Å²
     * Range: [QuantityValue](QuantityValue.md)
