
# Class: XRFImage

X-ray fluorescence (XRF) image showing elemental distribution

URI: [lambdaber:XRFImage](https://w3id.org/lambda-ber-schema/XRFImage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<flux%200..1-++[XRFImage&#124;beam_energy:float%20%3F;beam_size:float%20%3F;dwell_time:float%20%3F;elements_measured:string%20*;source_type:XRaySourceTypeEnum%20%3F;detector_technology:DetectorTechnologyEnum%20%3F;detector_model:string%20%3F;calibration_standard:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D]^-[XRFImage],[QuantityValue],[Image2D])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<flux%200..1-++[XRFImage&#124;beam_energy:float%20%3F;beam_size:float%20%3F;dwell_time:float%20%3F;elements_measured:string%20*;source_type:XRaySourceTypeEnum%20%3F;detector_technology:DetectorTechnologyEnum%20%3F;detector_model:string%20%3F;calibration_standard:string%20%3F;file_name(i):string;acquisition_date(i):string%20%3F;dose(i):float%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Image2D]^-[XRFImage],[QuantityValue],[Image2D])

## Parents

 *  is_a: [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)

## Attributes


### Own

 * [➞beam_energy](xRFImage__beam_energy.md)  <sub>0..1</sub>
     * Description: X-ray beam energy in keV
     * Range: [Float](types/Float.md)
 * [➞beam_size](xRFImage__beam_size.md)  <sub>0..1</sub>
     * Description: X-ray beam size in micrometers
     * Range: [Float](types/Float.md)
 * [➞dwell_time](xRFImage__dwell_time.md)  <sub>0..1</sub>
     * Description: Dwell time per pixel in milliseconds
     * Range: [Float](types/Float.md)
 * [➞elements_measured](xRFImage__elements_measured.md)  <sub>0..\*</sub>
     * Description: Elements detected and measured
     * Range: [String](types/String.md)
 * [➞source_type](xRFImage__source_type.md)  <sub>0..1</sub>
     * Description: X-ray source type (synchrotron or lab-source)
     * Range: [XRaySourceTypeEnum](XRaySourceTypeEnum.md)
 * [➞detector_technology](xRFImage__detector_technology.md)  <sub>0..1</sub>
     * Description: Type of X-ray detector technology used
     * Range: [DetectorTechnologyEnum](DetectorTechnologyEnum.md)
 * [➞detector_model](xRFImage__detector_model.md)  <sub>0..1</sub>
     * Description: Specific detector model used for XRF measurement
     * Range: [String](types/String.md)
 * [➞flux](xRFImage__flux.md)  <sub>0..1</sub>
     * Description: Photon flux, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞calibration_standard](xRFImage__calibration_standard.md)  <sub>0..1</sub>
     * Description: Reference standard used for calibration
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
     * Range: [Float](types/Float.md)
 * [➞defocus](image2D__defocus.md)  <sub>0..1</sub>
     * Description: Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞astigmatism](image2D__astigmatism.md)  <sub>0..1</sub>
     * Description: Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
