# Enum: PhasingMethodEnum 




_Methods for phase determination in X-ray crystallography_



URI: [lambdaber:PhasingMethodEnum](https://w3id.org/lambda-ber-schema/PhasingMethodEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| molecular_replacement | None | Molecular replacement (MR) |
| sad | None | Single-wavelength anomalous diffraction (SAD) |
| mad | None | Multi-wavelength anomalous diffraction (MAD) |
| sir | None | Single isomorphous replacement (SIR) |
| mir | None | Multiple isomorphous replacement (MIR) |
| siras | None | Single isomorphous replacement with anomalous scattering (SIRAS) |
| miras | None | Multiple isomorphous replacement with anomalous scattering (MIRAS) |
| fragile_mr | None | Fragile molecular replacement or ensemble-based MR |




## Slots

| Name | Description |
| ---  | --- |
| [phasing_method](phasing_method.md) | Phasing method used for X-ray crystallography structure determination |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: PhasingMethodEnum
description: Methods for phase determination in X-ray crystallography
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  molecular_replacement:
    text: molecular_replacement
    description: Molecular replacement (MR)
  sad:
    text: sad
    description: Single-wavelength anomalous diffraction (SAD)
  mad:
    text: mad
    description: Multi-wavelength anomalous diffraction (MAD)
  sir:
    text: sir
    description: Single isomorphous replacement (SIR)
  mir:
    text: mir
    description: Multiple isomorphous replacement (MIR)
  siras:
    text: siras
    description: Single isomorphous replacement with anomalous scattering (SIRAS)
  miras:
    text: miras
    description: Multiple isomorphous replacement with anomalous scattering (MIRAS)
  fragile_mr:
    text: fragile_mr
    description: Fragile molecular replacement or ensemble-based MR

```
</details>