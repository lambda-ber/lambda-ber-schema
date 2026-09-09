# LAMBDA Core RO-Crate Profile

**Version 0.3.0** · Technique-neutral · Normative specification

Binds `lambda-ber-schema` (LinkML) to RO-Crate 1.2 as a **file manifest** contract. A crate carries
the highest-level details a program needs to decide whether a dataset is worth opening, and then
*points* at the fuller record instead of restating it. It is a search-and-handoff surface, not a
second copy of the schema.

Profile URI: `https://w3id.org/lambda/profile/core/0.3.0`
Machine-readable source: [`lambda_rocrate_core.yaml`](../../../src/lambda_ber_schema/schema/lambda_rocrate_core.yaml)
Generated artifacts: `assets/rocrate/` (JSON Schema, JSON-LD context, OWL, prefix map, SSSOM crosswalk)

Companion technique extensions: the **LAMBDA SAXS profile v0.3.0** (in this repository) and a
prospective MX profile. Core defines the framework those cite; they add technique quantities and
tighten the tiers.

---

## 1. Scope and the unit of record

### 1.1 What a Core crate records

A crate is the machine-readable record of one coherent body of data — who produced it, at which
facility, by which technique, on which specimen, and what files it consists of — written so that a
program which has never seen the facility can decide whether to open it and, if so, where to look
next. Bulk detail lives elsewhere and is *linked*.

### 1.2 The unit is a manifest, not a dataset copy

The atomic thing a Core crate describes is a **manifest**: a root data entity plus the parts it
consists of. A part is either a **file** (addressable, sized, checksummed) or a **dataset part**
(a body of data described somewhere else). Core's job is to make both addressable and to insist that
a dataset part say where its description lives (§7).

This is the boundary rule. If a crate is restating molecular composition, buffer conditions,
per-frame parameters or a technique's quantity register, it is doing `lambda-ber-schema`'s job
badly. Those belong in the linked record.

### 1.3 Three layers, one graph

| Layer | What it is | Where it is defined |
| :---- | :---- | :---- |
| **RO-Crate 1.2** | packaging, `@graph`, identity, `hasPart` | the RO-Crate specification |
| **LAMBDA Core** | manifest contract, pointers, absence, tiers, designation | this document |
| **Technique extension** | technique quantities and their estimators | SAXS / MX profiles |

A Core crate MUST be readable as plain RO-Crate first. Extensions add terms; they never replace
Core's structure, and they never move a Core term.

---

## 2. Principles

- **P1 — the manifest is a search surface.** Everything in a crate earns its place by helping a
  reader decide whether to open the dataset. Detail that only matters *after* that decision belongs
  in the linked record.
- **P2 — one crate, one coherent body of data.** A federated search returns one row per crate.
- **P3 — every artefact is addressable and verifiable.** A part has a locator, a size and a
  checksum, or its absence is declared (§8).
- **P4 — a dataset part must say where its description lives.** Three mechanisms, at least one
  required (§7). A part that names data and then says nothing about it is not a manifest entry.
- **P5 — absence is declared, never implied.** A gap that is stated is metadata; a gap that is
  silent is indistinguishable from an assertion that the field does not exist (§8).
- **P6 — name the estimator.** A derived number without its definition and admissibility tier is
  not evidence (§10).
- **P7 — one designated result, provenance published.** Where several defensible results exist,
  say which is *the* one, under which rule, chosen by whom or what (§9).
- **P8 — mirror the schema, do not copy it.** A crate term that has a `lambda-ber-schema`
  counterpart carries the schema's own slot name, so the projection is identity rather than a
  lookup table nobody maintains (§14).
- **P9 — fail closed.** A builder that cannot reach a source declares the gap. It does not guess a
  default that reads as fact — an invented `open` licence or a fabricated checksum is worse than an
  admitted hole.
- **P10 — small core, composable extensions.** A profile is worth maintaining when it changes
  validation, identity, graph shape or round-trip behaviour. Not when only a file-naming convention
  differs.

---

## 3. Sufficiency tests

A crate is not simply "valid" or "invalid" — it is sufficient for some purposes and not others.
Four tiers, named so that extensions bind their own artefacts to shared meanings and a search can
gate filters rather than silently returning crates that cannot answer them.

- **S1 — findable.** The generic search fields resolve: identity, facility, technique, instrument,
  specimen, dates, access terms. Fields originating outside the pipeline (proposal identifiers,
  embargo status, PI) are declared absent when unreachable, per P9.
- **S2-core — retrievable core.** Every present artefact has a locator, a size and a **valid
  checksum**, and every dataset part resolves a metadata pointer (§7). **Required for conformance.**
- **S2-acquisition — reprocessable.** The raw acquisition is present and verifiable. Optional, but
  its absence MUST be *declared*, never silent. Most public deposits are S2-core without
  S2-acquisition, and that is a conformant, honest state — not a failure.
- **S3 — interpretable.** Every derived quantity names its estimator, defining convention and unit
  (§10). Largely delivered by technique extensions, since core carries few numbers.

The root SHOULD publish which tiers it meets in `lambdarc:sufficiency`. A search MUST require
`s2AcquisitionComplete` for any filter whose answer depends on reprocessing.

---

## 4. Conformance and namespaces

### 4.1 Declaring conformance

The root data entity MUST declare `conformsTo` naming **both** the RO-Crate version and this
profile:

```json
"conformsTo": [
  {"@id": "https://w3id.org/ro/crate/1.2"},
  {"@id": "https://w3id.org/lambda/profile/core/0.3.0"}
]
```

