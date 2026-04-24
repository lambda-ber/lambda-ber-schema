

# Slot: defocus_range_min 


_Minimum defocus range in micrometers_





URI: [lambda:defocus_range_min](http://w3id.org/lambda/defocus_range_min)
Alias: defocus_range_min

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
| self | lambda:defocus_range_min |
| native | lambda:defocus_range_min |
| exact | mmCIF:_em_imaging.nominal_defocus_min |




## LinkML Source

<details>
```yaml
name: defocus_range_min
description: Minimum defocus range in micrometers
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_em_imaging.nominal_defocus_min
rank: 1000
alias: defocus_range_min
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>