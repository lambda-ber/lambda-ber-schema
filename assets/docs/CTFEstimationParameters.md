
# Class: CTFEstimationParameters

Parameters specific to CTF estimation workflows

URI: [lambdaber:CTFEstimationParameters](https://w3id.org/lambda-ber-schema/CTFEstimationParameters)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20ctf_estimation_params%200..1>[CTFEstimationParameters&#124;defocus_search_min:float%20%3F;defocus_search_max:float%20%3F;defocus_step:float%20%3F;amplitude_contrast:float%20%3F;cs_used_in_estimation:float%20%3F;voltage_used_in_estimation:float%20%3F;description(i):string%20%3F],[AttributeGroup]^-[CTFEstimationParameters],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20ctf_estimation_params%200..1>[CTFEstimationParameters&#124;defocus_search_min:float%20%3F;defocus_search_max:float%20%3F;defocus_step:float%20%3F;amplitude_contrast:float%20%3F;cs_used_in_estimation:float%20%3F;voltage_used_in_estimation:float%20%3F;description(i):string%20%3F],[AttributeGroup]^-[CTFEstimationParameters],[WorkflowRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞ctf_estimation_params](workflowRun__ctf_estimation_params.md)*  <sub>0..1</sub>  **[CTFEstimationParameters](CTFEstimationParameters.md)**

## Attributes


### Own

 * [➞defocus_search_min](cTFEstimationParameters__defocus_search_min.md)  <sub>0..1</sub>
     * Description: Minimum defocus search range in micrometers
     * Range: [Float](types/Float.md)
 * [➞defocus_search_max](cTFEstimationParameters__defocus_search_max.md)  <sub>0..1</sub>
     * Description: Maximum defocus search range in micrometers
     * Range: [Float](types/Float.md)
 * [➞defocus_step](cTFEstimationParameters__defocus_step.md)  <sub>0..1</sub>
     * Description: Defocus search step in micrometers
     * Range: [Float](types/Float.md)
 * [➞amplitude_contrast](cTFEstimationParameters__amplitude_contrast.md)  <sub>0..1</sub>
     * Description: Amplitude contrast value
     * Range: [Float](types/Float.md)
 * [➞cs_used_in_estimation](cTFEstimationParameters__cs_used_in_estimation.md)  <sub>0..1</sub>
     * Description: Spherical aberration (Cs) value used during CTF estimation (in millimeters); may differ from instrument specification
     * Range: [Float](types/Float.md)
 * [➞voltage_used_in_estimation](cTFEstimationParameters__voltage_used_in_estimation.md)  <sub>0..1</sub>
     * Description: Accelerating voltage value used during CTF estimation (in kV); may differ from instrument specification
     * Range: [Float](types/Float.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
