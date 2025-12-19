
# Class: TextValue

A value described using a text string, optionally with a controlled vocabulary ID.

URI: [lambdaber:TextValue](https://w3id.org/lambda-ber-schema/TextValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AttributeValue]^-[TextValue&#124;value:string;value_cv_id:curie%20%3F;raw_value(i):string%20%3F],[AttributeValue],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[AttributeValue]^-[TextValue&#124;value:string;value_cv_id:curie%20%3F;raw_value(i):string%20%3F],[AttributeValue],[Attribute])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any attribute of an entity. This object can hold both the un-normalized atomic value and the structured value.

## Attributes


### Own

 * [➞value](textValue__value.md)  <sub>1..1</sub>
     * Description: The text value
     * Range: [String](types/String.md)
 * [➞value_cv_id](textValue__value_cv_id.md)  <sub>0..1</sub>
     * Description: For values in a controlled vocabulary, the CV ID for the value.
     * Range: [Curie](types/Curie.md)

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
| **Mappings:** | | nmdc:TextValue |
