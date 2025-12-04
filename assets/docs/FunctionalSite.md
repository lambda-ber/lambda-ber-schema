
# Class: FunctionalSite

Functional sites including catalytic, binding, and regulatory sites

URI: [lambdaber:FunctionalSite](https://w3id.org/lambda-ber-schema/FunctionalSite)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinAnnotation],[LigandInteraction],[LigandInteraction]<ligand_interactions%200..*-++[FunctionalSite&#124;site_type:FunctionalSiteTypeEnum;site_name:string%20%3F;residues:string%20*;conservation_score:float%20%3F;functional_importance:string%20%3F;go_terms:uriorcurie%20*;ec_number:string%20%3F;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[AggregatedProteinView]++-%20functional_sites%200..*>[FunctionalSite],[Sample]++-%20functional_sites%200..*>[FunctionalSite],[ProteinAnnotation]^-[FunctionalSite],[Sample],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinAnnotation],[LigandInteraction],[LigandInteraction]<ligand_interactions%200..*-++[FunctionalSite&#124;site_type:FunctionalSiteTypeEnum;site_name:string%20%3F;residues:string%20*;conservation_score:float%20%3F;functional_importance:string%20%3F;go_terms:uriorcurie%20*;ec_number:string%20%3F;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[AggregatedProteinView]++-%20functional_sites%200..*>[FunctionalSite],[Sample]++-%20functional_sites%200..*>[FunctionalSite],[ProteinAnnotation]^-[FunctionalSite],[Sample],[AggregatedProteinView])

## Parents

 *  is_a: [ProteinAnnotation](ProteinAnnotation.md) - Base class for all protein-related functional and structural annotations

## Referenced by Class

 *  **None** *[➞functional_sites](aggregatedProteinView__functional_sites.md)*  <sub>0..\*</sub>  **[FunctionalSite](FunctionalSite.md)**
 *  **None** *[➞functional_sites](sample__functional_sites.md)*  <sub>0..\*</sub>  **[FunctionalSite](FunctionalSite.md)**

## Attributes


### Own

 * [➞site_type](functionalSite__site_type.md)  <sub>1..1</sub>
     * Description: Type of functional site
     * Range: [FunctionalSiteTypeEnum](FunctionalSiteTypeEnum.md)
 * [➞site_name](functionalSite__site_name.md)  <sub>0..1</sub>
     * Description: Common name for this site
     * Range: [String](types/String.md)
 * [➞residues](functionalSite__residues.md)  <sub>0..\*</sub>
     * Description: List of residues forming the functional site. Each should be specified as a string (e.g., "45", "120A").
     * Range: [String](types/String.md)
 * [➞ligand_interactions](functionalSite__ligand_interactions.md)  <sub>0..\*</sub>
     * Description: Ligands that interact with this site
     * Range: [LigandInteraction](LigandInteraction.md)
 * [➞conservation_score](functionalSite__conservation_score.md)  <sub>0..1</sub>
     * Description: Evolutionary conservation score
     * Range: [Float](types/Float.md)
 * [➞functional_importance](functionalSite__functional_importance.md)  <sub>0..1</sub>
     * Description: Description of functional importance
     * Range: [String](types/String.md)
 * [➞go_terms](functionalSite__go_terms.md)  <sub>0..\*</sub>
     * Description: Associated Gene Ontology terms
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞ec_number](functionalSite__ec_number.md)  <sub>0..1</sub>
     * Description: Enzyme Commission number for catalytic sites
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
