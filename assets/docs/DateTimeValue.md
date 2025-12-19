
# Class: DateTimeValue

A date or date and time value.

URI: [lambdaber:DateTimeValue](https://w3id.org/lambda-ber-schema/DateTimeValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AttributeValue]^-[DateTimeValue&#124;value:string;raw_value(i):string%20%3F],[AttributeValue],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[AttributeValue]^-[DateTimeValue&#124;value:string;raw_value(i):string%20%3F],[AttributeValue],[Attribute])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any attribute of an entity. This object can hold both the un-normalized atomic value and the structured value.

## Attributes


### Own

 * [➞value](dateTimeValue__value.md)  <sub>1..1</sub>
     * Description: The date or date/time value, expressed in ISO 8601-compatible form. Dates should be expressed as YYYY-MM-DD; times should be expressed as HH:MM:SS with optional milliseconds and an indication of the timezone.
     * Range: [String](types/String.md)
     * Example: 2025-11-09 None
     * Example: 2025-09-16T22:48:54Z None

### Inherited from AttributeValue:

 * [➞attribute](attributeValue__attribute.md)  <sub>0..1</sub>
     * Description: The attribute being represented.
     * Range: [Attribute](Attribute.md)
 * [➞raw_value](attributeValue__raw_value.md)  <sub>0..1</sub>
     * Description: Unnormalized atomic string representation, suggested syntax {number} {unit}
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | nmdc:DateTimeValue |
