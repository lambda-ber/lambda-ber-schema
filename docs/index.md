# lambda-ber-schema-schema

lambda-ber-schema is a comprehensive schema for representing multimodal structural biology imaging data, 
from atomic-resolution structures to tissue-level organization. It supports diverse experimental 
techniques including cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and 
spectroscopic imaging.

__NOTE__ this schema was developed rapidly using AI assistance, there may be mistakes!

## Schema Organization

The schema follows a hierarchical structure that mirrors how structural biology research is organized:

The top-level entity is a [Dataset](elements/Dataset.md), which serves as a container for related research.
A dataset might represent all data from a specific grant, collaboration, or publication.

Each dataset contains one or more [Studies](elements/Study.md), which are focused investigations of specific
biological questions. For example, a study might investigate "Heat stress response in Arabidopsis"
or "Structure of the human ribosome under different conditions."

Within each study, you'll find:

### Biological Materials
- [Samples](elements/Sample.md): The biological specimens being studied (proteins, nucleic acids, complexes, 
  cells, tissues). Each sample includes detailed molecular composition, buffer conditions, and 
  storage information. For example, a purified protein with its sequence, concentration, and buffer pH.

- [Sample Preparations](elements/SamplePreparation.md): How samples were prepared for specific techniques.
  This includes cryo-EM grid preparation (vitrification parameters), crystallization conditions for
  X-ray studies, or staining protocols for fluorescence microscopy.

### Data Collection
- [Instruments](elements/Instrument.md): The equipment used, from Titan Krios microscopes to synchrotron 
  beamlines. Each instrument type ([CryoEMInstrument](elements/CryoEMInstrument.md), 
  [XRayInstrument](elements/XRayInstrument.md), [SAXSInstrument](elements/SAXSInstrument.md)) has specific parameters
  like accelerating voltage, detector type, or beam energy.

- [Experiment Runs](elements/ExperimentRun.md): Individual data collection sessions that link samples to 
  instruments. An experiment run captures when, how, and under what conditions data was collected,
  including quality metrics like resolution and completeness.

### Data Processing
- [Workflow Runs](elements/WorkflowRun.md): Computational processing steps applied to raw data. This includes
  motion correction for cryo-EM movies, 3D reconstruction, model building, or phase determination
  for crystallography. Each workflow tracks the software used, parameters, and computational resources.

### Data Products
- [Data Files](elements/DataFile.md): Any files generated or used, from raw data to final models. Each file
  is tracked with checksums for data integrity and typed (micrograph, particles, volume, model).

- [Images](elements/Image.md): Specialized classes for different imaging modalities:
  - [Image2D](elements/Image2D.md): Micrographs, diffraction patterns
  - [Image3D](elements/Image3D.md): 3D reconstructions, tomograms
  - [FTIRImage](elements/FTIRImage.md): Molecular composition maps from infrared spectroscopy
  - [FluorescenceImage](elements/FluorescenceImage.md): Fluorophore-labeled cellular components
  - [OpticalImage](elements/OpticalImage.md): Brightfield/phase contrast microscopy
  - [XRFImage](elements/XRFImage.md): Elemental distribution maps

## Example Usage

A typical cryo-EM study of a protein complex would include:

1. Sample records for the purified complex with molecular weight and buffer composition
2. Grid preparation details with vitrification parameters
3. Microscope specifications and data collection parameters
4. Processing workflows from motion correction through 3D refinement
5. Final reconstructed volumes and fitted atomic models

A multimodal plant imaging study might combine:

1. Whole plant optical imaging for morphology
2. XRF imaging to map nutrient distribution
3. FTIR spectroscopy to identify stress-related molecular changes
4. Fluorescence microscopy to track specific protein responses
5. Cryo-EM of isolated organelles for ultrastructural details

## Key Features

- **Technique-agnostic core**: The same schema handles data from any structural biology method
- **Rich metadata**: Comprehensive tracking from sample to structure
- **Workflow provenance**: Complete computational reproducibility
- **Multimodal support**: Seamlessly integrate data across scales and techniques
- **Standards-compliant**: Follows FAIR principles and integrates with existing ontologies


URI: https://w3id.org/lambda-ber-schema/

Name: lambda-ber-schema-schema



## Classes

