
# Class: WorkflowRun

A computational processing workflow execution

URI: [lambdaber:WorkflowRun](https://w3id.org/lambda-ber-schema/WorkflowRun)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataFile]<output_files%200..*-%20[WorkflowRun&#124;workflow_code:string;workflow_type:WorkflowTypeEnum;experiment_id:string;processing_level:integer%20%3F;software_name:string;software_version:string%20%3F;additional_software:string%20%3F;processing_parameters:string%20%3F;parameters_file_path:string%20%3F;indexer_module:string%20%3F;integrator_module:string%20%3F;scaler_module:string%20%3F;outlier_rejection_method:string%20%3F;phasing_method:PhasingMethodEnum%20%3F;search_model_pdb_id:string%20%3F;tls_used:boolean%20%3F;ncs_used:boolean%20%3F;restraints_other:string%20%3F;ligands_cofactors:string%20%3F;number_of_waters:integer%20%3F;refinement_resolution_a:float%20%3F;deposited_to_pdb:boolean%20%3F;pdb_id:string%20%3F;validation_report_path:string%20%3F;space_group:string%20%3F;rmerge:float%20%3F;rpim:float%20%3F;cc_half:float%20%3F;i_over_sigma:float%20%3F;multiplicity:float%20%3F;anomalous_multiplicity:float%20%3F;cc_anomalous:float%20%3F;r_anomalous:float%20%3F;sig_anomalous:float%20%3F;n_total_observations:integer%20%3F;n_total_unique:integer%20%3F;ispyb_auto_proc_program_id:integer%20%3F;ispyb_auto_proc_scaling_id:integer%20%3F;rwork:float%20%3F;rfree:float%20%3F;clashscore:float%20%3F;processing_notes:string%20%3F;started_at:string%20%3F;completed_at:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[FSCCurve]<fsc_curve%200..1-++[WorkflowRun],[RefinementParameters]<refinement_params%200..1-++[WorkflowRun],[ParticlePickingParameters]<particle_picking_params%200..1-++[WorkflowRun],[CTFEstimationParameters]<ctf_estimation_params%200..1-++[WorkflowRun],[MotionCorrectionParameters]<motion_correction_params%200..1-++[WorkflowRun],[ComputeResources]<compute_resources%200..1-++[WorkflowRun],[QuantityValue]<ramachandran_outliers%200..1-++[WorkflowRun],[QuantityValue]<ramachandran_favored%200..1-++[WorkflowRun],[QuantityValue]<rmsd_angles%200..1-++[WorkflowRun],[QuantityValue]<rmsd_bonds%200..1-++[WorkflowRun],[QuantityValue]<anomalous_completeness%200..1-++[WorkflowRun],[QuantityValue]<wilson_b_factor%200..1-++[WorkflowRun],[QuantityValue]<completeness_percent%200..1-++[WorkflowRun],[QuantityValue]<resolution_low%200..1-++[WorkflowRun],[QuantityValue]<resolution_high%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_gamma%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_beta%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_alpha%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_c%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_b%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_a%200..1-++[WorkflowRun],[Study]++-%20workflow_runs%200..*>[WorkflowRun],[NamedThing]^-[WorkflowRun],[Study],[RefinementParameters],[QuantityValue],[ParticlePickingParameters],[NamedThing],[MotionCorrectionParameters],[FSCCurve],[DataFile],[ComputeResources],[CTFEstimationParameters])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataFile]<output_files%200..*-%20[WorkflowRun&#124;workflow_code:string;workflow_type:WorkflowTypeEnum;experiment_id:string;processing_level:integer%20%3F;software_name:string;software_version:string%20%3F;additional_software:string%20%3F;processing_parameters:string%20%3F;parameters_file_path:string%20%3F;indexer_module:string%20%3F;integrator_module:string%20%3F;scaler_module:string%20%3F;outlier_rejection_method:string%20%3F;phasing_method:PhasingMethodEnum%20%3F;search_model_pdb_id:string%20%3F;tls_used:boolean%20%3F;ncs_used:boolean%20%3F;restraints_other:string%20%3F;ligands_cofactors:string%20%3F;number_of_waters:integer%20%3F;refinement_resolution_a:float%20%3F;deposited_to_pdb:boolean%20%3F;pdb_id:string%20%3F;validation_report_path:string%20%3F;space_group:string%20%3F;rmerge:float%20%3F;rpim:float%20%3F;cc_half:float%20%3F;i_over_sigma:float%20%3F;multiplicity:float%20%3F;anomalous_multiplicity:float%20%3F;cc_anomalous:float%20%3F;r_anomalous:float%20%3F;sig_anomalous:float%20%3F;n_total_observations:integer%20%3F;n_total_unique:integer%20%3F;ispyb_auto_proc_program_id:integer%20%3F;ispyb_auto_proc_scaling_id:integer%20%3F;rwork:float%20%3F;rfree:float%20%3F;clashscore:float%20%3F;processing_notes:string%20%3F;started_at:string%20%3F;completed_at:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[FSCCurve]<fsc_curve%200..1-++[WorkflowRun],[RefinementParameters]<refinement_params%200..1-++[WorkflowRun],[ParticlePickingParameters]<particle_picking_params%200..1-++[WorkflowRun],[CTFEstimationParameters]<ctf_estimation_params%200..1-++[WorkflowRun],[MotionCorrectionParameters]<motion_correction_params%200..1-++[WorkflowRun],[ComputeResources]<compute_resources%200..1-++[WorkflowRun],[QuantityValue]<ramachandran_outliers%200..1-++[WorkflowRun],[QuantityValue]<ramachandran_favored%200..1-++[WorkflowRun],[QuantityValue]<rmsd_angles%200..1-++[WorkflowRun],[QuantityValue]<rmsd_bonds%200..1-++[WorkflowRun],[QuantityValue]<anomalous_completeness%200..1-++[WorkflowRun],[QuantityValue]<wilson_b_factor%200..1-++[WorkflowRun],[QuantityValue]<completeness_percent%200..1-++[WorkflowRun],[QuantityValue]<resolution_low%200..1-++[WorkflowRun],[QuantityValue]<resolution_high%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_gamma%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_beta%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_alpha%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_c%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_b%200..1-++[WorkflowRun],[QuantityValue]<unit_cell_a%200..1-++[WorkflowRun],[Study]++-%20workflow_runs%200..*>[WorkflowRun],[NamedThing]^-[WorkflowRun],[Study],[RefinementParameters],[QuantityValue],[ParticlePickingParameters],[NamedThing],[MotionCorrectionParameters],[FSCCurve],[DataFile],[ComputeResources],[CTFEstimationParameters])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞workflow_runs](study__workflow_runs.md)*  <sub>0..\*</sub>  **[WorkflowRun](WorkflowRun.md)**

## Attributes


### Own

 * [➞workflow_code](workflowRun__workflow_code.md)  <sub>1..1</sub>
     * Description: Human-friendly identifier for the computational workflow run (e.g., 'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing pipelines and computational provenance.
     * Range: [String](types/String.md)
 * [➞workflow_type](workflowRun__workflow_type.md)  <sub>1..1</sub>
     * Description: Type of processing workflow
     * Range: [WorkflowTypeEnum](WorkflowTypeEnum.md)
 * [➞experiment_id](workflowRun__experiment_id.md)  <sub>1..1</sub>
     * Description: Reference to the source experiment
     * Range: [String](types/String.md)
 * [➞processing_level](workflowRun__processing_level.md)  <sub>0..1</sub>
     * Description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
     * Range: [Integer](types/Integer.md)
 * [➞software_name](workflowRun__software_name.md)  <sub>1..1</sub>
     * Description: Software used for processing
     * Range: [String](types/String.md)
 * [➞software_version](workflowRun__software_version.md)  <sub>0..1</sub>
     * Description: Software version
     * Range: [String](types/String.md)
 * [➞additional_software](workflowRun__additional_software.md)  <sub>0..1</sub>
     * Description: Additional software used in pipeline
     * Range: [String](types/String.md)
 * [➞processing_parameters](workflowRun__processing_parameters.md)  <sub>0..1</sub>
     * Description: Parameters used in processing
     * Range: [String](types/String.md)
 * [➞parameters_file_path](workflowRun__parameters_file_path.md)  <sub>0..1</sub>
     * Description: Path to parameters file or text of key parameters
     * Range: [String](types/String.md)
 * [➞indexer_module](workflowRun__indexer_module.md)  <sub>0..1</sub>
     * Description: Indexing module used (e.g., MOSFLM, XDS)
     * Range: [String](types/String.md)
 * [➞integrator_module](workflowRun__integrator_module.md)  <sub>0..1</sub>
     * Description: Integration module used
     * Range: [String](types/String.md)
 * [➞scaler_module](workflowRun__scaler_module.md)  <sub>0..1</sub>
     * Description: Scaling module used (e.g., AIMLESS, SCALA)
     * Range: [String](types/String.md)
 * [➞outlier_rejection_method](workflowRun__outlier_rejection_method.md)  <sub>0..1</sub>
     * Description: Method for rejecting outlier reflections
     * Range: [String](types/String.md)
 * [➞phasing_method](workflowRun__phasing_method.md)  <sub>0..1</sub>
     * Description: Phasing method used for X-ray crystallography structure determination
     * Range: [PhasingMethodEnum](PhasingMethodEnum.md)
 * [➞search_model_pdb_id](workflowRun__search_model_pdb_id.md)  <sub>0..1</sub>
     * Description: PDB ID of search model for molecular replacement
     * Range: [String](types/String.md)
 * [➞tls_used](workflowRun__tls_used.md)  <sub>0..1</sub>
     * Description: Whether TLS (Translation/Libration/Screw) refinement was used
     * Range: [Boolean](types/Boolean.md)
 * [➞ncs_used](workflowRun__ncs_used.md)  <sub>0..1</sub>
     * Description: Whether Non-Crystallographic Symmetry restraints were used
     * Range: [Boolean](types/Boolean.md)
 * [➞restraints_other](workflowRun__restraints_other.md)  <sub>0..1</sub>
     * Description: Other restraints applied during refinement
     * Range: [String](types/String.md)
 * [➞ligands_cofactors](workflowRun__ligands_cofactors.md)  <sub>0..1</sub>
     * Description: Ligands or cofactors modeled in the structure
     * Range: [String](types/String.md)
 * [➞number_of_waters](workflowRun__number_of_waters.md)  <sub>0..1</sub>
     * Description: Number of water molecules modeled
     * Range: [Integer](types/Integer.md)
 * [➞refinement_resolution_a](workflowRun__refinement_resolution_a.md)  <sub>0..1</sub>
     * Description: Resolution cutoff used for refinement in Angstroms
     * Range: [Float](types/Float.md)
 * [➞deposited_to_pdb](workflowRun__deposited_to_pdb.md)  <sub>0..1</sub>
     * Description: Whether structure was deposited to PDB
     * Range: [Boolean](types/Boolean.md)
 * [➞pdb_id](workflowRun__pdb_id.md)  <sub>0..1</sub>
     * Description: PDB accession code if deposited
     * Range: [String](types/String.md)
 * [➞validation_report_path](workflowRun__validation_report_path.md)  <sub>0..1</sub>
     * Description: Path to validation report
     * Range: [String](types/String.md)
 * [➞space_group](workflowRun__space_group.md)  <sub>0..1</sub>
     * Description: Crystallographic space group
     * Range: [String](types/String.md)
 * [➞unit_cell_a](workflowRun__unit_cell_a.md)  <sub>0..1</sub>
     * Description: Unit cell parameter a, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_b](workflowRun__unit_cell_b.md)  <sub>0..1</sub>
     * Description: Unit cell parameter b, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_c](workflowRun__unit_cell_c.md)  <sub>0..1</sub>
     * Description: Unit cell parameter c, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_alpha](workflowRun__unit_cell_alpha.md)  <sub>0..1</sub>
     * Description: Unit cell angle alpha, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_beta](workflowRun__unit_cell_beta.md)  <sub>0..1</sub>
     * Description: Unit cell angle beta, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_gamma](workflowRun__unit_cell_gamma.md)  <sub>0..1</sub>
     * Description: Unit cell angle gamma, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞resolution_high](workflowRun__resolution_high.md)  <sub>0..1</sub>
     * Description: High resolution limit, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞resolution_low](workflowRun__resolution_low.md)  <sub>0..1</sub>
     * Description: Low resolution limit, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞rmerge](workflowRun__rmerge.md)  <sub>0..1</sub>
     * Description: Rmerge - merge R-factor
     * Range: [Float](types/Float.md)
 * [➞rpim](workflowRun__rpim.md)  <sub>0..1</sub>
     * Description: Rpim - precision-indicating merging R-factor
     * Range: [Float](types/Float.md)
 * [➞cc_half](workflowRun__cc_half.md)  <sub>0..1</sub>
     * Description: Half-set correlation coefficient CC(1/2)
     * Range: [Float](types/Float.md)
 * [➞completeness_percent](workflowRun__completeness_percent.md)  <sub>0..1</sub>
     * Description: Data completeness as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞i_over_sigma](workflowRun__i_over_sigma.md)  <sub>0..1</sub>
     * Description: Mean I/sigma(I) - signal to noise ratio
     * Range: [Float](types/Float.md)
 * [➞wilson_b_factor](workflowRun__wilson_b_factor.md)  <sub>0..1</sub>
     * Description: Wilson B-factor, typically specified in Angstroms squared (Ų). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞multiplicity](workflowRun__multiplicity.md)  <sub>0..1</sub>
     * Description: Data multiplicity (redundancy)
     * Range: [Float](types/Float.md)
 * [➞anomalous_completeness](workflowRun__anomalous_completeness.md)  <sub>0..1</sub>
     * Description: Completeness of anomalous data as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞anomalous_multiplicity](workflowRun__anomalous_multiplicity.md)  <sub>0..1</sub>
     * Description: Multiplicity of anomalous data
     * Range: [Float](types/Float.md)
 * [➞cc_anomalous](workflowRun__cc_anomalous.md)  <sub>0..1</sub>
     * Description: Anomalous correlation coefficient
     * Range: [Float](types/Float.md)
 * [➞r_anomalous](workflowRun__r_anomalous.md)  <sub>0..1</sub>
     * Description: Anomalous R-factor
     * Range: [Float](types/Float.md)
 * [➞sig_anomalous](workflowRun__sig_anomalous.md)  <sub>0..1</sub>
     * Description: Mean anomalous difference signal
     * Range: [Float](types/Float.md)
 * [➞n_total_observations](workflowRun__n_total_observations.md)  <sub>0..1</sub>
     * Description: Total number of observations (before merging)
     * Range: [Integer](types/Integer.md)
 * [➞n_total_unique](workflowRun__n_total_unique.md)  <sub>0..1</sub>
     * Description: Total number of unique reflections
     * Range: [Integer](types/Integer.md)
 * [➞ispyb_auto_proc_program_id](workflowRun__ispyb_auto_proc_program_id.md)  <sub>0..1</sub>
     * Description: ISPyB AutoProcProgram.autoProcProgramId
     * Range: [Integer](types/Integer.md)
 * [➞ispyb_auto_proc_scaling_id](workflowRun__ispyb_auto_proc_scaling_id.md)  <sub>0..1</sub>
     * Description: ISPyB AutoProcScaling.autoProcScalingId
     * Range: [Integer](types/Integer.md)
 * [➞rwork](workflowRun__rwork.md)  <sub>0..1</sub>
     * Description: Refinement R-factor (working set)
     * Range: [Float](types/Float.md)
 * [➞rfree](workflowRun__rfree.md)  <sub>0..1</sub>
     * Description: R-free (test set)
     * Range: [Float](types/Float.md)
 * [➞rmsd_bonds](workflowRun__rmsd_bonds.md)  <sub>0..1</sub>
     * Description: RMSD from ideal bond lengths, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞rmsd_angles](workflowRun__rmsd_angles.md)  <sub>0..1</sub>
     * Description: RMSD from ideal bond angles, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ramachandran_favored](workflowRun__ramachandran_favored.md)  <sub>0..1</sub>
     * Description: Percentage of residues in favored Ramachandran regions (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ramachandran_outliers](workflowRun__ramachandran_outliers.md)  <sub>0..1</sub>
     * Description: Percentage of Ramachandran outliers (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞clashscore](workflowRun__clashscore.md)  <sub>0..1</sub>
     * Description: MolProbity clashscore
     * Range: [Float](types/Float.md)
 * [➞processing_notes](workflowRun__processing_notes.md)  <sub>0..1</sub>
     * Description: Additional notes about processing
     * Range: [String](types/String.md)
 * [➞compute_resources](workflowRun__compute_resources.md)  <sub>0..1</sub>
     * Description: Computational resources used
     * Range: [ComputeResources](ComputeResources.md)
 * [➞started_at](workflowRun__started_at.md)  <sub>0..1</sub>
     * Description: Workflow start time
     * Range: [String](types/String.md)
 * [➞completed_at](workflowRun__completed_at.md)  <sub>0..1</sub>
     * Description: Workflow completion time
     * Range: [String](types/String.md)
 * [➞motion_correction_params](workflowRun__motion_correction_params.md)  <sub>0..1</sub>
     * Description: Motion correction specific parameters
     * Range: [MotionCorrectionParameters](MotionCorrectionParameters.md)
 * [➞ctf_estimation_params](workflowRun__ctf_estimation_params.md)  <sub>0..1</sub>
     * Description: CTF estimation specific parameters
     * Range: [CTFEstimationParameters](CTFEstimationParameters.md)
 * [➞particle_picking_params](workflowRun__particle_picking_params.md)  <sub>0..1</sub>
     * Description: Particle picking specific parameters
     * Range: [ParticlePickingParameters](ParticlePickingParameters.md)
 * [➞refinement_params](workflowRun__refinement_params.md)  <sub>0..1</sub>
     * Description: 3D refinement specific parameters
     * Range: [RefinementParameters](RefinementParameters.md)
 * [➞fsc_curve](workflowRun__fsc_curve.md)  <sub>0..1</sub>
     * Description: Fourier Shell Correlation curve data
     * Range: [FSCCurve](FSCCurve.md)
 * [➞output_files](workflowRun__output_files.md)  <sub>0..\*</sub>
     * Description: Output files generated
     * Range: [DataFile](DataFile.md)

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
