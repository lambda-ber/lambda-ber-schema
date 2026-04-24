

# Slot: detector 


_Run-specific detector identifier or detector component used for data collection. Use this when a beamline/instrument can operate with multiple or swappable detectors and the detector identity is specific to this ExperimentRun._





URI: [lambda:detector](http://w3id.org/lambda/detector)
Alias: detector

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [String](String.md)



## Aliases


* detector_id
* detector_name


## Comments

* This is optional and distinct from Instrument-level detector model/manufacturer metadata.
* Use ExperimentInstrumentAssociation with role=detector when the detector is modeled as a separate Instrument record.

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:detector |
| native | lambda:detector |




## LinkML Source

<details>
```yaml
name: detector
description: Run-specific detector identifier or detector component used for data
  collection. Use this when a beamline/instrument can operate with multiple or swappable
  detectors and the detector identity is specific to this ExperimentRun.
comments:
- This is optional and distinct from Instrument-level detector model/manufacturer
  metadata.
- Use ExperimentInstrumentAssociation with role=detector when the detector is modeled
  as a separate Instrument record.
from_schema: http://w3id.org/lambda/
aliases:
- detector_id
- detector_name
rank: 1000
alias: detector
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string

```
</details>