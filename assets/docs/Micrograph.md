
# Class: Micrograph

Motion-corrected micrograph derived from movie

URI: [lambdaber:Micrograph](https://w3id.org/lambda-ber-schema/Micrograph)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<astigmatism%200..1-++[Micrograph&#124;origin_movie_id:string%20%3F;pixel_size:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<defocus%200..1-++[Micrograph],[QuantityValue]<ctf_quality_score%200..1-++[Micrograph],[QuantityValue]<resolution_fit_limit%200..1-++[Micrograph],[QuantityValue]<astigmatism_angle%200..1-++[Micrograph],[QuantityValue]<defocus_v%200..1-++[Micrograph],[QuantityValue]<defocus_u%200..1-++[Micrograph],[QuantityValue]<dose%200..1-++[Micrograph],[Image2D]^-[Micrograph],[Image2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<astigmatism%200..1-++[Micrograph&#124;origin_movie_id:string%20%3F;pixel_size:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<defocus%200..1-++[Micrograph],[QuantityValue]<ctf_quality_score%200..1-++[Micrograph],[QuantityValue]<resolution_fit_limit%200..1-++[Micrograph],[QuantityValue]<astigmatism_angle%200..1-++[Micrograph],[QuantityValue]<defocus_v%200..1-++[Micrograph],[QuantityValue]<defocus_u%200..1-++[Micrograph],[QuantityValue]<dose%200..1-++[Micrograph],[Image2D]^-[Micrograph],[Image2D])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)

## Referenced by Class


## Attributes


### Own

 * [➞dose](micrograph__dose.md)  <sub>0..1</sub>
     * Description: Total electron dose in e-/Angstrom^2
     * Range: [QuantityValue](QuantityValue.md)
 * [➞origin_movie_id](micrograph__origin_movie_id.md)  <sub>0..1</sub>
     * Description: Reference to original movie file
     * Range: [String](types/String.md)
 * [➞defocus_u](micrograph__defocus_u.md)  <sub>0..1</sub>
     * Description: Defocus U, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞defocus_v](micrograph__defocus_v.md)  <sub>0..1</sub>
     * Description: Defocus V, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞astigmatism_angle](micrograph__astigmatism_angle.md)  <sub>0..1</sub>
     * Description: Astigmatism angle, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞resolution_fit_limit](micrograph__resolution_fit_limit.md)  <sub>0..1</sub>
     * Description: Resolution fit limit, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ctf_quality_score](micrograph__ctf_quality_score.md)  <sub>0..1</sub>
     * Description: CTF estimation quality score
     * Range: [QuantityValue](QuantityValue.md)
 * [Micrograph➞pixel_size](Micrograph_pixel_size.md)  <sub>0..1</sub>
     * Description: Final pixel size in Angstroms per pixel
     * Range: [String](types/String.md)
 * [Micrograph➞defocus](Micrograph_defocus.md)  <sub>0..1</sub>
     * Description: Measured defocus in micrometers
     * Range: [QuantityValue](QuantityValue.md)
 * [Micrograph➞astigmatism](Micrograph_astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism in Angstroms
     * Range: [QuantityValue](QuantityValue.md)

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
     * Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞dimensions_y](image__dimensions_y.md)  <sub>0..1</sub>
     * Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞exposure_time](image__exposure_time.md)  <sub>0..1</sub>
     * Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
