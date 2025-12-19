

# Class: OpticalImage 


_Visible light optical microscopy or photography image_





URI: [lambdaber:OpticalImage](https://w3id.org/lambda-ber-schema/OpticalImage)





```mermaid
 classDiagram
    class OpticalImage
    click OpticalImage href "../OpticalImage/"
      Image2D <|-- OpticalImage
        click Image2D href "../Image2D/"
      
      OpticalImage : acquisition_date
        
      OpticalImage : astigmatism
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : astigmatism
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : color_channels
        
      OpticalImage : contrast_method
        
      OpticalImage : defocus
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : defocus
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : description
        
      OpticalImage : dimensions_x
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : dimensions_x
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : dimensions_y
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : dimensions_y
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : dose
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : dose
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : exposure_time
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : exposure_time
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : file_name
        
      OpticalImage : id
        
      OpticalImage : illumination_type
        
          
    
        
        
        OpticalImage --> "0..1" IlluminationTypeEnum : illumination_type
        click IlluminationTypeEnum href "../IlluminationTypeEnum/"
    

        
      OpticalImage : magnification
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : magnification
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : numerical_aperture
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : numerical_aperture
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : pixel_size
        
          
    
        
        
        OpticalImage --> "0..1" QuantityValue : pixel_size
        click QuantityValue href "../QuantityValue/"
    

        
      OpticalImage : title
        
      OpticalImage : white_balance
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [Image](Image.md)
        * [Image2D](Image2D.md)
            * **OpticalImage**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [illumination_type](illumination_type.md) | 0..1 <br/> [IlluminationTypeEnum](IlluminationTypeEnum.md) | Type of illumination (brightfield, darkfield, phase contrast, DIC) | direct |
| [magnification](magnification.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Optical magnification factor | direct |
| [numerical_aperture](numerical_aperture.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Numerical aperture of the objective lens | direct |
| [color_channels](color_channels.md) | * <br/> [String](String.md) | Color channels present (e | direct |
| [white_balance](white_balance.md) | 0..1 <br/> [String](String.md) | White balance settings | direct |
| [contrast_method](contrast_method.md) | 0..1 <br/> [String](String.md) | Contrast enhancement method used | direct |
| [defocus](defocus.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Defocus value, typically specified in micrometers | [Image2D](Image2D.md) |
| [astigmatism](astigmatism.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Astigmatism value, typically specified in Angstroms | [Image2D](Image2D.md) |
| [file_name](file_name.md) | 1 <br/> [String](String.md) | Image file name | [Image](Image.md) |
| [acquisition_date](acquisition_date.md) | 0..1 <br/> [String](String.md) | Date image was acquired | [Image](Image.md) |
| [pixel_size](pixel_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Pixel size, typically specified in Angstroms | [Image](Image.md) |
| [dimensions_x](dimensions_x.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Image width, typically specified in pixels | [Image](Image.md) |
| [dimensions_y](dimensions_y.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Image height, typically specified in pixels | [Image](Image.md) |
| [exposure_time](exposure_time.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Exposure time, typically specified in seconds | [Image](Image.md) |
| [dose](dose.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Electron dose in e-/Å² | [Image](Image.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:OpticalImage |
| native | lambdaber:OpticalImage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OpticalImage
description: Visible light optical microscopy or photography image
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image2D
attributes:
  illumination_type:
    name: illumination_type
    description: Type of illumination (brightfield, darkfield, phase contrast, DIC)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - OpticalImage
    range: IlluminationTypeEnum
  magnification:
    name: magnification
    description: Optical magnification factor. Data providers may specify the unit
      (e.g., times, X) in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - ExperimentRun
    - OpticalImage
    range: QuantityValue
    inlined: true
  numerical_aperture:
    name: numerical_aperture
    description: Numerical aperture of the objective lens. Data providers may include
      unit information in the QuantityValue if needed.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - OpticalImage
    range: QuantityValue
    inlined: true
  color_channels:
    name: color_channels
    description: Color channels present (e.g., RGB, grayscale)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - OpticalImage
    range: string
    multivalued: true
  white_balance:
    name: white_balance
    description: White balance settings
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - OpticalImage
    range: string
  contrast_method:
    name: contrast_method
    description: Contrast enhancement method used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - OpticalImage
    range: string

```
</details>

### Induced

<details>
```yaml
name: OpticalImage
description: Visible light optical microscopy or photography image
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image2D
attributes:
  illumination_type:
    name: illumination_type
    description: Type of illumination (brightfield, darkfield, phase contrast, DIC)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: illumination_type
    owner: OpticalImage
    domain_of:
    - OpticalImage
    range: IlluminationTypeEnum
  magnification:
    name: magnification
    description: Optical magnification factor. Data providers may specify the unit
      (e.g., times, X) in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: magnification
    owner: OpticalImage
    domain_of:
    - ExperimentRun
    - OpticalImage
    range: QuantityValue
    inlined: true
  numerical_aperture:
    name: numerical_aperture
    description: Numerical aperture of the objective lens. Data providers may include
      unit information in the QuantityValue if needed.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: numerical_aperture
    owner: OpticalImage
    domain_of:
    - OpticalImage
    range: QuantityValue
    inlined: true
  color_channels:
    name: color_channels
    description: Color channels present (e.g., RGB, grayscale)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: color_channels
    owner: OpticalImage
    domain_of:
    - OpticalImage
    range: string
    multivalued: true
  white_balance:
    name: white_balance
    description: White balance settings
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: white_balance
    owner: OpticalImage
    domain_of:
    - OpticalImage
    range: string
  contrast_method:
    name: contrast_method
    description: Contrast enhancement method used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: contrast_method
    owner: OpticalImage
    domain_of:
    - OpticalImage
    range: string
  defocus:
    name: defocus
    description: Defocus value, typically specified in micrometers. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: defocus
    owner: OpticalImage
    domain_of:
    - Image2D
    range: QuantityValue
    inlined: true
  astigmatism:
    name: astigmatism
    description: Astigmatism value, typically specified in Angstroms. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: astigmatism
    owner: OpticalImage
    domain_of:
    - Image2D
    range: QuantityValue
    inlined: true
  file_name:
    name: file_name
    description: Image file name
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: file_name
    owner: OpticalImage
    domain_of:
    - DataFile
    - Image
    range: string
    required: true
  acquisition_date:
    name: acquisition_date
    description: Date image was acquired
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: acquisition_date
    owner: OpticalImage
    domain_of:
    - Image
    range: string
  pixel_size:
    name: pixel_size
    description: Pixel size, typically specified in Angstroms. Data providers may
      specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: pixel_size
    owner: OpticalImage
    domain_of:
    - Image
    - RefinementParameters
    range: QuantityValue
    inlined: true
  dimensions_x:
    name: dimensions_x
    description: Image width, typically specified in pixels. Data providers may specify
      alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: dimensions_x
    owner: OpticalImage
    domain_of:
    - Image
    range: QuantityValue
    inlined: true
  dimensions_y:
    name: dimensions_y
    description: Image height, typically specified in pixels. Data providers may specify
      alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: dimensions_y
    owner: OpticalImage
    domain_of:
    - Image
    range: QuantityValue
    inlined: true
  exposure_time:
    name: exposure_time
    description: Exposure time, typically specified in seconds. Data providers may
      specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: exposure_time
    owner: OpticalImage
    domain_of:
    - ExperimentRun
    - Image
    - ExperimentalConditions
    range: QuantityValue
    inlined: true
  dose:
    name: dose
    description: Electron dose in e-/Å²
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: dose
    owner: OpticalImage
    domain_of:
    - Image
    - Micrograph
    range: QuantityValue
    inlined: true
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: OpticalImage
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
    owner: OpticalImage
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: OpticalImage
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>