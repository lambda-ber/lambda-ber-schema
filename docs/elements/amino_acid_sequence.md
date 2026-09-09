

# Slot: amino_acid_sequence 


_Canonical one-letter amino acid sequence of the protein, without tags or other construct additions. Construct-level sequence belongs on ProteinConstruct._





URI: [lambda:amino_acid_sequence](http://w3id.org/lambda/amino_acid_sequence)
Alias: amino_acid_sequence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a biological entity: its sequence, source organism, gene, and th... |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[ACDEFGHIKLMNPQRSTVWYBJOUXZ]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:amino_acid_sequence |
| native | lambda:amino_acid_sequence |
| exact | mmCIF:_entity_poly.pdbx_seq_one_letter_code_can |




## LinkML Source

<details>
```yaml
name: amino_acid_sequence
description: Canonical one-letter amino acid sequence of the protein, without tags
  or other construct additions. Construct-level sequence belongs on ProteinConstruct.
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_entity_poly.pdbx_seq_one_letter_code_can
rank: 1000
alias: amino_acid_sequence
owner: Protein
domain_of:
- Protein
range: string
pattern: ^[ACDEFGHIKLMNPQRSTVWYBJOUXZ]+$

```
</details>