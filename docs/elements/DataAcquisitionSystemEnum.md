# Enum: DataAcquisitionSystemEnum 




_Data acquisition (DAQ) systems for orchestrating experimental data collection at facilities. These systems coordinate hardware, execute scan sequences, and stream data and metadata during experiments._



URI: [lambda:DataAcquisitionSystemEnum](http://w3id.org/lambda/DataAcquisitionSystemEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| bluesky | None | Event-based data acquisition framework developed at NSLS-II (Brookhaven Natio... |
| spec | None | Legacy macro-based data acquisition system from Certified Scientific Software |
| sardana | None | Tango-based data acquisition and control system developed at ALBA |
| gda | None | Generic Data Acquisition - Java-based data acquisition framework developed at... |
| mxcube_daq | None | MXCuBE used as data collection interface for macromolecular crystallography |
| blu_ice | None | Data collection software developed at SSRL (Stanford Synchrotron Radiation Li... |
| jblue_ice | None | Java-based variant of Blu-Ice deployed at GM/CA (General Medicine and Cancer ... |




## Slots

| Name | Description |
| ---  | --- |
| [daq_system](daq_system.md) | Data acquisition system used for experiment orchestration |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: DataAcquisitionSystemEnum
description: Data acquisition (DAQ) systems for orchestrating experimental data collection
  at facilities. These systems coordinate hardware, execute scan sequences, and stream
  data and metadata during experiments.
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  bluesky:
    text: bluesky
    description: Event-based data acquisition framework developed at NSLS-II (Brookhaven
      National Laboratory). Uses a streaming document model with RunStart, Event,
      and RunStop documents. Built on Python with ophyd for hardware abstraction and
      databroker for data access. Increasingly adopted at ALS, APS, and international
      facilities.
    annotations:
      website:
        tag: website
        value: https://blueskyproject.io/
      github:
        tag: github
        value: https://github.com/bluesky
      event_model_github:
        tag: event_model_github
        value: https://github.com/bluesky/event-model
      databroker_github:
        tag: databroker_github
        value: https://github.com/bluesky/databroker
      publication:
        tag: publication
        value: https://doi.org/10.1080/08940886.2019.1608121
      facilities:
        tag: facilities
        value: NSLS-II, ALS (SIBYLS), APS, MAX IV
    title: Bluesky
  spec:
    text: spec
    description: Legacy macro-based data acquisition system from Certified Scientific
      Software. Long-standing standard at synchrotron beamlines, using a command-line
      interface with macro scripting. Still in use at many facilities but being replaced
      by modern alternatives.
    annotations:
      website:
        tag: website
        value: https://www.certif.com/content/spec/
    title: SPEC
  sardana:
    text: sardana
    description: Tango-based data acquisition and control system developed at ALBA.
      Provides a modular framework for beamline control with macro execution, scan
      management, and integration with Tango device servers.
    annotations:
      website:
        tag: website
        value: https://sardana-controls.org/
      github:
        tag: github
        value: https://github.com/sardana-org/sardana
      facilities:
        tag: facilities
        value: ALBA, MAX IV, SOLEIL, DESY
    title: Sardana
  gda:
    text: gda
    description: Generic Data Acquisition - Java-based data acquisition framework
      developed at Diamond Light Source. Provides beamline control, scan execution,
      and integration with EPICS and other control systems.
    annotations:
      website:
        tag: website
        value: https://www.opengda.org/
      github:
        tag: github
        value: https://github.com/openGDA
      facilities:
        tag: facilities
        value: Diamond Light Source
    title: GDA
  mxcube_daq:
    text: mxcube_daq
    description: MXCuBE used as data collection interface for macromolecular crystallography.
      Provides automated data collection strategies, sample centering, and integration
      with processing pipelines. See also mxcube_lims in LIMSSystemEnum for sample
      management.
    annotations:
      website:
        tag: website
        value: https://mxcube.github.io/mxcube/
      github:
        tag: github
        value: https://github.com/mxcube
      facilities:
        tag: facilities
        value: ESRF, MAX IV, SOLEIL, ALBA, DESY, EMBL
    title: MXCuBE (Data Collection)
  blu_ice:
    text: blu_ice
    description: Data collection software developed at SSRL (Stanford Synchrotron
      Radiation Lightsource) for macromolecular crystallography. Provides graphical
      interface for sample positioning, data collection strategy, and beamline control.
    annotations:
      publication:
        tag: publication
        value: https://doi.org/10.1107/S0909049505012719
      facilities:
        tag: facilities
        value: SSRL
    title: Blu-Ice
  jblue_ice:
    text: jblue_ice
    description: Java-based variant of Blu-Ice deployed at GM/CA (General Medicine
      and Cancer Institutes Collaborative Access Team) and SER-CAT beamlines at APS.
    annotations:
      facilities:
        tag: facilities
        value: APS (GM/CA, SER-CAT)
    title: JBluIce

```
</details>