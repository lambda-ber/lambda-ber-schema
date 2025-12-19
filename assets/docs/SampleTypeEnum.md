# Enum: SampleTypeEnum 




_Types of biological samples_



URI: [lambdaber:SampleTypeEnum](https://w3id.org/lambda-ber-schema/SampleTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| protein | None | Protein sample |
| nucleic_acid | None | Nucleic acid sample (DNA or RNA) |
| complex | None | Protein-protein or protein-nucleic acid complex |
| membrane_protein | None | Membrane protein sample |
| virus | None | Viral particle |
| organelle | None | Cellular organelle |




## Slots

| Name | Description |
| ---  | --- |
| [sample_type](sample_type.md) | Type of biological sample |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: SampleTypeEnum
description: Types of biological samples
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  protein:
    text: protein
    description: Protein sample
  nucleic_acid:
    text: nucleic_acid
    description: Nucleic acid sample (DNA or RNA)
  complex:
    text: complex
    description: Protein-protein or protein-nucleic acid complex
  membrane_protein:
    text: membrane_protein
    description: Membrane protein sample
  virus:
    text: virus
    description: Viral particle
  organelle:
    text: organelle
    description: Cellular organelle

```
</details>