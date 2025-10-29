

# Class: WorkflowRun 


_A computational processing workflow execution_





URI: [lambdaber:WorkflowRun](https://w3id.org/lambda-ber-schema/WorkflowRun)





```mermaid
 classDiagram
    class WorkflowRun
    click WorkflowRun href "../WorkflowRun/"
      NamedThing <|-- WorkflowRun
        click NamedThing href "../NamedThing/"
      
      WorkflowRun : additional_software
        
      WorkflowRun : completed_at
        
      WorkflowRun : compute_resources
        
          
    
        
        
        WorkflowRun --> "0..1" ComputeResources : compute_resources
        click ComputeResources href "../ComputeResources/"
    

        
      WorkflowRun : deposited_to_pdb
        
      WorkflowRun : description
        
      WorkflowRun : experiment_id
        
      WorkflowRun : id
        
      WorkflowRun : indexer_module
        
      WorkflowRun : integrator_module
        
      WorkflowRun : ligands_cofactors
        
      WorkflowRun : ncs_used
        
      WorkflowRun : number_of_waters
        
      WorkflowRun : outlier_rejection_method
        
      WorkflowRun : output_files
        
          
    
        
        
        WorkflowRun --> "*" DataFile : output_files
        click DataFile href "../DataFile/"
    

        
      WorkflowRun : parameters_file_path
        
      WorkflowRun : pdb_id
        
      WorkflowRun : phasing_method
        
          
    
        
        
        WorkflowRun --> "0..1" PhasingMethodEnum : phasing_method
        click PhasingMethodEnum href "../PhasingMethodEnum/"
    

        
      WorkflowRun : processing_level
        
      WorkflowRun : processing_notes
        
      WorkflowRun : processing_parameters
        
      WorkflowRun : refinement_resolution_a
        
      WorkflowRun : restraints_other
        
      WorkflowRun : scaler_module
        
      WorkflowRun : search_model_pdb_id
        
      WorkflowRun : software_name
        
      WorkflowRun : software_version
        
      WorkflowRun : started_at
        
      WorkflowRun : title
        
      WorkflowRun : tls_used
        
      WorkflowRun : validation_report_path
        
      WorkflowRun : workflow_code
        
      WorkflowRun : workflow_type
        
          
    
        
        
        WorkflowRun --> "1" WorkflowTypeEnum : workflow_type
        click WorkflowTypeEnum href "../WorkflowTypeEnum/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **WorkflowRun**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [workflow_code](workflow_code.md) | 1 <br/> [String](String.md) | Human-friendly identifier for the computational workflow run (e | direct |
| [workflow_type](workflow_type.md) | 1 <br/> [WorkflowTypeEnum](WorkflowTypeEnum.md) | Type of processing workflow | direct |
| [experiment_id](experiment_id.md) | 1 <br/> [String](String.md) | Reference to the source experiment | direct |
| [processing_level](processing_level.md) | 0..1 <br/> [Integer](Integer.md) | Processing level (0=raw, 1=corrected, 2=derived, 3=model) | direct |
| [software_name](software_name.md) | 1 <br/> [String](String.md) | Software used for processing | direct |
| [software_version](software_version.md) | 0..1 <br/> [String](String.md) | Software version | direct |
| [additional_software](additional_software.md) | 0..1 <br/> [String](String.md) | Additional software used in pipeline | direct |
| [processing_parameters](processing_parameters.md) | 0..1 <br/> [String](String.md) | Parameters used in processing | direct |
| [parameters_file_path](parameters_file_path.md) | 0..1 <br/> [String](String.md) | Path to parameters file or text of key parameters | direct |
| [indexer_module](indexer_module.md) | 0..1 <br/> [String](String.md) | Indexing module used (e | direct |
| [integrator_module](integrator_module.md) | 0..1 <br/> [String](String.md) | Integration module used | direct |
| [scaler_module](scaler_module.md) | 0..1 <br/> [String](String.md) | Scaling module used (e | direct |
| [outlier_rejection_method](outlier_rejection_method.md) | 0..1 <br/> [String](String.md) | Method for rejecting outlier reflections | direct |
| [phasing_method](phasing_method.md) | 0..1 <br/> [PhasingMethodEnum](PhasingMethodEnum.md) | Phasing method used for X-ray crystallography structure determination | direct |
| [search_model_pdb_id](search_model_pdb_id.md) | 0..1 <br/> [String](String.md) | PDB ID of search model for molecular replacement | direct |
| [tls_used](tls_used.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether TLS (Translation/Libration/Screw) refinement was used | direct |
| [ncs_used](ncs_used.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether Non-Crystallographic Symmetry restraints were used | direct |
| [restraints_other](restraints_other.md) | 0..1 <br/> [String](String.md) | Other restraints applied during refinement | direct |
| [ligands_cofactors](ligands_cofactors.md) | 0..1 <br/> [String](String.md) | Ligands or cofactors modeled in the structure | direct |
| [number_of_waters](number_of_waters.md) | 0..1 <br/> [Integer](Integer.md) | Number of water molecules modeled | direct |
| [refinement_resolution_a](refinement_resolution_a.md) | 0..1 <br/> [Float](Float.md) | Resolution cutoff used for refinement in Angstroms | direct |
| [deposited_to_pdb](deposited_to_pdb.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether structure was deposited to PDB | direct |
| [pdb_id](pdb_id.md) | 0..1 <br/> [String](String.md) | PDB accession code if deposited | direct |
| [validation_report_path](validation_report_path.md) | 0..1 <br/> [String](String.md) | Path to validation report | direct |
| [processing_notes](processing_notes.md) | 0..1 <br/> [String](String.md) | Additional notes about processing | direct |
| [compute_resources](compute_resources.md) | 0..1 <br/> [ComputeResources](ComputeResources.md) | Computational resources used | direct |
| [started_at](started_at.md) | 0..1 <br/> [String](String.md) | Workflow start time | direct |
| [completed_at](completed_at.md) | 0..1 <br/> [String](String.md) | Workflow completion time | direct |
| [output_files](output_files.md) | * <br/> [DataFile](DataFile.md) | Output files generated | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [workflow_runs](workflow_runs.md) | range | [WorkflowRun](WorkflowRun.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:WorkflowRun |
| native | lambdaber:WorkflowRun |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkflowRun
description: A computational processing workflow execution
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  workflow_code:
    name: workflow_code
    description: Human-friendly identifier for the computational workflow run (e.g.,
      'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing
      pipelines and computational provenance.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    required: true
  workflow_type:
    name: workflow_type
    description: Type of processing workflow
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: WorkflowTypeEnum
    required: true
  experiment_id:
    name: experiment_id
    description: Reference to the source experiment
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: string
    required: true
  processing_level:
    name: processing_level
    description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: integer
    minimum_value: 0
    maximum_value: 4
  software_name:
    name: software_name
    description: Software used for processing
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    required: true
  software_version:
    name: software_version
    description: Software version
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  additional_software:
    name: additional_software
    description: Additional software used in pipeline
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  processing_parameters:
    name: processing_parameters
    description: Parameters used in processing
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  parameters_file_path:
    name: parameters_file_path
    description: Path to parameters file or text of key parameters
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  indexer_module:
    name: indexer_module
    description: Indexing module used (e.g., MOSFLM, XDS)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  integrator_module:
    name: integrator_module
    description: Integration module used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  scaler_module:
    name: scaler_module
    description: Scaling module used (e.g., AIMLESS, SCALA)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  outlier_rejection_method:
    name: outlier_rejection_method
    description: Method for rejecting outlier reflections
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  phasing_method:
    name: phasing_method
    description: Phasing method used for X-ray crystallography structure determination
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: PhasingMethodEnum
  search_model_pdb_id:
    name: search_model_pdb_id
    description: PDB ID of search model for molecular replacement
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  tls_used:
    name: tls_used
    description: Whether TLS (Translation/Libration/Screw) refinement was used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: boolean
  ncs_used:
    name: ncs_used
    description: Whether Non-Crystallographic Symmetry restraints were used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: boolean
  restraints_other:
    name: restraints_other
    description: Other restraints applied during refinement
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  ligands_cofactors:
    name: ligands_cofactors
    description: Ligands or cofactors modeled in the structure
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  number_of_waters:
    name: number_of_waters
    description: Number of water molecules modeled
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: integer
  refinement_resolution_a:
    name: refinement_resolution_a
    description: Resolution cutoff used for refinement in Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: float
  deposited_to_pdb:
    name: deposited_to_pdb
    description: Whether structure was deposited to PDB
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: boolean
  pdb_id:
    name: pdb_id
    description: PDB accession code if deposited
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  validation_report_path:
    name: validation_report_path
    description: Path to validation report
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  processing_notes:
    name: processing_notes
    description: Additional notes about processing
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
  compute_resources:
    name: compute_resources
    description: Computational resources used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: ComputeResources
  started_at:
    name: started_at
    description: Workflow start time
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: string
  completed_at:
    name: completed_at
    description: Workflow completion time
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: string
  output_files:
    name: output_files
    description: Output files generated
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: DataFile
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: WorkflowRun
description: A computational processing workflow execution
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  workflow_code:
    name: workflow_code
    description: Human-friendly identifier for the computational workflow run (e.g.,
      'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing
      pipelines and computational provenance.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: workflow_code
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
    required: true
  workflow_type:
    name: workflow_type
    description: Type of processing workflow
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: workflow_type
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: WorkflowTypeEnum
    required: true
  experiment_id:
    name: experiment_id
    description: Reference to the source experiment
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: experiment_id
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
    required: true
  processing_level:
    name: processing_level
    description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: processing_level
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: integer
    minimum_value: 0
    maximum_value: 4
  software_name:
    name: software_name
    description: Software used for processing
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: software_name
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
    required: true
  software_version:
    name: software_version
    description: Software version
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: software_version
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  additional_software:
    name: additional_software
    description: Additional software used in pipeline
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: additional_software
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  processing_parameters:
    name: processing_parameters
    description: Parameters used in processing
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: processing_parameters
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  parameters_file_path:
    name: parameters_file_path
    description: Path to parameters file or text of key parameters
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: parameters_file_path
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  indexer_module:
    name: indexer_module
    description: Indexing module used (e.g., MOSFLM, XDS)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: indexer_module
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  integrator_module:
    name: integrator_module
    description: Integration module used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: integrator_module
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  scaler_module:
    name: scaler_module
    description: Scaling module used (e.g., AIMLESS, SCALA)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: scaler_module
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  outlier_rejection_method:
    name: outlier_rejection_method
    description: Method for rejecting outlier reflections
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: outlier_rejection_method
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  phasing_method:
    name: phasing_method
    description: Phasing method used for X-ray crystallography structure determination
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: phasing_method
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: PhasingMethodEnum
  search_model_pdb_id:
    name: search_model_pdb_id
    description: PDB ID of search model for molecular replacement
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: search_model_pdb_id
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  tls_used:
    name: tls_used
    description: Whether TLS (Translation/Libration/Screw) refinement was used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: tls_used
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: boolean
  ncs_used:
    name: ncs_used
    description: Whether Non-Crystallographic Symmetry restraints were used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: ncs_used
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: boolean
  restraints_other:
    name: restraints_other
    description: Other restraints applied during refinement
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: restraints_other
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  ligands_cofactors:
    name: ligands_cofactors
    description: Ligands or cofactors modeled in the structure
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: ligands_cofactors
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  number_of_waters:
    name: number_of_waters
    description: Number of water molecules modeled
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: number_of_waters
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: integer
  refinement_resolution_a:
    name: refinement_resolution_a
    description: Resolution cutoff used for refinement in Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: refinement_resolution_a
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: float
  deposited_to_pdb:
    name: deposited_to_pdb
    description: Whether structure was deposited to PDB
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: deposited_to_pdb
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: boolean
  pdb_id:
    name: pdb_id
    description: PDB accession code if deposited
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: pdb_id
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  validation_report_path:
    name: validation_report_path
    description: Path to validation report
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: validation_report_path
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  processing_notes:
    name: processing_notes
    description: Additional notes about processing
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: processing_notes
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  compute_resources:
    name: compute_resources
    description: Computational resources used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: compute_resources
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: ComputeResources
  started_at:
    name: started_at
    description: Workflow start time
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: started_at
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  completed_at:
    name: completed_at
    description: Workflow completion time
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: completed_at
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  output_files:
    name: output_files
    description: Output files generated
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: output_files
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: DataFile
    multivalued: true
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: WorkflowRun
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
    owner: WorkflowRun
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: WorkflowRun
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>