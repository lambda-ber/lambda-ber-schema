# Enum: ComplexStabilityEnum 




_Stability of protein complexes_



URI: [lambdaber:ComplexStabilityEnum](https://w3id.org/lambda-ber-schema/ComplexStabilityEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| stable | None | Stable complex |
| transient | None | Transient interaction |
| weak | None | Weak interaction |
| strong | None | Strong interaction |
| obligate | None | Obligate complex |
| non_obligate | None | Non-obligate complex |




## Slots

| Name | Description |
| ---  | --- |
| [complex_stability](complex_stability.md) | Stability assessment of the complex |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: ComplexStabilityEnum
description: Stability of protein complexes
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  stable:
    text: stable
    description: Stable complex
  transient:
    text: transient
    description: Transient interaction
  weak:
    text: weak
    description: Weak interaction
  strong:
    text: strong
    description: Strong interaction
  obligate:
    text: obligate
    description: Obligate complex
  non_obligate:
    text: non_obligate
    description: Non-obligate complex

```
</details>