

# Slot: unit 


_The unit of measurement. Should be taken from the UCUM unit collection or the Unit Ontology. Examples include Angstroms, micrometers, kilodaltons, degrees._





URI: [lambda:unit](http://w3id.org/lambda/unit)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:unit |
| native | lambda:unit |
| undefined | nmdc:unit, qud:unit, schema:unitCode, UO:0000000 |




## LinkML Source

<details>
```yaml
name: unit
description: The unit of measurement. Should be taken from the UCUM unit collection
  or the Unit Ontology. Examples include Angstroms, micrometers, kilodaltons, degrees.
from_schema: http://w3id.org/lambda/
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