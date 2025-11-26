
# Class: MolecularComposition

Molecular composition of a sample

URI: [lambdaber:MolecularComposition](https://w3id.org/lambda-ber-schema/MolecularComposition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]++-%20molecular_composition%200..1>[MolecularComposition&#124;sequences:string%20*;modifications:string%20*;ligands:string%20*;description(i):string%20%3F],[AttributeGroup]^-[MolecularComposition],[Sample],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]++-%20molecular_composition%200..1>[MolecularComposition&#124;sequences:string%20*;modifications:string%20*;ligands:string%20*;description(i):string%20%3F],[AttributeGroup]^-[MolecularComposition],[Sample],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞molecular_composition](sample__molecular_composition.md)*  <sub>0..1</sub>  **[MolecularComposition](MolecularComposition.md)**

## Attributes


### Own

 * [➞sequences](molecularComposition__sequences.md)  <sub>0..\*</sub>
     * Description: Amino acid or nucleotide sequences
     * Range: [String](types/String.md)
 * [➞modifications](molecularComposition__modifications.md)  <sub>0..\*</sub>
     * Description: Post-translational modifications or chemical modifications
     * Range: [String](types/String.md)
 * [➞ligands](molecularComposition__ligands.md)  <sub>0..\*</sub>
     * Description: Bound ligands or cofactors
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
