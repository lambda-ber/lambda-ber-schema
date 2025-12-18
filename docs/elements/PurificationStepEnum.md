# Enum: PurificationStepEnum 




_Protein purification steps and methods_



URI: [lambdaber:PurificationStepEnum](https://w3id.org/lambda-ber-schema/PurificationStepEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| affinity_ni_nta | None | Affinity chromatography using Ni-NTA resin |
| affinity_co_nta | None | Affinity chromatography using Co-NTA resin |
| affinity_strep | None | Affinity chromatography using Strep-tag |
| affinity_mbp | None | Affinity chromatography using maltose-binding protein (MBP) |
| affinity_gst | None | Affinity chromatography using glutathione S-transferase (GST) |
| tag_cleavage | None | Proteolytic cleavage of purification tags |
| ion_exchange | None | Ion-exchange chromatography (IEX) |
| hydrophobic_interaction | None | Hydrophobic interaction chromatography (HIC) |
| size_exclusion | None | Size-exclusion chromatography (SEC) |
| dialysis | None | Dialysis or buffer exchange |




## Slots

| Name | Description |
| ---  | --- |
| [purification_steps](purification_steps.md) | Ordered list of purification steps performed |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: PurificationStepEnum
description: Protein purification steps and methods
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  affinity_ni_nta:
    text: affinity_ni_nta
    description: Affinity chromatography using Ni-NTA resin
  affinity_co_nta:
    text: affinity_co_nta
    description: Affinity chromatography using Co-NTA resin
  affinity_strep:
    text: affinity_strep
    description: Affinity chromatography using Strep-tag
  affinity_mbp:
    text: affinity_mbp
    description: Affinity chromatography using maltose-binding protein (MBP)
  affinity_gst:
    text: affinity_gst
    description: Affinity chromatography using glutathione S-transferase (GST)
  tag_cleavage:
    text: tag_cleavage
    description: Proteolytic cleavage of purification tags
  ion_exchange:
    text: ion_exchange
    description: Ion-exchange chromatography (IEX)
  hydrophobic_interaction:
    text: hydrophobic_interaction
    description: Hydrophobic interaction chromatography (HIC)
  size_exclusion:
    text: size_exclusion
    description: Size-exclusion chromatography (SEC)
  dialysis:
    text: dialysis
    description: Dialysis or buffer exchange

```
</details>