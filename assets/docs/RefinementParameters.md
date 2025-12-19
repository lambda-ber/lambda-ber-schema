
# Class: RefinementParameters

Parameters specific to 3D refinement workflows

URI: [lambdaber:RefinementParameters](https://w3id.org/lambda-ber-schema/RefinementParameters)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<map_sharpening_bfactor%200..1-++[RefinementParameters&#124;symmetry:SymmetryEnum%20%3F;gold_standard:boolean%20%3F;split_strategy:string%20%3F;description(i):string%20%3F],[QuantityValue]<resolution_0_5%200..1-++[RefinementParameters],[QuantityValue]<resolution_0_143%200..1-++[RefinementParameters],[QuantityValue]<box_size%200..1-++[RefinementParameters],[QuantityValue]<pixel_size%200..1-++[RefinementParameters],[WorkflowRun]++-%20refinement_params%200..1>[RefinementParameters],[AttributeGroup]^-[RefinementParameters],[WorkflowRun],[QuantityValue],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<map_sharpening_bfactor%200..1-++[RefinementParameters&#124;symmetry:SymmetryEnum%20%3F;gold_standard:boolean%20%3F;split_strategy:string%20%3F;description(i):string%20%3F],[QuantityValue]<resolution_0_5%200..1-++[RefinementParameters],[QuantityValue]<resolution_0_143%200..1-++[RefinementParameters],[QuantityValue]<box_size%200..1-++[RefinementParameters],[QuantityValue]<pixel_size%200..1-++[RefinementParameters],[WorkflowRun]++-%20refinement_params%200..1>[RefinementParameters],[AttributeGroup]^-[RefinementParameters],[WorkflowRun],[QuantityValue],[AttributeGroup])

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
     * Description: Pixel size, typically specified in Angstroms per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞box_size](refinementParameters__box_size.md)  <sub>0..1</sub>
     * Description: Box size in pixels
     * Range: [QuantityValue](QuantityValue.md)
 * [➞gold_standard](refinementParameters__gold_standard.md)  <sub>0..1</sub>
     * Description: Whether gold-standard refinement was used
     * Range: [Boolean](types/Boolean.md)
 * [➞split_strategy](refinementParameters__split_strategy.md)  <sub>0..1</sub>
     * Description: Strategy for data splitting
     * Range: [String](types/String.md)
 * [➞resolution_0_143](refinementParameters__resolution_0_143.md)  <sub>0..1</sub>
     * Description: Resolution at FSC=0.143, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞resolution_0_5](refinementParameters__resolution_0_5.md)  <sub>0..1</sub>
     * Description: Resolution at FSC=0.5, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞map_sharpening_bfactor](refinementParameters__map_sharpening_bfactor.md)  <sub>0..1</sub>
     * Description: B-factor used for map sharpening, typically specified in Angstroms squared (Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
