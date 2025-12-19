

# Class: DataCollectionStrategy 


_Strategy for data collection_





URI: [lambdaber:DataCollectionStrategy](https://w3id.org/lambda-ber-schema/DataCollectionStrategy)





```mermaid
 classDiagram
    class DataCollectionStrategy
    click DataCollectionStrategy href "../DataCollectionStrategy/"
      AttributeGroup <|-- DataCollectionStrategy
        click AttributeGroup href "../AttributeGroup/"
      
      DataCollectionStrategy : attenuator
        
      DataCollectionStrategy : beam_center_x_px
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : beam_center_x_px
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : beam_center_y_px
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : beam_center_y_px
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : beam_size_um
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : beam_size_um
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : collection_mode
        
          
    
        
        
        DataCollectionStrategy --> "0..1" CollectionModeEnum : collection_mode
        click CollectionModeEnum href "../CollectionModeEnum/"
    

        
      DataCollectionStrategy : description
        
      DataCollectionStrategy : detector_distance_mm
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : detector_distance_mm
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : detector_mode
        
          
    
        
        
        DataCollectionStrategy --> "0..1" DetectorModeEnum : detector_mode
        click DetectorModeEnum href "../DetectorModeEnum/"
    

        
      DataCollectionStrategy : dose_per_frame
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : dose_per_frame
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : flux_photons_per_s
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : flux_photons_per_s
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : frame_rate
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : frame_rate
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : oscillation_per_image_deg
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : oscillation_per_image_deg
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : pixel_size_calibrated
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : pixel_size_calibrated
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : strategy_notes
        
      DataCollectionStrategy : temperature_k
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : temperature_k
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : total_dose
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : total_dose
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : total_frames
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : total_frames
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : total_rotation_deg
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : total_rotation_deg
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : transmission_percent
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : transmission_percent
        click QuantityValue href "../QuantityValue/"
    

        
      DataCollectionStrategy : wavelength_a
        
          
    
        
        
        DataCollectionStrategy --> "0..1" QuantityValue : wavelength_a
        click QuantityValue href "../QuantityValue/"
    

        
      
```





## Inheritance
* [AttributeGroup](AttributeGroup.md)
    * **DataCollectionStrategy**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [collection_mode](collection_mode.md) | 0..1 <br/> [CollectionModeEnum](CollectionModeEnum.md) | Mode of data collection | direct |
| [total_frames](total_frames.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total number of frames/images | direct |
| [frame_rate](frame_rate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Frame rate, typically specified in frames per second | direct |
| [total_dose](total_dose.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total electron dose for cryo-EM, typically specified in electrons per Angstro... | direct |
| [dose_per_frame](dose_per_frame.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Dose per frame, typically specified in electrons per Angstrom squared (e⁻/Å²) | direct |
| [wavelength_a](wavelength_a.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | X-ray wavelength, typically specified in Angstroms | direct |
| [detector_mode](detector_mode.md) | 0..1 <br/> [DetectorModeEnum](DetectorModeEnum.md) | Detector operating mode used during this experiment | direct |
| [pixel_size_calibrated](pixel_size_calibrated.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Calibrated pixel size for this experiment, typically specified in Angstroms (... | direct |
| [detector_distance_mm](detector_distance_mm.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Detector distance, typically specified in millimeters | direct |
| [beam_center_x_px](beam_center_x_px.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Beam center X coordinate in pixels | direct |
| [beam_center_y_px](beam_center_y_px.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Beam center Y coordinate in pixels | direct |
| [beam_size_um](beam_size_um.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Beam size, typically specified in micrometers | direct |
| [flux_photons_per_s](flux_photons_per_s.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Photon flux, typically specified in photons per second | direct |
| [transmission_percent](transmission_percent.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Beam transmission, typically specified as a percentage (0-100) | direct |
| [attenuator](attenuator.md) | 0..1 <br/> [String](String.md) | Attenuator setting used | direct |
| [temperature_k](temperature_k.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Data collection temperature, typically specified in Kelvin | direct |
| [oscillation_per_image_deg](oscillation_per_image_deg.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Oscillation angle per image, typically specified in degrees | direct |
| [total_rotation_deg](total_rotation_deg.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total rotation range, typically specified in degrees | direct |
| [strategy_notes](strategy_notes.md) | 0..1 <br/> [String](String.md) | Notes about data collection strategy | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | [AttributeGroup](AttributeGroup.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | [data_collection_strategy](data_collection_strategy.md) | range | [DataCollectionStrategy](DataCollectionStrategy.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:DataCollectionStrategy |
| native | lambdaber:DataCollectionStrategy |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataCollectionStrategy
description: Strategy for data collection
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeGroup
attributes:
  collection_mode:
    name: collection_mode
    description: Mode of data collection
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: CollectionModeEnum
  total_frames:
    name: total_frames
    description: Total number of frames/images
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  frame_rate:
    name: frame_rate
    description: Frame rate, typically specified in frames per second. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  total_dose:
    name: total_dose
    description: Total electron dose for cryo-EM, typically specified in electrons
      per Angstrom squared (e⁻/Å²). Data providers may specify alternative units by
      including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - ExperimentRun
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  dose_per_frame:
    name: dose_per_frame
    description: Dose per frame, typically specified in electrons per Angstrom squared
      (e⁻/Å²). Data providers may specify alternative units by including the unit
      in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - Movie
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  wavelength_a:
    name: wavelength_a
    description: X-ray wavelength, typically specified in Angstroms. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  detector_mode:
    name: detector_mode
    description: Detector operating mode used during this experiment
    comments:
    - 'For cryo-EM: counting, integrating, or super_resolution'
    - Detector technology, manufacturer, and model are specified in the Instrument
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - CryoEMInstrument
    - DataCollectionStrategy
    range: DetectorModeEnum
  pixel_size_calibrated:
    name: pixel_size_calibrated
    description: Calibrated pixel size for this experiment, typically specified in
      Angstroms (Å) per pixel. Data providers may specify alternative units by including
      the unit in the QuantityValue.
    comments:
    - 'For cryo-EM: depends on magnification (Å/pixel)'
    - 'For X-ray: typically mm/pixel or µm/pixel'
    - Physical pixel size is hardware spec stored in Instrument
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  detector_distance_mm:
    name: detector_distance_mm
    description: Detector distance, typically specified in millimeters. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  beam_center_x_px:
    name: beam_center_x_px
    description: Beam center X coordinate in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  beam_center_y_px:
    name: beam_center_y_px
    description: Beam center Y coordinate in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  beam_size_um:
    name: beam_size_um
    description: Beam size, typically specified in micrometers. Data providers may
      specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  flux_photons_per_s:
    name: flux_photons_per_s
    description: Photon flux, typically specified in photons per second. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  transmission_percent:
    name: transmission_percent
    description: Beam transmission, typically specified as a percentage (0-100). Data
      providers may specify as decimal fraction by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  attenuator:
    name: attenuator
    description: Attenuator setting used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
  temperature_k:
    name: temperature_k
    description: Data collection temperature, typically specified in Kelvin. Data
      providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  oscillation_per_image_deg:
    name: oscillation_per_image_deg
    description: Oscillation angle per image, typically specified in degrees. Data
      providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  total_rotation_deg:
    name: total_rotation_deg
    description: Total rotation range, typically specified in degrees. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  strategy_notes:
    name: strategy_notes
    description: Notes about data collection strategy
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - DataCollectionStrategy

```
</details>

### Induced

<details>
```yaml
name: DataCollectionStrategy
description: Strategy for data collection
from_schema: https://w3id.org/lambda-ber-schema/
is_a: AttributeGroup
attributes:
  collection_mode:
    name: collection_mode
    description: Mode of data collection
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: collection_mode
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: CollectionModeEnum
  total_frames:
    name: total_frames
    description: Total number of frames/images
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: total_frames
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  frame_rate:
    name: frame_rate
    description: Frame rate, typically specified in frames per second. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: frame_rate
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  total_dose:
    name: total_dose
    description: Total electron dose for cryo-EM, typically specified in electrons
      per Angstrom squared (e⁻/Å²). Data providers may specify alternative units by
      including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: total_dose
    owner: DataCollectionStrategy
    domain_of:
    - ExperimentRun
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  dose_per_frame:
    name: dose_per_frame
    description: Dose per frame, typically specified in electrons per Angstrom squared
      (e⁻/Å²). Data providers may specify alternative units by including the unit
      in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: dose_per_frame
    owner: DataCollectionStrategy
    domain_of:
    - Movie
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  wavelength_a:
    name: wavelength_a
    description: X-ray wavelength, typically specified in Angstroms. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: wavelength_a
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  detector_mode:
    name: detector_mode
    description: Detector operating mode used during this experiment
    comments:
    - 'For cryo-EM: counting, integrating, or super_resolution'
    - Detector technology, manufacturer, and model are specified in the Instrument
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: detector_mode
    owner: DataCollectionStrategy
    domain_of:
    - CryoEMInstrument
    - DataCollectionStrategy
    range: DetectorModeEnum
  pixel_size_calibrated:
    name: pixel_size_calibrated
    description: Calibrated pixel size for this experiment, typically specified in
      Angstroms (Å) per pixel. Data providers may specify alternative units by including
      the unit in the QuantityValue.
    comments:
    - 'For cryo-EM: depends on magnification (Å/pixel)'
    - 'For X-ray: typically mm/pixel or µm/pixel'
    - Physical pixel size is hardware spec stored in Instrument
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: pixel_size_calibrated
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  detector_distance_mm:
    name: detector_distance_mm
    description: Detector distance, typically specified in millimeters. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: detector_distance_mm
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  beam_center_x_px:
    name: beam_center_x_px
    description: Beam center X coordinate in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: beam_center_x_px
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  beam_center_y_px:
    name: beam_center_y_px
    description: Beam center Y coordinate in pixels
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: beam_center_y_px
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  beam_size_um:
    name: beam_size_um
    description: Beam size, typically specified in micrometers. Data providers may
      specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: beam_size_um
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  flux_photons_per_s:
    name: flux_photons_per_s
    description: Photon flux, typically specified in photons per second. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: flux_photons_per_s
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  transmission_percent:
    name: transmission_percent
    description: Beam transmission, typically specified as a percentage (0-100). Data
      providers may specify as decimal fraction by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: transmission_percent
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  attenuator:
    name: attenuator
    description: Attenuator setting used
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: attenuator
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: string
  temperature_k:
    name: temperature_k
    description: Data collection temperature, typically specified in Kelvin. Data
      providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: temperature_k
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  oscillation_per_image_deg:
    name: oscillation_per_image_deg
    description: Oscillation angle per image, typically specified in degrees. Data
      providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: oscillation_per_image_deg
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  total_rotation_deg:
    name: total_rotation_deg
    description: Total rotation range, typically specified in degrees. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: total_rotation_deg
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: QuantityValue
    inlined: true
  strategy_notes:
    name: strategy_notes
    description: Notes about data collection strategy
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: strategy_notes
    owner: DataCollectionStrategy
    domain_of:
    - DataCollectionStrategy
    range: string
  description:
    name: description
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: description
    owner: DataCollectionStrategy
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>