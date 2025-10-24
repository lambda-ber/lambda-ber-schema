-- # Abstract Class: NamedThing Description: A named thing
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Abstract Class: AttributeGroup Description: A grouping of related data attributes that form a logical unit
--     * Slot: id
--     * Slot: description
-- # Class: Dataset Description: A collection of studies
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: Study Description: A focused research investigation that groups related samples, experiments, and data collection around a specific biological question or hypothesis
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: Sample Description: A biological sample used in structural biology experiments
--     * Slot: sample_code Description: Human-friendly laboratory identifier or facility code for the sample (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference and tracking within laboratory workflows.
--     * Slot: sample_type Description: Type of biological sample
--     * Slot: molecular_weight Description: Molecular weight in kDa
--     * Slot: concentration Description: Sample concentration in mg/mL or µM
--     * Slot: concentration_unit Description: Unit of concentration measurement
--     * Slot: preparation_method Description: Method used to prepare the sample
--     * Slot: organism Description: Source organism for the sample (e.g., NCBITaxon:3702 for Arabidopsis thaliana)
--     * Slot: anatomy Description: Anatomical part or tissue (e.g., UBERON:0008945 for leaf)
--     * Slot: cell_type Description: Cell type if applicable (e.g., CL:0000057 for fibroblast)
--     * Slot: parent_sample_id Description: Reference to parent sample for derivation tracking
--     * Slot: purity_percentage Description: Sample purity as percentage
--     * Slot: quality_metrics Description: Quality control metrics for the sample
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: molecular_composition_id Description: Description of molecular composition including sequences, modifications, ligands
--     * Slot: buffer_composition_id Description: Buffer composition including pH, salts, additives
--     * Slot: storage_conditions_id Description: Storage conditions for the sample
-- # Class: SamplePreparation Description: A process that prepares a sample for imaging
--     * Slot: preparation_type Description: Type of sample preparation
--     * Slot: sample_id Description: Reference to the sample being prepared
--     * Slot: preparation_date Description: Date of sample preparation
--     * Slot: operator_id Description: Identifier or name of the person who performed the sample preparation (e.g., 'jsmith', 'John Smith', or personnel ID)
--     * Slot: protocol_description Description: Detailed protocol description
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
--     * Slot: Study_id Description: Autocreated FK slot
-- # Class: Instrument Description: An instrument used to collect data
--     * Slot: instrument_code Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
--     * Slot: manufacturer Description: Instrument manufacturer
--     * Slot: model Description: Instrument model
--     * Slot: installation_date Description: Date of instrument installation
--     * Slot: current_status Description: Current operational status
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: CryoEMInstrument Description: Cryo-EM microscope specifications
--     * Slot: accelerating_voltage Description: Accelerating voltage in kV
--     * Slot: cs_corrector Description: Spherical aberration corrector present
--     * Slot: phase_plate Description: Phase plate available
--     * Slot: detector_type Description: Type of detector
--     * Slot: detector_dimensions Description: Detector dimensions in pixels (e.g., 4096x4096)
--     * Slot: pixel_size_min Description: Minimum pixel size in Angstroms per pixel
--     * Slot: pixel_size_max Description: Maximum pixel size in Angstroms per pixel
--     * Slot: autoloader_capacity Description: Number of grids the autoloader can hold
--     * Slot: instrument_code Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
--     * Slot: manufacturer Description: Instrument manufacturer
--     * Slot: model Description: Instrument model
--     * Slot: installation_date Description: Date of instrument installation
--     * Slot: current_status Description: Current operational status
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: XRayInstrument Description: X-ray diffractometer or synchrotron beamline specifications
--     * Slot: source_type Description: Type of X-ray source
--     * Slot: energy_min Description: Minimum X-ray energy in keV
--     * Slot: energy_max Description: Maximum X-ray energy in keV
--     * Slot: beam_size_min Description: Minimum beam size in micrometers
--     * Slot: beam_size_max Description: Maximum beam size in micrometers
--     * Slot: flux_density Description: Photon flux density in photons/s/mm²
--     * Slot: monochromator_type Description: Type of monochromator
--     * Slot: goniometer_type Description: Type of goniometer
--     * Slot: crystal_cooling_capability Description: Crystal cooling system available
--     * Slot: instrument_code Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
--     * Slot: manufacturer Description: Instrument manufacturer
--     * Slot: model Description: Instrument model
--     * Slot: installation_date Description: Date of instrument installation
--     * Slot: current_status Description: Current operational status
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: SAXSInstrument Description: SAXS/WAXS instrument specifications
--     * Slot: q_range_min Description: Minimum q value in inverse Angstroms
--     * Slot: q_range_max Description: Maximum q value in inverse Angstroms
--     * Slot: detector_distance_min Description: Minimum detector distance in mm
--     * Slot: detector_distance_max Description: Maximum detector distance in mm
--     * Slot: sample_changer_capacity Description: Number of samples in automatic sample changer
--     * Slot: temperature_control_range Description: Temperature control range in Celsius
--     * Slot: instrument_code Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
--     * Slot: manufacturer Description: Instrument manufacturer
--     * Slot: model Description: Instrument model
--     * Slot: installation_date Description: Date of instrument installation
--     * Slot: current_status Description: Current operational status
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: ExperimentRun Description: An experimental data collection session
--     * Slot: experiment_code Description: Human-friendly laboratory or facility identifier for the experiment (e.g., 'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and cross-referencing within laboratory systems.
--     * Slot: sample_id Description: Reference to the sample being analyzed
--     * Slot: instrument_id Description: Reference to the instrument used
--     * Slot: experiment_date Description: Date of the experiment
--     * Slot: operator_id Description: Identifier or name of the person who performed the experiment data collection (e.g., 'jsmith', 'John Smith', or personnel ID)
--     * Slot: technique Description: Technique used for data collection
--     * Slot: raw_data_location Description: Location of raw data files
--     * Slot: processing_status Description: Current processing status
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: experimental_conditions_id Description: Environmental and experimental conditions
--     * Slot: data_collection_strategy_id Description: Strategy for data collection
--     * Slot: quality_metrics_id Description: Quality metrics for the experiment
-- # Class: WorkflowRun Description: A computational processing workflow execution
--     * Slot: workflow_code Description: Human-friendly identifier for the computational workflow run (e.g., 'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing pipelines and computational provenance.
--     * Slot: workflow_type Description: Type of processing workflow
--     * Slot: experiment_id Description: Reference to the source experiment
--     * Slot: processing_level Description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
--     * Slot: software_name Description: Software used for processing
--     * Slot: software_version Description: Software version
--     * Slot: processing_parameters Description: Parameters used in processing
--     * Slot: started_at Description: Workflow start time
--     * Slot: completed_at Description: Workflow completion time
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: compute_resources_id Description: Computational resources used
-- # Class: DataFile Description: A data file generated or used in the study
--     * Slot: file_name Description: Name of the file
--     * Slot: file_path Description: Path to the file
--     * Slot: file_format Description: File format
--     * Slot: file_size_bytes Description: File size in bytes
--     * Slot: checksum Description: SHA-256 checksum for data integrity
--     * Slot: creation_date Description: File creation date
--     * Slot: data_type Description: Type of data in the file
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
--     * Slot: Study_id Description: Autocreated FK slot
-- # Class: Image Description: An image file from structural biology experiments
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: pixel_size Description: Pixel size in Angstroms
--     * Slot: dimensions_x Description: Image width in pixels
--     * Slot: dimensions_y Description: Image height in pixels
--     * Slot: exposure_time Description: Exposure time in seconds
--     * Slot: dose Description: Electron dose in e-/Å²
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
--     * Slot: Study_id Description: Autocreated FK slot
-- # Class: Image2D Description: A 2D image (micrograph, diffraction pattern)
--     * Slot: defocus Description: Defocus value in micrometers
--     * Slot: astigmatism Description: Astigmatism value
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: pixel_size Description: Pixel size in Angstroms
--     * Slot: dimensions_x Description: Image width in pixels
--     * Slot: dimensions_y Description: Image height in pixels
--     * Slot: exposure_time Description: Exposure time in seconds
--     * Slot: dose Description: Electron dose in e-/Å²
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: Image3D Description: A 3D volume or tomogram
--     * Slot: dimensions_z Description: Image depth in pixels/slices
--     * Slot: voxel_size Description: Voxel size in Angstroms
--     * Slot: reconstruction_method Description: Method used for 3D reconstruction
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: pixel_size Description: Pixel size in Angstroms
--     * Slot: dimensions_x Description: Image width in pixels
--     * Slot: dimensions_y Description: Image height in pixels
--     * Slot: exposure_time Description: Exposure time in seconds
--     * Slot: dose Description: Electron dose in e-/Å²
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: FTIRImage Description: Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy
--     * Slot: wavenumber_min Description: Minimum wavenumber in cm⁻¹
--     * Slot: wavenumber_max Description: Maximum wavenumber in cm⁻¹
--     * Slot: spectral_resolution Description: Spectral resolution in cm⁻¹
--     * Slot: number_of_scans Description: Number of scans averaged for the spectrum
--     * Slot: apodization_function Description: Mathematical function used for apodization
--     * Slot: background_correction Description: Method used for background correction
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: pixel_size Description: Pixel size in Angstroms
--     * Slot: dimensions_x Description: Image width in pixels
--     * Slot: dimensions_y Description: Image height in pixels
--     * Slot: exposure_time Description: Exposure time in seconds
--     * Slot: dose Description: Electron dose in e-/Å²
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: FluorescenceImage Description: Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
--     * Slot: excitation_wavelength Description: Excitation wavelength in nanometers
--     * Slot: emission_wavelength Description: Emission wavelength in nanometers
--     * Slot: excitation_filter Description: Specifications of the excitation filter
--     * Slot: emission_filter Description: Specifications of the emission filter
--     * Slot: fluorophore Description: Name or type of fluorophore used
--     * Slot: channel_name Description: Name of the fluorescence channel (e.g., DAPI, GFP, RFP)
--     * Slot: laser_power Description: Laser power in milliwatts or percentage
--     * Slot: pinhole_size Description: Pinhole size in Airy units for confocal microscopy
--     * Slot: quantum_yield Description: Quantum yield of the fluorophore
--     * Slot: defocus Description: Defocus value in micrometers
--     * Slot: astigmatism Description: Astigmatism value
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: pixel_size Description: Pixel size in Angstroms
--     * Slot: dimensions_x Description: Image width in pixels
--     * Slot: dimensions_y Description: Image height in pixels
--     * Slot: exposure_time Description: Exposure time in seconds
--     * Slot: dose Description: Electron dose in e-/Å²
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: OpticalImage Description: Visible light optical microscopy or photography image
--     * Slot: illumination_type Description: Type of illumination (brightfield, darkfield, phase contrast, DIC)
--     * Slot: magnification Description: Optical magnification factor
--     * Slot: numerical_aperture Description: Numerical aperture of the objective lens
--     * Slot: white_balance Description: White balance settings
--     * Slot: contrast_method Description: Contrast enhancement method used
--     * Slot: defocus Description: Defocus value in micrometers
--     * Slot: astigmatism Description: Astigmatism value
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: pixel_size Description: Pixel size in Angstroms
--     * Slot: dimensions_x Description: Image width in pixels
--     * Slot: dimensions_y Description: Image height in pixels
--     * Slot: exposure_time Description: Exposure time in seconds
--     * Slot: dose Description: Electron dose in e-/Å²
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: XRFImage Description: X-ray fluorescence (XRF) image showing elemental distribution
--     * Slot: beam_energy Description: X-ray beam energy in keV
--     * Slot: beam_size Description: X-ray beam size in micrometers
--     * Slot: dwell_time Description: Dwell time per pixel in milliseconds
--     * Slot: source_type Description: X-ray source type (synchrotron or lab-source)
--     * Slot: detector_type Description: Type of X-ray detector used
--     * Slot: flux Description: Photon flux in photons/second
--     * Slot: calibration_standard Description: Reference standard used for calibration
--     * Slot: defocus Description: Defocus value in micrometers
--     * Slot: astigmatism Description: Astigmatism value
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: pixel_size Description: Pixel size in Angstroms
--     * Slot: dimensions_x Description: Image width in pixels
--     * Slot: dimensions_y Description: Image height in pixels
--     * Slot: exposure_time Description: Exposure time in seconds
--     * Slot: dose Description: Electron dose in e-/Å²
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: ImageFeature Description: Semantic annotations describing features identified in images using controlled vocabulary terms
--     * Slot: id
--     * Slot: terms
--     * Slot: description
-- # Class: OntologyTerm
--     * Slot: label
--     * Slot: definition
--     * Slot: ontology
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title
--     * Slot: description
-- # Class: MolecularComposition Description: Molecular composition of a sample
--     * Slot: id
--     * Slot: description
-- # Class: BufferComposition Description: Buffer composition for sample storage
--     * Slot: id
--     * Slot: ph Description: pH of the buffer
--     * Slot: description
-- # Class: StorageConditions Description: Storage conditions for samples
--     * Slot: id
--     * Slot: temperature Description: Storage temperature in Celsius
--     * Slot: temperature_unit Description: Temperature unit
--     * Slot: duration Description: Storage duration
--     * Slot: atmosphere Description: Storage atmosphere conditions
--     * Slot: description
-- # Abstract Class: TechniqueSpecificPreparation Description: Base class for technique-specific preparation details
--     * Slot: id
--     * Slot: description
-- # Class: CryoEMPreparation Description: Cryo-EM specific sample preparation
--     * Slot: id
--     * Slot: grid_type Description: Type of EM grid used
--     * Slot: support_film Description: Support film type
--     * Slot: hole_size Description: Hole size in micrometers
--     * Slot: vitrification_method Description: Method used for vitrification
--     * Slot: blot_time Description: Blotting time in seconds
--     * Slot: blot_force Description: Blotting force setting
--     * Slot: humidity_percentage Description: Chamber humidity during vitrification
--     * Slot: chamber_temperature Description: Chamber temperature in Celsius
--     * Slot: plasma_treatment Description: Plasma treatment details
--     * Slot: description
-- # Class: XRayPreparation Description: X-ray crystallography specific preparation
--     * Slot: id
--     * Slot: crystallization_method Description: Method used for crystallization
--     * Slot: crystallization_conditions Description: Detailed crystallization conditions
--     * Slot: crystal_size Description: Crystal dimensions in micrometers
--     * Slot: cryoprotectant Description: Cryoprotectant used
--     * Slot: cryoprotectant_concentration Description: Cryoprotectant concentration percentage
--     * Slot: mounting_method Description: Crystal mounting method
--     * Slot: flash_cooling_method Description: Flash cooling protocol
--     * Slot: description
-- # Class: SAXSPreparation Description: SAXS/WAXS specific preparation
--     * Slot: id
--     * Slot: buffer_matching_protocol Description: Protocol for buffer matching
--     * Slot: sample_cell_type Description: Type of sample cell used
--     * Slot: cell_path_length Description: Path length in mm
--     * Slot: temperature_control Description: Temperature control settings
--     * Slot: description
-- # Class: ExperimentalConditions Description: Environmental and experimental conditions
--     * Slot: id
--     * Slot: temperature Description: Temperature in Celsius
--     * Slot: humidity Description: Humidity percentage
--     * Slot: pressure Description: Pressure in kPa
--     * Slot: atmosphere Description: Atmosphere composition
--     * Slot: beam_energy Description: Beam energy in keV
--     * Slot: exposure_time Description: Exposure time in seconds
--     * Slot: description
-- # Class: DataCollectionStrategy Description: Strategy for data collection
--     * Slot: id
--     * Slot: collection_mode Description: Mode of data collection
--     * Slot: total_frames Description: Total number of frames/images
--     * Slot: frame_rate Description: Frames per second
--     * Slot: total_dose Description: Total electron dose for cryo-EM
--     * Slot: dose_per_frame Description: Dose per frame
--     * Slot: description
-- # Class: QualityMetrics Description: Quality metrics for experiments
--     * Slot: id
--     * Slot: resolution Description: Resolution in Angstroms
--     * Slot: completeness Description: Data completeness percentage
--     * Slot: signal_to_noise Description: Signal to noise ratio
--     * Slot: r_factor Description: R-factor for crystallography
--     * Slot: i_zero Description: Forward scattering intensity I(0)
--     * Slot: rg Description: Radius of gyration in Angstroms
--     * Slot: description
-- # Class: ComputeResources Description: Computational resources used
--     * Slot: id
--     * Slot: cpu_hours Description: CPU hours used
--     * Slot: gpu_hours Description: GPU hours used
--     * Slot: memory_gb Description: Maximum memory used in GB
--     * Slot: storage_gb Description: Storage used in GB
--     * Slot: description
-- # Class: Dataset_keywords
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: keywords
-- # Class: WorkflowRun_output_files
--     * Slot: WorkflowRun_id Description: Autocreated FK slot
--     * Slot: output_files_id Description: Output files generated
-- # Class: FTIRImage_molecular_signatures
--     * Slot: FTIRImage_id Description: Autocreated FK slot
--     * Slot: molecular_signatures Description: Identified molecular signatures or peaks
-- # Class: OpticalImage_color_channels
--     * Slot: OpticalImage_id Description: Autocreated FK slot
--     * Slot: color_channels Description: Color channels present (e.g., RGB, grayscale)
-- # Class: XRFImage_elements_measured
--     * Slot: XRFImage_id Description: Autocreated FK slot
--     * Slot: elements_measured Description: Elements detected and measured
-- # Class: MolecularComposition_sequences
--     * Slot: MolecularComposition_id Description: Autocreated FK slot
--     * Slot: sequences Description: Amino acid or nucleotide sequences
-- # Class: MolecularComposition_modifications
--     * Slot: MolecularComposition_id Description: Autocreated FK slot
--     * Slot: modifications Description: Post-translational modifications or chemical modifications
-- # Class: MolecularComposition_ligands
--     * Slot: MolecularComposition_id Description: Autocreated FK slot
--     * Slot: ligands Description: Bound ligands or cofactors
-- # Class: BufferComposition_components
--     * Slot: BufferComposition_id Description: Autocreated FK slot
--     * Slot: components Description: Buffer components and their concentrations
-- # Class: BufferComposition_additives
--     * Slot: BufferComposition_id Description: Autocreated FK slot
--     * Slot: additives Description: Additional additives in the buffer
-- # Class: SAXSPreparation_concentration_series
--     * Slot: SAXSPreparation_id Description: Autocreated FK slot
--     * Slot: concentration_series Description: Concentration values for series measurements

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NamedThing_id" ON "NamedThing" (id);
CREATE TABLE "AttributeGroup" (
	id INTEGER NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_AttributeGroup_id" ON "AttributeGroup" (id);
CREATE TABLE "Dataset" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);
CREATE TABLE "CryoEMInstrument" (
	accelerating_voltage INTEGER,
	cs_corrector BOOLEAN,
	phase_plate BOOLEAN,
	detector_type VARCHAR(15),
	detector_dimensions TEXT,
	pixel_size_min FLOAT,
	pixel_size_max FLOAT,
	autoloader_capacity INTEGER,
	instrument_code TEXT NOT NULL,
	manufacturer TEXT,
	model TEXT,
	installation_date TEXT,
	current_status VARCHAR(13),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CryoEMInstrument_id" ON "CryoEMInstrument" (id);
CREATE TABLE "XRayInstrument" (
	source_type VARCHAR(14),
	energy_min FLOAT,
	energy_max FLOAT,
	beam_size_min FLOAT,
	beam_size_max FLOAT,
	flux_density FLOAT,
	monochromator_type TEXT,
	goniometer_type TEXT,
	crystal_cooling_capability BOOLEAN,
	instrument_code TEXT NOT NULL,
	manufacturer TEXT,
	model TEXT,
	installation_date TEXT,
	current_status VARCHAR(13),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_XRayInstrument_id" ON "XRayInstrument" (id);
CREATE TABLE "SAXSInstrument" (
	q_range_min FLOAT,
	q_range_max FLOAT,
	detector_distance_min FLOAT,
	detector_distance_max FLOAT,
	sample_changer_capacity INTEGER,
	temperature_control_range TEXT,
	instrument_code TEXT NOT NULL,
	manufacturer TEXT,
	model TEXT,
	installation_date TEXT,
	current_status VARCHAR(13),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SAXSInstrument_id" ON "SAXSInstrument" (id);
CREATE TABLE "Image2D" (
	defocus FLOAT,
	astigmatism FLOAT,
	file_name TEXT NOT NULL,
	acquisition_date TEXT,
	pixel_size FLOAT,
	dimensions_x INTEGER,
	dimensions_y INTEGER,
	exposure_time FLOAT,
	dose FLOAT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Image2D_id" ON "Image2D" (id);
CREATE TABLE "Image3D" (
	dimensions_z INTEGER,
	voxel_size FLOAT,
	reconstruction_method TEXT,
	file_name TEXT NOT NULL,
	acquisition_date TEXT,
	pixel_size FLOAT,
	dimensions_x INTEGER,
	dimensions_y INTEGER,
	exposure_time FLOAT,
	dose FLOAT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Image3D_id" ON "Image3D" (id);
CREATE TABLE "FTIRImage" (
	wavenumber_min FLOAT,
	wavenumber_max FLOAT,
	spectral_resolution FLOAT,
	number_of_scans INTEGER,
	apodization_function TEXT,
	background_correction TEXT,
	file_name TEXT NOT NULL,
	acquisition_date TEXT,
	pixel_size FLOAT,
	dimensions_x INTEGER,
	dimensions_y INTEGER,
	exposure_time FLOAT,
	dose FLOAT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FTIRImage_id" ON "FTIRImage" (id);
CREATE TABLE "FluorescenceImage" (
	excitation_wavelength FLOAT,
	emission_wavelength FLOAT,
	excitation_filter TEXT,
	emission_filter TEXT,
	fluorophore TEXT,
	channel_name TEXT,
	laser_power FLOAT,
	pinhole_size FLOAT,
	quantum_yield FLOAT,
	defocus FLOAT,
	astigmatism FLOAT,
	file_name TEXT NOT NULL,
	acquisition_date TEXT,
	pixel_size FLOAT,
	dimensions_x INTEGER,
	dimensions_y INTEGER,
	exposure_time FLOAT,
	dose FLOAT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_FluorescenceImage_id" ON "FluorescenceImage" (id);
CREATE TABLE "OpticalImage" (
	illumination_type VARCHAR(14),
	magnification FLOAT,
	numerical_aperture FLOAT,
	white_balance TEXT,
	contrast_method TEXT,
	defocus FLOAT,
	astigmatism FLOAT,
	file_name TEXT NOT NULL,
	acquisition_date TEXT,
	pixel_size FLOAT,
	dimensions_x INTEGER,
	dimensions_y INTEGER,
	exposure_time FLOAT,
	dose FLOAT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_OpticalImage_id" ON "OpticalImage" (id);
CREATE TABLE "XRFImage" (
	beam_energy FLOAT,
	beam_size FLOAT,
	dwell_time FLOAT,
	source_type VARCHAR(14),
	detector_type TEXT,
	flux FLOAT,
	calibration_standard TEXT,
	defocus FLOAT,
	astigmatism FLOAT,
	file_name TEXT NOT NULL,
	acquisition_date TEXT,
	pixel_size FLOAT,
	dimensions_x INTEGER,
	dimensions_y INTEGER,
	exposure_time FLOAT,
	dose FLOAT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_XRFImage_id" ON "XRFImage" (id);
CREATE TABLE "OntologyTerm" (
	label TEXT,
	definition TEXT,
	ontology TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_OntologyTerm_id" ON "OntologyTerm" (id);
CREATE TABLE "MolecularComposition" (
	id INTEGER NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MolecularComposition_id" ON "MolecularComposition" (id);
CREATE TABLE "BufferComposition" (
	id INTEGER NOT NULL,
	ph FLOAT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_BufferComposition_id" ON "BufferComposition" (id);
CREATE TABLE "StorageConditions" (
	id INTEGER NOT NULL,
	temperature FLOAT,
	temperature_unit VARCHAR(10),
	duration TEXT,
	atmosphere TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_StorageConditions_id" ON "StorageConditions" (id);
CREATE TABLE "TechniqueSpecificPreparation" (
	id INTEGER NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TechniqueSpecificPreparation_id" ON "TechniqueSpecificPreparation" (id);
CREATE TABLE "CryoEMPreparation" (
	id INTEGER NOT NULL,
	grid_type VARCHAR(16),
	support_film TEXT,
	hole_size FLOAT,
	vitrification_method VARCHAR(22),
	blot_time FLOAT,
	blot_force INTEGER,
	humidity_percentage FLOAT,
	chamber_temperature FLOAT,
	plasma_treatment TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_CryoEMPreparation_id" ON "CryoEMPreparation" (id);
CREATE TABLE "XRayPreparation" (
	id INTEGER NOT NULL,
	crystallization_method VARCHAR(24),
	crystallization_conditions TEXT,
	crystal_size TEXT,
	cryoprotectant TEXT,
	cryoprotectant_concentration FLOAT,
	mounting_method TEXT,
	flash_cooling_method TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_XRayPreparation_id" ON "XRayPreparation" (id);
CREATE TABLE "SAXSPreparation" (
	id INTEGER NOT NULL,
	buffer_matching_protocol TEXT,
	sample_cell_type TEXT,
	cell_path_length FLOAT,
	temperature_control TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SAXSPreparation_id" ON "SAXSPreparation" (id);
CREATE TABLE "ExperimentalConditions" (
	id INTEGER NOT NULL,
	temperature FLOAT,
	humidity FLOAT,
	pressure FLOAT,
	atmosphere TEXT,
	beam_energy FLOAT,
	exposure_time FLOAT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ExperimentalConditions_id" ON "ExperimentalConditions" (id);
CREATE TABLE "DataCollectionStrategy" (
	id INTEGER NOT NULL,
	collection_mode VARCHAR(16),
	total_frames INTEGER,
	frame_rate FLOAT,
	total_dose FLOAT,
	dose_per_frame FLOAT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_DataCollectionStrategy_id" ON "DataCollectionStrategy" (id);
CREATE TABLE "QualityMetrics" (
	id INTEGER NOT NULL,
	resolution FLOAT,
	completeness FLOAT,
	signal_to_noise FLOAT,
	r_factor FLOAT,
	i_zero FLOAT,
	rg FLOAT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_QualityMetrics_id" ON "QualityMetrics" (id);
CREATE TABLE "ComputeResources" (
	id INTEGER NOT NULL,
	cpu_hours FLOAT,
	gpu_hours FLOAT,
	memory_gb FLOAT,
	storage_gb FLOAT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ComputeResources_id" ON "ComputeResources" (id);
CREATE TABLE "Study" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Study_id" ON "Study" (id);
CREATE TABLE "Instrument" (
	instrument_code TEXT NOT NULL,
	manufacturer TEXT,
	model TEXT,
	installation_date TEXT,
	current_status VARCHAR(13),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Instrument_id" ON "Instrument" (id);
CREATE TABLE "ImageFeature" (
	id INTEGER NOT NULL,
	terms TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(terms) REFERENCES "OntologyTerm" (id)
);CREATE INDEX "ix_ImageFeature_id" ON "ImageFeature" (id);
CREATE TABLE "Dataset_keywords" (
	"Dataset_id" TEXT,
	keywords TEXT,
	PRIMARY KEY ("Dataset_id", keywords),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Dataset_keywords_Dataset_id" ON "Dataset_keywords" ("Dataset_id");CREATE INDEX "ix_Dataset_keywords_keywords" ON "Dataset_keywords" (keywords);
CREATE TABLE "FTIRImage_molecular_signatures" (
	"FTIRImage_id" TEXT,
	molecular_signatures TEXT,
	PRIMARY KEY ("FTIRImage_id", molecular_signatures),
	FOREIGN KEY("FTIRImage_id") REFERENCES "FTIRImage" (id)
);CREATE INDEX "ix_FTIRImage_molecular_signatures_molecular_signatures" ON "FTIRImage_molecular_signatures" (molecular_signatures);CREATE INDEX "ix_FTIRImage_molecular_signatures_FTIRImage_id" ON "FTIRImage_molecular_signatures" ("FTIRImage_id");
CREATE TABLE "OpticalImage_color_channels" (
	"OpticalImage_id" TEXT,
	color_channels TEXT,
	PRIMARY KEY ("OpticalImage_id", color_channels),
	FOREIGN KEY("OpticalImage_id") REFERENCES "OpticalImage" (id)
);CREATE INDEX "ix_OpticalImage_color_channels_color_channels" ON "OpticalImage_color_channels" (color_channels);CREATE INDEX "ix_OpticalImage_color_channels_OpticalImage_id" ON "OpticalImage_color_channels" ("OpticalImage_id");
CREATE TABLE "XRFImage_elements_measured" (
	"XRFImage_id" TEXT,
	elements_measured TEXT,
	PRIMARY KEY ("XRFImage_id", elements_measured),
	FOREIGN KEY("XRFImage_id") REFERENCES "XRFImage" (id)
);CREATE INDEX "ix_XRFImage_elements_measured_elements_measured" ON "XRFImage_elements_measured" (elements_measured);CREATE INDEX "ix_XRFImage_elements_measured_XRFImage_id" ON "XRFImage_elements_measured" ("XRFImage_id");
CREATE TABLE "MolecularComposition_sequences" (
	"MolecularComposition_id" INTEGER,
	sequences TEXT,
	PRIMARY KEY ("MolecularComposition_id", sequences),
	FOREIGN KEY("MolecularComposition_id") REFERENCES "MolecularComposition" (id)
);CREATE INDEX "ix_MolecularComposition_sequences_MolecularComposition_id" ON "MolecularComposition_sequences" ("MolecularComposition_id");CREATE INDEX "ix_MolecularComposition_sequences_sequences" ON "MolecularComposition_sequences" (sequences);
CREATE TABLE "MolecularComposition_modifications" (
	"MolecularComposition_id" INTEGER,
	modifications TEXT,
	PRIMARY KEY ("MolecularComposition_id", modifications),
	FOREIGN KEY("MolecularComposition_id") REFERENCES "MolecularComposition" (id)
);CREATE INDEX "ix_MolecularComposition_modifications_modifications" ON "MolecularComposition_modifications" (modifications);CREATE INDEX "ix_MolecularComposition_modifications_MolecularComposition_id" ON "MolecularComposition_modifications" ("MolecularComposition_id");
CREATE TABLE "MolecularComposition_ligands" (
	"MolecularComposition_id" INTEGER,
	ligands TEXT,
	PRIMARY KEY ("MolecularComposition_id", ligands),
	FOREIGN KEY("MolecularComposition_id") REFERENCES "MolecularComposition" (id)
);CREATE INDEX "ix_MolecularComposition_ligands_MolecularComposition_id" ON "MolecularComposition_ligands" ("MolecularComposition_id");CREATE INDEX "ix_MolecularComposition_ligands_ligands" ON "MolecularComposition_ligands" (ligands);
CREATE TABLE "BufferComposition_components" (
	"BufferComposition_id" INTEGER,
	components TEXT,
	PRIMARY KEY ("BufferComposition_id", components),
	FOREIGN KEY("BufferComposition_id") REFERENCES "BufferComposition" (id)
);CREATE INDEX "ix_BufferComposition_components_BufferComposition_id" ON "BufferComposition_components" ("BufferComposition_id");CREATE INDEX "ix_BufferComposition_components_components" ON "BufferComposition_components" (components);
CREATE TABLE "BufferComposition_additives" (
	"BufferComposition_id" INTEGER,
	additives TEXT,
	PRIMARY KEY ("BufferComposition_id", additives),
	FOREIGN KEY("BufferComposition_id") REFERENCES "BufferComposition" (id)
);CREATE INDEX "ix_BufferComposition_additives_BufferComposition_id" ON "BufferComposition_additives" ("BufferComposition_id");CREATE INDEX "ix_BufferComposition_additives_additives" ON "BufferComposition_additives" (additives);
CREATE TABLE "SAXSPreparation_concentration_series" (
	"SAXSPreparation_id" INTEGER,
	concentration_series FLOAT,
	PRIMARY KEY ("SAXSPreparation_id", concentration_series),
	FOREIGN KEY("SAXSPreparation_id") REFERENCES "SAXSPreparation" (id)
);CREATE INDEX "ix_SAXSPreparation_concentration_series_SAXSPreparation_id" ON "SAXSPreparation_concentration_series" ("SAXSPreparation_id");CREATE INDEX "ix_SAXSPreparation_concentration_series_concentration_series" ON "SAXSPreparation_concentration_series" (concentration_series);
CREATE TABLE "Sample" (
	sample_code TEXT NOT NULL,
	sample_type VARCHAR(16) NOT NULL,
	molecular_weight FLOAT,
	concentration FLOAT,
	concentration_unit VARCHAR(10),
	preparation_method TEXT,
	organism TEXT,
	anatomy TEXT,
	cell_type TEXT,
	parent_sample_id TEXT,
	purity_percentage FLOAT,
	quality_metrics TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Study_id" TEXT,
	molecular_composition_id INTEGER,
	buffer_composition_id INTEGER,
	storage_conditions_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(organism) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(anatomy) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(cell_type) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(parent_sample_id) REFERENCES "Sample" (id),
	FOREIGN KEY("Study_id") REFERENCES "Study" (id),
	FOREIGN KEY(molecular_composition_id) REFERENCES "MolecularComposition" (id),
	FOREIGN KEY(buffer_composition_id) REFERENCES "BufferComposition" (id),
	FOREIGN KEY(storage_conditions_id) REFERENCES "StorageConditions" (id)
);CREATE INDEX "ix_Sample_id" ON "Sample" (id);
CREATE TABLE "SamplePreparation" (
	preparation_type VARCHAR(20) NOT NULL,
	sample_id TEXT NOT NULL,
	preparation_date TEXT,
	operator_id TEXT,
	protocol_description TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Study_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);CREATE INDEX "ix_SamplePreparation_id" ON "SamplePreparation" (id);
CREATE TABLE "ExperimentRun" (
	experiment_code TEXT NOT NULL,
	sample_id TEXT NOT NULL,
	instrument_id TEXT NOT NULL,
	experiment_date TEXT,
	operator_id TEXT,
	technique VARCHAR(20) NOT NULL,
	raw_data_location TEXT,
	processing_status VARCHAR(13),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Study_id" TEXT,
	experimental_conditions_id INTEGER,
	data_collection_strategy_id INTEGER,
	quality_metrics_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(instrument_id) REFERENCES "Instrument" (id),
	FOREIGN KEY("Study_id") REFERENCES "Study" (id),
	FOREIGN KEY(experimental_conditions_id) REFERENCES "ExperimentalConditions" (id),
	FOREIGN KEY(data_collection_strategy_id) REFERENCES "DataCollectionStrategy" (id),
	FOREIGN KEY(quality_metrics_id) REFERENCES "QualityMetrics" (id)
);CREATE INDEX "ix_ExperimentRun_id" ON "ExperimentRun" (id);
CREATE TABLE "WorkflowRun" (
	workflow_code TEXT NOT NULL,
	workflow_type VARCHAR(23) NOT NULL,
	experiment_id TEXT NOT NULL,
	processing_level INTEGER,
	software_name TEXT NOT NULL,
	software_version TEXT,
	processing_parameters TEXT,
	started_at TEXT,
	completed_at TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Study_id" TEXT,
	compute_resources_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Study_id") REFERENCES "Study" (id),
	FOREIGN KEY(compute_resources_id) REFERENCES "ComputeResources" (id)
);CREATE INDEX "ix_WorkflowRun_id" ON "WorkflowRun" (id);
CREATE TABLE "DataFile" (
	file_name TEXT NOT NULL,
	file_path TEXT,
	file_format VARCHAR(10) NOT NULL,
	file_size_bytes INTEGER,
	checksum TEXT,
	creation_date TEXT,
	data_type VARCHAR(14),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Study_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);CREATE INDEX "ix_DataFile_id" ON "DataFile" (id);
CREATE TABLE "Image" (
	file_name TEXT NOT NULL,
	acquisition_date TEXT,
	pixel_size FLOAT,
	dimensions_x INTEGER,
	dimensions_y INTEGER,
	exposure_time FLOAT,
	dose FLOAT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Study_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);CREATE INDEX "ix_Image_id" ON "Image" (id);
CREATE TABLE "WorkflowRun_output_files" (
	"WorkflowRun_id" TEXT,
	output_files_id TEXT,
	PRIMARY KEY ("WorkflowRun_id", output_files_id),
	FOREIGN KEY("WorkflowRun_id") REFERENCES "WorkflowRun" (id),
	FOREIGN KEY(output_files_id) REFERENCES "DataFile" (id)
);CREATE INDEX "ix_WorkflowRun_output_files_WorkflowRun_id" ON "WorkflowRun_output_files" ("WorkflowRun_id");CREATE INDEX "ix_WorkflowRun_output_files_output_files_id" ON "WorkflowRun_output_files" (output_files_id);
