
# Class: TechniqueSpecificPreparation

Base class for technique-specific preparation details

URI: [lambdaber:TechniqueSpecificPreparation](https://w3id.org/lambda-ber-schema/TechniqueSpecificPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[XRayPreparation],[TechniqueSpecificPreparation&#124;description(i):string%20%3F]^-[XRayPreparation],[TechniqueSpecificPreparation]^-[SAXSPreparation],[TechniqueSpecificPreparation]^-[CryoEMPreparation],[AttributeGroup]^-[TechniqueSpecificPreparation],[SAXSPreparation],[CryoEMPreparation],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[XRayPreparation],[TechniqueSpecificPreparation&#124;description(i):string%20%3F]^-[XRayPreparation],[TechniqueSpecificPreparation]^-[SAXSPreparation],[TechniqueSpecificPreparation]^-[CryoEMPreparation],[AttributeGroup]^-[TechniqueSpecificPreparation],[SAXSPreparation],[CryoEMPreparation],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Children

 * [CryoEMPreparation](CryoEMPreparation.md) - Cryo-EM specific sample preparation
 * [SAXSPreparation](SAXSPreparation.md) - SAXS/WAXS specific preparation
 * [XRayPreparation](XRayPreparation.md) - X-ray crystallography specific preparation

## Referenced by Class


## Attributes


### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
