
# Class: CryoEMInstrument

Cryo-EM microscope specifications

URI: [lambdaber:CryoEMInstrument](https://w3id.org/lambda-ber-schema/CryoEMInstrument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument],[Instrument]^-[CryoEMInstrument&#124;accelerating_voltage:integer%20%3F;cs_corrector:boolean%20%3F;phase_plate:boolean%20%3F;detector_technology:DetectorTechnologyEnum%20%3F;detector_manufacturer:string%20%3F;detector_model:string%20%3F;detector_mode:DetectorModeEnum%20%3F;detector_position:string%20%3F;detector_dimensions:string%20%3F;pixel_size_physical_um:float%20%3F;autoloader_capacity:integer%20%3F;cs:float%20%3F;c2_aperture:float%20%3F;objective_aperture:float%20%3F;phase_plate_type:string%20%3F;energy_filter_present:boolean%20%3F;energy_filter_make:string%20%3F;energy_filter_model:string%20%3F;energy_filter_slit_width:float%20%3F;pixel_size_physical:float%20%3F;microscope_software:string%20%3F;microscope_software_version:string%20%3F;spotsize:integer%20%3F;gunlens:integer%20%3F;imaging_mode:ImagingModeEnum%20%3F;tem_beam_diameter:float%20%3F;instrument_code(i):string;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument],[Instrument]^-[CryoEMInstrument&#124;accelerating_voltage:integer%20%3F;cs_corrector:boolean%20%3F;phase_plate:boolean%20%3F;detector_technology:DetectorTechnologyEnum%20%3F;detector_manufacturer:string%20%3F;detector_model:string%20%3F;detector_mode:DetectorModeEnum%20%3F;detector_position:string%20%3F;detector_dimensions:string%20%3F;pixel_size_physical_um:float%20%3F;autoloader_capacity:integer%20%3F;cs:float%20%3F;c2_aperture:float%20%3F;objective_aperture:float%20%3F;phase_plate_type:string%20%3F;energy_filter_present:boolean%20%3F;energy_filter_make:string%20%3F;energy_filter_model:string%20%3F;energy_filter_slit_width:float%20%3F;pixel_size_physical:float%20%3F;microscope_software:string%20%3F;microscope_software_version:string%20%3F;spotsize:integer%20%3F;gunlens:integer%20%3F;imaging_mode:ImagingModeEnum%20%3F;tem_beam_diameter:float%20%3F;instrument_code(i):string;manufacturer(i):string%20%3F;model(i):string%20%3F;installation_date(i):string%20%3F;current_status(i):InstrumentStatusEnum%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [Instrument](Instrument.md) - An instrument used to collect data

## Attributes


### Own

 * [➞accelerating_voltage](cryoEMInstrument__accelerating_voltage.md)  <sub>0..1</sub>
     * Description: Accelerating voltage in kV
     * Range: [Integer](types/Integer.md)
 * [➞cs_corrector](cryoEMInstrument__cs_corrector.md)  <sub>0..1</sub>
     * Description: Spherical aberration corrector present
     * Range: [Boolean](types/Boolean.md)
 * [➞phase_plate](cryoEMInstrument__phase_plate.md)  <sub>0..1</sub>
     * Description: Phase plate available
     * Range: [Boolean](types/Boolean.md)
 * [➞detector_technology](cryoEMInstrument__detector_technology.md)  <sub>0..1</sub>
     * Description: Generic detector technology type
     * Range: [DetectorTechnologyEnum](DetectorTechnologyEnum.md)
 * [➞detector_manufacturer](cryoEMInstrument__detector_manufacturer.md)  <sub>0..1</sub>
     * Description: Detector manufacturer (e.g., Gatan, ThermoFisher, DirectElectron)
     * Range: [String](types/String.md)
 * [➞detector_model](cryoEMInstrument__detector_model.md)  <sub>0..1</sub>
     * Description: Detector model (e.g., K3, Falcon 4i, DE-64)
     * Range: [String](types/String.md)
 * [➞detector_mode](cryoEMInstrument__detector_mode.md)  <sub>0..1</sub>
     * Description: Supported or default detector operating mode
     * Range: [DetectorModeEnum](DetectorModeEnum.md)
 * [➞detector_position](cryoEMInstrument__detector_position.md)  <sub>0..1</sub>
     * Description: Physical position of detector in microscope (e.g., post-GIF, pre-column)
     * Range: [String](types/String.md)
 * [➞detector_dimensions](cryoEMInstrument__detector_dimensions.md)  <sub>0..1</sub>
     * Description: Detector dimensions in pixels (e.g., 4096x4096, 5760x4092)
     * Range: [String](types/String.md)
 * [➞pixel_size_physical_um](cryoEMInstrument__pixel_size_physical_um.md)  <sub>0..1</sub>
     * Description: Physical pixel size of the detector in micrometers
     * Range: [Float](types/Float.md)
 * [➞autoloader_capacity](cryoEMInstrument__autoloader_capacity.md)  <sub>0..1</sub>
     * Description: Number of grids the autoloader can hold
     * Range: [Integer](types/Integer.md)
 * [➞cs](cryoEMInstrument__cs.md)  <sub>0..1</sub>
     * Description: Spherical aberration (Cs) in millimeters
     * Range: [Float](types/Float.md)
 * [➞c2_aperture](cryoEMInstrument__c2_aperture.md)  <sub>0..1</sub>
     * Description: C2 aperture size in micrometers
     * Range: [Float](types/Float.md)
 * [➞objective_aperture](cryoEMInstrument__objective_aperture.md)  <sub>0..1</sub>
     * Description: Objective aperture size in micrometers
     * Range: [Float](types/Float.md)
 * [➞phase_plate_type](cryoEMInstrument__phase_plate_type.md)  <sub>0..1</sub>
     * Description: Type of phase plate if present
     * Range: [String](types/String.md)
 * [➞energy_filter_present](cryoEMInstrument__energy_filter_present.md)  <sub>0..1</sub>
     * Description: Whether energy filter is present
     * Range: [Boolean](types/Boolean.md)
 * [➞energy_filter_make](cryoEMInstrument__energy_filter_make.md)  <sub>0..1</sub>
     * Description: Energy filter manufacturer
     * Range: [String](types/String.md)
 * [➞energy_filter_model](cryoEMInstrument__energy_filter_model.md)  <sub>0..1</sub>
     * Description: Energy filter model
     * Range: [String](types/String.md)
 * [➞energy_filter_slit_width](cryoEMInstrument__energy_filter_slit_width.md)  <sub>0..1</sub>
     * Description: Energy filter slit width in eV
     * Range: [Float](types/Float.md)
 * [➞pixel_size_physical](cryoEMInstrument__pixel_size_physical.md)  <sub>0..1</sub>
     * Description: Physical pixel size in micrometers
     * Range: [Float](types/Float.md)
 * [➞microscope_software](cryoEMInstrument__microscope_software.md)  <sub>0..1</sub>
     * Description: Microscope control software (e.g., SerialEM, EPU, Leginon)
     * Range: [String](types/String.md)
 * [➞microscope_software_version](cryoEMInstrument__microscope_software_version.md)  <sub>0..1</sub>
     * Description: Software version
     * Range: [String](types/String.md)
 * [➞spotsize](cryoEMInstrument__spotsize.md)  <sub>0..1</sub>
     * Description: Electron beam spot size setting
     * Range: [Integer](types/Integer.md)
 * [➞gunlens](cryoEMInstrument__gunlens.md)  <sub>0..1</sub>
     * Description: Gun lens setting
     * Range: [Integer](types/Integer.md)
 * [➞imaging_mode](cryoEMInstrument__imaging_mode.md)  <sub>0..1</sub>
     * Description: Imaging mode for electron microscopy
     * Range: [ImagingModeEnum](ImagingModeEnum.md)
 * [➞tem_beam_diameter](cryoEMInstrument__tem_beam_diameter.md)  <sub>0..1</sub>
     * Description: TEM beam diameter in micrometers
     * Range: [Float](types/Float.md)

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