| Class | Description |
| --- | --- |
| [BufferComposition](elements/BufferComposition.md) | Buffer composition for sample storage |
| [ComputeResources](elements/ComputeResources.md) | Computational resources used |
| [DataCollectionStrategy](elements/DataCollectionStrategy.md) | Strategy for data collection |
| [ExperimentalConditions](elements/ExperimentalConditions.md) | Environmental and experimental conditions |
| [ImageFeature](elements/ImageFeature.md) |  |
| [MolecularComposition](elements/MolecularComposition.md) | Molecular composition of a sample |
| [NamedThing](elements/NamedThing.md) | A named thing |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataFile](elements/DataFile.md) | A data file generated or used in the study |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dataset](elements/Dataset.md) | A collection of studies |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentRun](elements/ExperimentRun.md) | An experimental data collection session |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image](elements/Image.md) | An image file from structural biology experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FTIRImage](elements/FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image2D](elements/Image2D.md) | A 2D image (micrograph, diffraction pattern) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FluorescenceImage](elements/FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OpticalImage](elements/OpticalImage.md) | Visible light optical microscopy or photography image |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRFImage](elements/XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image3D](elements/Image3D.md) | A 3D volume or tomogram |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Instrument](elements/Instrument.md) | An instrument used to collect data |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CryoEMInstrument](elements/CryoEMInstrument.md) | Cryo-EM microscope specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SAXSInstrument](elements/SAXSInstrument.md) | SAXS/WAXS instrument specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRayInstrument](elements/XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sample](elements/Sample.md) | A biological sample used in structural biology experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SamplePreparation](elements/SamplePreparation.md) | A process that prepares a sample for imaging |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Study](elements/Study.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WorkflowRun](elements/WorkflowRun.md) | A computational processing workflow execution |
| [OntologyTerm](elements/OntologyTerm.md) |  |
| [QualityMetrics](elements/QualityMetrics.md) | Quality metrics for experiments |
| [StorageConditions](elements/StorageConditions.md) | Storage conditions for samples |
| [TechniqueSpecificPreparation](elements/TechniqueSpecificPreparation.md) | Base class for technique-specific preparation details |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CryoEMPreparation](elements/CryoEMPreparation.md) | Cryo-EM specific sample preparation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SAXSPreparation](elements/SAXSPreparation.md) | SAXS/WAXS specific preparation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRayPreparation](elements/XRayPreparation.md) | X-ray crystallography specific preparation |



## Slots

