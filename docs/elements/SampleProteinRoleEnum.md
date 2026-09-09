# Enum: SampleProteinRoleEnum 




_Part a protein plays in a sample_



URI: [lambda:SampleProteinRoleEnum](http://w3id.org/lambda/SampleProteinRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| target | None | The protein under investigation |
| subunit | None | One subunit of a complex that is the target as a whole |
| binding_partner | None | A protein present for its interaction with the target, such as a substrate, i... |
| fusion_partner | None | A solubility or affinity fusion partner left attached (e |
| chaperone | None | A chaperone or scaffold added to stabilize or reconstitute the target |
| contaminant | None | A protein present unintentionally and identified after the fact |
| standard | None | A reference protein added for calibration or as a size marker |








## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: SampleProteinRoleEnum
description: Part a protein plays in a sample
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  target:
    text: target
    description: The protein under investigation
  subunit:
    text: subunit
    description: One subunit of a complex that is the target as a whole
  binding_partner:
    text: binding_partner
    description: A protein present for its interaction with the target, such as a
      substrate, inhibitor or antibody
  fusion_partner:
    text: fusion_partner
    description: A solubility or affinity fusion partner left attached (e.g., MBP,
      GST, GFP)
  chaperone:
    text: chaperone
    description: A chaperone or scaffold added to stabilize or reconstitute the target
  contaminant:
    text: contaminant
    description: A protein present unintentionally and identified after the fact
  standard:
    text: standard
    description: A reference protein added for calibration or as a size marker

```
</details>