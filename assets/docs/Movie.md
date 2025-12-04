
# Class: Movie

Raw cryo-EM movie with frame-by-frame metadata for motion correction

URI: [lambdaber:Movie](https://w3id.org/lambda-ber-schema/Movie)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D]^-[Movie&#124;frames:integer%20%3F;super_resolution:boolean%20%3F;pixel_size_unbinned:float%20%3F;timestamp:string%20%3F;stage_position_x:float%20%3F;stage_position_y:float%20%3F;stage_position_z:float%20%3F;nominal_defocus:float%20%3F;dose_per_frame:float%20%3F;beam_shift_x:float%20%3F;beam_shift_y:float%20%3F;ice_thickness_estimate:float%20%3F;grid_square_id:string%20%3F;hole_id:string%20%3F;acquisition_group:string%20%3F;defocus(i):float%20%3F;astigmatism(i):float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D]^-[Movie&#124;frames:integer%20%3F;super_resolution:boolean%20%3F;pixel_size_unbinned:float%20%3F;timestamp:string%20%3F;stage_position_x:float%20%3F;stage_position_y:float%20%3F;stage_position_z:float%20%3F;nominal_defocus:float%20%3F;dose_per_frame:float%20%3F;beam_shift_x:float%20%3F;beam_shift_y:float%20%3F;ice_thickness_estimate:float%20%3F;grid_square_id:string%20%3F;hole_id:string%20%3F;acquisition_group:string%20%3F;defocus(i):float%20%3F;astigmatism(i):float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;pixel_size(i):float%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)

## Attributes


### Own

 * [➞frames](movie__frames.md)  <sub>0..1</sub>
     * Description: Number of frames in the movie
     * Range: [Integer](types/Integer.md)
 * [➞super_resolution](movie__super_resolution.md)  <sub>0..1</sub>
     * Description: Whether super-resolution mode was used
     * Range: [Boolean](types/Boolean.md)
 * [➞pixel_size_unbinned](movie__pixel_size_unbinned.md)  <sub>0..1</sub>
     * Description: Unbinned pixel size in Angstroms per pixel
     * Range: [Float](types/Float.md)
 * [➞timestamp](movie__timestamp.md)  <sub>0..1</sub>
     * Description: Acquisition timestamp
     * Range: [String](types/String.md)
 * [➞stage_position_x](movie__stage_position_x.md)  <sub>0..1</sub>
     * Description: Stage X position in micrometers
     * Range: [Float](types/Float.md)
 * [➞stage_position_y](movie__stage_position_y.md)  <sub>0..1</sub>
     * Description: Stage Y position in micrometers
     * Range: [Float](types/Float.md)
 * [➞stage_position_z](movie__stage_position_z.md)  <sub>0..1</sub>
     * Description: Stage Z position in micrometers
     * Range: [Float](types/Float.md)
 * [➞nominal_defocus](movie__nominal_defocus.md)  <sub>0..1</sub>
     * Description: Nominal defocus value in micrometers
     * Range: [Float](types/Float.md)
 * [➞dose_per_frame](movie__dose_per_frame.md)  <sub>0..1</sub>
     * Description: Electron dose per frame in e-/Angstrom^2
     * Range: [Float](types/Float.md)
 * [➞beam_shift_x](movie__beam_shift_x.md)  <sub>0..1</sub>
     * Description: Beam shift X in microradians
     * Range: [Float](types/Float.md)
 * [➞beam_shift_y](movie__beam_shift_y.md)  <sub>0..1</sub>
     * Description: Beam shift Y in microradians
     * Range: [Float](types/Float.md)
 * [➞ice_thickness_estimate](movie__ice_thickness_estimate.md)  <sub>0..1</sub>
     * Description: Estimated ice thickness in nanometers
     * Range: [Float](types/Float.md)
 * [➞grid_square_id](movie__grid_square_id.md)  <sub>0..1</sub>
     * Description: Grid square identifier
     * Range: [String](types/String.md)
 * [➞hole_id](movie__hole_id.md)  <sub>0..1</sub>
     * Description: Hole identifier within grid square
     * Range: [String](types/String.md)
 * [➞acquisition_group](movie__acquisition_group.md)  <sub>0..1</sub>
     * Description: Acquisition group identifier (e.g., template or area)
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
