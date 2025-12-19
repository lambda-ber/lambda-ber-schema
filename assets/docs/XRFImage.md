

# Class: XRFImage 


_X-ray fluorescence (XRF) image showing elemental distribution_





URI: [lambdaber:XRFImage](https://w3id.org/lambda-ber-schema/XRFImage)





```mermaid
 classDiagram
    class XRFImage
    click XRFImage href "../XRFImage/"
      Image2D <|-- XRFImage
        click Image2D href "../Image2D/"
      
      XRFImage : acquisition_date
        
      XRFImage : astigmatism
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : astigmatism
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : beam_energy
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : beam_energy
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : beam_size
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : beam_size
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : calibration_standard
        
      XRFImage : defocus
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : defocus
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : description
        
      XRFImage : detector_model
        
      XRFImage : detector_technology
        
          
    
        
        
        XRFImage --> "0..1" DetectorTechnologyEnum : detector_technology
        click DetectorTechnologyEnum href "../DetectorTechnologyEnum/"
    

        
      XRFImage : dimensions_x
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : dimensions_x
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : dimensions_y
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : dimensions_y
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : dose
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : dose
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : dwell_time
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : dwell_time
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : elements_measured
        
      XRFImage : exposure_time
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : exposure_time
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : file_name
        
      XRFImage : flux
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : flux
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : id
        
      XRFImage : pixel_size
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : pixel_size
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : source_type
        
          
    
        
        
        XRFImage --> "0..1" XRaySourceTypeEnum : source_type
        click XRaySourceTypeEnum href "../XRaySourceTypeEnum/"
    

        
      XRFImage : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [Image](Image.md)
        * [Image2D](Image2D.md)
            * **XRFImage**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [beam_energy](beam_energy.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | X-ray beam energy, typically specified in kiloelectronvolts (keV) | direct |
| [beam_size](beam_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | X-ray beam size, typically specified in micrometers | direct |
| [dwell_time](dwell_time.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Dwell time per pixel, typically specified in milliseconds | direct |
| [elements_measured](elements_measured.md) | * <br/> [String](String.md) | Elements detected and measured | direct |
| [source_type](source_type.md) | 0..1 <br/> [XRaySourceTypeEnum](XRaySourceTypeEnum.md) | X-ray source type (synchrotron or lab-source) | direct |
| [detector_technology](detector_technology.md) | 0..1 <br/> [DetectorTechnologyEnum](DetectorTechnologyEnum.md) | Type of X-ray detector technology used | direct |
| [detector_model](detector_model.md) | 0..1 <br/> [String](String.md) | Specific detector model used for XRF measurement | direct |
| [flux](flux.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Photon flux, typically specified in photons per second | direct |
| [calibration_standard](calibration_standard.md) | 0..1 <br/> [String](String.md) | Reference standard used for calibration | direct |
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
| self | lambdaber:XRFImage |
| native | lambdaber:XRFImage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: XRFImage
description: X-ray fluorescence (XRF) image showing elemental distribution
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image2D
attributes:
  beam_energy:
    name: beam_energy
    description: X-ray beam energy, typically specified in kiloelectronvolts (keV).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - XRFImage
    - ExperimentalConditions
    range: QuantityValue
    inlined: true
  beam_size:
    name: beam_size
    description: X-ray beam size, typically specified in micrometers. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - XRFImage
    range: QuantityValue
    inlined: true
  dwell_time:
    name: dwell_time
    description: Dwell time per pixel, typically specified in milliseconds. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - XRFImage
    range: QuantityValue
    inlined: true
  elements_measured:
    name: elements_measured
    description: Elements detected and measured
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - XRFImage
    range: string
    multivalued: true
  source_type:
    name: source_type
    description: X-ray source type (synchrotron or lab-source)
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - XRayInstrument
    - BeamlineInstrument
    - XRFImage
    range: XRaySourceTypeEnum
  detector_technology:
    name: detector_technology
    description: Type of X-ray detector technology used
    comments:
    - For XRF, typically energy-dispersive or wavelength-dispersive detectors
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - CryoEMInstrument
    - XRayInstrument
    - XRFImage
    range: DetectorTechnologyEnum
  detector_model:
    name: detector_model
    description: Specific detector model used for XRF measurement
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - CryoEMInstrument
    - XRayInstrument
    - XRFImage
    range: string
  flux:
    name: flux
    description: Photon flux, typically specified in photons per second. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - ExperimentRun
    - XRFImage
    range: QuantityValue
    inlined: true
  calibration_standard:
    name: calibration_standard
    description: Reference standard used for calibration
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - XRFImage
    range: string

```
</details>

### Induced

<details>
```yaml
name: XRFImage
description: X-ray fluorescence (XRF) image showing elemental distribution
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image2D
attributes:
  beam_energy:
    name: beam_energy
    description: X-ray beam energy, typically specified in kiloelectronvolts (keV).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: beam_energy
    owner: XRFImage
    domain_of:
    - XRFImage
    - ExperimentalConditions
    range: QuantityValue
    inlined: true
  beam_size:
    name: beam_size
    description: X-ray beam size, typically specified in micrometers. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: beam_size
    owner: XRFImage
    domain_of:
    - XRFImage
    range: QuantityValue
    inlined: true
  dwell_time:
    name: dwell_time
    description: Dwell time per pixel, typically specified in milliseconds. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: dwell_time
    owner: XRFImage
    domain_of:
    - XRFImage
    range: QuantityValue
    inlined: true
  elements_measured:
    name: elements_measured
    description: Elements detected and measured
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: elements_measured
    owner: XRFImage
    domain_of:
    - XRFImage
    range: string
    multivalued: true
  source_type:
    name: source_type
    description: X-ray source type (synchrotron or lab-source)
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: source_type
    owner: XRFImage
    domain_of:
    - XRayInstrument
    - BeamlineInstrument
    - XRFImage
    range: XRaySourceTypeEnum
  detector_technology:
    name: detector_technology
    description: Type of X-ray detector technology used
    comments:
    - For XRF, typically energy-dispersive or wavelength-dispersive detectors
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: detector_technology
    owner: XRFImage
    domain_of:
    - CryoEMInstrument
    - XRayInstrument
    - XRFImage
    range: DetectorTechnologyEnum
  detector_model:
    name: detector_model
    description: Specific detector model used for XRF measurement
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: detector_model
    owner: XRFImage
    domain_of:
    - CryoEMInstrument
    - XRayInstrument
    - XRFImage
    range: string
  flux:
    name: flux
    description: Photon flux, typically specified in photons per second. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: flux
    owner: XRFImage
    domain_of:
    - ExperimentRun
    - XRFImage
    range: QuantityValue
    inlined: true
  calibration_standard:
    name: calibration_standard
    description: Reference standard used for calibration
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: calibration_standard
    owner: XRFImage
    domain_of:
    - XRFImage
    range: string
  defocus:
    name: defocus
    description: Defocus value, typically specified in micrometers. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: defocus
    owner: XRFImage
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
    owner: XRFImage
    domain_of:
    - Image2D
    range: QuantityValue
    inlined: true
  file_name:
    name: file_name
    description: Image file name
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: file_name
    owner: XRFImage
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
    owner: XRFImage
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
    owner: XRFImage
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
    owner: XRFImage
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
    owner: XRFImage
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
    owner: XRFImage
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
    owner: XRFImage
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
    owner: XRFImage
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
    owner: XRFImage
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: XRFImage
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>