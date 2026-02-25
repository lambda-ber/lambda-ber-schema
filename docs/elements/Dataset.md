

# Class: Dataset 


_Root container holding flat entity collections and association tables. Follows relational database design patterns for structural biology data._





URI: [lambdaber:Dataset](https://w3id.org/lambda-ber-schema/Dataset)





```mermaid
 classDiagram
    class Dataset
    click Dataset href "../Dataset/"
      NamedThing <|-- Dataset
        click NamedThing href "../NamedThing/"
      
      Dataset : data_files
        
          
    
        
        
        Dataset --> "*" DataFile : data_files
        click DataFile href "../DataFile/"
    

        
      Dataset : description
        
      Dataset : experiment_instrument_associations
        
          
    
        
        
        Dataset --> "*" ExperimentInstrumentAssociation : experiment_instrument_associations
        click ExperimentInstrumentAssociation href "../ExperimentInstrumentAssociation/"
    

        
      Dataset : experiment_runs
        
          
    
        
        
        Dataset --> "*" ExperimentRun : experiment_runs
        click ExperimentRun href "../ExperimentRun/"
    

        
      Dataset : experiment_sample_associations
        
          
    
        
        
        Dataset --> "*" ExperimentSampleAssociation : experiment_sample_associations
        click ExperimentSampleAssociation href "../ExperimentSampleAssociation/"
    

        
      Dataset : id
        
      Dataset : images
        
          
    
        
        
        Dataset --> "*" Image : images
        click Image href "../Image/"
    

        
      Dataset : instruments
        
          
    
        
        
        Dataset --> "*" Instrument : instruments
        click Instrument href "../Instrument/"
    

        
      Dataset : keywords
        
      Dataset : protein_constructs
        
          
    
        
        
        Dataset --> "*" ProteinConstruct : protein_constructs
        click ProteinConstruct href "../ProteinConstruct/"
    

        
      Dataset : sample_preparations
        
          
    
        
        
        Dataset --> "*" SamplePreparation : sample_preparations
        click SamplePreparation href "../SamplePreparation/"
    

        
      Dataset : samples
        
          
    
        
        
        Dataset --> "*" Sample : samples
        click Sample href "../Sample/"
    

        
      Dataset : studies
        
          
    
        
        
        Dataset --> "*" Study : studies
        click Study href "../Study/"
    

        
      Dataset : study_experiment_associations
        
          
    
        
        
        Dataset --> "*" StudyExperimentAssociation : study_experiment_associations
        click StudyExperimentAssociation href "../StudyExperimentAssociation/"
    

        
      Dataset : study_sample_associations
        
          
    
        
        
        Dataset --> "*" StudySampleAssociation : study_sample_associations
        click StudySampleAssociation href "../StudySampleAssociation/"
    

        
      Dataset : study_workflow_associations
        
          
    
        
        
        Dataset --> "*" StudyWorkflowAssociation : study_workflow_associations
        click StudyWorkflowAssociation href "../StudyWorkflowAssociation/"
    

        
      Dataset : title
        
      Dataset : workflow_experiment_associations
        
          
    
        
        
        Dataset --> "*" WorkflowExperimentAssociation : workflow_experiment_associations
        click WorkflowExperimentAssociation href "../WorkflowExperimentAssociation/"
    

        
      Dataset : workflow_input_associations
        
          
    
        
        
        Dataset --> "*" WorkflowInputAssociation : workflow_input_associations
        click WorkflowInputAssociation href "../WorkflowInputAssociation/"
    

        
      Dataset : workflow_output_associations
        
          
    
        
        
        Dataset --> "*" WorkflowOutputAssociation : workflow_output_associations
        click WorkflowOutputAssociation href "../WorkflowOutputAssociation/"
    

        
      Dataset : workflow_runs
        
          
    
        
        
        Dataset --> "*" WorkflowRun : workflow_runs
        click WorkflowRun href "../WorkflowRun/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **Dataset**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [keywords](keywords.md) | * <br/> [String](String.md) | Keywords or tags describing the dataset for search and categorization | direct |
| [studies](studies.md) | * <br/> [Study](Study.md) | All studies in this dataset | direct |
| [instruments](instruments.md) | * <br/> [Instrument](Instrument.md) | All instruments used across studies | direct |
| [protein_constructs](protein_constructs.md) | * <br/> [ProteinConstruct](ProteinConstruct.md) | All protein constructs | direct |
| [samples](samples.md) | * <br/> [Sample](Sample.md) | All samples across all studies | direct |
| [sample_preparations](sample_preparations.md) | * <br/> [SamplePreparation](SamplePreparation.md) | All sample preparations | direct |
| [experiment_runs](experiment_runs.md) | * <br/> [ExperimentRun](ExperimentRun.md) | All experiment runs (data collection sessions) | direct |
| [workflow_runs](workflow_runs.md) | * <br/> [WorkflowRun](WorkflowRun.md) | All workflow runs (computational processing) | direct |
| [data_files](data_files.md) | * <br/> [DataFile](DataFile.md) | All data files | direct |
| [images](images.md) | * <br/> [Image](Image.md) | All images | direct |
| [study_sample_associations](study_sample_associations.md) | * <br/> [StudySampleAssociation](StudySampleAssociation.md) | Links between studies and samples (M:N) | direct |
| [study_experiment_associations](study_experiment_associations.md) | * <br/> [StudyExperimentAssociation](StudyExperimentAssociation.md) | Links between studies and experiments (M:N) | direct |
| [study_workflow_associations](study_workflow_associations.md) | * <br/> [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | Links between studies and workflows (M:N) | direct |
| [experiment_sample_associations](experiment_sample_associations.md) | * <br/> [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | Links between experiments and samples (M:N with role) | direct |
| [experiment_instrument_associations](experiment_instrument_associations.md) | * <br/> [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | Links between experiments and instruments (M:N) | direct |
| [workflow_experiment_associations](workflow_experiment_associations.md) | * <br/> [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md) | Links between workflows and source experiments (M:N) | direct |
| [workflow_input_associations](workflow_input_associations.md) | * <br/> [WorkflowInputAssociation](WorkflowInputAssociation.md) | Links between workflows and input files | direct |
| [workflow_output_associations](workflow_output_associations.md) | * <br/> [WorkflowOutputAssociation](WorkflowOutputAssociation.md) | Links between workflows and output files | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:Dataset |
| native | lambdaber:Dataset |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Dataset
description: Root container holding flat entity collections and association tables.
  Follows relational database design patterns for structural biology data.
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  keywords:
    name: keywords
    description: Keywords or tags describing the dataset for search and categorization
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    - Study
    range: string
    multivalued: true
  studies:
    name: studies
    description: All studies in this dataset
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: Study
    multivalued: true
    inlined: true
    inlined_as_list: true
  instruments:
    name: instruments
    description: All instruments used across studies
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: Instrument
    multivalued: true
    inlined: true
    inlined_as_list: true
  protein_constructs:
    name: protein_constructs
    description: All protein constructs
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: ProteinConstruct
    multivalued: true
    inlined: true
    inlined_as_list: true
  samples:
    name: samples
    description: All samples across all studies
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: Sample
    multivalued: true
    inlined: true
    inlined_as_list: true
  sample_preparations:
    name: sample_preparations
    description: All sample preparations
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: SamplePreparation
    multivalued: true
    inlined: true
    inlined_as_list: true
  experiment_runs:
    name: experiment_runs
    description: All experiment runs (data collection sessions)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: ExperimentRun
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_runs:
    name: workflow_runs
    description: All workflow runs (computational processing)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: WorkflowRun
    multivalued: true
    inlined: true
    inlined_as_list: true
  data_files:
    name: data_files
    description: All data files
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: DataFile
    multivalued: true
    inlined: true
    inlined_as_list: true
  images:
    name: images
    description: All images
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: Image
    multivalued: true
    inlined: true
    inlined_as_list: true
  study_sample_associations:
    name: study_sample_associations
    description: Links between studies and samples (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: StudySampleAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  study_experiment_associations:
    name: study_experiment_associations
    description: Links between studies and experiments (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: StudyExperimentAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  study_workflow_associations:
    name: study_workflow_associations
    description: Links between studies and workflows (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: StudyWorkflowAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  experiment_sample_associations:
    name: experiment_sample_associations
    description: Links between experiments and samples (M:N with role)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: ExperimentSampleAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  experiment_instrument_associations:
    name: experiment_instrument_associations
    description: Links between experiments and instruments (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: ExperimentInstrumentAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_experiment_associations:
    name: workflow_experiment_associations
    description: Links between workflows and source experiments (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: WorkflowExperimentAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_input_associations:
    name: workflow_input_associations
    description: Links between workflows and input files
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: WorkflowInputAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_output_associations:
    name: workflow_output_associations
    description: Links between workflows and output files
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Dataset
    range: WorkflowOutputAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Dataset
description: Root container holding flat entity collections and association tables.
  Follows relational database design patterns for structural biology data.
from_schema: https://w3id.org/lambda-ber-schema/
is_a: NamedThing
attributes:
  keywords:
    name: keywords
    description: Keywords or tags describing the dataset for search and categorization
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: keywords
    owner: Dataset
    domain_of:
    - Dataset
    - Study
    range: string
    multivalued: true
  studies:
    name: studies
    description: All studies in this dataset
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: studies
    owner: Dataset
    domain_of:
    - Dataset
    range: Study
    multivalued: true
    inlined: true
    inlined_as_list: true
  instruments:
    name: instruments
    description: All instruments used across studies
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: instruments
    owner: Dataset
    domain_of:
    - Dataset
    range: Instrument
    multivalued: true
    inlined: true
    inlined_as_list: true
  protein_constructs:
    name: protein_constructs
    description: All protein constructs
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: protein_constructs
    owner: Dataset
    domain_of:
    - Dataset
    range: ProteinConstruct
    multivalued: true
    inlined: true
    inlined_as_list: true
  samples:
    name: samples
    description: All samples across all studies
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: samples
    owner: Dataset
    domain_of:
    - Dataset
    range: Sample
    multivalued: true
    inlined: true
    inlined_as_list: true
  sample_preparations:
    name: sample_preparations
    description: All sample preparations
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: sample_preparations
    owner: Dataset
    domain_of:
    - Dataset
    range: SamplePreparation
    multivalued: true
    inlined: true
    inlined_as_list: true
  experiment_runs:
    name: experiment_runs
    description: All experiment runs (data collection sessions)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: experiment_runs
    owner: Dataset
    domain_of:
    - Dataset
    range: ExperimentRun
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_runs:
    name: workflow_runs
    description: All workflow runs (computational processing)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: workflow_runs
    owner: Dataset
    domain_of:
    - Dataset
    range: WorkflowRun
    multivalued: true
    inlined: true
    inlined_as_list: true
  data_files:
    name: data_files
    description: All data files
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: data_files
    owner: Dataset
    domain_of:
    - Dataset
    range: DataFile
    multivalued: true
    inlined: true
    inlined_as_list: true
  images:
    name: images
    description: All images
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: images
    owner: Dataset
    domain_of:
    - Dataset
    range: Image
    multivalued: true
    inlined: true
    inlined_as_list: true
  study_sample_associations:
    name: study_sample_associations
    description: Links between studies and samples (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: study_sample_associations
    owner: Dataset
    domain_of:
    - Dataset
    range: StudySampleAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  study_experiment_associations:
    name: study_experiment_associations
    description: Links between studies and experiments (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: study_experiment_associations
    owner: Dataset
    domain_of:
    - Dataset
    range: StudyExperimentAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  study_workflow_associations:
    name: study_workflow_associations
    description: Links between studies and workflows (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: study_workflow_associations
    owner: Dataset
    domain_of:
    - Dataset
    range: StudyWorkflowAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  experiment_sample_associations:
    name: experiment_sample_associations
    description: Links between experiments and samples (M:N with role)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: experiment_sample_associations
    owner: Dataset
    domain_of:
    - Dataset
    range: ExperimentSampleAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  experiment_instrument_associations:
    name: experiment_instrument_associations
    description: Links between experiments and instruments (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: experiment_instrument_associations
    owner: Dataset
    domain_of:
    - Dataset
    range: ExperimentInstrumentAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_experiment_associations:
    name: workflow_experiment_associations
    description: Links between workflows and source experiments (M:N)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: workflow_experiment_associations
    owner: Dataset
    domain_of:
    - Dataset
    range: WorkflowExperimentAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_input_associations:
    name: workflow_input_associations
    description: Links between workflows and input files
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: workflow_input_associations
    owner: Dataset
    domain_of:
    - Dataset
    range: WorkflowInputAssociation
    multivalued: true
    inlined: true
    inlined_as_list: true
  workflow_output_associations:
    name: workflow_output_associations
    description: Links between workflows and output files
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: workflow_output_associations
    owner: Dataset
    domain_of:
    - Dataset
    range: WorkflowOutputAssociation
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
    owner: Dataset
    domain_of:
    - NamedThing
    - Attribute
    range: uriorcurie
    required: true
  title:
    name: title
    description: A human-readable name or title for this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: Dataset
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: Dataset
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string
tree_root: true

```
</details>