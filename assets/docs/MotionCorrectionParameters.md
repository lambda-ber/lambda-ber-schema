
# Class: MotionCorrectionParameters

Parameters specific to motion correction workflows

URI: [lambdaber:MotionCorrectionParameters](https://w3id.org/lambda-ber-schema/MotionCorrectionParameters)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<drift_total%200..1-++[MotionCorrectionParameters&#124;dose_weighting:boolean%20%3F;anisotropic_correction:boolean%20%3F;description(i):string%20%3F],[QuantityValue]<output_binning%200..1-++[MotionCorrectionParameters],[QuantityValue]<frame_grouping%200..1-++[MotionCorrectionParameters],[QuantityValue]<bfactor_dose_weighting%200..1-++[MotionCorrectionParameters],[QuantityValue]<binning%200..1-++[MotionCorrectionParameters],[QuantityValue]<patch_size%200..1-++[MotionCorrectionParameters],[WorkflowRun]++-%20motion_correction_params%200..1>[MotionCorrectionParameters],[AttributeGroup]^-[MotionCorrectionParameters],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<drift_total%200..1-++[MotionCorrectionParameters&#124;dose_weighting:boolean%20%3F;anisotropic_correction:boolean%20%3F;description(i):string%20%3F],[QuantityValue]<output_binning%200..1-++[MotionCorrectionParameters],[QuantityValue]<frame_grouping%200..1-++[MotionCorrectionParameters],[QuantityValue]<bfactor_dose_weighting%200..1-++[MotionCorrectionParameters],[QuantityValue]<binning%200..1-++[MotionCorrectionParameters],[QuantityValue]<patch_size%200..1-++[MotionCorrectionParameters],[WorkflowRun]++-%20motion_correction_params%200..1>[MotionCorrectionParameters],[AttributeGroup]^-[MotionCorrectionParameters],[WorkflowRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞motion_correction_params](workflowRun__motion_correction_params.md)*  <sub>0..1</sub>  **[MotionCorrectionParameters](MotionCorrectionParameters.md)**

## Attributes


### Own

 * [➞patch_size](motionCorrectionParameters__patch_size.md)  <sub>0..1</sub>
     * Description: Patch size for local motion correction
     * Range: [QuantityValue](QuantityValue.md)
 * [➞binning](motionCorrectionParameters__binning.md)  <sub>0..1</sub>
     * Description: Binning factor applied during motion correction. This must be a positive float value (e.g., 1, 1.5, 2, 3).
     * Range: [QuantityValue](QuantityValue.md)
 * [➞dose_weighting](motionCorrectionParameters__dose_weighting.md)  <sub>0..1</sub>
     * Description: Whether dose weighting was applied
     * Range: [Boolean](types/Boolean.md)
 * [➞bfactor_dose_weighting](motionCorrectionParameters__bfactor_dose_weighting.md)  <sub>0..1</sub>
     * Description: B-factor for dose weighting, typically specified in Angstroms squared. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞anisotropic_correction](motionCorrectionParameters__anisotropic_correction.md)  <sub>0..1</sub>
     * Description: Whether anisotropic motion correction was applied
     * Range: [Boolean](types/Boolean.md)
 * [➞frame_grouping](motionCorrectionParameters__frame_grouping.md)  <sub>0..1</sub>
     * Description: Number of frames grouped together
     * Range: [QuantityValue](QuantityValue.md)
 * [➞output_binning](motionCorrectionParameters__output_binning.md)  <sub>0..1</sub>
     * Description: Output binning factor. This must be a positive float value (e.g., 1, 1.5, 2, 3).
     * Range: [QuantityValue](QuantityValue.md)
 * [➞drift_total](motionCorrectionParameters__drift_total.md)  <sub>0..1</sub>
     * Description: Total drift, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
