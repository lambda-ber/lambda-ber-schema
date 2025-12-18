
# Class: Instrument

An instrument used to collect data

URI: [lambdaber:Instrument](https://w3id.org/lambda-ber-schema/Instrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[XRayInstrument],[SAXSInstrument],[NamedThing],[Dataset]++-%20instruments%200..*>[Instrument&#124;instrument_code:string;instrument_category:InstrumentCategoryEnum%20%3F;facility_name:FacilityEnum%20%3F;facility_ror:uriorcurie%20%3F;beamline_id:string%20%3F;manufacturer:string%20%3F;model:string%20%3F;installation_date:string%20%3F;current_status:InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[ExperimentRun]-%20instrument_id%201..1>[Instrument],[Instrument]^-[XRayInstrument],[Instrument]^-[SAXSInstrument],[Instrument]^-[CryoEMInstrument],[Instrument]^-[BeamlineInstrument],[NamedThing]^-[Instrument],[ExperimentRun],[Dataset],[CryoEMInstrument],[BeamlineInstrument])](https://yuml.me/diagram/nofunky;dir:TB/class/[XRayInstrument],[SAXSInstrument],[NamedThing],[Dataset]++-%20instruments%200..*>[Instrument&#124;instrument_code:string;instrument_category:InstrumentCategoryEnum%20%3F;facility_name:FacilityEnum%20%3F;facility_ror:uriorcurie%20%3F;beamline_id:string%20%3F;manufacturer:string%20%3F;model:string%20%3F;installation_date:string%20%3F;current_status:InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[ExperimentRun]-%20instrument_id%201..1>[Instrument],[Instrument]^-[XRayInstrument],[Instrument]^-[SAXSInstrument],[Instrument]^-[CryoEMInstrument],[Instrument]^-[BeamlineInstrument],[NamedThing]^-[Instrument],[ExperimentRun],[Dataset],[CryoEMInstrument],[BeamlineInstrument])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Children

 * [BeamlineInstrument](BeamlineInstrument.md) - Multi-technique synchrotron beamline that supports multiple experimental methods
 * [CryoEMInstrument](CryoEMInstrument.md) - Cryo-EM microscope specifications
 * [SAXSInstrument](SAXSInstrument.md) - SAXS/WAXS instrument specifications
 * [XRayInstrument](XRayInstrument.md) - X-ray diffractometer or synchrotron beamline specifications

## Referenced by Class

 *  **None** *[➞instruments](dataset__instruments.md)*  <sub>0..\*</sub>  **[Instrument](Instrument.md)**
 *  **None** *[➞instrument_id](experimentRun__instrument_id.md)*  <sub>1..1</sub>  **[Instrument](Instrument.md)**

## Attributes


### Own

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

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
