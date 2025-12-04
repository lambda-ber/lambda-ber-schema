
# Class: ConformationalState

Individual conformational state

URI: [lambdaber:ConformationalState](https://w3id.org/lambda-ber-schema/ConformationalState)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ConformationalEnsemble]++-%20conformational_states%200..*>[ConformationalState&#124;state_id:string;state_name:string%20%3F;pdb_entries:string%20*;population:float%20%3F;free_energy:float%20%3F;rmsd_from_reference:float%20%3F;characteristic_features:string%20*;description(i):string%20%3F],[AttributeGroup]^-[ConformationalState],[ConformationalEnsemble],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[ConformationalEnsemble]++-%20conformational_states%200..*>[ConformationalState&#124;state_id:string;state_name:string%20%3F;pdb_entries:string%20*;population:float%20%3F;free_energy:float%20%3F;rmsd_from_reference:float%20%3F;characteristic_features:string%20*;description(i):string%20%3F],[AttributeGroup]^-[ConformationalState],[ConformationalEnsemble],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞conformational_states](conformationalEnsemble__conformational_states.md)*  <sub>0..\*</sub>  **[ConformationalState](ConformationalState.md)**

## Attributes


### Own

 * [➞state_id](conformationalState__state_id.md)  <sub>1..1</sub>
     * Description: Identifier for this state
     * Range: [String](types/String.md)
 * [➞state_name](conformationalState__state_name.md)  <sub>0..1</sub>
     * Description: Descriptive name (e.g., 'open', 'closed')
     * Range: [String](types/String.md)
 * [➞pdb_entries](conformationalState__pdb_entries.md)  <sub>0..\*</sub>
     * Description: PDB entries representing this state
     * Range: [String](types/String.md)
 * [➞population](conformationalState__population.md)  <sub>0..1</sub>
     * Description: Relative population of this state
     * Range: [Float](types/Float.md)
 * [➞free_energy](conformationalState__free_energy.md)  <sub>0..1</sub>
     * Description: Relative free energy (kcal/mol)
     * Range: [Float](types/Float.md)
 * [➞rmsd_from_reference](conformationalState__rmsd_from_reference.md)  <sub>0..1</sub>
     * Description: RMSD from reference structure
     * Range: [Float](types/Float.md)
 * [➞characteristic_features](conformationalState__characteristic_features.md)  <sub>0..\*</sub>
     * Description: Key features of this conformation
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
