
# lambda-ber-schema


**metamodel version:** 1.7.0

**version:** 0.1.1.post15.dev0+b4e2533


lambda-ber-schema is a comprehensive schema for representing multimodal structural biology imaging data, 
from atomic-resolution structures to tissue-level organization. It supports diverse experimental 
techniques including cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and 
spectroscopic imaging.

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


### Classes

 * [Any](Any.md)
 * [Attribute](Attribute.md) - A domain, measurement, attribute, property, or any descriptor for additional properties to be added to an entity. Where available, please use OBO Foundry ontologies or other controlled vocabularies for attributes; the label should be the term name from the ontology and the id should be the fully-qualified CURIE.
 * [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit
     * [BiophysicalProperty](BiophysicalProperty.md) - Measured or calculated biophysical properties
     * [BufferComposition](BufferComposition.md) - Buffer composition for sample storage
     * [CTFEstimationParameters](CTFEstimationParameters.md) - Parameters specific to CTF estimation workflows
     * [ComputeResources](ComputeResources.md) - Computational resources used
     * [ConformationalState](ConformationalState.md) - Individual conformational state
     * [CrystallizationConditions](CrystallizationConditions.md) - Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization mapping)
     * [DataCollectionStrategy](DataCollectionStrategy.md) - Strategy for data collection
     * [DatabaseCrossReference](DatabaseCrossReference.md) - Cross-references to external databases
     * [ExperimentalConditions](ExperimentalConditions.md) - Environmental and experimental conditions
     * [FSCCurve](FSCCurve.md) - Fourier Shell Correlation curve data.
     * [ImageFeature](ImageFeature.md) - Semantic annotations describing features identified in images using controlled vocabulary terms
     * [LigandInteraction](LigandInteraction.md) - Small molecule/ligand interactions with proteins
     * [MolecularComposition](MolecularComposition.md) - Molecular composition of a sample
     * [MotionCorrectionParameters](MotionCorrectionParameters.md) - Parameters specific to motion correction workflows
     * [ParticlePickingParameters](ParticlePickingParameters.md) - Parameters specific to particle picking workflows
     * [QualityMetrics](QualityMetrics.md) - Quality metrics for experiments
     * [RefinementParameters](RefinementParameters.md) - Parameters specific to 3D refinement workflows
     * [StorageConditions](StorageConditions.md) - Storage conditions for samples
     * [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) - Base class for technique-specific preparation details
         * [CryoEMPreparation](CryoEMPreparation.md) - Cryo-EM specific sample preparation
         * [SAXSPreparation](SAXSPreparation.md) - SAXS/WAXS specific preparation
         * [XRayPreparation](XRayPreparation.md) - X-ray crystallography specific preparation
 * [AttributeValue](AttributeValue.md) - The value for any attribute of an entity. This object can hold both the un-normalized atomic value and the structured value.
     * [DateTimeValue](DateTimeValue.md) - A date or date and time value.
     * [QuantityValue](QuantityValue.md) - A simple quantity value, representing a measurement with a numeric value and unit. This allows data providers to specify measurements in their preferred unit while enabling standardized interpretation. For example, a pixel size could be specified as 1.5 micrometers or 15 Angstroms, with the unit clearly specified.
     * [TextValue](TextValue.md) - A value described using a text string, optionally with a controlled vocabulary ID.
 * [NamedThing](NamedThing.md) - A named thing
     * [AggregatedProteinView](AggregatedProteinView.md) - Aggregated view of all structural and functional data for a protein
     * [ConformationalEnsemble](ConformationalEnsemble.md) - Ensemble of conformational states for a protein
     * [DataFile](DataFile.md) - A data file generated or used in the study
     * [Dataset](Dataset.md) - A collection of studies
     * [ExperimentRun](ExperimentRun.md) - An experimental data collection session
     * [Image](Image.md) - An image file from structural biology experiments
         * [FTIRImage](FTIRImage.md) - Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy
         * [Image2D](Image2D.md) - A 2D image (micrograph, diffraction pattern)
             * [FluorescenceImage](FluorescenceImage.md) - Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
             * [Micrograph](Micrograph.md) - Motion-corrected micrograph derived from movie
             * [Movie](Movie.md) - Raw cryo-EM movie with frame-by-frame metadata for motion correction
             * [OpticalImage](OpticalImage.md) - Visible light optical microscopy or photography image
             * [XRFImage](XRFImage.md) - X-ray fluorescence (XRF) image showing elemental distribution
         * [Image3D](Image3D.md) - A 3D volume or tomogram
     * [Instrument](Instrument.md) - An instrument used to collect data
         * [BeamlineInstrument](BeamlineInstrument.md) - Multi-technique synchrotron beamline that supports multiple experimental methods
         * [CryoEMInstrument](CryoEMInstrument.md) - Cryo-EM microscope specifications
         * [SAXSInstrument](SAXSInstrument.md) - SAXS/WAXS instrument specifications
         * [XRayInstrument](XRayInstrument.md) - X-ray diffractometer or synchrotron beamline specifications
     * [MeasurementConditions](MeasurementConditions.md) - Conditions under which biophysical measurements were made
     * [OntologyTerm](OntologyTerm.md) - A term from a controlled vocabulary or ontology
     * [ProteinAnnotation](ProteinAnnotation.md) - Base class for all protein-related functional and structural annotations
         * [EvolutionaryConservation](EvolutionaryConservation.md) - Evolutionary conservation information
         * [FunctionalSite](FunctionalSite.md) - Functional sites including catalytic, binding, and regulatory sites
         * [MutationEffect](MutationEffect.md) - Effects of mutations and variants on protein structure and function
         * [PostTranslationalModification](PostTranslationalModification.md) - Post-translational modifications observed or predicted
         * [ProteinProteinInteraction](ProteinProteinInteraction.md) - Protein-protein interactions and interfaces
         * [StructuralFeature](StructuralFeature.md) - Structural features and properties of protein regions
     * [ProteinConstruct](ProteinConstruct.md) - Detailed information about a protein construct including cloning and sequence design
     * [Sample](Sample.md) - A biological sample used in structural biology experiments
     * [SamplePreparation](SamplePreparation.md) - A process that prepares a sample for imaging
     * [Study](Study.md) - A focused research investigation that groups related samples, experiments, and data collection around a specific biological question or hypothesis
     * [WorkflowRun](WorkflowRun.md) - A computational processing workflow execution

### Mixins


