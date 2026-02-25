

# Class: OntologyTerm 


_A term from a controlled vocabulary or ontology_





URI: [lambdaber:OntologyTerm](https://w3id.org/lambda-ber-schema/OntologyTerm)





```mermaid
 classDiagram
    class OntologyTerm
    click OntologyTerm href "../OntologyTerm/"
      NamedThing <|-- OntologyTerm
        click NamedThing href "../NamedThing/"
      
      OntologyTerm : definition
        
      OntologyTerm : description
        
      OntologyTerm : id
        
      OntologyTerm : label
        
      OntologyTerm : ontology
        
      OntologyTerm : terms
        
          
    
        
        
        OntologyTerm --> "*" OntologyTerm : terms
        click OntologyTerm href "../OntologyTerm/"
    

        
      OntologyTerm : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **OntologyTerm**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [terms](terms.md) | * <br/> [OntologyTerm](OntologyTerm.md) | Collection of ontology terms | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | The human-readable label or name of the ontology term | direct |
| [definition](definition.md) | 0..1 <br/> [String](String.md) | The formal definition or meaning of the ontology term | direct |
| [ontology](ontology.md) | 0..1 <br/> [String](String.md) | The ontology or controlled vocabulary this term comes from (e | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Sample](Sample.md) | [organism](organism.md) | range | [OntologyTerm](OntologyTerm.md) |
| [Sample](Sample.md) | [anatomy](anatomy.md) | range | [OntologyTerm](OntologyTerm.md) |
| [Sample](Sample.md) | [cell_type](cell_type.md) | range | [OntologyTerm](OntologyTerm.md) |
| [ImageFeature](ImageFeature.md) | [terms](terms.md) | range | [OntologyTerm](OntologyTerm.md) |
| [OntologyTerm](OntologyTerm.md) | [terms](terms.md) | range | [OntologyTerm](OntologyTerm.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:OntologyTerm |
| native | lambdaber:OntologyTerm |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OntologyTerm
description: A term from a controlled vocabulary or ontology
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  terms:
    name: terms
    description: Collection of ontology terms
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - ImageFeature
    - OntologyTerm
    range: OntologyTerm
    multivalued: true
    inlined: true
    inlined_as_list: true
  label:
    name: label
    description: The human-readable label or name of the ontology term
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - OntologyTerm
    - Attribute
    range: string
  definition:
    name: definition
    description: The formal definition or meaning of the ontology term
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - OntologyTerm
    range: string
  ontology:
    name: ontology
    description: The ontology or controlled vocabulary this term comes from (e.g.,
      GO, SO, UBERON)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - OntologyTerm
    range: string

```
</details>

### Induced

<details>
```yaml
name: OntologyTerm
description: A term from a controlled vocabulary or ontology
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  terms:
    name: terms
    description: Collection of ontology terms
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: terms
    owner: OntologyTerm
    domain_of:
    - ImageFeature
    - OntologyTerm
    range: OntologyTerm
    multivalued: true
    inlined: true
    inlined_as_list: true
  label:
    name: label
    description: The human-readable label or name of the ontology term
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: label
    owner: OntologyTerm
    domain_of:
    - OntologyTerm
    - Attribute
    range: string
  definition:
    name: definition
    description: The formal definition or meaning of the ontology term
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: definition
    owner: OntologyTerm
    domain_of:
    - OntologyTerm
    range: string
  ontology:
    name: ontology
    description: The ontology or controlled vocabulary this term comes from (e.g.,
      GO, SO, UBERON)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: ontology
    owner: OntologyTerm
    domain_of:
    - OntologyTerm
    range: string
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: OntologyTerm
    domain_of:
    - NamedThing
    - Attribute
    range: uriorcurie
    required: true
  title:
    name: title
    description: A human-readable name or title for this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: OntologyTerm
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: OntologyTerm
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>