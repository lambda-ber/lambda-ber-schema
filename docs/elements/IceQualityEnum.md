# Enum: IceQualityEnum 




_Assessment of vitreous ice thickness/quality for cryo-EM data collection_



URI: [lambda:IceQualityEnum](http://w3id.org/lambda/IceQualityEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ideal | None | Ice thickness is ideal for data collection |
| too_thin | None | Ice is too thin, risk of air exposure or beam damage |
| too_thick | None | Ice is too thick, reducing contrast and signal quality |




## Slots

| Name | Description |
| ---  | --- |
| [ice_quality](ice_quality.md) | Assessment of vitreous ice thickness/quality for data collection |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: IceQualityEnum
description: Assessment of vitreous ice thickness/quality for cryo-EM data collection
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  ideal:
    text: ideal
    description: Ice thickness is ideal for data collection
  too_thin:
    text: too_thin
    description: Ice is too thin, risk of air exposure or beam damage
  too_thick:
    text: too_thick
    description: Ice is too thick, reducing contrast and signal quality

```
</details>