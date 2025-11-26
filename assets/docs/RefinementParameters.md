
# Class: RefinementParameters

Parameters specific to 3D refinement workflows

URI: [lambdaber:RefinementParameters](https://w3id.org/lambda-ber-schema/RefinementParameters)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20refinement_params%200..1>[RefinementParameters&#124;symmetry:SymmetryEnum%20%3F;pixel_size:float%20%3F;box_size:integer%20%3F;gold_standard:boolean%20%3F;split_strategy:string%20%3F;resolution_0_143:float%20%3F;resolution_0_5:float%20%3F;map_sharpening_bfactor:float%20%3F;description(i):string%20%3F],[AttributeGroup]^-[RefinementParameters],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20refinement_params%200..1>[RefinementParameters&#124;symmetry:SymmetryEnum%20%3F;pixel_size:float%20%3F;box_size:integer%20%3F;gold_standard:boolean%20%3F;split_strategy:string%20%3F;resolution_0_143:float%20%3F;resolution_0_5:float%20%3F;map_sharpening_bfactor:float%20%3F;description(i):string%20%3F],[AttributeGroup]^-[RefinementParameters],[WorkflowRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞refinement_params](workflowRun__refinement_params.md)*  <sub>0..1</sub>  **[RefinementParameters](RefinementParameters.md)**

## Attributes


### Own

 * [➞symmetry](refinementParameters__symmetry.md)  <sub>0..1</sub>
     * Description: Symmetry applied (C1, Cn, Dn, T, O, I)
     * Range: [SymmetryEnum](SymmetryEnum.md)
 * [➞pixel_size](refinementParameters__pixel_size.md)  <sub>0..1</sub>
     * Description: Pixel size in Angstroms per pixel
     * Range: [Float](types/Float.md)
 * [➞box_size](refinementParameters__box_size.md)  <sub>0..1</sub>
     * Description: Box size in pixels
     * Range: [Integer](types/Integer.md)
 * [➞gold_standard](refinementParameters__gold_standard.md)  <sub>0..1</sub>
     * Description: Whether gold-standard refinement was used
     * Range: [Boolean](types/Boolean.md)
 * [➞split_strategy](refinementParameters__split_strategy.md)  <sub>0..1</sub>
     * Description: Strategy for data splitting
     * Range: [String](types/String.md)
 * [➞resolution_0_143](refinementParameters__resolution_0_143.md)  <sub>0..1</sub>
     * Description: Resolution at FSC=0.143 in Angstroms
     * Range: [Float](types/Float.md)
 * [➞resolution_0_5](refinementParameters__resolution_0_5.md)  <sub>0..1</sub>
     * Description: Resolution at FSC=0.5 in Angstroms
     * Range: [Float](types/Float.md)
 * [➞map_sharpening_bfactor](refinementParameters__map_sharpening_bfactor.md)  <sub>0..1</sub>
     * Description: B-factor used for map sharpening in Angstroms^2
     * Range: [Float](types/Float.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
