
# Class: ExperimentRun

An experimental data collection session

URI: [lambdaber:ExperimentRun](https://w3id.org/lambda-ber-schema/ExperimentRun)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QualityMetrics],[NamedThing],[Instrument],[ExperimentalConditions],[QualityMetrics]<quality_metrics%200..1-++[ExperimentRun&#124;experiment_code:string;sample_id:string;experiment_date:string%20%3F;operator_id:string%20%3F;technique:TechniqueEnum;experimental_method:ExperimentalMethodEnum%20%3F;raw_data_location:string%20%3F;processing_status:ProcessingStatusEnum%20%3F;magnification:integer%20%3F;calibrated_pixel_size:float%20%3F;camera_binning:integer%20%3F;exposure_time_per_frame:float%20%3F;frames_per_movie:integer%20%3F;total_exposure_time:float%20%3F;total_dose:float%20%3F;dose_rate:float%20%3F;defocus_target:float%20%3F;defocus_range_min:float%20%3F;defocus_range_max:float%20%3F;defocus_range_increment:float%20%3F;astigmatism_target:float%20%3F;coma:float%20%3F;stage_tilt:float%20%3F;autoloader_slot:string%20%3F;shots_per_hole:integer%20%3F;holes_per_group:integer%20%3F;acquisition_software:string%20%3F;acquisition_software_version:string%20%3F;wavelength:float%20%3F;oscillation_angle:float%20%3F;start_angle:float%20%3F;number_of_images:integer%20%3F;beam_center_x:float%20%3F;beam_center_y:float%20%3F;detector_distance:float%20%3F;pixel_size_x:float%20%3F;pixel_size_y:float%20%3F;total_rotation:float%20%3F;beamline:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[DataCollectionStrategy]<data_collection_strategy%200..1-++[ExperimentRun],[ExperimentalConditions]<experimental_conditions%200..1-++[ExperimentRun],[Instrument]<instrument_id%201..1-%20[ExperimentRun],[Study]++-%20instrument_runs%200..*>[ExperimentRun],[NamedThing]^-[ExperimentRun],[Study],[DataCollectionStrategy])](https://yuml.me/diagram/nofunky;dir:TB/class/[QualityMetrics],[NamedThing],[Instrument],[ExperimentalConditions],[QualityMetrics]<quality_metrics%200..1-++[ExperimentRun&#124;experiment_code:string;sample_id:string;experiment_date:string%20%3F;operator_id:string%20%3F;technique:TechniqueEnum;experimental_method:ExperimentalMethodEnum%20%3F;raw_data_location:string%20%3F;processing_status:ProcessingStatusEnum%20%3F;magnification:integer%20%3F;calibrated_pixel_size:float%20%3F;camera_binning:integer%20%3F;exposure_time_per_frame:float%20%3F;frames_per_movie:integer%20%3F;total_exposure_time:float%20%3F;total_dose:float%20%3F;dose_rate:float%20%3F;defocus_target:float%20%3F;defocus_range_min:float%20%3F;defocus_range_max:float%20%3F;defocus_range_increment:float%20%3F;astigmatism_target:float%20%3F;coma:float%20%3F;stage_tilt:float%20%3F;autoloader_slot:string%20%3F;shots_per_hole:integer%20%3F;holes_per_group:integer%20%3F;acquisition_software:string%20%3F;acquisition_software_version:string%20%3F;wavelength:float%20%3F;oscillation_angle:float%20%3F;start_angle:float%20%3F;number_of_images:integer%20%3F;beam_center_x:float%20%3F;beam_center_y:float%20%3F;detector_distance:float%20%3F;pixel_size_x:float%20%3F;pixel_size_y:float%20%3F;total_rotation:float%20%3F;beamline:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[DataCollectionStrategy]<data_collection_strategy%200..1-++[ExperimentRun],[ExperimentalConditions]<experimental_conditions%200..1-++[ExperimentRun],[Instrument]<instrument_id%201..1-%20[ExperimentRun],[Study]++-%20instrument_runs%200..*>[ExperimentRun],[NamedThing]^-[ExperimentRun],[Study],[DataCollectionStrategy])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞instrument_runs](study__instrument_runs.md)*  <sub>0..\*</sub>  **[ExperimentRun](ExperimentRun.md)**

## Attributes


### Own

 * [➞experiment_code](experimentRun__experiment_code.md)  <sub>1..1</sub>
     * Description: Human-friendly laboratory or facility identifier for the experiment (e.g., 'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and cross-referencing within laboratory systems.
     * Range: [String](types/String.md)
 * [➞sample_id](experimentRun__sample_id.md)  <sub>1..1</sub>
     * Description: Reference to the sample being analyzed
     * Range: [String](types/String.md)
 * [➞instrument_id](experimentRun__instrument_id.md)  <sub>1..1</sub>
     * Description: Reference to the instrument used
     * Range: [Instrument](Instrument.md)
 * [➞experiment_date](experimentRun__experiment_date.md)  <sub>0..1</sub>
     * Description: Date of the experiment
     * Range: [String](types/String.md)
 * [➞operator_id](experimentRun__operator_id.md)  <sub>0..1</sub>
     * Description: Identifier or name of the person who performed the experiment data collection (e.g., 'jsmith', 'John Smith', or personnel ID)
     * Range: [String](types/String.md)
 * [➞technique](experimentRun__technique.md)  <sub>1..1</sub>
     * Description: Technique used for data collection
     * Range: [TechniqueEnum](TechniqueEnum.md)
 * [➞experimental_method](experimentRun__experimental_method.md)  <sub>0..1</sub>
     * Description: Specific experimental method for structure determination (particularly for diffraction techniques)
     * Range: [ExperimentalMethodEnum](ExperimentalMethodEnum.md)
 * [➞experimental_conditions](experimentRun__experimental_conditions.md)  <sub>0..1</sub>
     * Description: Environmental and experimental conditions
     * Range: [ExperimentalConditions](ExperimentalConditions.md)
 * [➞data_collection_strategy](experimentRun__data_collection_strategy.md)  <sub>0..1</sub>
     * Description: Strategy for data collection
     * Range: [DataCollectionStrategy](DataCollectionStrategy.md)
 * [➞quality_metrics](experimentRun__quality_metrics.md)  <sub>0..1</sub>
     * Description: Quality metrics for the experiment
     * Range: [QualityMetrics](QualityMetrics.md)
 * [➞raw_data_location](experimentRun__raw_data_location.md)  <sub>0..1</sub>
     * Description: Location of raw data files
     * Range: [String](types/String.md)
 * [➞processing_status](experimentRun__processing_status.md)  <sub>0..1</sub>
     * Description: Current processing status
     * Range: [ProcessingStatusEnum](ProcessingStatusEnum.md)
 * [➞magnification](experimentRun__magnification.md)  <sub>0..1</sub>
     * Description: Magnification used during data collection
     * Range: [Integer](types/Integer.md)
 * [➞calibrated_pixel_size](experimentRun__calibrated_pixel_size.md)  <sub>0..1</sub>
     * Description: Calibrated pixel size in Angstroms per pixel
     * Range: [Float](types/Float.md)
 * [➞camera_binning](experimentRun__camera_binning.md)  <sub>0..1</sub>
     * Description: Camera binning factor
     * Range: [Integer](types/Integer.md)
 * [➞exposure_time_per_frame](experimentRun__exposure_time_per_frame.md)  <sub>0..1</sub>
     * Description: Exposure time per frame in milliseconds
     * Range: [Float](types/Float.md)
 * [➞frames_per_movie](experimentRun__frames_per_movie.md)  <sub>0..1</sub>
     * Description: Number of frames per movie
     * Range: [Integer](types/Integer.md)
 * [➞total_exposure_time](experimentRun__total_exposure_time.md)  <sub>0..1</sub>
     * Description: Total exposure time in milliseconds
     * Range: [Float](types/Float.md)
 * [➞total_dose](experimentRun__total_dose.md)  <sub>0..1</sub>
     * Description: Total electron dose in e-/Angstrom^2
     * Range: [Float](types/Float.md)
 * [➞dose_rate](experimentRun__dose_rate.md)  <sub>0..1</sub>
     * Description: Dose rate in e-/pixel/s or e-/Angstrom^2/s
     * Range: [Float](types/Float.md)
 * [➞defocus_target](experimentRun__defocus_target.md)  <sub>0..1</sub>
     * Description: Target defocus value in micrometers
     * Range: [Float](types/Float.md)
 * [➞defocus_range_min](experimentRun__defocus_range_min.md)  <sub>0..1</sub>
     * Description: Minimum defocus range in micrometers
     * Range: [Float](types/Float.md)
 * [➞defocus_range_max](experimentRun__defocus_range_max.md)  <sub>0..1</sub>
     * Description: Maximum defocus range in micrometers
     * Range: [Float](types/Float.md)
 * [➞defocus_range_increment](experimentRun__defocus_range_increment.md)  <sub>0..1</sub>
     * Description: Defocus range increment in micrometers
     * Range: [Float](types/Float.md)
 * [➞astigmatism_target](experimentRun__astigmatism_target.md)  <sub>0..1</sub>
     * Description: Target astigmatism in Angstroms
     * Range: [Float](types/Float.md)
 * [➞coma](experimentRun__coma.md)  <sub>0..1</sub>
     * Description: Coma aberration in nanometers
     * Range: [Float](types/Float.md)
 * [➞stage_tilt](experimentRun__stage_tilt.md)  <sub>0..1</sub>
     * Description: Stage tilt angle in degrees
     * Range: [Float](types/Float.md)
 * [➞autoloader_slot](experimentRun__autoloader_slot.md)  <sub>0..1</sub>
     * Description: Autoloader slot identifier
     * Range: [String](types/String.md)
 * [➞shots_per_hole](experimentRun__shots_per_hole.md)  <sub>0..1</sub>
     * Description: Number of shots taken per hole
     * Range: [Integer](types/Integer.md)
 * [➞holes_per_group](experimentRun__holes_per_group.md)  <sub>0..1</sub>
     * Description: Number of holes per group
     * Range: [Integer](types/Integer.md)
 * [➞acquisition_software](experimentRun__acquisition_software.md)  <sub>0..1</sub>
     * Description: Acquisition software used (e.g., SerialEM, EPU, Leginon)
     * Range: [String](types/String.md)
 * [➞acquisition_software_version](experimentRun__acquisition_software_version.md)  <sub>0..1</sub>
     * Description: Version of acquisition software
     * Range: [String](types/String.md)
 * [➞wavelength](experimentRun__wavelength.md)  <sub>0..1</sub>
     * Description: X-ray wavelength
     * Range: [Float](types/Float.md)
 * [➞oscillation_angle](experimentRun__oscillation_angle.md)  <sub>0..1</sub>
     * Description: Oscillation angle per image
     * Range: [Float](types/Float.md)
 * [➞start_angle](experimentRun__start_angle.md)  <sub>0..1</sub>
     * Description: Starting rotation angle
     * Range: [Float](types/Float.md)
 * [➞number_of_images](experimentRun__number_of_images.md)  <sub>0..1</sub>
     * Description: Total number of diffraction images collected
     * Range: [Integer](types/Integer.md)
 * [➞beam_center_x](experimentRun__beam_center_x.md)  <sub>0..1</sub>
     * Description: Beam center X coordinate
     * Range: [Float](types/Float.md)
 * [➞beam_center_y](experimentRun__beam_center_y.md)  <sub>0..1</sub>
     * Description: Beam center Y coordinate
     * Range: [Float](types/Float.md)
 * [➞detector_distance](experimentRun__detector_distance.md)  <sub>0..1</sub>
     * Description: Distance from sample to detector
     * Range: [Float](types/Float.md)
 * [➞pixel_size_x](experimentRun__pixel_size_x.md)  <sub>0..1</sub>
     * Description: Pixel size X dimension
     * Range: [Float](types/Float.md)
 * [➞pixel_size_y](experimentRun__pixel_size_y.md)  <sub>0..1</sub>
     * Description: Pixel size Y dimension
     * Range: [Float](types/Float.md)
 * [➞total_rotation](experimentRun__total_rotation.md)  <sub>0..1</sub>
     * Description: Total rotation range collected
     * Range: [Float](types/Float.md)
 * [➞beamline](experimentRun__beamline.md)  <sub>0..1</sub>
     * Description: Beamline identifier (e.g., FMX, AMX, 12.3.1)
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
