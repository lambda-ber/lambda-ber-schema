

# Class: FluorescenceImage 


_Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling_





URI: [lambdaber:FluorescenceImage](https://w3id.org/lambda-ber-schema/FluorescenceImage)





```mermaid
 classDiagram
    class FluorescenceImage
    click FluorescenceImage href "../FluorescenceImage/"
      Image2D <|-- FluorescenceImage
        click Image2D href "../Image2D/"
      
      FluorescenceImage : acquisition_date
        
      FluorescenceImage : astigmatism
        
      FluorescenceImage : channel_name
        
      FluorescenceImage : defocus
        
      FluorescenceImage : description
        
      FluorescenceImage : dimensions_x
        
      FluorescenceImage : dimensions_y
        
      FluorescenceImage : dose
        
      FluorescenceImage : emission_filter
        
      FluorescenceImage : emission_wavelength
        
      FluorescenceImage : excitation_filter
        
      FluorescenceImage : excitation_wavelength
        
      FluorescenceImage : exposure_time
        
      FluorescenceImage : file_name
        
      FluorescenceImage : fluorophore
        
      FluorescenceImage : id
        
      FluorescenceImage : laser_power
        
      FluorescenceImage : pinhole_size
        
      FluorescenceImage : pixel_size
        
      FluorescenceImage : quantum_yield
        
      FluorescenceImage : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [Image](Image.md)
        * [Image2D](Image2D.md)
            * **FluorescenceImage**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [excitation_wavelength](excitation_wavelength.md) | 0..1 <br/> [Float](Float.md) | Excitation wavelength in nanometers | direct |
| [emission_wavelength](emission_wavelength.md) | 0..1 <br/> [Float](Float.md) | Emission wavelength in nanometers | direct |
| [excitation_filter](excitation_filter.md) | 0..1 <br/> [String](String.md) | Specifications of the excitation filter | direct |
| [emission_filter](emission_filter.md) | 0..1 <br/> [String](String.md) | Specifications of the emission filter | direct |
| [fluorophore](fluorophore.md) | 0..1 <br/> [String](String.md) | Name or type of fluorophore used | direct |
| [channel_name](channel_name.md) | 0..1 <br/> [String](String.md) | Name of the fluorescence channel (e | direct |
| [laser_power](laser_power.md) | 0..1 <br/> [Float](Float.md) | Laser power in milliwatts or percentage | direct |
| [pinhole_size](pinhole_size.md) | 0..1 <br/> [Float](Float.md) | Pinhole size in Airy units for confocal microscopy | direct |
| [quantum_yield](quantum_yield.md) | 0..1 <br/> [Float](Float.md) | Quantum yield of the fluorophore | direct |
| [defocus](defocus.md) | 0..1 <br/> [Float](Float.md) | Defocus value in micrometers | [Image2D](Image2D.md) |
| [astigmatism](astigmatism.md) | 0..1 <br/> [Float](Float.md) | Astigmatism value in Angstroms | [Image2D](Image2D.md) |
| [file_name](file_name.md) | 1 <br/> [String](String.md) | Image file name | [Image](Image.md) |
| [acquisition_date](acquisition_date.md) | 0..1 <br/> [String](String.md) | Date image was acquired | [Image](Image.md) |
| [pixel_size](pixel_size.md) | 0..1 <br/> [Float](Float.md) | Pixel size in Angstroms | [Image](Image.md) |
| [dimensions_x](dimensions_x.md) | 0..1 <br/> [Integer](Integer.md) | Image width in pixels | [Image](Image.md) |
| [dimensions_y](dimensions_y.md) | 0..1 <br/> [Integer](Integer.md) | Image height in pixels | [Image](Image.md) |
| [exposure_time](exposure_time.md) | 0..1 <br/> [Float](Float.md) | Exposure time in seconds | [Image](Image.md) |
| [dose](dose.md) | 0..1 <br/> [Float](Float.md) | Electron dose in e-/Å² | [Image](Image.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:FluorescenceImage |
| native | lambdaber:FluorescenceImage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FluorescenceImage
description: Fluorescence microscopy image capturing specific molecular targets through
  fluorescent labeling
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image2D
attributes:
  excitation_wavelength:
    name: excitation_wavelength
    description: Excitation wavelength in nanometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: float
  emission_wavelength:
    name: emission_wavelength
    description: Emission wavelength in nanometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: float
  excitation_filter:
    name: excitation_filter
    description: Specifications of the excitation filter
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: string
  emission_filter:
    name: emission_filter
    description: Specifications of the emission filter
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: string
  fluorophore:
    name: fluorophore
    description: Name or type of fluorophore used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: string
  channel_name:
    name: channel_name
    description: Name of the fluorescence channel (e.g., DAPI, GFP, RFP)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: string
  laser_power:
    name: laser_power
    description: Laser power in milliwatts or percentage
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: float
  pinhole_size:
    name: pinhole_size
    description: Pinhole size in Airy units for confocal microscopy
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: float
  quantum_yield:
    name: quantum_yield
    description: Quantum yield of the fluorophore
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FluorescenceImage
    range: float

```
</details>

### Induced

<details>
```yaml
name: FluorescenceImage
description: Fluorescence microscopy image capturing specific molecular targets through
  fluorescent labeling
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image2D
attributes:
  excitation_wavelength:
    name: excitation_wavelength
    description: Excitation wavelength in nanometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: excitation_wavelength
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: float
  emission_wavelength:
    name: emission_wavelength
    description: Emission wavelength in nanometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: emission_wavelength
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: float
  excitation_filter:
    name: excitation_filter
    description: Specifications of the excitation filter
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: excitation_filter
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: string
  emission_filter:
    name: emission_filter
    description: Specifications of the emission filter
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: emission_filter
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: string
  fluorophore:
    name: fluorophore
    description: Name or type of fluorophore used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: fluorophore
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: string
  channel_name:
    name: channel_name
    description: Name of the fluorescence channel (e.g., DAPI, GFP, RFP)
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: channel_name
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: string
  laser_power:
    name: laser_power
    description: Laser power in milliwatts or percentage
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: laser_power
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: float
  pinhole_size:
    name: pinhole_size
    description: Pinhole size in Airy units for confocal microscopy
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: pinhole_size
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: float
  quantum_yield:
    name: quantum_yield
    description: Quantum yield of the fluorophore
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: quantum_yield
    owner: FluorescenceImage
    domain_of:
    - FluorescenceImage
    range: float
  defocus:
    name: defocus
    description: Defocus value in micrometers
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: defocus
    owner: FluorescenceImage
    domain_of:
    - Image2D
    range: float
  astigmatism:
    name: astigmatism
    description: Astigmatism value in Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: astigmatism
    owner: FluorescenceImage
    domain_of:
    - Image2D
    range: float
  file_name:
    name: file_name
    description: Image file name
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: file_name
    owner: FluorescenceImage
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
    owner: FluorescenceImage
    domain_of:
    - Image
    range: string
  pixel_size:
    name: pixel_size
    description: Pixel size in Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: pixel_size
    owner: FluorescenceImage
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
    owner: FluorescenceImage
    domain_of:
    - Image
    range: integer
  dimensions_y:
    name: dimensions_y
    description: Image height in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: dimensions_y
    owner: FluorescenceImage
    domain_of:
    - Image
    range: integer
  exposure_time:
    name: exposure_time
    description: Exposure time in seconds
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: exposure_time
    owner: FluorescenceImage
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
    owner: FluorescenceImage
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
    owner: FluorescenceImage
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
    owner: FluorescenceImage
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: FluorescenceImage
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>