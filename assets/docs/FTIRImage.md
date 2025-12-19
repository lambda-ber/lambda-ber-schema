
# Class: FTIRImage

Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy

URI: [lambdaber:FTIRImage](https://w3id.org/lambda-ber-schema/FTIRImage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Image],[QuantityValue]<number_of_scans%200..1-++[FTIRImage&#124;apodization_function:string%20%3F;molecular_signatures:string%20*;background_correction:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<spectral_resolution%200..1-++[FTIRImage],[QuantityValue]<wavenumber_max%200..1-++[FTIRImage],[QuantityValue]<wavenumber_min%200..1-++[FTIRImage],[Image]^-[FTIRImage])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Image],[QuantityValue]<number_of_scans%200..1-++[FTIRImage&#124;apodization_function:string%20%3F;molecular_signatures:string%20*;background_correction:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<spectral_resolution%200..1-++[FTIRImage],[QuantityValue]<wavenumber_max%200..1-++[FTIRImage],[QuantityValue]<wavenumber_min%200..1-++[FTIRImage],[Image]^-[FTIRImage])

## Parents

 *  is_a: [Image](Image.md) - An image file from structural biology experiments

## Attributes


### Own

 * [➞wavenumber_min](fTIRImage__wavenumber_min.md)  <sub>0..1</sub>
     * Description: Minimum wavenumber, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞wavenumber_max](fTIRImage__wavenumber_max.md)  <sub>0..1</sub>
     * Description: Maximum wavenumber, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞spectral_resolution](fTIRImage__spectral_resolution.md)  <sub>0..1</sub>
     * Description: Spectral resolution, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞number_of_scans](fTIRImage__number_of_scans.md)  <sub>0..1</sub>
     * Description: Number of scans averaged for the spectrum
     * Range: [QuantityValue](QuantityValue.md)
 * [➞apodization_function](fTIRImage__apodization_function.md)  <sub>0..1</sub>
     * Description: Mathematical function used for apodization
     * Range: [String](types/String.md)
 * [➞molecular_signatures](fTIRImage__molecular_signatures.md)  <sub>0..\*</sub>
     * Description: Identified molecular signatures or peaks
     * Range: [String](types/String.md)
 * [➞background_correction](fTIRImage__background_correction.md)  <sub>0..1</sub>
     * Description: Method used for background correction
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
