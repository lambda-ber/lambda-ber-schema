

# Class: MotionCorrectionParameters 


_Parameters specific to motion correction workflows_





URI: [lambda:MotionCorrectionParameters](http://w3id.org/lambda/MotionCorrectionParameters)





```mermaid
 classDiagram
    class MotionCorrectionParameters
    click MotionCorrectionParameters href "../MotionCorrectionParameters/"
      AttributeGroup <|-- MotionCorrectionParameters
        click AttributeGroup href "../AttributeGroup/"
      
      MotionCorrectionParameters : anisotropic_correction
        
      MotionCorrectionParameters : bfactor_dose_weighting
        
          
    
        
        
        MotionCorrectionParameters --> "0..1" QuantityValue : bfactor_dose_weighting
        click QuantityValue href "../QuantityValue/"
    

        
      MotionCorrectionParameters : binning
        
          
    
        
        
        MotionCorrectionParameters --> "0..1" QuantityValue : binning
        click QuantityValue href "../QuantityValue/"
    

        
      MotionCorrectionParameters : description
        
      MotionCorrectionParameters : dose_weighting
        
      MotionCorrectionParameters : drift_total
        
          
    
        
        
        MotionCorrectionParameters --> "0..1" QuantityValue : drift_total
        click QuantityValue href "../QuantityValue/"
    

        
      MotionCorrectionParameters : frame_grouping
        
          
    
        
        
        MotionCorrectionParameters --> "0..1" QuantityValue : frame_grouping
        click QuantityValue href "../QuantityValue/"
    

        
      MotionCorrectionParameters : output_binning
        
          
    
        
        
        MotionCorrectionParameters --> "0..1" QuantityValue : output_binning
        click QuantityValue href "../QuantityValue/"
    

        
      MotionCorrectionParameters : patch_size
        
          
    
        
        
        MotionCorrectionParameters --> "0..1" QuantityValue : patch_size
        click QuantityValue href "../QuantityValue/"
    

        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * **MotionCorrectionParameters**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [patch_size](patch_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Patch size for local motion correction | direct |
| [binning](binning.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Binning factor applied during motion correction | direct |
| [dose_weighting](dose_weighting.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether dose weighting was applied | direct |
| [bfactor_dose_weighting](bfactor_dose_weighting.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | B-factor for dose weighting, typically specified in Angstroms squared | direct |
| [anisotropic_correction](anisotropic_correction.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether anisotropic motion correction was applied | direct |
| [frame_grouping](frame_grouping.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Number of frames grouped together | direct |
| [output_binning](output_binning.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Output binning factor | direct |
| [drift_total](drift_total.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total drift, typically specified in Angstroms | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WorkflowRun](WorkflowRun.md) | [motion_correction_params](motion_correction_params.md) | range | [MotionCorrectionParameters](MotionCorrectionParameters.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:MotionCorrectionParameters |
| native | lambda:MotionCorrectionParameters |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MotionCorrectionParameters
description: Parameters specific to motion correction workflows
from_schema: http://w3id.org/lambda/
is_a: AttributeGroup
attributes:
  patch_size:
    name: patch_size
    description: Patch size for local motion correction
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  binning:
    name: binning
    description: Binning factor applied during motion correction. This must be a positive
      float value (e.g., 1, 1.5, 2, 3).
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  dose_weighting:
    name: dose_weighting
    description: Whether dose weighting was applied
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - MotionCorrectionParameters
    range: boolean
  bfactor_dose_weighting:
    name: bfactor_dose_weighting
    description: B-factor for dose weighting, typically specified in Angstroms squared.
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  anisotropic_correction:
    name: anisotropic_correction
    description: Whether anisotropic motion correction was applied
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - MotionCorrectionParameters
    range: boolean
  frame_grouping:
    name: frame_grouping
    description: Number of frames grouped together
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  output_binning:
    name: output_binning
    description: Output binning factor. This must be a positive float value (e.g.,
      1, 1.5, 2, 3).
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  drift_total:
    name: drift_total
    description: Total drift, typically specified in Angstroms. Data providers may
      specify alternative units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: MotionCorrectionParameters
description: Parameters specific to motion correction workflows
from_schema: http://w3id.org/lambda/
is_a: AttributeGroup
attributes:
  patch_size:
    name: patch_size
    description: Patch size for local motion correction
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: patch_size
    owner: MotionCorrectionParameters
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  binning:
    name: binning
    description: Binning factor applied during motion correction. This must be a positive
      float value (e.g., 1, 1.5, 2, 3).
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: binning
    owner: MotionCorrectionParameters
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  dose_weighting:
    name: dose_weighting
    description: Whether dose weighting was applied
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: dose_weighting
    owner: MotionCorrectionParameters
    domain_of:
    - MotionCorrectionParameters
    range: boolean
  bfactor_dose_weighting:
    name: bfactor_dose_weighting
    description: B-factor for dose weighting, typically specified in Angstroms squared.
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: bfactor_dose_weighting
    owner: MotionCorrectionParameters
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  anisotropic_correction:
    name: anisotropic_correction
    description: Whether anisotropic motion correction was applied
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: anisotropic_correction
    owner: MotionCorrectionParameters
    domain_of:
    - MotionCorrectionParameters
    range: boolean
  frame_grouping:
    name: frame_grouping
    description: Number of frames grouped together
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: frame_grouping
    owner: MotionCorrectionParameters
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  output_binning:
    name: output_binning
    description: Output binning factor. This must be a positive float value (e.g.,
      1, 1.5, 2, 3).
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: output_binning
    owner: MotionCorrectionParameters
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  drift_total:
    name: drift_total
    description: Total drift, typically specified in Angstroms. Data providers may
      specify alternative units by including the unit in the QuantityValue.
    from_schema: http://w3id.org/lambda/
    rank: 1000
    alias: drift_total
    owner: MotionCorrectionParameters
    domain_of:
    - MotionCorrectionParameters
    range: QuantityValue
    inlined: true
  description:
    name: description
    from_schema: http://w3id.org/lambda/
    alias: description
    owner: MotionCorrectionParameters
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>