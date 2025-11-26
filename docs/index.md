# lambda-ber-schema

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


URI: https://w3id.org/lambda-ber-schema/

Name: lambda-ber-schema



## Classes

| Class | Description |
| --- | --- |
| [AttributeGroup](AttributeGroup.md) | A grouping of related data attributes that form a logical unit |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BufferComposition](BufferComposition.md) | Buffer composition for sample storage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComputeResources](ComputeResources.md) | Computational resources used |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConformationalState](ConformationalState.md) | Individual conformational state |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CrystallizationConditions](CrystallizationConditions.md) | Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization ma... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CTFEstimationParameters](CTFEstimationParameters.md) | Parameters specific to CTF estimation workflows |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DatabaseCrossReference](DatabaseCrossReference.md) | Cross-references to external databases |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentalConditions](ExperimentalConditions.md) | Environmental and experimental conditions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FSCCurve](FSCCurve.md) | Fourier Shell Correlation curve data |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ImageFeature](ImageFeature.md) | Semantic annotations describing features identified in images using controlle... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LigandInteraction](LigandInteraction.md) | Small molecule/ligand interactions with proteins |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularComposition](MolecularComposition.md) | Molecular composition of a sample |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MotionCorrectionParameters](MotionCorrectionParameters.md) | Parameters specific to motion correction workflows |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ParticlePickingParameters](ParticlePickingParameters.md) | Parameters specific to particle picking workflows |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QualityMetrics](QualityMetrics.md) | Quality metrics for experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RefinementParameters](RefinementParameters.md) | Parameters specific to 3D refinement workflows |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StorageConditions](StorageConditions.md) | Storage conditions for samples |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) | Base class for technique-specific preparation details |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CryoEMPreparation](CryoEMPreparation.md) | Cryo-EM specific sample preparation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SAXSPreparation](SAXSPreparation.md) | SAXS/WAXS specific preparation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |
| [NamedThing](NamedThing.md) | A named thing |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataFile](DataFile.md) | A data file generated or used in the study |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dataset](Dataset.md) | A collection of studies |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentRun](ExperimentRun.md) | An experimental data collection session |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image](Image.md) | An image file from structural biology experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Micrograph](Micrograph.md) | Motion-corrected micrograph derived from movie |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image3D](Image3D.md) | A 3D volume or tomogram |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Instrument](Instrument.md) | An instrument used to collect data |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SAXSInstrument](SAXSInstrument.md) | SAXS/WAXS instrument specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OntologyTerm](OntologyTerm.md) | A term from a controlled vocabulary or ontology |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinConstruct](ProteinConstruct.md) | Detailed information about a protein construct including cloning and sequence... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sample](Sample.md) | A biological sample used in structural biology experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Study](Study.md) | A focused research investigation that groups related samples, experiments, an... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |



## Slots

