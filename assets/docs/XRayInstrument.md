
# Class: XRayInstrument

X-ray diffractometer or synchrotron beamline specifications

URI: [lambdaber:XRayInstrument](https://w3id.org/lambda-ber-schema/XRayInstrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<flux_density%200..1-++[XRayInstrument&#124;source_type:XRaySourceTypeEnum%20%3F;detector_technology:DetectorTechnologyEnum%20%3F;detector_manufacturer:string%20%3F;detector_model:string%20%3F;monochromator_type:string%20%3F;goniometer_type:string%20%3F;crystal_cooling_capability:boolean%20%3F;instrument_code(i):string;instrument_category(i):InstrumentCategoryEnum%20%3F;facility_name(i):FacilityEnum%20%3F;facility_ror(i):uriorcurie%20%3F;beamline_id(i):string%20%3F;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<beam_size_max%200..1-++[XRayInstrument],[QuantityValue]<beam_size_min%200..1-++[XRayInstrument],[QuantityValue]<energy_max%200..1-++[XRayInstrument],[QuantityValue]<energy_min%200..1-++[XRayInstrument],[Instrument]^-[XRayInstrument],[QuantityValue],[Instrument])](https://yuml.me/diagram/nofunky;dir:TB/class/[QuantityValue]<flux_density%200..1-++[XRayInstrument&#124;source_type:XRaySourceTypeEnum%20%3F;detector_technology:DetectorTechnologyEnum%20%3F;detector_manufacturer:string%20%3F;detector_model:string%20%3F;monochromator_type:string%20%3F;goniometer_type:string%20%3F;crystal_cooling_capability:boolean%20%3F;instrument_code(i):string;instrument_category(i):InstrumentCategoryEnum%20%3F;facility_name(i):FacilityEnum%20%3F;facility_ror(i):uriorcurie%20%3F;beamline_id(i):string%20%3F;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[QuantityValue]<beam_size_max%200..1-++[XRayInstrument],[QuantityValue]<beam_size_min%200..1-++[XRayInstrument],[QuantityValue]<energy_max%200..1-++[XRayInstrument],[QuantityValue]<energy_min%200..1-++[XRayInstrument],[Instrument]^-[XRayInstrument],[QuantityValue],[Instrument])

## Parents

 *  is_a: [Instrument](Instrument.md) - An instrument used to collect data

## Attributes


### Own

 * [➞source_type](xRayInstrument__source_type.md)  <sub>0..1</sub>
     * Description: Type of X-ray source
     * Range: [XRaySourceTypeEnum](XRaySourceTypeEnum.md)
 * [➞detector_technology](xRayInstrument__detector_technology.md)  <sub>0..1</sub>
     * Description: Generic detector technology type
     * Range: [DetectorTechnologyEnum](DetectorTechnologyEnum.md)
 * [➞detector_manufacturer](xRayInstrument__detector_manufacturer.md)  <sub>0..1</sub>
     * Description: Detector manufacturer (e.g., Dectris, Bruker, Rigaku, Rayonix)
     * Range: [String](types/String.md)
 * [➞detector_model](xRayInstrument__detector_model.md)  <sub>0..1</sub>
     * Description: Detector model (e.g., EIGER2 X 16M, PILATUS3 X 6M, PHOTON III)
     * Range: [String](types/String.md)
 * [➞energy_min](xRayInstrument__energy_min.md)  <sub>0..1</sub>
     * Description: Minimum X-ray energy in keV
     * Range: [QuantityValue](QuantityValue.md)
 * [➞energy_max](xRayInstrument__energy_max.md)  <sub>0..1</sub>
     * Description: Maximum X-ray energy in keV
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_size_min](xRayInstrument__beam_size_min.md)  <sub>0..1</sub>
     * Description: Minimum beam size in micrometers
     * Range: [QuantityValue](QuantityValue.md)
 * [➞beam_size_max](xRayInstrument__beam_size_max.md)  <sub>0..1</sub>
     * Description: Maximum beam size in micrometers
     * Range: [QuantityValue](QuantityValue.md)
 * [➞flux_density](xRayInstrument__flux_density.md)  <sub>0..1</sub>
     * Description: Photon flux density in photons/s/mm²
     * Range: [QuantityValue](QuantityValue.md)
 * [➞monochromator_type](xRayInstrument__monochromator_type.md)  <sub>0..1</sub>
     * Description: Type of monochromator
     * Range: [String](types/String.md)
 * [➞goniometer_type](xRayInstrument__goniometer_type.md)  <sub>0..1</sub>
     * Description: Type of goniometer
     * Range: [String](types/String.md)
 * [➞crystal_cooling_capability](xRayInstrument__crystal_cooling_capability.md)  <sub>0..1</sub>
     * Description: Crystal cooling system available
     * Range: [Boolean](types/Boolean.md)

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