A technique extension appends its own URI; it never replaces the Core URI. The metadata descriptor
separately declares the RO-Crate version, as base RO-Crate requires.

### 4.2 Three term layers

| Prefix | Namespace | Carries |
| :---- | :---- | :---- |
| (RO-Crate base) | `http://schema.org/` | identity, access, packaging — `name`, `datePublished`, `license`, `author`, `hasPart`, `encodingFormat`, `contentSize` |
| `lambda:` | `http://w3id.org/lambda/` | terms that project onto a `lambda-ber-schema` slot |
| `lambdarc:` | `http://w3id.org/lambda/rocrate/` | profile-local machinery with no schema counterpart yet |
| `prov:` | `http://www.w3.org/ns/prov#` | provenance — activities, agents, plans, derivations (§9, §10) |

A crate's `@context` MUST include the RO-Crate 1.2 context URI and MUST bind `lambda` and
`lambdarc` as above:

```json
"@context": [
  "https://w3id.org/ro/crate/1.2/context",
  {"lambda": "http://w3id.org/lambda/",
   "lambdarc": "http://w3id.org/lambda/rocrate/"}
]
```

### 4.3 Why `lambda:` is the http form of the schema base

`lambda:` MUST expand to `http://w3id.org/lambda/` — the base of `lambda-ber-schema` itself — so
that `lambda:Dataset` in a crate **is** the LinkML class IRI and `lambda:file_format` **is** the
slot IRI. Verified: expanding a conformant crate yields `http://w3id.org/lambda/Dataset`, which is
what `SchemaView.get_uri` returns for the `Dataset` class.

Two adjacent traps:

- Crates published against the SSRL 0.2 vocabulary bound `lambda:` to
  `https://w3id.org/lambda/terms/0.2/`. Terms under that base resolve to no schema element at all;
  they look linked and are not. See §15.
- `lambda_ber_types.yaml` binds `schema:` to the **https** form of schema.org, while RO-Crate's own
  context maps its terms to the **http** form (confirmed against
  `https://w3id.org/ro/crate/1.2/context`: `name` → `http://schema.org/name`). These are different
  IRIs. The profile module therefore uses `sdo:` internally for the http form rather than colliding
  with the imported prefix. Crate authors never write either prefix — RO-Crate's context resolves
  the bare terms — so this is invisible in the crates themselves, but it is a real inconsistency
  in the schema and is filed as a change request (§16).

### 4.4 JSON-LD spelling freedom

A reader MUST apply two normalizations before validating. Both are things a JSON-LD processor does,
and neither changes meaning:

1. **Set expansion.** A single value stands for a one-element set wherever the profile declares a
   set: `"instrument": {"@id": "#x"}` and `"instrument": [{"@id": "#x"}]` are the same. This
   includes `@type`, and it applies **at any depth** — a `prov:qualifiedAssociation` nested inside a
   designation is as entitled to the shorthand as a top-level property.
2. **Term compaction.** An explicitly prefixed key compacts to the profile's own term:
   `"lambda:protein_name"` and a context-mapped `"protein_name"` are the same IRI. Real crates mix
   the two spellings *within a single entity*, so this is not a theoretical concern.

Validation in this profile is defined against the normalized form.

---

## 5. Identity and granularity

### 5.1 One crate is one coherent body of data

All data from one collection session on one specimen, or one processing result and its provenance,
lives in one crate. Where a study spans techniques, each technique gets its own crate and a
manifest crate links them (§7, and the `nested-pointers` fixture).

### 5.2 Identifiers

The root `@id` is `./` for a crate stored beside its payload, or an absolute URI for a detached
crate. Stable external identity goes in `identifier` as `PropertyValue` entries with a
`propertyID`, so a UUID, a DOI and a facility-local accession coexist without a reader having to
guess which is which. Contextual entities SHOULD use ORCID for people and ROR for organizations.

### 5.3 Bulk series are one part, not N entities

A frame series, an image sweep or any bulk collection is **one** dataset part carrying
`lambdarc:partCount` and a size. Enumerating 1800 frame files buries the manifest in noise and
tells a reader nothing the count does not.

---

## 6. Crate anatomy

### 6.1 Required entities

| Entity | Profile class | Carries |
| :---- | :---- | :---- |
| Metadata descriptor | `MetadataDescriptor` | RO-Crate conformance; `about` → root |
| Root `Dataset` (`./`) | `CrateRoot` | **the search row.** identity, access, facility, technique, specimen, tiers, `hasPart` |
| Files | `CrateFile` | locator, size, checksum, format, data type |
| Dataset parts | `CrateDatasetPart` | **a metadata pointer (§7)**, count, size |

### 6.2 Optional contextual entities

`PersonEntity`, `OrganizationEntity`, `SampleEntity`, `ProteinEntity`, `InstrumentEntity`,
`ExperimentRunAction`, `WorkflowRunAction`, `SoftwareApplicationEntity`, `DefinedTermEntity`,
`PropertyValueEntity`, `RelatedWork`. Each is optional; each is typed so that a plain RO-Crate
consumer understands it (`Person`, `Organization`, `Protein`, `CreateAction`, …) *and* a
LAMBDA-aware reader can project it.