| Slot | Description |
| --- | --- |
| [accelerating_voltage](accelerating_voltage.md) | Accelerating voltage in kV |
| [acquisition_date](acquisition_date.md) | Date image was acquired |
| [acquisition_group](acquisition_group.md) | Acquisition group identifier (e |
| [acquisition_software](acquisition_software.md) | Acquisition software used (e |
| [acquisition_software_version](acquisition_software_version.md) | Version of acquisition software |
| [additional_software](additional_software.md) | Additional software used in pipeline |
| [additives](additives.md) | Additional additives in the buffer |
| [affinity_column](affinity_column.md) | Affinity column specifications |
| [affinity_type](affinity_type.md) | Type of affinity chromatography |
| [aggregated_protein_views](aggregated_protein_views.md) | Aggregated functional and structural annotations for proteins in this study |
| [aggregation_assessment](aggregation_assessment.md) | Assessment of protein aggregation state |
| [alignment_depth](alignment_depth.md) | Number of sequences in alignment |
| [aliquoting](aliquoting.md) | How the protein was aliquoted for storage |
| [allele_frequency](allele_frequency.md) | Population allele frequency (range: 0-1) |
| [amplitude_contrast](amplitude_contrast.md) | Amplitude contrast value |
| [anatomy](anatomy.md) | Anatomical part or tissue (e |
| [anisotropic_correction](anisotropic_correction.md) | Whether anisotropic motion correction was applied |
| [annotation_method](annotation_method.md) | Computational or experimental method used |
| [anom_corr](anom_corr.md) | Anomalous correlation |
| [anom_sig_ano](anom_sig_ano.md) | Anomalous signal strength |
| [anomalous_used](anomalous_used.md) | Whether anomalous signal was used |
| [antibiotic_selection](antibiotic_selection.md) | Antibiotic or selection agent used |
| [apodization_function](apodization_function.md) | Mathematical function used for apodization |
| [astigmatism](astigmatism.md) | Astigmatism value in Angstroms |
| [astigmatism_angle](astigmatism_angle.md) | Astigmatism angle in degrees |
| [astigmatism_target](astigmatism_target.md) | Target astigmatism in Angstroms |
| [atmosphere](atmosphere.md) | Storage atmosphere conditions |
| [attenuator](attenuator.md) | Attenuator setting used |
| [autoloader_capacity](autoloader_capacity.md) | Number of grids the autoloader can hold |
| [autoloader_slot](autoloader_slot.md) | Autoloader slot identifier |
| [average_b_factor_a2](average_b_factor_a2.md) | Average B-factor in Angstroms squared |
| [backbone_flexibility](backbone_flexibility.md) | B-factor or flexibility measure |
| [background_correction](background_correction.md) | Method used for background correction |
| [beam_center_x](beam_center_x.md) | Beam center X coordinate |
| [beam_center_x_px](beam_center_x_px.md) | Beam center X coordinate in pixels |
| [beam_center_y](beam_center_y.md) | Beam center Y coordinate |
| [beam_center_y_px](beam_center_y_px.md) | Beam center Y coordinate in pixels |
| [beam_energy](beam_energy.md) | X-ray beam energy in keV |
| [beam_shift_x](beam_shift_x.md) | Beam shift X in microradians |
| [beam_shift_y](beam_shift_y.md) | Beam shift Y in microradians |
| [beam_size](beam_size.md) | X-ray beam size in micrometers |
| [beam_size_max](beam_size_max.md) | Maximum beam size in micrometers |
| [beam_size_min](beam_size_min.md) | Minimum beam size in micrometers |
| [beam_size_um](beam_size_um.md) | Beam size in micrometers |
| [beamline](beamline.md) | Beamline identifier (e |
| [beamline_id](beamline_id.md) | Beamline identifier at synchrotron facility |
| [bfactor_dose_weighting](bfactor_dose_weighting.md) | B-factor for dose weighting |
| [binding_affinity](binding_affinity.md) | Binding affinity value |
| [binding_affinity_type](binding_affinity_type.md) | Type of binding measurement (Kd, Ki, IC50) |
| [binding_affinity_unit](binding_affinity_unit.md) | Unit of binding affinity |
| [binding_energy](binding_energy.md) | Calculated binding energy (kcal/mol) |
| [binding_site_residues](binding_site_residues.md) | Residues involved in ligand binding |
| [binning](binning.md) | Binning factor applied during motion correction |
| [biological_assembly](biological_assembly.md) | Whether this represents a biological assembly |
| [biophysical_properties](biophysical_properties.md) | Measured or predicted biophysical properties |
| [blot_force](blot_force.md) | Blotting force setting |
| [blot_number](blot_number.md) | Number of blots applied |
| [blot_time](blot_time.md) | Blotting time in seconds (range: 0 |
| [blotter_height](blotter_height.md) | Blotter height setting |
| [blotter_setting](blotter_setting.md) | Blotter setting value |
| [box_size](box_size.md) | Particle box size in pixels |
| [buffer_composition](buffer_composition.md) | Buffer composition including pH, salts, additives |
| [buffer_matching_protocol](buffer_matching_protocol.md) | Protocol for buffer matching |
| [c2_aperture](c2_aperture.md) | C2 aperture size in micrometers |
| [calibrated_pixel_size](calibrated_pixel_size.md) | Calibrated pixel size in Angstroms per pixel |
| [calibration_standard](calibration_standard.md) | Reference standard used for calibration |
| [camera_binning](camera_binning.md) | Camera binning factor |
| [cc_half](cc_half.md) | Half-set correlation coefficient CC(1/2) |
| [cell_path_length](cell_path_length.md) | Path length in mm |
| [cell_type](cell_type.md) | Cell type if applicable (e |
| [chain_id](chain_id.md) | Chain identifier in the PDB structure |
| [chamber_temperature](chamber_temperature.md) | Chamber temperature in Celsius |
| [channel_name](channel_name.md) | Name of the fluorescence channel (e |
| [characteristic_features](characteristic_features.md) | Key features of this conformation |
| [checksum](checksum.md) | SHA-256 checksum for data integrity |
| [clashscore](clashscore.md) | MolProbity clashscore |
| [cleavage_site](cleavage_site.md) | Protease cleavage site sequence |
| [cleavage_temperature_c](cleavage_temperature_c.md) | Temperature during cleavage in Celsius |
| [cleavage_time_h](cleavage_time_h.md) | Duration of protease cleavage in hours |
| [clinical_significance](clinical_significance.md) | Clinical significance |
| [cloning_method](cloning_method.md) | Method used for cloning (e |
| [clustering_method](clustering_method.md) | Method used for conformational clustering |
| [codon_optimization_organism](codon_optimization_organism.md) | Organism for which codons were optimized |
| [coevolved_residues](coevolved_residues.md) | Pairs of coevolved residues |
| [collection_mode](collection_mode.md) | Mode of data collection |
| [color_channels](color_channels.md) | Color channels present (e |
| [coma](coma.md) | Coma aberration in nanometers |
| [completed_at](completed_at.md) | Workflow completion time |
| [completeness](completeness.md) | Data completeness percentage |
| [completeness_high_res_shell_percent](completeness_high_res_shell_percent.md) | Completeness in highest resolution shell |
| [completeness_percent](completeness_percent.md) | Data completeness percentage |
| [complex_stability](complex_stability.md) | Stability assessment of the complex |
| [components](components.md) | Buffer components and their concentrations |
| [compute_resources](compute_resources.md) | Computational resources used |
| [concentration](concentration.md) | Sample concentration in mg/mL or µM |
| [concentration_method](concentration_method.md) | Method used to concentrate protein |
| [concentration_series](concentration_series.md) | Concentration values for series measurements |
| [concentration_unit](concentration_unit.md) | Unit of concentration measurement |
| [confidence_score](confidence_score.md) | Confidence score for the annotation (range: 0-1) |
| [conformational_ensemble](conformational_ensemble.md) | Conformational states and dynamics |
| [conformational_state](conformational_state.md) | Conformational state descriptor |
| [conformational_states](conformational_states.md) | Individual conformational states |
| [conservation_method](conservation_method.md) | Method used for conservation analysis |
| [conservation_score](conservation_score.md) | Evolutionary conservation score (range: 0-1) |
| [conserved_residues](conserved_residues.md) | Highly conserved residues |
| [construct](construct.md) | Construct description (e |
| [construct_description](construct_description.md) | Human-readable description of the construct |
| [construct_id](construct_id.md) | Unique identifier for this construct |
| [contrast_method](contrast_method.md) | Contrast enhancement method used |
| [cpu_hours](cpu_hours.md) | CPU hours used |
| [creation_date](creation_date.md) | File creation date |
| [cross_references](cross_references.md) | Database cross-references |
| [cryo_protectant](cryo_protectant.md) | Cryoprotectant used for crystal cooling |
| [cryoprotectant](cryoprotectant.md) | Cryoprotectant used |
| [cryoprotectant_concentration](cryoprotectant_concentration.md) | Cryoprotectant concentration percentage |
| [crystal_cooling_capability](crystal_cooling_capability.md) | Crystal cooling system available |
| [crystal_id](crystal_id.md) | Identifier for the specific crystal used |
| [crystal_notes](crystal_notes.md) | Additional notes about crystal quality and handling |
| [crystal_size_um](crystal_size_um.md) | Crystal dimensions in micrometers (length x width x height) |
| [crystallization_conditions](crystallization_conditions.md) | Complete description of crystallization conditions including precipitant, pH,... |
| [crystallization_method](crystallization_method.md) | Method used for crystallization |
| [cs](cs.md) | Spherical aberration (Cs) in millimeters |
| [cs_corrector](cs_corrector.md) | Spherical aberration corrector present |
| [cs_used_in_estimation](cs_used_in_estimation.md) | Spherical aberration (Cs) value used during CTF estimation (in millimeters); ... |
| [ctf_estimation_params](ctf_estimation_params.md) | CTF estimation specific parameters |
| [ctf_quality_score](ctf_quality_score.md) | CTF estimation quality score |
| [culture_volume_l](culture_volume_l.md) | Culture volume in liters |
| [current_status](current_status.md) | Current operational status |
| [data_collection_strategy](data_collection_strategy.md) | Strategy for data collection |
| [data_files](data_files.md) | Data files generated or used in this study |
| [data_type](data_type.md) | Type of data in the file |
| [database_cross_references](database_cross_references.md) | Cross-references to external databases |
| [database_id](database_id.md) | Identifier in the external database |
| [database_name](database_name.md) | Name of the external database |
| [database_url](database_url.md) | URL to the database entry |
| [definition](definition.md) | The formal definition or meaning of the ontology term |
| [defocus](defocus.md) | Defocus value in micrometers |
| [defocus_range_increment](defocus_range_increment.md) | Defocus range increment in micrometers |
| [defocus_range_max](defocus_range_max.md) | Maximum defocus range in micrometers |
| [defocus_range_min](defocus_range_min.md) | Minimum defocus range in micrometers |
| [defocus_search_max](defocus_search_max.md) | Maximum defocus search range in micrometers |
| [defocus_search_min](defocus_search_min.md) | Minimum defocus search range in micrometers |
| [defocus_step](defocus_step.md) | Defocus search step in micrometers |
| [defocus_target](defocus_target.md) | Target defocus value in micrometers |
| [defocus_u](defocus_u.md) | Defocus U in micrometers |
| [defocus_v](defocus_v.md) | Defocus V in micrometers |
| [delta_delta_g](delta_delta_g.md) | Change in folding free energy (kcal/mol) |
| [deposited_to_pdb](deposited_to_pdb.md) | Whether structure was deposited to PDB |
| [description](description.md) | A detailed textual description of this entity |
| [detector_dimensions](detector_dimensions.md) | Detector dimensions in pixels (e |
| [detector_distance](detector_distance.md) | Distance from sample to detector |
| [detector_distance_max](detector_distance_max.md) | Maximum detector distance in mm |
| [detector_distance_min](detector_distance_min.md) | Minimum detector distance in mm |
| [detector_distance_mm](detector_distance_mm.md) | Detector distance in millimeters |
| [detector_manufacturer](detector_manufacturer.md) | Detector manufacturer (e |
| [detector_mode](detector_mode.md) | Supported or default detector operating mode |
| [detector_model](detector_model.md) | Detector model (e |
| [detector_position](detector_position.md) | Physical position of detector in microscope (e |
| [detector_technology](detector_technology.md) | Generic detector technology type |
| [dimensions_x](dimensions_x.md) | Image width in pixels |
| [dimensions_y](dimensions_y.md) | Image height in pixels |
| [dimensions_z](dimensions_z.md) | Image depth in pixels/slices |
| [disease_association](disease_association.md) | Associated disease or phenotype |
| [disorder_probability](disorder_probability.md) | Probability of disorder (range: 0-1) |
| [dissociation_constant](dissociation_constant.md) | Experimental Kd if available |
| [domain_assignment](domain_assignment.md) | Domain database assignment (CATH, SCOP, Pfam) |
| [domain_id](domain_id.md) | Domain identifier from domain database |
| [dose](dose.md) | Electron dose in e-/Å² |
| [dose_per_frame](dose_per_frame.md) | Electron dose per frame in e-/Angstrom^2 |
| [dose_rate](dose_rate.md) | Dose rate in e-/pixel/s or e-/Angstrom^2/s |
| [dose_weighting](dose_weighting.md) | Whether dose weighting was applied |
| [drift_total](drift_total.md) | Total drift in Angstroms |
| [drop_ratio_protein_to_reservoir](drop_ratio_protein_to_reservoir.md) | Ratio of protein to reservoir solution in drop (e |
| [drop_volume](drop_volume.md) | Total drop volume in nanoliters |
| [drop_volume_nl](drop_volume_nl.md) | Total drop volume in nanoliters |
| [druggability_score](druggability_score.md) | Druggability score of the binding site (range: 0-1) |
| [duration](duration.md) | Storage duration |
| [dwell_time](dwell_time.md) | Dwell time per pixel in milliseconds |
| [ec_number](ec_number.md) | Enzyme Commission number for catalytic sites |
| [effect_on_function](effect_on_function.md) | Effect on protein function |
| [effect_on_stability](effect_on_stability.md) | Effect on protein stability |
| [elements_measured](elements_measured.md) | Elements detected and measured |
| [elution_buffer](elution_buffer.md) | Buffer composition for elution |
| [emission_filter](emission_filter.md) | Specifications of the emission filter |
| [emission_wavelength](emission_wavelength.md) | Emission wavelength in nanometers |
| [energy_filter_make](energy_filter_make.md) | Energy filter manufacturer |
| [energy_filter_model](energy_filter_model.md) | Energy filter model |
| [energy_filter_present](energy_filter_present.md) | Whether energy filter is present |
| [energy_filter_slit_width](energy_filter_slit_width.md) | Energy filter slit width in eV |
| [energy_landscape](energy_landscape.md) | Description of the energy landscape |
| [energy_max](energy_max.md) | Maximum X-ray energy in keV |
| [energy_min](energy_min.md) | Minimum X-ray energy in keV |
| [enzyme](enzyme.md) | Enzyme responsible for modification |
| [error](error.md) | Experimental error or uncertainty |
| [ethane_temperature](ethane_temperature.md) | Ethane temperature in Celsius |
| [evidence_code](evidence_code.md) | Evidence and Conclusion Ontology (ECO) code |
| [evidence_type](evidence_type.md) | Type of evidence supporting this annotation |
| [evolutionary_conservation](evolutionary_conservation.md) | Evolutionary conservation data |
| [excitation_filter](excitation_filter.md) | Specifications of the excitation filter |
| [excitation_wavelength](excitation_wavelength.md) | Excitation wavelength in nanometers |
| [experiment_code](experiment_code.md) | Human-friendly laboratory or facility identifier for the experiment (e |
| [experiment_date](experiment_date.md) | Date of the experiment |
| [experiment_id](experiment_id.md) | Reference to the source experiment |
| [experimental_conditions](experimental_conditions.md) | Environmental and experimental conditions |
| [experimental_method](experimental_method.md) | Specific experimental method for structure determination (particularly for di... |
| [exposure_time](exposure_time.md) | Exposure time in seconds |
| [exposure_time_per_frame](exposure_time_per_frame.md) | Exposure time per frame in milliseconds |
| [expression_system](expression_system.md) | Expression system used |
| [feature_type](feature_type.md) | Type of structural feature |
| [file_format](file_format.md) | File format |
| [file_name](file_name.md) | Name of the file |
| [file_path](file_path.md) | Path to the file |
| [file_role](file_role.md) | Role of the file (raw, intermediate, final, diagnostic, metadata) |
| [file_size_bytes](file_size_bytes.md) | File size in bytes |
| [final_buffer](final_buffer.md) | Final buffer composition after purification |
| [final_concentration_mg_per_ml](final_concentration_mg_per_ml.md) | Final protein concentration in mg/mL |
| [flash_cooling_method](flash_cooling_method.md) | Flash cooling protocol |
| [fluorophore](fluorophore.md) | Name or type of fluorophore used |
| [flux](flux.md) | Photon flux in photons/second |
| [flux_density](flux_density.md) | Photon flux density in photons/s/mm² |
| [flux_photons_per_s](flux_photons_per_s.md) | Photon flux in photons per second |
| [frame_grouping](frame_grouping.md) | Number of frames grouped together |
| [frame_rate](frame_rate.md) | Frames per second |
| [frames](frames.md) | Number of frames in the movie |
| [frames_per_movie](frames_per_movie.md) | Number of frames per movie |
| [free_energy](free_energy.md) | Relative free energy (kcal/mol) |
| [fsc_curve](fsc_curve.md) | Fourier Shell Correlation curve data |
| [fsc_value](fsc_value.md) | FSC values corresponding to each resolution |
| [functional_effect](functional_effect.md) | Known functional effect of this PTM |
| [functional_impact_description](functional_impact_description.md) | Description of functional impact |
| [functional_importance](functional_importance.md) | Description of functional importance |
| [functional_sites](functional_sites.md) | Functional site annotations for proteins in the sample |
| [gene_name](gene_name.md) | Gene name |
| [gene_synthesis_provider](gene_synthesis_provider.md) | Company or facility that synthesized the gene |
| [glow_discharge_applied](glow_discharge_applied.md) | Whether glow discharge treatment was applied |
| [glow_discharge_atmosphere](glow_discharge_atmosphere.md) | Glow discharge atmosphere (air, amylamine) |
| [glow_discharge_current](glow_discharge_current.md) | Glow discharge current in milliamperes |
| [glow_discharge_pressure](glow_discharge_pressure.md) | Glow discharge pressure in millibar |
| [glow_discharge_time](glow_discharge_time.md) | Glow discharge time in seconds |
| [go_terms](go_terms.md) | Associated Gene Ontology terms |
| [gold_standard](gold_standard.md) | Whether gold-standard refinement was used |
| [goniometer_type](goniometer_type.md) | Type of goniometer |
| [gpu_hours](gpu_hours.md) | GPU hours used |
| [grid_material](grid_material.md) | Grid material |
| [grid_square_id](grid_square_id.md) | Grid square identifier |
| [grid_type](grid_type.md) | Type of EM grid used |
| [growth_temperature_c](growth_temperature_c.md) | Growth temperature in Celsius |
| [gunlens](gunlens.md) | Gun lens setting |
| [harvest_timepoint](harvest_timepoint.md) | Time point when cells were harvested |
| [hic_column](hic_column.md) | Hydrophobic interaction column used |
| [hole_id](hole_id.md) | Hole identifier within grid square |
| [hole_size](hole_size.md) | Hole size in micrometers (range: 0 |
| [holes_per_group](holes_per_group.md) | Number of holes per group |
| [host_strain_or_cell_line](host_strain_or_cell_line.md) | Specific strain or cell line used (e |
| [humidity](humidity.md) | Humidity percentage |
| [humidity_percentage](humidity_percentage.md) | Chamber humidity during vitrification (range: 0-100) |
| [i_over_sigma](i_over_sigma.md) | Mean I/sigma(I) - signal to noise ratio |
| [i_zero](i_zero.md) | Forward scattering intensity I(0) |
| [ice_thickness_estimate](ice_thickness_estimate.md) | Estimated ice thickness in nanometers |
| [id](id.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... |
| [iex_column](iex_column.md) | Ion-exchange column used |
| [illumination_type](illumination_type.md) | Type of illumination (brightfield, darkfield, phase contrast, DIC) |
| [images](images.md) | Images acquired or generated in this study |
| [imaging_mode](imaging_mode.md) | Imaging mode for electron microscopy |
| [indexer_module](indexer_module.md) | Indexing module used (e |
| [inducer_concentration](inducer_concentration.md) | Concentration of induction agent |
| [induction_agent](induction_agent.md) | Agent used to induce expression (e |
| [induction_temperature_c](induction_temperature_c.md) | Temperature during induction in Celsius |
| [induction_time_h](induction_time_h.md) | Duration of induction in hours |
| [initial_hit_condition](initial_hit_condition.md) | Description of initial crystallization hit condition |
| [insert_boundaries](insert_boundaries.md) | Start and end positions of insert in vector |
| [installation_date](installation_date.md) | Date of instrument installation |
| [instrument_code](instrument_code.md) | Human-friendly facility or laboratory identifier for the instrument (e |
| [instrument_id](instrument_id.md) | Reference to the instrument used |
| [instrument_runs](instrument_runs.md) | Experimental data collection runs performed in this study |
| [instruments](instruments.md) | Instruments used across all studies in this dataset |
| [integrator_module](integrator_module.md) | Integration module used |
| [interaction_distance](interaction_distance.md) | Distance criteria for interaction (Angstroms) |
| [interaction_evidence](interaction_evidence.md) | Evidence for this interaction |
| [interaction_type](interaction_type.md) | Type of interaction |
| [interface_area](interface_area.md) | Buried surface area at interface (Ų) |
| [interface_residues](interface_residues.md) | Residues at the interaction interface |
| [ionic_strength](ionic_strength.md) | Ionic strength in molar of material in solution |
| [is_cofactor](is_cofactor.md) | Whether the ligand is a cofactor |
| [is_drug_like](is_drug_like.md) | Whether the ligand has drug-like properties |
| [keywords](keywords.md) | Keywords or tags describing the dataset for search and categorization |
| [label](label.md) | The human-readable label or name of the ontology term |
| [laser_power](laser_power.md) | Laser power in milliwatts or percentage |
| [last_updated](last_updated.md) | Date of last update |
| [ligand](ligand.md) | Ligand or small molecule bound to sample |
| [ligand_id](ligand_id.md) | Ligand identifier (ChEMBL, ChEBI, PubChem) |
| [ligand_interactions](ligand_interactions.md) | Small molecule interaction annotations |
| [ligand_name](ligand_name.md) | Common name of the ligand |
| [ligand_smiles](ligand_smiles.md) | SMILES representation of the ligand |
| [ligands](ligands.md) | Bound ligands or cofactors |
| [ligands_cofactors](ligands_cofactors.md) | Ligands or cofactors modeled in the structure |
| [loop_size](loop_size.md) | Loop size in micrometers |
| [lysis_buffer](lysis_buffer.md) | Buffer composition for lysis |
| [lysis_method](lysis_method.md) | Method used for cell lysis |
| [magnification](magnification.md) | Magnification used during data collection |
| [manufacturer](manufacturer.md) | Instrument manufacturer |
| [map_sharpening_bfactor](map_sharpening_bfactor.md) | B-factor used for map sharpening in Angstroms^2 |
| [mass_shift](mass_shift.md) | Mass change due to modification (Da) |
| [mean_i_over_sigma_i](mean_i_over_sigma_i.md) | Mean I/sigma(I) |
| [measurement_conditions](measurement_conditions.md) | Conditions under which measurement was made |
| [medium](medium.md) | Growth medium used |
| [memory_gb](memory_gb.md) | Maximum memory used in GB |
| [method](method.md) | Crystallization method used |
| [microscope_software](microscope_software.md) | Microscope control software (e |
| [microscope_software_version](microscope_software_version.md) | Software version |
| [model](model.md) | Instrument model |
| [model_file](model_file.md) | Path to deep learning model file if used |
| [modification_group](modification_group.md) | Chemical group added (e |
| [modification_type](modification_type.md) | Type of PTM |
| [modifications](modifications.md) | Post-translational modifications or chemical modifications |
| [modified_residue](modified_residue.md) | Residue that is modified |
| [molecular_composition](molecular_composition.md) | Description of molecular composition including sequences, modifications, liga... |
| [molecular_signatures](molecular_signatures.md) | Identified molecular signatures or peaks |
| [molecular_weight](molecular_weight.md) | Molecular weight in kDa |
| [molprobity_score](molprobity_score.md) | Overall MolProbity score |
| [monochromator_type](monochromator_type.md) | Type of monochromator |
| [motion_correction_params](motion_correction_params.md) | Motion correction specific parameters |
| [mounting_method](mounting_method.md) | Crystal mounting method |
| [mounting_temperature](mounting_temperature.md) | Temperature during mounting in Kelvin |
| [multiplicity](multiplicity.md) | Data multiplicity (redundancy) |
| [mutation](mutation.md) | Mutation in standard notation (e |
| [mutation_effects](mutation_effects.md) | Effects of mutations present in the sample |
| [mutation_type](mutation_type.md) | Type of mutation |
| [mutations](mutations.md) | Mutations present in the sample |
| [ncbi_taxid](ncbi_taxid.md) | NCBI Taxonomy ID for source organism |
| [ncc_score](ncc_score.md) | Normalized cross-correlation score threshold |
| [ncs_used](ncs_used.md) | Whether Non-Crystallographic Symmetry restraints were used |
| [nominal_defocus](nominal_defocus.md) | Nominal defocus value in micrometers |
| [number_of_images](number_of_images.md) | Total number of diffraction images collected |
| [number_of_scans](number_of_scans.md) | Number of scans averaged for the spectrum |
| [number_of_waters](number_of_waters.md) | Number of water molecules modeled |
| [numerical_aperture](numerical_aperture.md) | Numerical aperture of the objective lens |
| [objective_aperture](objective_aperture.md) | Objective aperture size in micrometers |
| [od600_at_induction](od600_at_induction.md) | Optical density at 600nm when induction was started |
| [omim_id](omim_id.md) | OMIM database identifier |
| [ontology](ontology.md) | The ontology or controlled vocabulary this term comes from (e |
| [operator_id](operator_id.md) | Identifier or name of the person who performed the sample preparation (e |
| [optimization_strategy](optimization_strategy.md) | Strategy used to optimize crystals |
| [optimized_condition](optimized_condition.md) | Final optimized crystallization condition |
| [organism](organism.md) | Source organism for the sample (e |
| [organism_id](organism_id.md) | NCBI taxonomy ID |
| [origin_movie_id](origin_movie_id.md) | Reference to original movie file |
| [oscillation_angle](oscillation_angle.md) | Oscillation angle per image |
| [oscillation_per_image_deg](oscillation_per_image_deg.md) | Oscillation angle per image in degrees |
| [outlier_rejection_method](outlier_rejection_method.md) | Method for rejecting outlier reflections |
| [output_binning](output_binning.md) | Output binning factor |
| [output_files](output_files.md) | Output files generated |
| [parameters_file_path](parameters_file_path.md) | Path to parameters file or text of key parameters |
| [parent_sample_id](parent_sample_id.md) | Reference to parent sample for derivation tracking |
| [particle_picking_params](particle_picking_params.md) | Particle picking specific parameters |
| [partner_chain_id](partner_chain_id.md) | Chain ID of interacting partner |
| [partner_interface_residues](partner_interface_residues.md) | Partner residues at the interaction interface |
| [partner_protein_id](partner_protein_id.md) | UniProt ID of interacting partner |
| [patch_size](patch_size.md) | Patch size for local motion correction |
| [pdb_entries](pdb_entries.md) | PDB entries representing this state |
| [pdb_entry](pdb_entry.md) | PDB identifier |
| [pdb_id](pdb_id.md) | PDB accession code if deposited |
| [ph](ph.md) | pH of the buffer (range: 0-14) |
| [phase_plate](phase_plate.md) | Phase plate available |
| [phase_plate_type](phase_plate_type.md) | Type of phase plate if present |
| [phasing_method](phasing_method.md) | Phasing method used for X-ray crystallography structure determination |
| [picking_method](picking_method.md) | Method used (manual, template_matching, deep_learning, LoG, Topaz, other) |
| [pinhole_size](pinhole_size.md) | Pinhole size in Airy units for confocal microscopy |
| [pixel_size](pixel_size.md) | Pixel size in Angstroms |
| [pixel_size_calibrated](pixel_size_calibrated.md) | Calibrated pixel size for this experiment |
| [pixel_size_physical](pixel_size_physical.md) | Physical pixel size in micrometers |
| [pixel_size_physical_um](pixel_size_physical_um.md) | Physical pixel size of the detector in micrometers |
| [pixel_size_unbinned](pixel_size_unbinned.md) | Unbinned pixel size in Angstroms per pixel |
| [pixel_size_x](pixel_size_x.md) | Pixel size X dimension |
| [pixel_size_y](pixel_size_y.md) | Pixel size Y dimension |
| [plasma_treatment](plasma_treatment.md) | Plasma treatment details |
| [population](population.md) | Relative population of this state (range: 0-1) |
| [power_score](power_score.md) | Power score threshold |
| [preparation_date](preparation_date.md) | Date of sample preparation |
| [preparation_method](preparation_method.md) | Method used to prepare the sample |
| [preparation_type](preparation_type.md) | Type of sample preparation |
| [pressure](pressure.md) | Pressure in kPa |
| [principal_motions](principal_motions.md) | Description of principal motions |
| [processing_level](processing_level.md) | Processing level (0=raw, 1=corrected, 2=derived, 3=model) |
| [processing_notes](processing_notes.md) | Additional notes about processing |
| [processing_parameters](processing_parameters.md) | Parameters used in processing |
| [processing_status](processing_status.md) | Current processing status |
| [promoter](promoter.md) | Promoter used for expression |
| [property_type](property_type.md) | Type of biophysical property |
| [protease](protease.md) | Protease used for tag cleavage |
| [protease_inhibitors](protease_inhibitors.md) | Protease inhibitors added |
| [protease_ratio](protease_ratio.md) | Ratio of protease to protein |
| [protein_buffer](protein_buffer.md) | Buffer composition for protein solution |
| [protein_concentration](protein_concentration.md) | Protein concentration for crystallization in mg/mL |
| [protein_concentration_mg_per_ml](protein_concentration_mg_per_ml.md) | Protein concentration for crystallization in mg/mL |
| [protein_constructs](protein_constructs.md) | Protein constructs and cloning information |
| [protein_id](protein_id.md) | UniProt accession number |
| [protein_interactions](protein_interactions.md) | Protein-protein interaction annotations |
| [protein_name](protein_name.md) | Name of the protein |
| [protocol_description](protocol_description.md) | Detailed protocol description |
| [ptm_annotations](ptm_annotations.md) | Post-translational modification annotations |
| [ptms](ptms.md) | All post-translational modifications |
| [publication_ids](publication_ids.md) | IDs of one or more publications supporting this annotation |
| [purification_steps](purification_steps.md) | Ordered list of purification steps performed |
| [purity_by_sds_page_percent](purity_by_sds_page_percent.md) | Purity percentage by SDS-PAGE |
| [purity_percentage](purity_percentage.md) | Sample purity as percentage (range: 0-100) |
| [q_range_max](q_range_max.md) | Maximum q value in inverse Angstroms |
| [q_range_min](q_range_min.md) | Minimum q value in inverse Angstroms |
| [quality_metrics](quality_metrics.md) | Quality control metrics for the sample |
| [quantum_yield](quantum_yield.md) | Quantum yield of the fluorophore |
| [r_factor](r_factor.md) | R-factor for crystallography (deprecated, use r_work) |
| [r_free](r_free.md) | R-free (test set) |
| [r_merge](r_merge.md) | Rmerge - merge R-factor |
| [r_pim](r_pim.md) | Rpim - precision-indicating merging R-factor |
| [r_work](r_work.md) | Refinement R-factor (working set) |
| [ramachandran_favored](ramachandran_favored.md) | Percentage of residues in favored Ramachandran regions |
| [ramachandran_favored_percent](ramachandran_favored_percent.md) | Percentage of residues in favored Ramachandran regions |
| [ramachandran_outliers](ramachandran_outliers.md) | Percentage of Ramachandran outliers |
| [ramachandran_outliers_percent](ramachandran_outliers_percent.md) | Percentage of Ramachandran outliers |
| [raw_data_location](raw_data_location.md) | Location of raw data files |
| [reconstruction_method](reconstruction_method.md) | Method used for 3D reconstruction |
| [refinement_params](refinement_params.md) | 3D refinement specific parameters |
| [refinement_resolution_a](refinement_resolution_a.md) | Resolution cutoff used for refinement in Angstroms |
| [regulatory_role](regulatory_role.md) | Role in regulation |
| [related_entity](related_entity.md) | ID of the entity that owns this file |
| [removal_enzyme](removal_enzyme.md) | Enzyme that removes modification |
| [reservoir_volume_ul](reservoir_volume_ul.md) | Reservoir volume in microliters |
| [residue_range](residue_range.md) | Range of residues (e |
| [residues](residues.md) | List of residues forming the functional site |
| [resolution](resolution.md) | Resolution in Angstroms |
| [resolution_0_143](resolution_0_143.md) | Resolution at FSC=0 |
| [resolution_0_5](resolution_0_5.md) | Resolution at FSC=0 |
| [resolution_angstrom](resolution_angstrom.md) | Resolution values in Angstroms |
| [resolution_fit_limit](resolution_fit_limit.md) | Resolution fit limit in Angstroms |
| [resolution_high](resolution_high.md) | High resolution limit |
| [resolution_high_shell_a](resolution_high_shell_a.md) | High resolution shell limit in Angstroms |
| [resolution_low](resolution_low.md) | Low resolution limit |
| [resolution_low_a](resolution_low_a.md) | Low resolution limit in Angstroms |
| [restraints_other](restraints_other.md) | Other restraints applied during refinement |
| [rfree](rfree.md) | R-free (test set) |
| [rg](rg.md) | Radius of gyration in Angstroms |
| [rmerge](rmerge.md) | Rmerge - merge R-factor |
| [rmsd_angles](rmsd_angles.md) | RMSD from ideal bond angles |
| [rmsd_bonds](rmsd_bonds.md) | RMSD from ideal bond lengths |
| [rmsd_from_reference](rmsd_from_reference.md) | RMSD from reference structure |
| [rmsd_threshold](rmsd_threshold.md) | RMSD threshold for clustering (Angstroms) |
| [rpim](rpim.md) | Rpim - precision-indicating merging R-factor |
| [rwork](rwork.md) | Refinement R-factor (working set) |
| [sample_applied_volume](sample_applied_volume.md) | Volume of sample applied in microliters |
| [sample_cell_type](sample_cell_type.md) | Type of sample cell used |
| [sample_changer_capacity](sample_changer_capacity.md) | Number of samples in automatic sample changer |
| [sample_code](sample_code.md) | Human-friendly laboratory identifier or facility code for the sample (e |
| [sample_id](sample_id.md) | Reference to the sample being prepared |
| [sample_preparations](sample_preparations.md) | Sample preparation procedures performed in this study |
| [sample_type](sample_type.md) | Type of biological sample |
| [samples](samples.md) | Experimental samples used in this study, including biological samples  |
| [scaler_module](scaler_module.md) | Scaling module used (e |
| [screen_name](screen_name.md) | Name of crystallization screen used |
| [search_model_pdb_id](search_model_pdb_id.md) | PDB ID of search model for molecular replacement |
| [sec_buffer](sec_buffer.md) | Buffer for size-exclusion chromatography |
| [sec_column](sec_column.md) | Size-exclusion column used |
| [second_affinity_reverse](second_affinity_reverse.md) | Second affinity or reverse affinity step |
| [secondary_structure](secondary_structure.md) | Secondary structure assignment |
| [seed_stock_dilution](seed_stock_dilution.md) | Dilution factor for seed stock |
| [seeding_type](seeding_type.md) | Type of seeding used (micro, macro, streak) |
| [selectable_marker](selectable_marker.md) | Antibiotic resistance or other selectable marker |
| [sequence_file_path](sequence_file_path.md) | Path to sequence file |
| [sequence_length_aa](sequence_length_aa.md) | Length of the protein sequence in amino acids |
| [sequence_verified_by](sequence_verified_by.md) | Method or person who verified the sequence |
| [sequences](sequences.md) | Amino acid or nucleotide sequences |
| [shots_per_hole](shots_per_hole.md) | Number of shots taken per hole |
| [signal_peptide](signal_peptide.md) | Signal peptide sequence if present |
| [signal_to_noise](signal_to_noise.md) | Signal to noise ratio |
| [site_name](site_name.md) | Common name for this site |
| [site_type](site_type.md) | Type of functional site |
| [soak_compound](soak_compound.md) | Compound used for soaking (ligand, heavy atom) |
| [soak_conditions](soak_conditions.md) | Conditions for crystal soaking |
| [software_name](software_name.md) | Software used for processing |
| [software_version](software_version.md) | Software version |
| [solvent_accessibility](solvent_accessibility.md) | Relative solvent accessible surface area (range: 0-1) |
| [source_database](source_database.md) | Source database or resource that provided this annotation |
| [source_type](source_type.md) | Type of X-ray source |
| [space_group](space_group.md) | Crystallographic space group |
| [spectral_resolution](spectral_resolution.md) | Spectral resolution in cm⁻¹ |
| [split_strategy](split_strategy.md) | Strategy for data splitting |
| [spotsize](spotsize.md) | Electron beam spot size setting |
| [stage_position_x](stage_position_x.md) | Stage X position in micrometers |
| [stage_position_y](stage_position_y.md) | Stage Y position in micrometers |
| [stage_position_z](stage_position_z.md) | Stage Z position in micrometers |
| [stage_tilt](stage_tilt.md) | Stage tilt angle in degrees |
| [start_angle](start_angle.md) | Starting rotation angle |
| [started_at](started_at.md) | Workflow start time |
| [state_id](state_id.md) | Identifier for this state |
| [state_name](state_name.md) | Descriptive name (e |
| [storage_conditions](storage_conditions.md) | Storage conditions for the sample |
| [storage_gb](storage_gb.md) | Storage used in GB |
| [storage_uri](storage_uri.md) | Storage URI (S3, Globus, etc |
| [strategy_notes](strategy_notes.md) | Notes about data collection strategy |
| [structural_features](structural_features.md) | Structural feature annotations |
| [structural_motif](structural_motif.md) | Known structural motif |
| [studies](studies.md) | Individual research studies contained in this dataset |
| [super_resolution](super_resolution.md) | Whether super-resolution mode was used |
| [support_film](support_film.md) | Support film type |
| [symmetry](symmetry.md) | Symmetry applied (C1, Cn, Dn, T, O, I) |
| [tag](tag.md) | Affinity tag (e |
| [tag_cterm](tag_cterm.md) | C-terminal tag |
| [tag_nterm](tag_nterm.md) | N-terminal tag (e |
| [tag_removal](tag_removal.md) | Whether and how affinity tag was removed |
| [taxonomic_range](taxonomic_range.md) | Taxonomic range of conservation |
| [technique](technique.md) | Technique used for data collection |
| [tem_beam_diameter](tem_beam_diameter.md) | TEM beam diameter in micrometers |
| [temperature](temperature.md) | Storage temperature in Celsius |
| [temperature_c](temperature_c.md) | Crystallization temperature in Celsius |
| [temperature_control](temperature_control.md) | Temperature control settings |
| [temperature_control_range](temperature_control_range.md) | Temperature control range in Celsius |
| [temperature_k](temperature_k.md) | Data collection temperature in Kelvin |
| [temperature_unit](temperature_unit.md) | Temperature unit |
| [terms](terms.md) | Ontology terms describing features identified in the image |
| [threshold](threshold.md) | Picking threshold |
| [timestamp](timestamp.md) | Acquisition timestamp |
| [title](title.md) | A human-readable name or title for this entity |
| [tls_used](tls_used.md) | Whether TLS (Translation/Libration/Screw) refinement was used |
| [total_dose](total_dose.md) | Total electron dose in e-/Angstrom^2 |
| [total_exposure_time](total_exposure_time.md) | Total exposure time in milliseconds |
| [total_frames](total_frames.md) | Total number of frames/images |
| [total_rotation](total_rotation.md) | Total rotation range collected |
| [total_rotation_deg](total_rotation_deg.md) | Total rotation range in degrees |
| [transition_pathways](transition_pathways.md) | Description of transition pathways between states |
| [transmission_percent](transmission_percent.md) | Beam transmission percentage |
| [uniprot_id](uniprot_id.md) | UniProt accession for the target protein |
| [unit](unit.md) | Unit of measurement |
| [unit_cell_a](unit_cell_a.md) | Unit cell parameter a |
| [unit_cell_alpha](unit_cell_alpha.md) | Unit cell angle alpha |
| [unit_cell_b](unit_cell_b.md) | Unit cell parameter b |
| [unit_cell_beta](unit_cell_beta.md) | Unit cell angle beta |
| [unit_cell_c](unit_cell_c.md) | Unit cell parameter c |
| [unit_cell_gamma](unit_cell_gamma.md) | Unit cell angle gamma |
| [validation_report_path](validation_report_path.md) | Path to validation report |
| [value](value.md) | Numerical value of the property |
| [variable_residues](variable_residues.md) | Highly variable residues |
| [vector_backbone](vector_backbone.md) | Base plasmid backbone used |
| [vector_name](vector_name.md) | Complete vector name |
| [verification_notes](verification_notes.md) | Notes from sequence verification |
| [vitrification_instrument](vitrification_instrument.md) | Vitrification instrument used (e |
| [vitrification_method](vitrification_method.md) | Method used for vitrification |
| [voltage_used_in_estimation](voltage_used_in_estimation.md) | Accelerating voltage value used during CTF estimation (in kV); may differ fro... |
| [voxel_size](voxel_size.md) | Voxel size in Angstroms |
| [wait_time](wait_time.md) | Wait time before blotting in seconds |
| [wash_buffer](wash_buffer.md) | Buffer composition for washing |
| [wavelength](wavelength.md) | X-ray wavelength |
| [wavelength_a](wavelength_a.md) | X-ray wavelength in Angstroms |
| [wavenumber_max](wavenumber_max.md) | Maximum wavenumber in cm⁻¹ |
| [wavenumber_min](wavenumber_min.md) | Minimum wavenumber in cm⁻¹ |
| [white_balance](white_balance.md) | White balance settings |
| [wilson_b_factor](wilson_b_factor.md) | Wilson B-factor |
| [wilson_b_factor_a2](wilson_b_factor_a2.md) | Wilson B-factor in Angstroms squared |
| [workflow_code](workflow_code.md) | Human-friendly identifier for the computational workflow run (e |
| [workflow_runs](workflow_runs.md) | Computational workflow executions for data processing in this study |
| [workflow_type](workflow_type.md) | Type of processing workflow |
| [yield_mg](yield_mg.md) | Total yield in milligrams |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AffinityUnitEnum](AffinityUnitEnum.md) | Units for affinity measurements |
| [AnnotationSourceEnum](AnnotationSourceEnum.md) | Sources of functional annotations |
| [BindingAffinityTypeEnum](BindingAffinityTypeEnum.md) | Types of binding affinity measurements |
| [BiophysicalMethodEnum](BiophysicalMethodEnum.md) | Methods for biophysical measurements |
| [BiophysicalPropertyEnum](BiophysicalPropertyEnum.md) | Types of biophysical properties |
| [ClinicalSignificanceEnum](ClinicalSignificanceEnum.md) | Clinical significance of variants |
| [CollectionModeEnum](CollectionModeEnum.md) | Data collection modes |
| [ComplexStabilityEnum](ComplexStabilityEnum.md) | Stability of protein complexes |
| [ConcentrationUnitEnum](ConcentrationUnitEnum.md) | Units for concentration measurement |
| [ConformationalStateEnum](ConformationalStateEnum.md) | Conformational states |
| [CrystallizationMethodEnum](CrystallizationMethodEnum.md) | Methods for protein crystallization |
| [DatabaseNameEnum](DatabaseNameEnum.md) | External database names |
| [DataTypeEnum](DataTypeEnum.md) | Types of data |
| [DetectorModeEnum](DetectorModeEnum.md) | Operating modes for detectors during data collection |
| [DetectorTechnologyEnum](DetectorTechnologyEnum.md) | Generic detector technologies for structural biology imaging |
| [DetectorTypeEnum](DetectorTypeEnum.md) | DEPRECATED: Use DetectorTechnologyEnum instead |
| [EvidenceTypeEnum](EvidenceTypeEnum.md) | Types of evidence |
| [ExperimentalMethodEnum](ExperimentalMethodEnum.md) | Experimental methods for structure determination |
| [ExpressionSystemEnum](ExpressionSystemEnum.md) | Expression systems for recombinant protein production |
| [FacilityEnum](FacilityEnum.md) | Major synchrotron and structural biology research facilities worldwide |
| [FileFormatEnum](FileFormatEnum.md) | File formats |
| [FunctionalEffectEnum](FunctionalEffectEnum.md) | Effect on protein function |
| [FunctionalSiteTypeEnum](FunctionalSiteTypeEnum.md) | Types of functional sites in proteins |
| [GridMaterialEnum](GridMaterialEnum.md) | Materials used for EM grids |
| [GridTypeEnum](GridTypeEnum.md) | Types of EM grids |
| [IlluminationTypeEnum](IlluminationTypeEnum.md) | Types of illumination for optical microscopy |
| [ImagingModeEnum](ImagingModeEnum.md) | Imaging modes for electron microscopy |
| [InstrumentStatusEnum](InstrumentStatusEnum.md) | Operational status of instruments |
| [InteractionEvidenceEnum](InteractionEvidenceEnum.md) | Evidence for interactions |
| [InteractionTypeEnum](InteractionTypeEnum.md) | Types of molecular interactions |
| [MutationTypeEnum](MutationTypeEnum.md) | Types of mutations |
| [PhasingMethodEnum](PhasingMethodEnum.md) | Methods for phase determination in X-ray crystallography |
| [PreparationTypeEnum](PreparationTypeEnum.md) | Types of sample preparation |
| [ProcessingStatusEnum](ProcessingStatusEnum.md) | Processing status |
| [PTMTypeEnum](PTMTypeEnum.md) | Types of post-translational modifications |
| [PurificationStepEnum](PurificationStepEnum.md) | Protein purification steps and methods |
| [SampleTypeEnum](SampleTypeEnum.md) | Types of biological samples |
| [SecondaryStructureEnum](SecondaryStructureEnum.md) | Secondary structure types |
| [StabilityEffectEnum](StabilityEffectEnum.md) | Effect on protein stability |
| [StructuralFeatureTypeEnum](StructuralFeatureTypeEnum.md) | Types of structural features |
| [SymmetryEnum](SymmetryEnum.md) | Crystallographic and non-crystallographic symmetry groups for cryo-EM |
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
| [SmilesString](SmilesString.md) | A SMILES representation of a chemical structure |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
