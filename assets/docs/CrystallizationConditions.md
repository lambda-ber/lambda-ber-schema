
# Class: CrystallizationConditions

Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization mapping)

URI: [lambdaber:CrystallizationConditions](https://w3id.org/lambda-ber-schema/CrystallizationConditions)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[XRayPreparation]++-%20crystallization_conditions%200..1>[CrystallizationConditions&#124;method:CrystallizationMethodEnum%20%3F;crystallization_conditions:string%20%3F;drop_volume:float%20%3F;protein_concentration:float%20%3F;crystal_size_um:string%20%3F;cryo_protectant:string%20%3F;crystal_id:string%20%3F;screen_name:string%20%3F;temperature_c:float%20%3F;drop_ratio_protein_to_reservoir:string%20%3F;reservoir_volume_ul:float%20%3F;seeding_type:string%20%3F;seed_stock_dilution:string%20%3F;description(i):string%20%3F],[AttributeGroup]^-[CrystallizationConditions],[XRayPreparation],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[XRayPreparation]++-%20crystallization_conditions%200..1>[CrystallizationConditions&#124;method:CrystallizationMethodEnum%20%3F;crystallization_conditions:string%20%3F;drop_volume:float%20%3F;protein_concentration:float%20%3F;crystal_size_um:string%20%3F;cryo_protectant:string%20%3F;crystal_id:string%20%3F;screen_name:string%20%3F;temperature_c:float%20%3F;drop_ratio_protein_to_reservoir:string%20%3F;reservoir_volume_ul:float%20%3F;seeding_type:string%20%3F;seed_stock_dilution:string%20%3F;description(i):string%20%3F],[AttributeGroup]^-[CrystallizationConditions],[XRayPreparation],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞crystallization_conditions](xRayPreparation__crystallization_conditions.md)*  <sub>0..1</sub>  **[CrystallizationConditions](CrystallizationConditions.md)**

## Attributes


### Own

 * [➞method](crystallizationConditions__method.md)  <sub>0..1</sub>
     * Description: Crystallization method used
     * Range: [CrystallizationMethodEnum](CrystallizationMethodEnum.md)
 * [➞crystallization_conditions](crystallizationConditions__crystallization_conditions.md)  <sub>0..1</sub>
     * Description: Complete description of crystallization conditions including precipitant, pH, salts
     * Range: [String](types/String.md)
 * [➞drop_volume](crystallizationConditions__drop_volume.md)  <sub>0..1</sub>
     * Description: Total drop volume in nanoliters
     * Range: [Float](types/Float.md)
 * [➞protein_concentration](crystallizationConditions__protein_concentration.md)  <sub>0..1</sub>
     * Description: Protein concentration for crystallization in mg/mL
     * Range: [Float](types/Float.md)
 * [➞crystal_size_um](crystallizationConditions__crystal_size_um.md)  <sub>0..1</sub>
     * Description: Crystal dimensions in micrometers (length x width x height)
     * Range: [String](types/String.md)
 * [➞cryo_protectant](crystallizationConditions__cryo_protectant.md)  <sub>0..1</sub>
     * Description: Cryoprotectant used for crystal cooling
     * Range: [String](types/String.md)
 * [➞crystal_id](crystallizationConditions__crystal_id.md)  <sub>0..1</sub>
     * Description: Identifier for the specific crystal used
     * Range: [String](types/String.md)
 * [➞screen_name](crystallizationConditions__screen_name.md)  <sub>0..1</sub>
     * Description: Name of crystallization screen used
     * Range: [String](types/String.md)
 * [➞temperature_c](crystallizationConditions__temperature_c.md)  <sub>0..1</sub>
     * Description: Crystallization temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞drop_ratio_protein_to_reservoir](crystallizationConditions__drop_ratio_protein_to_reservoir.md)  <sub>0..1</sub>
     * Description: Ratio of protein to reservoir solution in drop (e.g., 1:1, 2:1)
     * Range: [String](types/String.md)
 * [➞reservoir_volume_ul](crystallizationConditions__reservoir_volume_ul.md)  <sub>0..1</sub>
     * Description: Reservoir volume in microliters
     * Range: [Float](types/Float.md)
 * [➞seeding_type](crystallizationConditions__seeding_type.md)  <sub>0..1</sub>
     * Description: Type of seeding used (micro, macro, streak)
     * Range: [String](types/String.md)
 * [➞seed_stock_dilution](crystallizationConditions__seed_stock_dilution.md)  <sub>0..1</sub>
     * Description: Dilution factor for seed stock
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
