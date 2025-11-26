
# Class: ComputeResources

Computational resources used

URI: [lambdaber:ComputeResources](https://w3id.org/lambda-ber-schema/ComputeResources)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20compute_resources%200..1>[ComputeResources&#124;cpu_hours:float%20%3F;gpu_hours:float%20%3F;memory_gb:float%20%3F;storage_gb:float%20%3F;description(i):string%20%3F],[AttributeGroup]^-[ComputeResources],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20compute_resources%200..1>[ComputeResources&#124;cpu_hours:float%20%3F;gpu_hours:float%20%3F;memory_gb:float%20%3F;storage_gb:float%20%3F;description(i):string%20%3F],[AttributeGroup]^-[ComputeResources],[WorkflowRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞compute_resources](workflowRun__compute_resources.md)*  <sub>0..1</sub>  **[ComputeResources](ComputeResources.md)**

## Attributes


### Own

 * [➞cpu_hours](computeResources__cpu_hours.md)  <sub>0..1</sub>
     * Description: CPU hours used
     * Range: [Float](types/Float.md)
 * [➞gpu_hours](computeResources__gpu_hours.md)  <sub>0..1</sub>
     * Description: GPU hours used
     * Range: [Float](types/Float.md)
 * [➞memory_gb](computeResources__memory_gb.md)  <sub>0..1</sub>
     * Description: Maximum memory used in GB
     * Range: [Float](types/Float.md)
 * [➞storage_gb](computeResources__storage_gb.md)  <sub>0..1</sub>
     * Description: Storage used in GB
     * Range: [Float](types/Float.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
