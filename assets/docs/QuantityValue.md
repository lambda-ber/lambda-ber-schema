
# Class: QuantityValue

A simple quantity value, representing a measurement with a numeric value and unit. This allows data providers to specify measurements in their preferred unit while enabling standardized interpretation. For example, a pixel size could be specified as 1.5 micrometers or 15 Angstroms, with the unit clearly specified.

URI: [lambdaber:QuantityValue](https://w3id.org/lambda-ber-schema/QuantityValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionStrategy]++-%20pixel_size_calibrated%200..1>[QuantityValue&#124;maximum_numeric_value:float%20%3F;minimum_numeric_value:float%20%3F;numeric_value:float;unit:string;unit_cv_id:curie%20%3F;raw_value:string%20%3F],[ExperimentRun]++-%20beam_center_x%200..1>[QuantityValue],[ExperimentRun]++-%20beam_center_y%200..1>[QuantityValue],[ExperimentRun]++-%20detector_distance%200..1>[QuantityValue],[ExperimentRun]++-%20exposure_time%200..1>[QuantityValue],[ExperimentRun]++-%20flux%200..1>[QuantityValue],[ExperimentRun]++-%20flux_end%200..1>[QuantityValue],[ExperimentRun]++-%20oscillation_angle%200..1>[QuantityValue],[ExperimentRun]++-%20pixel_size_x%200..1>[QuantityValue],[ExperimentRun]++-%20pixel_size_y%200..1>[QuantityValue],[ExperimentRun]++-%20resolution%200..1>[QuantityValue],[ExperimentRun]++-%20resolution_at_corner%200..1>[QuantityValue],[ExperimentRun]++-%20slit_gap_horizontal%200..1>[QuantityValue],[ExperimentRun]++-%20slit_gap_vertical%200..1>[QuantityValue],[ExperimentRun]++-%20start_angle%200..1>[QuantityValue],[ExperimentRun]++-%20total_rotation%200..1>[QuantityValue],[ExperimentRun]++-%20transmission%200..1>[QuantityValue],[ExperimentRun]++-%20undulator_gap%200..1>[QuantityValue],[ExperimentRun]++-%20wavelength%200..1>[QuantityValue],[SamplePreparation]++-%20culture_volume_l%200..1>[QuantityValue],[SamplePreparation]++-%20growth_temperature_c%200..1>[QuantityValue],[Sample]++-%20molecular_weight%200..1>[QuantityValue],[WorkflowRun]++-%20anomalous_completeness%200..1>[QuantityValue],[WorkflowRun]++-%20completeness_percent%200..1>[QuantityValue],[WorkflowRun]++-%20ramachandran_favored%200..1>[QuantityValue],[WorkflowRun]++-%20ramachandran_outliers%200..1>[QuantityValue],[WorkflowRun]++-%20resolution_high%200..1>[QuantityValue],[WorkflowRun]++-%20resolution_low%200..1>[QuantityValue],[WorkflowRun]++-%20rmsd_angles%200..1>[QuantityValue],[WorkflowRun]++-%20rmsd_bonds%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_a%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_alpha%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_b%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_beta%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_c%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_gamma%200..1>[QuantityValue],[WorkflowRun]++-%20wilson_b_factor%200..1>[QuantityValue],[AttributeValue]^-[QuantityValue],[WorkflowRun],[SamplePreparation],[Sample],[ExperimentRun],[DataCollectionStrategy],[AttributeValue],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionStrategy]++-%20pixel_size_calibrated%200..1>[QuantityValue&#124;maximum_numeric_value:float%20%3F;minimum_numeric_value:float%20%3F;numeric_value:float;unit:string;unit_cv_id:curie%20%3F;raw_value:string%20%3F],[ExperimentRun]++-%20beam_center_x%200..1>[QuantityValue],[ExperimentRun]++-%20beam_center_y%200..1>[QuantityValue],[ExperimentRun]++-%20detector_distance%200..1>[QuantityValue],[ExperimentRun]++-%20exposure_time%200..1>[QuantityValue],[ExperimentRun]++-%20flux%200..1>[QuantityValue],[ExperimentRun]++-%20flux_end%200..1>[QuantityValue],[ExperimentRun]++-%20oscillation_angle%200..1>[QuantityValue],[ExperimentRun]++-%20pixel_size_x%200..1>[QuantityValue],[ExperimentRun]++-%20pixel_size_y%200..1>[QuantityValue],[ExperimentRun]++-%20resolution%200..1>[QuantityValue],[ExperimentRun]++-%20resolution_at_corner%200..1>[QuantityValue],[ExperimentRun]++-%20slit_gap_horizontal%200..1>[QuantityValue],[ExperimentRun]++-%20slit_gap_vertical%200..1>[QuantityValue],[ExperimentRun]++-%20start_angle%200..1>[QuantityValue],[ExperimentRun]++-%20total_rotation%200..1>[QuantityValue],[ExperimentRun]++-%20transmission%200..1>[QuantityValue],[ExperimentRun]++-%20undulator_gap%200..1>[QuantityValue],[ExperimentRun]++-%20wavelength%200..1>[QuantityValue],[SamplePreparation]++-%20culture_volume_l%200..1>[QuantityValue],[SamplePreparation]++-%20growth_temperature_c%200..1>[QuantityValue],[Sample]++-%20molecular_weight%200..1>[QuantityValue],[WorkflowRun]++-%20anomalous_completeness%200..1>[QuantityValue],[WorkflowRun]++-%20completeness_percent%200..1>[QuantityValue],[WorkflowRun]++-%20ramachandran_favored%200..1>[QuantityValue],[WorkflowRun]++-%20ramachandran_outliers%200..1>[QuantityValue],[WorkflowRun]++-%20resolution_high%200..1>[QuantityValue],[WorkflowRun]++-%20resolution_low%200..1>[QuantityValue],[WorkflowRun]++-%20rmsd_angles%200..1>[QuantityValue],[WorkflowRun]++-%20rmsd_bonds%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_a%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_alpha%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_b%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_beta%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_c%200..1>[QuantityValue],[WorkflowRun]++-%20unit_cell_gamma%200..1>[QuantityValue],[WorkflowRun]++-%20wilson_b_factor%200..1>[QuantityValue],[AttributeValue]^-[QuantityValue],[WorkflowRun],[SamplePreparation],[Sample],[ExperimentRun],[DataCollectionStrategy],[AttributeValue],[Attribute])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any attribute of an entity. This object can hold both the un-normalized atomic value and the structured value.

## Referenced by Class

 *  **None** *[➞pixel_size_calibrated](dataCollectionStrategy__pixel_size_calibrated.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞beam_center_x](experimentRun__beam_center_x.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞beam_center_y](experimentRun__beam_center_y.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞detector_distance](experimentRun__detector_distance.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞exposure_time](experimentRun__exposure_time.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞flux](experimentRun__flux.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞flux_end](experimentRun__flux_end.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞oscillation_angle](experimentRun__oscillation_angle.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞pixel_size_x](experimentRun__pixel_size_x.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞pixel_size_y](experimentRun__pixel_size_y.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞resolution](experimentRun__resolution.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞resolution_at_corner](experimentRun__resolution_at_corner.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞slit_gap_horizontal](experimentRun__slit_gap_horizontal.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞slit_gap_vertical](experimentRun__slit_gap_vertical.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞start_angle](experimentRun__start_angle.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞total_rotation](experimentRun__total_rotation.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞transmission](experimentRun__transmission.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞undulator_gap](experimentRun__undulator_gap.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞wavelength](experimentRun__wavelength.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞culture_volume_l](samplePreparation__culture_volume_l.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞growth_temperature_c](samplePreparation__growth_temperature_c.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞molecular_weight](sample__molecular_weight.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞anomalous_completeness](workflowRun__anomalous_completeness.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞completeness_percent](workflowRun__completeness_percent.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞ramachandran_favored](workflowRun__ramachandran_favored.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞ramachandran_outliers](workflowRun__ramachandran_outliers.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞resolution_high](workflowRun__resolution_high.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞resolution_low](workflowRun__resolution_low.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞rmsd_angles](workflowRun__rmsd_angles.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞rmsd_bonds](workflowRun__rmsd_bonds.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞unit_cell_a](workflowRun__unit_cell_a.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞unit_cell_alpha](workflowRun__unit_cell_alpha.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞unit_cell_b](workflowRun__unit_cell_b.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞unit_cell_beta](workflowRun__unit_cell_beta.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞unit_cell_c](workflowRun__unit_cell_c.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞unit_cell_gamma](workflowRun__unit_cell_gamma.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**
 *  **None** *[➞wilson_b_factor](workflowRun__wilson_b_factor.md)*  <sub>0..1</sub>  **[QuantityValue](QuantityValue.md)**

## Attributes


### Own

 * [maximum_numeric_value](maximum_numeric_value.md)  <sub>0..1</sub>
     * Description: The maximum value part, expressed as a number, of the quantity value when the value covers a range.
     * Range: [Float](types/Float.md)
 * [minimum_numeric_value](minimum_numeric_value.md)  <sub>0..1</sub>
     * Description: The minimum value part, expressed as a number, of the quantity value when the value covers a range.
     * Range: [Float](types/Float.md)
 * [QuantityValue➞numeric_value](QuantityValue_numeric_value.md)  <sub>1..1</sub>
     * Description: The numerical value of the quantity
     * Range: [Float](types/Float.md)
 * [QuantityValue➞unit](QuantityValue_unit.md)  <sub>1..1</sub>
     * Description: The unit of measurement (e.g., "Angstroms", "micrometers", "kilodaltons"). Should match the UCUM standard notation or Unit Ontology.
     * Range: [String](types/String.md)
 * [unit_cv_id](unit_cv_id.md)  <sub>0..1</sub>
     * Description: The unit of the quantity, expressed as a CURIE from the Unit Ontology (e.g., UO:0000016 for micrometer).
     * Range: [Curie](types/Curie.md)
 * [QuantityValue➞raw_value](QuantityValue_raw_value.md)  <sub>0..1</sub>
     * Description: Unnormalized atomic string representation, suggested syntax {number} {unit}
     * Range: [String](types/String.md)
     * Example: 1.5 micrometers None
     * Example: 50 Angstroms None

### Inherited from AttributeValue:

 * [➞attribute](attributeValue__attribute.md)  <sub>0..1</sub>
     * Description: The attribute being represented.
     * Range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | nmdc:QuantityValue |
|  | | schema:QuantityValue |
