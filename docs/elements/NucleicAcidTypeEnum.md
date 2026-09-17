# Enum: NucleicAcidTypeEnum 




_Chemical type of a nucleic acid polymer. The mmCIF _entity_poly.type value is given for each._



URI: [lambda:NucleicAcidTypeEnum](http://w3id.org/lambda/NucleicAcidTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| dna | None | Deoxyribonucleic acid (mmCIF: polydeoxyribonucleotide) |
| rna | None | Ribonucleic acid (mmCIF: polyribonucleotide) |
| dna_rna_hybrid | None | A single strand containing both deoxyribo- and ribonucleotides (mmCIF: polyde... |
| peptide_nucleic_acid | None | Peptide nucleic acid, a synthetic analogue with a peptide-like backbone (mmCI... |
| other | None | Another nucleic acid analogue, such as a locked nucleic acid, morpholino or t... |




## Slots

| Name | Description |
| ---  | --- |
| [nucleic_acid_type](nucleic_acid_type.md) | Chemical type of the polymer: DNA, RNA, a DNA/RNA hybrid, or an analogue |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: NucleicAcidTypeEnum
description: Chemical type of a nucleic acid polymer. The mmCIF _entity_poly.type
  value is given for each.
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  dna:
    text: dna
    description: 'Deoxyribonucleic acid (mmCIF: polydeoxyribonucleotide)'
  rna:
    text: rna
    description: 'Ribonucleic acid (mmCIF: polyribonucleotide)'
  dna_rna_hybrid:
    text: dna_rna_hybrid
    description: 'A single strand containing both deoxyribo- and ribonucleotides (mmCIF:
      polydeoxyribonucleotide/polyribonucleotide hybrid)'
  peptide_nucleic_acid:
    text: peptide_nucleic_acid
    description: 'Peptide nucleic acid, a synthetic analogue with a peptide-like backbone
      (mmCIF: peptide nucleic acid)'
  other:
    text: other
    description: Another nucleic acid analogue, such as a locked nucleic acid, morpholino
      or threose nucleic acid

```
</details>