# Enum: ExperimentalMethodEnum 




_Experimental methods for structure determination_



URI: [lambda:ExperimentalMethodEnum](http://w3id.org/lambda/ExperimentalMethodEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| x_ray_diffraction | CHMO:0000156 | X-ray diffraction |
| neutron_diffraction | None | Neutron diffraction |
| electron_diffraction | None | Electron diffraction (e |
| fiber_diffraction | None | Fiber diffraction |




## Slots

| Name | Description |
| ---  | --- |
| [experimental_method](experimental_method.md) | Specific experimental method for structure determination (particularly for di... |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: ExperimentalMethodEnum
description: Experimental methods for structure determination
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  x_ray_diffraction:
    text: x_ray_diffraction
    description: X-ray diffraction
    meaning: CHMO:0000156
  neutron_diffraction:
    text: neutron_diffraction
    description: Neutron diffraction
  electron_diffraction:
    text: electron_diffraction
    description: Electron diffraction (e.g., microED)
  fiber_diffraction:
    text: fiber_diffraction
    description: Fiber diffraction

```
</details>