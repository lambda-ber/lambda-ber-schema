
# Class: StructuralFeature

Structural features and properties of protein regions

URI: [lambdaber:StructuralFeature](https://w3id.org/lambda-ber-schema/StructuralFeature)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AggregatedProteinView]++-%20structural_features%200..*>[StructuralFeature&#124;feature_type:StructuralFeatureTypeEnum;secondary_structure:SecondaryStructureEnum%20%3F;solvent_accessibility:float%20%3F;backbone_flexibility:float%20%3F;disorder_probability:float%20%3F;conformational_state:ConformationalStateEnum%20%3F;structural_motif:string%20%3F;domain_assignment:string%20%3F;domain_id:string%20%3F;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20structural_features%200..*>[StructuralFeature],[ProteinAnnotation]^-[StructuralFeature],[Sample],[ProteinAnnotation],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[AggregatedProteinView]++-%20structural_features%200..*>[StructuralFeature&#124;feature_type:StructuralFeatureTypeEnum;secondary_structure:SecondaryStructureEnum%20%3F;solvent_accessibility:float%20%3F;backbone_flexibility:float%20%3F;disorder_probability:float%20%3F;conformational_state:ConformationalStateEnum%20%3F;structural_motif:string%20%3F;domain_assignment:string%20%3F;domain_id:string%20%3F;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20structural_features%200..*>[StructuralFeature],[ProteinAnnotation]^-[StructuralFeature],[Sample],[ProteinAnnotation],[AggregatedProteinView])

## Parents

 *  is_a: [ProteinAnnotation](ProteinAnnotation.md) - Base class for all protein-related functional and structural annotations

## Referenced by Class

 *  **None** *[➞structural_features](aggregatedProteinView__structural_features.md)*  <sub>0..\*</sub>  **[StructuralFeature](StructuralFeature.md)**
 *  **None** *[➞structural_features](sample__structural_features.md)*  <sub>0..\*</sub>  **[StructuralFeature](StructuralFeature.md)**

## Attributes


### Own

 * [➞feature_type](structuralFeature__feature_type.md)  <sub>1..1</sub>
     * Description: Type of structural feature
     * Range: [StructuralFeatureTypeEnum](StructuralFeatureTypeEnum.md)
 * [➞secondary_structure](structuralFeature__secondary_structure.md)  <sub>0..1</sub>
     * Description: Secondary structure assignment
     * Range: [SecondaryStructureEnum](SecondaryStructureEnum.md)
 * [➞solvent_accessibility](structuralFeature__solvent_accessibility.md)  <sub>0..1</sub>
     * Description: Relative solvent accessible surface area
     * Range: [Float](types/Float.md)
 * [➞backbone_flexibility](structuralFeature__backbone_flexibility.md)  <sub>0..1</sub>
     * Description: B-factor or flexibility measure
     * Range: [Float](types/Float.md)
 * [➞disorder_probability](structuralFeature__disorder_probability.md)  <sub>0..1</sub>
     * Description: Probability of disorder (0-1)
     * Range: [Float](types/Float.md)
 * [➞conformational_state](structuralFeature__conformational_state.md)  <sub>0..1</sub>
     * Description: Conformational state descriptor
     * Range: [ConformationalStateEnum](ConformationalStateEnum.md)
 * [➞structural_motif](structuralFeature__structural_motif.md)  <sub>0..1</sub>
     * Description: Known structural motif
     * Range: [String](types/String.md)
 * [➞domain_assignment](structuralFeature__domain_assignment.md)  <sub>0..1</sub>
     * Description: Domain database assignment (CATH, SCOP, Pfam)
     * Range: [String](types/String.md)
 * [➞domain_id](structuralFeature__domain_id.md)  <sub>0..1</sub>
     * Description: Domain identifier from domain database
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
