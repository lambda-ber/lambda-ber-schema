

# Slot: map_sharpening_bfactor 


_B-factor used for map sharpening, typically specified in Angstroms squared (Å²). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [lambda:map_sharpening_bfactor](http://w3id.org/lambda/map_sharpening_bfactor)
Alias: map_sharpening_bfactor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RefinementParameters](RefinementParameters.md) | Parameters specific to 3D refinement workflows |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:map_sharpening_bfactor |
| native | lambda:map_sharpening_bfactor |




## LinkML Source

<details>
```yaml
name: map_sharpening_bfactor
description: B-factor used for map sharpening, typically specified in Angstroms squared
  (Å²). Data providers may specify alternative units by including the unit in the
  QuantityValue.
from_schema: http://w3id.org/lambda/
rank: 1000
alias: map_sharpening_bfactor
owner: RefinementParameters
domain_of:
- RefinementParameters
range: QuantityValue
inlined: true

```
</details>