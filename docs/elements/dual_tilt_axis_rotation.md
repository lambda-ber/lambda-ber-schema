

# Slot: dual_tilt_axis_rotation 


_Rotation between the two tilt axes in a dual-axis tomography acquisition, typically specified in degrees. Omit for the far more common single-axis case._





URI: [lambda:dual_tilt_axis_rotation](http://w3id.org/lambda/dual_tilt_axis_rotation)
Alias: dual_tilt_axis_rotation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:dual_tilt_axis_rotation |
| native | lambda:dual_tilt_axis_rotation |
| exact | mmCIF:_em_tomography.dual_tilt_axis_rotation |




## LinkML Source

<details>
```yaml
name: dual_tilt_axis_rotation
description: Rotation between the two tilt axes in a dual-axis tomography acquisition,
  typically specified in degrees. Omit for the far more common single-axis case.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_tomography.dual_tilt_axis_rotation
rank: 1000
alias: dual_tilt_axis_rotation
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>