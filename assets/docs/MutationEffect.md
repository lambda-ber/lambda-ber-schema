
# Class: MutationEffect

Effects of mutations and variants on protein structure and function

URI: [lambdaber:MutationEffect](https://w3id.org/lambda-ber-schema/MutationEffect)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinAnnotation],[AggregatedProteinView]++-%20mutations%200..*>[MutationEffect&#124;mutation:string;mutation_type:MutationTypeEnum%20%3F;effect_on_stability:StabilityEffectEnum%20%3F;delta_delta_g:float%20%3F;effect_on_function:FunctionalEffectEnum%20%3F;functional_impact_description:string%20%3F;disease_association:string%20%3F;omim_id:string%20%3F;clinical_significance:ClinicalSignificanceEnum%20%3F;allele_frequency:float%20%3F;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20mutation_effects%200..*>[MutationEffect],[ProteinAnnotation]^-[MutationEffect],[Sample],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProteinAnnotation],[AggregatedProteinView]++-%20mutations%200..*>[MutationEffect&#124;mutation:string;mutation_type:MutationTypeEnum%20%3F;effect_on_stability:StabilityEffectEnum%20%3F;delta_delta_g:float%20%3F;effect_on_function:FunctionalEffectEnum%20%3F;functional_impact_description:string%20%3F;disease_association:string%20%3F;omim_id:string%20%3F;clinical_significance:ClinicalSignificanceEnum%20%3F;allele_frequency:float%20%3F;protein_id(i):string;pdb_entry(i):string%20%3F;chain_id(i):string%20%3F;residue_range(i):string%20%3F;confidence_score(i):float%20%3F;evidence_type(i):EvidenceTypeEnum%20%3F;evidence_code(i):uriorcurie%20%3F;source_database(i):AnnotationSourceEnum%20%3F;annotation_method(i):string%20%3F;publication_ids(i):string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Sample]++-%20mutation_effects%200..*>[MutationEffect],[ProteinAnnotation]^-[MutationEffect],[Sample],[AggregatedProteinView])

## Parents

 *  is_a: [ProteinAnnotation](ProteinAnnotation.md) - Base class for all protein-related functional and structural annotations

## Referenced by Class

 *  **None** *[➞mutations](aggregatedProteinView__mutations.md)*  <sub>0..\*</sub>  **[MutationEffect](MutationEffect.md)**
 *  **None** *[➞mutation_effects](sample__mutation_effects.md)*  <sub>0..\*</sub>  **[MutationEffect](MutationEffect.md)**

## Attributes


### Own

 * [➞mutation](mutationEffect__mutation.md)  <sub>1..1</sub>
     * Description: Mutation in standard notation (e.g., 'A123V')
     * Range: [String](types/String.md)
 * [➞mutation_type](mutationEffect__mutation_type.md)  <sub>0..1</sub>
     * Description: Type of mutation
     * Range: [MutationTypeEnum](MutationTypeEnum.md)
 * [➞effect_on_stability](mutationEffect__effect_on_stability.md)  <sub>0..1</sub>
     * Description: Effect on protein stability
     * Range: [StabilityEffectEnum](StabilityEffectEnum.md)
 * [➞delta_delta_g](mutationEffect__delta_delta_g.md)  <sub>0..1</sub>
     * Description: Change in folding free energy (kcal/mol)
     * Range: [Float](types/Float.md)
 * [➞effect_on_function](mutationEffect__effect_on_function.md)  <sub>0..1</sub>
     * Description: Effect on protein function
     * Range: [FunctionalEffectEnum](FunctionalEffectEnum.md)
 * [➞functional_impact_description](mutationEffect__functional_impact_description.md)  <sub>0..1</sub>
     * Description: Description of functional impact
     * Range: [String](types/String.md)
 * [➞disease_association](mutationEffect__disease_association.md)  <sub>0..1</sub>
     * Description: Associated disease or phenotype
     * Range: [String](types/String.md)
 * [➞omim_id](mutationEffect__omim_id.md)  <sub>0..1</sub>
     * Description: OMIM database identifier
     * Range: [String](types/String.md)
 * [➞clinical_significance](mutationEffect__clinical_significance.md)  <sub>0..1</sub>
     * Description: Clinical significance
     * Range: [ClinicalSignificanceEnum](ClinicalSignificanceEnum.md)
 * [➞allele_frequency](mutationEffect__allele_frequency.md)  <sub>0..1</sub>
     * Description: Population allele frequency
     * Range: [Float](types/Float.md)

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