**Specimen and protein are two entities.** A `SampleEntity` is the thing in the tube or on the
grid; a `ProteinEntity` is the protein it contains, and the same protein entity serves every sample
in the crate that contains it. The sample points at its proteins with schema.org's own
`hasBioChemEntityPart`, which the RO-Crate 1.2 context resolves. A protein entity's `@id` SHOULD be
its UniProt IRI (`http://purl.uniprot.org/uniprot/P69905`), so that the same protein in two crates
is the same node, and it carries the accession as the CURIE the schema uses:

```json
{"@id": "#sample-hba", "@type": ["BioChemEntity", "lambda:Sample"],
 "sample_code": "HBA-OXY-001", "sample_type": "complex", "protein_name": "Hemoglobin A (oxy)",
 "hasBioChemEntityPart": [{"@id": "http://purl.uniprot.org/uniprot/P69905"},
                          {"@id": "http://purl.uniprot.org/uniprot/P68871"}]},
{"@id": "http://purl.uniprot.org/uniprot/P69905", "@type": ["Protein", "lambda:Protein"],
 "name": "Hemoglobin subunit alpha", "uniprot_id": "uniprot:P69905",
 "protein_name": "Hemoglobin subunit alpha", "gene_name": "HBA1", "organism": "NCBITaxon:9606",
 "pdb_entries": ["pdb:1HHO"]}
```

`protein_name` stays on the sample too, as the name the facility recorded and the cheapest search
field. A protein with no UniProt accession is still a protein entity; it MUST then declare
`uniprot_id` in `missing` (§8). Crates that write `uniprot_id` SHOULD bind `uniprot` to
`http://purl.uniprot.org/uniprot/` in their context, so that a reader treating the value as a CURIE
expands it to the entity's own `@id`.

Facility and technique SHOULD be carried as `DefinedTerm` entities rather than bare strings — this
is what lets a federated index join across crates, and the SSRL 0.2 crates already do it.

### 6.3 Value objects nest

`MissingValueDeclaration`, `Designation`, `EstimatorDescriptor`, `SchemaSetEntry` and
`SufficiencyReport` nest inside their owner. They are not graph entities and do not get an `@id`.

### 6.4 Required properties

`CrateRoot` MUST carry `@id`, `@type`, `name`, `description`, `datePublished`, `license`,
`conformsTo`, `hasPart`. `CrateFile` MUST carry `@id`, `@type`, `name`, `encodingFormat`,
`contentSize`, `sha256`.

`license` and `datePublished` are **not** required, but their absence MUST be declared in
`lambdarc:missing`. Earlier drafts required them; that was wrong for the deposits this profile
actually has to describe. A SASBDB entry records a deposition date and no publication date, and
often no licence at all — requiring both would have made the majority of real public deposits
non-conformant while changing nothing about what is knowable. Declared absence already carries the
information a reader needs, and it carries it honestly.

What is *not* acceptable is silence. A root that simply omits `license` is indistinguishable from
one whose builder never looked. Where the date is a deposition rather than a publication, use
`dateCreated` and declare `datePublished` absent.

`sha256` is required on files for the same reason: integrity is what distinguishes a manifest from
a directory listing. When the bytes are unreachable, declare it (§8) rather than omitting it.

---

## 7. Pointing at fuller metadata

This is the substance of the profile. A `CrateDatasetPart` names a body of data that Core
deliberately does not describe in detail. It MUST therefore resolve **at least one** of three
mechanisms, or declare in `lambdarc:missing` why it resolves none. More than one is fine.

### 7.1 Mechanism 1 — nested crate

The part carries `conformsTo` naming a LAMBDA profile, and either a `hasPart` member ending in
`ro-crate-metadata.json` (a subdirectory with its own crate) or an absolute `@id` naming a remote
crate.

```json
{
  "@id": "saxs/",
  "@type": "Dataset",
  "name": "SEC-SAXS-MALS of GluRS (ALS SIBYLS 12.3.1)",
  "conformsTo": [{"@id": "https://w3id.org/lambda/profile/core/0.3.0"},
                 {"@id": "https://w3id.org/lambda/profile/saxs/0.3.0"}],
  "hasPart": [{"@id": "saxs/ro-crate-metadata.json"}]
}
```

Note that a nested crate's descriptor is a plain `File` **of the enclosing crate**, not the
enclosing crate's own descriptor. A reader identifies its own descriptor as the entity whose `@id`
is exactly `ro-crate-metadata.json` (or, for a detached crate, an absolute URI ending in it and
carrying `about`).

### 7.2 Mechanism 2 — schema record

The part references a file holding a full `lambda-ber-schema` document, with the schema version and
a checksum. This is how the rigorous metadata travels without being inlined.

```json
{
  "@id": "mx/",
  "@type": "Dataset",
  "schemaRecord": {"@id": "mx/glurs_mx_lambda_ber.yaml"},
  "schemaVersion": "0.1.2"
}
```

The referenced file is itself a `CrateFile` and MUST carry its own checksum and
`conformsTo` the schema.

### 7.3 Mechanism 3 — remote registration

The part is registered in a public archive under its own accession. Record the identity and the
locator, and claim nothing about bytes the crate does not hold.

```json
{
  "@id": "https://www.sasbdb.org/data/SASDD42/",
  "@type": "Dataset",
  "identifier": [{"@type": "PropertyValue", "propertyID": "SASBDB", "value": "SASDD42"}],
  "url": "https://www.sasbdb.org/data/SASDD42/",
  "missing": [{"field": "sha256", "reason": "not-available", "blocks": "S2-core",
               "note": "Archive publishes no per-entry checksums."}]
}
```

### 7.4 Declaring that a part has no pointer

