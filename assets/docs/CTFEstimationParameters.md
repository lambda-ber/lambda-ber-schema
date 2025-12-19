
# Class: CTFEstimationParameters

Parameters specific to CTF estimation workflows

URI: [lambdaber:CTFEstimationParameters](https://w3id.org/lambda-ber-schema/CTFEstimationParameters)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<voltage_used_in_estimation%200..1-++[CTFEstimationParameters&#124;description(i):string%20%3F],[QuantityValue]<cs_used_in_estimation%200..1-++[CTFEstimationParameters],[QuantityValue]<amplitude_contrast%200..1-++[CTFEstimationParameters],[QuantityValue]<defocus_step%200..1-++[CTFEstimationParameters],[QuantityValue]<defocus_search_max%200..1-++[CTFEstimationParameters],[QuantityValue]<defocus_search_min%200..1-++[CTFEstimationParameters],[WorkflowRun]++-%20ctf_estimation_params%200..1>[CTFEstimationParameters],[AttributeGroup]^-[CTFEstimationParameters],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<voltage_used_in_estimation%200..1-++[CTFEstimationParameters&#124;description(i):string%20%3F],[QuantityValue]<cs_used_in_estimation%200..1-++[CTFEstimationParameters],[QuantityValue]<amplitude_contrast%200..1-++[CTFEstimationParameters],[QuantityValue]<defocus_step%200..1-++[CTFEstimationParameters],[QuantityValue]<defocus_search_max%200..1-++[CTFEstimationParameters],[QuantityValue]<defocus_search_min%200..1-++[CTFEstimationParameters],[WorkflowRun]++-%20ctf_estimation_params%200..1>[CTFEstimationParameters],[AttributeGroup]^-[CTFEstimationParameters],[WorkflowRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞ctf_estimation_params](workflowRun__ctf_estimation_params.md)*  <sub>0..1</sub>  **[CTFEstimationParameters](CTFEstimationParameters.md)**

## Attributes


### Own

 * [➞defocus_search_min](cTFEstimationParameters__defocus_search_min.md)  <sub>0..1</sub>
     * Description: Minimum defocus search range, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞defocus_search_max](cTFEstimationParameters__defocus_search_max.md)  <sub>0..1</sub>
     * Description: Maximum defocus search range, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞defocus_step](cTFEstimationParameters__defocus_step.md)  <sub>0..1</sub>
     * Description: Defocus search step, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞amplitude_contrast](cTFEstimationParameters__amplitude_contrast.md)  <sub>0..1</sub>
     * Description: Amplitude contrast value
     * Range: [QuantityValue](QuantityValue.md)
 * [➞cs_used_in_estimation](cTFEstimationParameters__cs_used_in_estimation.md)  <sub>0..1</sub>
     * Description: Spherical aberration (Cs) value used during CTF estimation, typically specified in millimeters; may differ from instrument specification. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞voltage_used_in_estimation](cTFEstimationParameters__voltage_used_in_estimation.md)  <sub>0..1</sub>
     * Description: Accelerating voltage value used during CTF estimation, typically specified in kilovolts (kV); may differ from instrument specification. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
