# Enum: StabilityEffectEnum 




_Effect on protein stability_



URI: [lambdaber:StabilityEffectEnum](https://w3id.org/lambda-ber-schema/StabilityEffectEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| stabilizing | None | Increases stability |
| destabilizing | None | Decreases stability |
| neutral | None | No significant effect |
| highly_stabilizing | None | Strongly increases stability |
| highly_destabilizing | None | Strongly decreases stability |




## Slots

| Name | Description |
| ---  | --- |
| [effect_on_stability](effect_on_stability.md) | Effect on protein stability |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: StabilityEffectEnum
description: Effect on protein stability
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  stabilizing:
    text: stabilizing
    description: Increases stability
  destabilizing:
    text: destabilizing
    description: Decreases stability
  neutral:
    text: neutral
    description: No significant effect
  highly_stabilizing:
    text: highly_stabilizing
    description: Strongly increases stability
  highly_destabilizing:
    text: highly_destabilizing
    description: Strongly decreases stability

```
</details>