Legitimate when the part is described by another entity *in the same crate* — a raw frame series
described by its `ExperimentRun`. Say so:

```json
"missing": [{"field": "schemaRecord", "reason": "not-applicable",
             "note": "Described by #exp-secsaxs in this crate; no separate record exists."}]
```

---

## 8. Declared absence

`lambdarc:missing` is the honesty mechanism. Each entry names the field or artefact, why it is
absent, and which tier the absence blocks.

```json
"missing": [
  {"field": "raw_frame_series", "reason": "not-deposited", "blocks": "S2-acquisition",
   "note": "1800 frames remain on facility disk; not published with this package."},
  {"field": "proposal_id", "reason": "not-registered", "blocks": "S1"}
]
```

Reasons, and why the distinctions matter:

| Reason | Meaning |
| :---- | :---- |
| `not-registered` | No upstream system ever held it. Typically proposal-system fields. |
| `not-available` | It exists in an otherwise complete source; this build could not reach the bytes. |
| `not-deposited` | The artefact exists or existed, but the source archive did not include it. The normal case for raw acquisition in public deposits. |
| `embargoed` | Withheld under an access embargo; may become available later. |
| `not-applicable` | Does not apply to this technique or mode. Not a gap — nothing is missing. |

Rules:

1. `blocks` is REQUIRED for every reason except `not-applicable`, which by definition blocks nothing.
2. A field MUST NOT be both present on an entity and declared missing on it.
3. Do not invent a stand-in. An empty `Dataset` for absent frames, a zero-length file, or
   descriptive prose passed off as the artefact are all worse than a declared gap.
4. A declared-absent S2-acquisition artefact does not affect S2-core conformance.

### 8.1 Vocabulary gaps

Declared absence handles a *value* that is missing. `lambdarc:vocabEntry` handles the opposite case:
the value is present and real, and the schema's controlled vocabulary has no term for it.

```json
"vocabEntry": [{
  "module": "lambda-ber-schema",
  "enum": "BeamlineEnum",
  "key": "DORIS3_X33",
  "note": "Decommissioned beamline; no BeamlineEnum term exists."
}]
```

The alternatives are all worse. Coercing to the nearest permissible term produces something that
looks like data and is wrong, and nothing downstream can tell. Dropping the value loses it silently.
Inventing a term forks the vocabulary. Declaring the gap keeps the crate honest *and* turns the gap
into a change request with a real example attached, which is how enums should grow.

`enum` and `key` are REQUIRED. Adopted from Peter Zwart's SAXS drafts (§15.2), where a decommissioned
beamline had no term and the crate said so instead of guessing.

---

## 9. Designation

Where several defensible results exist, `lambdarc:designated` names which is *the* result and how
that was decided.

A designation is expressed in **W3C PROV**, because that is what it is: an activity that used some
inputs, generated a designated output, and was carried out by an agent acting under a plan.

```json
"designated": [{
  "@type": ["lambdarc:Designation", "prov:Activity"],
  "prov:generated": [{"@id": "mtz/XA_x16_autoproc.mtz"}],
  "prov:used":      [{"@id": "#rawunit-90000002"}],
  "selection": "autoproc merged reflection data, run 1",
  "prov:qualifiedAssociation": {
    "@type": "prov:Association",
    "prov:agent": {
      "@id": "urn:lambdarc:policy:ssrl-autoproc-select/0.1",
      "@type": "prov:SoftwareAgent",
      "name": "SSRL autoPROC result selection policy",
      "prov:actedOnBehalfOf": {"@id": "https://ror.org/05gzmn429"}
    },
    "prov:hadPlan": {"@id": "https://w3id.org/lambda/rules/mx-reflections/1.0"}
  }
}]
```

`prov:generated` and `prov:qualifiedAssociation` are REQUIRED. The association is the part that
carries conformance weight: an agent acting under a resolvable, versioned `prov:hadPlan` is
provenance; an unattributed choice is not.

`prov:qualifiedAssociation` is a **set**. PROV does not make it functional, and real activities have
more than one responsible party — a collection session has an operator and a local contact, a
processing run may be attributed to both a person and the policy they ran under. A single-valued
slot would silently drop whichever agent the builder wrote second. As everywhere else, a lone
association MAY be written unwrapped and a reader expands it (§4.4).

Earlier drafts used flat `designatedEntity` / `producedBy` / `rule` / `mode` / `decidedBy` /
`decidedAt` slots and a `manual`-implies-decider rule. PROV says all of it better, and the `mode`
flag disappears entirely: a `prov:Person` and a `prov:SoftwareAgent` are already different things,
so nothing needs to assert which kind of decision it was. `prov:actedOnBehalfOf` additionally
expresses something the flat form could not — that a policy acted for an institution.

Non-designated alternatives remain in the crate as further workflow runs and artefacts; designation
selects, it does not delete.

---

## 10. Estimators and admissibility

Any derived number in a crate travels with an `lambdarc:estimator`:

```json
"estimator": {
  "prov:wasAttributedTo": {
    "@id": "#software-autoproc", "@type": "prov:SoftwareAgent",
    "name": "autoPROC", "version": "0.7.13"
  },
  "sourceField": "CORRECT.LP merging statistics",
  "definition": "STARANISO default resolution cutoff and merging statistics from the processing log",
  "admissibility": "local"
}
```

The producing software is a `prov:SoftwareAgent` referenced by `@id`, so one agent entity serves
every estimate it produced instead of being retyped beside each. Bare `software` / `version` strings
remain accepted for sources that publish nothing more.

