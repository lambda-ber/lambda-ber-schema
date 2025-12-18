# Enum: DetectorTypeEnum  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 




_DEPRECATED: Use DetectorTechnologyEnum instead. Legacy enum mixing technologies and brands._



URI: [lambdaber:DetectorTypeEnum](https://w3id.org/lambda-ber-schema/DetectorTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| direct_electron | None | Direct electron detector |
| ccd | None | CCD camera |
| cmos | None | CMOS detector |
| hybrid_pixel | None | Hybrid pixel detector |
| eiger | None | Dectris EIGER detector (hybrid photon counting) |
| pilatus | None | Dectris PILATUS detector |
| rayonix | None | Rayonix CCD detector |
| adsc | None | ADSC CCD detector |
| mar | None | MAR CCD or imaging plate detector |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: DetectorTypeEnum
description: 'DEPRECATED: Use DetectorTechnologyEnum instead. Legacy enum mixing technologies
  and brands.'
deprecated: Use DetectorTechnologyEnum for detector technology, and separate manufacturer/model
  fields
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  direct_electron:
    text: direct_electron
    description: Direct electron detector
  ccd:
    text: ccd
    description: CCD camera
  cmos:
    text: cmos
    description: CMOS detector
  hybrid_pixel:
    text: hybrid_pixel
    description: Hybrid pixel detector
  eiger:
    text: eiger
    description: Dectris EIGER detector (hybrid photon counting)
  pilatus:
    text: pilatus
    description: Dectris PILATUS detector
  rayonix:
    text: rayonix
    description: Rayonix CCD detector
  adsc:
    text: adsc
    description: ADSC CCD detector
  mar:
    text: mar
    description: MAR CCD or imaging plate detector

```
</details>