# Enum: LIMSSystemEnum 




_Laboratory Information Management Systems (LIMS) used at structural biology facilities to manage samples, experiments, and data workflows. These systems track samples from shipment through data collection and processing._



URI: [lambdaber:LIMSSystemEnum](https://w3id.org/lambda-ber-schema/LIMSSystemEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ispyb | None | Information System for Protein crystallography Beamlines - the community-main... |
| ispyb_diamond | None | Diamond Light Source variant of ISPyB, the original reference implementation |
| icat | None | ICAT is a metadata catalogue and data management system designed to support l... |
| mxlive | None | Web-based LIMS developed at the Canadian Light Source for macromolecular crys... |
| mxcube_lims | None | Macromolecular Crystallography Beamline Control Unit Environment - a unified ... |
| user_office | None | Generic facility user office or proposal management system for tracking beam ... |




## Slots

| Name | Description |
| ---  | --- |
| [lims_system](lims_system.md) | Laboratory Information Management System used at this beamline |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: LIMSSystemEnum
description: Laboratory Information Management Systems (LIMS) used at structural biology
  facilities to manage samples, experiments, and data workflows. These systems track
  samples from shipment through data collection and processing.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  ispyb:
    text: ispyb
    description: Information System for Protein crystallography Beamlines - the community-maintained
      variant developed collaboratively by ESRF, MAX IV, SOLEIL, ALBA, and other facilities.
      Provides comprehensive tracking of samples, data collections, and processing
      results for macromolecular crystallography. The py-ispyb Python API targets
      this variant.
    annotations:
      github:
        tag: github
        value: https://github.com/ispyb/ispyb-database-modeling
      api_github:
        tag: api_github
        value: https://github.com/ispyb/py-ispyb
      publication:
        tag: publication
        value: https://doi.org/10.1093/bioinformatics/btr535
      facilities:
        tag: facilities
        value: ESRF, MAX IV, SOLEIL, ALBA
    title: ISPyB (Community)
  ispyb_diamond:
    text: ispyb_diamond
    description: Diamond Light Source variant of ISPyB, the original reference implementation.
      Tightly integrated with Diamond's infrastructure and SynchWeb web interface.
      Shares core schema with community ISPyB but has diverged in extensions and APIs.
    annotations:
      github:
        tag: github
        value: https://github.com/DiamondLightSource/ispyb-database
      synchweb_publication:
        tag: synchweb_publication
        value: https://doi.org/10.1107/S1600577515005317
      facilities:
        tag: facilities
        value: Diamond Light Source
    title: ISPyB (Diamond)
  icat:
    text: icat
    description: ICAT is a metadata catalogue and data management system designed
      to support large facility experimental data. Used primarily at neutron and photon
      sources for cataloging experimental data with rich metadata and providing data
      access APIs.
    annotations:
      website:
        tag: website
        value: https://icatproject.org/
      github:
        tag: github
        value: https://github.com/icatproject
      facilities:
        tag: facilities
        value: ISIS, Diamond, ESRF, ILL, ORNL
    title: ICAT
  mxlive:
    text: mxlive
    description: Web-based LIMS developed at the Canadian Light Source for macromolecular
      crystallography beamlines. Provides sample tracking, data collection scheduling,
      and integration with automated data processing pipelines.
    annotations:
      facilities:
        tag: facilities
        value: Canadian Light Source
    title: MXLive
  mxcube_lims:
    text: mxcube_lims
    description: Macromolecular Crystallography Beamline Control Unit Environment
      - a unified beamline control and experiment management system. Originally developed
      at ESRF, now a collaborative project. MXCuBE3 is the modern web-based version.
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
    title: MXCuBE (LIMS)
  user_office:
    text: user_office
    description: Generic facility user office or proposal management system for tracking
      beam time proposals, user access, and administrative metadata.
    title: User Office System

```
</details>