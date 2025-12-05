
# Class: ConformationalEnsemble

Ensemble of conformational states for a protein

URI: [lambdaber:ConformationalEnsemble](https://w3id.org/lambda-ber-schema/ConformationalEnsemble)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[ConformationalState],[ConformationalState]<conformational_states%200..*-++[ConformationalEnsemble&#124;protein_id:string;clustering_method:string%20%3F;rmsd_threshold:float%20%3F;transition_pathways:string%20%3F;energy_landscape:string%20%3F;principal_motions:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[AggregatedProteinView]++-%20conformational_ensemble%200..1>[ConformationalEnsemble],[Sample]++-%20conformational_ensemble%200..1>[ConformationalEnsemble],[NamedThing]^-[ConformationalEnsemble],[Sample],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[ConformationalState],[ConformationalState]<conformational_states%200..*-++[ConformationalEnsemble&#124;protein_id:string;clustering_method:string%20%3F;rmsd_threshold:float%20%3F;transition_pathways:string%20%3F;energy_landscape:string%20%3F;principal_motions:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[AggregatedProteinView]++-%20conformational_ensemble%200..1>[ConformationalEnsemble],[Sample]++-%20conformational_ensemble%200..1>[ConformationalEnsemble],[NamedThing]^-[ConformationalEnsemble],[Sample],[AggregatedProteinView])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞conformational_ensemble](aggregatedProteinView__conformational_ensemble.md)*  <sub>0..1</sub>  **[ConformationalEnsemble](ConformationalEnsemble.md)**
 *  **None** *[➞conformational_ensemble](sample__conformational_ensemble.md)*  <sub>0..1</sub>  **[ConformationalEnsemble](ConformationalEnsemble.md)**

## Attributes


### Own

 * [➞protein_id](conformationalEnsemble__protein_id.md)  <sub>1..1</sub>
     * Description: UniProt accession
     * Range: [String](types/String.md)
 * [➞conformational_states](conformationalEnsemble__conformational_states.md)  <sub>0..\*</sub>
     * Description: Individual conformational states
     * Range: [ConformationalState](ConformationalState.md)
 * [➞clustering_method](conformationalEnsemble__clustering_method.md)  <sub>0..1</sub>
     * Description: Method used for conformational clustering
     * Range: [String](types/String.md)
 * [➞rmsd_threshold](conformationalEnsemble__rmsd_threshold.md)  <sub>0..1</sub>
     * Description: RMSD threshold for clustering (Angstroms)
     * Range: [Float](types/Float.md)
 * [➞transition_pathways](conformationalEnsemble__transition_pathways.md)  <sub>0..1</sub>
     * Description: Description of transition pathways between states
     * Range: [String](types/String.md)
 * [➞energy_landscape](conformationalEnsemble__energy_landscape.md)  <sub>0..1</sub>
     * Description: Description of the energy landscape
     * Range: [String](types/String.md)
 * [➞principal_motions](conformationalEnsemble__principal_motions.md)  <sub>0..\*</sub>
     * Description: Description of principal motions
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
