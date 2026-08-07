

# Slot: dose_per_tilt 


_Electron dose applied at each tilt step, typically specified in e-/Angstrom^2. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:dose_per_tilt](http://w3id.org/lambda/dose_per_tilt)
Alias: dose_per_tilt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* Use total_dose for the accumulated dose across the whole tilt series.

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:dose_per_tilt |
| native | lambda:dose_per_tilt |
| close | mmCIF:_em_image_recording.avg_electron_dose_per_image |




## LinkML Source

<details>
```yaml
name: dose_per_tilt
description: Electron dose applied at each tilt step, typically specified in e-/Angstrom^2.
  Data providers may specify alternative units by including the unit in the QuantityValue.
comments:
- Use total_dose for the accumulated dose across the whole tilt series.
from_schema: http://w3id.org/lambda/
close_mappings:
- mmCIF:_em_image_recording.avg_electron_dose_per_image
rank: 1000
alias: dose_per_tilt
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>