# Enum: DetectorTechnologyEnum 




_Generic detector technologies for structural biology imaging_



URI: [lambdaber:DetectorTechnologyEnum](https://w3id.org/lambda-ber-schema/DetectorTechnologyEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| direct_electron_detector | None | Direct electron detector for cryo-EM (e |
| ccd | None | Charge-coupled device camera |
| cmos | None | Complementary metal-oxide-semiconductor detector |
| hybrid_photon_counting | None | Hybrid pixel photon counting detector for X-ray crystallography |
| scintillator_coupled | None | Scintillator-coupled indirect detection |
| imaging_plate | None | Imaging plate detector |
| film | None | Photographic film |




## Slots

| Name | Description |
| ---  | --- |
| [detector_technology](detector_technology.md) | Generic detector technology type |





## Comments

* Separates detector technology from manufacturer/model for better ontology mapping
* Use detector_manufacturer and detector_model fields for specific equipment details

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: DetectorTechnologyEnum
description: Generic detector technologies for structural biology imaging
comments:
- Separates detector technology from manufacturer/model for better ontology mapping
- Use detector_manufacturer and detector_model fields for specific equipment details
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  direct_electron_detector:
    text: direct_electron_detector
    description: Direct electron detector for cryo-EM (e.g., Gatan K2/K3, ThermoFisher
      Falcon, DirectElectron DE-64)
    comments:
    - Modern cryo-EM detectors with direct electron counting capability
  ccd:
    text: ccd
    description: Charge-coupled device camera
    comments:
    - Used in both cryo-EM (older systems) and X-ray crystallography
  cmos:
    text: cmos
    description: Complementary metal-oxide-semiconductor detector
    comments:
    - Used in both cryo-EM and X-ray crystallography (e.g., Rigaku HyPix, Bruker PIXIUM)
  hybrid_photon_counting:
    text: hybrid_photon_counting
    description: Hybrid pixel photon counting detector for X-ray crystallography
    comments:
    - Modern X-ray detectors (e.g., Dectris EIGER/PILATUS, Bruker PHOTON)
  scintillator_coupled:
    text: scintillator_coupled
    description: Scintillator-coupled indirect detection
    comments:
    - Indirect detection via scintillator conversion
  imaging_plate:
    text: imaging_plate
    description: Imaging plate detector
    comments:
    - Storage phosphor technology, historically common in X-ray crystallography
  film:
    text: film
    description: Photographic film
    comments:
    - Legacy detector type for historical datasets

```
</details>