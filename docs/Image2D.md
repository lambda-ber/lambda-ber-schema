

# Class: Image2D 


_A 2D image (micrograph, diffraction pattern)_





URI: [lambdaber:Image2D](https://w3id.org/lambda-ber-schema/Image2D)





```mermaid
 classDiagram
    class Image2D
    click Image2D href "../Image2D/"
      Image <|-- Image2D
        click Image href "../Image/"
      

      Image2D <|-- Movie
        click Movie href "../Movie/"
      Image2D <|-- Micrograph
        click Micrograph href "../Micrograph/"
      Image2D <|-- FluorescenceImage
        click FluorescenceImage href "../FluorescenceImage/"
      Image2D <|-- OpticalImage
        click OpticalImage href "../OpticalImage/"
      Image2D <|-- XRFImage
        click XRFImage href "../XRFImage/"
      

      Image2D : acquisition_date
        
      Image2D : astigmatism
        
      Image2D : defocus
        
      Image2D : description
        
      Image2D : dimensions_x
        
      Image2D : dimensions_y
        
      Image2D : dose
        
      Image2D : exposure_time
        
      Image2D : file_name
        
      Image2D : id
        
      Image2D : pixel_size
        
      Image2D : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [Image](Image.md)
        * **Image2D**
            * [Movie](Movie.md)
            * [Micrograph](Micrograph.md)
            * [FluorescenceImage](FluorescenceImage.md)
            * [OpticalImage](OpticalImage.md)
            * [XRFImage](XRFImage.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [defocus](defocus.md) | 0..1 <br/> [Float](Float.md) | Defocus value in micrometers | direct |
| [astigmatism](astigmatism.md) | 0..1 <br/> [Float](Float.md) | Astigmatism value in Angstroms | direct |
| [file_name](file_name.md) | 1 <br/> [String](String.md) | Image file name | [Image](Image.md) |
| [acquisition_date](acquisition_date.md) | 0..1 <br/> [String](String.md) | Date image was acquired | [Image](Image.md) |
| [pixel_size](pixel_size.md) | 0..1 <br/> [Float](Float.md) | Pixel size in Angstroms | [Image](Image.md) |
| [dimensions_x](dimensions_x.md) | 0..1 <br/> [Integer](Integer.md) | Image width in pixels | [Image](Image.md) |
| [dimensions_y](dimensions_y.md) | 0..1 <br/> [Integer](Integer.md) | Image height in pixels | [Image](Image.md) |
| [exposure_time](exposure_time.md) | 0..1 <br/> [Float](Float.md) | Exposure time in seconds | [Image](Image.md) |
| [dose](dose.md) | 0..1 <br/> [Float](Float.md) | Electron dose in e-/Å² | [Image](Image.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:Image2D |
| native | lambdaber:Image2D |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Image2D
description: A 2D image (micrograph, diffraction pattern)
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image
attributes:
  defocus:
    name: defocus
    description: Defocus value in micrometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Image2D
    range: float
  astigmatism:
    name: astigmatism
    description: Astigmatism value in Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - Image2D
    range: float

```
</details>

### Induced

<details>
```yaml
name: Image2D
description: A 2D image (micrograph, diffraction pattern)
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image
attributes:
  defocus:
    name: defocus
    description: Defocus value in micrometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: defocus
    owner: Image2D
    domain_of:
    - Image2D
    range: float
  astigmatism:
    name: astigmatism
    description: Astigmatism value in Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: astigmatism
    owner: Image2D
    domain_of:
    - Image2D
    range: float
  file_name:
    name: file_name
    description: Image file name
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: file_name
    owner: Image2D
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
    owner: Image2D
    domain_of:
    - Image
    range: string
  pixel_size:
    name: pixel_size
    description: Pixel size in Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: pixel_size
    owner: Image2D
    domain_of:
    - Image
    - RefinementParameters
    range: float
  dimensions_x:
    name: dimensions_x
    description: Image width in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: dimensions_x
    owner: Image2D
    domain_of:
    - Image
    range: integer
  dimensions_y:
    name: dimensions_y
    description: Image height in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: dimensions_y
    owner: Image2D
    domain_of:
    - Image
    range: integer
  exposure_time:
    name: exposure_time
    description: Exposure time in seconds
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: exposure_time
    owner: Image2D
    domain_of:
    - Image
    - ExperimentalConditions
    range: float
  dose:
    name: dose
    description: Electron dose in e-/Å²
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: dose
    owner: Image2D
    domain_of:
    - Image
    - Micrograph
    range: float
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: Image2D
    domain_of:
    - NamedThing
    range: uriorcurie
    required: true
  title:
    name: title
    description: A human-readable name or title for this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: Image2D
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: Image2D
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>