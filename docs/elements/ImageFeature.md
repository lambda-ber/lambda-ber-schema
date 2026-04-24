

# Class: ImageFeature 


_Semantic annotations describing features identified in images using controlled vocabulary terms_





URI: [lambda:ImageFeature](http://w3id.org/lambda/ImageFeature)





```mermaid
 classDiagram
    class ImageFeature
    click ImageFeature href "../ImageFeature/"
      AttributeGroup <|-- ImageFeature
        click AttributeGroup href "../AttributeGroup/"
      
      ImageFeature : description
        
      ImageFeature : terms
        
          
    
        
        
        ImageFeature --> "*" OntologyTerm : terms
        click OntologyTerm href "../OntologyTerm/"
    

        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * **ImageFeature**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [terms](terms.md) | * <br/> [OntologyTerm](OntologyTerm.md) | Ontology terms describing features identified in the image | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:ImageFeature |
| native | lambda:ImageFeature |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ImageFeature
description: Semantic annotations describing features identified in images using controlled
  vocabulary terms
from_schema: http://w3id.org/lambda/
is_a: AttributeGroup
attributes:
  terms:
    name: terms
    description: Ontology terms describing features identified in the image
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - ImageFeature
    - OntologyTerm
    range: OntologyTerm
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: ImageFeature
description: Semantic annotations describing features identified in images using controlled
  vocabulary terms
from_schema: http://w3id.org/lambda/
is_a: AttributeGroup
attributes:
  terms:
    name: terms
    description: Ontology terms describing features identified in the image
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: terms
    owner: ImageFeature
    domain_of:
    - ImageFeature
    - OntologyTerm
    range: OntologyTerm
    multivalued: true
    inlined: true
    inlined_as_list: true
  description:
    name: description
    from_schema: http://w3id.org/lambda/
    alias: description
    owner: ImageFeature
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>