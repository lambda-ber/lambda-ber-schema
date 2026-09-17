

# Slot: sequence_accession 


_Accession of the reference nucleotide sequence as a CURIE: RefSeq (refseq:NM_000518.5) or INSDC, which covers GenBank, ENA and DDBJ (insdc:J00153.1). For transcripts, genes and genomic fragments; a synthetic oligonucleotide has none._





URI: [lambda:sequence_accession](http://w3id.org/lambda/sequence_accession)
Alias: sequence_accession

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | A nucleic acid as a molecular entity: one DNA, RNA or hybrid strand, with its... |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^(refseq|insdc):[A-Z][A-Z0-9_]*[0-9](\.[0-9]+)?$`




## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:sequence_accession |
| native | lambda:sequence_accession |
| exact | mmCIF:_struct_ref.pdbx_db_accession |




## LinkML Source

<details>
```yaml
name: sequence_accession
description: 'Accession of the reference nucleotide sequence as a CURIE: RefSeq (refseq:NM_000518.5)
  or INSDC, which covers GenBank, ENA and DDBJ (insdc:J00153.1). For transcripts,
  genes and genomic fragments; a synthetic oligonucleotide has none.'
from_schema: http://w3id.org/lambda/
exact_mappings:
- mmCIF:_struct_ref.pdbx_db_accession
rank: 1000
alias: sequence_accession
owner: NucleicAcid
domain_of:
- NucleicAcid
range: uriorcurie
pattern: ^(refseq|insdc):[A-Z][A-Z0-9_]*[0-9](\.[0-9]+)?$

```
</details>