| Slot | Description |
| --- | --- |
| [accelerating_voltage](elements/accelerating_voltage.md) | Accelerating voltage in kV |
| [acquisition_date](elements/acquisition_date.md) | Date image was acquired |
| [additives](elements/additives.md) | Additional additives in the buffer |
| [apodization_function](elements/apodization_function.md) | Mathematical function used for apodization |
| [astigmatism](elements/astigmatism.md) | Astigmatism value |
| [atmosphere](elements/atmosphere.md) | Storage atmosphere conditions |
| [autoloader_capacity](elements/autoloader_capacity.md) | Number of grids the autoloader can hold |
| [background_correction](elements/background_correction.md) | Method used for background correction |
| [beam_energy](elements/beam_energy.md) | X-ray beam energy in keV |
| [beam_size](elements/beam_size.md) | X-ray beam size in micrometers |
| [beam_size_max](elements/beam_size_max.md) | Maximum beam size in micrometers |
| [beam_size_min](elements/beam_size_min.md) | Minimum beam size in micrometers |
| [blot_force](elements/blot_force.md) | Blotting force setting |
| [blot_time](elements/blot_time.md) | Blotting time in seconds |
| [buffer_composition](elements/buffer_composition.md) | Buffer composition including pH, salts, additives |
| [buffer_matching_protocol](elements/buffer_matching_protocol.md) | Protocol for buffer matching |
| [calibration_standard](elements/calibration_standard.md) | Reference standard used for calibration |
| [cell_path_length](elements/cell_path_length.md) | Path length in mm |
| [chamber_temperature](elements/chamber_temperature.md) | Chamber temperature in Celsius |
| [channel_name](elements/channel_name.md) | Name of the fluorescence channel (e |
| [checksum](elements/checksum.md) | SHA-256 checksum for data integrity |
| [collection_mode](elements/collection_mode.md) | Mode of data collection |
| [color_channels](elements/color_channels.md) | Color channels present (e |
| [completed_at](elements/completed_at.md) | Workflow completion time |
| [completeness](elements/completeness.md) | Data completeness percentage |
| [components](elements/components.md) | Buffer components and their concentrations |
| [compute_resources](elements/compute_resources.md) | Computational resources used |
| [concentration](elements/concentration.md) | Sample concentration in mg/mL or µM |
| [concentration_series](elements/concentration_series.md) | Concentration values for series measurements |
| [concentration_unit](elements/concentration_unit.md) | Unit of concentration measurement |
| [contrast_method](elements/contrast_method.md) | Contrast enhancement method used |
| [cpu_hours](elements/cpu_hours.md) | CPU hours used |
| [creation_date](elements/creation_date.md) | File creation date |
| [cryoprotectant](elements/cryoprotectant.md) | Cryoprotectant used |
| [cryoprotectant_concentration](elements/cryoprotectant_concentration.md) | Cryoprotectant concentration percentage |
| [crystal_cooling_capability](elements/crystal_cooling_capability.md) | Crystal cooling system available |
| [crystal_size](crystal_size.md) | Crystal dimensions in micrometers |
| [crystallization_conditions](elements/crystallization_conditions.md) | Detailed crystallization conditions |
| [crystallization_method](elements/crystallization_method.md) | Method used for crystallization |
| [cs_corrector](elements/cs_corrector.md) | Spherical aberration corrector present |
| [current_status](elements/current_status.md) | Current operational status |
| [data_collection_strategy](elements/data_collection_strategy.md) | Strategy for data collection |
| [data_files](elements/data_files.md) |  |
| [data_type](elements/data_type.md) | Type of data in the file |
| [definition](elements/definition.md) |  |
| [defocus](elements/defocus.md) | Defocus value in micrometers |
| [description](elements/description.md) |  |
| [detector_dimensions](elements/detector_dimensions.md) | Detector dimensions in pixels (e |
| [detector_distance_max](elements/detector_distance_max.md) | Maximum detector distance in mm |
| [detector_distance_min](elements/detector_distance_min.md) | Minimum detector distance in mm |
| [detector_type](detector_type.md) | Type of detector |
| [dimensions_x](elements/dimensions_x.md) | Image width in pixels |
| [dimensions_y](elements/dimensions_y.md) | Image height in pixels |
| [dimensions_z](elements/dimensions_z.md) | Image depth in pixels/slices |
| [dose](elements/dose.md) | Electron dose in e-/Å² |
| [dose_per_frame](elements/dose_per_frame.md) | Dose per frame |
| [duration](elements/duration.md) | Storage duration |
| [dwell_time](elements/dwell_time.md) | Dwell time per pixel in milliseconds |
| [elements_measured](elements/elements_measured.md) | Elements detected and measured |
| [emission_filter](elements/emission_filter.md) | Specifications of the emission filter |
| [emission_wavelength](elements/emission_wavelength.md) | Emission wavelength in nanometers |
| [energy_max](elements/energy_max.md) | Maximum X-ray energy in keV |
| [energy_min](elements/energy_min.md) | Minimum X-ray energy in keV |
| [excitation_filter](elements/excitation_filter.md) | Specifications of the excitation filter |
| [excitation_wavelength](elements/excitation_wavelength.md) | Excitation wavelength in nanometers |
| [experiment_code](elements/experiment_code.md) | Unique experiment identifier |
| [experiment_date](elements/experiment_date.md) | Date of the experiment |
| [experiment_id](elements/experiment_id.md) | Reference to the source experiment |
| [experimental_conditions](elements/experimental_conditions.md) | Environmental and experimental conditions |
| [exposure_time](elements/exposure_time.md) | Exposure time in seconds |
| [file_format](elements/file_format.md) | File format |
| [file_name](elements/file_name.md) | Name of the file |
| [file_path](elements/file_path.md) | Path to the file |
| [file_size_bytes](elements/file_size_bytes.md) | File size in bytes |
| [flash_cooling_method](elements/flash_cooling_method.md) | Flash cooling protocol |
| [fluorophore](elements/fluorophore.md) | Name or type of fluorophore used |
| [flux](elements/flux.md) | Photon flux in photons/second |
| [flux_density](elements/flux_density.md) | Photon flux density in photons/s/mm² |
| [frame_rate](elements/frame_rate.md) | Frames per second |
| [goniometer_type](elements/goniometer_type.md) | Type of goniometer |
| [gpu_hours](elements/gpu_hours.md) | GPU hours used |
| [grid_type](elements/grid_type.md) | Type of EM grid used |
| [hole_size](elements/hole_size.md) | Hole size in micrometers |
| [humidity](elements/humidity.md) | Humidity percentage |
| [humidity_percentage](elements/humidity_percentage.md) | Chamber humidity during vitrification |
| [id](elements/id.md) |  |
| [illumination_type](elements/illumination_type.md) | Type of illumination (brightfield, darkfield, phase contrast, DIC) |
| [images](elements/images.md) |  |
| [installation_date](elements/installation_date.md) | Date of instrument installation |
| [instrument_code](elements/instrument_code.md) | Unique identifier code for the instrument |
| [instrument_id](elements/instrument_id.md) | Reference to the instrument used |
| [instrument_runs](elements/instrument_runs.md) |  |
| [keywords](elements/keywords.md) |  |
| [label](elements/label.md) |  |
| [laser_power](elements/laser_power.md) | Laser power in milliwatts or percentage |
| [ligands](elements/ligands.md) | Bound ligands or cofactors |
| [magnification](elements/magnification.md) | Optical magnification factor |
| [manufacturer](elements/manufacturer.md) | Instrument manufacturer |
| [memory_gb](elements/memory_gb.md) | Maximum memory used in GB |
| [model](elements/model.md) | Instrument model |
| [modifications](elements/modifications.md) | Post-translational modifications or chemical modifications |
| [molecular_composition](elements/molecular_composition.md) | Description of molecular composition including sequences, modifications, liga... |
| [molecular_signatures](elements/molecular_signatures.md) | Identified molecular signatures or peaks |
| [molecular_weight](elements/molecular_weight.md) | Molecular weight in kDa |
| [monochromator_type](elements/monochromator_type.md) | Type of monochromator |
| [mounting_method](elements/mounting_method.md) | Crystal mounting method |
| [number_of_scans](elements/number_of_scans.md) | Number of scans averaged for the spectrum |
| [numerical_aperture](elements/numerical_aperture.md) | Numerical aperture of the objective lens |
| [ontology](elements/ontology.md) |  |
| [operator_id](elements/operator_id.md) | Person who performed the preparation |
| [output_files](elements/output_files.md) | Output files generated |
| [parent_sample_id](elements/parent_sample_id.md) | Reference to parent sample for derivation tracking |
| [ph](elements/ph.md) | pH of the buffer |
| [phase_plate](elements/phase_plate.md) | Phase plate available |
| [pinhole_size](elements/pinhole_size.md) | Pinhole size in Airy units for confocal microscopy |
| [pixel_size](elements/pixel_size.md) | Pixel size in Angstroms |
| [pixel_size_max](pixel_size_max.md) | Maximum pixel size in Angstroms per pixel |
| [pixel_size_min](pixel_size_min.md) | Minimum pixel size in Angstroms per pixel |
| [plasma_treatment](elements/plasma_treatment.md) | Plasma treatment details |
| [preparation_date](elements/preparation_date.md) | Date of sample preparation |
| [preparation_method](elements/preparation_method.md) | Method used to prepare the sample |
| [preparation_type](elements/preparation_type.md) | Type of sample preparation |
| [pressure](elements/pressure.md) | Pressure in kPa |
| [processing_level](elements/processing_level.md) | Processing level (0=raw, 1=corrected, 2=derived, 3=model) |
| [processing_parameters](elements/processing_parameters.md) | Parameters used in processing |
| [processing_status](elements/processing_status.md) | Current processing status |
| [protocol_description](elements/protocol_description.md) | Detailed protocol description |
| [purity_percentage](elements/purity_percentage.md) | Sample purity as percentage |
| [q_range_max](elements/q_range_max.md) | Maximum q value in inverse Angstroms |
| [q_range_min](elements/q_range_min.md) | Minimum q value in inverse Angstroms |
| [quality_metrics](elements/quality_metrics.md) | Quality control metrics for the sample |
| [quantum_yield](elements/quantum_yield.md) | Quantum yield of the fluorophore |
| [r_factor](elements/r_factor.md) | R-factor for crystallography |
| [raw_data_location](elements/raw_data_location.md) | Location of raw data files |
| [reconstruction_method](elements/reconstruction_method.md) | Method used for 3D reconstruction |
| [resolution](elements/resolution.md) | Resolution in Angstroms |
| [sample_cell_type](elements/sample_cell_type.md) | Type of sample cell used |
| [sample_changer_capacity](elements/sample_changer_capacity.md) | Number of samples in automatic sample changer |
| [sample_code](elements/sample_code.md) | Unique identifier code for the sample |
| [sample_id](elements/sample_id.md) | Reference to the sample being prepared |
| [sample_preparations](elements/sample_preparations.md) |  |
| [sample_type](elements/sample_type.md) | Type of biological sample |
| [samples](elements/samples.md) |  |
| [sequences](elements/sequences.md) | Amino acid or nucleotide sequences |
| [signal_to_noise](elements/signal_to_noise.md) | Signal to noise ratio |
| [software_name](elements/software_name.md) | Software used for processing |
| [software_version](elements/software_version.md) | Software version |
| [source_type](elements/source_type.md) | Type of X-ray source |
| [spectral_resolution](elements/spectral_resolution.md) | Spectral resolution in cm⁻¹ |
| [started_at](elements/started_at.md) | Workflow start time |
| [storage_conditions](elements/storage_conditions.md) | Storage conditions for the sample |
| [storage_gb](elements/storage_gb.md) | Storage used in GB |
| [studies](elements/studies.md) |  |
| [support_film](elements/support_film.md) | Support film type |
| [technique](elements/technique.md) | Technique used for data collection |
| [temperature](elements/temperature.md) | Storage temperature in Celsius |
| [temperature_control](elements/temperature_control.md) | Temperature control settings |
| [temperature_control_range](elements/temperature_control_range.md) | Temperature control range in Celsius |
| [temperature_unit](elements/temperature_unit.md) | Temperature unit |
| [terms](elements/terms.md) |  |
| [title](elements/title.md) |  |
| [total_dose](elements/total_dose.md) | Total electron dose for cryo-EM |
| [total_frames](elements/total_frames.md) | Total number of frames/images |
| [vitrification_method](elements/vitrification_method.md) | Method used for vitrification |
| [voxel_size](elements/voxel_size.md) | Voxel size in Angstroms |
| [wavenumber_max](elements/wavenumber_max.md) | Maximum wavenumber in cm⁻¹ |
| [wavenumber_min](elements/wavenumber_min.md) | Minimum wavenumber in cm⁻¹ |
| [white_balance](elements/white_balance.md) | White balance settings |
| [workflow_code](elements/workflow_code.md) | Unique workflow identifier |
| [workflow_runs](elements/workflow_runs.md) |  |
| [workflow_type](elements/workflow_type.md) | Type of processing workflow |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CollectionModeEnum](elements/CollectionModeEnum.md) | Data collection modes |
| [ConcentrationUnitEnum](elements/ConcentrationUnitEnum.md) | Units for concentration measurement |
| [CrystallizationMethodEnum](elements/CrystallizationMethodEnum.md) | Methods for protein crystallization |
| [DataTypeEnum](elements/DataTypeEnum.md) | Types of data |
| [DetectorTypeEnum](elements/DetectorTypeEnum.md) | Types of detectors for cryo-EM |
| [FileFormatEnum](elements/FileFormatEnum.md) | File formats |
| [GridTypeEnum](elements/GridTypeEnum.md) | Types of EM grids |
| [IlluminationTypeEnum](elements/IlluminationTypeEnum.md) | Types of illumination for optical microscopy |
| [InstrumentStatusEnum](elements/InstrumentStatusEnum.md) | Operational status of instruments |
| [PreparationTypeEnum](elements/PreparationTypeEnum.md) | Types of sample preparation |
| [ProcessingStatusEnum](elements/ProcessingStatusEnum.md) | Processing status |
| [SampleTypeEnum](elements/SampleTypeEnum.md) | Types of biological samples |
| [TechniqueEnum](elements/TechniqueEnum.md) | Structural biology techniques |
| [TemperatureUnitEnum](elements/TemperatureUnitEnum.md) | Units for temperature measurement |
| [VitrificationMethodEnum](elements/VitrificationMethodEnum.md) | Methods for vitrification |
| [WorkflowTypeEnum](elements/WorkflowTypeEnum.md) | Types of processing workflows |
| [XRaySourceTypeEnum](elements/XRaySourceTypeEnum.md) | Types of X-ray sources |


## Types

| Type | Description |
| --- | --- |
| [Boolean](elements/Boolean.md) | A binary (true or false) value |
| [Curie](elements/Curie.md) | a compact URI |
| [Date](elements/Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](elements/DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](elements/Datetime.md) | The combination of a date and time |
| [Decimal](elements/Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](elements/Double.md) | A real number that conforms to the xsd:double specification |
| [Float](elements/Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](elements/Integer.md) | An integer |
| [Jsonpath](elements/Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](elements/Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](elements/Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](elements/Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](elements/Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](elements/Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](elements/String.md) | A character string |
| [Time](elements/Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](elements/Uri.md) | a complete URI |
| [Uriorcurie](elements/Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
