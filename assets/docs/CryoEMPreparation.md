
# Class: CryoEMPreparation

Cryo-EM specific sample preparation

URI: [lambdaber:CryoEMPreparation](https://w3id.org/lambda-ber-schema/CryoEMPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation],[TechniqueSpecificPreparation]^-[CryoEMPreparation&#124;grid_type:GridTypeEnum%20%3F;support_film:string%20%3F;hole_size:float%20%3F;vitrification_method:VitrificationMethodEnum%20%3F;blot_time:float%20%3F;blot_force:integer%20%3F;humidity_percentage:float%20%3F;chamber_temperature:float%20%3F;grid_material:GridMaterialEnum%20%3F;glow_discharge_applied:boolean%20%3F;glow_discharge_time:float%20%3F;glow_discharge_current:float%20%3F;glow_discharge_atmosphere:string%20%3F;glow_discharge_pressure:float%20%3F;vitrification_instrument:string%20%3F;blot_number:integer%20%3F;wait_time:float%20%3F;blotter_height:float%20%3F;blotter_setting:float%20%3F;sample_applied_volume:float%20%3F;ethane_temperature:float%20%3F;plasma_treatment:string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation],[TechniqueSpecificPreparation]^-[CryoEMPreparation&#124;grid_type:GridTypeEnum%20%3F;support_film:string%20%3F;hole_size:float%20%3F;vitrification_method:VitrificationMethodEnum%20%3F;blot_time:float%20%3F;blot_force:integer%20%3F;humidity_percentage:float%20%3F;chamber_temperature:float%20%3F;grid_material:GridMaterialEnum%20%3F;glow_discharge_applied:boolean%20%3F;glow_discharge_time:float%20%3F;glow_discharge_current:float%20%3F;glow_discharge_atmosphere:string%20%3F;glow_discharge_pressure:float%20%3F;vitrification_instrument:string%20%3F;blot_number:integer%20%3F;wait_time:float%20%3F;blotter_height:float%20%3F;blotter_setting:float%20%3F;sample_applied_volume:float%20%3F;ethane_temperature:float%20%3F;plasma_treatment:string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) - Base class for technique-specific preparation details

## Attributes


### Own

 * [➞grid_type](cryoEMPreparation__grid_type.md)  <sub>0..1</sub>
     * Description: Type of EM grid used
     * Range: [GridTypeEnum](GridTypeEnum.md)
 * [➞support_film](cryoEMPreparation__support_film.md)  <sub>0..1</sub>
     * Description: Support film type
     * Range: [String](types/String.md)
 * [➞hole_size](cryoEMPreparation__hole_size.md)  <sub>0..1</sub>
     * Description: Hole size in micrometers
     * Range: [Float](types/Float.md)
 * [➞vitrification_method](cryoEMPreparation__vitrification_method.md)  <sub>0..1</sub>
     * Description: Method used for vitrification
     * Range: [VitrificationMethodEnum](VitrificationMethodEnum.md)
 * [➞blot_time](cryoEMPreparation__blot_time.md)  <sub>0..1</sub>
     * Description: Blotting time in seconds
     * Range: [Float](types/Float.md)
 * [➞blot_force](cryoEMPreparation__blot_force.md)  <sub>0..1</sub>
     * Description: Blotting force setting
     * Range: [Integer](types/Integer.md)
 * [➞humidity_percentage](cryoEMPreparation__humidity_percentage.md)  <sub>0..1</sub>
     * Description: Chamber humidity during vitrification
     * Range: [Float](types/Float.md)
 * [➞chamber_temperature](cryoEMPreparation__chamber_temperature.md)  <sub>0..1</sub>
     * Description: Chamber temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞grid_material](cryoEMPreparation__grid_material.md)  <sub>0..1</sub>
     * Description: Grid material
     * Range: [GridMaterialEnum](GridMaterialEnum.md)
 * [➞glow_discharge_applied](cryoEMPreparation__glow_discharge_applied.md)  <sub>0..1</sub>
     * Description: Whether glow discharge treatment was applied
     * Range: [Boolean](types/Boolean.md)
 * [➞glow_discharge_time](cryoEMPreparation__glow_discharge_time.md)  <sub>0..1</sub>
     * Description: Glow discharge time in seconds
     * Range: [Float](types/Float.md)
 * [➞glow_discharge_current](cryoEMPreparation__glow_discharge_current.md)  <sub>0..1</sub>
     * Description: Glow discharge current in milliamperes
     * Range: [Float](types/Float.md)
 * [➞glow_discharge_atmosphere](cryoEMPreparation__glow_discharge_atmosphere.md)  <sub>0..1</sub>
     * Description: Glow discharge atmosphere (air, amylamine)
     * Range: [String](types/String.md)
 * [➞glow_discharge_pressure](cryoEMPreparation__glow_discharge_pressure.md)  <sub>0..1</sub>
     * Description: Glow discharge pressure in millibar
     * Range: [Float](types/Float.md)
 * [➞vitrification_instrument](cryoEMPreparation__vitrification_instrument.md)  <sub>0..1</sub>
     * Description: Vitrification instrument used (e.g., Vitrobot)
     * Range: [String](types/String.md)
 * [➞blot_number](cryoEMPreparation__blot_number.md)  <sub>0..1</sub>
     * Description: Number of blots applied
     * Range: [Integer](types/Integer.md)
 * [➞wait_time](cryoEMPreparation__wait_time.md)  <sub>0..1</sub>
     * Description: Wait time before blotting in seconds
     * Range: [Float](types/Float.md)
 * [➞blotter_height](cryoEMPreparation__blotter_height.md)  <sub>0..1</sub>
     * Description: Blotter height setting
     * Range: [Float](types/Float.md)
 * [➞blotter_setting](cryoEMPreparation__blotter_setting.md)  <sub>0..1</sub>
     * Description: Blotter setting value
     * Range: [Float](types/Float.md)
 * [➞sample_applied_volume](cryoEMPreparation__sample_applied_volume.md)  <sub>0..1</sub>
     * Description: Volume of sample applied in microliters
     * Range: [Float](types/Float.md)
 * [➞ethane_temperature](cryoEMPreparation__ethane_temperature.md)  <sub>0..1</sub>
     * Description: Ethane temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞plasma_treatment](cryoEMPreparation__plasma_treatment.md)  <sub>0..1</sub>
     * Description: Plasma treatment details
     * Range: [String](types/String.md)

### Inherited from TechniqueSpecificPreparation:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
