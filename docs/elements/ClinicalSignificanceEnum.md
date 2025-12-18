# Enum: ClinicalSignificanceEnum 




_Clinical significance of variants_



URI: [lambdaber:ClinicalSignificanceEnum](https://w3id.org/lambda-ber-schema/ClinicalSignificanceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| pathogenic | None | Pathogenic |
| likely_pathogenic | None | Likely pathogenic |
| benign | None | Benign |
| likely_benign | None | Likely benign |
| uncertain_significance | None | Uncertain significance |




## Slots

| Name | Description |
| ---  | --- |
| [clinical_significance](clinical_significance.md) | Clinical significance |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: ClinicalSignificanceEnum
description: Clinical significance of variants
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  pathogenic:
    text: pathogenic
    description: Pathogenic
  likely_pathogenic:
    text: likely_pathogenic
    description: Likely pathogenic
  benign:
    text: benign
    description: Benign
  likely_benign:
    text: likely_benign
    description: Likely benign
  uncertain_significance:
    text: uncertain_significance
    description: Uncertain significance

```
</details>