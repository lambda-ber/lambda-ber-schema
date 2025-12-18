
# Class: OntologyTerm

A term from a controlled vocabulary or ontology

URI: [lambdaber:OntologyTerm](https://w3id.org/lambda-ber-schema/OntologyTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm]<terms%200..*-++[OntologyTerm&#124;label:string%20%3F;definition:string%20%3F;ontology:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[ImageFeature]++-%20terms%200..*>[OntologyTerm],[Sample]-%20anatomy%200..1>[OntologyTerm],[Sample]-%20cell_type%200..1>[OntologyTerm],[Sample]-%20organism%200..1>[OntologyTerm],[NamedThing]^-[OntologyTerm],[Sample],[NamedThing],[ImageFeature])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyTerm]<terms%200..*-++[OntologyTerm&#124;label:string%20%3F;definition:string%20%3F;ontology:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[ImageFeature]++-%20terms%200..*>[OntologyTerm],[Sample]-%20anatomy%200..1>[OntologyTerm],[Sample]-%20cell_type%200..1>[OntologyTerm],[Sample]-%20organism%200..1>[OntologyTerm],[NamedThing]^-[OntologyTerm],[Sample],[NamedThing],[ImageFeature])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞terms](imageFeature__terms.md)*  <sub>0..\*</sub>  **[OntologyTerm](OntologyTerm.md)**
 *  **None** *[➞terms](ontologyTerm__terms.md)*  <sub>0..\*</sub>  **[OntologyTerm](OntologyTerm.md)**
 *  **None** *[➞anatomy](sample__anatomy.md)*  <sub>0..1</sub>  **[OntologyTerm](OntologyTerm.md)**
 *  **None** *[➞cell_type](sample__cell_type.md)*  <sub>0..1</sub>  **[OntologyTerm](OntologyTerm.md)**
 *  **None** *[➞organism](sample__organism.md)*  <sub>0..1</sub>  **[OntologyTerm](OntologyTerm.md)**

## Attributes


### Own

 * [➞terms](ontologyTerm__terms.md)  <sub>0..\*</sub>
     * Description: Collection of ontology terms
     * Range: [OntologyTerm](OntologyTerm.md)
 * [➞label](ontologyTerm__label.md)  <sub>0..1</sub>
     * Description: The human-readable label or name of the ontology term
     * Range: [String](types/String.md)
 * [➞definition](ontologyTerm__definition.md)  <sub>0..1</sub>
     * Description: The formal definition or meaning of the ontology term
     * Range: [String](types/String.md)
 * [➞ontology](ontologyTerm__ontology.md)  <sub>0..1</sub>
     * Description: The ontology or controlled vocabulary this term comes from (e.g., GO, SO, UBERON)
     * Range: [String](types/String.md)

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