### Slots

 * [➞biophysical_properties](aggregatedProteinView__biophysical_properties.md) - All biophysical properties
 * [➞conformational_ensemble](aggregatedProteinView__conformational_ensemble.md) - Conformational ensemble data
 * [➞cross_references](aggregatedProteinView__cross_references.md) - Database cross-references
 * [➞evolutionary_conservation](aggregatedProteinView__evolutionary_conservation.md) - Conservation analysis
 * [➞functional_sites](aggregatedProteinView__functional_sites.md) - All functional site annotations
 * [➞ligand_interactions](aggregatedProteinView__ligand_interactions.md) - All ligand interactions
 * [➞mutations](aggregatedProteinView__mutations.md) - All mutation annotations
 * [➞organism](aggregatedProteinView__organism.md) - Source organism
 * [➞organism_id](aggregatedProteinView__organism_id.md) - NCBI taxonomy ID
 * [➞pdb_entries](aggregatedProteinView__pdb_entries.md) - All PDB entries for this protein
 * [➞protein_interactions](aggregatedProteinView__protein_interactions.md) - All protein-protein interactions
 * [➞protein_name](aggregatedProteinView__protein_name.md) - Protein name
 * [➞ptms](aggregatedProteinView__ptms.md) - All post-translational modifications
 * [➞structural_features](aggregatedProteinView__structural_features.md) - All structural feature annotations
 * [➞uniprot_id](aggregatedProteinView__uniprot_id.md) - UniProt accession
 * [attribute](attribute.md) - The attribute being represented.
 * [➞description](attributeGroup__description.md)
 * [➞attribute](attributeValue__attribute.md) - The attribute being represented.
 * [➞raw_value](attributeValue__raw_value.md) - Unnormalized atomic string representation, suggested syntax {number} {unit}
     * [QuantityValue➞raw_value](QuantityValue_raw_value.md)
 * [➞id](attribute__id.md) - A CURIE for the attribute, should one exist. Where available, please use OBO Foundry ontologies or other controlled vocabularies for labelling attributes; the id should be the term ID from the ontology.
 * [➞label](attribute__label.md) - Text string to describe the attribute. Where available, please use OBO Foundry ontologies or other controlled vocabularies for labelling attributes; the label should be the term name from the ontology.
 * [➞energy_max](beamlineInstrument__energy_max.md) - Maximum X-ray energy in keV
 * [➞energy_min](beamlineInstrument__energy_min.md) - Minimum X-ray energy in keV
 * [➞mail_in_service](beamlineInstrument__mail_in_service.md) - Whether mail-in sample service is available
 * [➞q_range_max](beamlineInstrument__q_range_max.md) - Maximum q value for SAXS in inverse Angstroms
 * [➞q_range_min](beamlineInstrument__q_range_min.md) - Minimum q value for SAXS in inverse Angstroms
 * [➞sample_changer_capacity](beamlineInstrument__sample_changer_capacity.md) - Automatic sample changer capacity
 * [➞source_type](beamlineInstrument__source_type.md) - Type of X-ray source
 * [➞techniques_supported](beamlineInstrument__techniques_supported.md) - Experimental techniques available at this beamline
 * [➞website](beamlineInstrument__website.md) - Beamline website URL
 * [➞error](biophysicalProperty__error.md) - Experimental error or uncertainty
 * [➞experimental_method](biophysicalProperty__experimental_method.md) - Method used for measurement
 * [➞measurement_conditions](biophysicalProperty__measurement_conditions.md) - Conditions under which measurement was made. If multiple sets of conditions were used, this will represent that the same values were obtained under different conditions. If values differ under different conditions, separate BiophysicalProperty instances should be created.
 * [➞property_type](biophysicalProperty__property_type.md) - Type of biophysical property
 * [➞unit](biophysicalProperty__unit.md) - Unit of measurement
 * [➞value](biophysicalProperty__value.md) - Numerical value of the property
 * [➞additives](bufferComposition__additives.md) - Additional additives in the buffer
 * [➞components](bufferComposition__components.md) - Buffer components and their concentrations
 * [➞ph](bufferComposition__ph.md) - pH of the buffer (range: 0-14)
 * [➞amplitude_contrast](cTFEstimationParameters__amplitude_contrast.md) - Amplitude contrast value
 * [➞cs_used_in_estimation](cTFEstimationParameters__cs_used_in_estimation.md) - Spherical aberration (Cs) value used during CTF estimation, typically specified in millimeters; may differ from instrument specification. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞defocus_search_max](cTFEstimationParameters__defocus_search_max.md) - Maximum defocus search range, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞defocus_search_min](cTFEstimationParameters__defocus_search_min.md) - Minimum defocus search range, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞defocus_step](cTFEstimationParameters__defocus_step.md) - Defocus search step, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞voltage_used_in_estimation](cTFEstimationParameters__voltage_used_in_estimation.md) - Accelerating voltage value used during CTF estimation, typically specified in kilovolts (kV); may differ from instrument specification. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞cpu_hours](computeResources__cpu_hours.md) - CPU hours used, measured in hours. Data providers may specify alternative time units by including the unit in the QuantityValue.
 * [➞gpu_hours](computeResources__gpu_hours.md) - GPU hours used, measured in hours. Data providers may specify alternative time units by including the unit in the QuantityValue.
 * [➞memory_gb](computeResources__memory_gb.md) - Maximum memory used, typically specified in gigabytes (GB). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞storage_gb](computeResources__storage_gb.md) - Storage used, typically specified in gigabytes (GB). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞clustering_method](conformationalEnsemble__clustering_method.md) - Method used for conformational clustering
 * [➞conformational_states](conformationalEnsemble__conformational_states.md) - Individual conformational states
 * [➞energy_landscape](conformationalEnsemble__energy_landscape.md) - Description of the energy landscape
 * [➞principal_motions](conformationalEnsemble__principal_motions.md) - Description of principal motions
 * [➞protein_id](conformationalEnsemble__protein_id.md) - UniProt accession
 * [➞rmsd_threshold](conformationalEnsemble__rmsd_threshold.md) - RMSD threshold for clustering (Angstroms)
 * [➞transition_pathways](conformationalEnsemble__transition_pathways.md) - Description of transition pathways between states
 * [➞characteristic_features](conformationalState__characteristic_features.md) - Key features of this conformation
 * [➞free_energy](conformationalState__free_energy.md) - Relative free energy (kcal/mol)
 * [➞pdb_entries](conformationalState__pdb_entries.md) - PDB entries representing this state
 * [➞population](conformationalState__population.md) - Relative population of this state (range: 0-1)
 * [➞rmsd_from_reference](conformationalState__rmsd_from_reference.md) - RMSD from reference structure
 * [➞state_id](conformationalState__state_id.md) - Identifier for this state
 * [➞state_name](conformationalState__state_name.md) - Descriptive name (e.g., 'open', 'closed')
 * [➞accelerating_voltage](cryoEMInstrument__accelerating_voltage.md) - Accelerating voltage in kV
 * [➞autoloader_capacity](cryoEMInstrument__autoloader_capacity.md) - Number of grids the autoloader can hold
 * [➞c2_aperture](cryoEMInstrument__c2_aperture.md) - C2 aperture size in micrometers
 * [➞cs](cryoEMInstrument__cs.md) - Spherical aberration (Cs) in millimeters
 * [➞cs_corrector](cryoEMInstrument__cs_corrector.md) - Spherical aberration corrector present
 * [➞detector_dimensions](cryoEMInstrument__detector_dimensions.md) - Detector dimensions in pixels (e.g., 4096x4096, 5760x4092)
 * [➞detector_manufacturer](cryoEMInstrument__detector_manufacturer.md) - Detector manufacturer (e.g., Gatan, ThermoFisher, DirectElectron)
 * [➞detector_mode](cryoEMInstrument__detector_mode.md) - Supported or default detector operating mode
 * [➞detector_model](cryoEMInstrument__detector_model.md) - Detector model (e.g., K3, Falcon 4i, DE-64)
 * [➞detector_position](cryoEMInstrument__detector_position.md) - Physical position of detector in microscope (e.g., post-GIF, pre-column)
 * [➞detector_technology](cryoEMInstrument__detector_technology.md) - Generic detector technology type
 * [➞energy_filter_make](cryoEMInstrument__energy_filter_make.md) - Energy filter manufacturer
 * [➞energy_filter_model](cryoEMInstrument__energy_filter_model.md) - Energy filter model
 * [➞energy_filter_present](cryoEMInstrument__energy_filter_present.md) - Whether energy filter is present
 * [➞energy_filter_slit_width](cryoEMInstrument__energy_filter_slit_width.md) - Energy filter slit width in eV
 * [➞gunlens](cryoEMInstrument__gunlens.md) - Gun lens setting
 * [➞imaging_mode](cryoEMInstrument__imaging_mode.md) - Imaging mode for electron microscopy
 * [➞microscope_software](cryoEMInstrument__microscope_software.md) - Microscope control software (e.g., SerialEM, EPU, Leginon)
 * [➞microscope_software_version](cryoEMInstrument__microscope_software_version.md) - Software version
 * [➞objective_aperture](cryoEMInstrument__objective_aperture.md) - Objective aperture size in micrometers
 * [➞phase_plate](cryoEMInstrument__phase_plate.md) - Phase plate available
 * [➞phase_plate_type](cryoEMInstrument__phase_plate_type.md) - Type of phase plate if present
 * [➞pixel_size_physical](cryoEMInstrument__pixel_size_physical.md) - Physical pixel size in micrometers
 * [➞pixel_size_physical_um](cryoEMInstrument__pixel_size_physical_um.md) - Physical pixel size of the detector in micrometers
 * [➞spotsize](cryoEMInstrument__spotsize.md) - Electron beam spot size setting
 * [➞tem_beam_diameter](cryoEMInstrument__tem_beam_diameter.md) - TEM beam diameter in micrometers
 * [➞blot_force](cryoEMPreparation__blot_force.md) - Blotting force setting
 * [➞blot_number](cryoEMPreparation__blot_number.md) - Number of blots applied
 * [➞blot_time](cryoEMPreparation__blot_time.md) - Blotting time, typically specified in seconds (range: 0.5-10.0). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞blotter_height](cryoEMPreparation__blotter_height.md) - Blotter height setting. Data providers may include unit information in the QuantityValue if needed.
 * [➞blotter_setting](cryoEMPreparation__blotter_setting.md) - Blotter setting value. Data providers may include unit information in the QuantityValue if needed.
 * [➞chamber_temperature](cryoEMPreparation__chamber_temperature.md) - Chamber temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞ethane_temperature](cryoEMPreparation__ethane_temperature.md) - Ethane temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞glow_discharge_applied](cryoEMPreparation__glow_discharge_applied.md) - Whether glow discharge treatment was applied
 * [➞glow_discharge_atmosphere](cryoEMPreparation__glow_discharge_atmosphere.md) - Glow discharge atmosphere (air, amylamine)
 * [➞glow_discharge_current](cryoEMPreparation__glow_discharge_current.md) - Glow discharge current, typically specified in milliamperes. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞glow_discharge_pressure](cryoEMPreparation__glow_discharge_pressure.md) - Glow discharge pressure, typically specified in millibars. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞glow_discharge_time](cryoEMPreparation__glow_discharge_time.md) - Glow discharge time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞grid_material](cryoEMPreparation__grid_material.md) - Grid material
 * [➞grid_type](cryoEMPreparation__grid_type.md) - Type of EM grid used
 * [➞hole_size](cryoEMPreparation__hole_size.md) - Hole size, typically specified in micrometers (range: 0.5-5.0). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞humidity_percentage](cryoEMPreparation__humidity_percentage.md) - Chamber humidity during vitrification (range: 0-100), typically specified as a percentage. Data providers may specify as decimal fraction by including the unit in the QuantityValue.
 * [➞plasma_treatment](cryoEMPreparation__plasma_treatment.md) - Plasma treatment details
 * [➞sample_applied_volume](cryoEMPreparation__sample_applied_volume.md) - Volume of sample applied, typically specified in microliters. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞support_film](cryoEMPreparation__support_film.md) - Support film type
 * [➞vitrification_instrument](cryoEMPreparation__vitrification_instrument.md) - Vitrification instrument used (e.g., Vitrobot)
 * [➞vitrification_method](cryoEMPreparation__vitrification_method.md) - Method used for vitrification
 * [➞wait_time](cryoEMPreparation__wait_time.md) - Wait time before blotting, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞cryo_protectant](crystallizationConditions__cryo_protectant.md) - Cryoprotectant used for crystal cooling
 * [➞crystal_id](crystallizationConditions__crystal_id.md) - Identifier for the specific crystal used
 * [➞crystal_size_um](crystallizationConditions__crystal_size_um.md) - Crystal dimensions in micrometers (length x width x height)
 * [➞crystallization_conditions](crystallizationConditions__crystallization_conditions.md) - Complete description of crystallization conditions including precipitant, pH, salts
 * [➞drop_ratio_protein_to_reservoir](crystallizationConditions__drop_ratio_protein_to_reservoir.md) - Ratio of protein to reservoir solution in drop (e.g., 1:1, 2:1)
 * [➞drop_volume](crystallizationConditions__drop_volume.md) - Total drop volume, typically specified in nanoliters. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞method](crystallizationConditions__method.md) - Crystallization method used
 * [➞protein_concentration](crystallizationConditions__protein_concentration.md) - Protein concentration for crystallization in mg/mL
 * [➞reservoir_volume_ul](crystallizationConditions__reservoir_volume_ul.md) - Reservoir volume, typically specified in microliters. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞screen_name](crystallizationConditions__screen_name.md) - Name of crystallization screen used
 * [➞seed_stock_dilution](crystallizationConditions__seed_stock_dilution.md) - Dilution factor for seed stock
 * [➞seeding_type](crystallizationConditions__seeding_type.md) - Type of seeding used (micro, macro, streak)
 * [➞temperature_c](crystallizationConditions__temperature_c.md) - Crystallization temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞attenuator](dataCollectionStrategy__attenuator.md) - Attenuator setting used
 * [➞beam_center_x_px](dataCollectionStrategy__beam_center_x_px.md) - Beam center X coordinate in pixels
 * [➞beam_center_y_px](dataCollectionStrategy__beam_center_y_px.md) - Beam center Y coordinate in pixels
 * [➞beam_size_um](dataCollectionStrategy__beam_size_um.md) - Beam size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞collection_mode](dataCollectionStrategy__collection_mode.md) - Mode of data collection
 * [➞detector_distance_mm](dataCollectionStrategy__detector_distance_mm.md) - Detector distance, typically specified in millimeters. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞detector_mode](dataCollectionStrategy__detector_mode.md) - Detector operating mode used during this experiment
 * [➞dose_per_frame](dataCollectionStrategy__dose_per_frame.md) - Dose per frame, typically specified in electrons per Angstrom squared (e⁻/Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞flux_photons_per_s](dataCollectionStrategy__flux_photons_per_s.md) - Photon flux, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞frame_rate](dataCollectionStrategy__frame_rate.md) - Frame rate, typically specified in frames per second. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞oscillation_per_image_deg](dataCollectionStrategy__oscillation_per_image_deg.md) - Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞pixel_size_calibrated](dataCollectionStrategy__pixel_size_calibrated.md) - Calibrated pixel size for this experiment, typically specified in Angstroms (Å) per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞strategy_notes](dataCollectionStrategy__strategy_notes.md) - Notes about data collection strategy
 * [➞temperature_k](dataCollectionStrategy__temperature_k.md) - Data collection temperature, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞total_dose](dataCollectionStrategy__total_dose.md) - Total electron dose for cryo-EM, typically specified in electrons per Angstrom squared (e⁻/Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞total_frames](dataCollectionStrategy__total_frames.md) - Total number of frames/images
 * [➞total_rotation_deg](dataCollectionStrategy__total_rotation_deg.md) - Total rotation range, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞transmission_percent](dataCollectionStrategy__transmission_percent.md) - Beam transmission, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
 * [➞wavelength_a](dataCollectionStrategy__wavelength_a.md) - X-ray wavelength, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞checksum](dataFile__checksum.md) - SHA-256 checksum for data integrity
 * [➞creation_date](dataFile__creation_date.md) - File creation date
 * [➞data_type](dataFile__data_type.md) - Type of data in the file
 * [➞file_format](dataFile__file_format.md) - File format
 * [➞file_name](dataFile__file_name.md) - Name of the file
 * [➞file_path](dataFile__file_path.md) - Path to the file
 * [➞file_role](dataFile__file_role.md) - Role of the file (raw, intermediate, final, diagnostic, metadata)
 * [➞file_size_bytes](dataFile__file_size_bytes.md) - File size in bytes
 * [➞related_entity](dataFile__related_entity.md) - ID of the entity that owns this file
 * [➞storage_uri](dataFile__storage_uri.md) - Storage URI (S3, Globus, etc.)
 * [➞database_id](databaseCrossReference__database_id.md) - Identifier in the external database
 * [➞database_name](databaseCrossReference__database_name.md) - Name of the external database
 * [➞database_url](databaseCrossReference__database_url.md) - URL to the database entry
 * [➞last_updated](databaseCrossReference__last_updated.md) - Date of last update
 * [➞instruments](dataset__instruments.md) - Instruments used across all studies in this dataset
 * [➞keywords](dataset__keywords.md) - Keywords or tags describing the dataset for search and categorization
 * [➞studies](dataset__studies.md) - Individual research studies contained in this dataset
 * [➞value](dateTimeValue__value.md) - The date or date/time value, expressed in ISO 8601-compatible form. Dates should be expressed as YYYY-MM-DD; times should be expressed as HH:MM:SS with optional milliseconds and an indication of the timezone.
 * [➞alignment_depth](evolutionaryConservation__alignment_depth.md) - Number of sequences in alignment
 * [➞coevolved_residues](evolutionaryConservation__coevolved_residues.md) - Pairs of coevolved residues
 * [➞conservation_method](evolutionaryConservation__conservation_method.md) - Method used for conservation analysis
 * [➞conservation_score](evolutionaryConservation__conservation_score.md) - Overall conservation score (range: 0-1)
 * [➞conserved_residues](evolutionaryConservation__conserved_residues.md) - Highly conserved residues
 * [➞taxonomic_range](evolutionaryConservation__taxonomic_range.md) - Taxonomic range of conservation
 * [➞variable_residues](evolutionaryConservation__variable_residues.md) - Highly variable residues
 * [➞acquisition_software](experimentRun__acquisition_software.md) - Acquisition software used (e.g., SerialEM, EPU, Leginon)
 * [➞acquisition_software_version](experimentRun__acquisition_software_version.md) - Version of acquisition software
 * [➞astigmatism_target](experimentRun__astigmatism_target.md) - Target astigmatism in Angstroms
 * [➞autoloader_slot](experimentRun__autoloader_slot.md) - Autoloader slot identifier
 * [➞beam_center_x](experimentRun__beam_center_x.md) - Beam center X coordinate, typically specified in pixels ([px]). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞beam_center_y](experimentRun__beam_center_y.md) - Beam center Y coordinate, typically specified in pixels ([px]). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞beamline](experimentRun__beamline.md) - Beamline identifier (e.g., FMX, AMX, 12.3.1)
 * [➞calibrated_pixel_size](experimentRun__calibrated_pixel_size.md) - Calibrated pixel size in Angstroms per pixel
 * [➞camera_binning](experimentRun__camera_binning.md) - Camera binning factor. This must be a positive float value (e.g., 1, 1.5, 2, 3).
 * [➞coma](experimentRun__coma.md) - Coma aberration in nanometers
 * [➞data_collection_strategy](experimentRun__data_collection_strategy.md) - Strategy for data collection
 * [➞defocus_range_increment](experimentRun__defocus_range_increment.md) - Defocus range increment in micrometers
 * [➞defocus_range_max](experimentRun__defocus_range_max.md) - Maximum defocus range in micrometers
 * [➞defocus_range_min](experimentRun__defocus_range_min.md) - Minimum defocus range in micrometers
 * [➞defocus_target](experimentRun__defocus_target.md) - Target defocus value in micrometers
 * [➞detector_distance](experimentRun__detector_distance.md) - Distance from sample to detector, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞dose_rate](experimentRun__dose_rate.md) - Dose rate in e-/pixel/s or e-/Angstrom^2/s
 * [➞end_time](experimentRun__end_time.md) - Data collection end timestamp
 * [➞experiment_code](experimentRun__experiment_code.md) - Human-friendly laboratory or facility identifier for the experiment (e.g., 'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and cross-referencing within laboratory systems.
 * [➞experiment_date](experimentRun__experiment_date.md) - Date of the experiment
 * [➞experimental_conditions](experimentRun__experimental_conditions.md) - Environmental and experimental conditions
 * [➞experimental_method](experimentRun__experimental_method.md) - Specific experimental method for structure determination (particularly for diffraction techniques)
 * [➞exposure_time](experimentRun__exposure_time.md) - Exposure time per image, typically specified in seconds (s). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞exposure_time_per_frame](experimentRun__exposure_time_per_frame.md) - Exposure time per frame in milliseconds
 * [➞flux](experimentRun__flux.md) - Photon flux at sample position, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞flux_end](experimentRun__flux_end.md) - Photon flux at end of data collection, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞frames_per_movie](experimentRun__frames_per_movie.md) - Number of frames per movie
 * [➞holes_per_group](experimentRun__holes_per_group.md) - Number of holes per group. Data providers may include unit information in the QuantityValue if needed.
 * [➞instrument_id](experimentRun__instrument_id.md) - Reference to the instrument used
 * [➞ispyb_data_collection_id](experimentRun__ispyb_data_collection_id.md) - ISPyB DataCollection.dataCollectionId for traceability
 * [➞ispyb_session_id](experimentRun__ispyb_session_id.md) - ISPyB BLSession.sessionId
 * [➞magnification](experimentRun__magnification.md) - Magnification used during data collection
 * [➞number_of_images](experimentRun__number_of_images.md) - Total number of diffraction images collected
 * [➞operator_id](experimentRun__operator_id.md) - Identifier or name of the person who performed the experiment data collection (e.g., 'jsmith', 'John Smith', or personnel ID)
 * [➞oscillation_angle](experimentRun__oscillation_angle.md) - Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞pixel_size_x](experimentRun__pixel_size_x.md) - Pixel size X dimension, typically specified in micrometers (µm). Data providers may specify alternative units (e.g., Angstroms) by including the unit in the QuantityValue.
 * [➞pixel_size_y](experimentRun__pixel_size_y.md) - Pixel size Y dimension, typically specified in micrometers (µm). Data providers may specify alternative units (e.g., Angstroms) by including the unit in the QuantityValue.
 * [➞processing_status](experimentRun__processing_status.md) - Current processing status
 * [➞quality_metrics](experimentRun__quality_metrics.md) - Quality metrics for the experiment
 * [➞raw_data_location](experimentRun__raw_data_location.md) - Location of raw data files
 * [➞resolution](experimentRun__resolution.md) - Resolution at edge of detector, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞resolution_at_corner](experimentRun__resolution_at_corner.md) - Resolution at corner of detector, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞sample_id](experimentRun__sample_id.md) - Reference to the sample being analyzed
 * [➞shots_per_hole](experimentRun__shots_per_hole.md) - Number of shots taken per hole
 * [➞slit_gap_horizontal](experimentRun__slit_gap_horizontal.md) - Horizontal slit gap aperture, typically specified in micrometers (µm). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞slit_gap_vertical](experimentRun__slit_gap_vertical.md) - Vertical slit gap aperture, typically specified in micrometers (µm). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞stage_tilt](experimentRun__stage_tilt.md) - Stage tilt angle in degrees
 * [➞start_angle](experimentRun__start_angle.md) - Starting rotation angle, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞start_time](experimentRun__start_time.md) - Data collection start timestamp
 * [➞synchrotron_mode](experimentRun__synchrotron_mode.md) - Synchrotron storage ring fill mode
 * [➞technique](experimentRun__technique.md) - Technique used for data collection
 * [➞total_dose](experimentRun__total_dose.md) - Total electron dose in e-/Angstrom^2
 * [➞total_exposure_time](experimentRun__total_exposure_time.md) - Total exposure time in milliseconds
 * [➞total_rotation](experimentRun__total_rotation.md) - Total rotation range collected, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞transmission](experimentRun__transmission.md) - X-ray beam transmission as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
 * [➞undulator_gap](experimentRun__undulator_gap.md) - Undulator gap setting, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue. Primary undulator gap for beamlines with insertion devices.
 * [➞wavelength](experimentRun__wavelength.md) - X-ray wavelength, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞atmosphere](experimentalConditions__atmosphere.md) - Atmosphere composition
 * [➞beam_energy](experimentalConditions__beam_energy.md) - Beam energy, typically specified in kiloelectronvolts (keV). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞exposure_time](experimentalConditions__exposure_time.md) - Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞humidity](experimentalConditions__humidity.md) - Humidity, typically specified as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
 * [➞pressure](experimentalConditions__pressure.md) - Pressure, typically specified in kilopascals (kPa). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞temperature](experimentalConditions__temperature.md) - Temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞fsc_value](fSCCurve__fsc_value.md) - FSC values corresponding to each resolution
 * [➞resolution_angstrom](fSCCurve__resolution_angstrom.md) - Resolution values in Angstroms
 * [➞apodization_function](fTIRImage__apodization_function.md) - Mathematical function used for apodization
 * [➞background_correction](fTIRImage__background_correction.md) - Method used for background correction
 * [➞molecular_signatures](fTIRImage__molecular_signatures.md) - Identified molecular signatures or peaks
 * [➞number_of_scans](fTIRImage__number_of_scans.md) - Number of scans averaged for the spectrum
 * [➞spectral_resolution](fTIRImage__spectral_resolution.md) - Spectral resolution, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞wavenumber_max](fTIRImage__wavenumber_max.md) - Maximum wavenumber, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞wavenumber_min](fTIRImage__wavenumber_min.md) - Minimum wavenumber, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞channel_name](fluorescenceImage__channel_name.md) - Name of the fluorescence channel (e.g., DAPI, GFP, RFP)
 * [➞emission_filter](fluorescenceImage__emission_filter.md) - Specifications of the emission filter
 * [➞emission_wavelength](fluorescenceImage__emission_wavelength.md) - Emission wavelength, typically specified in nanometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞excitation_filter](fluorescenceImage__excitation_filter.md) - Specifications of the excitation filter
 * [➞excitation_wavelength](fluorescenceImage__excitation_wavelength.md) - Excitation wavelength, typically specified in nanometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞fluorophore](fluorescenceImage__fluorophore.md) - Name or type of fluorophore used
 * [➞laser_power](fluorescenceImage__laser_power.md) - Laser power, typically specified in milliwatts. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞pinhole_size](fluorescenceImage__pinhole_size.md) - Pinhole size, typically specified in Airy units for confocal microscopy. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞quantum_yield](fluorescenceImage__quantum_yield.md) - Quantum yield of the fluorophore
 * [➞conservation_score](functionalSite__conservation_score.md) - Evolutionary conservation score (range: 0-1)
 * [➞ec_number](functionalSite__ec_number.md) - Enzyme Commission number for catalytic sites
 * [➞functional_importance](functionalSite__functional_importance.md) - Description of functional importance
 * [➞go_terms](functionalSite__go_terms.md) - Associated Gene Ontology terms
 * [➞ligand_interactions](functionalSite__ligand_interactions.md) - Ligands that interact with this site
 * [➞residues](functionalSite__residues.md) - List of residues forming the functional site. Each should be specified as a string (e.g., "45", "120A").
 * [➞site_name](functionalSite__site_name.md) - Common name for this site
 * [➞site_type](functionalSite__site_type.md) - Type of functional site
 * [➞astigmatism](image2D__astigmatism.md) - Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * [Micrograph➞astigmatism](Micrograph_astigmatism.md) - Astigmatism in Angstroms
 * [➞defocus](image2D__defocus.md) - Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * [Micrograph➞defocus](Micrograph_defocus.md) - Measured defocus in micrometers
 * [➞dimensions_z](image3D__dimensions_z.md) - Image depth, typically specified in pixels or slices. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞reconstruction_method](image3D__reconstruction_method.md) - Method used for 3D reconstruction
 * [➞voxel_size](image3D__voxel_size.md) - Voxel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞terms](imageFeature__terms.md) - Ontology terms describing features identified in the image
 * [➞acquisition_date](image__acquisition_date.md) - Date image was acquired
 * [➞dimensions_x](image__dimensions_x.md) - Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞dimensions_y](image__dimensions_y.md) - Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞dose](image__dose.md) - Electron dose in e-/Å²
 * [➞exposure_time](image__exposure_time.md) - Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞file_name](image__file_name.md) - Image file name
 * [➞pixel_size](image__pixel_size.md) - Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞beamline_id](instrument__beamline_id.md) - Beamline identifier at synchrotron/neutron facility
 * [➞current_status](instrument__current_status.md) - Current operational status
 * [➞facility_name](instrument__facility_name.md) - Name of the research facility where the instrument is located
 * [➞facility_ror](instrument__facility_ror.md) - Research Organization Registry (ROR) identifier for the facility
 * [➞installation_date](instrument__installation_date.md) - Date of instrument installation
 * [➞instrument_category](instrument__instrument_category.md) - Category distinguishing beamlines from laboratory equipment
 * [➞instrument_code](instrument__instrument_code.md) - Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
 * [➞manufacturer](instrument__manufacturer.md) - Instrument manufacturer
 * [➞model](instrument__model.md) - Instrument model
 * [➞binding_affinity](ligandInteraction__binding_affinity.md) - Binding affinity value
 * [➞binding_affinity_type](ligandInteraction__binding_affinity_type.md) - Type of binding measurement (Kd, Ki, IC50)
 * [➞binding_affinity_unit](ligandInteraction__binding_affinity_unit.md) - Unit of binding affinity
 * [➞binding_site_residues](ligandInteraction__binding_site_residues.md) - Residues involved in ligand binding
 * [➞druggability_score](ligandInteraction__druggability_score.md) - Druggability score of the binding site (range: 0-1)
 * [➞interaction_distance](ligandInteraction__interaction_distance.md) - Distance criteria for interaction (Angstroms)
 * [➞interaction_type](ligandInteraction__interaction_type.md) - Type of interaction
 * [➞is_cofactor](ligandInteraction__is_cofactor.md) - Whether the ligand is a cofactor
 * [➞is_drug_like](ligandInteraction__is_drug_like.md) - Whether the ligand has drug-like properties
 * [➞ligand_id](ligandInteraction__ligand_id.md) - Ligand identifier (ChEMBL, ChEBI, PubChem)
 * [➞ligand_name](ligandInteraction__ligand_name.md) - Common name of the ligand
 * [➞ligand_smiles](ligandInteraction__ligand_smiles.md) - SMILES representation of the ligand
 * [➞buffer_composition](measurementConditions__buffer_composition.md) - Composition of the buffer used
 * [➞ionic_strength](measurementConditions__ionic_strength.md) - Ionic strength, typically specified in molar (mol/L). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞ph](measurementConditions__ph.md) - pH value of the solution during measurement (range: 0-14), typically expressed in pH units. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞temperature](measurementConditions__temperature.md) - Temperature during measurement, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞astigmatism_angle](micrograph__astigmatism_angle.md) - Astigmatism angle, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞ctf_quality_score](micrograph__ctf_quality_score.md) - CTF estimation quality score
 * [➞defocus_u](micrograph__defocus_u.md) - Defocus U, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞defocus_v](micrograph__defocus_v.md) - Defocus V, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞dose](micrograph__dose.md) - Total electron dose in e-/Angstrom^2
 * [➞origin_movie_id](micrograph__origin_movie_id.md) - Reference to original movie file
 * [➞resolution_fit_limit](micrograph__resolution_fit_limit.md) - Resolution fit limit, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞ligands](molecularComposition__ligands.md) - Bound ligands or cofactors
 * [➞modifications](molecularComposition__modifications.md) - Post-translational modifications or chemical modifications
 * [➞sequences](molecularComposition__sequences.md) - Amino acid or nucleotide sequences
 * [➞anisotropic_correction](motionCorrectionParameters__anisotropic_correction.md) - Whether anisotropic motion correction was applied
 * [➞bfactor_dose_weighting](motionCorrectionParameters__bfactor_dose_weighting.md) - B-factor for dose weighting, typically specified in Angstroms squared. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞binning](motionCorrectionParameters__binning.md) - Binning factor applied during motion correction. This must be a positive float value (e.g., 1, 1.5, 2, 3).
 * [➞dose_weighting](motionCorrectionParameters__dose_weighting.md) - Whether dose weighting was applied
 * [➞drift_total](motionCorrectionParameters__drift_total.md) - Total drift, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞frame_grouping](motionCorrectionParameters__frame_grouping.md) - Number of frames grouped together
 * [➞output_binning](motionCorrectionParameters__output_binning.md) - Output binning factor. This must be a positive float value (e.g., 1, 1.5, 2, 3).
 * [➞patch_size](motionCorrectionParameters__patch_size.md) - Patch size for local motion correction
 * [➞acquisition_group](movie__acquisition_group.md) - Acquisition group identifier (e.g., template or area)
 * [➞beam_shift_x](movie__beam_shift_x.md) - Beam shift X in microradians
 * [➞beam_shift_y](movie__beam_shift_y.md) - Beam shift Y in microradians
 * [➞dose_per_frame](movie__dose_per_frame.md) - Electron dose per frame in e-/Angstrom^2
 * [➞frames](movie__frames.md) - Number of frames in the movie
 * [➞grid_square_id](movie__grid_square_id.md) - Grid square identifier
 * [➞hole_id](movie__hole_id.md) - Hole identifier within grid square
 * [➞ice_thickness_estimate](movie__ice_thickness_estimate.md) - Estimated ice thickness, typically specified in nanometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞nominal_defocus](movie__nominal_defocus.md) - Nominal defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞pixel_size_unbinned](movie__pixel_size_unbinned.md) - Unbinned pixel size, typically specified in Angstroms per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞stage_position_x](movie__stage_position_x.md) - Stage X position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞stage_position_y](movie__stage_position_y.md) - Stage Y position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞stage_position_z](movie__stage_position_z.md) - Stage Z position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞super_resolution](movie__super_resolution.md) - Whether super-resolution mode was used
 * [➞timestamp](movie__timestamp.md) - Acquisition timestamp
 * [➞allele_frequency](mutationEffect__allele_frequency.md) - Population allele frequency (range: 0-1)
 * [➞clinical_significance](mutationEffect__clinical_significance.md) - Clinical significance
 * [➞delta_delta_g](mutationEffect__delta_delta_g.md) - Change in folding free energy (kcal/mol)
 * [➞disease_association](mutationEffect__disease_association.md) - Associated disease or phenotype
 * [➞effect_on_function](mutationEffect__effect_on_function.md) - Effect on protein function
 * [➞effect_on_stability](mutationEffect__effect_on_stability.md) - Effect on protein stability
 * [➞functional_impact_description](mutationEffect__functional_impact_description.md) - Description of functional impact
 * [➞mutation](mutationEffect__mutation.md) - Mutation in standard notation (e.g., 'A123V')
 * [➞mutation_type](mutationEffect__mutation_type.md) - Type of mutation
 * [➞omim_id](mutationEffect__omim_id.md) - OMIM database identifier
 * [➞description](namedThing__description.md) - A detailed textual description of this entity
 * [➞id](namedThing__id.md) - Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
 * [➞title](namedThing__title.md) - A human-readable name or title for this entity
 * [numeric_value](numeric_value.md) - The numerical part of a quantity value, expressed as a number.
     * [QuantityValue➞numeric_value](QuantityValue_numeric_value.md) - The numerical value of the quantity
     * [maximum_numeric_value](maximum_numeric_value.md) - The maximum value part, expressed as a number, of the quantity value when the value covers a range.
     * [minimum_numeric_value](minimum_numeric_value.md) - The minimum value part, expressed as a number, of the quantity value when the value covers a range.
 * [➞definition](ontologyTerm__definition.md) - The formal definition or meaning of the ontology term
 * [➞label](ontologyTerm__label.md) - The human-readable label or name of the ontology term
 * [➞ontology](ontologyTerm__ontology.md) - The ontology or controlled vocabulary this term comes from (e.g., GO, SO, UBERON)
 * [➞terms](ontologyTerm__terms.md) - Collection of ontology terms
 * [➞color_channels](opticalImage__color_channels.md) - Color channels present (e.g., RGB, grayscale)
 * [➞contrast_method](opticalImage__contrast_method.md) - Contrast enhancement method used
 * [➞illumination_type](opticalImage__illumination_type.md) - Type of illumination (brightfield, darkfield, phase contrast, DIC)
 * [➞magnification](opticalImage__magnification.md) - Optical magnification factor. Data providers may specify the unit (e.g., times, X) in the QuantityValue.
 * [➞numerical_aperture](opticalImage__numerical_aperture.md) - Numerical aperture of the objective lens. Data providers may include unit information in the QuantityValue if needed.
 * [➞white_balance](opticalImage__white_balance.md) - White balance settings
 * [➞box_size](particlePickingParameters__box_size.md) - Particle box size in pixels
 * [➞model_file_path](particlePickingParameters__model_file_path.md) - Path to deep learning model file if using a local or custom trained model file. Use this instead of model_name when pointing to a specific file on disk. Either model_name or model_file_path should be provided when using deep learning methods.
 * [➞model_name](particlePickingParameters__model_name.md) - Name or identifier of the deep learning model (e.g., 'resnet16', 'resnet8', 'cryolo_general'). Use this for standard pretrained models. Either model_name or model_file_path should be provided when using deep learning methods.
 * [➞model_source](particlePickingParameters__model_source.md) - Source or software associated with the model (e.g., 'topaz', 'cryolo', 'warp', 'custom', 'pretrained'). Helps track model provenance and should be provided alongside model_name or model_file_path to document which software/framework the model is for.
 * [➞ncc_score](particlePickingParameters__ncc_score.md) - Normalized cross-correlation score threshold
 * [➞picking_method](particlePickingParameters__picking_method.md) - Method used (manual, template_matching, deep_learning, LoG, Topaz, other)
 * [➞power_score](particlePickingParameters__power_score.md) - Power score threshold
 * [➞threshold](particlePickingParameters__threshold.md) - Picking threshold
 * [pixel_size](pixel_size.md) - Final pixel size in Angstroms per pixel
     * [Micrograph➞pixel_size](Micrograph_pixel_size.md)
 * [➞enzyme](postTranslationalModification__enzyme.md) - Enzyme responsible for modification
 * [➞functional_effect](postTranslationalModification__functional_effect.md) - Known functional effect of this PTM
 * [➞mass_shift](postTranslationalModification__mass_shift.md) - Mass change due to modification (Da)
 * [➞modification_group](postTranslationalModification__modification_group.md) - Chemical group added (e.g., 'phosphate', 'methyl')
 * [➞modification_type](postTranslationalModification__modification_type.md) - Type of PTM
 * [➞modified_residue](postTranslationalModification__modified_residue.md) - Residue that is modified
 * [➞regulatory_role](postTranslationalModification__regulatory_role.md) - Role in regulation
 * [➞removal_enzyme](postTranslationalModification__removal_enzyme.md) - Enzyme that removes modification
 * [➞annotation_method](proteinAnnotation__annotation_method.md) - Computational or experimental method used
 * [➞chain_id](proteinAnnotation__chain_id.md) - Chain identifier in the PDB structure
 * [➞confidence_score](proteinAnnotation__confidence_score.md) - Confidence score for the annotation (range: 0-1)
 * [➞evidence_code](proteinAnnotation__evidence_code.md) - Evidence and Conclusion Ontology (ECO) code
 * [➞evidence_type](proteinAnnotation__evidence_type.md) - Type of evidence supporting this annotation
 * [➞pdb_entry](proteinAnnotation__pdb_entry.md) - PDB identifier
 * [➞protein_id](proteinAnnotation__protein_id.md) - UniProt accession number
 * [➞publication_ids](proteinAnnotation__publication_ids.md) - IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
 * [➞residue_range](proteinAnnotation__residue_range.md) - Range of residues (e.g., '1-100', '25,27,30-35')
 * [➞source_database](proteinAnnotation__source_database.md) - Source database or resource that provided this annotation
 * [➞cleavage_site](proteinConstruct__cleavage_site.md) - Protease cleavage site sequence
 * [➞cloning_method](proteinConstruct__cloning_method.md) - Method used for cloning (e.g., restriction digest, Gibson, InFusion)
 * [➞codon_optimization_organism](proteinConstruct__codon_optimization_organism.md) - Organism for which codons were optimized
 * [➞construct_description](proteinConstruct__construct_description.md) - Human-readable description of the construct
 * [➞construct_id](proteinConstruct__construct_id.md) - Unique identifier for this construct
 * [➞gene_name](proteinConstruct__gene_name.md) - Gene name
 * [➞gene_synthesis_provider](proteinConstruct__gene_synthesis_provider.md) - Company or facility that synthesized the gene
 * [➞insert_boundaries](proteinConstruct__insert_boundaries.md) - Start and end positions of insert in vector
 * [➞ncbi_taxid](proteinConstruct__ncbi_taxid.md) - NCBI Taxonomy ID for source organism
 * [➞promoter](proteinConstruct__promoter.md) - Promoter used for expression
 * [➞selectable_marker](proteinConstruct__selectable_marker.md) - Antibiotic resistance or other selectable marker
 * [➞sequence_file_path](proteinConstruct__sequence_file_path.md) - Path to sequence file
 * [➞sequence_length_aa](proteinConstruct__sequence_length_aa.md) - Length of the protein sequence in amino acids
 * [➞sequence_verified_by](proteinConstruct__sequence_verified_by.md) - Method or person who verified the sequence
 * [➞signal_peptide](proteinConstruct__signal_peptide.md) - Signal peptide sequence if present
 * [➞tag_cterm](proteinConstruct__tag_cterm.md) - C-terminal tag
 * [➞tag_nterm](proteinConstruct__tag_nterm.md) - N-terminal tag (e.g., His6, MBP, GST)
 * [➞uniprot_id](proteinConstruct__uniprot_id.md) - UniProt accession for the target protein
 * [➞vector_backbone](proteinConstruct__vector_backbone.md) - Base plasmid backbone used
 * [➞vector_name](proteinConstruct__vector_name.md) - Complete vector name
 * [➞verification_notes](proteinConstruct__verification_notes.md) - Notes from sequence verification
 * [➞binding_energy](proteinProteinInteraction__binding_energy.md) - Calculated binding energy (kcal/mol)
 * [➞biological_assembly](proteinProteinInteraction__biological_assembly.md) - Whether this represents a biological assembly
 * [➞complex_stability](proteinProteinInteraction__complex_stability.md) - Stability assessment of the complex
 * [➞dissociation_constant](proteinProteinInteraction__dissociation_constant.md) - Experimental Kd if available
 * [➞interaction_evidence](proteinProteinInteraction__interaction_evidence.md) - Evidence for this interaction
 * [➞interface_area](proteinProteinInteraction__interface_area.md) - Buried surface area at interface (Ų)
 * [➞interface_residues](proteinProteinInteraction__interface_residues.md) - Residues at the interaction interface
 * [➞partner_chain_id](proteinProteinInteraction__partner_chain_id.md) - Chain ID of interacting partner
 * [➞partner_interface_residues](proteinProteinInteraction__partner_interface_residues.md) - Partner residues at the interaction interface
 * [➞partner_protein_id](proteinProteinInteraction__partner_protein_id.md) - UniProt ID of interacting partner
 * [➞anom_corr](qualityMetrics__anom_corr.md) - Anomalous correlation
 * [➞anom_sig_ano](qualityMetrics__anom_sig_ano.md) - Anomalous signal strength
 * [➞anomalous_used](qualityMetrics__anomalous_used.md) - Whether anomalous signal was used
 * [➞average_b_factor_a2](qualityMetrics__average_b_factor_a2.md) - Average B-factor in Angstroms squared
 * [➞cc_half](qualityMetrics__cc_half.md) - Half-set correlation coefficient CC(1/2)
 * [➞clashscore](qualityMetrics__clashscore.md) - MolProbity clashscore
 * [➞completeness](qualityMetrics__completeness.md) - Data completeness, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
 * [➞completeness_high_res_shell_percent](qualityMetrics__completeness_high_res_shell_percent.md) - Completeness in highest resolution shell, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
 * [➞i_zero](qualityMetrics__i_zero.md) - Forward scattering intensity I(0)
 * [➞mean_i_over_sigma_i](qualityMetrics__mean_i_over_sigma_i.md) - Mean I/sigma(I)
 * [➞molprobity_score](qualityMetrics__molprobity_score.md) - Overall MolProbity score
 * [➞multiplicity](qualityMetrics__multiplicity.md) - Data multiplicity (redundancy)
 * [➞r_factor](qualityMetrics__r_factor.md) - R-factor for crystallography (deprecated, use r_work)
 * [➞r_free](qualityMetrics__r_free.md) - R-free (test set)
 * [➞r_merge](qualityMetrics__r_merge.md) - Rmerge - merge R-factor
 * [➞r_pim](qualityMetrics__r_pim.md) - Rpim - precision-indicating merging R-factor
 * [➞r_work](qualityMetrics__r_work.md) - Refinement R-factor (working set)
 * [➞ramachandran_favored_percent](qualityMetrics__ramachandran_favored_percent.md) - Percentage of residues in favored Ramachandran regions
 * [➞ramachandran_outliers_percent](qualityMetrics__ramachandran_outliers_percent.md) - Percentage of Ramachandran outliers
 * [➞resolution](qualityMetrics__resolution.md) - Resolution, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞resolution_high_shell_a](qualityMetrics__resolution_high_shell_a.md) - High resolution shell limit, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞resolution_low_a](qualityMetrics__resolution_low_a.md) - Low resolution limit, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞rg](qualityMetrics__rg.md) - Radius of gyration, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞signal_to_noise](qualityMetrics__signal_to_noise.md) - Signal to noise ratio
 * [➞space_group](qualityMetrics__space_group.md) - Crystallographic space group
 * [➞unit_cell_a](qualityMetrics__unit_cell_a.md) - Unit cell parameter a, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_alpha](qualityMetrics__unit_cell_alpha.md) - Unit cell angle alpha, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_b](qualityMetrics__unit_cell_b.md) - Unit cell parameter b, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_beta](qualityMetrics__unit_cell_beta.md) - Unit cell angle beta, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_c](qualityMetrics__unit_cell_c.md) - Unit cell parameter c, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_gamma](qualityMetrics__unit_cell_gamma.md) - Unit cell angle gamma, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞wilson_b_factor_a2](qualityMetrics__wilson_b_factor_a2.md) - Wilson B-factor in Angstroms squared
 * [raw_value](raw_value.md) - The value that was specified in raw form, i.e. a string. E.g. "2 Angstroms" or "2-4 micrometers"
 * [➞box_size](refinementParameters__box_size.md) - Box size in pixels
 * [➞gold_standard](refinementParameters__gold_standard.md) - Whether gold-standard refinement was used
 * [➞map_sharpening_bfactor](refinementParameters__map_sharpening_bfactor.md) - B-factor used for map sharpening, typically specified in Angstroms squared (Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞pixel_size](refinementParameters__pixel_size.md) - Pixel size, typically specified in Angstroms per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞resolution_0_143](refinementParameters__resolution_0_143.md) - Resolution at FSC=0.143, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞resolution_0_5](refinementParameters__resolution_0_5.md) - Resolution at FSC=0.5, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞split_strategy](refinementParameters__split_strategy.md) - Strategy for data splitting
 * [➞symmetry](refinementParameters__symmetry.md) - Symmetry applied (C1, Cn, Dn, T, O, I)
 * [➞detector_distance_max](sAXSInstrument__detector_distance_max.md) - Maximum detector distance in mm
 * [➞detector_distance_min](sAXSInstrument__detector_distance_min.md) - Minimum detector distance in mm
 * [➞q_range_max](sAXSInstrument__q_range_max.md) - Maximum q value in inverse Angstroms
 * [➞q_range_min](sAXSInstrument__q_range_min.md) - Minimum q value in inverse Angstroms
 * [➞sample_changer_capacity](sAXSInstrument__sample_changer_capacity.md) - Number of samples in automatic sample changer
 * [➞temperature_control_range](sAXSInstrument__temperature_control_range.md) - Temperature control range in Celsius
 * [➞buffer_matching_protocol](sAXSPreparation__buffer_matching_protocol.md) - Protocol for buffer matching
 * [➞cell_path_length](sAXSPreparation__cell_path_length.md) - Path length, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞concentration_series](sAXSPreparation__concentration_series.md) - Concentration values for series measurements
 * [➞sample_cell_type](sAXSPreparation__sample_cell_type.md) - Type of sample cell used
 * [➞temperature_control](sAXSPreparation__temperature_control.md) - Temperature control settings
 * [➞affinity_column](samplePreparation__affinity_column.md) - Affinity column specifications
 * [➞affinity_type](samplePreparation__affinity_type.md) - Type of affinity chromatography
 * [➞aggregation_assessment](samplePreparation__aggregation_assessment.md) - Assessment of protein aggregation state
 * [➞aliquoting](samplePreparation__aliquoting.md) - How the protein was aliquoted for storage
 * [➞antibiotic_selection](samplePreparation__antibiotic_selection.md) - Antibiotic or selection agent used
 * [➞cleavage_temperature_c](samplePreparation__cleavage_temperature_c.md) - Temperature during cleavage in Celsius
 * [➞cleavage_time_h](samplePreparation__cleavage_time_h.md) - Duration of protease cleavage in hours
 * [➞concentration_method](samplePreparation__concentration_method.md) - Method used to concentrate protein
 * [➞culture_volume_l](samplePreparation__culture_volume_l.md) - Culture volume, typically specified in liters (L). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞elution_buffer](samplePreparation__elution_buffer.md) - Buffer composition for elution
 * [➞expression_system](samplePreparation__expression_system.md) - Expression system used for recombinant protein production
 * [➞final_buffer](samplePreparation__final_buffer.md) - Final buffer composition after purification
 * [➞final_concentration_mg_per_ml](samplePreparation__final_concentration_mg_per_ml.md) - Final protein concentration in mg/mL
 * [➞growth_temperature_c](samplePreparation__growth_temperature_c.md) - Growth temperature, typically specified in degrees Celsius. Data providers may specify alternative units (e.g., Kelvin) by including the unit in the QuantityValue.
 * [➞harvest_timepoint](samplePreparation__harvest_timepoint.md) - Time point when cells were harvested
 * [➞hic_column](samplePreparation__hic_column.md) - Hydrophobic interaction column used
 * [➞host_strain_or_cell_line](samplePreparation__host_strain_or_cell_line.md) - Specific strain or cell line used (e.g., BL21(DE3), Sf9, HEK293F)
 * [➞iex_column](samplePreparation__iex_column.md) - Ion-exchange column used
 * [➞inducer_concentration](samplePreparation__inducer_concentration.md) - Concentration of induction agent
 * [➞induction_agent](samplePreparation__induction_agent.md) - Agent used to induce expression (e.g., IPTG, tetracycline)
 * [➞induction_temperature_c](samplePreparation__induction_temperature_c.md) - Temperature during induction, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞induction_time_h](samplePreparation__induction_time_h.md) - Duration of induction, typically specified in hours. Data providers may specify alternative units (e.g., minutes, seconds) by including the unit in the QuantityValue.
 * [➞lysis_buffer](samplePreparation__lysis_buffer.md) - Buffer composition for lysis
 * [➞lysis_method](samplePreparation__lysis_method.md) - Method used for cell lysis
 * [➞medium](samplePreparation__medium.md) - Growth medium used
 * [➞od600_at_induction](samplePreparation__od600_at_induction.md) - Optical density at 600nm when induction was started. Data providers may include unit information in the QuantityValue if needed.
 * [➞operator_id](samplePreparation__operator_id.md) - Identifier or name of the person who performed the sample preparation (e.g., 'jsmith', 'John Smith', or personnel ID)
 * [➞preparation_date](samplePreparation__preparation_date.md) - Date of sample preparation
 * [➞preparation_type](samplePreparation__preparation_type.md) - Type of sample preparation
 * [➞protease](samplePreparation__protease.md) - Protease used for tag cleavage
 * [➞protease_inhibitors](samplePreparation__protease_inhibitors.md) - Protease inhibitors added
 * [➞protease_ratio](samplePreparation__protease_ratio.md) - Ratio of protease to protein
 * [➞protocol_description](samplePreparation__protocol_description.md) - Detailed protocol description
 * [➞purification_steps](samplePreparation__purification_steps.md) - Ordered list of purification steps performed
 * [➞purity_by_sds_page_percent](samplePreparation__purity_by_sds_page_percent.md) - Purity percentage by SDS-PAGE
 * [➞sample_id](samplePreparation__sample_id.md) - Reference to the sample being prepared
 * [➞sec_buffer](samplePreparation__sec_buffer.md) - Buffer for size-exclusion chromatography
 * [➞sec_column](samplePreparation__sec_column.md) - Size-exclusion column used
 * [➞second_affinity_reverse](samplePreparation__second_affinity_reverse.md) - Second affinity or reverse affinity step
 * [➞tag_removal](samplePreparation__tag_removal.md) - Whether and how affinity tag was removed
 * [➞wash_buffer](samplePreparation__wash_buffer.md) - Buffer composition for washing
 * [➞yield_mg](samplePreparation__yield_mg.md) - Total yield in milligrams
 * [➞anatomy](sample__anatomy.md) - Anatomical part or tissue (e.g., UBERON:0008945 for leaf)
 * [➞biophysical_properties](sample__biophysical_properties.md) - Measured or predicted biophysical properties
 * [➞buffer_composition](sample__buffer_composition.md) - Buffer composition including pH, salts, additives
 * [➞cell_type](sample__cell_type.md) - Cell type if applicable (e.g., CL:0000057 for fibroblast)
 * [➞concentration](sample__concentration.md) - Sample concentration, typically specified in mg/mL or µM. Data providers may specify alternative units (e.g., molar, g/L) by including the unit in the QuantityValue.
 * [➞conformational_ensemble](sample__conformational_ensemble.md) - Conformational states and dynamics
 * [➞construct](sample__construct.md) - Construct description (e.g., domain boundaries, truncations)
 * [➞database_cross_references](sample__database_cross_references.md) - Cross-references to external databases
 * [➞evolutionary_conservation](sample__evolutionary_conservation.md) - Evolutionary conservation data
 * [➞expression_system](sample__expression_system.md) - Expression system used
 * [➞functional_sites](sample__functional_sites.md) - Functional site annotations for proteins in the sample
 * [➞ligand](sample__ligand.md) - Ligand or small molecule bound to sample
 * [➞ligand_interactions](sample__ligand_interactions.md) - Small molecule interaction annotations
 * [➞molecular_composition](sample__molecular_composition.md) - Description of molecular composition including sequences, modifications, ligands
 * [➞molecular_weight](sample__molecular_weight.md) - Molecular weight, typically specified in kilodaltons (kDa). Data providers may specify alternative units (e.g., Daltons, g/mol) by including the unit in the QuantityValue.
 * [➞mutation_effects](sample__mutation_effects.md) - Effects of mutations present in the sample
 * [➞mutations](sample__mutations.md) - Mutations present in the sample
 * [➞organism](sample__organism.md) - Source organism for the sample (e.g., NCBITaxon:3702 for Arabidopsis thaliana)
 * [➞parent_sample_id](sample__parent_sample_id.md) - Reference to parent sample for derivation tracking
 * [➞preparation_method](sample__preparation_method.md) - Method used to prepare the sample
 * [➞protein_interactions](sample__protein_interactions.md) - Protein-protein interaction annotations
 * [➞protein_name](sample__protein_name.md) - Name of the protein
 * [➞ptm_annotations](sample__ptm_annotations.md) - Post-translational modification annotations
 * [➞purity_percentage](sample__purity_percentage.md) - Sample purity, typically specified as a percentage (range: 0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
 * [➞quality_metrics](sample__quality_metrics.md) - Quality control metrics for the sample
 * [➞sample_code](sample__sample_code.md) - Human-friendly laboratory identifier or facility code for the sample (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference and tracking within laboratory workflows.
 * [➞sample_type](sample__sample_type.md) - Type of biological sample
 * [➞storage_conditions](sample__storage_conditions.md) - Storage conditions for the sample
 * [➞structural_features](sample__structural_features.md) - Structural feature annotations
 * [➞tag](sample__tag.md) - Affinity tag (e.g., His6, GST, MBP)
 * [➞atmosphere](storageConditions__atmosphere.md) - Storage atmosphere conditions
 * [➞duration](storageConditions__duration.md) - Storage duration
 * [➞temperature](storageConditions__temperature.md) - Storage temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞backbone_flexibility](structuralFeature__backbone_flexibility.md) - B-factor or flexibility measure
 * [➞conformational_state](structuralFeature__conformational_state.md) - Conformational state descriptor
 * [➞disorder_probability](structuralFeature__disorder_probability.md) - Probability of disorder (range: 0-1)
 * [➞domain_assignment](structuralFeature__domain_assignment.md) - Domain database assignment (CATH, SCOP, Pfam)
 * [➞domain_id](structuralFeature__domain_id.md) - Domain identifier from domain database
 * [➞feature_type](structuralFeature__feature_type.md) - Type of structural feature
 * [➞secondary_structure](structuralFeature__secondary_structure.md) - Secondary structure assignment
 * [➞solvent_accessibility](structuralFeature__solvent_accessibility.md) - Relative solvent accessible surface area (range: 0-1)
 * [➞structural_motif](structuralFeature__structural_motif.md) - Known structural motif
 * [➞aggregated_protein_views](study__aggregated_protein_views.md) - Aggregated functional and structural annotations for proteins in this study
 * [➞data_files](study__data_files.md) - Data files generated or used in this study
 * [➞images](study__images.md) - Images acquired or generated in this study
 * [➞instrument_runs](study__instrument_runs.md) - Experimental data collection runs performed in this study
 * [➞protein_constructs](study__protein_constructs.md) - Protein constructs and cloning information
 * [➞sample_preparations](study__sample_preparations.md) - Sample preparation procedures performed in this study
 * [➞samples](study__samples.md) - Experimental samples used in this study, including biological samples
 * [➞workflow_runs](study__workflow_runs.md) - Computational workflow executions for data processing in this study
 * [➞value](textValue__value.md) - The text value
 * [➞value_cv_id](textValue__value_cv_id.md) - For values in a controlled vocabulary, the CV ID for the value.
 * [unit](unit.md) - The unit of measurement. Should be taken from the UCUM unit collection or the Unit Ontology. Examples include Angstroms, micrometers, kilodaltons, degrees.
     * [QuantityValue➞unit](QuantityValue_unit.md) - The unit of measurement (e.g., "Angstroms", "micrometers", "kilodaltons"). Should match the UCUM standard notation or Unit Ontology.
 * [unit_cv_id](unit_cv_id.md) - The unit of the quantity, expressed as a CURIE from the Unit Ontology (e.g., UO:0000016 for micrometer).
 * [value](value.md) - The value, as a text string.
 * [value_cv_id](value_cv_id.md) - For values that are in a controlled vocabulary (CV), this attribute should capture the controlled vocabulary ID for the value.
 * [➞additional_software](workflowRun__additional_software.md) - Additional software used in pipeline
 * [➞anomalous_completeness](workflowRun__anomalous_completeness.md) - Completeness of anomalous data as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
 * [➞anomalous_multiplicity](workflowRun__anomalous_multiplicity.md) - Multiplicity of anomalous data
 * [➞cc_anomalous](workflowRun__cc_anomalous.md) - Anomalous correlation coefficient
 * [➞cc_half](workflowRun__cc_half.md) - Half-set correlation coefficient CC(1/2)
 * [➞clashscore](workflowRun__clashscore.md) - MolProbity clashscore
 * [➞completed_at](workflowRun__completed_at.md) - Workflow completion time
 * [➞completeness_percent](workflowRun__completeness_percent.md) - Data completeness as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
 * [➞compute_resources](workflowRun__compute_resources.md) - Computational resources used
 * [➞ctf_estimation_params](workflowRun__ctf_estimation_params.md) - CTF estimation specific parameters
 * [➞deposited_to_pdb](workflowRun__deposited_to_pdb.md) - Whether structure was deposited to PDB
 * [➞experiment_id](workflowRun__experiment_id.md) - Reference to the source experiment
 * [➞fsc_curve](workflowRun__fsc_curve.md) - Fourier Shell Correlation curve data
 * [➞i_over_sigma](workflowRun__i_over_sigma.md) - Mean I/sigma(I) - signal to noise ratio
 * [➞indexer_module](workflowRun__indexer_module.md) - Indexing module used (e.g., MOSFLM, XDS)
 * [➞integrator_module](workflowRun__integrator_module.md) - Integration module used
 * [➞ispyb_auto_proc_program_id](workflowRun__ispyb_auto_proc_program_id.md) - ISPyB AutoProcProgram.autoProcProgramId
 * [➞ispyb_auto_proc_scaling_id](workflowRun__ispyb_auto_proc_scaling_id.md) - ISPyB AutoProcScaling.autoProcScalingId
 * [➞ligands_cofactors](workflowRun__ligands_cofactors.md) - Ligands or cofactors modeled in the structure
 * [➞motion_correction_params](workflowRun__motion_correction_params.md) - Motion correction specific parameters
 * [➞multiplicity](workflowRun__multiplicity.md) - Data multiplicity (redundancy)
 * [➞n_total_observations](workflowRun__n_total_observations.md) - Total number of observations (before merging)
 * [➞n_total_unique](workflowRun__n_total_unique.md) - Total number of unique reflections
 * [➞ncs_used](workflowRun__ncs_used.md) - Whether Non-Crystallographic Symmetry restraints were used
 * [➞number_of_waters](workflowRun__number_of_waters.md) - Number of water molecules modeled
 * [➞outlier_rejection_method](workflowRun__outlier_rejection_method.md) - Method for rejecting outlier reflections
 * [➞output_files](workflowRun__output_files.md) - Output files generated
 * [➞parameters_file_path](workflowRun__parameters_file_path.md) - Path to parameters file or text of key parameters
 * [➞particle_picking_params](workflowRun__particle_picking_params.md) - Particle picking specific parameters
 * [➞pdb_id](workflowRun__pdb_id.md) - PDB accession code if deposited
 * [➞phasing_method](workflowRun__phasing_method.md) - Phasing method used for X-ray crystallography structure determination
 * [➞processing_level](workflowRun__processing_level.md) - Processing level (0=raw, 1=corrected, 2=derived, 3=model)
 * [➞processing_notes](workflowRun__processing_notes.md) - Additional notes about processing
 * [➞processing_parameters](workflowRun__processing_parameters.md) - Parameters used in processing
 * [➞r_anomalous](workflowRun__r_anomalous.md) - Anomalous R-factor
 * [➞ramachandran_favored](workflowRun__ramachandran_favored.md) - Percentage of residues in favored Ramachandran regions (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
 * [➞ramachandran_outliers](workflowRun__ramachandran_outliers.md) - Percentage of Ramachandran outliers (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
 * [➞refinement_params](workflowRun__refinement_params.md) - 3D refinement specific parameters
 * [➞refinement_resolution_a](workflowRun__refinement_resolution_a.md) - Resolution cutoff used for refinement in Angstroms
 * [➞resolution_high](workflowRun__resolution_high.md) - High resolution limit, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞resolution_low](workflowRun__resolution_low.md) - Low resolution limit, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞restraints_other](workflowRun__restraints_other.md) - Other restraints applied during refinement
 * [➞rfree](workflowRun__rfree.md) - R-free (test set)
 * [➞rmerge](workflowRun__rmerge.md) - Rmerge - merge R-factor
 * [➞rmsd_angles](workflowRun__rmsd_angles.md) - RMSD from ideal bond angles, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞rmsd_bonds](workflowRun__rmsd_bonds.md) - RMSD from ideal bond lengths, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞rpim](workflowRun__rpim.md) - Rpim - precision-indicating merging R-factor
 * [➞rwork](workflowRun__rwork.md) - Refinement R-factor (working set)
 * [➞scaler_module](workflowRun__scaler_module.md) - Scaling module used (e.g., AIMLESS, SCALA)
 * [➞search_model_pdb_id](workflowRun__search_model_pdb_id.md) - PDB ID of search model for molecular replacement
 * [➞sig_anomalous](workflowRun__sig_anomalous.md) - Mean anomalous difference signal
 * [➞software_name](workflowRun__software_name.md) - Software used for processing
 * [➞software_version](workflowRun__software_version.md) - Software version
 * [➞space_group](workflowRun__space_group.md) - Crystallographic space group
 * [➞started_at](workflowRun__started_at.md) - Workflow start time
 * [➞tls_used](workflowRun__tls_used.md) - Whether TLS (Translation/Libration/Screw) refinement was used
 * [➞unit_cell_a](workflowRun__unit_cell_a.md) - Unit cell parameter a, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_alpha](workflowRun__unit_cell_alpha.md) - Unit cell angle alpha, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_b](workflowRun__unit_cell_b.md) - Unit cell parameter b, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_beta](workflowRun__unit_cell_beta.md) - Unit cell angle beta, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_c](workflowRun__unit_cell_c.md) - Unit cell parameter c, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞unit_cell_gamma](workflowRun__unit_cell_gamma.md) - Unit cell angle gamma, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞validation_report_path](workflowRun__validation_report_path.md) - Path to validation report
 * [➞wilson_b_factor](workflowRun__wilson_b_factor.md) - Wilson B-factor, typically specified in Angstroms squared (Ų). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞workflow_code](workflowRun__workflow_code.md) - Human-friendly identifier for the computational workflow run (e.g., 'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing pipelines and computational provenance.
 * [➞workflow_type](workflowRun__workflow_type.md) - Type of processing workflow
 * [➞beam_energy](xRFImage__beam_energy.md) - X-ray beam energy, typically specified in kiloelectronvolts (keV). Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞beam_size](xRFImage__beam_size.md) - X-ray beam size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞calibration_standard](xRFImage__calibration_standard.md) - Reference standard used for calibration
 * [➞detector_model](xRFImage__detector_model.md) - Specific detector model used for XRF measurement
 * [➞detector_technology](xRFImage__detector_technology.md) - Type of X-ray detector technology used
 * [➞dwell_time](xRFImage__dwell_time.md) - Dwell time per pixel, typically specified in milliseconds. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞elements_measured](xRFImage__elements_measured.md) - Elements detected and measured
 * [➞flux](xRFImage__flux.md) - Photon flux, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞source_type](xRFImage__source_type.md) - X-ray source type (synchrotron or lab-source)
 * [➞beam_size_max](xRayInstrument__beam_size_max.md) - Maximum beam size in micrometers
 * [➞beam_size_min](xRayInstrument__beam_size_min.md) - Minimum beam size in micrometers
 * [➞crystal_cooling_capability](xRayInstrument__crystal_cooling_capability.md) - Crystal cooling system available
 * [➞detector_manufacturer](xRayInstrument__detector_manufacturer.md) - Detector manufacturer (e.g., Dectris, Bruker, Rigaku, Rayonix)
 * [➞detector_model](xRayInstrument__detector_model.md) - Detector model (e.g., EIGER2 X 16M, PILATUS3 X 6M, PHOTON III)
 * [➞detector_technology](xRayInstrument__detector_technology.md) - Generic detector technology type
 * [➞energy_max](xRayInstrument__energy_max.md) - Maximum X-ray energy in keV
 * [➞energy_min](xRayInstrument__energy_min.md) - Minimum X-ray energy in keV
 * [➞flux_density](xRayInstrument__flux_density.md) - Photon flux density in photons/s/mm²
 * [➞goniometer_type](xRayInstrument__goniometer_type.md) - Type of goniometer
 * [➞monochromator_type](xRayInstrument__monochromator_type.md) - Type of monochromator
 * [➞source_type](xRayInstrument__source_type.md) - Type of X-ray source
 * [➞additives](xRayPreparation__additives.md) - Additives mixed with protein before crystallization
 * [➞cryoprotectant](xRayPreparation__cryoprotectant.md) - Cryoprotectant used
 * [➞cryoprotectant_concentration](xRayPreparation__cryoprotectant_concentration.md) - Cryoprotectant concentration, typically specified as a percentage. Data providers may specify as decimal fraction by including the unit in the QuantityValue.
 * [➞crystal_notes](xRayPreparation__crystal_notes.md) - Additional notes about crystal quality and handling
 * [➞crystal_size_um](xRayPreparation__crystal_size_um.md) - Crystal dimensions in micrometers
 * [➞crystallization_conditions](xRayPreparation__crystallization_conditions.md) - Detailed crystallization conditions
 * [➞crystallization_method](xRayPreparation__crystallization_method.md) - Method used for crystallization
 * [➞drop_ratio_protein_to_reservoir](xRayPreparation__drop_ratio_protein_to_reservoir.md) - Ratio of protein to reservoir solution in drop (e.g., 1:1, 2:1)
 * [➞drop_volume_nl](xRayPreparation__drop_volume_nl.md) - Total drop volume, typically specified in nanoliters. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞flash_cooling_method](xRayPreparation__flash_cooling_method.md) - Flash cooling protocol
 * [➞initial_hit_condition](xRayPreparation__initial_hit_condition.md) - Description of initial crystallization hit condition
 * [➞loop_size](xRayPreparation__loop_size.md) - Loop size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞mounting_method](xRayPreparation__mounting_method.md) - Crystal mounting method
 * [➞mounting_temperature](xRayPreparation__mounting_temperature.md) - Temperature during mounting, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞optimization_strategy](xRayPreparation__optimization_strategy.md) - Strategy used to optimize crystals
 * [➞optimized_condition](xRayPreparation__optimized_condition.md) - Final optimized crystallization condition
 * [➞protein_buffer](xRayPreparation__protein_buffer.md) - Buffer composition for protein solution
 * [➞protein_concentration_mg_per_ml](xRayPreparation__protein_concentration_mg_per_ml.md) - Protein concentration for crystallization in mg/mL
 * [➞reservoir_volume_ul](xRayPreparation__reservoir_volume_ul.md) - Reservoir volume, typically specified in microliters. Data providers may specify alternative units by including the unit in the QuantityValue.
 * [➞screen_name](xRayPreparation__screen_name.md) - Name of crystallization screen used
 * [➞seed_stock_dilution](xRayPreparation__seed_stock_dilution.md) - Dilution factor for seed stock
 * [➞seeding_type](xRayPreparation__seeding_type.md) - Type of seeding used (micro, macro, streak)
 * [➞soak_compound](xRayPreparation__soak_compound.md) - Compound used for soaking (ligand, heavy atom)
 * [➞soak_conditions](xRayPreparation__soak_conditions.md) - Conditions for crystal soaking
 * [➞temperature_c](xRayPreparation__temperature_c.md) - Crystallization temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.

