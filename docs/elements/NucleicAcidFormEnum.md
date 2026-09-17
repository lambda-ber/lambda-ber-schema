# Enum: NucleicAcidFormEnum 




_Form a nucleic acid strand takes in a sample_



URI: [lambda:NucleicAcidFormEnum](http://w3id.org/lambda/NucleicAcidFormEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| single_stranded | None | Unpaired, or with no defined secondary structure |
| double_stranded | None | Paired with a complementary strand in a duplex, including a self-complementar... |
| hairpin | None | Folded back on itself to form a stem-loop |
| triplex | None | Three strands, a third strand bound in the major groove of a duplex |
| quadruplex | None | Four-stranded, such as a G-quadruplex or i-motif |
| junction | None | A three- or four-way junction, such as a Holliday junction |
| circular | None | Covalently closed circle, such as a plasmid or a circular RNA |
| other | None | A form not listed, described in the association's description |




## Slots

| Name | Description |
| ---  | --- |
| [structural_form](structural_form.md) | Form the strand takes in this sample: single-stranded, paired in a duplex, fo... |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: NucleicAcidFormEnum
description: Form a nucleic acid strand takes in a sample
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  single_stranded:
    text: single_stranded
    description: Unpaired, or with no defined secondary structure
  double_stranded:
    text: double_stranded
    description: Paired with a complementary strand in a duplex, including a self-complementary
      strand paired with a second copy of itself
  hairpin:
    text: hairpin
    description: Folded back on itself to form a stem-loop
  triplex:
    text: triplex
    description: Three strands, a third strand bound in the major groove of a duplex
  quadruplex:
    text: quadruplex
    description: Four-stranded, such as a G-quadruplex or i-motif
  junction:
    text: junction
    description: A three- or four-way junction, such as a Holliday junction
  circular:
    text: circular
    description: Covalently closed circle, such as a plasmid or a circular RNA
  other:
    text: other
    description: A form not listed, described in the association's description

```
</details>