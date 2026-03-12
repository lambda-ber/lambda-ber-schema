
# Class: Attribute

A domain, measurement, attribute, property, or any descriptor for additional properties to be added to an entity. Where available, please use OBO Foundry ontologies or other controlled vocabularies for attributes; the label should be the term name from the ontology and the id should be the fully-qualified CURIE.

URI: [lambdaber:Attribute](https://w3id.org/lambda-ber-schema/Attribute)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AttributeValue]++-%20attribute%200..1>[Attribute&#124;id:string%20%3F;label:string],[AttributeValue])](https://yuml.me/diagram/nofunky;dir:TB/class/[AttributeValue]++-%20attribute%200..1>[Attribute&#124;id:string%20%3F;label:string],[AttributeValue])

## Referenced by Class

 *  **None** *[attribute](attribute.md)*  <sub>1..1</sub>  **[Attribute](Attribute.md)**
 *  **None** *[➞attribute](attributeValue__attribute.md)*  <sub>0..1</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [➞id](attribute__id.md)  <sub>0..1</sub>
     * Description: A CURIE for the attribute, should one exist. Where available, please use OBO Foundry ontologies or other controlled vocabularies for labelling attributes; the id should be the term ID from the ontology.
     * Range: [String](types/String.md)
 * [➞label](attribute__label.md)  <sub>1..1</sub>
     * Description: Text string to describe the attribute. Where available, please use OBO Foundry ontologies or other controlled vocabularies for labelling attributes; the label should be the term name from the ontology.
     * Range: [String](types/String.md)
