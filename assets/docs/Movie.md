
# Class: Movie

Raw cryo-EM movie with frame-by-frame metadata for motion correction

URI: [lambdaber:Movie](https://w3id.org/lambda-ber-schema/Movie)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<ice_thickness_estimate%200..1-++[Movie&#124;super_resolution:boolean%20%3F;timestamp:string%20%3F;grid_square_id:string%20%3F;hole_id:string%20%3F;acquisition_group:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<beam_shift_y%200..1-++[Movie],[QuantityValue]<beam_shift_x%200..1-++[Movie],[QuantityValue]<dose_per_frame%200..1-++[Movie],[QuantityValue]<nominal_defocus%200..1-++[Movie],[QuantityValue]<stage_position_z%200..1-++[Movie],[QuantityValue]<stage_position_y%200..1-++[Movie],[QuantityValue]<stage_position_x%200..1-++[Movie],[QuantityValue]<pixel_size_unbinned%200..1-++[Movie],[QuantityValue]<frames%200..1-++[Movie],[Image2D]^-[Movie],[Image2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<ice_thickness_estimate%200..1-++[Movie&#124;super_resolution:boolean%20%3F;timestamp:string%20%3F;grid_square_id:string%20%3F;hole_id:string%20%3F;acquisition_group:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<beam_shift_y%200..1-++[Movie],[QuantityValue]<beam_shift_x%200..1-++[Movie],[QuantityValue]<dose_per_frame%200..1-++[Movie],[QuantityValue]<nominal_defocus%200..1-++[Movie],[QuantityValue]<stage_position_z%200..1-++[Movie],[QuantityValue]<stage_position_y%200..1-++[Movie],[QuantityValue]<stage_position_x%200..1-++[Movie],[QuantityValue]<pixel_size_unbinned%200..1-++[Movie],[QuantityValue]<frames%200..1-++[Movie],[Image2D]^-[Movie],[Image2D])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)

## Attributes


### Own

 * [➞frames](movie__frames.md)  <sub>0..1</sub>
     * Description: Number of frames in the movie
     * Range: [QuantityValue](QuantityValue.md)
 * [➞super_resolution](movie__super_resolution.md)  <sub>0..1</sub>
     * Description: Whether super-resolution mode was used
     * Range: [Boolean](types/Boolean.md)
 * [➞pixel_size_unbinned](movie__pixel_size_unbinned.md)  <sub>0..1</sub>
     * Description: Unbinned pixel size, typically specified in Angstroms per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞timestamp](movie__timestamp.md)  <sub>0..1</sub>
     * Description: Acquisition timestamp
     * Range: [String](types/String.md)
 * [➞stage_position_x](movie__stage_position_x.md)  <sub>0..1</sub>
     * Description: Stage X position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞stage_position_y](movie__stage_position_y.md)  <sub>0..1</sub>
     * Description: Stage Y position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞stage_position_z](movie__stage_position_z.md)  <sub>0..1</sub>
     * Description: Stage Z position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞nominal_defocus](movie__nominal_defocus.md)  <sub>0..1</sub>
     * Description: Nominal defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞dose_per_frame](movie__dose_per_frame.md)  <sub>0..1</sub>
     * Description: Electron dose per frame in e-/Angstrom^2
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_shift_x](movie__beam_shift_x.md)  <sub>0..1</sub>
     * Description: Beam shift X in microradians
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_shift_y](movie__beam_shift_y.md)  <sub>0..1</sub>
     * Description: Beam shift Y in microradians
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ice_thickness_estimate](movie__ice_thickness_estimate.md)  <sub>0..1</sub>
     * Description: Estimated ice thickness, typically specified in nanometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
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
 * [➞defocus](image2D__defocus.md)  <sub>0..1</sub>
     * Description: Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞astigmatism](image2D__astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
