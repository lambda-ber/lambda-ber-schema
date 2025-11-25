

# Class: DataFile 


_A data file generated or used in the study_





URI: [lambdaber:DataFile](https://w3id.org/lambda-ber-schema/DataFile)





```mermaid
 classDiagram
    class DataFile
    click DataFile href "../DataFile/"
      NamedThing <|-- DataFile
        click NamedThing href "../NamedThing/"
      
      DataFile : checksum
        
      DataFile : creation_date
        
      DataFile : data_type
        
          
    
        
        
        DataFile --> "0..1" DataTypeEnum : data_type
        click DataTypeEnum href "../DataTypeEnum/"
    

        
      DataFile : description
        
      DataFile : file_format
        
          
    
        
        
        DataFile --> "1" FileFormatEnum : file_format
        click FileFormatEnum href "../FileFormatEnum/"
    

        
      DataFile : file_name
        
      DataFile : file_path
        
      DataFile : file_role
        
      DataFile : file_size_bytes
        
      DataFile : id
        
      DataFile : related_entity
        
      DataFile : storage_uri
        
      DataFile : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **DataFile**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [file_name](file_name.md) | 1 <br/> [String](String.md) | Name of the file | direct |
| [file_path](file_path.md) | 0..1 <br/> [String](String.md) | Path to the file | direct |
| [file_format](file_format.md) | 1 <br/> [FileFormatEnum](FileFormatEnum.md) | File format | direct |
| [file_size_bytes](file_size_bytes.md) | 0..1 <br/> [Integer](Integer.md) | File size in bytes | direct |
| [checksum](checksum.md) | 0..1 <br/> [String](String.md) | SHA-256 checksum for data integrity | direct |
| [creation_date](creation_date.md) | 0..1 <br/> [String](String.md) | File creation date | direct |
| [data_type](data_type.md) | 0..1 <br/> [DataTypeEnum](DataTypeEnum.md) | Type of data in the file | direct |
| [storage_uri](storage_uri.md) | 0..1 <br/> [String](String.md) | Storage URI (S3, Globus, etc | direct |
| [related_entity](related_entity.md) | 0..1 <br/> [String](String.md) | ID of the entity that owns this file | direct |
| [file_role](file_role.md) | 0..1 <br/> [String](String.md) | Role of the file (raw, intermediate, final, diagnostic, metadata) | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [data_files](data_files.md) | range | [DataFile](DataFile.md) |
| [WorkflowRun](WorkflowRun.md) | [output_files](output_files.md) | range | [DataFile](DataFile.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:DataFile |
| native | lambdaber:DataFile |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataFile
description: A data file generated or used in the study
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  file_name:
    name: file_name
    description: Name of the file
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
    - Image
    required: true
  file_path:
    name: file_path
    description: Path to the file
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
  file_format:
    name: file_format
    description: File format
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
    range: FileFormatEnum
    required: true
  file_size_bytes:
    name: file_size_bytes
    description: File size in bytes
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
    range: integer
  checksum:
    name: checksum
    description: SHA-256 checksum for data integrity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
  creation_date:
    name: creation_date
    description: File creation date
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
    range: string
  data_type:
    name: data_type
    description: Type of data in the file
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
    range: DataTypeEnum
  storage_uri:
    name: storage_uri
    description: Storage URI (S3, Globus, etc.)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
    range: string
  related_entity:
    name: related_entity
    description: ID of the entity that owns this file
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
    range: string
  file_role:
    name: file_role
    description: Role of the file (raw, intermediate, final, diagnostic, metadata)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataFile
    range: string

```
</details>

### Induced

<details>
```yaml
name: DataFile
description: A data file generated or used in the study
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  file_name:
    name: file_name
    description: Name of the file
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: file_name
    owner: DataFile
    domain_of:
    - DataFile
    - Image
    range: string
    required: true
  file_path:
    name: file_path
    description: Path to the file
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: file_path
    owner: DataFile
    domain_of:
    - DataFile
    range: string
  file_format:
    name: file_format
    description: File format
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: file_format
    owner: DataFile
    domain_of:
    - DataFile
    range: FileFormatEnum
    required: true
  file_size_bytes:
    name: file_size_bytes
    description: File size in bytes
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: file_size_bytes
    owner: DataFile
    domain_of:
    - DataFile
    range: integer
  checksum:
    name: checksum
    description: SHA-256 checksum for data integrity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: checksum
    owner: DataFile
    domain_of:
    - DataFile
    range: string
  creation_date:
    name: creation_date
    description: File creation date
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: creation_date
    owner: DataFile
    domain_of:
    - DataFile
    range: string
  data_type:
    name: data_type
    description: Type of data in the file
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: data_type
    owner: DataFile
    domain_of:
    - DataFile
    range: DataTypeEnum
  storage_uri:
    name: storage_uri
    description: Storage URI (S3, Globus, etc.)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: storage_uri
    owner: DataFile
    domain_of:
    - DataFile
    range: string
  related_entity:
    name: related_entity
    description: ID of the entity that owns this file
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: related_entity
    owner: DataFile
    domain_of:
    - DataFile
    range: string
  file_role:
    name: file_role
    description: Role of the file (raw, intermediate, final, diagnostic, metadata)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: file_role
    owner: DataFile
    domain_of:
    - DataFile
    range: string
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: DataFile
    domain_of:
    - NamedThing
    range: uriorcurie
    required: true
  title:
    name: title
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: DataFile
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: DataFile
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>