
# Class: FluorescenceImage

Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling

URI: [lambdaber:FluorescenceImage](https://w3id.org/lambda-ber-schema/FluorescenceImage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Image2D],[Image2D]^-[FluorescenceImage&#124;excitation_wavelength:float%20%3F;emission_wavelength:float%20%3F;excitation_filter:string%20%3F;emission_filter:string%20%3F;fluorophore:string%20%3F;channel_name:string%20%3F;laser_power:float%20%3F;pinhole_size:float%20%3F;quantum_yield:float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Image2D],[Image2D]^-[FluorescenceImage&#124;excitation_wavelength:float%20%3F;emission_wavelength:float%20%3F;excitation_filter:string%20%3F;emission_filter:string%20%3F;fluorophore:string%20%3F;channel_name:string%20%3F;laser_power:float%20%3F;pinhole_size:float%20%3F;quantum_yield:float%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)

## Attributes


### Own

 * [➞excitation_wavelength](fluorescenceImage__excitation_wavelength.md)  <sub>0..1</sub>
     * Description: Excitation wavelength in nanometers
     * Range: [Float](types/Float.md)
 * [➞emission_wavelength](fluorescenceImage__emission_wavelength.md)  <sub>0..1</sub>
     * Description: Emission wavelength in nanometers
     * Range: [Float](types/Float.md)
 * [➞excitation_filter](fluorescenceImage__excitation_filter.md)  <sub>0..1</sub>
     * Description: Specifications of the excitation filter
     * Range: [String](types/String.md)
 * [➞emission_filter](fluorescenceImage__emission_filter.md)  <sub>0..1</sub>
     * Description: Specifications of the emission filter
     * Range: [String](types/String.md)
 * [➞fluorophore](fluorescenceImage__fluorophore.md)  <sub>0..1</sub>
     * Description: Name or type of fluorophore used
     * Range: [String](types/String.md)
 * [➞channel_name](fluorescenceImage__channel_name.md)  <sub>0..1</sub>
     * Description: Name of the fluorescence channel (e.g., DAPI, GFP, RFP)
     * Range: [String](types/String.md)
 * [➞laser_power](fluorescenceImage__laser_power.md)  <sub>0..1</sub>
     * Description: Laser power in milliwatts or percentage
     * Range: [Float](types/Float.md)
 * [➞pinhole_size](fluorescenceImage__pinhole_size.md)  <sub>0..1</sub>
     * Description: Pinhole size in Airy units for confocal microscopy
     * Range: [Float](types/Float.md)
 * [➞quantum_yield](fluorescenceImage__quantum_yield.md)  <sub>0..1</sub>
     * Description: Quantum yield of the fluorophore
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
     * Range: [Float](types/Float.md)
 * [➞defocus](image2D__defocus.md)  <sub>0..1</sub>
     * Description: Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞astigmatism](image2D__astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
