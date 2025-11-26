
# Class: OpticalImage

Visible light optical microscopy or photography image

URI: [lambdaber:OpticalImage](https://w3id.org/lambda-ber-schema/OpticalImage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D]^-[OpticalImage&#124;illumination_type:IlluminationTypeEnum%20%3F;magnification:float%20%3F;numerical_aperture:float%20%3F;color_channels:string%20*;white_balance:string%20%3F;contrast_method:string%20%3F;defocus(i):float%20%3F;astigmatism(i):float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D]^-[OpticalImage&#124;illumination_type:IlluminationTypeEnum%20%3F;magnification:float%20%3F;numerical_aperture:float%20%3F;color_channels:string%20*;white_balance:string%20%3F;contrast_method:string%20%3F;defocus(i):float%20%3F;astigmatism(i):float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)

## Attributes


### Own

 * [➞illumination_type](opticalImage__illumination_type.md)  <sub>0..1</sub>
     * Description: Type of illumination (brightfield, darkfield, phase contrast, DIC)
     * Range: [IlluminationTypeEnum](IlluminationTypeEnum.md)
 * [➞magnification](opticalImage__magnification.md)  <sub>0..1</sub>
     * Description: Optical magnification factor
     * Range: [Float](types/Float.md)
 * [➞numerical_aperture](opticalImage__numerical_aperture.md)  <sub>0..1</sub>
     * Description: Numerical aperture of the objective lens
     * Range: [Float](types/Float.md)
 * [➞color_channels](opticalImage__color_channels.md)  <sub>0..\*</sub>
     * Description: Color channels present (e.g., RGB, grayscale)
     * Range: [String](types/String.md)
 * [➞white_balance](opticalImage__white_balance.md)  <sub>0..1</sub>
     * Description: White balance settings
     * Range: [String](types/String.md)
 * [➞contrast_method](opticalImage__contrast_method.md)  <sub>0..1</sub>
     * Description: Contrast enhancement method used
     * Range: [String](types/String.md)

### Inherited from Image2D:

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
 * [➞defocus](image2D__defocus.md)  <sub>0..1</sub>
     * Description: Defocus value in micrometers
     * Range: [Float](types/Float.md)
 * [➞astigmatism](image2D__astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism value in Angstroms
     * Range: [Float](types/Float.md)
