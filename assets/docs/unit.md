

# Slot: unit 


_The unit of measurement. Should be taken from the UCUM unit collection or the Unit Ontology. Examples include Angstroms, micrometers, kilodaltons, degrees._





URI: [lambdaber:unit](https://w3id.org/lambda-ber-schema/unit)
Alias: unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |  no  |
| [QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |  yes  |






## Properties

* Range: [String](String.md)



## Aliases


* scale


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:unit |
| native | lambdaber:unit |
| undefined | nmdc:unit, qud:unit, schema:unitCode, UO:0000000 |




## LinkML Source

<details>
```yaml
name: unit
description: The unit of measurement. Should be taken from the UCUM unit collection
  or the Unit Ontology. Examples include Angstroms, micrometers, kilodaltons, degrees.
from_schema: https://w3id.org/lambda-ber-schema/
aliases:
- scale
mappings:
- nmdc:unit
- qud:unit
- schema:unitCode
- UO:0000000
rank: 1000
alias: unit
domain_of:
- QuantityValue
- BiophysicalProperty
range: string

```
</details>