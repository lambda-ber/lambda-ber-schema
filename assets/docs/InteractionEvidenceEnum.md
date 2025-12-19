# Enum: InteractionEvidenceEnum 




_Evidence for interactions_



URI: [lambdaber:InteractionEvidenceEnum](https://w3id.org/lambda-ber-schema/InteractionEvidenceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| experimental | None | Experimental evidence |
| predicted | None | Computational prediction |
| homology | None | Homology-based |
| coexpression | None | Co-expression data |
| colocalization | None | Co-localization |
| genetic | None | Genetic evidence |
| physical | None | Physical interaction |
| functional | None | Functional association |




## Slots

| Name | Description |
| ---  | --- |
| [interaction_evidence](interaction_evidence.md) | Evidence for this interaction |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: InteractionEvidenceEnum
description: Evidence for interactions
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  experimental:
    text: experimental
    description: Experimental evidence
  predicted:
    text: predicted
    description: Computational prediction
  homology:
    text: homology
    description: Homology-based
  coexpression:
    text: coexpression
    description: Co-expression data
  colocalization:
    text: colocalization
    description: Co-localization
  genetic:
    text: genetic
    description: Genetic evidence
  physical:
    text: physical
    description: Physical interaction
  functional:
    text: functional
    description: Functional association

```
</details>