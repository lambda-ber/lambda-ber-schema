
# Class: PostTranslationalModification

Post-translational modifications observed or predicted

URI: [lambdaber:PostTranslationalModification](https://w3id.org/lambda-ber-schema/PostTranslationalModification)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinAnnotation],[AggregatedProteinView]++-%20ptms%200..*>[PostTranslationalModification&#124;modification_type:PTMTypeEnum;modified_residue:string;modification_group:string%20%3F;mass_shift:float%20%3F;functional_effect:string%20%3F;regulatory_role:string%20%3F;enzyme:string%20%3F;removal_enzyme:string%20%3F;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20ptm_annotations%200..*>[PostTranslationalModification],[ProteinAnnotation]^-[PostTranslationalModification],[Sample],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinAnnotation],[AggregatedProteinView]++-%20ptms%200..*>[PostTranslationalModification&#124;modification_type:PTMTypeEnum;modified_residue:string;modification_group:string%20%3F;mass_shift:float%20%3F;functional_effect:string%20%3F;regulatory_role:string%20%3F;enzyme:string%20%3F;removal_enzyme:string%20%3F;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20ptm_annotations%200..*>[PostTranslationalModification],[ProteinAnnotation]^-[PostTranslationalModification],[Sample],[AggregatedProteinView])

## Parents

 *  is_a: [ProteinAnnotation](ProteinAnnotation.md) - Base class for all protein-related functional and structural annotations

## Referenced by Class

 *  **None** *[➞ptms](aggregatedProteinView__ptms.md)*  <sub>0..\*</sub>  **[PostTranslationalModification](PostTranslationalModification.md)**
 *  **None** *[➞ptm_annotations](sample__ptm_annotations.md)*  <sub>0..\*</sub>  **[PostTranslationalModification](PostTranslationalModification.md)**

## Attributes


### Own

 * [➞modification_type](postTranslationalModification__modification_type.md)  <sub>1..1</sub>
     * Description: Type of PTM
     * Range: [PTMTypeEnum](PTMTypeEnum.md)
 * [➞modified_residue](postTranslationalModification__modified_residue.md)  <sub>1..1</sub>
     * Description: Residue that is modified
     * Range: [String](types/String.md)
 * [➞modification_group](postTranslationalModification__modification_group.md)  <sub>0..1</sub>
     * Description: Chemical group added (e.g., 'phosphate', 'methyl')
     * Range: [String](types/String.md)
 * [➞mass_shift](postTranslationalModification__mass_shift.md)  <sub>0..1</sub>
     * Description: Mass change due to modification (Da)
     * Range: [Float](types/Float.md)
 * [➞functional_effect](postTranslationalModification__functional_effect.md)  <sub>0..1</sub>
     * Description: Known functional effect of this PTM
     * Range: [String](types/String.md)
 * [➞regulatory_role](postTranslationalModification__regulatory_role.md)  <sub>0..1</sub>
     * Description: Role in regulation
     * Range: [String](types/String.md)
 * [➞enzyme](postTranslationalModification__enzyme.md)  <sub>0..1</sub>
     * Description: Enzyme responsible for modification
     * Range: [String](types/String.md)
 * [➞removal_enzyme](postTranslationalModification__removal_enzyme.md)  <sub>0..1</sub>
     * Description: Enzyme that removes modification
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
