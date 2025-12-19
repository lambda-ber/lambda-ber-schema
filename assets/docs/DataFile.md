
# Class: DataFile

A data file generated or used in the study

URI: [lambdaber:DataFile](https://w3id.org/lambda-ber-schema/DataFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[NamedThing],[QuantityValue]<file_size_bytes%200..1-++[DataFile&#124;file_name:string;file_path:string%20%3F;file_format:FileFormatEnum;checksum:string%20%3F;creation_date:string%20%3F;data_type:DataTypeEnum%20%3F;storage_uri:string%20%3F;related_entity:string%20%3F;file_role:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Study]++-%20data_files%200..*>[DataFile],[WorkflowRun]-%20output_files%200..*>[DataFile],[NamedThing]^-[DataFile],[WorkflowRun],[Study])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[NamedThing],[QuantityValue]<file_size_bytes%200..1-++[DataFile&#124;file_name:string;file_path:string%20%3F;file_format:FileFormatEnum;checksum:string%20%3F;creation_date:string%20%3F;data_type:DataTypeEnum%20%3F;storage_uri:string%20%3F;related_entity:string%20%3F;file_role:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[Study]++-%20data_files%200..*>[DataFile],[WorkflowRun]-%20output_files%200..*>[DataFile],[NamedThing]^-[DataFile],[WorkflowRun],[Study])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞data_files](study__data_files.md)*  <sub>0..\*</sub>  **[DataFile](DataFile.md)**
 *  **None** *[➞output_files](workflowRun__output_files.md)*  <sub>0..\*</sub>  **[DataFile](DataFile.md)**

## Attributes


### Own

 * [➞file_name](dataFile__file_name.md)  <sub>1..1</sub>
     * Description: Name of the file
     * Range: [String](types/String.md)
 * [➞file_path](dataFile__file_path.md)  <sub>0..1</sub>
     * Description: Path to the file
     * Range: [String](types/String.md)
 * [➞file_format](dataFile__file_format.md)  <sub>1..1</sub>
     * Description: File format
     * Range: [FileFormatEnum](FileFormatEnum.md)
 * [➞file_size_bytes](dataFile__file_size_bytes.md)  <sub>0..1</sub>
     * Description: File size in bytes
     * Range: [QuantityValue](QuantityValue.md)
 * [➞checksum](dataFile__checksum.md)  <sub>0..1</sub>
     * Description: SHA-256 checksum for data integrity
     * Range: [String](types/String.md)
 * [➞creation_date](dataFile__creation_date.md)  <sub>0..1</sub>
     * Description: File creation date
     * Range: [String](types/String.md)
 * [➞data_type](dataFile__data_type.md)  <sub>0..1</sub>
     * Description: Type of data in the file
     * Range: [DataTypeEnum](DataTypeEnum.md)
 * [➞storage_uri](dataFile__storage_uri.md)  <sub>0..1</sub>
     * Description: Storage URI (S3, Globus, etc.)
     * Range: [String](types/String.md)
 * [➞related_entity](dataFile__related_entity.md)  <sub>0..1</sub>
     * Description: ID of the entity that owns this file
     * Range: [String](types/String.md)
 * [➞file_role](dataFile__file_role.md)  <sub>0..1</sub>
     * Description: Role of the file (raw, intermediate, final, diagnostic, metadata)
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
