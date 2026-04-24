# Enum: InstrumentStatusEnum 




_Operational status of instruments_



URI: [lambda:InstrumentStatusEnum](http://w3id.org/lambda/InstrumentStatusEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| operational | None | Instrument is operational |
| maintenance | None | Instrument under maintenance |
| offline | None | Instrument is offline |
| commissioning | None | Instrument being commissioned |




## Slots

| Name | Description |
| ---  | --- |
| [current_status](current_status.md) | Current operational status |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: InstrumentStatusEnum
description: Operational status of instruments
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  operational:
    text: operational
    description: Instrument is operational
  maintenance:
    text: maintenance
    description: Instrument under maintenance
  offline:
    text: offline
    description: Instrument is offline
  commissioning:
    text: commissioning
    description: Instrument being commissioned

```
</details>