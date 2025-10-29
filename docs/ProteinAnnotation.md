

# Class: ProteinAnnotation 


_Base class for all protein-related functional and structural annotations_





URI: [lambdaber:ProteinAnnotation](https://w3id.org/lambda-ber-schema/ProteinAnnotation)





```mermaid
 classDiagram
    class ProteinAnnotation
    click ProteinAnnotation href "../ProteinAnnotation/"
      NamedThing <|-- ProteinAnnotation
        click NamedThing href "../NamedThing/"
      

      ProteinAnnotation <|-- FunctionalSite
        click FunctionalSite href "../FunctionalSite/"
      ProteinAnnotation <|-- StructuralFeature
        click StructuralFeature href "../StructuralFeature/"
      ProteinAnnotation <|-- ProteinProteinInteraction
        click ProteinProteinInteraction href "../ProteinProteinInteraction/"
      ProteinAnnotation <|-- MutationEffect
        click MutationEffect href "../MutationEffect/"
      ProteinAnnotation <|-- PostTranslationalModification
        click PostTranslationalModification href "../PostTranslationalModification/"
      ProteinAnnotation <|-- EvolutionaryConservation
        click EvolutionaryConservation href "../EvolutionaryConservation/"
      

      ProteinAnnotation : annotation_method
        
      ProteinAnnotation : chain_id
        
      ProteinAnnotation : confidence_score
        
      ProteinAnnotation : description
        
      ProteinAnnotation : evidence_code
        
      ProteinAnnotation : evidence_type
        
          
    
        
        
        ProteinAnnotation --> "0..1" EvidenceTypeEnum : evidence_type
        click EvidenceTypeEnum href "../EvidenceTypeEnum/"
    

        
      ProteinAnnotation : id
        
      ProteinAnnotation : pdb_entry
        
      ProteinAnnotation : protein_id
        
      ProteinAnnotation : publication_ids
        
      ProteinAnnotation : residue_range
        
      ProteinAnnotation : source_database
        
          
    
        
        
        ProteinAnnotation --> "0..1" AnnotationSourceEnum : source_database
        click AnnotationSourceEnum href "../AnnotationSourceEnum/"
    

        
      ProteinAnnotation : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **ProteinAnnotation**
        * [FunctionalSite](FunctionalSite.md)
        * [StructuralFeature](StructuralFeature.md)
        * [ProteinProteinInteraction](ProteinProteinInteraction.md)
        * [MutationEffect](MutationEffect.md)
        * [PostTranslationalModification](PostTranslationalModification.md)
        * [EvolutionaryConservation](EvolutionaryConservation.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [protein_id](protein_id.md) | 1 <br/> [String](String.md) | UniProt accession number | direct |
| [pdb_entry](pdb_entry.md) | 0..1 <br/> [String](String.md) | PDB identifier | direct |
| [chain_id](chain_id.md) | 0..1 <br/> [String](String.md) | Chain identifier in the PDB structure | direct |
| [residue_range](residue_range.md) | 0..1 <br/> [String](String.md) | Range of residues (e | direct |
| [confidence_score](confidence_score.md) | 0..1 <br/> [Float](Float.md) | Confidence score for the annotation (0-1) | direct |
| [evidence_type](evidence_type.md) | 0..1 <br/> [EvidenceTypeEnum](EvidenceTypeEnum.md) | Type of evidence supporting this annotation | direct |
| [evidence_code](evidence_code.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Evidence and Conclusion Ontology (ECO) code | direct |
| [source_database](source_database.md) | 0..1 <br/> [AnnotationSourceEnum](AnnotationSourceEnum.md) | Source database or resource that provided this annotation | direct |
| [annotation_method](annotation_method.md) | 0..1 <br/> [String](String.md) | Computational or experimental method used | direct |
| [publication_ids](publication_ids.md) | * <br/> [String](String.md) | PubMed IDs supporting this annotation | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:ProteinAnnotation |
| native | lambdaber:ProteinAnnotation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProteinAnnotation
description: Base class for all protein-related functional and structural annotations
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  protein_id:
    name: protein_id
    description: UniProt accession number
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
    - ConformationalEnsemble
    required: true
    pattern: ^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$
  pdb_entry:
    name: pdb_entry
    description: PDB identifier
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
    pattern: ^[0-9][A-Za-z0-9]{3}$
  chain_id:
    name: chain_id
    description: Chain identifier in the PDB structure
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
    pattern: ^[A-Za-z0-9]+$
  residue_range:
    name: residue_range
    description: Range of residues (e.g., '1-100', '25,27,30-35')
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
  confidence_score:
    name: confidence_score
    description: Confidence score for the annotation (0-1)
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
    range: float
    minimum_value: 0
    maximum_value: 1
  evidence_type:
    name: evidence_type
    description: Type of evidence supporting this annotation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
    range: EvidenceTypeEnum
  evidence_code:
    name: evidence_code
    description: Evidence and Conclusion Ontology (ECO) code
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
    range: uriorcurie
  source_database:
    name: source_database
    description: Source database or resource that provided this annotation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
    range: AnnotationSourceEnum
  annotation_method:
    name: annotation_method
    description: Computational or experimental method used
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
  publication_ids:
    name: publication_ids
    description: PubMed IDs supporting this annotation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - ProteinAnnotation
    multivalued: true
    pattern: ^PMID:[0-9]+$

```
</details>

### Induced

<details>
```yaml
name: ProteinAnnotation
description: Base class for all protein-related functional and structural annotations
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  protein_id:
    name: protein_id
    description: UniProt accession number
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: protein_id
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    - ConformationalEnsemble
    range: string
    required: true
    pattern: ^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$
  pdb_entry:
    name: pdb_entry
    description: PDB identifier
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: pdb_entry
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: string
    pattern: ^[0-9][A-Za-z0-9]{3}$
  chain_id:
    name: chain_id
    description: Chain identifier in the PDB structure
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: chain_id
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: string
    pattern: ^[A-Za-z0-9]+$
  residue_range:
    name: residue_range
    description: Range of residues (e.g., '1-100', '25,27,30-35')
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: residue_range
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: string
  confidence_score:
    name: confidence_score
    description: Confidence score for the annotation (0-1)
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: confidence_score
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: float
    minimum_value: 0
    maximum_value: 1
  evidence_type:
    name: evidence_type
    description: Type of evidence supporting this annotation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: evidence_type
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: EvidenceTypeEnum
  evidence_code:
    name: evidence_code
    description: Evidence and Conclusion Ontology (ECO) code
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: evidence_code
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: uriorcurie
  source_database:
    name: source_database
    description: Source database or resource that provided this annotation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: source_database
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: AnnotationSourceEnum
  annotation_method:
    name: annotation_method
    description: Computational or experimental method used
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: annotation_method
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: string
  publication_ids:
    name: publication_ids
    description: PubMed IDs supporting this annotation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: publication_ids
    owner: ProteinAnnotation
    domain_of:
    - ProteinAnnotation
    range: string
    multivalued: true
    pattern: ^PMID:[0-9]+$
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: ProteinAnnotation
    domain_of:
    - NamedThing
    range: uriorcurie
    required: true
  title:
    name: title
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: ProteinAnnotation
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: ProteinAnnotation
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>