Where a single value was read out of a specific artefact, `lambdarc:provenance` records which one
and which field within it:

```json
"lambdarc:provenance": {
  "@type": "prov:Derivation",
  "prov:entity": {"@id": "SASDA55.sascif"},
  "sourceField": "sas_result.Rg_from_Guinier"
}
```

`definition` and `admissibility` are REQUIRED. Two numbers computed under different definitions are
different quantities however alike their labels look.

| Admissibility | Meaning |
| :---- | :---- |
| `local` | Meaningful only inside the producing pipeline. Displayable, **not** filterable. |
| `comparable` | Comparable across datasets sharing the stated definition and companions. |
| `global` | Comparable unconditionally, under a published shared definition. |

A search MUST NOT filter or rank on a `local` value: doing so ranks datasets against each other on
a number that only means something in one pipeline.

---

## 11. Search projection

A LAMBDA federated search projects from the root alone, without opening parts:

| Field | From |
| :---- | :---- |
| identity / pid | `identifier` (`PropertyValue` with `propertyID`) |
| title, summary | `name`, `description` |
| facility | `lambda:facility_name`, `lambda:facility_ror`, or the `facility` `DefinedTerm` |
| instrument | `lambda:instrumentName`, or `instrument_code` / `beamline_id` on the instrument entity |
| technique | `lambda:technique` (`TechniqueEnum`), plus a PaNET IRI from an extension |
| specimen | `lambda:sample_code`, `lambda:protein_name`, `lambda:organism` |
| protein | `lambda:uniprot_id`, `lambda:gene_name` on the `Protein` entities the sample points at with `hasBioChemEntityPart` |
| dates | `datePublished`, `lambda:collectionDate` |
| people | `author` / `agent` → `Person` entities, by ORCID where known; `role` gives the capacity |
| access | `conditionsOfAccess`, `license` |
| size | `contentSize` |
| tiers | `lambdarc:sufficiency` |

Findability is tied to S2-core; reprocessing is tied to S2-acquisition. A search surface MUST expose
`s2AcquisitionComplete` so that "crates I can reprocess" filters are gated rather than silently
returning crates that cannot answer them.

---

## 12. Validation

Three layers, because a flat `@graph` is an open world and no single tool covers it.

**Layer 1 — document shape.** `assets/rocrate/jsonschema/lambda_rocrate_core.schema.json`,
generated with `--top-class ROCrateMetadataDocument`. `@graph` is deliberately permissive at this
level so that a crate carrying technique-extension terms still validates as a document.

**Layer 2 — per entity.** Dispatch each entity on its `@type` (after §4.4 normalization) and
validate against the matching profile class. These classes are **closed**, so an undeclared term
fails. This is where the profile bites, and it is why a technique quantity must nest inside
`lambdarc:resultSummary` rather than being scattered as a bare property: nesting keeps the crate
valid against Core while the extension gives the block its shape.

**Layer 3 — graph rules.** The cross-entity constraints, in
[`tests/test_rocrate_profile.py`](../../../tests/test_rocrate_profile.py):

1. A metadata descriptor exists and its `about` resolves to an entity in the graph.
2. A root data entity exists, typed `lambda:Dataset` (or the deprecated `lambda:Experiment`).
3. Every `hasPart` target resolves to an entity in the graph — a manifest MUST NOT promise a part
   it does not describe. The same holds for every `hasBioChemEntityPart` target: a sample MUST NOT
   point at a protein the graph does not describe.
4. Every `CrateDatasetPart` resolves a metadata pointer or declares why it resolves none (§7).
5. Every `missing` entry names a `blocks` tier unless its reason is `not-applicable`.
6. No field is both present on an entity and declared missing on it.
7. The root's `conformsTo` names both an RO-Crate version and a LAMBDA Core profile.
8. A file entity carries `File` in its `@type`. **`DataFile` is not an RO-Crate term** — it appears
   in neither the 1.1 nor the 1.2 context (2899 terms, checked), and those contexts declare no
   `@vocab`, so the token resolves to a relative IRI against the document base rather than to any
   class. A crate using it has untyped files as far as any generic consumer is concerned. Use
   `File`, which the context maps to `schema:MediaObject`.
9. `license` and `datePublished`, when absent from the root, appear in `lambdarc:missing` (§6.4).
10. A `ProteinEntity` carries `uniprot_id` or declares it in `lambdarc:missing` (§6.2).

SHACL shapes would be the natural home for layer 3, since RDF validation dispatches on `rdf:type`
properly. They are **not** generated: `gen-shacl` raises `KeyError('lambda-ber-schema')` for classes
whose slots come from an imported schema (`shaclgen.py::_build_ignored_properties`). Worth
revisiting when that is fixed upstream.

`linkml-validate` is not usable against a crate: it iterates a data source as a collection of
instances, so a single JSON object is walked key by key, and `--legacy-mode` routes through
`gen-python`, which cannot represent `@`-keyword aliases (§16.7).

---

## 13. Worked examples

Five conformant fixtures in `tests/data/rocrate/valid/`:

| Fixture | Shows |
| :---- | :---- |
| `minimal-manifest.json` | the smallest conformant crate — the thing to hand a new facility |
| `ssrl-mx-XA_x16.json` | a real SSRL MX package brought to Core 0.3.0, with MX quantities nested in `resultSummary` |
| `saxs-glurs.json` | the SAXS GluRS dataset reduced to Core terms — the extension boundary made concrete; its sample points at a `Protein` entity (§6.2) |
| `nested-pointers.json` | one manifest using all three pointer mechanisms at once |
| `ssrl-mx-XA_x16-core-0.2.json` (in `legacy/`) | the published 0.2 crate, unmodified — see §15 |

