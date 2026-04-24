# Enum: TechniqueEnum 




_Structural biology techniques_



URI: [lambda:TechniqueEnum](http://w3id.org/lambda/TechniqueEnum)

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
| neutron_crystallography | CHMO:0000182 | Neutron macromolecular crystallography |
| fiber_diffraction | CHMO:0000156 | Fiber diffraction for structural analysis of fibrous samples |
| time_resolved_crystallography | CHMO:0000156 | Time-resolved macromolecular crystallography |
| xray_tomography | CHMO:0002743 | X-ray computed tomography (micro-CT) for 3D imaging |




## Slots

| Name | Description |
| ---  | --- |
| [technique](technique.md) | Primary technique (should always be sans for this class) |
| [techniques_supported](techniques_supported.md) | Experimental techniques available at this beamline |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: TechniqueEnum
description: Structural biology techniques
from_schema: http://w3id.org/lambda/
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
  neutron_crystallography:
    text: neutron_crystallography
    description: Neutron macromolecular crystallography
    meaning: CHMO:0000182
    comments:
    - Also known as neutron protein crystallography or neutron macromolecular diffraction
    - Used for hydrogen/deuterium visualization in protein structures
  fiber_diffraction:
    text: fiber_diffraction
    description: Fiber diffraction for structural analysis of fibrous samples
    meaning: CHMO:0000156
    comments:
    - Used for studying filamentous proteins, DNA fibers, muscle fibers
  time_resolved_crystallography:
    text: time_resolved_crystallography
    description: Time-resolved macromolecular crystallography
    meaning: CHMO:0000156
    comments:
    - Pump-probe crystallography for capturing structural dynamics
    - Requires fast X-ray pulses (synchrotron or XFEL)
  xray_tomography:
    text: xray_tomography
    description: X-ray computed tomography (micro-CT) for 3D imaging
    meaning: CHMO:0002743
    comments:
    - Non-destructive 3D imaging technique
    - Includes micro-CT, nano-CT, and phase contrast tomography
    - Used for cellular imaging, materials science, and paleontology
    exact_mappings:
    - PaNET:01154

```
</details>