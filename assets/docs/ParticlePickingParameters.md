
# Class: ParticlePickingParameters

Parameters specific to particle picking workflows

URI: [lambdaber:ParticlePickingParameters](https://w3id.org/lambda-ber-schema/ParticlePickingParameters)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20particle_picking_params%200..1>[ParticlePickingParameters&#124;picking_method:string%20%3F;box_size:integer%20%3F;threshold:float%20%3F;power_score:float%20%3F;ncc_score:float%20%3F;model_file:string%20%3F;description(i):string%20%3F],[AttributeGroup]^-[ParticlePickingParameters],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowRun]++-%20particle_picking_params%200..1>[ParticlePickingParameters&#124;picking_method:string%20%3F;box_size:integer%20%3F;threshold:float%20%3F;power_score:float%20%3F;ncc_score:float%20%3F;model_file:string%20%3F;description(i):string%20%3F],[AttributeGroup]^-[ParticlePickingParameters],[WorkflowRun],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞particle_picking_params](workflowRun__particle_picking_params.md)*  <sub>0..1</sub>  **[ParticlePickingParameters](ParticlePickingParameters.md)**

## Attributes


### Own

 * [➞picking_method](particlePickingParameters__picking_method.md)  <sub>0..1</sub>
     * Description: Method used (manual, template_matching, deep_learning, LoG, Topaz, other)
     * Range: [String](types/String.md)
 * [➞box_size](particlePickingParameters__box_size.md)  <sub>0..1</sub>
     * Description: Particle box size in pixels
     * Range: [Integer](types/Integer.md)
 * [➞threshold](particlePickingParameters__threshold.md)  <sub>0..1</sub>
     * Description: Picking threshold
     * Range: [Float](types/Float.md)
 * [➞power_score](particlePickingParameters__power_score.md)  <sub>0..1</sub>
     * Description: Power score threshold
     * Range: [Float](types/Float.md)
 * [➞ncc_score](particlePickingParameters__ncc_score.md)  <sub>0..1</sub>
     * Description: Normalized cross-correlation score threshold
     * Range: [Float](types/Float.md)
 * [➞model_file](particlePickingParameters__model_file.md)  <sub>0..1</sub>
     * Description: Path to deep learning model file if used
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
