
# Class: ParticlePickingParameters

Parameters specific to particle picking workflows

URI: [lambdaber:ParticlePickingParameters](https://w3id.org/lambda-ber-schema/ParticlePickingParameters)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<ncc_score%200..1-++[ParticlePickingParameters&#124;picking_method:string%20%3F;model_name:string%20%3F;model_file_path:string%20%3F;model_source:string%20%3F;description(i):string%20%3F],[QuantityValue]<power_score%200..1-++[ParticlePickingParameters],[QuantityValue]<threshold%200..1-++[ParticlePickingParameters],[QuantityValue]<box_size%200..1-++[ParticlePickingParameters],[WorkflowRun]++-%20particle_picking_params%200..1>[ParticlePickingParameters],[AttributeGroup]^-[ParticlePickingParameters],[WorkflowRun],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[QuantityValue]<ncc_score%200..1-++[ParticlePickingParameters&#124;picking_method:string%20%3F;model_name:string%20%3F;model_file_path:string%20%3F;model_source:string%20%3F;description(i):string%20%3F],[QuantityValue]<power_score%200..1-++[ParticlePickingParameters],[QuantityValue]<threshold%200..1-++[ParticlePickingParameters],[QuantityValue]<box_size%200..1-++[ParticlePickingParameters],[WorkflowRun]++-%20particle_picking_params%200..1>[ParticlePickingParameters],[AttributeGroup]^-[ParticlePickingParameters],[WorkflowRun],[AttributeGroup])

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
     * Range: [QuantityValue](QuantityValue.md)
 * [➞threshold](particlePickingParameters__threshold.md)  <sub>0..1</sub>
     * Description: Picking threshold
     * Range: [QuantityValue](QuantityValue.md)
 * [➞power_score](particlePickingParameters__power_score.md)  <sub>0..1</sub>
     * Description: Power score threshold
     * Range: [QuantityValue](QuantityValue.md)
 * [➞ncc_score](particlePickingParameters__ncc_score.md)  <sub>0..1</sub>
     * Description: Normalized cross-correlation score threshold
     * Range: [QuantityValue](QuantityValue.md)
 * [➞model_name](particlePickingParameters__model_name.md)  <sub>0..1</sub>
     * Description: Name or identifier of the deep learning model (e.g., 'resnet16', 'resnet8', 'cryolo_general'). Use this for standard pretrained models. Either model_name or model_file_path should be provided when using deep learning methods.
     * Range: [String](types/String.md)
 * [➞model_file_path](particlePickingParameters__model_file_path.md)  <sub>0..1</sub>
     * Description: Path to deep learning model file if using a local or custom trained model file. Use this instead of model_name when pointing to a specific file on disk. Either model_name or model_file_path should be provided when using deep learning methods.
     * Range: [String](types/String.md)
 * [➞model_source](particlePickingParameters__model_source.md)  <sub>0..1</sub>
     * Description: Source or software associated with the model (e.g., 'topaz', 'cryolo', 'warp', 'custom', 'pretrained'). Helps track model provenance and should be provided alongside model_name or model_file_path to document which software/framework the model is for.
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
