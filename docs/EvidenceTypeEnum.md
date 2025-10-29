# Enum: EvidenceTypeEnum 




_Types of evidence_



URI: [lambdaber:EvidenceTypeEnum](https://w3id.org/lambda-ber-schema/EvidenceTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| experimental | None | Direct experimental evidence |
| predicted | None | Computational prediction |
| inferred | None | Inferred from homology |
| literature | None | Literature curation |
| author_statement | None | Author statement |
| curator_inference | None | Curator inference |




## Slots

| Name | Description |
| ---  | --- |
| [evidence_type](evidence_type.md) | Type of evidence supporting this annotation |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: EvidenceTypeEnum
description: Types of evidence
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  experimental:
    text: experimental
    description: Direct experimental evidence
  predicted:
    text: predicted
    description: Computational prediction
  inferred:
    text: inferred
    description: Inferred from homology
  literature:
    text: literature
    description: Literature curation
  author_statement:
    text: author_statement
    description: Author statement
  curator_inference:
    text: curator_inference
    description: Curator inference

```
</details>