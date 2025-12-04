
# Class: ProteinAnnotation

Base class for all protein-related functional and structural annotations

URI: [lambdaber:ProteinAnnotation](https://w3id.org/lambda-ber-schema/ProteinAnnotation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StructuralFeature],[ProteinProteinInteraction],[ProteinAnnotation&#124;protein_id:string;pdb_entry:string%20%3F;chain_id:string%20%3F;residue_range:string%20%3F;confidence_score:float%20%3F;evidence_type:EvidenceTypeEnum%20%3F;evidence_code:uriorcurie%20%3F;source_database:AnnotationSourceEnum%20%3F;annotation_method:string%20%3F;publication_ids:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F]^-[StructuralFeature],[ProteinAnnotation]^-[ProteinProteinInteraction],[ProteinAnnotation]^-[PostTranslationalModification],[ProteinAnnotation]^-[MutationEffect],[ProteinAnnotation]^-[FunctionalSite],[ProteinAnnotation]^-[EvolutionaryConservation],[NamedThing]^-[ProteinAnnotation],[PostTranslationalModification],[NamedThing],[MutationEffect],[FunctionalSite],[EvolutionaryConservation])](https://yuml.me/diagram/nofunky;dir:TB/class/[StructuralFeature],[ProteinProteinInteraction],[ProteinAnnotation&#124;protein_id:string;pdb_entry:string%20%3F;chain_id:string%20%3F;residue_range:string%20%3F;confidence_score:float%20%3F;evidence_type:EvidenceTypeEnum%20%3F;evidence_code:uriorcurie%20%3F;source_database:AnnotationSourceEnum%20%3F;annotation_method:string%20%3F;publication_ids:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F]^-[StructuralFeature],[ProteinAnnotation]^-[ProteinProteinInteraction],[ProteinAnnotation]^-[PostTranslationalModification],[ProteinAnnotation]^-[MutationEffect],[ProteinAnnotation]^-[FunctionalSite],[ProteinAnnotation]^-[EvolutionaryConservation],[NamedThing]^-[ProteinAnnotation],[PostTranslationalModification],[NamedThing],[MutationEffect],[FunctionalSite],[EvolutionaryConservation])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Children

 * [EvolutionaryConservation](EvolutionaryConservation.md) - Evolutionary conservation information
 * [FunctionalSite](FunctionalSite.md) - Functional sites including catalytic, binding, and regulatory sites
 * [MutationEffect](MutationEffect.md) - Effects of mutations and variants on protein structure and function
 * [PostTranslationalModification](PostTranslationalModification.md) - Post-translational modifications observed or predicted
 * [ProteinProteinInteraction](ProteinProteinInteraction.md) - Protein-protein interactions and interfaces
 * [StructuralFeature](StructuralFeature.md) - Structural features and properties of protein regions

## Referenced by Class


## Attributes


### Own

 * [➞protein_id](proteinAnnotation__protein_id.md)  <sub>1..1</sub>
     * Description: UniProt accession number
     * Range: [String](types/String.md)
 * [➞pdb_entry](proteinAnnotation__pdb_entry.md)  <sub>0..1</sub>
     * Description: PDB identifier
     * Range: [String](types/String.md)
 * [➞chain_id](proteinAnnotation__chain_id.md)  <sub>0..1</sub>
     * Description: Chain identifier in the PDB structure
     * Range: [String](types/String.md)
 * [➞residue_range](proteinAnnotation__residue_range.md)  <sub>0..1</sub>
     * Description: Range of residues (e.g., '1-100', '25,27,30-35')
     * Range: [String](types/String.md)
 * [➞confidence_score](proteinAnnotation__confidence_score.md)  <sub>0..1</sub>
     * Description: Confidence score for the annotation (0-1)
     * Range: [Float](types/Float.md)
 * [➞evidence_type](proteinAnnotation__evidence_type.md)  <sub>0..1</sub>
     * Description: Type of evidence supporting this annotation
     * Range: [EvidenceTypeEnum](EvidenceTypeEnum.md)
 * [➞evidence_code](proteinAnnotation__evidence_code.md)  <sub>0..1</sub>
     * Description: Evidence and Conclusion Ontology (ECO) code
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞source_database](proteinAnnotation__source_database.md)  <sub>0..1</sub>
     * Description: Source database or resource that provided this annotation
     * Range: [AnnotationSourceEnum](AnnotationSourceEnum.md)
 * [➞annotation_method](proteinAnnotation__annotation_method.md)  <sub>0..1</sub>
     * Description: Computational or experimental method used
     * Range: [String](types/String.md)
 * [➞publication_ids](proteinAnnotation__publication_ids.md)  <sub>0..\*</sub>
     * Description: IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
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
