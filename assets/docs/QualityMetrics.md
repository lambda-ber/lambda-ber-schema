
# Class: QualityMetrics

Quality metrics for experiments

URI: [lambdaber:QualityMetrics](https://w3id.org/lambda-ber-schema/QualityMetrics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<r_factor%200..1-++[QualityMetrics&#124;space_group:string%20%3F;anomalous_used:boolean%20%3F;description(i):string%20%3F],[QuantityValue]<rg%200..1-++[QualityMetrics],[QuantityValue]<i_zero%200..1-++[QualityMetrics],[QuantityValue]<average_b_factor_a2%200..1-++[QualityMetrics],[QuantityValue]<molprobity_score%200..1-++[QualityMetrics],[QuantityValue]<clashscore%200..1-++[QualityMetrics],[QuantityValue]<ramachandran_outliers_percent%200..1-++[QualityMetrics],[QuantityValue]<ramachandran_favored_percent%200..1-++[QualityMetrics],[QuantityValue]<r_free%200..1-++[QualityMetrics],[QuantityValue]<r_work%200..1-++[QualityMetrics],[QuantityValue]<anom_sig_ano%200..1-++[QualityMetrics],[QuantityValue]<anom_corr%200..1-++[QualityMetrics],[QuantityValue]<wilson_b_factor_a2%200..1-++[QualityMetrics],[QuantityValue]<r_pim%200..1-++[QualityMetrics],[QuantityValue]<r_merge%200..1-++[QualityMetrics],[QuantityValue]<cc_half%200..1-++[QualityMetrics],[QuantityValue]<multiplicity%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_gamma%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_beta%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_alpha%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_c%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_b%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_a%200..1-++[QualityMetrics],[QuantityValue]<mean_i_over_sigma_i%200..1-++[QualityMetrics],[QuantityValue]<signal_to_noise%200..1-++[QualityMetrics],[QuantityValue]<completeness_high_res_shell_percent%200..1-++[QualityMetrics],[QuantityValue]<completeness%200..1-++[QualityMetrics],[QuantityValue]<resolution_low_a%200..1-++[QualityMetrics],[QuantityValue]<resolution_high_shell_a%200..1-++[QualityMetrics],[QuantityValue]<resolution%200..1-++[QualityMetrics],[ExperimentRun]++-%20quality_metrics%200..1>[QualityMetrics],[AttributeGroup]^-[QualityMetrics],[ExperimentRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<r_factor%200..1-++[QualityMetrics&#124;space_group:string%20%3F;anomalous_used:boolean%20%3F;description(i):string%20%3F],[QuantityValue]<rg%200..1-++[QualityMetrics],[QuantityValue]<i_zero%200..1-++[QualityMetrics],[QuantityValue]<average_b_factor_a2%200..1-++[QualityMetrics],[QuantityValue]<molprobity_score%200..1-++[QualityMetrics],[QuantityValue]<clashscore%200..1-++[QualityMetrics],[QuantityValue]<ramachandran_outliers_percent%200..1-++[QualityMetrics],[QuantityValue]<ramachandran_favored_percent%200..1-++[QualityMetrics],[QuantityValue]<r_free%200..1-++[QualityMetrics],[QuantityValue]<r_work%200..1-++[QualityMetrics],[QuantityValue]<anom_sig_ano%200..1-++[QualityMetrics],[QuantityValue]<anom_corr%200..1-++[QualityMetrics],[QuantityValue]<wilson_b_factor_a2%200..1-++[QualityMetrics],[QuantityValue]<r_pim%200..1-++[QualityMetrics],[QuantityValue]<r_merge%200..1-++[QualityMetrics],[QuantityValue]<cc_half%200..1-++[QualityMetrics],[QuantityValue]<multiplicity%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_gamma%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_beta%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_alpha%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_c%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_b%200..1-++[QualityMetrics],[QuantityValue]<unit_cell_a%200..1-++[QualityMetrics],[QuantityValue]<mean_i_over_sigma_i%200..1-++[QualityMetrics],[QuantityValue]<signal_to_noise%200..1-++[QualityMetrics],[QuantityValue]<completeness_high_res_shell_percent%200..1-++[QualityMetrics],[QuantityValue]<completeness%200..1-++[QualityMetrics],[QuantityValue]<resolution_low_a%200..1-++[QualityMetrics],[QuantityValue]<resolution_high_shell_a%200..1-++[QualityMetrics],[QuantityValue]<resolution%200..1-++[QualityMetrics],[ExperimentRun]++-%20quality_metrics%200..1>[QualityMetrics],[AttributeGroup]^-[QualityMetrics],[ExperimentRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞quality_metrics](experimentRun__quality_metrics.md)*  <sub>0..1</sub>  **[QualityMetrics](QualityMetrics.md)**

## Attributes


### Own

 * [➞resolution](qualityMetrics__resolution.md)  <sub>0..1</sub>
     * Description: Resolution, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞resolution_high_shell_a](qualityMetrics__resolution_high_shell_a.md)  <sub>0..1</sub>
     * Description: High resolution shell limit, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞resolution_low_a](qualityMetrics__resolution_low_a.md)  <sub>0..1</sub>
     * Description: Low resolution limit, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞completeness](qualityMetrics__completeness.md)  <sub>0..1</sub>
     * Description: Data completeness, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞completeness_high_res_shell_percent](qualityMetrics__completeness_high_res_shell_percent.md)  <sub>0..1</sub>
     * Description: Completeness in highest resolution shell, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞signal_to_noise](qualityMetrics__signal_to_noise.md)  <sub>0..1</sub>
     * Description: Signal to noise ratio
     * Range: [QuantityValue](QuantityValue.md)
 * [➞mean_i_over_sigma_i](qualityMetrics__mean_i_over_sigma_i.md)  <sub>0..1</sub>
     * Description: Mean I/sigma(I)
     * Range: [QuantityValue](QuantityValue.md)
 * [➞space_group](qualityMetrics__space_group.md)  <sub>0..1</sub>
     * Description: Crystallographic space group
     * Range: [String](types/String.md)
 * [➞unit_cell_a](qualityMetrics__unit_cell_a.md)  <sub>0..1</sub>
     * Description: Unit cell parameter a, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_b](qualityMetrics__unit_cell_b.md)  <sub>0..1</sub>
     * Description: Unit cell parameter b, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_c](qualityMetrics__unit_cell_c.md)  <sub>0..1</sub>
     * Description: Unit cell parameter c, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_alpha](qualityMetrics__unit_cell_alpha.md)  <sub>0..1</sub>
     * Description: Unit cell angle alpha, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_beta](qualityMetrics__unit_cell_beta.md)  <sub>0..1</sub>
     * Description: Unit cell angle beta, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞unit_cell_gamma](qualityMetrics__unit_cell_gamma.md)  <sub>0..1</sub>
     * Description: Unit cell angle gamma, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞multiplicity](qualityMetrics__multiplicity.md)  <sub>0..1</sub>
     * Description: Data multiplicity (redundancy)
     * Range: [QuantityValue](QuantityValue.md)
 * [➞cc_half](qualityMetrics__cc_half.md)  <sub>0..1</sub>
     * Description: Half-set correlation coefficient CC(1/2)
     * Range: [QuantityValue](QuantityValue.md)
 * [➞r_merge](qualityMetrics__r_merge.md)  <sub>0..1</sub>
     * Description: Rmerge - merge R-factor
     * Range: [QuantityValue](QuantityValue.md)
 * [➞r_pim](qualityMetrics__r_pim.md)  <sub>0..1</sub>
     * Description: Rpim - precision-indicating merging R-factor
     * Range: [QuantityValue](QuantityValue.md)
 * [➞wilson_b_factor_a2](qualityMetrics__wilson_b_factor_a2.md)  <sub>0..1</sub>
     * Description: Wilson B-factor in Angstroms squared
     * Range: [QuantityValue](QuantityValue.md)
 * [➞anomalous_used](qualityMetrics__anomalous_used.md)  <sub>0..1</sub>
     * Description: Whether anomalous signal was used
     * Range: [Boolean](types/Boolean.md)
 * [➞anom_corr](qualityMetrics__anom_corr.md)  <sub>0..1</sub>
     * Description: Anomalous correlation
     * Range: [QuantityValue](QuantityValue.md)
 * [➞anom_sig_ano](qualityMetrics__anom_sig_ano.md)  <sub>0..1</sub>
     * Description: Anomalous signal strength
     * Range: [QuantityValue](QuantityValue.md)
 * [➞r_work](qualityMetrics__r_work.md)  <sub>0..1</sub>
     * Description: Refinement R-factor (working set)
     * Range: [QuantityValue](QuantityValue.md)
 * [➞r_free](qualityMetrics__r_free.md)  <sub>0..1</sub>
     * Description: R-free (test set)
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ramachandran_favored_percent](qualityMetrics__ramachandran_favored_percent.md)  <sub>0..1</sub>
     * Description: Percentage of residues in favored Ramachandran regions
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ramachandran_outliers_percent](qualityMetrics__ramachandran_outliers_percent.md)  <sub>0..1</sub>
     * Description: Percentage of Ramachandran outliers
     * Range: [QuantityValue](QuantityValue.md)
 * [➞clashscore](qualityMetrics__clashscore.md)  <sub>0..1</sub>
     * Description: MolProbity clashscore
     * Range: [QuantityValue](QuantityValue.md)
 * [➞molprobity_score](qualityMetrics__molprobity_score.md)  <sub>0..1</sub>
     * Description: Overall MolProbity score
     * Range: [QuantityValue](QuantityValue.md)
 * [➞average_b_factor_a2](qualityMetrics__average_b_factor_a2.md)  <sub>0..1</sub>
     * Description: Average B-factor in Angstroms squared
     * Range: [QuantityValue](QuantityValue.md)
 * [➞i_zero](qualityMetrics__i_zero.md)  <sub>0..1</sub>
     * Description: Forward scattering intensity I(0)
     * Range: [QuantityValue](QuantityValue.md)
 * [➞rg](qualityMetrics__rg.md)  <sub>0..1</sub>
     * Description: Radius of gyration, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞r_factor](qualityMetrics__r_factor.md)  <sub>0..1</sub>
     * Description: R-factor for crystallography (deprecated, use r_work)
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