### Enums

 * [AffinityUnitEnum](AffinityUnitEnum.md) - Units for affinity measurements
 * [AnnotationSourceEnum](AnnotationSourceEnum.md) - Sources of functional annotations
 * [BindingAffinityTypeEnum](BindingAffinityTypeEnum.md) - Types of binding affinity measurements
 * [BiophysicalMethodEnum](BiophysicalMethodEnum.md) - Methods for biophysical measurements
 * [BiophysicalPropertyEnum](BiophysicalPropertyEnum.md) - Types of biophysical properties
 * [ClinicalSignificanceEnum](ClinicalSignificanceEnum.md) - Clinical significance of variants
 * [CollectionModeEnum](CollectionModeEnum.md) - Data collection modes
 * [ComplexStabilityEnum](ComplexStabilityEnum.md) - Stability of protein complexes
 * [ConformationalStateEnum](ConformationalStateEnum.md) - Conformational states
 * [CrystallizationMethodEnum](CrystallizationMethodEnum.md) - Methods for protein crystallization
 * [DataTypeEnum](DataTypeEnum.md) - Types of data
 * [DatabaseNameEnum](DatabaseNameEnum.md) - External database names
 * [DetectorModeEnum](DetectorModeEnum.md) - Operating modes for detectors during data collection
 * [DetectorTechnologyEnum](DetectorTechnologyEnum.md) - Generic detector technologies for structural biology imaging
 * [DetectorTypeEnum](DetectorTypeEnum.md) - DEPRECATED: Use DetectorTechnologyEnum instead. Legacy enum mixing technologies and brands.
 * [EvidenceTypeEnum](EvidenceTypeEnum.md) - Types of evidence
 * [ExperimentalMethodEnum](ExperimentalMethodEnum.md) - Experimental methods for structure determination
 * [ExpressionSystemEnum](ExpressionSystemEnum.md) - Expression systems for recombinant protein production
 * [FacilityEnum](FacilityEnum.md) - Major synchrotron and structural biology research facilities worldwide
 * [FacilityTypeEnum](FacilityTypeEnum.md) - Types of research facilities
 * [FileFormatEnum](FileFormatEnum.md) - File formats
 * [FunctionalEffectEnum](FunctionalEffectEnum.md) - Effect on protein function
 * [FunctionalSiteTypeEnum](FunctionalSiteTypeEnum.md) - Types of functional sites in proteins
 * [GridMaterialEnum](GridMaterialEnum.md) - Materials used for EM grids
 * [GridTypeEnum](GridTypeEnum.md) - Types of EM grids
 * [IlluminationTypeEnum](IlluminationTypeEnum.md) - Types of illumination for optical microscopy
 * [ImagingModeEnum](ImagingModeEnum.md) - Imaging modes for electron microscopy
 * [InstrumentCategoryEnum](InstrumentCategoryEnum.md) - Categories of instruments based on their nature and location
 * [InstrumentStatusEnum](InstrumentStatusEnum.md) - Operational status of instruments
 * [InteractionEvidenceEnum](InteractionEvidenceEnum.md) - Evidence for interactions
 * [InteractionTypeEnum](InteractionTypeEnum.md) - Types of molecular interactions
 * [MutationTypeEnum](MutationTypeEnum.md) - Types of mutations
 * [PTMTypeEnum](PTMTypeEnum.md) - Types of post-translational modifications
 * [PhasingMethodEnum](PhasingMethodEnum.md) - Methods for phase determination in X-ray crystallography
 * [PreparationTypeEnum](PreparationTypeEnum.md) - Types of sample preparation
 * [ProcessingStatusEnum](ProcessingStatusEnum.md) - Processing status
 * [PurificationStepEnum](PurificationStepEnum.md) - Protein purification steps and methods
 * [SampleTypeEnum](SampleTypeEnum.md) - Types of biological samples
 * [SecondaryStructureEnum](SecondaryStructureEnum.md) - Secondary structure types
 * [StabilityEffectEnum](StabilityEffectEnum.md) - Effect on protein stability
 * [StructuralFeatureTypeEnum](StructuralFeatureTypeEnum.md) - Types of structural features
 * [SymmetryEnum](SymmetryEnum.md) - Crystallographic and non-crystallographic symmetry groups for cryo-EM
 * [TechniqueEnum](TechniqueEnum.md) - Structural biology techniques
 * [VitrificationMethodEnum](VitrificationMethodEnum.md) - Methods for vitrification
 * [WorkflowTypeEnum](WorkflowTypeEnum.md) - Types of processing workflows
 * [XRaySourceTypeEnum](XRaySourceTypeEnum.md) - Types of X-ray sources

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [DecimalDegree](types/DecimalDegree.md)  (**float**)  - A decimal degree expresses latitude or longitude as decimal fractions.
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [SmilesString](types/SmilesString.md)  ([String](types/String.md))  - A SMILES representation of a chemical structure
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
