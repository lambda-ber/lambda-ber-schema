
# Class: ComputeResources

Computational resources used

URI: [lambdaber:ComputeResources](https://w3id.org/lambda-ber-schema/ComputeResources)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<storage_gb%200..1-++[ComputeResources&#124;description(i):string%20%3F],[QuantityValue]<memory_gb%200..1-++[ComputeResources],[QuantityValue]<gpu_hours%200..1-++[ComputeResources],[QuantityValue]<cpu_hours%200..1-++[ComputeResources],[WorkflowRun]++-%20compute_resources%200..1>[ComputeResources],[AttributeGroup]^-[ComputeResources],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<storage_gb%200..1-++[ComputeResources&#124;description(i):string%20%3F],[QuantityValue]<memory_gb%200..1-++[ComputeResources],[QuantityValue]<gpu_hours%200..1-++[ComputeResources],[QuantityValue]<cpu_hours%200..1-++[ComputeResources],[WorkflowRun]++-%20compute_resources%200..1>[ComputeResources],[AttributeGroup]^-[ComputeResources],[WorkflowRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞compute_resources](workflowRun__compute_resources.md)*  <sub>0..1</sub>  **[ComputeResources](ComputeResources.md)**

## Attributes


### Own

 * [➞cpu_hours](computeResources__cpu_hours.md)  <sub>0..1</sub>
     * Description: CPU hours used, measured in hours. Data providers may specify alternative time units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞gpu_hours](computeResources__gpu_hours.md)  <sub>0..1</sub>
     * Description: GPU hours used, measured in hours. Data providers may specify alternative time units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞memory_gb](computeResources__memory_gb.md)  <sub>0..1</sub>
     * Description: Maximum memory used, typically specified in gigabytes (GB). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞storage_gb](computeResources__storage_gb.md)  <sub>0..1</sub>
     * Description: Storage used, typically specified in gigabytes (GB). Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
