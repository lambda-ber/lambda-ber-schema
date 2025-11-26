
# Class: Image

An image file from structural biology experiments

URI: [lambdaber:Image](https://w3id.org/lambda-ber-schema/Image)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[Image3D],[Image2D],[Study]++-%20images%200..*>[Image&#124;file_name:string;acquisition_date:string%20%3F;pixel_size:float%20%3F;dimensions_x:integer%20%3F;dimensions_y:integer%20%3F;exposure_time:float%20%3F;dose:float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image]^-[Image3D],[Image]^-[Image2D],[Image]^-[FTIRImage],[NamedThing]^-[Image],[Study],[FTIRImage])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[Image3D],[Image2D],[Study]++-%20images%200..*>[Image&#124;file_name:string;acquisition_date:string%20%3F;pixel_size:float%20%3F;dimensions_x:integer%20%3F;dimensions_y:integer%20%3F;exposure_time:float%20%3F;dose:float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image]^-[Image3D],[Image]^-[Image2D],[Image]^-[FTIRImage],[NamedThing]^-[Image],[Study],[FTIRImage])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Children

 * [FTIRImage](FTIRImage.md) - Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy
 * [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)
 * [Image3D](Image3D.md) - A 3D volume or tomogram

## Referenced by Class

 *  **None** *[➞images](study__images.md)*  <sub>0..\*</sub>  **[Image](Image.md)**

## Attributes


### Own

 * [➞file_name](image__file_name.md)  <sub>1..1</sub>
     * Description: Image file name
     * Range: [String](types/String.md)
 * [➞acquisition_date](image__acquisition_date.md)  <sub>0..1</sub>
     * Description: Date image was acquired
     * Range: [String](types/String.md)
 * [➞pixel_size](image__pixel_size.md)  <sub>0..1</sub>
     * Description: Pixel size in Angstroms
     * Range: [Float](types/Float.md)
 * [➞dimensions_x](image__dimensions_x.md)  <sub>0..1</sub>
     * Description: Image width in pixels
     * Range: [Integer](types/Integer.md)
 * [➞dimensions_y](image__dimensions_y.md)  <sub>0..1</sub>
     * Description: Image height in pixels
     * Range: [Integer](types/Integer.md)
 * [➞exposure_time](image__exposure_time.md)  <sub>0..1</sub>
     * Description: Exposure time in seconds
     * Range: [Float](types/Float.md)
 * [➞dose](image__dose.md)  <sub>0..1</sub>
     * Description: Electron dose in e-/Å²
     * Range: [Float](types/Float.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
