
# Class: ProteinProteinInteraction

Protein-protein interactions and interfaces

URI: [lambdaber:ProteinProteinInteraction](https://w3id.org/lambda-ber-schema/ProteinProteinInteraction)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AggregatedProteinView]++-%20protein_interactions%200..*>[ProteinProteinInteraction&#124;partner_protein_id:string;partner_chain_id:string%20%3F;interface_residues:string%20*;partner_interface_residues:string%20*;interface_area:float%20%3F;binding_energy:float%20%3F;dissociation_constant:float%20%3F;complex_stability:ComplexStabilityEnum%20%3F;biological_assembly:boolean%20%3F;interaction_evidence:InteractionEvidenceEnum%20*;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20protein_interactions%200..*>[ProteinProteinInteraction],[ProteinAnnotation]^-[ProteinProteinInteraction],[Sample],[ProteinAnnotation],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[AggregatedProteinView]++-%20protein_interactions%200..*>[ProteinProteinInteraction&#124;partner_protein_id:string;partner_chain_id:string%20%3F;interface_residues:string%20*;partner_interface_residues:string%20*;interface_area:float%20%3F;binding_energy:float%20%3F;dissociation_constant:float%20%3F;complex_stability:ComplexStabilityEnum%20%3F;biological_assembly:boolean%20%3F;interaction_evidence:InteractionEvidenceEnum%20*;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20protein_interactions%200..*>[ProteinProteinInteraction],[ProteinAnnotation]^-[ProteinProteinInteraction],[Sample],[ProteinAnnotation],[AggregatedProteinView])

## Parents

 *  is_a: [ProteinAnnotation](ProteinAnnotation.md) - Base class for all protein-related functional and structural annotations

## Referenced by Class

 *  **None** *[➞protein_interactions](aggregatedProteinView__protein_interactions.md)*  <sub>0..\*</sub>  **[ProteinProteinInteraction](ProteinProteinInteraction.md)**
 *  **None** *[➞protein_interactions](sample__protein_interactions.md)*  <sub>0..\*</sub>  **[ProteinProteinInteraction](ProteinProteinInteraction.md)**

## Attributes


### Own

 * [➞partner_protein_id](proteinProteinInteraction__partner_protein_id.md)  <sub>1..1</sub>
     * Description: UniProt ID of interacting partner
     * Range: [String](types/String.md)
 * [➞partner_chain_id](proteinProteinInteraction__partner_chain_id.md)  <sub>0..1</sub>
     * Description: Chain ID of interacting partner
     * Range: [String](types/String.md)
 * [➞interface_residues](proteinProteinInteraction__interface_residues.md)  <sub>0..\*</sub>
     * Description: Residues at the interaction interface
     * Range: [String](types/String.md)
 * [➞partner_interface_residues](proteinProteinInteraction__partner_interface_residues.md)  <sub>0..\*</sub>
     * Description: Partner residues at the interaction interface
     * Range: [String](types/String.md)
 * [➞interface_area](proteinProteinInteraction__interface_area.md)  <sub>0..1</sub>
     * Description: Buried surface area at interface (Ų)
     * Range: [Float](types/Float.md)
 * [➞binding_energy](proteinProteinInteraction__binding_energy.md)  <sub>0..1</sub>
     * Description: Calculated binding energy (kcal/mol)
     * Range: [Float](types/Float.md)
 * [➞dissociation_constant](proteinProteinInteraction__dissociation_constant.md)  <sub>0..1</sub>
     * Description: Experimental Kd if available
     * Range: [Float](types/Float.md)
 * [➞complex_stability](proteinProteinInteraction__complex_stability.md)  <sub>0..1</sub>
     * Description: Stability assessment of the complex
     * Range: [ComplexStabilityEnum](ComplexStabilityEnum.md)
 * [➞biological_assembly](proteinProteinInteraction__biological_assembly.md)  <sub>0..1</sub>
     * Description: Whether this represents a biological assembly
     * Range: [Boolean](types/Boolean.md)
 * [➞interaction_evidence](proteinProteinInteraction__interaction_evidence.md)  <sub>0..\*</sub>
     * Description: Evidence for this interaction
     * Range: [InteractionEvidenceEnum](InteractionEvidenceEnum.md)

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
