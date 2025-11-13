# lambda-ber-schema-schema

lambda-ber-schema is a comprehensive schema for representing multimodal structural biology imaging data, 
from atomic-resolution structures to tissue-level organization. It supports diverse experimental 
techniques including cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and 
spectroscopic imaging.

__NOTE__ this schema was developed rapidly using AI assistance, there may be mistakes!

## Schema Organization

The schema follows a hierarchical structure that mirrors how structural biology research is organized:

The top-level entity is a [Dataset](Dataset.md), which serves as a container for related research.
A dataset might represent all data from a specific grant, collaboration, or publication.

Each dataset contains one or more [Studies](Study.md), which are focused investigations of specific
biological questions. For example, a study might investigate "Heat stress response in Arabidopsis"
or "Structure of the human ribosome under different conditions."

Within each study, you'll find:

### Biological Materials
- [Samples](Sample.md): The biological specimens being studied (proteins, nucleic acids, complexes, 
  cells, tissues). Each sample includes detailed molecular composition, buffer conditions, and 
  storage information. For example, a purified protein with its sequence, concentration, and buffer pH.

- [Sample Preparations](SamplePreparation.md): How samples were prepared for specific techniques.
  This includes cryo-EM grid preparation (vitrification parameters), crystallization conditions for
  X-ray studies, or staining protocols for fluorescence microscopy.

### Data Collection
- [Instruments](Instrument.md): The equipment used, from Titan Krios microscopes to synchrotron 
  beamlines. Each instrument type ([CryoEMInstrument](CryoEMInstrument.md), 
  [XRayInstrument](XRayInstrument.md), [SAXSInstrument](SAXSInstrument.md)) has specific parameters
  like accelerating voltage, detector type, or beam energy.

- [Experiment Runs](ExperimentRun.md): Individual data collection sessions that link samples to 
  instruments. An experiment run captures when, how, and under what conditions data was collected,
  including quality metrics like resolution and completeness.

### Data Processing
- [Workflow Runs](WorkflowRun.md): Computational processing steps applied to raw data. This includes
  motion correction for cryo-EM movies, 3D reconstruction, model building, or phase determination
  for crystallography. Each workflow tracks the software used, parameters, and computational resources.

### Data Products
- [Data Files](DataFile.md): Any files generated or used, from raw data to final models. Each file
  is tracked with checksums for data integrity and typed (micrograph, particles, volume, model).

- [Images](Image.md): Specialized classes for different imaging modalities:
  - [Image2D](Image2D.md): Micrographs, diffraction patterns
  - [Image3D](Image3D.md): 3D reconstructions, tomograms
  - [FTIRImage](FTIRImage.md): Molecular composition maps from infrared spectroscopy
  - [FluorescenceImage](FluorescenceImage.md): Fluorophore-labeled cellular components
  - [OpticalImage](OpticalImage.md): Brightfield/phase contrast microscopy
  - [XRFImage](XRFImage.md): Elemental distribution maps

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
| [BufferComposition](BufferComposition.md) | Buffer composition for sample storage |
| [ComputeResources](ComputeResources.md) | Computational resources used |
| [DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |
| [ExperimentalConditions](ExperimentalConditions.md) | Environmental and experimental conditions |
| [ImageFeature](ImageFeature.md) |  |
| [MolecularComposition](MolecularComposition.md) | Molecular composition of a sample |
| [NamedThing](NamedThing.md) | A named thing |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataFile](DataFile.md) | A data file generated or used in the study |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dataset](Dataset.md) | A collection of studies |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentRun](ExperimentRun.md) | An experimental data collection session |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image](Image.md) | An image file from structural biology experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image3D](Image3D.md) | A 3D volume or tomogram |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Instrument](Instrument.md) | An instrument used to collect data |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sample](Sample.md) | A biological sample used in structural biology experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Study](Study.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |
| [OntologyTerm](OntologyTerm.md) |  |
| [QualityMetrics](QualityMetrics.md) | Quality metrics for experiments |
| [StorageConditions](StorageConditions.md) | Storage conditions for samples |
| [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) | Base class for technique-specific preparation details |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CryoEMPreparation](CryoEMPreparation.md) | Cryo-EM specific sample preparation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SAXSPreparation](SAXSPreparation.md) | SAXS/WAXS specific preparation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |



## Slots

