
# Class: Micrograph

Motion-corrected micrograph derived from movie

URI: [lambdaber:Micrograph](https://w3id.org/lambda-ber-schema/Micrograph)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D]^-[Micrograph&#124;dose:float%20%3F;origin_movie_id:string%20%3F;defocus_u:float%20%3F;defocus_v:float%20%3F;astigmatism_angle:float%20%3F;resolution_fit_limit:float%20%3F;ctf_quality_score:float%20%3F;pixel_size:string%20%3F;defocus:float%20%3F;astigmatism:float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[Image2D]^-[Micrograph&#124;dose:float%20%3F;origin_movie_id:string%20%3F;defocus_u:float%20%3F;defocus_v:float%20%3F;astigmatism_angle:float%20%3F;resolution_fit_limit:float%20%3F;ctf_quality_score:float%20%3F;pixel_size:string%20%3F;defocus:float%20%3F;astigmatism:float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;dimensions_x(i):integer%20%3F;dimensions_y(i):integer%20%3F;exposure_time(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)

## Referenced by Class


## Attributes


### Own

 * [➞dose](micrograph__dose.md)  <sub>0..1</sub>
     * Description: Total electron dose in e-/Angstrom^2
     * Range: [Float](types/Float.md)
 * [➞origin_movie_id](micrograph__origin_movie_id.md)  <sub>0..1</sub>
     * Description: Reference to original movie file
     * Range: [String](types/String.md)
 * [➞defocus_u](micrograph__defocus_u.md)  <sub>0..1</sub>
     * Description: Defocus U in micrometers
     * Range: [Float](types/Float.md)
 * [➞defocus_v](micrograph__defocus_v.md)  <sub>0..1</sub>
     * Description: Defocus V in micrometers
     * Range: [Float](types/Float.md)
 * [➞astigmatism_angle](micrograph__astigmatism_angle.md)  <sub>0..1</sub>
     * Description: Astigmatism angle in degrees
     * Range: [Float](types/Float.md)
 * [➞resolution_fit_limit](micrograph__resolution_fit_limit.md)  <sub>0..1</sub>
     * Description: Resolution fit limit in Angstroms
     * Range: [Float](types/Float.md)
 * [➞ctf_quality_score](micrograph__ctf_quality_score.md)  <sub>0..1</sub>
     * Description: CTF estimation quality score
     * Range: [Float](types/Float.md)
 * [Micrograph➞pixel_size](Micrograph_pixel_size.md)  <sub>0..1</sub>
     * Description: Final pixel size in Angstroms per pixel
     * Range: [String](types/String.md)
 * [Micrograph➞defocus](Micrograph_defocus.md)  <sub>0..1</sub>
     * Description: Measured defocus in micrometers
     * Range: [Float](types/Float.md)
 * [Micrograph➞astigmatism](Micrograph_astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism in Angstroms
     * Range: [Float](types/Float.md)

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
 * [➞dimensions_x](image__dimensions_x.md)  <sub>0..1</sub>
     * Description: Image width in pixels
     * Range: [Integer](types/Integer.md)
 * [➞dimensions_y](image__dimensions_y.md)  <sub>0..1</sub>
     * Description: Image height in pixels
     * Range: [Integer](types/Integer.md)
 * [➞exposure_time](image__exposure_time.md)  <sub>0..1</sub>
     * Description: Exposure time in seconds
     * Range: [Float](types/Float.md)
