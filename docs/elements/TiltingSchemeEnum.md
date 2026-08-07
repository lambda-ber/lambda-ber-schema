# Enum: TiltingSchemeEnum 




_Tilt scheme used during tomographic or continuous-rotation data collection_



URI: [lambda:TiltingSchemeEnum](http://w3id.org/lambda/TiltingSchemeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| none | None | No tilting performed (single exposure or non-tilt acquisition) |
| dose_symmetric | None | Dose-symmetric tilt scheme alternating around zero tilt to minimize accumulat... |
| linear | None | Linear tilt scheme collecting images in a single sweep from minimum to maximu... |
| continuous | None | Continuous rotation data collection (e |




## Slots

| Name | Description |
| ---  | --- |
| [tilting_scheme](tilting_scheme.md) | Tilt scheme used during tomographic data collection |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: TiltingSchemeEnum
description: Tilt scheme used during tomographic or continuous-rotation data collection
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  none:
    text: none
    description: No tilting performed (single exposure or non-tilt acquisition)
  dose_symmetric:
    text: dose_symmetric
    description: Dose-symmetric tilt scheme alternating around zero tilt to minimize
      accumulated dose at low tilt angles
  linear:
    text: linear
    description: Linear tilt scheme collecting images in a single sweep from minimum
      to maximum tilt
  continuous:
    text: continuous
    description: Continuous rotation data collection (e.g., used in MicroED/3DED)

```
</details>