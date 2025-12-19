
# Class: EvolutionaryConservation

Evolutionary conservation information

URI: [lambdaber:EvolutionaryConservation](https://w3id.org/lambda-ber-schema/EvolutionaryConservation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinAnnotation],[AggregatedProteinView]++-%20evolutionary_conservation%200..1>[EvolutionaryConservation&#124;conservation_score:float%20%3F;conserved_residues:string%20*;variable_residues:string%20*;conservation_method:string%20%3F;alignment_depth:integer%20%3F;taxonomic_range:string%20%3F;coevolved_residues:string%20*;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20evolutionary_conservation%200..1>[EvolutionaryConservation],[ProteinAnnotation]^-[EvolutionaryConservation],[Sample],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinAnnotation],[AggregatedProteinView]++-%20evolutionary_conservation%200..1>[EvolutionaryConservation&#124;conservation_score:float%20%3F;conserved_residues:string%20*;variable_residues:string%20*;conservation_method:string%20%3F;alignment_depth:integer%20%3F;taxonomic_range:string%20%3F;coevolved_residues:string%20*;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20evolutionary_conservation%200..1>[EvolutionaryConservation],[ProteinAnnotation]^-[EvolutionaryConservation],[Sample],[AggregatedProteinView])

## Parents

 *  is_a: [ProteinAnnotation](ProteinAnnotation.md) - Base class for all protein-related functional and structural annotations

## Referenced by Class

 *  **None** *[➞evolutionary_conservation](aggregatedProteinView__evolutionary_conservation.md)*  <sub>0..1</sub>  **[EvolutionaryConservation](EvolutionaryConservation.md)**
 *  **None** *[➞evolutionary_conservation](sample__evolutionary_conservation.md)*  <sub>0..1</sub>  **[EvolutionaryConservation](EvolutionaryConservation.md)**

## Attributes


### Own

 * [➞conservation_score](evolutionaryConservation__conservation_score.md)  <sub>0..1</sub>
     * Description: Overall conservation score (range: 0-1)
     * Range: [Float](types/Float.md)
 * [➞conserved_residues](evolutionaryConservation__conserved_residues.md)  <sub>0..\*</sub>
     * Description: Highly conserved residues
     * Range: [String](types/String.md)
 * [➞variable_residues](evolutionaryConservation__variable_residues.md)  <sub>0..\*</sub>
     * Description: Highly variable residues
     * Range: [String](types/String.md)
 * [➞conservation_method](evolutionaryConservation__conservation_method.md)  <sub>0..1</sub>
     * Description: Method used for conservation analysis
     * Range: [String](types/String.md)
 * [➞alignment_depth](evolutionaryConservation__alignment_depth.md)  <sub>0..1</sub>
     * Description: Number of sequences in alignment
     * Range: [Integer](types/Integer.md)
 * [➞taxonomic_range](evolutionaryConservation__taxonomic_range.md)  <sub>0..1</sub>
     * Description: Taxonomic range of conservation
     * Range: [String](types/String.md)
 * [➞coevolved_residues](evolutionaryConservation__coevolved_residues.md)  <sub>0..\*</sub>
     * Description: Pairs of coevolved residues
     * Range: [String](types/String.md)

### Inherited from ProteinAnnotation:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
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
     * Description: Confidence score for the annotation (range: 0-1)
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
