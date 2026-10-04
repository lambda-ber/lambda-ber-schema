# Case study: PDB 7ZYI, human NTCP, from archive to paper

**Entry**: [PDB 7ZYI](https://www.rcsb.org/structure/7ZYI) ·
[EMD-15024](https://www.ebi.ac.uk/emdb/EMD-15024)
**Publication**: Liu H, Irobalieva RN, Bang-Sørensen R, Nosol K, Mukherjee S, Agrawal P, Stieger B,
Kossiakoff AA, Locher KP. *Structure of human NTCP reveals the basis of recognition and sodium-driven
transport of bile salts into the liver.* Cell Research 32:773–776 (2022).
[doi:10.1038/s41422-022-00680-4](https://doi.org/10.1038/s41422-022-00680-4)
**Examples**: `tests/data/valid/Dataset-pdb-7ZYI-NTCP-fab-nanobody.yaml` (loader output),
`tests/data/valid/Dataset-pdb-7ZYI-NTCP-curated-from-paper.yaml` (loader output plus the paper)

This page follows one structure from the archive to the paper behind it, and asks two questions:

1. **What does the PDB know, and does lambda-ber-schema keep all of it?** This part is settled: the
   PDB loader now gives every field the RCSB Data API can return a recorded disposition, and a test
   holds it to that.
2. **What does the paper know that the PDB does not, and what would the schema need to keep it?**
   This part is open. The paper's surplus is described here in three tiers, the curated example
   shows how far the current schema stretches, and the last section makes concrete proposals for
   extending it. None of the proposals is applied in this change: the schema changes made here stop
   at what the PDB itself can express.

## The structure in brief

NTCP (SLC10A1) moves bile salts from portal blood into liver cells, driven by sodium, and is the
entry receptor for hepatitis B and D viruses. 7ZYI is a 2.9 Å single-particle cryo-EM structure of
wild-type human NTCP in a lipid nanodisc, bound to:

- **NTCP_Fab12**, a synthetic Fab against NTCP's external face, and a **Fab-binding nanobody**. NTCP
  is about 38 kDa and mostly buried in the nanodisc, too small and featureless for particles to
  align on their own; the Fab and nanobody add mass and a rigid, asymmetric feature. They are
  experimental aids, not biology, and the paper checks that the Fab does not inhibit transport.
- **Glycochenodeoxycholic acid (GCDC)**, a bile salt substrate, added at 100 µM. Two GCDC molecules
  sit in a tunnel through the transporter, at sites the authors call S_out and S_in.
- **Two sodium ions**, at sites Na1 and Na2 between TM3 and TM8.

From these the authors propose a mechanism: two Na⁺ and one bile salt per cycle, with a bile salt
shuttling from S_out to S_in. Its endpoint is the molecular function the Gene Ontology already names:

```
id: GO:0008508
name: bile acid:sodium symporter activity
intersection_of: GO:0015293 ! symporter activity
intersection_of: has_primary_input CHEBI:29101 ! sodium(1+)
intersection_of: has_primary_input CHEBI:3098 ! bile acid
```

GO says *what* NTCP does. The paper's contribution is *how*: which residues hold which partner, in
what order, through which states.

---

## Part 1. Closing the gap between the PDB and lambda-ber-schema

### How coverage is measured

"Everything the PDB has" is made concrete in three files:

| File | What it holds |
|---|---|
| `src/lambda_ber_schema/loaders/pdb_rcsb_fields.json` | Every leaf field the RCSB Data API's JSON schemas allow on the ten record kinds the loader fetches (entry; polymer, non-polymer and branched entities and their instances; chemical components; assemblies; interfaces), 1,943 in all, with RCSB's units |
| `src/lambda_ber_schema/loaders/pdb_field_map.yaml` | A disposition for every one of them |
| `tests/loaders/test_pdb_coverage.py` | Fails if any field is unclassified, if a rule names a slot the schema lacks, or if a value marked as carried is missing from the output for 16 captured entries |

The dispositions, and how the 1,943 fields divide among them:

| Disposition | Meaning | Fields |
|---|---|---|
| `to` | carried in a named schema slot | 426 |
| `metric` | carried in `additional_metrics` / `additional_properties`, keyed by its mmCIF item | 463 |
| `reference` | general knowledge about the molecule RCSB imports from elsewhere (GO labels, ChEMBL bioactivities of other compounds, sequence clusters, computed per-residue features); reachable through the cross-references kept | 292 |
| `derived` | recomputable from fields that are carried | 283 |
| `join` | an identifier used only to connect records | 210 |
| `linked_file` | atom- or operator-level detail in a file the dataset links (the mmCIF coordinates, the validation report) | 151 |
| `bookkeeping` | archive housekeeping: revision audit trails, processing sites | 102 |
| `out_of_scope` | fields of computed-model entries, which the loader does not load | 16 |

"Zero gap" therefore means zero *unaccounted* fields, not zero dropped fields. The non-carried
dispositions are judgements, written down where they can be reviewed: anyone who disagrees that,
say, a polymer's hydropathy profile is reference data rather than a fact about this deposition can
change one line and the test will demand the loader carry it.

The 16 captured entries were chosen to exercise every kind of PDB entry: single-particle, helical
and subtomogram cryo-EM, MicroED, X-ray, serial femtosecond crystallography, joint X-ray and neutron,
solution NMR, solution scattering, negative stain, a virus, a glycoprotein, a protein–DNA complex, a
natural-source protein, and a 1983 entry. For 7ZYI alone, 714 distinct fields are present: 150
carried in named slots, 66 as metrics, the rest classified.

`uv run lambda-ber-schema etl pdb-coverage --entry <id>` runs the same classification on any live
entry.

### What was wrong before

Measuring coverage this way turned up defects that had been invisible:

- **R-factors and space groups never arrived** from real X-ray entries. The loader read
  `refine.ls_rfactor_rwork` and `symmetry.space_group_name_hm`; RCSB spells them
  `ls_R_factor_R_work` and `space_group_name_H_M`. The test fixture for 1HHO had been edited to the
  wrong spellings, so the tests passed.
- **Every instrument subclass field was silently dropped on output**, for every loader. Pydantic
  serializes a list typed `Instrument` as `Instrument`, so a cryo-EM microscope's voltage and a
  beamline's detector never reached the YAML.
- **The deposition date stood in for the experiment date**, and cryo-EM entries listed a
  structure-factor file that does not exist.
- **Each polymer chain was its own sample**, so the four chains of 7ZYI were four unrelated samples
  and there was nowhere to put the ligands, which belong to the specimen as a whole.
- **Ligands, glycans, assemblies, interfaces and per-copy records were never fetched.**

### What 7ZYI looks like now

One specimen sample with a component per entity:

| Component | Type | Identity | Copies |
|---|---|---|---|
| Sodium/bile acid cotransporter | protein | `uniprot:Q14973` | 1 |
| heavy chain of Fab | protein | `pdb:7ZYI/protein/2` (no UniProt entry; sequence carried) | 1 |
| light chain of Fab | protein | `pdb:7ZYI/protein/3` | 1 |
| Nanobody | protein | `pdb:7ZYI/protein/4` | 1 |
| cholesterol | small molecule | `pdb.ligand:CLR` (two candidate ChEBI ids, so neither is used as identity) | 2 |
| GCDC | small molecule | `CHEBI:36274`, role `ligand` (the author flagged it as subject of investigation) | 2 |
| sodium ion | small molecule | `pdb.ligand:NA` | 2 |

Interactions come from two RCSB sources. **Interfaces** between polymers in the first assembly say
which chain binds which, with the residues each side buries:

```yaml
- subject_id: pdb:7ZYI/component/2        # heavy chain of Fab
  object_id: pdb:7ZYI/component/1         # NTCP
  interaction_type: binds
  interaction_status: observed
  subject_site: S36,H38,S55,Y58,G59,Y60,T61,S62,Y63,K68,...
  object_site: G19,K20,R21,N87,I88,G144,Y146,D147,G148,K153,...
  description: 'Contact in the first assembly: interface 2: 823 square angstroms buried, 47 interface residues (2 core)'
```

The four contacts recovered are: Fab heavy chain → NTCP, Fab light chain → NTCP, nanobody → Fab light
chain, and the two Fab chains to each other. The nanobody touches only the Fab, which is what the
paper means by a "Fab-binding nanobody".

**Instance records**, one per ligand copy, give each copy's contact residues, its declared bonds and
its fit to the map. Each copy becomes its own row, so the two GCDC molecules get two different sites,
and the two sodium ions two different coordination shells:

```yaml
- subject_id: pdb:7ZYI/component/7        # sodium
  object_id: pdb:7ZYI/component/1         # NTCP
  interaction_type: is_coordinated_by     # from a declared metal-coordination bond
  stoichiometry: '1:1'
  object_site: S105,S119,T123,E257
  description: Copy NA A 706 (label chain J) in the deposited model; site residues are those within
    contact distance; bonded to E257, S105, T123
```

Per-copy validation stays on the component, keyed by copy:

```yaml
additional_metrics:
- attribute: {id: rcsb:rcsb_nonpolymer_instance_validation_score.Q_score,
              label: 'rcsb_nonpolymer_instance_validation_score[F].Q_score'}
  numeric_value: 0.41
```

Around the sample: a `CryoEMInstrument` (TFS Krios, 300 kV, K3 with energy filter), the
vitrification preparation (Vitrobot Mark IV, ethane-propane, 100% humidity), expression preparations
(NTCP in HEK293, Fab and nanobody in *E. coli*), workflow runs for CTF correction (Gctf), 3D
reconstruction (RELION 4, 161,093 particles, 2.88 Å at FSC 0.143), model building (Coot), model
refinement (PHENIX, with restraint deviations) and validation, the publication, nine authors with
ORCIDs where given, the SNSF as funder, and files for the coordinates, the EMDB map and the
validation report.

### Schema changes made, all driven by what the PDB expresses

| Change | PDB source it serves |
|---|---|
| `Publication`, `StudyPublicationAssociation` | `citation` |
| `Study.database_cross_references` | `database_2`, `pdbx_database_related`, EMDB ids, `rcsb_external_references` |
| `Dataset.deposition_date`, `release_date`, `last_revision_date`, `revision` | `rcsb_accession_info` |
| `cryoem_preparation`, `xray_preparation`, `saxs_preparation` on `SamplePreparation` (the classes existed but nothing pointed to them) | `em_vitrification`, `em_staining`, `exptl_crystal_grow`, `pdbx_soln_scatter` |
| `NMRInstrument`; `solution_nmr`, `solid_state_nmr` and the other PDB methods in `TechniqueEnum`; EM reconstruction methods in `ExperimentalMethodEnum` | `exptl.method`, `em_experiment`, `pdbx_nmr_spectrometer` |
| `ResolutionShell` and `WorkflowRun.resolution_shells` | `reflns_shell`, `em_diffraction_shell` |
| `ProteinConstruct.amino_acid_sequence`, `mutations` | `entity_poly`, `entity.pdbx_mutation` |
| EM microscope and grid slots (electron source, illumination, specimen holder, cryogen, stain, embedding) | `em_imaging`, `em_vitrification`, `em_staining`, `em_embedding` |
| `XRayPreparation.crystallization_ph`, `matthews_coefficient`, `solvent_content_percent`; refinement particle counts and helical parameters | `exptl_crystal_grow`, `exptl_crystal`, `em_3d_reconstruction`, `em_helical_entity` |
| `additional_metrics`, `additional_properties` on runs, workflows, preparations, instruments, samples, components and molecules | the long tail of statistics with no named slot, each keyed by its mmCIF item |
| `Instrument.instrument_type`, a type designator | lets one instrument table hold subclass rows that validate and round-trip |
| Database, file format and enum additions (EMDB, BMRB, GlyTouCan, PDF, NMR-STAR, ...) | cross-references and files the PDB names |

### Known limits of the ingest

- Interfaces are fetched for the first assembly only, up to 60; instance records up to 150 per kind.
  Virus capsids and long filaments are truncated, with a warning.
- When RCSB relates a chemical component to several ChEBI entries (cholesterol has two), none is used
  as the molecule's identity; all are kept as cross-references.
- Units RCSB does not state are written `unspecified` rather than guessed.
- Sites are written in the entity's sequence numbering (the label numbering). For 7ZYI this matches
  the authors' numbering; for entries with offsets it will not.
- The deposition does not say which GCDC copy is at S_out and which at S_in. That naming exists only
  in the paper (see below).

---

## Part 2. The gap between the paper and the PDB

The paper says much the PDB does not. Sorting it, three tiers emerge, though as the examples show the
boundaries are not clean.

### Tier 1: experimental facts

What was done and measured, independent of interpretation.

| Fact in the paper | In the PDB? | Where it goes in the schema today | Gap |
|---|---|---|---|
| NTCP expressed in HEK293 | yes (`entity_src_gen`) | expression `SamplePreparation` | none |
| Purified in detergent, reconstituted into lipid nanodiscs | no | `SampleComponent` of type `membrane_mimetic`, role `carrier`; purification `SamplePreparation` | composition is only in the supplement |
| Cholesteryl hemisuccinate present during purification | no | `SampleComponent` → `SmallMolecule` `CHEBI:138742`, role `additive` | none |
| 100 µM GCDC on the grids | no | `SampleComponent.concentration` | none |
| Fab and nanobody are there for particle alignment | no | role `chaperone` | *why* a chaperone was used has no slot |
| NTCP_Fab12 binds NTCP with apparent K_d 60 nM | no | `SampleComponentInteraction.affinity`, `affinity_type: kd` | where the number came from is free text |
| GCDC's K_M ≈ 0.6 µM (from earlier work) | no | interaction `is_substrate_of`, status `expected`, `affinity_type: km` | the citation is free text |
| Taurocholate uptake assays (Fig. 1b, six conditions, three replicates) | no | reduced to three interaction rows: GCDC `inhibits` (observed), CHS `inhibits` (not_observed), Fab `inhibits` (not_observed) | **no home for an assay**: readout, system, values, controls, error |
| Data collected at ScopeM, ETH Zürich | no | `Organization`, role `operating_institution` | none |
| NIH grant GM117372, SNSF award 310030_189111 | partly: the PDB names the SNSF, without award number, and not the NIH | `StudyOrganizationAssociation.award_number` | none |
| Full author names and affiliations | partly (initials, some ORCIDs) | `Person`, `PersonOrganizationAssociation` | none |

Tier 1 is mostly expressible today. The curated example carries all of it, and the one real gap is the
assay.

### Tier 2: interpretations of the map

Choices the authors made between alternatives, on evidence.

| Interpretation | Alternatives considered | Evidence given | What the PDB records | What the schema can say |
|---|---|---|---|---|
| The two elongated densities are GCDC | cholesterol, CHS (both present) | GCDC at about 170× K_M; GCDC inhibits uptake, CHS does not; no report of cholesterol transport | GCDC modelled, flagged subject of investigation; per-copy Q-score 0.41 and 0.47 | status `observed`, and the reasoning only as description text |
| The densities near TM3/TM8 are Na⁺ at sites Na1 and Na2 | — | coordination geometry; homology to the bacterial ASBT sites | Na modelled; 5 coordination bonds declared; contacts listed | site residues, but not the site's *name* |
| A density between Na1 and Na2 is water, possibly a transient Na⁺ site | Na⁺ | no proper coordination | not modelled as anything | nothing |
| The Fab captures a functional state | a Fab-trapped artefactual state | Fab at 12× K_d does not inhibit uptake | nothing | Fab `inhibits` `not_observed`, with no link to the claim it supports |
| S_out is near the outer membrane boundary, S_in nearer the cytoplasm | — | position in the tunnel | two GCDC copies, unnamed | neither copy can be named |

Two findings from setting the paper beside the deposition:

**The "same" sodium site has three residue lists.** For Na2, the deposition declares one coordination
bond (Q68). RCSB's contact calculation adds G97, S99 and Q261. The paper's Fig. 1i adds C98. For Na1:
declared bonds S105, T123, E257; contacts add S119; the paper adds N106. Each list is correct for
what it measures (a modelled bond, a distance cut-off, an author's reading that includes main-chain
carbonyls), and a consumer needs to know which one they hold. The schema stores one `object_site`
string per row, with no slot saying which kind of list it is.

**The deposition models two cholesterols the paper never mentions.** The paper discusses cholesterol
only as an alternative it rejected for the GCDC densities. The deposited model nonetheless contains two
cholesterol molecules. One packs against residues that also line a GCDC copy (S206, L287 and I291 are
in both contact lists); the other sits on a different face (F231, L235, Y238, R251, ...). Neither the
deposition nor the paper says what these densities are taken to be or why they were modelled. A
curated record has to hold the deposition's statement and the paper's silence side by side, without
either overriding the other.

### Tier 3: mechanism

What the authors propose happens:

1. Two Na⁺ bind at Na1 and Na2 from the outside; a bile salt binds at S_out.
2. The bile salt shifts from S_out to S_in.
3. The bile salt at S_in is released into the cytoplasm with the two Na⁺; S_out is reloaded.

Alongside the cycle come a stoichiometry (2 Na⁺ : 1 bile salt), a contrast with canonical alternating
access (NTCP has an open tunnel instead), an explanation of why cholesterol is not transported, and an
inference that the human homologues ASBT and SOAT work the same way.

The schema has fragments of this. `Protein.go_terms` can hold GO:0008508.
`functional_annotation.yaml` has `FunctionalSite` (residues, ligand interactions, GO terms, publication
ids) and `ConformationalEnsemble` / `ConformationalState`. Nothing ties sites and states into an
ordered cycle, or links a GO function to the components that fulfil its `has_primary_input` roles in
this sample.

### Where the tiers blur

- **The Fab non-inhibition assay is a Tier 1 fact that licenses a Tier 2 claim.** On its own it is a
  number. Its purpose is to justify reading the structure as a functional state. A representation that
  keeps the number but not what it supports keeps the wrong half.
- **"Chaperone" is a fact about intent.** That the Fab and nanobody are in the sample is in the PDB;
  that they are there only to make the particle tractable is the authors' design, stated nowhere in the
  archive. It changes how a reader should treat the interfaces they make.
- **The GCDC assignment rests on Tier 1 facts.** The concentration and the inhibition data are the
  evidence. Kept apart, the facts look incidental and the assignment looks unsupported.

So the useful distinction is less "objective versus tacit" than "what kind of claim, resting on what
evidence, from which source".

### What the curated example shows

`Dataset-pdb-7ZYI-NTCP-curated-from-paper.yaml` adds Tier 1 and as much of Tier 2 as fits, without
changing the schema. It is built by `scripts/curate_7zyi_from_paper.py` from the loader's output.
Every value taken from the paper ends its description with
`[Liu et al. 2022, Cell Res 32:773 (doi:10.1038/s41422-022-00680-4), Fig. 1b]`. That bracketed
citation is the clearest sign of what is missing: provenance, evidence and the paper's site names
travel as prose inside a description, where no query can reach them.

Other strains visible in the file:

- Fab → NTCP appears **twice**: once from the deposited interface (sites, buried area) and once from
  the paper's binding assay (K_d 60 nM). They are the same relationship from two sources. The rows
  cannot be told apart except by reading their descriptions.
- GCDC → NTCP appears **four** times: two structural rows (one per copy), one `is_substrate_of` row
  carrying a K_M from a cited paper, and one `inhibits` row from the uptake assay.
- The paper's sodium site names and residue lists sit in the description beside RCSB's contact list.

---

## Proposals for extending the schema

Each proposal is anchored in something the case study could not express, says how it relates to what
the PDB can represent, and gives a LinkML sketch. None is applied here.

### P1. Provenance on assertions

**Problem.** A row from the deposition and a row from the paper are indistinguishable. Provenance lives
in description text.

**Proposal.** A mixin for any assertion-like row (`SampleComponentInteraction`, `SampleComponent`,
`FunctionalSite`) recording where it was asserted, by what kind of source, and where in that source.

```yaml
classes:
  AssertionProvenance:
    mixin: true
    attributes:
      asserted_by:
        description: What kind of source made the assertion
        range: AssertionSourceEnum
      asserted_in:
        description: The publication the assertion comes from, when it comes from one
        range: Publication
      source_locator:
        description: Where in the source ('Fig. 1b', 'Supplementary Fig. S2', 'struct_conn metalc3')
        range: string
enums:
  AssertionSourceEnum:
    permissible_values:
      deposition: {description: The archive entry the dataset was loaded from}
      publication: {description: A publication describing the study}
      curation: {description: A curator, from reading one or more sources}
      external_database: {description: Another database (BindingDB, ChEMBL, ...)}
```

**Relation to the PDB.** Within the PDB, provenance is implicit: everything is the deposition, and
RCSB's own derived fields carry `provenance_source` (which the loader currently treats as
bookkeeping). Adopting P1 would let the loader set `asserted_by: deposition` on every row and
`external_database` on BindingDB affinities, at no cost.

### P2. Site names and the basis of a site's residue list

**Problem.** Na1, Na2, S_out and S_in cannot be named. The three residue lists for one sodium site
(declared bonds, contacts, the author's reading) cannot be told apart.

**Proposal.** Name the site, and say what its residue list means.

```yaml
SampleComponentInteraction:
  attributes:
    object_site_name:
      description: The source's name for the site on the object ('Na1', 'S_out')
    object_site_basis:
      description: What the residue list in object_site records
      range: SiteBasisEnum
enums:
  SiteBasisEnum:
    permissible_values:
      declared_bond: {description: Residues joined to the subject by a bond the model declares}
      contact_distance: {description: Residues within a distance cut-off in the model}
      buried_surface: {description: Residues whose accessible area the subject buries}
      author_assignment: {description: Residues the authors name as forming the site}
```

A heavier alternative is to point at a `FunctionalSite` (which already has `site_name` and `residues`)
from the interaction, giving one site record that several interactions and sources can share.

**Relation to the PDB.** `declared_bond`, `contact_distance` and `buried_surface` all come straight
from RCSB (struct_conn, target neighbours, interfaces). The loader would set them today.
`author_assignment` is paper-only.

### P3. Interpretive status and alternatives considered

**Problem.** "The density is GCDC, not CHS, because…" is a choice among alternatives. The schema can
say a binding is `observed`; it cannot say the identity of what is bound was *assigned*, against what
alternatives, or why they were rejected. The water that might be a transient sodium site cannot be
recorded at all.

**Proposal.** A status for assigned identities, and a structured list of alternatives.

```yaml
enums:
  InteractionStatusEnum:
    permissible_values:
      assigned:
        description: >-
          Seen in the data, with the identity of a participant assigned by the authors among
          alternatives the data alone could not exclude
classes:
  AlternativeAssignment:
    attributes:
      candidate:
        description: The alternative considered for the subject
        range: SmallMolecule
      reason_rejected:
        description: Why the authors preferred the assignment made
      supporting_evidence:
        description: Assay results or other rows the decision rests on (see P4)
SampleComponentInteraction:
  attributes:
    alternatives_considered:
      range: AlternativeAssignment
      multivalued: true
      inlined_as_list: true
```

**Relation to the PDB.** The PDB has no notion of an alternative assignment. Its closest signals are
fit statistics (per-copy Q-score, RSCC), which the loader now keeps, and the author's
subject-of-investigation flag. P3 goes beyond PDB expressivity and is paper-only.

### P4. Assay results

**Problem.** Fig. 1b, the taurocholate uptake assay under six conditions, is the evidence for three
separate claims (GCDC is a substrate and binds; CHS does not inhibit; the Fab leaves NTCP functional).
The curated example can only flatten it into three interaction rows.

**Proposal.** A class for one measured condition of a functional assay, tied to the components it
perturbs and the claims it supports.

```yaml
classes:
  AssayResult:
    is_a: NamedThing
    mixins: [AssertionProvenance]
    attributes:
      assay_type:
        description: The kind of assay, as an ontology term (BAO or OBI)
        range: OntologyTerm
      assay_system:
        description: Where the assay was done ('HEK293 cells expressing NTCP-YFP')
      readout:
        description: What was measured ('Na+-driven uptake of [3H]-taurocholate')
      perturbant_id:
        description: The component varied in this condition
        range: SampleComponent
      perturbant_concentration:
        range: QuantityValue
      value:
        description: The result, relative to the control where normalized
        range: QuantityValue
      error:
        range: QuantityValue
      replicates:
        range: integer
      control_id:
        description: The result this one is normalized against
        range: AssayResult
```

Interactions then cite results through an `evidence_assay_ids` slot rather than restating them.

**Relation to the PDB.** The PDB holds no assays. The nearest it comes is `rcsb_binding_affinity`,
imported from BindingDB and others, which the loader already turns into interaction affinities. P4 is
paper-only and the largest proposal here. It should probably align with an existing assay model
before being written.

### P5. Why a component is there

**Problem.** `role: chaperone` says the Fab and nanobody support NTCP, but not *how*: as size and
fiducial markers for cryo-EM, as crystallization chaperones, or as conformational locks. The
distinction matters, because a conformational lock changes how the structure should be read and a
fiducial marker, if shown not to inhibit, does not.

**Proposal.** A small enum on `SampleComponent`.

```yaml
SampleComponent:
  attributes:
    purpose:
      range: ComponentPurposeEnum
enums:
  ComponentPurposeEnum:
    permissible_values:
      fiducial_marker: {description: Adds mass or features so particles can be aligned}
      crystallization_chaperone: {description: Provides lattice contacts}
      conformational_stabilizer: {description: Holds the target in one conformation}
      solubilization: {description: Keeps a membrane protein in solution}
      biological_partner: {description: Present because it is part of the biology studied}
```

**Relation to the PDB.** Not expressed. The PDB records that the Fab is present, not why.

### P6. Function, participants and mechanism

**Problem.** GO:0008508 can sit on `Protein.go_terms`, but nothing says that in *this* sample GCDC
fills the bile-acid input and the two sodium ions fill the sodium input, in a 2:1 ratio, at named
sites. Nothing represents the transport cycle.

**Proposal, in two steps.**

*Step 1, within reach:* a function assertion linking a GO molecular function to the sample components
that fill its participant roles, with stoichiometry and evidence.

```yaml
classes:
  FunctionAssertion:
    mixins: [AssertionProvenance]
    attributes:
      sample_id: {range: Sample, required: true}
      enabled_by: {range: SampleComponent, required: true}
      function: {description: GO molecular function, range: uriorcurie, required: true}
      participants:
        range: FunctionParticipant
        multivalued: true
        inlined_as_list: true
      stoichiometry: {description: "'2 Na+ : 1 bile salt'"}
  FunctionParticipant:
    attributes:
      component_id: {range: SampleComponent}
      relation: {description: The GO relation the component fills (has_primary_input), range: uriorcurie}
      site_name: {description: Site where it engages ('Na1', 'S_out')}
```

*Step 2, defer:* the ordered mechanism (states, transitions, which partner binds or leaves at each
step) is a causal model. GO-CAM already represents those. Rather than build a parallel model,
lambda-ber-schema could carry structural evidence (sites, states, the structures that capture them)
and link to a GO-CAM model by identifier for the causal chain.

**Relation to the PDB.** Not expressed. The PDB holds structures of states; it says nothing of the
order between them.

### P7. Reconciling the deposition and the paper

**Problem.** The two sources disagree in small ways: cholesterol modelled but not discussed; funders
listed differently; author names abbreviated in one and in full in the other; site residue lists that
differ by one residue.

**Proposal.** No new structure beyond P1 and P2. With provenance on every assertion, both versions can
coexist as separate rows, and a curated view can choose. What is needed is a convention: a curator
does not overwrite a deposition-derived value with a paper-derived one, but adds the paper's assertion
alongside it.

### Suggested order

1. **P1 and P2.** Cheap; the PDB loader can populate most of them immediately; they remove the worst
   strain in the curated example.
2. **P5.** One enum; immediately useful for any antibody- or nanobody-assisted structure.
3. **P4.** Large, and should follow a review of existing assay models.
4. **P3, then P6 step 1.** These move the schema from describing experiments toward describing
   claims, and deserve a decision about how far lambda-ber-schema should go in that direction.
5. **P6 step 2** stays outside the schema, as a link to GO-CAM.

## Reproducing this case study

```bash
# loader output, from the live API
uv run lambda-ber-schema etl pdb --entry 7ZYI -o tests/data/valid/Dataset-pdb-7ZYI-NTCP-fab-nanobody.yaml
# how the entry's fields are handled
uv run lambda-ber-schema etl pdb-coverage --entry 7ZYI
# the curated layer
uv run python scripts/curate_7zyi_from_paper.py
# validate both
uv run linkml-validate -s src/lambda_ber_schema/schema/lambda_ber_schema.yaml -C Dataset \
  tests/data/valid/Dataset-pdb-7ZYI-NTCP-curated-from-paper.yaml
```
