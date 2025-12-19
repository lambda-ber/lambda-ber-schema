
# Class: SAXSInstrument

SAXS/WAXS instrument specifications

URI: [lambdaber:SAXSInstrument](https://w3id.org/lambda-ber-schema/SAXSInstrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<sample_changer_capacity%200..1-++[SAXSInstrument&#124;temperature_control_range:string%20%3F;instrument_code(i):string;instrument_category(i):InstrumentCategoryEnum%20%3F;facility_name(i):FacilityEnum%20%3F;facility_ror(i):uriorcurie%20%3F;beamline_id(i):string%20%3F;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<detector_distance_max%200..1-++[SAXSInstrument],[QuantityValue]<detector_distance_min%200..1-++[SAXSInstrument],[QuantityValue]<q_range_max%200..1-++[SAXSInstrument],[QuantityValue]<q_range_min%200..1-++[SAXSInstrument],[Instrument]^-[SAXSInstrument],[QuantityValue],[Instrument])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<sample_changer_capacity%200..1-++[SAXSInstrument&#124;temperature_control_range:string%20%3F;instrument_code(i):string;instrument_category(i):InstrumentCategoryEnum%20%3F;facility_name(i):FacilityEnum%20%3F;facility_ror(i):uriorcurie%20%3F;beamline_id(i):string%20%3F;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<detector_distance_max%200..1-++[SAXSInstrument],[QuantityValue]<detector_distance_min%200..1-++[SAXSInstrument],[QuantityValue]<q_range_max%200..1-++[SAXSInstrument],[QuantityValue]<q_range_min%200..1-++[SAXSInstrument],[Instrument]^-[SAXSInstrument],[QuantityValue],[Instrument])

## Parents

 *  is_a: [Instrument](Instrument.md) - An instrument used to collect data

## Attributes


### Own

 * [➞q_range_min](sAXSInstrument__q_range_min.md)  <sub>0..1</sub>
     * Description: Minimum q value in inverse Angstroms
     * Range: [QuantityValue](QuantityValue.md)
 * [➞q_range_max](sAXSInstrument__q_range_max.md)  <sub>0..1</sub>
     * Description: Maximum q value in inverse Angstroms
     * Range: [QuantityValue](QuantityValue.md)
 * [➞detector_distance_min](sAXSInstrument__detector_distance_min.md)  <sub>0..1</sub>
     * Description: Minimum detector distance in mm
     * Range: [QuantityValue](QuantityValue.md)
 * [➞detector_distance_max](sAXSInstrument__detector_distance_max.md)  <sub>0..1</sub>
     * Description: Maximum detector distance in mm
     * Range: [QuantityValue](QuantityValue.md)
 * [➞sample_changer_capacity](sAXSInstrument__sample_changer_capacity.md)  <sub>0..1</sub>
     * Description: Number of samples in automatic sample changer
     * Range: [QuantityValue](QuantityValue.md)
 * [➞temperature_control_range](sAXSInstrument__temperature_control_range.md)  <sub>0..1</sub>
     * Description: Temperature control range in Celsius
     * Range: [String](types/String.md)

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
