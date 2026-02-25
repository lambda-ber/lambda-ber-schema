

# Class: Study 


_A logical grouping of related experiments investigating a research question. In the relational model, Study is lightweight - all relationships are via association tables._





URI: [lambdaber:Study](https://w3id.org/lambda-ber-schema/Study)





```mermaid
 classDiagram
    class Study
    click Study href "../Study/"
      NamedThing <|-- Study
        click NamedThing href "../NamedThing/"
      
      Study : description
        
      Study : id
        
      Study : keywords
        
      Study : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **Study**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [keywords](keywords.md) | * <br/> [String](String.md) | Keywords or tags describing the study for search and categorization | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [studies](studies.md) | range | [Study](Study.md) |
| [StudySampleAssociation](StudySampleAssociation.md) | [study_id](study_id.md) | range | [Study](Study.md) |
| [StudyExperimentAssociation](StudyExperimentAssociation.md) | [study_id](study_id.md) | range | [Study](Study.md) |
| [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | [study_id](study_id.md) | range | [Study](Study.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:Study |
| native | lambdaber:Study |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Study
description: A logical grouping of related experiments investigating a research question.
  In the relational model, Study is lightweight - all relationships are via association
  tables.
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  keywords:
    name: keywords
    description: Keywords or tags describing the study for search and categorization
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - Dataset
    - Study
    range: string
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Study
description: A logical grouping of related experiments investigating a research question.
  In the relational model, Study is lightweight - all relationships are via association
  tables.
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  keywords:
    name: keywords
    description: Keywords or tags describing the study for search and categorization
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: keywords
    owner: Study
    domain_of:
    - Dataset
    - Study
    range: string
    multivalued: true
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: Study
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
    owner: Study
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: Study
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>