

# Slot: voltage_used_in_estimation 


_Accelerating voltage value used during CTF estimation, typically specified in kilovolts (kV); may differ from instrument specification. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambdaber:voltage_used_in_estimation](https://w3id.org/lambda-ber-schema/voltage_used_in_estimation)
Alias: voltage_used_in_estimation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CTFEstimationParameters](CTFEstimationParameters.md) | Parameters specific to CTF estimation workflows |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:voltage_used_in_estimation |
| native | lambdaber:voltage_used_in_estimation |




## LinkML Source

<details>
```yaml
name: voltage_used_in_estimation
description: Accelerating voltage value used during CTF estimation, typically specified
  in kilovolts (kV); may differ from instrument specification. Data providers may
  specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: voltage_used_in_estimation
owner: CTFEstimationParameters
domain_of:
- CTFEstimationParameters
range: QuantityValue
inlined: true

```
</details>