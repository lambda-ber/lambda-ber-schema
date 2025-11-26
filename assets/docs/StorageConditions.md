
# Class: StorageConditions

Storage conditions for samples

URI: [lambdaber:StorageConditions](https://w3id.org/lambda-ber-schema/StorageConditions)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]++-%20storage_conditions%200..1>[StorageConditions&#124;temperature:float%20%3F;temperature_unit:TemperatureUnitEnum%20%3F;duration:string%20%3F;atmosphere:string%20%3F;description(i):string%20%3F],[AttributeGroup]^-[StorageConditions],[Sample],[AttributeGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]++-%20storage_conditions%200..1>[StorageConditions&#124;temperature:float%20%3F;temperature_unit:TemperatureUnitEnum%20%3F;duration:string%20%3F;atmosphere:string%20%3F;description(i):string%20%3F],[AttributeGroup]^-[StorageConditions],[Sample],[AttributeGroup])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞storage_conditions](sample__storage_conditions.md)*  <sub>0..1</sub>  **[StorageConditions](StorageConditions.md)**

## Attributes


### Own

 * [➞temperature](storageConditions__temperature.md)  <sub>0..1</sub>
     * Description: Storage temperature in Celsius
     * Range: [Float](types/Float.md)
 * [➞temperature_unit](storageConditions__temperature_unit.md)  <sub>0..1</sub>
     * Description: Temperature unit
     * Range: [TemperatureUnitEnum](TemperatureUnitEnum.md)
 * [➞duration](storageConditions__duration.md)  <sub>0..1</sub>
     * Description: Storage duration
     * Range: [String](types/String.md)
 * [➞atmosphere](storageConditions__atmosphere.md)  <sub>0..1</sub>
     * Description: Storage atmosphere conditions
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
