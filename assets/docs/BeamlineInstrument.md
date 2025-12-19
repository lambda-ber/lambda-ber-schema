
# Class: BeamlineInstrument

Multi-technique synchrotron beamline that supports multiple experimental methods

URI: [lambdaber:BeamlineInstrument](https://w3id.org/lambda-ber-schema/BeamlineInstrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Instrument],[QuantityValue]<sample_changer_capacity%200..1-++[BeamlineInstrument&#124;techniques_supported:TechniqueEnum%20%2B;source_type:XRaySourceTypeEnum%20%3F;mail_in_service:boolean%20%3F;website:uri%20%3F;instrument_code(i):string;instrument_category(i):InstrumentCategoryEnum%20%3F;facility_name(i):FacilityEnum%20%3F;facility_ror(i):uriorcurie%20%3F;beamline_id(i):string%20%3F;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<q_range_max%200..1-++[BeamlineInstrument],[QuantityValue]<q_range_min%200..1-++[BeamlineInstrument],[QuantityValue]<energy_max%200..1-++[BeamlineInstrument],[QuantityValue]<energy_min%200..1-++[BeamlineInstrument],[Instrument]^-[BeamlineInstrument])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue],[Instrument],[QuantityValue]<sample_changer_capacity%200..1-++[BeamlineInstrument&#124;techniques_supported:TechniqueEnum%20%2B;source_type:XRaySourceTypeEnum%20%3F;mail_in_service:boolean%20%3F;website:uri%20%3F;instrument_code(i):string;instrument_category(i):InstrumentCategoryEnum%20%3F;facility_name(i):FacilityEnum%20%3F;facility_ror(i):uriorcurie%20%3F;beamline_id(i):string%20%3F;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<q_range_max%200..1-++[BeamlineInstrument],[QuantityValue]<q_range_min%200..1-++[BeamlineInstrument],[QuantityValue]<energy_max%200..1-++[BeamlineInstrument],[QuantityValue]<energy_min%200..1-++[BeamlineInstrument],[Instrument]^-[BeamlineInstrument])

## Parents

 *  is_a: [Instrument](Instrument.md) - An instrument used to collect data

## Attributes


### Own

 * [➞techniques_supported](beamlineInstrument__techniques_supported.md)  <sub>1..\*</sub>
     * Description: Experimental techniques available at this beamline
     * Range: [TechniqueEnum](TechniqueEnum.md)
 * [➞source_type](beamlineInstrument__source_type.md)  <sub>0..1</sub>
     * Description: Type of X-ray source
     * Range: [XRaySourceTypeEnum](XRaySourceTypeEnum.md)
 * [➞energy_min](beamlineInstrument__energy_min.md)  <sub>0..1</sub>
     * Description: Minimum X-ray energy in keV
     * Range: [QuantityValue](QuantityValue.md)
 * [➞energy_max](beamlineInstrument__energy_max.md)  <sub>0..1</sub>
     * Description: Maximum X-ray energy in keV
     * Range: [QuantityValue](QuantityValue.md)
 * [➞q_range_min](beamlineInstrument__q_range_min.md)  <sub>0..1</sub>
     * Description: Minimum q value for SAXS in inverse Angstroms
     * Range: [QuantityValue](QuantityValue.md)
 * [➞q_range_max](beamlineInstrument__q_range_max.md)  <sub>0..1</sub>
     * Description: Maximum q value for SAXS in inverse Angstroms
     * Range: [QuantityValue](QuantityValue.md)
 * [➞sample_changer_capacity](beamlineInstrument__sample_changer_capacity.md)  <sub>0..1</sub>
     * Description: Automatic sample changer capacity
     * Range: [QuantityValue](QuantityValue.md)
 * [➞mail_in_service](beamlineInstrument__mail_in_service.md)  <sub>0..1</sub>
     * Description: Whether mail-in sample service is available
     * Range: [Boolean](types/Boolean.md)
 * [➞website](beamlineInstrument__website.md)  <sub>0..1</sub>
     * Description: Beamline website URL
     * Range: [Uri](types/Uri.md)

### Inherited from Instrument:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
 * [➞instrument_code](instrument__instrument_code.md)  <sub>1..1</sub>
     * Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
     * Range: [String](types/String.md)
 * [➞instrument_category](instrument__instrument_category.md)  <sub>0..1</sub>
     * Description: Category distinguishing beamlines from laboratory equipment
     * Range: [InstrumentCategoryEnum](InstrumentCategoryEnum.md)
 * [➞facility_name](instrument__facility_name.md)  <sub>0..1</sub>
     * Description: Name of the research facility where the instrument is located
     * Range: [FacilityEnum](FacilityEnum.md)
 * [➞facility_ror](instrument__facility_ror.md)  <sub>0..1</sub>
     * Description: Research Organization Registry (ROR) identifier for the facility
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞beamline_id](instrument__beamline_id.md)  <sub>0..1</sub>
     * Description: Beamline identifier at synchrotron/neutron facility
     * Range: [String](types/String.md)
 * [➞manufacturer](instrument__manufacturer.md)  <sub>0..1</sub>
     * Description: Instrument manufacturer
     * Range: [String](types/String.md)
 * [➞model](instrument__model.md)  <sub>0..1</sub>
     * Description: Instrument model
     * Range: [String](types/String.md)
 * [➞installation_date](instrument__installation_date.md)  <sub>0..1</sub>
     * Description: Date of instrument installation
     * Range: [String](types/String.md)
 * [➞current_status](instrument__current_status.md)  <sub>0..1</sub>
     * Description: Current operational status
     * Range: [InstrumentStatusEnum](InstrumentStatusEnum.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Use for beamlines like SIBYLS that support both SAXS and crystallography |
|  | | For single-technique beamlines, use XRayInstrument or SAXSInstrument |
