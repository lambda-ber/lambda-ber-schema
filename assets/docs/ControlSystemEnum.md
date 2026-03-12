
# Enum: ControlSystemEnum

Low-level control systems and middleware frameworks for device communication and hardware abstraction at experimental facilities. These provide the foundation layer that data acquisition systems build upon.

URI: [lambda:ControlSystemEnum](http://w3id.org/lambda/ControlSystemEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| epics | Experimental Physics and Industrial Control System - open-source control system framework widely used at accelerators and large experimental facilities worldwide. Provides distributed control with Channel Access protocol, IOCs (Input/Output Controllers), and extensive tool ecosystem. |  | {'annotations': {'website': Annotation(tag='website', value='https://epics-controls.org/', extensions={}, annotations={}), 'github': Annotation(tag='github', value='https://github.com/epics-base', extensions={}, annotations={}), 'facilities': Annotation(tag='facilities', value='Most US synchrotrons (ALS, APS, NSLS-II, SSRL), many international facilities', extensions={}, annotations={})}, 'title': 'EPICS'} |
| tango | Object-oriented distributed control system developed at ESRF. Provides device servers, a naming service, and tools for building control applications. Widely adopted at European synchrotrons and other facilities. |  | {'annotations': {'website': Annotation(tag='website', value='https://www.tango-controls.org/', extensions={}, annotations={}), 'github': Annotation(tag='github', value='https://github.com/tango-controls', extensions={}, annotations={}), 'facilities': Annotation(tag='facilities', value='ESRF, ALBA, MAX IV, SOLEIL, DESY, ELETTRA', extensions={}, annotations={})}, 'title': 'Tango Controls'} |
| labview | Graphical programming environment from National Instruments for instrument control and data acquisition. Used at some laboratory and smaller-scale facilities for custom instrument integration. |  | {'annotations': {'website': Annotation(tag='website', value='https://www.ni.com/labview', extensions={}, annotations={})}, 'title': 'LabVIEW'} |
| opi | Operator Interface - legacy control system used at ALS before EPICS adoption. Historical reference for older beamline configurations. |  | {'title': 'OPI'} |
