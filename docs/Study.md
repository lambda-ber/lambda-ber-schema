

# Class: Study 


_A focused research investigation that groups related samples, experiments, and data collection around a specific biological question or hypothesis_





URI: [lambdaber:Study](https://w3id.org/lambda-ber-schema/Study)





```mermaid
 classDiagram
    class Study
    click Study href "../Study/"
      NamedThing <|-- Study
        click NamedThing href "../NamedThing/"
      
      Study : data_files
        
          
    
        
        
        Study --> "*" DataFile : data_files
        click DataFile href "../DataFile/"
    

        
      Study : description
        
      Study : id
        
      Study : images
        
          
    
        
        
        Study --> "*" Image : images
        click Image href "../Image/"
    

        
      Study : instrument_runs
        
          
    
        
        
        Study --> "*" ExperimentRun : instrument_runs
        click ExperimentRun href "../ExperimentRun/"
    

        
      Study : sample_preparations
        
          
    
        
        
        Study --> "*" SamplePreparation : sample_preparations
        click SamplePreparation href "../SamplePreparation/"
    

        
      Study : samples
        
          
    
        
        
        Study --> "*" Sample : samples
        click Sample href "../Sample/"
    

        
      Study : title
        
      Study : workflow_runs
        
          
    
        
        
        Study --> "*" WorkflowRun : workflow_runs
        click WorkflowRun href "../WorkflowRun/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **Study**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [samples](samples.md) | * <br/> [Sample](Sample.md) |  | direct |
| [sample_preparations](sample_preparations.md) | * <br/> [SamplePreparation](SamplePreparation.md) |  | direct |
| [instrument_runs](instrument_runs.md) | * <br/> [ExperimentRun](ExperimentRun.md) |  | direct |
| [workflow_runs](workflow_runs.md) | * <br/> [WorkflowRun](WorkflowRun.md) |  | direct |
| [data_files](data_files.md) | * <br/> [DataFile](DataFile.md) |  | direct |
| [images](images.md) | * <br/> [Image](Image.md) |  | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [studies](studies.md) | range | [Study](Study.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:Study |
| native | lambdaber:Study |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Study
description: A focused research investigation that groups related samples, experiments,
  and data collection around a specific biological question or hypothesis
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  samples:
    name: samples
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Study
    range: Sample
    multivalued: true
    inlined: true
    inlined_as_list: true
  sample_preparations:
    name: sample_preparations
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Study
    range: SamplePreparation
    multivalued: true
    inlined: true
    inlined_as_list: true
  instrument_runs:
    name: instrument_runs
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Study
    range: ExperimentRun
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_runs:
    name: workflow_runs
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Study
    range: WorkflowRun
    multivalued: true
    inlined: true
    inlined_as_list: true
  data_files:
    name: data_files
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Study
    range: DataFile
    multivalued: true
    inlined: true
    inlined_as_list: true
  images:
    name: images
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Study
    range: Image
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: Study
description: A focused research investigation that groups related samples, experiments,
  and data collection around a specific biological question or hypothesis
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  samples:
    name: samples
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: samples
    owner: Study
    domain_of:
    - Study
    range: Sample
    multivalued: true
    inlined: true
    inlined_as_list: true
  sample_preparations:
    name: sample_preparations
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: sample_preparations
    owner: Study
    domain_of:
    - Study
    range: SamplePreparation
    multivalued: true
    inlined: true
    inlined_as_list: true
  instrument_runs:
    name: instrument_runs
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: instrument_runs
    owner: Study
    domain_of:
    - Study
    range: ExperimentRun
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_runs:
    name: workflow_runs
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: workflow_runs
    owner: Study
    domain_of:
    - Study
    range: WorkflowRun
    multivalued: true
    inlined: true
    inlined_as_list: true
  data_files:
    name: data_files
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: data_files
    owner: Study
    domain_of:
    - Study
    range: DataFile
    multivalued: true
    inlined: true
    inlined_as_list: true
  images:
    name: images
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: images
    owner: Study
    domain_of:
    - Study
    range: Image
    multivalued: true
    inlined: true
    inlined_as_list: true
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: Study
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
    owner: Study
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: Study
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>