Twelve negative fixtures in `tests/data/rocrate/invalid/`, each isolating one rule, with the test
asserting *which* rule failed so that a fixture cannot pass for the wrong reason.

---

## 14. Crosswalk to `lambda-ber-schema`

The profile module `imports` the main schema, so every controlled vocabulary — `TechniqueEnum`,
`FacilityEnum`, `FileFormatEnum`, `DataTypeEnum`, `WorkflowTypeEnum`, `SampleTypeEnum` — is
*referenced*, never restated. Every crate term with a schema counterpart declares it as an
`exact_mappings` or `close_mappings`, and `make gen-rocrate` emits the crosswalk to
`assets/rocrate/lambda_rocrate_core.sssom.tsv` — one row per mapped term, regenerated with the
profile. That file, not this table, is authoritative; no count is quoted here because it would be
wrong by the next commit.

Note that `deprecated_element_has_exact_replacement` is documentation, not a mapping predicate, so
`gen-sssom` does not read it. Every deprecated term therefore *also* carries an explicit
`exact_mappings` / `close_mappings` / `related_mappings` to its replacement — otherwise the
migration would be prose a reader has to transcribe by hand.

Class-level projection:

| Profile class | `@type` in crates | Schema class |
| :---- | :---- | :---- |
| `CrateRoot` | `["Dataset", "lambda:Dataset"]` | `Dataset` (+ `Study`, close) |
| `CrateFile` | `File` | `DataFile` |
| `SampleEntity` | `["BioChemEntity", "lambda:Sample"]` | `Sample` (+ `SampleProteinAssociation`, via `hasBioChemEntityPart`) |
| `ProteinEntity` | `["Protein", "lambda:Protein"]` | `Protein` |
| `InstrumentEntity` | `["IndividualProduct", "lambda:Instrument"]` | `Instrument` |
| `ExperimentRunAction` | `["Action", "lambda:ExperimentRun"]` | `ExperimentRun` |
| `WorkflowRunAction` | `["CreateAction", "lambda:WorkflowRun"]` | `WorkflowRun` |
| `PersonEntity` | `Person` | `Person` |
| `OrganizationEntity` | `Organization` | `Organization` |
| `CrateDatasetPart` | `Dataset` | *no counterpart* — the pointer entity |

`PersonEntity` projects onto `Person` plus a person association. The crate carries a person's role
*on the person*, because a crate describes one body of work and a flat graph has nowhere else to put
it; the schema carries it on `StudyPersonAssociation` / `ExperimentPersonAssociation` /
`WorkflowPersonAssociation`, because one person record should serve every role they hold across a
dataset. A projector therefore reads `role` (and `author_position`, `corresponding`) off the crate
entity and writes them to the association, not to `Person`.

`SampleEntity` and `ProteinEntity` split the same way the schema does. `hasBioChemEntityPart` on
the sample projects onto one `SampleProteinAssociation` per target, with `sample_id` and
`protein_id` and nothing else: the role, copy number, residue range and modifications that
association can carry describe a preparation in detail a manifest does not attempt, and belong to
the fuller record. The protein entity itself projects onto `Protein` by identity — `uniprot_id`,
`protein_name`, `gene_name`, `organism`, `pdb_entries` are the schema's own slot names. The
deprecated `uniprotId` on a sample (§15) projects by *creating* that `Protein` and association,
which is why its mapping is close rather than exact: the value is bare where the schema's is a CURIE.

`OrganizationEntity` works the same way, projecting onto `Organization` plus
`StudyOrganizationAssociation` / `PersonOrganizationAssociation`. Note the deliberate split between
`ror` and `facility_ror`: an organization's own identifier is `ror`, while `facility_ror` is a
property of an *instrument* naming the facility it sits at. Putting `facility_ror` on an
organization would assert that an organization has a facility's identifier rather than its own.

An organization that is a unit of a larger institution — a light source inside a national laboratory
— SHOULD carry `parentOrganization` and omit `ror` unless it holds one in its own right. Copying the
parent's ROR down makes the child indistinguishable from its parent in exactly the index that was
supposed to tell them apart.

Slot-level, the projection is deliberately **identity**: a crate term that maps to a schema slot
carries the schema's own `snake_case` slot name, so `lambda:file_format` in a crate *is*
`DataFile.file_format`. Only three groups deviate, each for a stated reason:

- **schema.org terms** keep schema.org's camelCase, because that is what they are (`hasPart`,
  `encodingFormat`, `datePublished`).
- **`lambdarc:` machinery** uses camelCase, following the SAXS profile's style, and has no schema
  counterpart yet (§16).
- **deprecated 0.2 spellings** keep the exact JSON key SSRL published (§15), but sit under
  `lambdarc:` like all other profile-local terms. The `lambda:` base is reserved for terms that
  resolve to a schema element; a term that resolves to nothing there would claim a projection it
  cannot make, and `lambda:rawIncluded` under the schema base is not the same IRI as the
  `lambda:rawIncluded` an SSRL crate publishes under its own base anyway. The relationship to a
  schema slot, where one exists, is carried by mappings — which is what mappings are for.

---

## 15. The SSRL 0.2 vocabulary: accepted, deprecated

