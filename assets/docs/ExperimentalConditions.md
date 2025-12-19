
# Class: ExperimentalConditions

Environmental and experimental conditions

URI: [lambdaber:ExperimentalConditions](https://w3id.org/lambda-ber-schema/ExperimentalConditions)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<exposure_time%200..1-++[ExperimentalConditions&#124;atmosphere:string%20%3F;description(i):string%20%3F],[QuantityValue]<beam_energy%200..1-++[ExperimentalConditions],[QuantityValue]<pressure%200..1-++[ExperimentalConditions],[QuantityValue]<humidity%200..1-++[ExperimentalConditions],[QuantityValue]<temperature%200..1-++[ExperimentalConditions],[ExperimentRun]++-%20experimental_conditions%200..1>[ExperimentalConditions],[AttributeGroup]^-[ExperimentalConditions],[ExperimentRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<exposure_time%200..1-++[ExperimentalConditions&#124;atmosphere:string%20%3F;description(i):string%20%3F],[QuantityValue]<beam_energy%200..1-++[ExperimentalConditions],[QuantityValue]<pressure%200..1-++[ExperimentalConditions],[QuantityValue]<humidity%200..1-++[ExperimentalConditions],[QuantityValue]<temperature%200..1-++[ExperimentalConditions],[ExperimentRun]++-%20experimental_conditions%200..1>[ExperimentalConditions],[AttributeGroup]^-[ExperimentalConditions],[ExperimentRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞experimental_conditions](experimentRun__experimental_conditions.md)*  <sub>0..1</sub>  **[ExperimentalConditions](ExperimentalConditions.md)**

## Attributes


### Own

 * [➞temperature](experimentalConditions__temperature.md)  <sub>0..1</sub>
     * Description: Temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞humidity](experimentalConditions__humidity.md)  <sub>0..1</sub>
     * Description: Humidity, typically specified as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞pressure](experimentalConditions__pressure.md)  <sub>0..1</sub>
     * Description: Pressure, typically specified in kilopascals (kPa). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞atmosphere](experimentalConditions__atmosphere.md)  <sub>0..1</sub>
     * Description: Atmosphere composition
     * Range: [String](types/String.md)
 * [➞beam_energy](experimentalConditions__beam_energy.md)  <sub>0..1</sub>
     * Description: Beam energy, typically specified in kiloelectronvolts (keV). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞exposure_time](experimentalConditions__exposure_time.md)  <sub>0..1</sub>
     * Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
