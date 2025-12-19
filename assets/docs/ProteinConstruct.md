
# Class: ProteinConstruct

Detailed information about a protein construct including cloning and sequence design

URI: [lambdaber:ProteinConstruct](https://w3id.org/lambda-ber-schema/ProteinConstruct)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<sequence_length_aa%200..1-++[ProteinConstruct&#124;construct_id:string;uniprot_id:string%20%3F;gene_name:string%20%3F;ncbi_taxid:string%20%3F;construct_description:string%20%3F;gene_synthesis_provider:string%20%3F;codon_optimization_organism:string%20%3F;vector_backbone:string%20%3F;vector_name:string%20%3F;promoter:string%20%3F;tag_nterm:string%20%3F;tag_cterm:string%20%3F;cleavage_site:string%20%3F;signal_peptide:string%20%3F;selectable_marker:string%20%3F;cloning_method:string%20%3F;insert_boundaries:string%20%3F;sequence_file_path:string%20%3F;sequence_verified_by:string%20%3F;verification_notes:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Study]++-%20protein_constructs%200..*>[ProteinConstruct],[NamedThing]^-[ProteinConstruct],[Study],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<sequence_length_aa%200..1-++[ProteinConstruct&#124;construct_id:string;uniprot_id:string%20%3F;gene_name:string%20%3F;ncbi_taxid:string%20%3F;construct_description:string%20%3F;gene_synthesis_provider:string%20%3F;codon_optimization_organism:string%20%3F;vector_backbone:string%20%3F;vector_name:string%20%3F;promoter:string%20%3F;tag_nterm:string%20%3F;tag_cterm:string%20%3F;cleavage_site:string%20%3F;signal_peptide:string%20%3F;selectable_marker:string%20%3F;cloning_method:string%20%3F;insert_boundaries:string%20%3F;sequence_file_path:string%20%3F;sequence_verified_by:string%20%3F;verification_notes:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Study]++-%20protein_constructs%200..*>[ProteinConstruct],[NamedThing]^-[ProteinConstruct],[Study],[NamedThing])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞protein_constructs](study__protein_constructs.md)*  <sub>0..\*</sub>  **[ProteinConstruct](ProteinConstruct.md)**

## Attributes


### Own

 * [➞construct_id](proteinConstruct__construct_id.md)  <sub>1..1</sub>
     * Description: Unique identifier for this construct
     * Range: [String](types/String.md)
 * [➞uniprot_id](proteinConstruct__uniprot_id.md)  <sub>0..1</sub>
     * Description: UniProt accession for the target protein
     * Range: [String](types/String.md)
 * [➞gene_name](proteinConstruct__gene_name.md)  <sub>0..1</sub>
     * Description: Gene name
     * Range: [String](types/String.md)
 * [➞ncbi_taxid](proteinConstruct__ncbi_taxid.md)  <sub>0..1</sub>
     * Description: NCBI Taxonomy ID for source organism
     * Range: [String](types/String.md)
 * [➞sequence_length_aa](proteinConstruct__sequence_length_aa.md)  <sub>0..1</sub>
     * Description: Length of the protein sequence in amino acids
     * Range: [QuantityValue](QuantityValue.md)
 * [➞construct_description](proteinConstruct__construct_description.md)  <sub>0..1</sub>
     * Description: Human-readable description of the construct
     * Range: [String](types/String.md)
 * [➞gene_synthesis_provider](proteinConstruct__gene_synthesis_provider.md)  <sub>0..1</sub>
     * Description: Company or facility that synthesized the gene
     * Range: [String](types/String.md)
 * [➞codon_optimization_organism](proteinConstruct__codon_optimization_organism.md)  <sub>0..1</sub>
     * Description: Organism for which codons were optimized
     * Range: [String](types/String.md)
 * [➞vector_backbone](proteinConstruct__vector_backbone.md)  <sub>0..1</sub>
     * Description: Base plasmid backbone used
     * Range: [String](types/String.md)
 * [➞vector_name](proteinConstruct__vector_name.md)  <sub>0..1</sub>
     * Description: Complete vector name
     * Range: [String](types/String.md)
 * [➞promoter](proteinConstruct__promoter.md)  <sub>0..1</sub>
     * Description: Promoter used for expression
     * Range: [String](types/String.md)
 * [➞tag_nterm](proteinConstruct__tag_nterm.md)  <sub>0..1</sub>
     * Description: N-terminal tag (e.g., His6, MBP, GST)
     * Range: [String](types/String.md)
 * [➞tag_cterm](proteinConstruct__tag_cterm.md)  <sub>0..1</sub>
     * Description: C-terminal tag
     * Range: [String](types/String.md)
 * [➞cleavage_site](proteinConstruct__cleavage_site.md)  <sub>0..1</sub>
     * Description: Protease cleavage site sequence
     * Range: [String](types/String.md)
 * [➞signal_peptide](proteinConstruct__signal_peptide.md)  <sub>0..1</sub>
     * Description: Signal peptide sequence if present
     * Range: [String](types/String.md)
 * [➞selectable_marker](proteinConstruct__selectable_marker.md)  <sub>0..1</sub>
     * Description: Antibiotic resistance or other selectable marker
     * Range: [String](types/String.md)
 * [➞cloning_method](proteinConstruct__cloning_method.md)  <sub>0..1</sub>
     * Description: Method used for cloning (e.g., restriction digest, Gibson, InFusion)
     * Range: [String](types/String.md)
 * [➞insert_boundaries](proteinConstruct__insert_boundaries.md)  <sub>0..1</sub>
     * Description: Start and end positions of insert in vector
     * Range: [String](types/String.md)
 * [➞sequence_file_path](proteinConstruct__sequence_file_path.md)  <sub>0..1</sub>
     * Description: Path to sequence file
     * Range: [String](types/String.md)
 * [➞sequence_verified_by](proteinConstruct__sequence_verified_by.md)  <sub>0..1</sub>
     * Description: Method or person who verified the sequence
     * Range: [String](types/String.md)
 * [➞verification_notes](proteinConstruct__verification_notes.md)  <sub>0..1</sub>
     * Description: Notes from sequence verification
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
