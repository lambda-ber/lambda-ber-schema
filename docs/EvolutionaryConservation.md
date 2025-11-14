

# Class: EvolutionaryConservation 


_Evolutionary conservation information_





URI: [lambdaber:EvolutionaryConservation](https://w3id.org/lambda-ber-schema/EvolutionaryConservation)





```mermaid
 classDiagram
    class EvolutionaryConservation
    click EvolutionaryConservation href "../EvolutionaryConservation/"
      ProteinAnnotation <|-- EvolutionaryConservation
        click ProteinAnnotation href "../ProteinAnnotation/"
      
      EvolutionaryConservation : alignment_depth
        
      EvolutionaryConservation : annotation_method
        
      EvolutionaryConservation : chain_id
        
      EvolutionaryConservation : coevolved_residues
        
      EvolutionaryConservation : confidence_score
        
      EvolutionaryConservation : conservation_method
        
      EvolutionaryConservation : conservation_score
        
      EvolutionaryConservation : conserved_residues
        
      EvolutionaryConservation : description
        
      EvolutionaryConservation : evidence_code
        
      EvolutionaryConservation : evidence_type
        
          
    
        
        
        EvolutionaryConservation --> "0..1" EvidenceTypeEnum : evidence_type
        click EvidenceTypeEnum href "../EvidenceTypeEnum/"
    

        
      EvolutionaryConservation : id
        
      EvolutionaryConservation : pdb_entry
        
      EvolutionaryConservation : protein_id
        
      EvolutionaryConservation : publication_ids
        
      EvolutionaryConservation : residue_range
        
      EvolutionaryConservation : source_database
        
          
    
        
        
        EvolutionaryConservation --> "0..1" AnnotationSourceEnum : source_database
        click AnnotationSourceEnum href "../AnnotationSourceEnum/"
    

        
      EvolutionaryConservation : taxonomic_range
        
      EvolutionaryConservation : title
        
      EvolutionaryConservation : variable_residues
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [ProteinAnnotation](ProteinAnnotation.md)
        * **EvolutionaryConservation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [conservation_score](conservation_score.md) | 0..1 <br/> [Float](Float.md) | Overall conservation score | direct |
| [conserved_residues](conserved_residues.md) | * <br/> [String](String.md) | Highly conserved residues | direct |
| [variable_residues](variable_residues.md) | * <br/> [String](String.md) | Highly variable residues | direct |
| [conservation_method](conservation_method.md) | 0..1 <br/> [String](String.md) | Method used for conservation analysis | direct |
| [alignment_depth](alignment_depth.md) | 0..1 <br/> [Integer](Integer.md) | Number of sequences in alignment | direct |
| [taxonomic_range](taxonomic_range.md) | 0..1 <br/> [String](String.md) | Taxonomic range of conservation | direct |
| [coevolved_residues](coevolved_residues.md) | * <br/> [String](String.md) | Pairs of coevolved residues | direct |
| [protein_id](protein_id.md) | 1 <br/> [String](String.md) | UniProt accession number | [ProteinAnnotation](ProteinAnnotation.md) |
| [pdb_entry](pdb_entry.md) | 0..1 <br/> [String](String.md) | PDB identifier | [ProteinAnnotation](ProteinAnnotation.md) |
| [chain_id](chain_id.md) | 0..1 <br/> [String](String.md) | Chain identifier in the PDB structure | [ProteinAnnotation](ProteinAnnotation.md) |
| [residue_range](residue_range.md) | 0..1 <br/> [String](String.md) | Range of residues (e | [ProteinAnnotation](ProteinAnnotation.md) |
| [confidence_score](confidence_score.md) | 0..1 <br/> [Float](Float.md) | Confidence score for the annotation (0-1) | [ProteinAnnotation](ProteinAnnotation.md) |
| [evidence_type](evidence_type.md) | 0..1 <br/> [EvidenceTypeEnum](EvidenceTypeEnum.md) | Type of evidence supporting this annotation | [ProteinAnnotation](ProteinAnnotation.md) |
| [evidence_code](evidence_code.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Evidence and Conclusion Ontology (ECO) code | [ProteinAnnotation](ProteinAnnotation.md) |
| [source_database](source_database.md) | 0..1 <br/> [AnnotationSourceEnum](AnnotationSourceEnum.md) | Source database or resource that provided this annotation | [ProteinAnnotation](ProteinAnnotation.md) |
| [annotation_method](annotation_method.md) | 0..1 <br/> [String](String.md) | Computational or experimental method used | [ProteinAnnotation](ProteinAnnotation.md) |
| [publication_ids](publication_ids.md) | * <br/> [String](String.md) | IDs of one or more publications supporting this annotation | [ProteinAnnotation](ProteinAnnotation.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Sample](Sample.md) | [evolutionary_conservation](evolutionary_conservation.md) | range | [EvolutionaryConservation](EvolutionaryConservation.md) |
| [AggregatedProteinView](AggregatedProteinView.md) | [evolutionary_conservation](evolutionary_conservation.md) | range | [EvolutionaryConservation](EvolutionaryConservation.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:EvolutionaryConservation |
| native | lambdaber:EvolutionaryConservation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EvolutionaryConservation
description: Evolutionary conservation information
from_schema: https://w3id.org/lambda-ber-schema/
is_a: ProteinAnnotation
attributes:
  conservation_score:
    name: conservation_score
    description: Overall conservation score
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    domain_of:
    - FunctionalSite
    - EvolutionaryConservation
    range: float
    minimum_value: 0
    maximum_value: 1
  conserved_residues:
    name: conserved_residues
    description: Highly conserved residues
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - EvolutionaryConservation
    multivalued: true
  variable_residues:
    name: variable_residues
    description: Highly variable residues
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - EvolutionaryConservation
    multivalued: true
  conservation_method:
    name: conservation_method
    description: Method used for conservation analysis
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - EvolutionaryConservation
  alignment_depth:
    name: alignment_depth
    description: Number of sequences in alignment
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - EvolutionaryConservation
    range: integer
  taxonomic_range:
    name: taxonomic_range
    description: Taxonomic range of conservation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - EvolutionaryConservation
  coevolved_residues:
    name: coevolved_residues
    description: Pairs of coevolved residues
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    domain_of:
    - EvolutionaryConservation
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: EvolutionaryConservation
description: Evolutionary conservation information
from_schema: https://w3id.org/lambda-ber-schema/
is_a: ProteinAnnotation
attributes:
  conservation_score:
    name: conservation_score
    description: Overall conservation score
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    alias: conservation_score
    owner: EvolutionaryConservation
    domain_of:
    - FunctionalSite
    - EvolutionaryConservation
    range: float
    minimum_value: 0
    maximum_value: 1
  conserved_residues:
    name: conserved_residues
    description: Highly conserved residues
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: conserved_residues
    owner: EvolutionaryConservation
    domain_of:
    - EvolutionaryConservation
    range: string
    multivalued: true
  variable_residues:
    name: variable_residues
    description: Highly variable residues
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: variable_residues
    owner: EvolutionaryConservation
    domain_of:
    - EvolutionaryConservation
    range: string
    multivalued: true
  conservation_method:
    name: conservation_method
    description: Method used for conservation analysis
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: conservation_method
    owner: EvolutionaryConservation
    domain_of:
    - EvolutionaryConservation
    range: string
  alignment_depth:
    name: alignment_depth
    description: Number of sequences in alignment
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: alignment_depth
    owner: EvolutionaryConservation
    domain_of:
    - EvolutionaryConservation
    range: integer
  taxonomic_range:
    name: taxonomic_range
    description: Taxonomic range of conservation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: taxonomic_range
    owner: EvolutionaryConservation
    domain_of:
    - EvolutionaryConservation
    range: string
  coevolved_residues:
    name: coevolved_residues
    description: Pairs of coevolved residues
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: coevolved_residues
    owner: EvolutionaryConservation
    domain_of:
    - EvolutionaryConservation
    range: string
    multivalued: true
  protein_id:
    name: protein_id
    description: UniProt accession number
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: protein_id
    owner: EvolutionaryConservation
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
    owner: EvolutionaryConservation
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
    owner: EvolutionaryConservation
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
    owner: EvolutionaryConservation
    domain_of:
    - ProteinAnnotation
    range: string
    pattern: ^[0-9,\-]+$
  confidence_score:
    name: confidence_score
    description: Confidence score for the annotation (0-1)
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: confidence_score
    owner: EvolutionaryConservation
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
    owner: EvolutionaryConservation
    domain_of:
    - ProteinAnnotation
    range: EvidenceTypeEnum
  evidence_code:
    name: evidence_code
    description: Evidence and Conclusion Ontology (ECO) code
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: evidence_code
    owner: EvolutionaryConservation
    domain_of:
    - ProteinAnnotation
    range: uriorcurie
  source_database:
    name: source_database
    description: Source database or resource that provided this annotation
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: source_database
    owner: EvolutionaryConservation
    domain_of:
    - ProteinAnnotation
    range: AnnotationSourceEnum
  annotation_method:
    name: annotation_method
    description: Computational or experimental method used
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: annotation_method
    owner: EvolutionaryConservation
    domain_of:
    - ProteinAnnotation
    range: string
  publication_ids:
    name: publication_ids
    description: IDs of one or more publications supporting this annotation. Use PubMed
      IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
    from_schema: https://w3id.org/lambda-ber-schema/functional_annotation
    rank: 1000
    alias: publication_ids
    owner: EvolutionaryConservation
    domain_of:
    - ProteinAnnotation
    range: string
    multivalued: true
    pattern: ^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: EvolutionaryConservation
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
    owner: EvolutionaryConservation
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: EvolutionaryConservation
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>