SSRL publishes crates conforming to `https://w3id.org/lambda/profile/core/0.2` — a URI with no
written specification — using `lambda:Experiment` / `lambda:RawUnit` / `lambda:DerivedProduct` /
`lambda:AuxiliaryMetadataItem` and camelCase terms under
`https://w3id.org/lambda/terms/0.2/`. Those crates exist and a loader consumes them, so Core 0.3.0
accepts the 0.2 spellings and marks them deprecated rather than breaking them.

| 0.2 spelling | Core 0.3.0 |
| :---- | :---- |
| `lambda:Experiment` (root type) | `lambda:Dataset` |
| `lambda:RawUnit`, `lambda:DerivedProduct` | `Dataset` part → `CrateDatasetPart` |
| `CreateAction` for workflow runs | unchanged — 0.2 got this right |
| `sampleName` | `lambda:sample_code` |
| `proteinName` | `lambda:protein_name` |
| `uniprotId` (bare accession, on the sample) | `lambda:uniprot_id` (CURIE), on a `Protein` entity the sample points at with `hasBioChemEntityPart` |
| `rawUnitId`, `productId`, `workflowRunId` | the entity's `@id`, with `identifier` for facility accessions |
| `sampleComposition` | `lambda:molecular_composition`, in the linked record |
| `lambda:runDefinition` | `lambda:runParameters` (already renamed in 0.2) |
| `mimeType` | `encodingFormat` |
| `lambda:` = `https://w3id.org/lambda/terms/0.2/` | `lambda:` = `http://w3id.org/lambda/` (§4.3) |

Each deprecated term is declared in the profile module with its replacement, so the SSSOM crosswalk
is a machine-readable migration map rather than prose a reader has to transcribe.

### 15.1 Audit of the published 0.2 crate

The published crate is kept unmodified at
`tests/data/rocrate/legacy/ssrl-mx-XA_x16-core-0.2.json` and checked on every test run. After the
§4.4 normalizations and the alias layer, **three** substantive gaps remain — the naming differences
all resolve, so what is left is real:

1. **No `license` on the root.** Reuse terms are unstated, so the crate cannot be handed on
   safely (§6.4).
2. **MX quantities as bare properties on the `CreateAction`** — `lambda:unitCell`,
   `lambda:spaceGroup`, `lambda:completeness`, `lambda:ccHalf`, `lambda:meanISigma`,
   `lambda:resolutionAngstrom`. These belong nested in `lambdarc:resultSummary`, shaped by an MX
   extension (§12, layer 2). As written they are readable but not composable.
3. **Neither dataset part resolves a metadata pointer** (§7). The `RawUnit` and the
   `DerivedProduct` each name a body of data and say nothing about where its description lives.

None is a naming quibble and none is hard to fix; the retyped
`tests/data/rocrate/valid/ssrl-mx-XA_x16.json` shows the same package with all three closed.
`tests/test_rocrate_profile.py::test_legacy_crate_gaps_are_exactly_the_known_ones` pins them, so
when they are fixed upstream the test says so.

Coordination note: the loader that reads these crates lives on the unmerged
`feature/ssrl-mx-rocrate-loader` branch and is **not** modified by this profile. It already carries
back-compat branches for the 0.2 → later renames; those could read the SSSOM crosswalk instead of
hardcoding, but that is a separate change on that branch.

---

## 15.2 Peter Zwart's SAXS drafts: reconciliation

A parallel SAXS profile (v0.4.0) produces crates such as `SASDA55_ro-crate-metadata_v0.4.0.json`.
It agrees with Core on the things that matter most and disagrees on where the shared machinery
lives.

**Already aligned.** It binds `lambda:` to `http://w3id.org/lambda/` — the schema's own base, the
same call Core makes and the one the SSRL 0.2 crates got wrong. Its root is typed
`["Dataset", "lambda:Dataset"]`. Every one of its 38 `lambda:` terms resolves to a real schema class
or slot. It passes every Core graph rule except the `DataFile` token (§12 check 8).

**Where Core took its lead.** PROV (§9, §10), `vocabEntry` (§8.1) and `idRecipeVersion` all come
from these drafts. They are better than what Core had.

**The reconciliation.** Those drafts place the technique-neutral machinery in the SAXS terms
namespace, which would force MX either to import SAXS terms or to redefine them. Core keeps it in
`lambdarc:` and registers the SAXS spellings as mappings, so `gen-sssom` emits the migration:

| SAXS draft spelling | LAMBDA Core |
| :---- | :---- |
| `lambdax:missing` | `lambdarc:missing` (identical fields) |
| `lambdax:derived` | `lambdarc:derived` |
| `lambdax:schemaSet` | `lambdarc:schemaSet` (identical fields) |
| `lambdax:summary` | `lambdarc:resultSummary` |
| `lambdax:estimator` | `lambdarc:estimator` |
| `lambdax:designated` | `lambdarc:isDesignated` |
| `lambdax:s2_acquisition_complete` | `lambdarc:sufficiency.s2AcquisitionComplete` |
| `lambdax:sourceField` / `definition` / `admissibility` | same names under `lambdarc:` |
| `lambdax:vocabEntry`, `lambdax:idRecipeVersion` | same names under `lambdarc:` |
| `lambdax:facility` | `lambda:facility` — it is a schema slot |
| `lambdax:processing_level` | `lambda:processing_level` — likewise |

`lambdax:` keeps what is genuinely SAXS: `rg`, `i0`, `dmax`, `porodVolume`, `qRangeMeasured`,
`intensityScale`, `subtraction`, `seriesCoordinate`, `curveDesignation` / `analysisDesignation`.

