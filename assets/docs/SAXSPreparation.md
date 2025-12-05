
# Class: SAXSPreparation

SAXS/WAXS specific preparation

URI: [lambdaber:SAXSPreparation](https://w3id.org/lambda-ber-schema/SAXSPreparation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation],[TechniqueSpecificPreparation]^-[SAXSPreparation&#124;concentration_series:float%20*;buffer_matching_protocol:string%20%3F;sample_cell_type:string%20%3F;cell_path_length:float%20%3F;temperature_control:string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[TechniqueSpecificPreparation],[TechniqueSpecificPreparation]^-[SAXSPreparation&#124;concentration_series:float%20*;buffer_matching_protocol:string%20%3F;sample_cell_type:string%20%3F;cell_path_length:float%20%3F;temperature_control:string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) - Base class for technique-specific preparation details

## Attributes


### Own

 * [➞concentration_series](sAXSPreparation__concentration_series.md)  <sub>0..\*</sub>
     * Description: Concentration values for series measurements
     * Range: [Float](types/Float.md)
 * [➞buffer_matching_protocol](sAXSPreparation__buffer_matching_protocol.md)  <sub>0..1</sub>
     * Description: Protocol for buffer matching
     * Range: [String](types/String.md)
 * [➞sample_cell_type](sAXSPreparation__sample_cell_type.md)  <sub>0..1</sub>
     * Description: Type of sample cell used
     * Range: [String](types/String.md)
 * [➞cell_path_length](sAXSPreparation__cell_path_length.md)  <sub>0..1</sub>
     * Description: Path length in mm
     * Range: [Float](types/Float.md)
 * [➞temperature_control](sAXSPreparation__temperature_control.md)  <sub>0..1</sub>
     * Description: Temperature control settings
     * Range: [String](types/String.md)

### Inherited from TechniqueSpecificPreparation:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
