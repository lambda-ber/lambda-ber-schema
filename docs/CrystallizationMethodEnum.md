# Enum: CrystallizationMethodEnum 




_Methods for protein crystallization_



URI: [lambdaber:CrystallizationMethodEnum](https://w3id.org/lambda-ber-schema/CrystallizationMethodEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| vapor_diffusion_hanging | None | Vapor diffusion hanging drop |
| vapor_diffusion_sitting | None | Vapor diffusion sitting drop |
| batch | None | Batch crystallization |
| microbatch | None | Microbatch under oil |
| lcp | None | Lipidic cubic phase (LCP) |
| dialysis | None | Dialysis method |
| free_interface_diffusion | None | Free interface diffusion |




## Slots

| Name | Description |
| ---  | --- |
| [crystallization_method](crystallization_method.md) | Method used for crystallization |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: CrystallizationMethodEnum
description: Methods for protein crystallization
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  vapor_diffusion_hanging:
    text: vapor_diffusion_hanging
    description: Vapor diffusion hanging drop
  vapor_diffusion_sitting:
    text: vapor_diffusion_sitting
    description: Vapor diffusion sitting drop
  batch:
    text: batch
    description: Batch crystallization
  microbatch:
    text: microbatch
    description: Microbatch under oil
  lcp:
    text: lcp
    description: Lipidic cubic phase (LCP)
  dialysis:
    text: dialysis
    description: Dialysis method
  free_interface_diffusion:
    text: free_interface_diffusion
    description: Free interface diffusion

```
</details>