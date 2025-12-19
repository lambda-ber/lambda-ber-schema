
# Class: XRayPreparation

X-ray crystallography specific preparation

URI: [lambdaber:XRayPreparation](https://w3id.org/lambda-ber-schema/XRayPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<mounting_temperature%200..1-++[XRayPreparation&#124;protein_buffer:string%20%3F;additives:string%20%3F;crystallization_method:CrystallizationMethodEnum%20%3F;screen_name:string%20%3F;drop_ratio_protein_to_reservoir:string%20%3F;seeding_type:string%20%3F;seed_stock_dilution:string%20%3F;initial_hit_condition:string%20%3F;optimization_strategy:string%20%3F;optimized_condition:string%20%3F;crystal_size_um:string%20%3F;cryoprotectant:string%20%3F;soak_compound:string%20%3F;soak_conditions:string%20%3F;mounting_method:string%20%3F;flash_cooling_method:string%20%3F;crystal_notes:string%20%3F;description(i):string%20%3F],[QuantityValue]<loop_size%200..1-++[XRayPreparation],[QuantityValue]<cryoprotectant_concentration%200..1-++[XRayPreparation],[QuantityValue]<reservoir_volume_ul%200..1-++[XRayPreparation],[QuantityValue]<drop_volume_nl%200..1-++[XRayPreparation],[QuantityValue]<temperature_c%200..1-++[XRayPreparation],[CrystallizationConditions]<crystallization_conditions%200..1-++[XRayPreparation],[QuantityValue]<protein_concentration_mg_per_ml%200..1-++[XRayPreparation],[TechniqueSpecificPreparation]^-[XRayPreparation],[TechniqueSpecificPreparation],[QuantityValue],[CrystallizationConditions])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<mounting_temperature%200..1-++[XRayPreparation&#124;protein_buffer:string%20%3F;additives:string%20%3F;crystallization_method:CrystallizationMethodEnum%20%3F;screen_name:string%20%3F;drop_ratio_protein_to_reservoir:string%20%3F;seeding_type:string%20%3F;seed_stock_dilution:string%20%3F;initial_hit_condition:string%20%3F;optimization_strategy:string%20%3F;optimized_condition:string%20%3F;crystal_size_um:string%20%3F;cryoprotectant:string%20%3F;soak_compound:string%20%3F;soak_conditions:string%20%3F;mounting_method:string%20%3F;flash_cooling_method:string%20%3F;crystal_notes:string%20%3F;description(i):string%20%3F],[QuantityValue]<loop_size%200..1-++[XRayPreparation],[QuantityValue]<cryoprotectant_concentration%200..1-++[XRayPreparation],[QuantityValue]<reservoir_volume_ul%200..1-++[XRayPreparation],[QuantityValue]<drop_volume_nl%200..1-++[XRayPreparation],[QuantityValue]<temperature_c%200..1-++[XRayPreparation],[CrystallizationConditions]<crystallization_conditions%200..1-++[XRayPreparation],[QuantityValue]<protein_concentration_mg_per_ml%200..1-++[XRayPreparation],[TechniqueSpecificPreparation]^-[XRayPreparation],[TechniqueSpecificPreparation],[QuantityValue],[CrystallizationConditions])

## Parents

 *  is_a: [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) - Base class for technique-specific preparation details

## Attributes


### Own

 * [➞protein_concentration_mg_per_ml](xRayPreparation__protein_concentration_mg_per_ml.md)  <sub>0..1</sub>
     * Description: Protein concentration for crystallization in mg/mL
     * Range: [QuantityValue](QuantityValue.md)
 * [➞protein_buffer](xRayPreparation__protein_buffer.md)  <sub>0..1</sub>
     * Description: Buffer composition for protein solution
     * Range: [String](types/String.md)
 * [➞additives](xRayPreparation__additives.md)  <sub>0..1</sub>
     * Description: Additives mixed with protein before crystallization
     * Range: [String](types/String.md)
 * [➞crystallization_method](xRayPreparation__crystallization_method.md)  <sub>0..1</sub>
     * Description: Method used for crystallization
     * Range: [CrystallizationMethodEnum](CrystallizationMethodEnum.md)
 * [➞crystallization_conditions](xRayPreparation__crystallization_conditions.md)  <sub>0..1</sub>
     * Description: Detailed crystallization conditions
     * Range: [CrystallizationConditions](CrystallizationConditions.md)
 * [➞screen_name](xRayPreparation__screen_name.md)  <sub>0..1</sub>
     * Description: Name of crystallization screen used
     * Range: [String](types/String.md)
 * [➞temperature_c](xRayPreparation__temperature_c.md)  <sub>0..1</sub>
     * Description: Crystallization temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞drop_ratio_protein_to_reservoir](xRayPreparation__drop_ratio_protein_to_reservoir.md)  <sub>0..1</sub>
     * Description: Ratio of protein to reservoir solution in drop (e.g., 1:1, 2:1)
     * Range: [String](types/String.md)
 * [➞drop_volume_nl](xRayPreparation__drop_volume_nl.md)  <sub>0..1</sub>
     * Description: Total drop volume, typically specified in nanoliters. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞reservoir_volume_ul](xRayPreparation__reservoir_volume_ul.md)  <sub>0..1</sub>
     * Description: Reservoir volume, typically specified in microliters. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞seeding_type](xRayPreparation__seeding_type.md)  <sub>0..1</sub>
     * Description: Type of seeding used (micro, macro, streak)
     * Range: [String](types/String.md)
 * [➞seed_stock_dilution](xRayPreparation__seed_stock_dilution.md)  <sub>0..1</sub>
     * Description: Dilution factor for seed stock
     * Range: [String](types/String.md)
 * [➞initial_hit_condition](xRayPreparation__initial_hit_condition.md)  <sub>0..1</sub>
     * Description: Description of initial crystallization hit condition
     * Range: [String](types/String.md)
 * [➞optimization_strategy](xRayPreparation__optimization_strategy.md)  <sub>0..1</sub>
     * Description: Strategy used to optimize crystals
     * Range: [String](types/String.md)
 * [➞optimized_condition](xRayPreparation__optimized_condition.md)  <sub>0..1</sub>
     * Description: Final optimized crystallization condition
     * Range: [String](types/String.md)
 * [➞crystal_size_um](xRayPreparation__crystal_size_um.md)  <sub>0..1</sub>
     * Description: Crystal dimensions in micrometers
     * Range: [String](types/String.md)
 * [➞cryoprotectant](xRayPreparation__cryoprotectant.md)  <sub>0..1</sub>
     * Description: Cryoprotectant used
     * Range: [String](types/String.md)
 * [➞cryoprotectant_concentration](xRayPreparation__cryoprotectant_concentration.md)  <sub>0..1</sub>
     * Description: Cryoprotectant concentration, typically specified as a percentage. Data providers may specify as decimal fraction by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞soak_compound](xRayPreparation__soak_compound.md)  <sub>0..1</sub>
     * Description: Compound used for soaking (ligand, heavy atom)
     * Range: [String](types/String.md)
 * [➞soak_conditions](xRayPreparation__soak_conditions.md)  <sub>0..1</sub>
     * Description: Conditions for crystal soaking
     * Range: [String](types/String.md)
 * [➞mounting_method](xRayPreparation__mounting_method.md)  <sub>0..1</sub>
     * Description: Crystal mounting method
     * Range: [String](types/String.md)
 * [➞flash_cooling_method](xRayPreparation__flash_cooling_method.md)  <sub>0..1</sub>
     * Description: Flash cooling protocol
     * Range: [String](types/String.md)
 * [➞crystal_notes](xRayPreparation__crystal_notes.md)  <sub>0..1</sub>
     * Description: Additional notes about crystal quality and handling
     * Range: [String](types/String.md)
 * [➞loop_size](xRayPreparation__loop_size.md)  <sub>0..1</sub>
     * Description: Loop size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞mounting_temperature](xRayPreparation__mounting_temperature.md)  <sub>0..1</sub>
     * Description: Temperature during mounting, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from TechniqueSpecificPreparation:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
