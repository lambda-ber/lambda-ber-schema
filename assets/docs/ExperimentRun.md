
# Class: ExperimentRun

An experimental data collection session

URI: [lambdaber:ExperimentRun](https://w3id.org/lambda-ber-schema/ExperimentRun)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QualityMetrics],[NamedThing],[Instrument],[ExperimentalConditions],[QuantityValue]<ispyb_session_id%200..1-++[ExperimentRun&#124;experiment_code:string;sample_id:string;experiment_date:string%20%3F;operator_id:string%20%3F;technique:TechniqueEnum;experimental_method:ExperimentalMethodEnum%20%3F;raw_data_location:string%20%3F;processing_status:ProcessingStatusEnum%20%3F;autoloader_slot:string%20%3F;acquisition_software:string%20%3F;acquisition_software_version:string%20%3F;beamline:string%20%3F;synchrotron_mode:string%20%3F;start_time:string%20%3F;end_time:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<ispyb_data_collection_id%200..1-++[ExperimentRun],[QuantityValue]<resolution_at_corner%200..1-++[ExperimentRun],[QuantityValue]<resolution%200..1-++[ExperimentRun],[QuantityValue]<exposure_time%200..1-++[ExperimentRun],[QuantityValue]<undulator_gap%200..1-++[ExperimentRun],[QuantityValue]<slit_gap_vertical%200..1-++[ExperimentRun],[QuantityValue]<slit_gap_horizontal%200..1-++[ExperimentRun],[QuantityValue]<flux_end%200..1-++[ExperimentRun],[QuantityValue]<flux%200..1-++[ExperimentRun],[QuantityValue]<transmission%200..1-++[ExperimentRun],[QuantityValue]<total_rotation%200..1-++[ExperimentRun],[QuantityValue]<pixel_size_y%200..1-++[ExperimentRun],[QuantityValue]<pixel_size_x%200..1-++[ExperimentRun],[QuantityValue]<detector_distance%200..1-++[ExperimentRun],[QuantityValue]<beam_center_y%200..1-++[ExperimentRun],[QuantityValue]<beam_center_x%200..1-++[ExperimentRun],[QuantityValue]<number_of_images%200..1-++[ExperimentRun],[QuantityValue]<start_angle%200..1-++[ExperimentRun],[QuantityValue]<oscillation_angle%200..1-++[ExperimentRun],[QuantityValue]<wavelength%200..1-++[ExperimentRun],[QuantityValue]<holes_per_group%200..1-++[ExperimentRun],[QuantityValue]<shots_per_hole%200..1-++[ExperimentRun],[QuantityValue]<stage_tilt%200..1-++[ExperimentRun],[QuantityValue]<coma%200..1-++[ExperimentRun],[QuantityValue]<astigmatism_target%200..1-++[ExperimentRun],[QuantityValue]<defocus_range_increment%200..1-++[ExperimentRun],[QuantityValue]<defocus_range_max%200..1-++[ExperimentRun],[QuantityValue]<defocus_range_min%200..1-++[ExperimentRun],[QuantityValue]<defocus_target%200..1-++[ExperimentRun],[QuantityValue]<dose_rate%200..1-++[ExperimentRun],[QuantityValue]<total_dose%200..1-++[ExperimentRun],[QuantityValue]<total_exposure_time%200..1-++[ExperimentRun],[QuantityValue]<frames_per_movie%200..1-++[ExperimentRun],[QuantityValue]<exposure_time_per_frame%200..1-++[ExperimentRun],[QuantityValue]<camera_binning%200..1-++[ExperimentRun],[QuantityValue]<calibrated_pixel_size%200..1-++[ExperimentRun],[QuantityValue]<magnification%200..1-++[ExperimentRun],[QualityMetrics]<quality_metrics%200..1-++[ExperimentRun],[DataCollectionStrategy]<data_collection_strategy%200..1-++[ExperimentRun],[ExperimentalConditions]<experimental_conditions%200..1-++[ExperimentRun],[Instrument]<instrument_id%201..1-%20[ExperimentRun],[Study]++-%20instrument_runs%200..*>[ExperimentRun],[NamedThing]^-[ExperimentRun],[Study],[DataCollectionStrategy])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QualityMetrics],[NamedThing],[Instrument],[ExperimentalConditions],[QuantityValue]<ispyb_session_id%200..1-++[ExperimentRun&#124;experiment_code:string;sample_id:string;experiment_date:string%20%3F;operator_id:string%20%3F;technique:TechniqueEnum;experimental_method:ExperimentalMethodEnum%20%3F;raw_data_location:string%20%3F;processing_status:ProcessingStatusEnum%20%3F;autoloader_slot:string%20%3F;acquisition_software:string%20%3F;acquisition_software_version:string%20%3F;beamline:string%20%3F;synchrotron_mode:string%20%3F;start_time:string%20%3F;end_time:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<ispyb_data_collection_id%200..1-++[ExperimentRun],[QuantityValue]<resolution_at_corner%200..1-++[ExperimentRun],[QuantityValue]<resolution%200..1-++[ExperimentRun],[QuantityValue]<exposure_time%200..1-++[ExperimentRun],[QuantityValue]<undulator_gap%200..1-++[ExperimentRun],[QuantityValue]<slit_gap_vertical%200..1-++[ExperimentRun],[QuantityValue]<slit_gap_horizontal%200..1-++[ExperimentRun],[QuantityValue]<flux_end%200..1-++[ExperimentRun],[QuantityValue]<flux%200..1-++[ExperimentRun],[QuantityValue]<transmission%200..1-++[ExperimentRun],[QuantityValue]<total_rotation%200..1-++[ExperimentRun],[QuantityValue]<pixel_size_y%200..1-++[ExperimentRun],[QuantityValue]<pixel_size_x%200..1-++[ExperimentRun],[QuantityValue]<detector_distance%200..1-++[ExperimentRun],[QuantityValue]<beam_center_y%200..1-++[ExperimentRun],[QuantityValue]<beam_center_x%200..1-++[ExperimentRun],[QuantityValue]<number_of_images%200..1-++[ExperimentRun],[QuantityValue]<start_angle%200..1-++[ExperimentRun],[QuantityValue]<oscillation_angle%200..1-++[ExperimentRun],[QuantityValue]<wavelength%200..1-++[ExperimentRun],[QuantityValue]<holes_per_group%200..1-++[ExperimentRun],[QuantityValue]<shots_per_hole%200..1-++[ExperimentRun],[QuantityValue]<stage_tilt%200..1-++[ExperimentRun],[QuantityValue]<coma%200..1-++[ExperimentRun],[QuantityValue]<astigmatism_target%200..1-++[ExperimentRun],[QuantityValue]<defocus_range_increment%200..1-++[ExperimentRun],[QuantityValue]<defocus_range_max%200..1-++[ExperimentRun],[QuantityValue]<defocus_range_min%200..1-++[ExperimentRun],[QuantityValue]<defocus_target%200..1-++[ExperimentRun],[QuantityValue]<dose_rate%200..1-++[ExperimentRun],[QuantityValue]<total_dose%200..1-++[ExperimentRun],[QuantityValue]<total_exposure_time%200..1-++[ExperimentRun],[QuantityValue]<frames_per_movie%200..1-++[ExperimentRun],[QuantityValue]<exposure_time_per_frame%200..1-++[ExperimentRun],[QuantityValue]<camera_binning%200..1-++[ExperimentRun],[QuantityValue]<calibrated_pixel_size%200..1-++[ExperimentRun],[QuantityValue]<magnification%200..1-++[ExperimentRun],[QualityMetrics]<quality_metrics%200..1-++[ExperimentRun],[DataCollectionStrategy]<data_collection_strategy%200..1-++[ExperimentRun],[ExperimentalConditions]<experimental_conditions%200..1-++[ExperimentRun],[Instrument]<instrument_id%201..1-%20[ExperimentRun],[Study]++-%20instrument_runs%200..*>[ExperimentRun],[NamedThing]^-[ExperimentRun],[Study],[DataCollectionStrategy])

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
     * Range: [QuantityValue](QuantityValue.md)
 * [➞calibrated_pixel_size](experimentRun__calibrated_pixel_size.md)  <sub>0..1</sub>
     * Description: Calibrated pixel size in Angstroms per pixel
     * Range: [QuantityValue](QuantityValue.md)
 * [➞camera_binning](experimentRun__camera_binning.md)  <sub>0..1</sub>
     * Description: Camera binning factor. This must be a positive float value (e.g., 1, 1.5, 2, 3).
     * Range: [QuantityValue](QuantityValue.md)
 * [➞exposure_time_per_frame](experimentRun__exposure_time_per_frame.md)  <sub>0..1</sub>
     * Description: Exposure time per frame in milliseconds
     * Range: [QuantityValue](QuantityValue.md)
 * [➞frames_per_movie](experimentRun__frames_per_movie.md)  <sub>0..1</sub>
     * Description: Number of frames per movie
     * Range: [QuantityValue](QuantityValue.md)
 * [➞total_exposure_time](experimentRun__total_exposure_time.md)  <sub>0..1</sub>
     * Description: Total exposure time in milliseconds
     * Range: [QuantityValue](QuantityValue.md)
 * [➞total_dose](experimentRun__total_dose.md)  <sub>0..1</sub>
     * Description: Total electron dose in e-/Angstrom^2
     * Range: [QuantityValue](QuantityValue.md)
 * [➞dose_rate](experimentRun__dose_rate.md)  <sub>0..1</sub>
     * Description: Dose rate in e-/pixel/s or e-/Angstrom^2/s
     * Range: [QuantityValue](QuantityValue.md)
 * [➞defocus_target](experimentRun__defocus_target.md)  <sub>0..1</sub>
     * Description: Target defocus value in micrometers
     * Range: [QuantityValue](QuantityValue.md)
 * [➞defocus_range_min](experimentRun__defocus_range_min.md)  <sub>0..1</sub>
     * Description: Minimum defocus range in micrometers
     * Range: [QuantityValue](QuantityValue.md)
 * [➞defocus_range_max](experimentRun__defocus_range_max.md)  <sub>0..1</sub>
     * Description: Maximum defocus range in micrometers
     * Range: [QuantityValue](QuantityValue.md)
 * [➞defocus_range_increment](experimentRun__defocus_range_increment.md)  <sub>0..1</sub>
     * Description: Defocus range increment in micrometers
     * Range: [QuantityValue](QuantityValue.md)
 * [➞astigmatism_target](experimentRun__astigmatism_target.md)  <sub>0..1</sub>
     * Description: Target astigmatism in Angstroms
     * Range: [QuantityValue](QuantityValue.md)
 * [➞coma](experimentRun__coma.md)  <sub>0..1</sub>
     * Description: Coma aberration in nanometers
     * Range: [QuantityValue](QuantityValue.md)
 * [➞stage_tilt](experimentRun__stage_tilt.md)  <sub>0..1</sub>
     * Description: Stage tilt angle in degrees
     * Range: [QuantityValue](QuantityValue.md)
 * [➞autoloader_slot](experimentRun__autoloader_slot.md)  <sub>0..1</sub>
     * Description: Autoloader slot identifier
     * Range: [String](types/String.md)
 * [➞shots_per_hole](experimentRun__shots_per_hole.md)  <sub>0..1</sub>
     * Description: Number of shots taken per hole
     * Range: [QuantityValue](QuantityValue.md)
 * [➞holes_per_group](experimentRun__holes_per_group.md)  <sub>0..1</sub>
     * Description: Number of holes per group. Data providers may include unit information in the QuantityValue if needed.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞acquisition_software](experimentRun__acquisition_software.md)  <sub>0..1</sub>
     * Description: Acquisition software used (e.g., SerialEM, EPU, Leginon)
     * Range: [String](types/String.md)
 * [➞acquisition_software_version](experimentRun__acquisition_software_version.md)  <sub>0..1</sub>
     * Description: Version of acquisition software
     * Range: [String](types/String.md)
 * [➞wavelength](experimentRun__wavelength.md)  <sub>0..1</sub>
     * Description: X-ray wavelength, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞oscillation_angle](experimentRun__oscillation_angle.md)  <sub>0..1</sub>
     * Description: Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞start_angle](experimentRun__start_angle.md)  <sub>0..1</sub>
     * Description: Starting rotation angle, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞number_of_images](experimentRun__number_of_images.md)  <sub>0..1</sub>
     * Description: Total number of diffraction images collected
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_center_x](experimentRun__beam_center_x.md)  <sub>0..1</sub>
     * Description: Beam center X coordinate, typically specified in pixels ([px]). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_center_y](experimentRun__beam_center_y.md)  <sub>0..1</sub>
     * Description: Beam center Y coordinate, typically specified in pixels ([px]). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞detector_distance](experimentRun__detector_distance.md)  <sub>0..1</sub>
     * Description: Distance from sample to detector, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞pixel_size_x](experimentRun__pixel_size_x.md)  <sub>0..1</sub>
     * Description: Pixel size X dimension, typically specified in micrometers (µm). Data providers may specify alternative units (e.g., Angstroms) by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞pixel_size_y](experimentRun__pixel_size_y.md)  <sub>0..1</sub>
     * Description: Pixel size Y dimension, typically specified in micrometers (µm). Data providers may specify alternative units (e.g., Angstroms) by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞total_rotation](experimentRun__total_rotation.md)  <sub>0..1</sub>
     * Description: Total rotation range collected, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beamline](experimentRun__beamline.md)  <sub>0..1</sub>
     * Description: Beamline identifier (e.g., FMX, AMX, 12.3.1)
     * Range: [String](types/String.md)
 * [➞transmission](experimentRun__transmission.md)  <sub>0..1</sub>
     * Description: X-ray beam transmission as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞flux](experimentRun__flux.md)  <sub>0..1</sub>
     * Description: Photon flux at sample position, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞flux_end](experimentRun__flux_end.md)  <sub>0..1</sub>
     * Description: Photon flux at end of data collection, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞slit_gap_horizontal](experimentRun__slit_gap_horizontal.md)  <sub>0..1</sub>
     * Description: Horizontal slit gap aperture, typically specified in micrometers (µm). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞slit_gap_vertical](experimentRun__slit_gap_vertical.md)  <sub>0..1</sub>
     * Description: Vertical slit gap aperture, typically specified in micrometers (µm). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞undulator_gap](experimentRun__undulator_gap.md)  <sub>0..1</sub>
     * Description: Undulator gap setting, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue. Primary undulator gap for beamlines with insertion devices.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞synchrotron_mode](experimentRun__synchrotron_mode.md)  <sub>0..1</sub>
     * Description: Synchrotron storage ring fill mode
     * Range: [String](types/String.md)
 * [➞exposure_time](experimentRun__exposure_time.md)  <sub>0..1</sub>
     * Description: Exposure time per image, typically specified in seconds (s). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞start_time](experimentRun__start_time.md)  <sub>0..1</sub>
     * Description: Data collection start timestamp
     * Range: [String](types/String.md)
 * [➞end_time](experimentRun__end_time.md)  <sub>0..1</sub>
     * Description: Data collection end timestamp
     * Range: [String](types/String.md)
 * [➞resolution](experimentRun__resolution.md)  <sub>0..1</sub>
     * Description: Resolution at edge of detector, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞resolution_at_corner](experimentRun__resolution_at_corner.md)  <sub>0..1</sub>
     * Description: Resolution at corner of detector, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ispyb_data_collection_id](experimentRun__ispyb_data_collection_id.md)  <sub>0..1</sub>
     * Description: ISPyB DataCollection.dataCollectionId for traceability
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ispyb_session_id](experimentRun__ispyb_session_id.md)  <sub>0..1</sub>
     * Description: ISPyB BLSession.sessionId
     * Range: [QuantityValue](QuantityValue.md)

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
