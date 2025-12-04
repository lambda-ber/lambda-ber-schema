
# Class: LigandInteraction

Small molecule/ligand interactions with proteins

URI: [lambdaber:LigandInteraction](https://w3id.org/lambda-ber-schema/LigandInteraction)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AggregatedProteinView]++-%20ligand_interactions%200..*>[LigandInteraction&#124;ligand_id:uriorcurie;ligand_name:string;ligand_smiles:smiles_string%20%3F;binding_affinity:float%20%3F;binding_affinity_type:BindingAffinityTypeEnum%20%3F;binding_affinity_unit:AffinityUnitEnum%20%3F;interaction_type:InteractionTypeEnum%20%3F;binding_site_residues:string%20*;is_cofactor:boolean%20%3F;is_drug_like:boolean%20%3F;druggability_score:float%20%3F;interaction_distance:float%20%3F;description(i):string%20%3F],[FunctionalSite]++-%20ligand_interactions%200..*>[LigandInteraction],[Sample]++-%20ligand_interactions%200..*>[LigandInteraction],[AttributeGroup]^-[LigandInteraction],[Sample],[FunctionalSite],[AttributeGroup],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[AggregatedProteinView]++-%20ligand_interactions%200..*>[LigandInteraction&#124;ligand_id:uriorcurie;ligand_name:string;ligand_smiles:smiles_string%20%3F;binding_affinity:float%20%3F;binding_affinity_type:BindingAffinityTypeEnum%20%3F;binding_affinity_unit:AffinityUnitEnum%20%3F;interaction_type:InteractionTypeEnum%20%3F;binding_site_residues:string%20*;is_cofactor:boolean%20%3F;is_drug_like:boolean%20%3F;druggability_score:float%20%3F;interaction_distance:float%20%3F;description(i):string%20%3F],[FunctionalSite]++-%20ligand_interactions%200..*>[LigandInteraction],[Sample]++-%20ligand_interactions%200..*>[LigandInteraction],[AttributeGroup]^-[LigandInteraction],[Sample],[FunctionalSite],[AttributeGroup],[AggregatedProteinView])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞ligand_interactions](aggregatedProteinView__ligand_interactions.md)*  <sub>0..\*</sub>  **[LigandInteraction](LigandInteraction.md)**
 *  **None** *[➞ligand_interactions](functionalSite__ligand_interactions.md)*  <sub>0..\*</sub>  **[LigandInteraction](LigandInteraction.md)**
 *  **None** *[➞ligand_interactions](sample__ligand_interactions.md)*  <sub>0..\*</sub>  **[LigandInteraction](LigandInteraction.md)**

## Attributes


### Own

 * [➞ligand_id](ligandInteraction__ligand_id.md)  <sub>1..1</sub>
     * Description: Ligand identifier (ChEMBL, ChEBI, PubChem)
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞ligand_name](ligandInteraction__ligand_name.md)  <sub>1..1</sub>
     * Description: Common name of the ligand
     * Range: [String](types/String.md)
 * [➞ligand_smiles](ligandInteraction__ligand_smiles.md)  <sub>0..1</sub>
     * Description: SMILES representation of the ligand
     * Range: [SmilesString](types/SmilesString.md)
 * [➞binding_affinity](ligandInteraction__binding_affinity.md)  <sub>0..1</sub>
     * Description: Binding affinity value
     * Range: [Float](types/Float.md)
 * [➞binding_affinity_type](ligandInteraction__binding_affinity_type.md)  <sub>0..1</sub>
     * Description: Type of binding measurement (Kd, Ki, IC50)
     * Range: [BindingAffinityTypeEnum](BindingAffinityTypeEnum.md)
 * [➞binding_affinity_unit](ligandInteraction__binding_affinity_unit.md)  <sub>0..1</sub>
     * Description: Unit of binding affinity
     * Range: [AffinityUnitEnum](AffinityUnitEnum.md)
 * [➞interaction_type](ligandInteraction__interaction_type.md)  <sub>0..1</sub>
     * Description: Type of interaction
     * Range: [InteractionTypeEnum](InteractionTypeEnum.md)
 * [➞binding_site_residues](ligandInteraction__binding_site_residues.md)  <sub>0..\*</sub>
     * Description: Residues involved in ligand binding
     * Range: [String](types/String.md)
 * [➞is_cofactor](ligandInteraction__is_cofactor.md)  <sub>0..1</sub>
     * Description: Whether the ligand is a cofactor
     * Range: [Boolean](types/Boolean.md)
 * [➞is_drug_like](ligandInteraction__is_drug_like.md)  <sub>0..1</sub>
     * Description: Whether the ligand has drug-like properties
     * Range: [Boolean](types/Boolean.md)
 * [➞druggability_score](ligandInteraction__druggability_score.md)  <sub>0..1</sub>
     * Description: Druggability score of the binding site
     * Range: [Float](types/Float.md)
 * [➞interaction_distance](ligandInteraction__interaction_distance.md)  <sub>0..1</sub>
     * Description: Distance criteria for interaction (Angstroms)
     * Range: [Float](types/Float.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
