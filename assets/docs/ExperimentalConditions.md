
# Class: ExperimentalConditions

Environmental and experimental conditions

URI: [lambdaber:ExperimentalConditions](https://w3id.org/lambda-ber-schema/ExperimentalConditions)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<exposure_time%200..1-++[ExperimentalConditions&#124;temperature:float%20%3F;humidity:float%20%3F;pressure:float%20%3F;atmosphere:string%20%3F;beam_energy:float%20%3F;description(i):string%20%3F],[ExperimentRun]++-%20experimental_conditions%200..1>[ExperimentalConditions],[AttributeGroup]^-[ExperimentalConditions],[ExperimentRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<exposure_time%200..1-++[ExperimentalConditions&#124;temperature:float%20%3F;humidity:float%20%3F;pressure:float%20%3F;atmosphere:string%20%3F;beam_energy:float%20%3F;description(i):string%20%3F],[ExperimentRun]++-%20experimental_conditions%200..1>[ExperimentalConditions],[AttributeGroup]^-[ExperimentalConditions],[ExperimentRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞experimental_conditions](experimentRun__experimental_conditions.md)*  <sub>0..1</sub>  **[ExperimentalConditions](ExperimentalConditions.md)**

## Attributes


### Own

 * [➞temperature](experimentalConditions__temperature.md)  <sub>0..1</sub>
     * Description: Temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞humidity](experimentalConditions__humidity.md)  <sub>0..1</sub>
     * Description: Humidity percentage
     * Range: [Float](types/Float.md)
 * [➞pressure](experimentalConditions__pressure.md)  <sub>0..1</sub>
     * Description: Pressure in kPa
     * Range: [Float](types/Float.md)
 * [➞atmosphere](experimentalConditions__atmosphere.md)  <sub>0..1</sub>
     * Description: Atmosphere composition
     * Range: [String](types/String.md)
 * [➞beam_energy](experimentalConditions__beam_energy.md)  <sub>0..1</sub>
     * Description: Beam energy in keV
     * Range: [Float](types/Float.md)
 * [➞exposure_time](experimentalConditions__exposure_time.md)  <sub>0..1</sub>
     * Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
