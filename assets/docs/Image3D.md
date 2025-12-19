
# Class: Image3D

A 3D volume or tomogram

URI: [lambdaber:Image3D](https://w3id.org/lambda-ber-schema/Image3D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<voxel_size%200..1-++[Image3D&#124;reconstruction_method:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<dimensions_z%200..1-++[Image3D],[Image]^-[Image3D],[Image])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<voxel_size%200..1-++[Image3D&#124;reconstruction_method:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<dimensions_z%200..1-++[Image3D],[Image]^-[Image3D],[Image])

## Parents

 *  is_a: [Image](Image.md) - An image file from structural biology experiments

## Attributes


### Own

 * [➞dimensions_z](image3D__dimensions_z.md)  <sub>0..1</sub>
     * Description: Image depth, typically specified in pixels or slices. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞voxel_size](image3D__voxel_size.md)  <sub>0..1</sub>
     * Description: Voxel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞reconstruction_method](image3D__reconstruction_method.md)  <sub>0..1</sub>
     * Description: Method used for 3D reconstruction
     * Range: [String](types/String.md)

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
