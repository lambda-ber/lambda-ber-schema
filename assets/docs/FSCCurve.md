
# Class: FSCCurve

Fourier Shell Correlation curve data.

The `resolution_angstrom` and `fsc_value` arrays must be of equal length, with each value at index i in `resolution_angstrom`
corresponding to the value at index i in `fsc_value`. Both arrays should not exceed 10,000 elements.

URI: [lambdaber:FSCCurve](https://w3id.org/lambda-ber-schema/FSCCurve)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20fsc_curve%200..1>[FSCCurve&#124;resolution_angstrom:float%20*;fsc_value:float%20*;description(i):string%20%3F],[AttributeGroup]^-[FSCCurve],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20fsc_curve%200..1>[FSCCurve&#124;resolution_angstrom:float%20*;fsc_value:float%20*;description(i):string%20%3F],[AttributeGroup]^-[FSCCurve],[WorkflowRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞fsc_curve](workflowRun__fsc_curve.md)*  <sub>0..1</sub>  **[FSCCurve](FSCCurve.md)**

## Attributes


### Own

 * [➞resolution_angstrom](fSCCurve__resolution_angstrom.md)  <sub>0..\*</sub>
     * Description: Resolution values in Angstroms
     * Range: [Float](types/Float.md)
 * [➞fsc_value](fSCCurve__fsc_value.md)  <sub>0..\*</sub>
     * Description: FSC values corresponding to each resolution
     * Range: [Float](types/Float.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
