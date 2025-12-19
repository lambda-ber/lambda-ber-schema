
# Class: CryoEMPreparation

Cryo-EM specific sample preparation

URI: [lambdaber:CryoEMPreparation](https://w3id.org/lambda-ber-schema/CryoEMPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation],[QuantityValue],[QuantityValue]<ethane_temperature%200..1-++[CryoEMPreparation&#124;grid_type:GridTypeEnum%20%3F;support_film:string%20%3F;vitrification_method:VitrificationMethodEnum%20%3F;grid_material:GridMaterialEnum%20%3F;glow_discharge_applied:boolean%20%3F;glow_discharge_atmosphere:string%20%3F;vitrification_instrument:string%20%3F;plasma_treatment:string%20%3F;description(i):string%20%3F],[QuantityValue]<sample_applied_volume%200..1-++[CryoEMPreparation],[QuantityValue]<blotter_setting%200..1-++[CryoEMPreparation],[QuantityValue]<blotter_height%200..1-++[CryoEMPreparation],[QuantityValue]<wait_time%200..1-++[CryoEMPreparation],[QuantityValue]<blot_number%200..1-++[CryoEMPreparation],[QuantityValue]<glow_discharge_pressure%200..1-++[CryoEMPreparation],[QuantityValue]<glow_discharge_current%200..1-++[CryoEMPreparation],[QuantityValue]<glow_discharge_time%200..1-++[CryoEMPreparation],[QuantityValue]<chamber_temperature%200..1-++[CryoEMPreparation],[QuantityValue]<humidity_percentage%200..1-++[CryoEMPreparation],[QuantityValue]<blot_force%200..1-++[CryoEMPreparation],[QuantityValue]<blot_time%200..1-++[CryoEMPreparation],[QuantityValue]<hole_size%200..1-++[CryoEMPreparation],[TechniqueSpecificPreparation]^-[CryoEMPreparation])](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation],[QuantityValue],[QuantityValue]<ethane_temperature%200..1-++[CryoEMPreparation&#124;grid_type:GridTypeEnum%20%3F;support_film:string%20%3F;vitrification_method:VitrificationMethodEnum%20%3F;grid_material:GridMaterialEnum%20%3F;glow_discharge_applied:boolean%20%3F;glow_discharge_atmosphere:string%20%3F;vitrification_instrument:string%20%3F;plasma_treatment:string%20%3F;description(i):string%20%3F],[QuantityValue]<sample_applied_volume%200..1-++[CryoEMPreparation],[QuantityValue]<blotter_setting%200..1-++[CryoEMPreparation],[QuantityValue]<blotter_height%200..1-++[CryoEMPreparation],[QuantityValue]<wait_time%200..1-++[CryoEMPreparation],[QuantityValue]<blot_number%200..1-++[CryoEMPreparation],[QuantityValue]<glow_discharge_pressure%200..1-++[CryoEMPreparation],[QuantityValue]<glow_discharge_current%200..1-++[CryoEMPreparation],[QuantityValue]<glow_discharge_time%200..1-++[CryoEMPreparation],[QuantityValue]<chamber_temperature%200..1-++[CryoEMPreparation],[QuantityValue]<humidity_percentage%200..1-++[CryoEMPreparation],[QuantityValue]<blot_force%200..1-++[CryoEMPreparation],[QuantityValue]<blot_time%200..1-++[CryoEMPreparation],[QuantityValue]<hole_size%200..1-++[CryoEMPreparation],[TechniqueSpecificPreparation]^-[CryoEMPreparation])

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
     * Description: Hole size, typically specified in micrometers (range: 0.5-5.0). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞vitrification_method](cryoEMPreparation__vitrification_method.md)  <sub>0..1</sub>
     * Description: Method used for vitrification
     * Range: [VitrificationMethodEnum](VitrificationMethodEnum.md)
 * [➞blot_time](cryoEMPreparation__blot_time.md)  <sub>0..1</sub>
     * Description: Blotting time, typically specified in seconds (range: 0.5-10.0). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞blot_force](cryoEMPreparation__blot_force.md)  <sub>0..1</sub>
     * Description: Blotting force setting
     * Range: [QuantityValue](QuantityValue.md)
 * [➞humidity_percentage](cryoEMPreparation__humidity_percentage.md)  <sub>0..1</sub>
     * Description: Chamber humidity during vitrification (range: 0-100), typically specified as a percentage. Data providers may specify as decimal fraction by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞chamber_temperature](cryoEMPreparation__chamber_temperature.md)  <sub>0..1</sub>
     * Description: Chamber temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞grid_material](cryoEMPreparation__grid_material.md)  <sub>0..1</sub>
     * Description: Grid material
     * Range: [GridMaterialEnum](GridMaterialEnum.md)
 * [➞glow_discharge_applied](cryoEMPreparation__glow_discharge_applied.md)  <sub>0..1</sub>
     * Description: Whether glow discharge treatment was applied
     * Range: [Boolean](types/Boolean.md)
 * [➞glow_discharge_time](cryoEMPreparation__glow_discharge_time.md)  <sub>0..1</sub>
     * Description: Glow discharge time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞glow_discharge_current](cryoEMPreparation__glow_discharge_current.md)  <sub>0..1</sub>
     * Description: Glow discharge current, typically specified in milliamperes. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞glow_discharge_atmosphere](cryoEMPreparation__glow_discharge_atmosphere.md)  <sub>0..1</sub>
     * Description: Glow discharge atmosphere (air, amylamine)
     * Range: [String](types/String.md)
 * [➞glow_discharge_pressure](cryoEMPreparation__glow_discharge_pressure.md)  <sub>0..1</sub>
     * Description: Glow discharge pressure, typically specified in millibars. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞vitrification_instrument](cryoEMPreparation__vitrification_instrument.md)  <sub>0..1</sub>
     * Description: Vitrification instrument used (e.g., Vitrobot)
     * Range: [String](types/String.md)
 * [➞blot_number](cryoEMPreparation__blot_number.md)  <sub>0..1</sub>
     * Description: Number of blots applied
     * Range: [QuantityValue](QuantityValue.md)
 * [➞wait_time](cryoEMPreparation__wait_time.md)  <sub>0..1</sub>
     * Description: Wait time before blotting, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞blotter_height](cryoEMPreparation__blotter_height.md)  <sub>0..1</sub>
     * Description: Blotter height setting. Data providers may include unit information in the QuantityValue if needed.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞blotter_setting](cryoEMPreparation__blotter_setting.md)  <sub>0..1</sub>
     * Description: Blotter setting value. Data providers may include unit information in the QuantityValue if needed.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞sample_applied_volume](cryoEMPreparation__sample_applied_volume.md)  <sub>0..1</sub>
     * Description: Volume of sample applied, typically specified in microliters. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ethane_temperature](cryoEMPreparation__ethane_temperature.md)  <sub>0..1</sub>
     * Description: Ethane temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞plasma_treatment](cryoEMPreparation__plasma_treatment.md)  <sub>0..1</sub>
     * Description: Plasma treatment details
     * Range: [String](types/String.md)

### Inherited from TechniqueSpecificPreparation:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
