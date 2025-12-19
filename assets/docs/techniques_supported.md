

# Slot: techniques_supported 


_Experimental techniques available at this beamline_





URI: [lambdaber:techniques_supported](https://w3id.org/lambda-ber-schema/techniques_supported)
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


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:techniques_supported |
| native | lambdaber:techniques_supported |




## LinkML Source

<details>
```yaml
name: techniques_supported
description: Experimental techniques available at this beamline
comments:
- List all techniques this beamline supports
- 'Example: [saxs, xray_crystallography] for SIBYLS'
from_schema: https://w3id.org/lambda-ber-schema/
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