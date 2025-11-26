
# Class: ImageFeature

Semantic annotations describing features identified in images using controlled vocabulary terms

URI: [lambdaber:ImageFeature](https://w3id.org/lambda-ber-schema/ImageFeature)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[OntologyTerm]<terms%200..*-++[ImageFeature&#124;description(i):string%20%3F],[AttributeGroup]^-[ImageFeature],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm],[OntologyTerm]<terms%200..*-++[ImageFeature&#124;description(i):string%20%3F],[AttributeGroup]^-[ImageFeature],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Attributes


### Own

 * [➞terms](imageFeature__terms.md)  <sub>0..\*</sub>
     * Description: Ontology terms describing features identified in the image
     * Range: [OntologyTerm](OntologyTerm.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
