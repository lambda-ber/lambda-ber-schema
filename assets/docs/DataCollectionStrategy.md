
# Class: DataCollectionStrategy

Strategy for data collection

URI: [lambdaber:DataCollectionStrategy](https://w3id.org/lambda-ber-schema/DataCollectionStrategy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20data_collection_strategy%200..1>[DataCollectionStrategy&#124;collection_mode:CollectionModeEnum%20%3F;total_frames:integer%20%3F;frame_rate:float%20%3F;total_dose:float%20%3F;dose_per_frame:float%20%3F;wavelength_a:float%20%3F;detector_mode:DetectorModeEnum%20%3F;pixel_size_calibrated:float%20%3F;detector_distance_mm:float%20%3F;beam_center_x_px:integer%20%3F;beam_center_y_px:integer%20%3F;beam_size_um:float%20%3F;flux_photons_per_s:float%20%3F;transmission_percent:float%20%3F;attenuator:string%20%3F;temperature_k:float%20%3F;oscillation_per_image_deg:float%20%3F;total_rotation_deg:float%20%3F;strategy_notes:string%20%3F;description(i):string%20%3F],[AttributeGroup]^-[DataCollectionStrategy],[ExperimentRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20data_collection_strategy%200..1>[DataCollectionStrategy&#124;collection_mode:CollectionModeEnum%20%3F;total_frames:integer%20%3F;frame_rate:float%20%3F;total_dose:float%20%3F;dose_per_frame:float%20%3F;wavelength_a:float%20%3F;detector_mode:DetectorModeEnum%20%3F;pixel_size_calibrated:float%20%3F;detector_distance_mm:float%20%3F;beam_center_x_px:integer%20%3F;beam_center_y_px:integer%20%3F;beam_size_um:float%20%3F;flux_photons_per_s:float%20%3F;transmission_percent:float%20%3F;attenuator:string%20%3F;temperature_k:float%20%3F;oscillation_per_image_deg:float%20%3F;total_rotation_deg:float%20%3F;strategy_notes:string%20%3F;description(i):string%20%3F],[AttributeGroup]^-[DataCollectionStrategy],[ExperimentRun],[AttributeGroup])

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
     * Range: [Integer](types/Integer.md)
 * [➞frame_rate](dataCollectionStrategy__frame_rate.md)  <sub>0..1</sub>
     * Description: Frames per second
     * Range: [Float](types/Float.md)
 * [➞total_dose](dataCollectionStrategy__total_dose.md)  <sub>0..1</sub>
     * Description: Total electron dose for cryo-EM
     * Range: [Float](types/Float.md)
 * [➞dose_per_frame](dataCollectionStrategy__dose_per_frame.md)  <sub>0..1</sub>
     * Description: Dose per frame
     * Range: [Float](types/Float.md)
 * [➞wavelength_a](dataCollectionStrategy__wavelength_a.md)  <sub>0..1</sub>
     * Description: X-ray wavelength in Angstroms
     * Range: [Float](types/Float.md)
 * [➞detector_mode](dataCollectionStrategy__detector_mode.md)  <sub>0..1</sub>
     * Description: Detector operating mode used during this experiment
     * Range: [DetectorModeEnum](DetectorModeEnum.md)
 * [➞pixel_size_calibrated](dataCollectionStrategy__pixel_size_calibrated.md)  <sub>0..1</sub>
     * Description: Calibrated pixel size for this experiment
     * Range: [Float](types/Float.md)
 * [➞detector_distance_mm](dataCollectionStrategy__detector_distance_mm.md)  <sub>0..1</sub>
     * Description: Detector distance in millimeters
     * Range: [Float](types/Float.md)
 * [➞beam_center_x_px](dataCollectionStrategy__beam_center_x_px.md)  <sub>0..1</sub>
     * Description: Beam center X coordinate in pixels
     * Range: [Integer](types/Integer.md)
 * [➞beam_center_y_px](dataCollectionStrategy__beam_center_y_px.md)  <sub>0..1</sub>
     * Description: Beam center Y coordinate in pixels
     * Range: [Integer](types/Integer.md)
 * [➞beam_size_um](dataCollectionStrategy__beam_size_um.md)  <sub>0..1</sub>
     * Description: Beam size in micrometers
     * Range: [Float](types/Float.md)
 * [➞flux_photons_per_s](dataCollectionStrategy__flux_photons_per_s.md)  <sub>0..1</sub>
     * Description: Photon flux in photons per second
     * Range: [Float](types/Float.md)
 * [➞transmission_percent](dataCollectionStrategy__transmission_percent.md)  <sub>0..1</sub>
     * Description: Beam transmission percentage
     * Range: [Float](types/Float.md)
 * [➞attenuator](dataCollectionStrategy__attenuator.md)  <sub>0..1</sub>
     * Description: Attenuator setting used
     * Range: [String](types/String.md)
 * [➞temperature_k](dataCollectionStrategy__temperature_k.md)  <sub>0..1</sub>
     * Description: Data collection temperature in Kelvin
     * Range: [Float](types/Float.md)
 * [➞oscillation_per_image_deg](dataCollectionStrategy__oscillation_per_image_deg.md)  <sub>0..1</sub>
     * Description: Oscillation angle per image in degrees
     * Range: [Float](types/Float.md)
 * [➞total_rotation_deg](dataCollectionStrategy__total_rotation_deg.md)  <sub>0..1</sub>
     * Description: Total rotation range in degrees
     * Range: [Float](types/Float.md)
 * [➞strategy_notes](dataCollectionStrategy__strategy_notes.md)  <sub>0..1</sub>
     * Description: Notes about data collection strategy
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
