
# Class: StorageConditions

Storage conditions for samples

URI: [lambdaber:StorageConditions](https://w3id.org/lambda-ber-schema/StorageConditions)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<temperature%200..1-++[StorageConditions&#124;duration:string%20%3F;atmosphere:string%20%3F;description(i):string%20%3F],[Sample]++-%20storage_conditions%200..1>[StorageConditions],[AttributeGroup]^-[StorageConditions],[Sample],[QuantityValue],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<temperature%200..1-++[StorageConditions&#124;duration:string%20%3F;atmosphere:string%20%3F;description(i):string%20%3F],[Sample]++-%20storage_conditions%200..1>[StorageConditions],[AttributeGroup]^-[StorageConditions],[Sample],[QuantityValue],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞storage_conditions](sample__storage_conditions.md)*  <sub>0..1</sub>  **[StorageConditions](StorageConditions.md)**

## Attributes


### Own

 * [➞temperature](storageConditions__temperature.md)  <sub>0..1</sub>
     * Description: Storage temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
     * Range: [QuantityValue](QuantityValue.md)
 * [➞duration](storageConditions__duration.md)  <sub>0..1</sub>
     * Description: Storage duration
     * Range: [String](types/String.md)
 * [➞atmosphere](storageConditions__atmosphere.md)  <sub>0..1</sub>
     * Description: Storage atmosphere conditions
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
