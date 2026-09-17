# Enum: SampleNucleicAcidRoleEnum 




_Part a nucleic acid plays in a sample_



URI: [lambda:SampleNucleicAcidRoleEnum](http://w3id.org/lambda/SampleNucleicAcidRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| target | None | The nucleic acid under investigation |
| subunit | None | One strand of a duplex, or one chain of an assembly, that is the target as a ... |
| binding_partner | None | A nucleic acid present for its interaction with the target, such as the DNA s... |
| template | None | The strand a polymerase or reverse transcriptase reads |
| primer | None | The strand a polymerase extends |
| guide | None | A guide RNA or DNA that directs a nuclease or other effector to its target (e |
| scaffold | None | A nucleic acid used as a structural scaffold, as in DNA origami or a nanopart... |
| contaminant | None | A nucleic acid present unintentionally and identified after the fact, such as... |
| standard | None | A reference nucleic acid added for calibration or as a size marker |








## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: SampleNucleicAcidRoleEnum
description: Part a nucleic acid plays in a sample
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  target:
    text: target
    description: The nucleic acid under investigation
  subunit:
    text: subunit
    description: One strand of a duplex, or one chain of an assembly, that is the
      target as a whole
  binding_partner:
    text: binding_partner
    description: A nucleic acid present for its interaction with the target, such
      as the DNA site a transcription factor binds, an aptamer, or an enzyme substrate
  template:
    text: template
    description: The strand a polymerase or reverse transcriptase reads
  primer:
    text: primer
    description: The strand a polymerase extends
  guide:
    text: guide
    description: A guide RNA or DNA that directs a nuclease or other effector to its
      target (e.g., sgRNA, crRNA)
  scaffold:
    text: scaffold
    description: A nucleic acid used as a structural scaffold, as in DNA origami or
      a nanoparticle assembly
  contaminant:
    text: contaminant
    description: A nucleic acid present unintentionally and identified after the fact,
      such as host DNA co-purified with a protein
  standard:
    text: standard
    description: A reference nucleic acid added for calibration or as a size marker

```
</details>