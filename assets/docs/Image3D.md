
# Class: Image3D

A 3D volume or tomogram

URI: [lambdaber:Image3D](https://w3id.org/lambda-ber-schema/Image3D)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Image]^-[Image3D&#124;dimensions_z:integer%20%3F;voxel_size:float%20%3F;reconstruction_method:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image])](https://yuml.me/diagram/nofunky;dir:TB/class/[Image]^-[Image3D&#124;dimensions_z:integer%20%3F;voxel_size:float%20%3F;reconstruction_method:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image])

## Parents

 *  is_a: [Image](Image.md) - An image file from structural biology experiments

## Attributes


### Own

 * [➞dimensions_z](image3D__dimensions_z.md)  <sub>0..1</sub>
     * Description: Image depth in pixels/slices
     * Range: [Integer](types/Integer.md)
 * [➞voxel_size](image3D__voxel_size.md)  <sub>0..1</sub>
     * Description: Voxel size in Angstroms
     * Range: [Float](types/Float.md)
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
