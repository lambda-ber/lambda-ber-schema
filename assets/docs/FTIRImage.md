

# Class: FTIRImage 


_Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy_





URI: [lambdaber:FTIRImage](https://w3id.org/lambda-ber-schema/FTIRImage)





```mermaid
 classDiagram
    class FTIRImage
    click FTIRImage href "../FTIRImage/"
      Image <|-- FTIRImage
        click Image href "../Image/"
      
      FTIRImage : acquisition_date
        
      FTIRImage : apodization_function
        
      FTIRImage : background_correction
        
      FTIRImage : description
        
      FTIRImage : dimensions_x
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : dimensions_x
        click QuantityValue href "../QuantityValue/"
    

        
      FTIRImage : dimensions_y
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : dimensions_y
        click QuantityValue href "../QuantityValue/"
    

        
      FTIRImage : dose
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : dose
        click QuantityValue href "../QuantityValue/"
    

        
      FTIRImage : exposure_time
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : exposure_time
        click QuantityValue href "../QuantityValue/"
    

        
      FTIRImage : file_name
        
      FTIRImage : id
        
      FTIRImage : molecular_signatures
        
      FTIRImage : number_of_scans
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : number_of_scans
        click QuantityValue href "../QuantityValue/"
    

        
      FTIRImage : pixel_size
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : pixel_size
        click QuantityValue href "../QuantityValue/"
    

        
      FTIRImage : spectral_resolution
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : spectral_resolution
        click QuantityValue href "../QuantityValue/"
    

        
      FTIRImage : title
        
      FTIRImage : wavenumber_max
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : wavenumber_max
        click QuantityValue href "../QuantityValue/"
    

        
      FTIRImage : wavenumber_min
        
          
    
        
        
        FTIRImage --> "0..1" QuantityValue : wavenumber_min
        click QuantityValue href "../QuantityValue/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [Image](Image.md)
        * **FTIRImage**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [wavenumber_min](wavenumber_min.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Minimum wavenumber, typically specified in inverse centimeters (cm⁻¹) | direct |
| [wavenumber_max](wavenumber_max.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Maximum wavenumber, typically specified in inverse centimeters (cm⁻¹) | direct |
| [spectral_resolution](spectral_resolution.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Spectral resolution, typically specified in inverse centimeters (cm⁻¹) | direct |
| [number_of_scans](number_of_scans.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Number of scans averaged for the spectrum | direct |
| [apodization_function](apodization_function.md) | 0..1 <br/> [String](String.md) | Mathematical function used for apodization | direct |
| [molecular_signatures](molecular_signatures.md) | * <br/> [String](String.md) | Identified molecular signatures or peaks | direct |
| [background_correction](background_correction.md) | 0..1 <br/> [String](String.md) | Method used for background correction | direct |
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
| self | lambdaber:FTIRImage |
| native | lambdaber:FTIRImage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FTIRImage
description: Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular
  composition through vibrational spectroscopy
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image
attributes:
  wavenumber_min:
    name: wavenumber_min
    description: Minimum wavenumber, typically specified in inverse centimeters (cm⁻¹).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FTIRImage
    range: QuantityValue
    inlined: true
  wavenumber_max:
    name: wavenumber_max
    description: Maximum wavenumber, typically specified in inverse centimeters (cm⁻¹).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FTIRImage
    range: QuantityValue
    inlined: true
  spectral_resolution:
    name: spectral_resolution
    description: Spectral resolution, typically specified in inverse centimeters (cm⁻¹).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FTIRImage
    range: QuantityValue
    inlined: true
  number_of_scans:
    name: number_of_scans
    description: Number of scans averaged for the spectrum
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FTIRImage
    range: QuantityValue
    inlined: true
  apodization_function:
    name: apodization_function
    description: Mathematical function used for apodization
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FTIRImage
    range: string
  molecular_signatures:
    name: molecular_signatures
    description: Identified molecular signatures or peaks
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FTIRImage
    range: string
    multivalued: true
  background_correction:
    name: background_correction
    description: Method used for background correction
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - FTIRImage
    range: string

```
</details>

### Induced

<details>
```yaml
name: FTIRImage
description: Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular
  composition through vibrational spectroscopy
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Image
attributes:
  wavenumber_min:
    name: wavenumber_min
    description: Minimum wavenumber, typically specified in inverse centimeters (cm⁻¹).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: wavenumber_min
    owner: FTIRImage
    domain_of:
    - FTIRImage
    range: QuantityValue
    inlined: true
  wavenumber_max:
    name: wavenumber_max
    description: Maximum wavenumber, typically specified in inverse centimeters (cm⁻¹).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: wavenumber_max
    owner: FTIRImage
    domain_of:
    - FTIRImage
    range: QuantityValue
    inlined: true
  spectral_resolution:
    name: spectral_resolution
    description: Spectral resolution, typically specified in inverse centimeters (cm⁻¹).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: spectral_resolution
    owner: FTIRImage
    domain_of:
    - FTIRImage
    range: QuantityValue
    inlined: true
  number_of_scans:
    name: number_of_scans
    description: Number of scans averaged for the spectrum
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: number_of_scans
    owner: FTIRImage
    domain_of:
    - FTIRImage
    range: QuantityValue
    inlined: true
  apodization_function:
    name: apodization_function
    description: Mathematical function used for apodization
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: apodization_function
    owner: FTIRImage
    domain_of:
    - FTIRImage
    range: string
  molecular_signatures:
    name: molecular_signatures
    description: Identified molecular signatures or peaks
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: molecular_signatures
    owner: FTIRImage
    domain_of:
    - FTIRImage
    range: string
    multivalued: true
  background_correction:
    name: background_correction
    description: Method used for background correction
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: background_correction
    owner: FTIRImage
    domain_of:
    - FTIRImage
    range: string
  file_name:
    name: file_name
    description: Image file name
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: file_name
    owner: FTIRImage
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
    owner: FTIRImage
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
    owner: FTIRImage
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
    owner: FTIRImage
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
    owner: FTIRImage
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
    owner: FTIRImage
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
    owner: FTIRImage
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
    owner: FTIRImage
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
    owner: FTIRImage
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: FTIRImage
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>