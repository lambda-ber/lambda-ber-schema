# Enum: NucleicAcidSourceEnum 




_How a nucleic acid strand was produced for a preparation_



URI: [lambda:NucleicAcidSourceEnum](http://w3id.org/lambda/NucleicAcidSourceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| chemical_synthesis | None | Solid-phase chemical synthesis, as for most oligonucleotides |
| in_vitro_transcription | None | Transcribed in vitro, typically by T7 RNA polymerase from a DNA template |
| pcr_amplification | None | Amplified by PCR |
| plasmid_preparation | None | Purified as plasmid DNA from a host |
| isolated_from_organism | None | Purified from cells, tissue or virions without amplification, as for native t... |
| other | None | A method not listed, described in the association's description |




## Slots

| Name | Description |
| ---  | --- |
| [source_method](source_method.md) | How this strand was made for this preparation: chemical synthesis, in vitro t... |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: NucleicAcidSourceEnum
description: How a nucleic acid strand was produced for a preparation
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  chemical_synthesis:
    text: chemical_synthesis
    description: Solid-phase chemical synthesis, as for most oligonucleotides
  in_vitro_transcription:
    text: in_vitro_transcription
    description: Transcribed in vitro, typically by T7 RNA polymerase from a DNA template
  pcr_amplification:
    text: pcr_amplification
    description: Amplified by PCR
  plasmid_preparation:
    text: plasmid_preparation
    description: Purified as plasmid DNA from a host
  isolated_from_organism:
    text: isolated_from_organism
    description: Purified from cells, tissue or virions without amplification, as
      for native tRNA or genomic DNA
  other:
    text: other
    description: A method not listed, described in the association's description

```
</details>