# Enum: InstrumentCategoryEnum 




_Categories of instruments based on their nature and location_



URI: [lambdaber:InstrumentCategoryEnum](https://w3id.org/lambda-ber-schema/InstrumentCategoryEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SYNCHROTRON_BEAMLINE | CHMO:0001084 | Beamline at a synchrotron light source |
| NEUTRON_BEAMLINE | None | Beamline at a neutron source |
| XFEL_BEAMLINE | None | Beamline at a free electron laser (X-ray FEL) |
| ELECTRON_MICROSCOPE | None | Electron microscope (TEM, SEM, cryo-EM) |
| BENCHTOP_XRAY | None | Benchtop X-ray diffractometer or other laboratory X-ray source |
| OPTICAL_MICROSCOPE | None | Optical or fluorescence microscope |
| SPECTROMETER | None | Spectroscopy instrument (FTIR, Raman, mass spec, etc |




## Slots

| Name | Description |
| ---  | --- |
| [instrument_category](instrument_category.md) | Category distinguishing beamlines from laboratory equipment |





## Comments

* Use to distinguish synchrotron beamlines from laboratory equipment

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: InstrumentCategoryEnum
description: Categories of instruments based on their nature and location
comments:
- Use to distinguish synchrotron beamlines from laboratory equipment
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  SYNCHROTRON_BEAMLINE:
    text: SYNCHROTRON_BEAMLINE
    description: Beamline at a synchrotron light source
    meaning: CHMO:0001084
  NEUTRON_BEAMLINE:
    text: NEUTRON_BEAMLINE
    description: Beamline at a neutron source
  XFEL_BEAMLINE:
    text: XFEL_BEAMLINE
    description: Beamline at a free electron laser (X-ray FEL)
  ELECTRON_MICROSCOPE:
    text: ELECTRON_MICROSCOPE
    description: Electron microscope (TEM, SEM, cryo-EM)
  BENCHTOP_XRAY:
    text: BENCHTOP_XRAY
    description: Benchtop X-ray diffractometer or other laboratory X-ray source
  OPTICAL_MICROSCOPE:
    text: OPTICAL_MICROSCOPE
    description: Optical or fluorescence microscope
  SPECTROMETER:
    text: SPECTROMETER
    description: Spectroscopy instrument (FTIR, Raman, mass spec, etc.)

```
</details>