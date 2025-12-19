
# Class: MeasurementConditions

Conditions under which biophysical measurements were made

URI: [lambdaber:MeasurementConditions](https://w3id.org/lambda-ber-schema/MeasurementConditions)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[NamedThing],[QuantityValue]<temperature%200..1-++[MeasurementConditions&#124;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<ionic_strength%200..1-++[MeasurementConditions],[QuantityValue]<ph%200..1-++[MeasurementConditions],[BufferComposition]<buffer_composition%200..1-++[MeasurementConditions],[BiophysicalProperty]++-%20measurement_conditions%200..*>[MeasurementConditions],[NamedThing]^-[MeasurementConditions],[BufferComposition],[BiophysicalProperty])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[NamedThing],[QuantityValue]<temperature%200..1-++[MeasurementConditions&#124;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<ionic_strength%200..1-++[MeasurementConditions],[QuantityValue]<ph%200..1-++[MeasurementConditions],[BufferComposition]<buffer_composition%200..1-++[MeasurementConditions],[BiophysicalProperty]++-%20measurement_conditions%200..*>[MeasurementConditions],[NamedThing]^-[MeasurementConditions],[BufferComposition],[BiophysicalProperty])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞measurement_conditions](biophysicalProperty__measurement_conditions.md)*  <sub>0..\*</sub>  **[MeasurementConditions](MeasurementConditions.md)**

## Attributes


### Own

 * [➞buffer_composition](measurementConditions__buffer_composition.md)  <sub>0..1</sub>
     * Description: Composition of the buffer used
     * Range: [BufferComposition](BufferComposition.md)
 * [➞ph](measurementConditions__ph.md)  <sub>0..1</sub>
     * Description: pH value of the solution during measurement (range: 0-14), typically expressed in pH units. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ionic_strength](measurementConditions__ionic_strength.md)  <sub>0..1</sub>
     * Description: Ionic strength, typically specified in molar (mol/L). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞temperature](measurementConditions__temperature.md)  <sub>0..1</sub>
     * Description: Temperature during measurement, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

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
