
# Class: AggregatedProteinView

Aggregated view of all structural and functional data for a protein

URI: [lambdaber:AggregatedProteinView](https://w3id.org/lambda-ber-schema/AggregatedProteinView)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StructuralFeature],[ProteinProteinInteraction],[PostTranslationalModification],[NamedThing],[MutationEffect],[LigandInteraction],[FunctionalSite],[EvolutionaryConservation],[DatabaseCrossReference],[ConformationalEnsemble],[BiophysicalProperty],[DatabaseCrossReference]<cross_references%200..*-++[AggregatedProteinView&#124;uniprot_id:string;protein_name:string;organism:string%20%3F;organism_id:integer%20%3F;pdb_entries:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[EvolutionaryConservation]<evolutionary_conservation%200..1-++[AggregatedProteinView],[ConformationalEnsemble]<conformational_ensemble%200..1-++[AggregatedProteinView],[BiophysicalProperty]<biophysical_properties%200..*-++[AggregatedProteinView],[PostTranslationalModification]<ptms%200..*-++[AggregatedProteinView],[MutationEffect]<mutations%200..*-++[AggregatedProteinView],[LigandInteraction]<ligand_interactions%200..*-++[AggregatedProteinView],[ProteinProteinInteraction]<protein_interactions%200..*-++[AggregatedProteinView],[StructuralFeature]<structural_features%200..*-++[AggregatedProteinView],[FunctionalSite]<functional_sites%200..*-++[AggregatedProteinView],[Study]++-%20aggregated_protein_views%200..*>[AggregatedProteinView],[NamedThing]^-[AggregatedProteinView],[Study])](https://yuml.me/diagram/nofunky;dir:TB/class/[StructuralFeature],[ProteinProteinInteraction],[PostTranslationalModification],[NamedThing],[MutationEffect],[LigandInteraction],[FunctionalSite],[EvolutionaryConservation],[DatabaseCrossReference],[ConformationalEnsemble],[BiophysicalProperty],[DatabaseCrossReference]<cross_references%200..*-++[AggregatedProteinView&#124;uniprot_id:string;protein_name:string;organism:string%20%3F;organism_id:integer%20%3F;pdb_entries:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[EvolutionaryConservation]<evolutionary_conservation%200..1-++[AggregatedProteinView],[ConformationalEnsemble]<conformational_ensemble%200..1-++[AggregatedProteinView],[BiophysicalProperty]<biophysical_properties%200..*-++[AggregatedProteinView],[PostTranslationalModification]<ptms%200..*-++[AggregatedProteinView],[MutationEffect]<mutations%200..*-++[AggregatedProteinView],[LigandInteraction]<ligand_interactions%200..*-++[AggregatedProteinView],[ProteinProteinInteraction]<protein_interactions%200..*-++[AggregatedProteinView],[StructuralFeature]<structural_features%200..*-++[AggregatedProteinView],[FunctionalSite]<functional_sites%200..*-++[AggregatedProteinView],[Study]++-%20aggregated_protein_views%200..*>[AggregatedProteinView],[NamedThing]^-[AggregatedProteinView],[Study])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞aggregated_protein_views](study__aggregated_protein_views.md)*  <sub>0..\*</sub>  **[AggregatedProteinView](AggregatedProteinView.md)**

## Attributes


### Own

 * [➞uniprot_id](aggregatedProteinView__uniprot_id.md)  <sub>1..1</sub>
     * Description: UniProt accession
     * Range: [String](types/String.md)
 * [➞protein_name](aggregatedProteinView__protein_name.md)  <sub>1..1</sub>
     * Description: Protein name
     * Range: [String](types/String.md)
 * [➞organism](aggregatedProteinView__organism.md)  <sub>0..1</sub>
     * Description: Source organism
     * Range: [String](types/String.md)
 * [➞organism_id](aggregatedProteinView__organism_id.md)  <sub>0..1</sub>
     * Description: NCBI taxonomy ID
     * Range: [Integer](types/Integer.md)
 * [➞pdb_entries](aggregatedProteinView__pdb_entries.md)  <sub>0..\*</sub>
     * Description: All PDB entries for this protein
     * Range: [String](types/String.md)
 * [➞functional_sites](aggregatedProteinView__functional_sites.md)  <sub>0..\*</sub>
     * Description: All functional site annotations
     * Range: [FunctionalSite](FunctionalSite.md)
 * [➞structural_features](aggregatedProteinView__structural_features.md)  <sub>0..\*</sub>
     * Description: All structural feature annotations
     * Range: [StructuralFeature](StructuralFeature.md)
 * [➞protein_interactions](aggregatedProteinView__protein_interactions.md)  <sub>0..\*</sub>
     * Description: All protein-protein interactions
     * Range: [ProteinProteinInteraction](ProteinProteinInteraction.md)
 * [➞ligand_interactions](aggregatedProteinView__ligand_interactions.md)  <sub>0..\*</sub>
     * Description: All ligand interactions
     * Range: [LigandInteraction](LigandInteraction.md)
 * [➞mutations](aggregatedProteinView__mutations.md)  <sub>0..\*</sub>
     * Description: All mutation annotations
     * Range: [MutationEffect](MutationEffect.md)
 * [➞ptms](aggregatedProteinView__ptms.md)  <sub>0..\*</sub>
     * Description: All post-translational modifications
     * Range: [PostTranslationalModification](PostTranslationalModification.md)
 * [➞biophysical_properties](aggregatedProteinView__biophysical_properties.md)  <sub>0..\*</sub>
     * Description: All biophysical properties
     * Range: [BiophysicalProperty](BiophysicalProperty.md)
 * [➞conformational_ensemble](aggregatedProteinView__conformational_ensemble.md)  <sub>0..1</sub>
     * Description: Conformational ensemble data
     * Range: [ConformationalEnsemble](ConformationalEnsemble.md)
 * [➞evolutionary_conservation](aggregatedProteinView__evolutionary_conservation.md)  <sub>0..1</sub>
     * Description: Conservation analysis
     * Range: [EvolutionaryConservation](EvolutionaryConservation.md)
 * [➞cross_references](aggregatedProteinView__cross_references.md)  <sub>0..\*</sub>
     * Description: Database cross-references
     * Range: [DatabaseCrossReference](DatabaseCrossReference.md)

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
