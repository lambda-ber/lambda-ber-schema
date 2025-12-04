
# Class: QualityMetrics

Quality metrics for experiments

URI: [lambdaber:QualityMetrics](https://w3id.org/lambda-ber-schema/QualityMetrics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20quality_metrics%200..1>[QualityMetrics&#124;resolution:float%20%3F;resolution_high_shell_a:float%20%3F;resolution_low_a:float%20%3F;completeness:float%20%3F;completeness_high_res_shell_percent:float%20%3F;signal_to_noise:float%20%3F;mean_i_over_sigma_i:float%20%3F;space_group:string%20%3F;unit_cell_a:float%20%3F;unit_cell_b:float%20%3F;unit_cell_c:float%20%3F;unit_cell_alpha:float%20%3F;unit_cell_beta:float%20%3F;unit_cell_gamma:float%20%3F;multiplicity:float%20%3F;cc_half:float%20%3F;r_merge:float%20%3F;r_pim:float%20%3F;wilson_b_factor_a2:float%20%3F;anomalous_used:boolean%20%3F;anom_corr:float%20%3F;anom_sig_ano:float%20%3F;r_work:float%20%3F;r_free:float%20%3F;ramachandran_favored_percent:float%20%3F;ramachandran_outliers_percent:float%20%3F;clashscore:float%20%3F;molprobity_score:float%20%3F;average_b_factor_a2:float%20%3F;i_zero:float%20%3F;rg:float%20%3F;r_factor:float%20%3F;description(i):string%20%3F],[AttributeGroup]^-[QualityMetrics],[ExperimentRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]++-%20quality_metrics%200..1>[QualityMetrics&#124;resolution:float%20%3F;resolution_high_shell_a:float%20%3F;resolution_low_a:float%20%3F;completeness:float%20%3F;completeness_high_res_shell_percent:float%20%3F;signal_to_noise:float%20%3F;mean_i_over_sigma_i:float%20%3F;space_group:string%20%3F;unit_cell_a:float%20%3F;unit_cell_b:float%20%3F;unit_cell_c:float%20%3F;unit_cell_alpha:float%20%3F;unit_cell_beta:float%20%3F;unit_cell_gamma:float%20%3F;multiplicity:float%20%3F;cc_half:float%20%3F;r_merge:float%20%3F;r_pim:float%20%3F;wilson_b_factor_a2:float%20%3F;anomalous_used:boolean%20%3F;anom_corr:float%20%3F;anom_sig_ano:float%20%3F;r_work:float%20%3F;r_free:float%20%3F;ramachandran_favored_percent:float%20%3F;ramachandran_outliers_percent:float%20%3F;clashscore:float%20%3F;molprobity_score:float%20%3F;average_b_factor_a2:float%20%3F;i_zero:float%20%3F;rg:float%20%3F;r_factor:float%20%3F;description(i):string%20%3F],[AttributeGroup]^-[QualityMetrics],[ExperimentRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞quality_metrics](experimentRun__quality_metrics.md)*  <sub>0..1</sub>  **[QualityMetrics](QualityMetrics.md)**

## Attributes


### Own

 * [➞resolution](qualityMetrics__resolution.md)  <sub>0..1</sub>
     * Description: Resolution in Angstroms
     * Range: [Float](types/Float.md)
 * [➞resolution_high_shell_a](qualityMetrics__resolution_high_shell_a.md)  <sub>0..1</sub>
     * Description: High resolution shell limit in Angstroms
     * Range: [Float](types/Float.md)
 * [➞resolution_low_a](qualityMetrics__resolution_low_a.md)  <sub>0..1</sub>
     * Description: Low resolution limit in Angstroms
     * Range: [Float](types/Float.md)
 * [➞completeness](qualityMetrics__completeness.md)  <sub>0..1</sub>
     * Description: Data completeness percentage
     * Range: [Float](types/Float.md)
 * [➞completeness_high_res_shell_percent](qualityMetrics__completeness_high_res_shell_percent.md)  <sub>0..1</sub>
     * Description: Completeness in highest resolution shell
     * Range: [Float](types/Float.md)
 * [➞signal_to_noise](qualityMetrics__signal_to_noise.md)  <sub>0..1</sub>
     * Description: Signal to noise ratio
     * Range: [Float](types/Float.md)
 * [➞mean_i_over_sigma_i](qualityMetrics__mean_i_over_sigma_i.md)  <sub>0..1</sub>
     * Description: Mean I/sigma(I)
     * Range: [Float](types/Float.md)
 * [➞space_group](qualityMetrics__space_group.md)  <sub>0..1</sub>
     * Description: Crystallographic space group
     * Range: [String](types/String.md)
 * [➞unit_cell_a](qualityMetrics__unit_cell_a.md)  <sub>0..1</sub>
     * Description: Unit cell parameter a in Angstroms
     * Range: [Float](types/Float.md)
 * [➞unit_cell_b](qualityMetrics__unit_cell_b.md)  <sub>0..1</sub>
     * Description: Unit cell parameter b in Angstroms
     * Range: [Float](types/Float.md)
 * [➞unit_cell_c](qualityMetrics__unit_cell_c.md)  <sub>0..1</sub>
     * Description: Unit cell parameter c in Angstroms
     * Range: [Float](types/Float.md)
 * [➞unit_cell_alpha](qualityMetrics__unit_cell_alpha.md)  <sub>0..1</sub>
     * Description: Unit cell angle alpha in degrees
     * Range: [Float](types/Float.md)
 * [➞unit_cell_beta](qualityMetrics__unit_cell_beta.md)  <sub>0..1</sub>
     * Description: Unit cell angle beta in degrees
     * Range: [Float](types/Float.md)
 * [➞unit_cell_gamma](qualityMetrics__unit_cell_gamma.md)  <sub>0..1</sub>
     * Description: Unit cell angle gamma in degrees
     * Range: [Float](types/Float.md)
 * [➞multiplicity](qualityMetrics__multiplicity.md)  <sub>0..1</sub>
     * Description: Data multiplicity (redundancy)
     * Range: [Float](types/Float.md)
 * [➞cc_half](qualityMetrics__cc_half.md)  <sub>0..1</sub>
     * Description: Half-set correlation coefficient CC(1/2)
     * Range: [Float](types/Float.md)
 * [➞r_merge](qualityMetrics__r_merge.md)  <sub>0..1</sub>
     * Description: Rmerge - merge R-factor
     * Range: [Float](types/Float.md)
 * [➞r_pim](qualityMetrics__r_pim.md)  <sub>0..1</sub>
     * Description: Rpim - precision-indicating merging R-factor
     * Range: [Float](types/Float.md)
 * [➞wilson_b_factor_a2](qualityMetrics__wilson_b_factor_a2.md)  <sub>0..1</sub>
     * Description: Wilson B-factor in Angstroms squared
     * Range: [Float](types/Float.md)
 * [➞anomalous_used](qualityMetrics__anomalous_used.md)  <sub>0..1</sub>
     * Description: Whether anomalous signal was used
     * Range: [Boolean](types/Boolean.md)
 * [➞anom_corr](qualityMetrics__anom_corr.md)  <sub>0..1</sub>
     * Description: Anomalous correlation
     * Range: [Float](types/Float.md)
 * [➞anom_sig_ano](qualityMetrics__anom_sig_ano.md)  <sub>0..1</sub>
     * Description: Anomalous signal strength
     * Range: [Float](types/Float.md)
 * [➞r_work](qualityMetrics__r_work.md)  <sub>0..1</sub>
     * Description: Refinement R-factor (working set)
     * Range: [Float](types/Float.md)
 * [➞r_free](qualityMetrics__r_free.md)  <sub>0..1</sub>
     * Description: R-free (test set)
     * Range: [Float](types/Float.md)
 * [➞ramachandran_favored_percent](qualityMetrics__ramachandran_favored_percent.md)  <sub>0..1</sub>
     * Description: Percentage of residues in favored Ramachandran regions
     * Range: [Float](types/Float.md)
 * [➞ramachandran_outliers_percent](qualityMetrics__ramachandran_outliers_percent.md)  <sub>0..1</sub>
     * Description: Percentage of Ramachandran outliers
     * Range: [Float](types/Float.md)
 * [➞clashscore](qualityMetrics__clashscore.md)  <sub>0..1</sub>
     * Description: MolProbity clashscore
     * Range: [Float](types/Float.md)
 * [➞molprobity_score](qualityMetrics__molprobity_score.md)  <sub>0..1</sub>
     * Description: Overall MolProbity score
     * Range: [Float](types/Float.md)
 * [➞average_b_factor_a2](qualityMetrics__average_b_factor_a2.md)  <sub>0..1</sub>
     * Description: Average B-factor in Angstroms squared
     * Range: [Float](types/Float.md)
 * [➞i_zero](qualityMetrics__i_zero.md)  <sub>0..1</sub>
     * Description: Forward scattering intensity I(0)
     * Range: [Float](types/Float.md)
 * [➞rg](qualityMetrics__rg.md)  <sub>0..1</sub>
     * Description: Radius of gyration in Angstroms
     * Range: [Float](types/Float.md)
 * [➞r_factor](qualityMetrics__r_factor.md)  <sub>0..1</sub>
     * Description: R-factor for crystallography (deprecated, use r_work)
     * Range: [Float](types/Float.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