| Slot | Description |
| --- | --- |
| [accelerating_voltage](accelerating_voltage.md) | Accelerating voltage in kV |
| [acquisition_date](acquisition_date.md) | Date image was acquired |
| [additives](additives.md) | Additional additives in the buffer |
| [apodization_function](apodization_function.md) | Mathematical function used for apodization |
| [astigmatism](astigmatism.md) | Astigmatism value |
| [atmosphere](atmosphere.md) | Storage atmosphere conditions |
| [autoloader_capacity](autoloader_capacity.md) | Number of grids the autoloader can hold |
| [background_correction](background_correction.md) | Method used for background correction |
| [beam_energy](beam_energy.md) | X-ray beam energy in keV |
| [beam_size](beam_size.md) | X-ray beam size in micrometers |
| [beam_size_max](beam_size_max.md) | Maximum beam size in micrometers |
| [beam_size_min](beam_size_min.md) | Minimum beam size in micrometers |
| [blot_force](blot_force.md) | Blotting force setting |
| [blot_time](blot_time.md) | Blotting time in seconds |
| [buffer_composition](buffer_composition.md) | Buffer composition including pH, salts, additives |
| [buffer_matching_protocol](buffer_matching_protocol.md) | Protocol for buffer matching |
| [calibration_standard](calibration_standard.md) | Reference standard used for calibration |
| [cell_path_length](cell_path_length.md) | Path length in mm |
| [chamber_temperature](chamber_temperature.md) | Chamber temperature in Celsius |
| [channel_name](channel_name.md) | Name of the fluorescence channel (e |
| [checksum](checksum.md) | SHA-256 checksum for data integrity |
| [collection_mode](collection_mode.md) | Mode of data collection |
| [color_channels](color_channels.md) | Color channels present (e |
| [completed_at](completed_at.md) | Workflow completion time |
| [completeness](completeness.md) | Data completeness percentage |
| [components](components.md) | Buffer components and their concentrations |
| [compute_resources](compute_resources.md) | Computational resources used |
| [concentration](concentration.md) | Sample concentration in mg/mL or µM |
| [concentration_series](concentration_series.md) | Concentration values for series measurements |
| [concentration_unit](concentration_unit.md) | Unit of concentration measurement |
| [contrast_method](contrast_method.md) | Contrast enhancement method used |
| [cpu_hours](cpu_hours.md) | CPU hours used |
| [creation_date](creation_date.md) | File creation date |
| [cryoprotectant](cryoprotectant.md) | Cryoprotectant used |
| [cryoprotectant_concentration](cryoprotectant_concentration.md) | Cryoprotectant concentration percentage |
| [crystal_cooling_capability](crystal_cooling_capability.md) | Crystal cooling system available |
| [crystal_size](crystal_size.md) | Crystal dimensions in micrometers |
| [crystallization_conditions](crystallization_conditions.md) | Detailed crystallization conditions |
| [crystallization_method](crystallization_method.md) | Method used for crystallization |
| [cs_corrector](cs_corrector.md) | Spherical aberration corrector present |
| [current_status](current_status.md) | Current operational status |
| [data_collection_strategy](data_collection_strategy.md) | Strategy for data collection |
| [data_files](data_files.md) |  |
| [data_type](data_type.md) | Type of data in the file |
| [definition](definition.md) |  |
| [defocus](defocus.md) | Defocus value in micrometers |
| [description](description.md) |  |
| [detector_dimensions](detector_dimensions.md) | Detector dimensions in pixels (e |
| [detector_distance_max](detector_distance_max.md) | Maximum detector distance in mm |
| [detector_distance_min](detector_distance_min.md) | Minimum detector distance in mm |
| [detector_type](detector_type.md) | Type of detector |
| [dimensions_x](dimensions_x.md) | Image width in pixels |
| [dimensions_y](dimensions_y.md) | Image height in pixels |
| [dimensions_z](dimensions_z.md) | Image depth in pixels/slices |
| [dose](dose.md) | Electron dose in e-/Å² |
| [dose_per_frame](dose_per_frame.md) | Dose per frame |
| [duration](duration.md) | Storage duration |
| [dwell_time](dwell_time.md) | Dwell time per pixel in milliseconds |
| [elements_measured](elements_measured.md) | Elements detected and measured |
| [emission_filter](emission_filter.md) | Specifications of the emission filter |
| [emission_wavelength](emission_wavelength.md) | Emission wavelength in nanometers |
| [energy_max](energy_max.md) | Maximum X-ray energy in keV |
| [energy_min](energy_min.md) | Minimum X-ray energy in keV |
| [excitation_filter](excitation_filter.md) | Specifications of the excitation filter |
| [excitation_wavelength](excitation_wavelength.md) | Excitation wavelength in nanometers |
| [experiment_code](experiment_code.md) | Unique experiment identifier |
| [experiment_date](experiment_date.md) | Date of the experiment |
| [experiment_id](experiment_id.md) | Reference to the source experiment |
| [experimental_conditions](experimental_conditions.md) | Environmental and experimental conditions |
| [exposure_time](exposure_time.md) | Exposure time in seconds |
| [file_format](file_format.md) | File format |
| [file_name](file_name.md) | Name of the file |
| [file_path](file_path.md) | Path to the file |
| [file_size_bytes](file_size_bytes.md) | File size in bytes |
| [flash_cooling_method](flash_cooling_method.md) | Flash cooling protocol |
| [fluorophore](fluorophore.md) | Name or type of fluorophore used |
| [flux](flux.md) | Photon flux in photons/second |
| [flux_density](flux_density.md) | Photon flux density in photons/s/mm² |
| [frame_rate](frame_rate.md) | Frames per second |
| [goniometer_type](goniometer_type.md) | Type of goniometer |
| [gpu_hours](gpu_hours.md) | GPU hours used |
| [grid_type](grid_type.md) | Type of EM grid used |
| [hole_size](hole_size.md) | Hole size in micrometers |
| [humidity](humidity.md) | Humidity percentage |
| [humidity_percentage](humidity_percentage.md) | Chamber humidity during vitrification |
| [id](id.md) |  |
| [illumination_type](illumination_type.md) | Type of illumination (brightfield, darkfield, phase contrast, DIC) |
| [images](images.md) |  |
| [installation_date](installation_date.md) | Date of instrument installation |
| [instrument_code](instrument_code.md) | Unique identifier code for the instrument |
| [instrument_id](instrument_id.md) | Reference to the instrument used |
| [instrument_runs](instrument_runs.md) |  |
| [keywords](keywords.md) |  |
| [label](label.md) |  |
| [laser_power](laser_power.md) | Laser power in milliwatts or percentage |
| [ligands](ligands.md) | Bound ligands or cofactors |
| [magnification](magnification.md) | Optical magnification factor |
| [manufacturer](manufacturer.md) | Instrument manufacturer |
| [memory_gb](memory_gb.md) | Maximum memory used in GB |
| [model](model.md) | Instrument model |
| [modifications](modifications.md) | Post-translational modifications or chemical modifications |
| [molecular_composition](molecular_composition.md) | Description of molecular composition including sequences, modifications, liga... |
| [molecular_signatures](molecular_signatures.md) | Identified molecular signatures or peaks |
| [molecular_weight](molecular_weight.md) | Molecular weight in kDa |
| [monochromator_type](monochromator_type.md) | Type of monochromator |
| [mounting_method](mounting_method.md) | Crystal mounting method |
| [number_of_scans](number_of_scans.md) | Number of scans averaged for the spectrum |
| [numerical_aperture](numerical_aperture.md) | Numerical aperture of the objective lens |
| [ontology](ontology.md) |  |
| [operator_id](operator_id.md) | Person who performed the preparation |
| [output_files](output_files.md) | Output files generated |
| [parent_sample_id](parent_sample_id.md) | Reference to parent sample for derivation tracking |
| [ph](ph.md) | pH of the buffer |
| [phase_plate](phase_plate.md) | Phase plate available |
| [pinhole_size](pinhole_size.md) | Pinhole size in Airy units for confocal microscopy |
| [pixel_size](pixel_size.md) | Pixel size in Angstroms |
| [pixel_size_max](pixel_size_max.md) | Maximum pixel size in Angstroms per pixel |
| [pixel_size_min](pixel_size_min.md) | Minimum pixel size in Angstroms per pixel |
| [plasma_treatment](plasma_treatment.md) | Plasma treatment details |
| [preparation_date](preparation_date.md) | Date of sample preparation |
| [preparation_method](preparation_method.md) | Method used to prepare the sample |
| [preparation_type](preparation_type.md) | Type of sample preparation |
| [pressure](pressure.md) | Pressure in kPa |
| [processing_level](processing_level.md) | Processing level (0=raw, 1=corrected, 2=derived, 3=model) |
| [processing_parameters](processing_parameters.md) | Parameters used in processing |
| [processing_status](processing_status.md) | Current processing status |
| [protocol_description](protocol_description.md) | Detailed protocol description |
| [purity_percentage](purity_percentage.md) | Sample purity as percentage |
| [q_range_max](q_range_max.md) | Maximum q value in inverse Angstroms |
| [q_range_min](q_range_min.md) | Minimum q value in inverse Angstroms |
| [quality_metrics](quality_metrics.md) | Quality control metrics for the sample |
| [quantum_yield](quantum_yield.md) | Quantum yield of the fluorophore |
| [r_factor](r_factor.md) | R-factor for crystallography |
| [raw_data_location](raw_data_location.md) | Location of raw data files |
| [reconstruction_method](reconstruction_method.md) | Method used for 3D reconstruction |
| [resolution](resolution.md) | Resolution in Angstroms |
| [sample_cell_type](sample_cell_type.md) | Type of sample cell used |
| [sample_changer_capacity](sample_changer_capacity.md) | Number of samples in automatic sample changer |
| [sample_code](sample_code.md) | Unique identifier code for the sample |
| [sample_id](sample_id.md) | Reference to the sample being prepared |
| [sample_preparations](sample_preparations.md) |  |
| [sample_type](sample_type.md) | Type of biological sample |
| [samples](samples.md) |  |
| [sequences](sequences.md) | Amino acid or nucleotide sequences |
| [signal_to_noise](signal_to_noise.md) | Signal to noise ratio |
| [software_name](software_name.md) | Software used for processing |
| [software_version](software_version.md) | Software version |
| [source_type](source_type.md) | Type of X-ray source |
| [spectral_resolution](spectral_resolution.md) | Spectral resolution in cm⁻¹ |
| [started_at](started_at.md) | Workflow start time |
| [storage_conditions](storage_conditions.md) | Storage conditions for the sample |
| [storage_gb](storage_gb.md) | Storage used in GB |
| [studies](studies.md) |  |
| [support_film](support_film.md) | Support film type |
| [technique](technique.md) | Technique used for data collection |
| [temperature](temperature.md) | Storage temperature in Celsius |
| [temperature_control](temperature_control.md) | Temperature control settings |
| [temperature_control_range](temperature_control_range.md) | Temperature control range in Celsius |
| [temperature_unit](temperature_unit.md) | Temperature unit |
| [terms](terms.md) |  |
| [title](title.md) |  |
| [total_dose](total_dose.md) | Total electron dose for cryo-EM |
| [total_frames](total_frames.md) | Total number of frames/images |
| [vitrification_method](vitrification_method.md) | Method used for vitrification |
| [voxel_size](voxel_size.md) | Voxel size in Angstroms |
| [wavenumber_max](wavenumber_max.md) | Maximum wavenumber in cm⁻¹ |
| [wavenumber_min](wavenumber_min.md) | Minimum wavenumber in cm⁻¹ |
| [white_balance](white_balance.md) | White balance settings |
| [workflow_code](workflow_code.md) | Unique workflow identifier |
| [workflow_runs](workflow_runs.md) |  |
| [workflow_type](workflow_type.md) | Type of processing workflow |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CollectionModeEnum](CollectionModeEnum.md) | Data collection modes |
| [ConcentrationUnitEnum](ConcentrationUnitEnum.md) | Units for concentration measurement |
| [CrystallizationMethodEnum](CrystallizationMethodEnum.md) | Methods for protein crystallization |
| [DataTypeEnum](DataTypeEnum.md) | Types of data |
| [DetectorTypeEnum](DetectorTypeEnum.md) | Types of detectors for cryo-EM |
| [FileFormatEnum](FileFormatEnum.md) | File formats |
| [GridTypeEnum](GridTypeEnum.md) | Types of EM grids |
| [IlluminationTypeEnum](IlluminationTypeEnum.md) | Types of illumination for optical microscopy |
| [InstrumentStatusEnum](InstrumentStatusEnum.md) | Operational status of instruments |
| [PreparationTypeEnum](PreparationTypeEnum.md) | Types of sample preparation |
| [ProcessingStatusEnum](ProcessingStatusEnum.md) | Processing status |
| [SampleTypeEnum](SampleTypeEnum.md) | Types of biological samples |
| [TechniqueEnum](TechniqueEnum.md) | Structural biology techniques |
| [TemperatureUnitEnum](TemperatureUnitEnum.md) | Units for temperature measurement |
| [VitrificationMethodEnum](VitrificationMethodEnum.md) | Methods for vitrification |
| [WorkflowTypeEnum](WorkflowTypeEnum.md) | Types of processing workflows |
| [XRaySourceTypeEnum](XRaySourceTypeEnum.md) | Types of X-ray sources |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
