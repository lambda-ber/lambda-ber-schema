

# Class: BeamlineInstrument 


_Multi-technique synchrotron beamline that supports multiple experimental methods_





URI: [lambdaber:BeamlineInstrument](https://w3id.org/lambda-ber-schema/BeamlineInstrument)





```mermaid
 classDiagram
    class BeamlineInstrument
    click BeamlineInstrument href "../BeamlineInstrument/"
      Instrument <|-- BeamlineInstrument
        click Instrument href "../Instrument/"
      
      BeamlineInstrument : beamline_id
        
      BeamlineInstrument : current_status
        
          
    
        
        
        BeamlineInstrument --> "0..1" InstrumentStatusEnum : current_status
        click InstrumentStatusEnum href "../InstrumentStatusEnum/"
    

        
      BeamlineInstrument : description
        
      BeamlineInstrument : energy_max
        
          
    
        
        
        BeamlineInstrument --> "0..1" QuantityValue : energy_max
        click QuantityValue href "../QuantityValue/"
    

        
      BeamlineInstrument : energy_min
        
          
    
        
        
        BeamlineInstrument --> "0..1" QuantityValue : energy_min
        click QuantityValue href "../QuantityValue/"
    

        
      BeamlineInstrument : facility_name
        
          
    
        
        
        BeamlineInstrument --> "0..1" FacilityEnum : facility_name
        click FacilityEnum href "../FacilityEnum/"
    

        
      BeamlineInstrument : facility_ror
        
      BeamlineInstrument : id
        
      BeamlineInstrument : installation_date
        
      BeamlineInstrument : instrument_category
        
          
    
        
        
        BeamlineInstrument --> "0..1" InstrumentCategoryEnum : instrument_category
        click InstrumentCategoryEnum href "../InstrumentCategoryEnum/"
    

        
      BeamlineInstrument : instrument_code
        
      BeamlineInstrument : mail_in_service
        
      BeamlineInstrument : manufacturer
        
      BeamlineInstrument : model
        
      BeamlineInstrument : q_range_max
        
          
    
        
        
        BeamlineInstrument --> "0..1" QuantityValue : q_range_max
        click QuantityValue href "../QuantityValue/"
    

        
      BeamlineInstrument : q_range_min
        
          
    
        
        
        BeamlineInstrument --> "0..1" QuantityValue : q_range_min
        click QuantityValue href "../QuantityValue/"
    

        
      BeamlineInstrument : sample_changer_capacity
        
          
    
        
        
        BeamlineInstrument --> "0..1" QuantityValue : sample_changer_capacity
        click QuantityValue href "../QuantityValue/"
    

        
      BeamlineInstrument : source_type
        
          
    
        
        
        BeamlineInstrument --> "0..1" XRaySourceTypeEnum : source_type
        click XRaySourceTypeEnum href "../XRaySourceTypeEnum/"
    

        
      BeamlineInstrument : techniques_supported
        
          
    
        
        
        BeamlineInstrument --> "1..*" TechniqueEnum : techniques_supported
        click TechniqueEnum href "../TechniqueEnum/"
    

        
      BeamlineInstrument : title
        
      BeamlineInstrument : website
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [Instrument](Instrument.md)
        * **BeamlineInstrument**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [techniques_supported](techniques_supported.md) | 1..* <br/> [TechniqueEnum](TechniqueEnum.md) | Experimental techniques available at this beamline | direct |
| [source_type](source_type.md) | 0..1 <br/> [XRaySourceTypeEnum](XRaySourceTypeEnum.md) | Type of X-ray source | direct |
| [energy_min](energy_min.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Minimum X-ray energy in keV | direct |
| [energy_max](energy_max.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Maximum X-ray energy in keV | direct |
| [q_range_min](q_range_min.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Minimum q value for SAXS in inverse Angstroms | direct |
| [q_range_max](q_range_max.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Maximum q value for SAXS in inverse Angstroms | direct |
| [sample_changer_capacity](sample_changer_capacity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Automatic sample changer capacity | direct |
| [mail_in_service](mail_in_service.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether mail-in sample service is available | direct |
| [website](website.md) | 0..1 <br/> [Uri](Uri.md) | Beamline website URL | direct |
| [instrument_code](instrument_code.md) | 1 <br/> [String](String.md) | Human-friendly facility or laboratory identifier for the instrument (e | [Instrument](Instrument.md) |
| [instrument_category](instrument_category.md) | 0..1 <br/> [InstrumentCategoryEnum](InstrumentCategoryEnum.md) | Category distinguishing beamlines from laboratory equipment | [Instrument](Instrument.md) |
| [facility_name](facility_name.md) | 0..1 <br/> [FacilityEnum](FacilityEnum.md) | Name of the research facility where the instrument is located | [Instrument](Instrument.md) |
| [facility_ror](facility_ror.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Research Organization Registry (ROR) identifier for the facility | [Instrument](Instrument.md) |
| [beamline_id](beamline_id.md) | 0..1 <br/> [String](String.md) | Beamline identifier at synchrotron/neutron facility | [Instrument](Instrument.md) |
| [manufacturer](manufacturer.md) | 0..1 <br/> [String](String.md) | Instrument manufacturer | [Instrument](Instrument.md) |
| [model](model.md) | 0..1 <br/> [String](String.md) | Instrument model | [Instrument](Instrument.md) |
| [installation_date](installation_date.md) | 0..1 <br/> [String](String.md) | Date of instrument installation | [Instrument](Instrument.md) |
| [current_status](current_status.md) | 0..1 <br/> [InstrumentStatusEnum](InstrumentStatusEnum.md) | Current operational status | [Instrument](Instrument.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |










## Comments

* Use for beamlines like SIBYLS that support both SAXS and crystallography
* For single-technique beamlines, use XRayInstrument or SAXSInstrument

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:BeamlineInstrument |
| native | lambdaber:BeamlineInstrument |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BeamlineInstrument
description: Multi-technique synchrotron beamline that supports multiple experimental
  methods
comments:
- Use for beamlines like SIBYLS that support both SAXS and crystallography
- For single-technique beamlines, use XRayInstrument or SAXSInstrument
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Instrument
attributes:
  techniques_supported:
    name: techniques_supported
    description: Experimental techniques available at this beamline
    comments:
    - List all techniques this beamline supports
    - 'Example: [saxs, xray_crystallography] for SIBYLS'
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - BeamlineInstrument
    range: TechniqueEnum
    required: true
    multivalued: true
  source_type:
    name: source_type
    description: Type of X-ray source
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - XRayInstrument
    - BeamlineInstrument
    - XRFImage
    range: XRaySourceTypeEnum
  energy_min:
    name: energy_min
    description: Minimum X-ray energy in keV
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - XRayInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  energy_max:
    name: energy_max
    description: Maximum X-ray energy in keV
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - XRayInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  q_range_min:
    name: q_range_min
    description: Minimum q value for SAXS in inverse Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - SAXSInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  q_range_max:
    name: q_range_max
    description: Maximum q value for SAXS in inverse Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - SAXSInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  sample_changer_capacity:
    name: sample_changer_capacity
    description: Automatic sample changer capacity
    from_schema: https://w3id.org/lambda-ber-schema/
    domain_of:
    - SAXSInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  mail_in_service:
    name: mail_in_service
    description: Whether mail-in sample service is available
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - BeamlineInstrument
    range: boolean
  website:
    name: website
    description: Beamline website URL
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    domain_of:
    - BeamlineInstrument
    range: uri

```
</details>

### Induced

<details>
```yaml
name: BeamlineInstrument
description: Multi-technique synchrotron beamline that supports multiple experimental
  methods
comments:
- Use for beamlines like SIBYLS that support both SAXS and crystallography
- For single-technique beamlines, use XRayInstrument or SAXSInstrument
from_schema: https://w3id.org/lambda-ber-schema/
is_a: Instrument
attributes:
  techniques_supported:
    name: techniques_supported
    description: Experimental techniques available at this beamline
    comments:
    - List all techniques this beamline supports
    - 'Example: [saxs, xray_crystallography] for SIBYLS'
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: techniques_supported
    owner: BeamlineInstrument
    domain_of:
    - BeamlineInstrument
    range: TechniqueEnum
    required: true
    multivalued: true
  source_type:
    name: source_type
    description: Type of X-ray source
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: source_type
    owner: BeamlineInstrument
    domain_of:
    - XRayInstrument
    - BeamlineInstrument
    - XRFImage
    range: XRaySourceTypeEnum
  energy_min:
    name: energy_min
    description: Minimum X-ray energy in keV
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: energy_min
    owner: BeamlineInstrument
    domain_of:
    - XRayInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  energy_max:
    name: energy_max
    description: Maximum X-ray energy in keV
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: energy_max
    owner: BeamlineInstrument
    domain_of:
    - XRayInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  q_range_min:
    name: q_range_min
    description: Minimum q value for SAXS in inverse Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: q_range_min
    owner: BeamlineInstrument
    domain_of:
    - SAXSInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  q_range_max:
    name: q_range_max
    description: Maximum q value for SAXS in inverse Angstroms
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: q_range_max
    owner: BeamlineInstrument
    domain_of:
    - SAXSInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  sample_changer_capacity:
    name: sample_changer_capacity
    description: Automatic sample changer capacity
    from_schema: https://w3id.org/lambda-ber-schema/
    alias: sample_changer_capacity
    owner: BeamlineInstrument
    domain_of:
    - SAXSInstrument
    - BeamlineInstrument
    range: QuantityValue
    inlined: true
  mail_in_service:
    name: mail_in_service
    description: Whether mail-in sample service is available
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: mail_in_service
    owner: BeamlineInstrument
    domain_of:
    - BeamlineInstrument
    range: boolean
  website:
    name: website
    description: Beamline website URL
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: website
    owner: BeamlineInstrument
    domain_of:
    - BeamlineInstrument
    range: uri
  instrument_code:
    name: instrument_code
    description: Human-friendly facility or laboratory identifier for the instrument
      (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local
      reference and equipment tracking.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: instrument_code
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: string
    required: true
  instrument_category:
    name: instrument_category
    description: Category distinguishing beamlines from laboratory equipment
    comments:
    - Use SYNCHROTRON_BEAMLINE for synchrotron beamlines
    - Use ELECTRON_MICROSCOPE for cryo-EM instruments
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: instrument_category
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: InstrumentCategoryEnum
  facility_name:
    name: facility_name
    description: Name of the research facility where the instrument is located
    comments:
    - Select from the standardized list of major synchrotron facilities
    - Leave empty for laboratory-based instruments
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: facility_name
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: FacilityEnum
  facility_ror:
    name: facility_ror
    description: Research Organization Registry (ROR) identifier for the facility
    comments:
    - Persistent identifier for the facility organization
    - 'Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)'
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: facility_ror
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: uriorcurie
    pattern: ^https://ror\.org/\w+$
  beamline_id:
    name: beamline_id
    description: Beamline identifier at synchrotron/neutron facility
    comments:
    - Use facility-specific naming convention
    - 'Examples: ''12.3.1'' (ALS), ''17-ID-1'' (NSLS-II), ''I04'' (Diamond)'
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    slot_uri: mmCIF:_diffrn_source.pdbx_synchrotron_beamline
    alias: beamline_id
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: string
  manufacturer:
    name: manufacturer
    description: Instrument manufacturer
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: manufacturer
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: string
  model:
    name: model
    description: Instrument model
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: model
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: string
  installation_date:
    name: installation_date
    description: Date of instrument installation
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: installation_date
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: string
  current_status:
    name: current_status
    description: Current operational status
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: current_status
    owner: BeamlineInstrument
    domain_of:
    - Instrument
    range: InstrumentStatusEnum
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    identifier: true
    alias: id
    owner: BeamlineInstrument
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
    owner: BeamlineInstrument
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/lambda-ber-schema/
    rank: 1000
    alias: description
    owner: BeamlineInstrument
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>