**Open differences**, both for the SAXS profile rather than Core: `lambda:samples` / `instruments` /
`experiment_runs` / `workflow_runs` on the root restate the `Dataset` collection slots, where Core
relies on `hasPart` plus typed entities; and `lambda:title` is used where RO-Crate consumers look
for `name`. Carrying both costs little and is probably the right answer.

---

## 16. Change requests to `lambda-ber-schema`

Each `lambdarc:` term is a standing request; these are the ones this profile could not work around.

1. ~~**A `Person` class.**~~ **Resolved.** `Person` now exists, with `orcid`, `full_name`,
   `given_name`, `family_name`, `email`, `affiliation`, `affiliation_ror` and `person_local_id`,
   plus `StudyPersonAssociation`, `ExperimentPersonAssociation` and `WorkflowPersonAssociation`
   carrying `PersonRoleEnum` (and, on the study association, `author_position` and `corresponding`).
   `author` and `agent` now project. `ExperimentRun.operator_id` is retained for sources that
   publish only a bare operator string, and points at the structured route.
2. ~~**An `Organization` class.**~~ **Resolved.** `Organization` now exists, with `ror`, `acronym`,
   `organization_type`, `facility_code`, `facility_type`, `parent_organization_id`, `location`,
   `country`, `website`, `wikidata_id`, `is_doe_facility` and `doe_office`, plus
   `StudyOrganizationAssociation` (carrying `award_number`) and `PersonOrganizationAssociation`
   (carrying affiliation dates), and `Instrument.facility_organization_id`. `publisher` now projects.

   The class was shaped by what `FacilityEnum` already carries: every one of its 14 permissible
   values holds a ROR as the term's `meaning` plus annotations for `parent_organization`,
   `parent_ror`, `location`, `country`, `doe_office`, `website` and `wikidata_id`. That is an
   organization registry living in enum annotations, where the values are unvalidated strings and
   nothing can point at them. `Organization` gives those fields a typed home; `FacilityEnum` stays
   the controlled vocabulary saying *which* facility, joined by `facility_code`.
3. **Dataset-level publication metadata.** `Dataset` has no `license`, `datePublished`,
   `conditionsOfAccess` or `publisher`. A crate must carry these; nothing receives them.
4. **Typed checksums.** `DataFile.checksum` is an untyped string with no algorithm slot, so
   `sha256` has to be profile-local. Add an algorithm, or name the slot for its algorithm.
5. **Media types on `FileFormatEnum`.** No permissible value carries an IANA media type, so
   `encodingFormat` cannot be derived from `file_format` and both must be carried.
6. **`schema:` prefix inconsistency.** `lambda_ber_types.yaml` binds `schema:` to
   `https://schema.org/`; RO-Crate and this profile need `http://schema.org/`. Different IRIs,
   silently. Worth settling schema-wide (§4.3).
7. **`@`-keyword aliases break the language-binding generators.** `gen-python`, `gen-graphql`,
   `gen-proto` and `gen-sqlddl` all emit `@id` / `@type` as bare identifiers and produce files that
   will not parse, so `conf/rocrate-gen-config.yaml` excludes them. Upstream LinkML issue; the
   workaround is to generate bindings from the JSON Schema, where keys are strings.
8. **`gen-shacl` and imported schemas.** `KeyError('lambda-ber-schema')` in
   `_build_ignored_properties`, which costs this profile its SHACL layer (§12).
9. **Enum values real SAXS deposits need.** `DataTypeEnum` has no `scattering_curve`,
   `saxs_analysis_record`, `pddf_gnom` or `fit`; `FacilityEnum` has no `DESY`. Each is carried by a
   real crate today and declared through §8.1 rather than coerced, so the evidence for adding them
   is already written down.
10. **`WorkflowRun.output_files` duplicates `WorkflowOutputAssociation`.** Two ways to say the same
   thing means a crate builder must choose, and different builders will choose differently.
11. ~~**A `Protein` class, and a home for the UniProt accession.**~~ **Resolved.** `Protein` now
   exists in `Dataset.proteins`, identified by UniProt CURIE, with `uniprot_id`, `protein_name`,
   `gene_name`, `organism`, `amino_acid_sequence`, `pdb_entries` and the functional annotation
   collections, plus `SampleProteinAssociation` carrying role, copy number, residue range,
   modifications and observed mass. `lambdarc:uniprotId` was the standing request; `ProteinEntity`
   and `lambda:uniprot_id` now project, and the 0.2 spelling is deprecated (§15).

Not requested: technique quantity classes. Those belong to the SAXS and MX extensions, whose own
change requests already cover them.

---

## 17. Extension points

A technique extension imports this module and:

1. gives `lambdarc:resultSummary` a shape — its quantity register, method-tagged and estimator-bearing;
2. binds its artefacts to the sufficiency tiers (which file is S2-core, which is S2-acquisition);
3. adds technique acquisition terms to `ExperimentRunAction`;
4. declares its own profile URI alongside Core's in `conformsTo`;
5. generates its own JSON Schema, against which its crates validate. A Core-only schema will reject
   extension terms at layer 2, by design — validate a crate against the most specific profile it
   claims.

An extension MUST NOT redefine a Core term, move a Core term to a different entity, or relax a Core
requirement. It may tighten one.

Per P10: do not create a profile because a dataset has a name. Create one when required entities,
cardinalities, quality rules or round-trip guarantees actually differ.
