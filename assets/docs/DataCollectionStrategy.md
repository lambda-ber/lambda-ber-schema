
# Class: DataCollectionStrategy

Strategy for data collection

URI: [lambdaber:DataCollectionStrategy](https://w3id.org/lambda-ber-schema/DataCollectionStrategy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<total_rotation_deg%200..1-++[DataCollectionStrategy&#124;collection_mode:CollectionModeEnum%20%3F;detector_mode:DetectorModeEnum%20%3F;attenuator:string%20%3F;strategy_notes:string%20%3F;description(i):string%20%3F],[QuantityValue]<oscillation_per_image_deg%200..1-++[DataCollectionStrategy],[QuantityValue]<temperature_k%200..1-++[DataCollectionStrategy],[QuantityValue]<transmission_percent%200..1-++[DataCollectionStrategy],[QuantityValue]<flux_photons_per_s%200..1-++[DataCollectionStrategy],[QuantityValue]<beam_size_um%200..1-++[DataCollectionStrategy],[QuantityValue]<beam_center_y_px%200..1-++[DataCollectionStrategy],[QuantityValue]<beam_center_x_px%200..1-++[DataCollectionStrategy],[QuantityValue]<detector_distance_mm%200..1-++[DataCollectionStrategy],[QuantityValue]<pixel_size_calibrated%200..1-++[DataCollectionStrategy],[QuantityValue]<wavelength_a%200..1-++[DataCollectionStrategy],[QuantityValue]<dose_per_frame%200..1-++[DataCollectionStrategy],[QuantityValue]<total_dose%200..1-++[DataCollectionStrategy],[QuantityValue]<frame_rate%200..1-++[DataCollectionStrategy],[QuantityValue]<total_frames%200..1-++[DataCollectionStrategy],[ExperimentRun]++-%20data_collection_strategy%200..1>[DataCollectionStrategy],[AttributeGroup]^-[DataCollectionStrategy],[ExperimentRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<total_rotation_deg%200..1-++[DataCollectionStrategy&#124;collection_mode:CollectionModeEnum%20%3F;detector_mode:DetectorModeEnum%20%3F;attenuator:string%20%3F;strategy_notes:string%20%3F;description(i):string%20%3F],[QuantityValue]<oscillation_per_image_deg%200..1-++[DataCollectionStrategy],[QuantityValue]<temperature_k%200..1-++[DataCollectionStrategy],[QuantityValue]<transmission_percent%200..1-++[DataCollectionStrategy],[QuantityValue]<flux_photons_per_s%200..1-++[DataCollectionStrategy],[QuantityValue]<beam_size_um%200..1-++[DataCollectionStrategy],[QuantityValue]<beam_center_y_px%200..1-++[DataCollectionStrategy],[QuantityValue]<beam_center_x_px%200..1-++[DataCollectionStrategy],[QuantityValue]<detector_distance_mm%200..1-++[DataCollectionStrategy],[QuantityValue]<pixel_size_calibrated%200..1-++[DataCollectionStrategy],[QuantityValue]<wavelength_a%200..1-++[DataCollectionStrategy],[QuantityValue]<dose_per_frame%200..1-++[DataCollectionStrategy],[QuantityValue]<total_dose%200..1-++[DataCollectionStrategy],[QuantityValue]<frame_rate%200..1-++[DataCollectionStrategy],[QuantityValue]<total_frames%200..1-++[DataCollectionStrategy],[ExperimentRun]++-%20data_collection_strategy%200..1>[DataCollectionStrategy],[AttributeGroup]^-[DataCollectionStrategy],[ExperimentRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞data_collection_strategy](experimentRun__data_collection_strategy.md)*  <sub>0..1</sub>  **[DataCollectionStrategy](DataCollectionStrategy.md)**

## Attributes


### Own

 * [➞collection_mode](dataCollectionStrategy__collection_mode.md)  <sub>0..1</sub>
     * Description: Mode of data collection
     * Range: [CollectionModeEnum](CollectionModeEnum.md)
 * [➞total_frames](dataCollectionStrategy__total_frames.md)  <sub>0..1</sub>
     * Description: Total number of frames/images
     * Range: [QuantityValue](QuantityValue.md)
 * [➞frame_rate](dataCollectionStrategy__frame_rate.md)  <sub>0..1</sub>
     * Description: Frame rate, typically specified in frames per second. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞total_dose](dataCollectionStrategy__total_dose.md)  <sub>0..1</sub>
     * Description: Total electron dose for cryo-EM, typically specified in electrons per Angstrom squared (e⁻/Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞dose_per_frame](dataCollectionStrategy__dose_per_frame.md)  <sub>0..1</sub>
     * Description: Dose per frame, typically specified in electrons per Angstrom squared (e⁻/Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞wavelength_a](dataCollectionStrategy__wavelength_a.md)  <sub>0..1</sub>
     * Description: X-ray wavelength, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞detector_mode](dataCollectionStrategy__detector_mode.md)  <sub>0..1</sub>
     * Description: Detector operating mode used during this experiment
     * Range: [DetectorModeEnum](DetectorModeEnum.md)
 * [➞pixel_size_calibrated](dataCollectionStrategy__pixel_size_calibrated.md)  <sub>0..1</sub>
     * Description: Calibrated pixel size for this experiment, typically specified in Angstroms (Å) per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞detector_distance_mm](dataCollectionStrategy__detector_distance_mm.md)  <sub>0..1</sub>
     * Description: Detector distance, typically specified in millimeters. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_center_x_px](dataCollectionStrategy__beam_center_x_px.md)  <sub>0..1</sub>
     * Description: Beam center X coordinate in pixels
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_center_y_px](dataCollectionStrategy__beam_center_y_px.md)  <sub>0..1</sub>
     * Description: Beam center Y coordinate in pixels
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_size_um](dataCollectionStrategy__beam_size_um.md)  <sub>0..1</sub>
     * Description: Beam size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞flux_photons_per_s](dataCollectionStrategy__flux_photons_per_s.md)  <sub>0..1</sub>
     * Description: Photon flux, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞transmission_percent](dataCollectionStrategy__transmission_percent.md)  <sub>0..1</sub>
     * Description: Beam transmission, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞attenuator](dataCollectionStrategy__attenuator.md)  <sub>0..1</sub>
     * Description: Attenuator setting used
     * Range: [String](types/String.md)
 * [➞temperature_k](dataCollectionStrategy__temperature_k.md)  <sub>0..1</sub>
     * Description: Data collection temperature, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞oscillation_per_image_deg](dataCollectionStrategy__oscillation_per_image_deg.md)  <sub>0..1</sub>
     * Description: Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞total_rotation_deg](dataCollectionStrategy__total_rotation_deg.md)  <sub>0..1</sub>
     * Description: Total rotation range, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞strategy_notes](dataCollectionStrategy__strategy_notes.md)  <sub>0..1</sub>
     * Description: Notes about data collection strategy
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
