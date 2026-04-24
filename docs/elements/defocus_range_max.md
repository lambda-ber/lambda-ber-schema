

# Slot: defocus_range_max 


_Maximum defocus range in micrometers_





URI: [lambda:defocus_range_max](http://w3id.org/lambda/defocus_range_max)
Alias: defocus_range_max

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
| self | lambda:defocus_range_max |
| native | lambda:defocus_range_max |
| exact | mmCIF:_em_imaging.nominal_defocus_max |




## LinkML Source

<details>
```yaml
name: defocus_range_max
description: Maximum defocus range in micrometers
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_imaging.nominal_defocus_max
rank: 1000
alias: defocus_range_max
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>