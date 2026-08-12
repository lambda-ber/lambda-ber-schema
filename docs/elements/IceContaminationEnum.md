# Enum: IceContaminationEnum 




_Assessment of ice contamination level on a cryo-EM grid_



URI: [lambda:IceContaminationEnum](http://w3id.org/lambda/IceContaminationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| none | None | No ice contamination observed |
| limited | None | Limited ice contamination that does not significantly affect data quality |
| severe | None | Severe ice contamination that significantly degrades data quality |




## Slots

| Name | Description |
| ---  | --- |
| [ice_contamination](ice_contamination.md) | Assessment of ice contamination level on the cryo-EM grid |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: IceContaminationEnum
description: Assessment of ice contamination level on a cryo-EM grid
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  none:
    text: none
    description: No ice contamination observed
  limited:
    text: limited
    description: Limited ice contamination that does not significantly affect data
      quality
  severe:
    text: severe
    description: Severe ice contamination that significantly degrades data quality

```
</details>