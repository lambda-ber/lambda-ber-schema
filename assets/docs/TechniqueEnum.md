# Enum: TechniqueEnum 




_Structural biology techniques_



URI: [lambdaber:TechniqueEnum](https://w3id.org/lambda-ber-schema/TechniqueEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| cryo_em | CHMO:0002413 | Cryo-electron microscopy |
| xray_crystallography | CHMO:0000156 | X-ray crystallography |
| saxs | CHMO:0000204 | Small-angle X-ray scattering |
| waxs | CHMO:0000207 | Wide-angle X-ray scattering |
| sans | CHMO:0000184 | Small-angle neutron scattering |
| cryo_et | CHMO:0002413 | Cryo-electron tomography |
| electron_microscopy | CHMO:0000068 | General electron microscopy |
| mass_spectrometry | CHMO:0000470 | Mass spectrometry |
| xas | CHMO:0000298 | X-ray absorption spectroscopy |
| xanes | CHMO:0000305 | X-ray absorption near edge structure spectroscopy |
| exafs | CHMO:0000300 | Extended X-ray absorption fine structure spectroscopy |
| xmcd | None | X-ray magnetic circular dichroism |




## Slots

| Name | Description |
| ---  | --- |
| [techniques_supported](techniques_supported.md) | Experimental techniques available at this beamline |
| [technique](technique.md) | Technique used for data collection |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: TechniqueEnum
description: Structural biology techniques
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  cryo_em:
    text: cryo_em
    description: Cryo-electron microscopy
    meaning: CHMO:0002413
  xray_crystallography:
    text: xray_crystallography
    description: X-ray crystallography
    meaning: CHMO:0000156
    exact_mappings:
    - PaNET:01164
  saxs:
    text: saxs
    description: Small-angle X-ray scattering
    meaning: CHMO:0000204
    exact_mappings:
    - PaNET:01188
  waxs:
    text: waxs
    description: Wide-angle X-ray scattering
    meaning: CHMO:0000207
    exact_mappings:
    - PaNET:01191
  sans:
    text: sans
    description: Small-angle neutron scattering
    meaning: CHMO:0000184
    exact_mappings:
    - PaNET:01189
  cryo_et:
    text: cryo_et
    description: Cryo-electron tomography
    meaning: CHMO:0002413
    comments:
    - Uses same CHMO term as cryo_em; tomography is a specific application
  electron_microscopy:
    text: electron_microscopy
    description: General electron microscopy
    meaning: CHMO:0000068
  mass_spectrometry:
    text: mass_spectrometry
    description: Mass spectrometry
    meaning: CHMO:0000470
  xas:
    text: xas
    description: X-ray absorption spectroscopy
    meaning: CHMO:0000298
    exact_mappings:
    - PaNET:01196
  xanes:
    text: xanes
    description: X-ray absorption near edge structure spectroscopy
    meaning: CHMO:0000305
    comments:
    - Also known as NEXAFS (near-edge X-ray absorption fine structure)
    - Used for electronic structure, oxidation state, coordination geometry
    exact_mappings:
    - PaNET:01199
  exafs:
    text: exafs
    description: Extended X-ray absorption fine structure spectroscopy
    meaning: CHMO:0000300
    comments:
    - Used for local atomic structure around specific elements
    - Commonly used for metalloprotein active site characterization
    exact_mappings:
    - PaNET:01198
  xmcd:
    text: xmcd
    description: X-ray magnetic circular dichroism
    comments:
    - Element-specific magnetometry technique
    exact_mappings:
    - PaNET:01137

```
</details>