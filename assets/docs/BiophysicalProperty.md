
# Class: BiophysicalProperty

Measured or calculated biophysical properties

URI: [lambdaber:BiophysicalProperty](https://w3id.org/lambda-ber-schema/BiophysicalProperty)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MeasurementConditions],[MeasurementConditions]<measurement_conditions%200..*-++[BiophysicalProperty&#124;property_type:BiophysicalPropertyEnum;value:float;unit:string;error:float%20%3F;experimental_method:BiophysicalMethodEnum%20%3F;description(i):string%20%3F],[AggregatedProteinView]++-%20biophysical_properties%200..*>[BiophysicalProperty],[Sample]++-%20biophysical_properties%200..*>[BiophysicalProperty],[AttributeGroup]^-[BiophysicalProperty],[Sample],[AttributeGroup],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[MeasurementConditions],[MeasurementConditions]<measurement_conditions%200..*-++[BiophysicalProperty&#124;property_type:BiophysicalPropertyEnum;value:float;unit:string;error:float%20%3F;experimental_method:BiophysicalMethodEnum%20%3F;description(i):string%20%3F],[AggregatedProteinView]++-%20biophysical_properties%200..*>[BiophysicalProperty],[Sample]++-%20biophysical_properties%200..*>[BiophysicalProperty],[AttributeGroup]^-[BiophysicalProperty],[Sample],[AttributeGroup],[AggregatedProteinView])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞biophysical_properties](aggregatedProteinView__biophysical_properties.md)*  <sub>0..\*</sub>  **[BiophysicalProperty](BiophysicalProperty.md)**
 *  **None** *[➞biophysical_properties](sample__biophysical_properties.md)*  <sub>0..\*</sub>  **[BiophysicalProperty](BiophysicalProperty.md)**

## Attributes


### Own

 * [➞property_type](biophysicalProperty__property_type.md)  <sub>1..1</sub>
     * Description: Type of biophysical property
     * Range: [BiophysicalPropertyEnum](BiophysicalPropertyEnum.md)
 * [➞value](biophysicalProperty__value.md)  <sub>1..1</sub>
     * Description: Numerical value of the property
     * Range: [Float](types/Float.md)
 * [➞unit](biophysicalProperty__unit.md)  <sub>1..1</sub>
     * Description: Unit of measurement
     * Range: [String](types/String.md)
 * [➞error](biophysicalProperty__error.md)  <sub>0..1</sub>
     * Description: Experimental error or uncertainty
     * Range: [Float](types/Float.md)
 * [➞measurement_conditions](biophysicalProperty__measurement_conditions.md)  <sub>0..\*</sub>
     * Description: Conditions under which measurement was made. If multiple sets of conditions were used, this will represent that the same values were obtained under different conditions. If values differ under different conditions, separate BiophysicalProperty instances should be created.
     * Range: [MeasurementConditions](MeasurementConditions.md)
 * [➞experimental_method](biophysicalProperty__experimental_method.md)  <sub>0..1</sub>
     * Description: Method used for measurement
     * Range: [BiophysicalMethodEnum](BiophysicalMethodEnum.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
