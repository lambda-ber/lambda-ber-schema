

# Slot: nucleotide_sequence 


_Sequence in one-letter code, written 5' to 3'. T for DNA, U for RNA; IUPAC ambiguity codes and I for inosine are allowed. A modified nucleotide is written as its parent base and described in the association's modifications or in cross_references._





URI: [lambda:nucleotide_sequence](http://w3id.org/lambda/nucleotide_sequence)
Alias: nucleotide_sequence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | A nucleic acid as a molecular entity: one DNA, RNA or hybrid strand, with its... |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[ACGTURYKMSWBDHVNI]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:nucleotide_sequence |
| native | lambda:nucleotide_sequence |
| exact | mmCIF:_entity_poly.pdbx_seq_one_letter_code_can |




## LinkML Source

<details>
```yaml
name: nucleotide_sequence
description: Sequence in one-letter code, written 5' to 3'. T for DNA, U for RNA;
  IUPAC ambiguity codes and I for inosine are allowed. A modified nucleotide is written
  as its parent base and described in the association's modifications or in cross_references.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_entity_poly.pdbx_seq_one_letter_code_can
rank: 1000
alias: nucleotide_sequence
owner: NucleicAcid
domain_of:
- NucleicAcid
range: string
pattern: ^[ACGTURYKMSWBDHVNI]+$

```
</details>