

# Slot: techniques_supported 


_Experimental techniques available at this beamline_





URI: [lambda:techniques_supported](http://w3id.org/lambda/techniques_supported)
Alias: techniques_supported

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BeamlineInstrument](BeamlineInstrument.md) | Multi-technique synchrotron beamline that supports multiple experimental meth... |  no  |






## Properties

* Range: [TechniqueEnum](TechniqueEnum.md)

* Multivalued: True

* Required: True




## Comments

* List all techniques this beamline supports
* Example: [saxs, xray_crystallography] for SIBYLS

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:techniques_supported |
| native | lambda:techniques_supported |




## LinkML Source

<details>
```yaml
name: techniques_supported
description: Experimental techniques available at this beamline
comments:
- List all techniques this beamline supports
- 'Example: [saxs, xray_crystallography] for SIBYLS'
from_schema: http://w3id.org/lambda/
rank: 1000
alias: techniques_supported
owner: BeamlineInstrument
domain_of:
- BeamlineInstrument
range: TechniqueEnum
required: true
multivalued: true

```
</details>