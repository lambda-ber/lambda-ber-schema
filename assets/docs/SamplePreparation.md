
# Class: SamplePreparation

A process that prepares a sample for imaging

URI: [lambdaber:SamplePreparation](https://w3id.org/lambda-ber-schema/SamplePreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]++-%20sample_preparations%200..*>[SamplePreparation&#124;preparation_type:PreparationTypeEnum;sample_id:string;preparation_date:string%20%3F;operator_id:string%20%3F;protocol_description:string%20%3F;expression_system:ExpressionSystemEnum%20%3F;host_strain_or_cell_line:string%20%3F;culture_volume_l:float%20%3F;medium:string%20%3F;antibiotic_selection:string%20%3F;growth_temperature_c:float%20%3F;induction_agent:string%20%3F;inducer_concentration:string%20%3F;induction_temperature_c:float%20%3F;induction_time_h:float%20%3F;od600_at_induction:float%20%3F;harvest_timepoint:string%20%3F;lysis_method:string%20%3F;protease_inhibitors:string%20%3F;purification_steps:PurificationStepEnum%20*;affinity_type:string%20%3F;affinity_column:string%20%3F;lysis_buffer:string%20%3F;wash_buffer:string%20%3F;elution_buffer:string%20%3F;tag_removal:boolean%20%3F;protease:string%20%3F;protease_ratio:string%20%3F;cleavage_time_h:float%20%3F;cleavage_temperature_c:float%20%3F;second_affinity_reverse:string%20%3F;iex_column:string%20%3F;hic_column:string%20%3F;sec_column:string%20%3F;sec_buffer:string%20%3F;concentration_method:string%20%3F;final_buffer:string%20%3F;final_concentration_mg_per_ml:float%20%3F;yield_mg:float%20%3F;purity_by_sds_page_percent:float%20%3F;aggregation_assessment:string%20%3F;aliquoting:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[SamplePreparation],[Study],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]++-%20sample_preparations%200..*>[SamplePreparation&#124;preparation_type:PreparationTypeEnum;sample_id:string;preparation_date:string%20%3F;operator_id:string%20%3F;protocol_description:string%20%3F;expression_system:ExpressionSystemEnum%20%3F;host_strain_or_cell_line:string%20%3F;culture_volume_l:float%20%3F;medium:string%20%3F;antibiotic_selection:string%20%3F;growth_temperature_c:float%20%3F;induction_agent:string%20%3F;inducer_concentration:string%20%3F;induction_temperature_c:float%20%3F;induction_time_h:float%20%3F;od600_at_induction:float%20%3F;harvest_timepoint:string%20%3F;lysis_method:string%20%3F;protease_inhibitors:string%20%3F;purification_steps:PurificationStepEnum%20*;affinity_type:string%20%3F;affinity_column:string%20%3F;lysis_buffer:string%20%3F;wash_buffer:string%20%3F;elution_buffer:string%20%3F;tag_removal:boolean%20%3F;protease:string%20%3F;protease_ratio:string%20%3F;cleavage_time_h:float%20%3F;cleavage_temperature_c:float%20%3F;second_affinity_reverse:string%20%3F;iex_column:string%20%3F;hic_column:string%20%3F;sec_column:string%20%3F;sec_buffer:string%20%3F;concentration_method:string%20%3F;final_buffer:string%20%3F;final_concentration_mg_per_ml:float%20%3F;yield_mg:float%20%3F;purity_by_sds_page_percent:float%20%3F;aggregation_assessment:string%20%3F;aliquoting:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[SamplePreparation],[Study],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞sample_preparations](study__sample_preparations.md)*  <sub>0..\*</sub>  **[SamplePreparation](SamplePreparation.md)**

## Attributes


### Own

 * [➞preparation_type](samplePreparation__preparation_type.md)  <sub>1..1</sub>
     * Description: Type of sample preparation
     * Range: [PreparationTypeEnum](PreparationTypeEnum.md)
 * [➞sample_id](samplePreparation__sample_id.md)  <sub>1..1</sub>
     * Description: Reference to the sample being prepared
     * Range: [String](types/String.md)
 * [➞preparation_date](samplePreparation__preparation_date.md)  <sub>0..1</sub>
     * Description: Date of sample preparation
     * Range: [String](types/String.md)
 * [➞operator_id](samplePreparation__operator_id.md)  <sub>0..1</sub>
     * Description: Identifier or name of the person who performed the sample preparation (e.g., 'jsmith', 'John Smith', or personnel ID)
     * Range: [String](types/String.md)
 * [➞protocol_description](samplePreparation__protocol_description.md)  <sub>0..1</sub>
     * Description: Detailed protocol description
     * Range: [String](types/String.md)
 * [➞expression_system](samplePreparation__expression_system.md)  <sub>0..1</sub>
     * Description: Expression system used for recombinant protein production
     * Range: [ExpressionSystemEnum](ExpressionSystemEnum.md)
 * [➞host_strain_or_cell_line](samplePreparation__host_strain_or_cell_line.md)  <sub>0..1</sub>
     * Description: Specific strain or cell line used (e.g., BL21(DE3), Sf9, HEK293F)
     * Range: [String](types/String.md)
 * [➞culture_volume_l](samplePreparation__culture_volume_l.md)  <sub>0..1</sub>
     * Description: Culture volume in liters
     * Range: [Float](types/Float.md)
 * [➞medium](samplePreparation__medium.md)  <sub>0..1</sub>
     * Description: Growth medium used
     * Range: [String](types/String.md)
 * [➞antibiotic_selection](samplePreparation__antibiotic_selection.md)  <sub>0..1</sub>
     * Description: Antibiotic or selection agent used
     * Range: [String](types/String.md)
 * [➞growth_temperature_c](samplePreparation__growth_temperature_c.md)  <sub>0..1</sub>
     * Description: Growth temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞induction_agent](samplePreparation__induction_agent.md)  <sub>0..1</sub>
     * Description: Agent used to induce expression (e.g., IPTG, tetracycline)
     * Range: [String](types/String.md)
 * [➞inducer_concentration](samplePreparation__inducer_concentration.md)  <sub>0..1</sub>
     * Description: Concentration of induction agent
     * Range: [String](types/String.md)
 * [➞induction_temperature_c](samplePreparation__induction_temperature_c.md)  <sub>0..1</sub>
     * Description: Temperature during induction in Celsius
     * Range: [Float](types/Float.md)
 * [➞induction_time_h](samplePreparation__induction_time_h.md)  <sub>0..1</sub>
     * Description: Duration of induction in hours
     * Range: [Float](types/Float.md)
 * [➞od600_at_induction](samplePreparation__od600_at_induction.md)  <sub>0..1</sub>
     * Description: Optical density at 600nm when induction was started
     * Range: [Float](types/Float.md)
 * [➞harvest_timepoint](samplePreparation__harvest_timepoint.md)  <sub>0..1</sub>
     * Description: Time point when cells were harvested
     * Range: [String](types/String.md)
 * [➞lysis_method](samplePreparation__lysis_method.md)  <sub>0..1</sub>
     * Description: Method used for cell lysis
     * Range: [String](types/String.md)
 * [➞protease_inhibitors](samplePreparation__protease_inhibitors.md)  <sub>0..1</sub>
     * Description: Protease inhibitors added
     * Range: [String](types/String.md)
 * [➞purification_steps](samplePreparation__purification_steps.md)  <sub>0..\*</sub>
     * Description: Ordered list of purification steps performed
     * Range: [PurificationStepEnum](PurificationStepEnum.md)
 * [➞affinity_type](samplePreparation__affinity_type.md)  <sub>0..1</sub>
     * Description: Type of affinity chromatography
     * Range: [String](types/String.md)
 * [➞affinity_column](samplePreparation__affinity_column.md)  <sub>0..1</sub>
     * Description: Affinity column specifications
     * Range: [String](types/String.md)
 * [➞lysis_buffer](samplePreparation__lysis_buffer.md)  <sub>0..1</sub>
     * Description: Buffer composition for lysis
     * Range: [String](types/String.md)
 * [➞wash_buffer](samplePreparation__wash_buffer.md)  <sub>0..1</sub>
     * Description: Buffer composition for washing
     * Range: [String](types/String.md)
 * [➞elution_buffer](samplePreparation__elution_buffer.md)  <sub>0..1</sub>
     * Description: Buffer composition for elution
     * Range: [String](types/String.md)
 * [➞tag_removal](samplePreparation__tag_removal.md)  <sub>0..1</sub>
     * Description: Whether and how affinity tag was removed
     * Range: [Boolean](types/Boolean.md)
 * [➞protease](samplePreparation__protease.md)  <sub>0..1</sub>
     * Description: Protease used for tag cleavage
     * Range: [String](types/String.md)
 * [➞protease_ratio](samplePreparation__protease_ratio.md)  <sub>0..1</sub>
     * Description: Ratio of protease to protein
     * Range: [String](types/String.md)
 * [➞cleavage_time_h](samplePreparation__cleavage_time_h.md)  <sub>0..1</sub>
     * Description: Duration of protease cleavage in hours
     * Range: [Float](types/Float.md)
 * [➞cleavage_temperature_c](samplePreparation__cleavage_temperature_c.md)  <sub>0..1</sub>
     * Description: Temperature during cleavage in Celsius
     * Range: [Float](types/Float.md)
 * [➞second_affinity_reverse](samplePreparation__second_affinity_reverse.md)  <sub>0..1</sub>
     * Description: Second affinity or reverse affinity step
     * Range: [String](types/String.md)
 * [➞iex_column](samplePreparation__iex_column.md)  <sub>0..1</sub>
     * Description: Ion-exchange column used
     * Range: [String](types/String.md)
 * [➞hic_column](samplePreparation__hic_column.md)  <sub>0..1</sub>
     * Description: Hydrophobic interaction column used
     * Range: [String](types/String.md)
 * [➞sec_column](samplePreparation__sec_column.md)  <sub>0..1</sub>
     * Description: Size-exclusion column used
     * Range: [String](types/String.md)
 * [➞sec_buffer](samplePreparation__sec_buffer.md)  <sub>0..1</sub>
     * Description: Buffer for size-exclusion chromatography
     * Range: [String](types/String.md)
 * [➞concentration_method](samplePreparation__concentration_method.md)  <sub>0..1</sub>
     * Description: Method used to concentrate protein
     * Range: [String](types/String.md)
 * [➞final_buffer](samplePreparation__final_buffer.md)  <sub>0..1</sub>
     * Description: Final buffer composition after purification
     * Range: [String](types/String.md)
 * [➞final_concentration_mg_per_ml](samplePreparation__final_concentration_mg_per_ml.md)  <sub>0..1</sub>
     * Description: Final protein concentration in mg/mL
     * Range: [Float](types/Float.md)
 * [➞yield_mg](samplePreparation__yield_mg.md)  <sub>0..1</sub>
     * Description: Total yield in milligrams
     * Range: [Float](types/Float.md)
 * [➞purity_by_sds_page_percent](samplePreparation__purity_by_sds_page_percent.md)  <sub>0..1</sub>
     * Description: Purity percentage by SDS-PAGE
     * Range: [Float](types/Float.md)
 * [➞aggregation_assessment](samplePreparation__aggregation_assessment.md)  <sub>0..1</sub>
     * Description: Assessment of protein aggregation state
     * Range: [String](types/String.md)
 * [➞aliquoting](samplePreparation__aliquoting.md)  <sub>0..1</sub>
     * Description: How the protein was aliquoted for storage
     * Range: [String](types/String.md)

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
