
# Class: AttributeValue

The value for any attribute of an entity. This object can hold both the un-normalized atomic value and the structured value.

URI: [lambdaber:AttributeValue](https://w3id.org/lambda-ber-schema/AttributeValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TextValue],[QuantityValue],[DateTimeValue],[Attribute]<attribute%200..1-++[AttributeValue&#124;raw_value:string%20%3F],[AttributeValue]^-[TextValue],[AttributeValue]^-[QuantityValue],[AttributeValue]^-[DateTimeValue],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[TextValue],[QuantityValue],[DateTimeValue],[Attribute]<attribute%200..1-++[AttributeValue&#124;raw_value:string%20%3F],[AttributeValue]^-[TextValue],[AttributeValue]^-[QuantityValue],[AttributeValue]^-[DateTimeValue],[Attribute])

## Children

 * [DateTimeValue](DateTimeValue.md) - A date or date and time value.
 * [QuantityValue](QuantityValue.md) - A simple quantity value, representing a measurement with a numeric value and unit. This allows data providers to specify measurements in their preferred unit while enabling standardized interpretation. For example, a pixel size could be specified as 1.5 micrometers or 15 Angstroms, with the unit clearly specified.
 * [TextValue](TextValue.md) - A value described using a text string, optionally with a controlled vocabulary ID.

## Referenced by Class


## Attributes


### Own

 * [➞attribute](attributeValue__attribute.md)  <sub>0..1</sub>
     * Description: The attribute being represented.
     * Range: [Attribute](Attribute.md)
 * [➞raw_value](attributeValue__raw_value.md)  <sub>0..1</sub>
     * Description: Unnormalized atomic string representation, suggested syntax {number} {unit}
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | nmdc:AttributeValue |
