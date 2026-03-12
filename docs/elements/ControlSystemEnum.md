# Enum: ControlSystemEnum 




_Low-level control systems and middleware frameworks for device communication and hardware abstraction at experimental facilities. These provide the foundation layer that data acquisition systems build upon._



URI: [lambdaber:ControlSystemEnum](https://w3id.org/lambda-ber-schema/ControlSystemEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| epics | None | Experimental Physics and Industrial Control System - open-source control syst... |
| tango | None | Object-oriented distributed control system developed at ESRF |
| labview | None | Graphical programming environment from National Instruments for instrument co... |
| opi | None | Operator Interface - legacy control system used at ALS before EPICS adoption |




## Slots

| Name | Description |
| ---  | --- |
| [control_system](control_system.md) | Low-level control system for device communication |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: ControlSystemEnum
description: Low-level control systems and middleware frameworks for device communication
  and hardware abstraction at experimental facilities. These provide the foundation
  layer that data acquisition systems build upon.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  epics:
    text: epics
    description: Experimental Physics and Industrial Control System - open-source
      control system framework widely used at accelerators and large experimental
      facilities worldwide. Provides distributed control with Channel Access protocol,
      IOCs (Input/Output Controllers), and extensive tool ecosystem.
    annotations:
      website:
        tag: website
        value: https://epics-controls.org/
      github:
        tag: github
        value: https://github.com/epics-base
      facilities:
        tag: facilities
        value: Most US synchrotrons (ALS, APS, NSLS-II, SSRL), many international
          facilities
    title: EPICS
  tango:
    text: tango
    description: Object-oriented distributed control system developed at ESRF. Provides
      device servers, a naming service, and tools for building control applications.
      Widely adopted at European synchrotrons and other facilities.
    annotations:
      website:
        tag: website
        value: https://www.tango-controls.org/
      github:
        tag: github
        value: https://github.com/tango-controls
      facilities:
        tag: facilities
        value: ESRF, ALBA, MAX IV, SOLEIL, DESY, ELETTRA
    title: Tango Controls
  labview:
    text: labview
    description: Graphical programming environment from National Instruments for instrument
      control and data acquisition. Used at some laboratory and smaller-scale facilities
      for custom instrument integration.
    annotations:
      website:
        tag: website
        value: https://www.ni.com/labview
    title: LabVIEW
  opi:
    text: opi
    description: Operator Interface - legacy control system used at ALS before EPICS
      adoption. Historical reference for older beamline configurations.
    title: OPI

```
</details>