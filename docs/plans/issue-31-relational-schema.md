# Plan: Make the Schema More Relational (Issue #31)

## Problem Statement

The current schema follows an NMDC-style document-oriented design optimized for MongoDB:
- `Dataset` is `tree_root: true` - mandatory entry point
- Everything must be bundled within a `Study` using `inlined: true` and `inlined_as_list: true`
- Forces hierarchical containment rather than relational references
- No support for M:N relationships (e.g., sample used in multiple studies)

**Goal**: Restructure to a proper relational model with explicit association tables for M:N relationships.

---

## Current Architecture (Document-Oriented)

```
Dataset (tree_root: true)
├── instruments: Instrument[] (inlined)
└── studies: Study[] (inlined)
    ├── samples: Sample[] (inlined)
    ├── sample_preparations: SamplePreparation[] (inlined)
    ├── instrument_runs: ExperimentRun[] (inlined)
    ├── workflow_runs: WorkflowRun[] (inlined)
    ├── data_files: DataFile[] (inlined)
    └── images: Image[] (inlined)
```

### Problems with Current Design
1. Entities cannot exist independently of Study
2. No M:N relationships - sample can't be shared across studies
3. Relationship metadata has no home (e.g., "sample's role in experiment")
4. Doesn't map cleanly to SQL tables

---

## Proposed Architecture (Relational with Association Tables)

### Design Principles
1. **Flat entity collections** - All entities live directly in Dataset
2. **Explicit association tables** - M:N relationships via link classes
3. **No inlined collections** - Study becomes a lightweight grouping entity
4. **Relationship metadata** - Association classes can carry attributes (role, date, etc.)
5. **SQL-friendly** - Maps directly to normalized database tables

### Target Structure

```
Dataset (tree_root: true)
├── Entity Tables (flat collections)
│   ├── studies: Study[]
│   ├── instruments: Instrument[]
│   ├── samples: Sample[]
│   ├── sample_preparations: SamplePreparation[]
│   ├── experiment_runs: ExperimentRun[]
│   ├── workflow_runs: WorkflowRun[]
│   ├── data_files: DataFile[]
│   └── images: Image[]
│
└── Association Tables (M:N link tables)
    ├── study_sample_associations: StudySampleAssociation[]
    ├── study_experiment_associations: StudyExperimentAssociation[]
    ├── study_workflow_associations: StudyWorkflowAssociation[]
    ├── experiment_sample_associations: ExperimentSampleAssociation[]
    ├── experiment_instrument_associations: ExperimentInstrumentAssociation[]
    ├── workflow_experiment_associations: WorkflowExperimentAssociation[]
    ├── workflow_input_associations: WorkflowInputAssociation[]
    └── workflow_output_associations: WorkflowOutputAssociation[]
```

### Association Classes

```yaml
StudySampleAssociation:
  description: "Links a sample to a study (M:N)"
  attributes:
    study_id:
      range: Study
      required: true
    sample_id:
      range: Sample
      required: true
    role:
      description: "Role of sample in study (e.g., target, control, reference)"
      range: SampleRoleEnum
    date_added:
      range: date

StudyExperimentAssociation:
  description: "Links an experiment run to a study (M:N)"
  attributes:
    study_id:
      range: Study
      required: true
    experiment_id:
      range: ExperimentRun
      required: true

ExperimentSampleAssociation:
  description: "Links a sample to an experiment (M:N)"
  attributes:
    experiment_id:
      range: ExperimentRun
      required: true
    sample_id:
      range: Sample
      required: true
    role:
      description: "Role in experiment (e.g., target, buffer_blank, standard)"
      range: ExperimentSampleRoleEnum
    preparation_id:
      description: "Specific preparation used for this sample in this experiment"
      range: SamplePreparation

ExperimentInstrumentAssociation:
  description: "Links an instrument to an experiment (M:N for multi-instrument setups)"
  attributes:
    experiment_id:
      range: ExperimentRun
      required: true
    instrument_id:
      range: Instrument
      required: true
    role:
      description: "Role of instrument (e.g., primary, detector, sample_changer)"
      range: InstrumentRoleEnum

WorkflowExperimentAssociation:
  description: "Links source experiments to a workflow (M:N - workflows can merge data)"
  attributes:
    workflow_id:
      range: WorkflowRun
      required: true
    experiment_id:
      range: ExperimentRun
      required: true

WorkflowInputAssociation:
  description: "Links input files to a workflow"
  attributes:
    workflow_id:
      range: WorkflowRun
      required: true
    file_id:
      range: DataFile
      required: true
    input_type:
      description: "Type of input (e.g., raw_data, reference, parameters)"
      range: InputTypeEnum

WorkflowOutputAssociation:
  description: "Links output files to a workflow"
  attributes:
    workflow_id:
      range: WorkflowRun
      required: true
    file_id:
      range: DataFile
      required: true
    output_type:
      description: "Type of output (e.g., processed_data, log, model)"
      range: OutputTypeEnum
```

### Entity Changes

**Study** - Remove all inlined collections, becomes lightweight:
```yaml
Study:
  is_a: NamedThing
  description: "A logical grouping of related experiments around a research question"
  attributes:
    # Keep metadata only
    keywords: ...
    # NO samples, experiment_runs, etc. - use association tables
```

**Sample, ExperimentRun, WorkflowRun, etc.** - Remove study_ids, use association tables:
```yaml
Sample:
  attributes:
    # NO study_ids - relationship via StudySampleAssociation
    # Keep all other attributes

ExperimentRun:
  attributes:
    # NO study_ids, sample_ids, instrument_id
    # Relationships via association tables
    # Keep technique, experimental_conditions, quality_metrics, etc.

WorkflowRun:
  attributes:
    # NO study_ids, experiment_ids, input/output file refs
    # Relationships via association tables
    # Keep workflow_type, software_name, processing_parameters, etc.
```

### Relationship Cardinality

| Relationship | Association Table | Metadata Fields |
|--------------|-------------------|-----------------|
| Study ↔ Sample | StudySampleAssociation | role, date_added |
| Study ↔ ExperimentRun | StudyExperimentAssociation | - |
| Study ↔ WorkflowRun | StudyWorkflowAssociation | - |
| ExperimentRun ↔ Sample | ExperimentSampleAssociation | role, preparation_id |
| ExperimentRun ↔ Instrument | ExperimentInstrumentAssociation | role |
| WorkflowRun ↔ ExperimentRun | WorkflowExperimentAssociation | - |
| WorkflowRun ↔ DataFile (in) | WorkflowInputAssociation | input_type |
| WorkflowRun ↔ DataFile (out) | WorkflowOutputAssociation | output_type |

---

## Detailed Schema Changes

### Dataset (Complete Restructure)

```yaml
Dataset:
  is_a: NamedThing
  tree_root: true
  description: >-
    Root container holding flat entity collections and association tables.
    Follows relational database design patterns.
  attributes:
    keywords:
      range: string
      multivalued: true

    # ===== ENTITY TABLES =====
    studies:
      description: "All studies in this dataset"
      range: Study
      multivalued: true
      inlined_as_list: true
    instruments:
      description: "All instruments"
      range: Instrument
      multivalued: true
      inlined_as_list: true
    protein_constructs:
      range: ProteinConstruct
      multivalued: true
      inlined_as_list: true
    samples:
      range: Sample
      multivalued: true
      inlined_as_list: true
    sample_preparations:
      range: SamplePreparation
      multivalued: true
      inlined_as_list: true
    experiment_runs:
      range: ExperimentRun
      multivalued: true
      inlined_as_list: true
    workflow_runs:
      range: WorkflowRun
      multivalued: true
      inlined_as_list: true
    data_files:
      range: DataFile
      multivalued: true
      inlined_as_list: true
    images:
      range: Image
      multivalued: true
      inlined_as_list: true

    # ===== ASSOCIATION TABLES =====
    study_sample_associations:
      description: "Links between studies and samples (M:N)"
      range: StudySampleAssociation
      multivalued: true
      inlined_as_list: true
    study_experiment_associations:
      description: "Links between studies and experiments (M:N)"
      range: StudyExperimentAssociation
      multivalued: true
      inlined_as_list: true
    study_workflow_associations:
      description: "Links between studies and workflows (M:N)"
      range: StudyWorkflowAssociation
      multivalued: true
      inlined_as_list: true
    experiment_sample_associations:
      description: "Links between experiments and samples (M:N with role)"
      range: ExperimentSampleAssociation
      multivalued: true
      inlined_as_list: true
    experiment_instrument_associations:
      description: "Links between experiments and instruments (M:N)"
      range: ExperimentInstrumentAssociation
      multivalued: true
      inlined_as_list: true
    workflow_experiment_associations:
      description: "Links between workflows and source experiments (M:N)"
      range: WorkflowExperimentAssociation
      multivalued: true
      inlined_as_list: true
    workflow_input_associations:
      description: "Links between workflows and input files"
      range: WorkflowInputAssociation
      multivalued: true
      inlined_as_list: true
    workflow_output_associations:
      description: "Links between workflows and output files"
      range: WorkflowOutputAssociation
      multivalued: true
      inlined_as_list: true
```

### Study (Simplified - No Inlined Collections)

```yaml
Study:
  is_a: NamedThing
  description: "A logical grouping of related experiments investigating a research question"
  attributes:
    keywords:
      range: string
      multivalued: true
    # All relationships via association tables - no inlined collections
```

### Sample (No Relationship Slots)

```yaml
Sample:
  is_a: NamedThing
  attributes:
    sample_code:
      required: true
    sample_type:
      range: SampleTypeEnum
      required: true
    # ... keep all existing data attributes
    # REMOVE: study_ids (use StudySampleAssociation)
    # Keep parent_sample_id as it's a true FK, not M:N
    parent_sample_id:
      range: Sample
```

### ExperimentRun (No Relationship Slots)

```yaml
ExperimentRun:
  is_a: NamedThing
  attributes:
    experiment_code:
      required: true
    technique:
      range: TechniqueEnum
      required: true
    # ... keep all existing data attributes (experimental_conditions, quality_metrics, etc.)
    # REMOVE: sample_id, instrument_id, study_ids
    # All relationships via association tables
```

### WorkflowRun (No Relationship Slots)

```yaml
WorkflowRun:
  is_a: NamedThing
  attributes:
    workflow_code:
      required: true
    workflow_type:
      range: WorkflowTypeEnum
      required: true
    software_name:
      required: true
    # ... keep all existing data attributes
    # REMOVE: experiment_id, study_ids, input/output file refs
    # All relationships via association tables
```

### New Association Classes

```yaml
StudySampleAssociation:
  description: "M:N link between Study and Sample"
  attributes:
    study_id:
      range: Study
      required: true
    sample_id:
      range: Sample
      required: true
    role:
      range: SampleRoleEnum
    date_added:
      range: date

StudyExperimentAssociation:
  description: "M:N link between Study and ExperimentRun"
  attributes:
    study_id:
      range: Study
      required: true
    experiment_id:
      range: ExperimentRun
      required: true

StudyWorkflowAssociation:
  description: "M:N link between Study and WorkflowRun"
  attributes:
    study_id:
      range: Study
      required: true
    workflow_id:
      range: WorkflowRun
      required: true

ExperimentSampleAssociation:
  description: "M:N link between ExperimentRun and Sample with role metadata"
  attributes:
    experiment_id:
      range: ExperimentRun
      required: true
    sample_id:
      range: Sample
      required: true
    role:
      description: "Role of sample in experiment"
      range: ExperimentSampleRoleEnum
    preparation_id:
      description: "Specific preparation used"
      range: SamplePreparation

ExperimentInstrumentAssociation:
  description: "M:N link between ExperimentRun and Instrument"
  attributes:
    experiment_id:
      range: ExperimentRun
      required: true
    instrument_id:
      range: Instrument
      required: true
    role:
      range: InstrumentRoleEnum

WorkflowExperimentAssociation:
  description: "M:N link between WorkflowRun and source ExperimentRuns"
  attributes:
    workflow_id:
      range: WorkflowRun
      required: true
    experiment_id:
      range: ExperimentRun
      required: true

WorkflowInputAssociation:
  description: "Links input DataFiles to WorkflowRun"
  attributes:
    workflow_id:
      range: WorkflowRun
      required: true
    file_id:
      range: DataFile
      required: true
    input_type:
      range: InputTypeEnum

WorkflowOutputAssociation:
  description: "Links output DataFiles to WorkflowRun"
  attributes:
    workflow_id:
      range: WorkflowRun
      required: true
    file_id:
      range: DataFile
      required: true
    output_type:
      range: OutputTypeEnum
```

### New Enumerations

```yaml
SampleRoleEnum:
  permissible_values:
    target:
      description: "Primary sample under investigation"
    control:
      description: "Control sample"
    reference:
      description: "Reference standard"
    blank:
      description: "Buffer blank or negative control"

ExperimentSampleRoleEnum:
  permissible_values:
    target:
      description: "Primary target of measurement"
    buffer_blank:
      description: "Buffer-only measurement for subtraction"
    standard:
      description: "Calibration or reference standard"
    size_marker:
      description: "Molecular weight marker"

InstrumentRoleEnum:
  permissible_values:
    primary:
      description: "Primary data collection instrument"
    detector:
      description: "Secondary detector"
    sample_handler:
      description: "Automated sample handling"

InputTypeEnum:
  permissible_values:
    raw_data:
      description: "Raw experimental data"
    reference:
      description: "Reference data (e.g., PDB model)"
    parameters:
      description: "Processing parameters file"
    mask:
      description: "Mask or selection file"

OutputTypeEnum:
  permissible_values:
    processed_data:
      description: "Processed/corrected data"
    model:
      description: "Structural model"
    map:
      description: "Density map or reconstruction"
    log:
      description: "Processing log"
    statistics:
      description: "Quality statistics"
```

---

## Example Data: Relational with Association Tables

```yaml
# Dataset-relational-example.yaml
id: lambdaber:dataset_berkeley_multimodal
title: "Berkeley Multimodal Structural Biology Dataset"
description: "Demonstrating relational pattern with explicit association tables"

# ===== ENTITY TABLES =====

instruments:
  - id: lambdaber:titan_001
    instrument_code: "TITAN-K3-001"
    manufacturer: "ThermoFisher"

  - id: lambdaber:sibyls_001
    instrument_code: "ALS-12.3.1"
    facility_name: "ALS"

studies:
  - id: lambdaber:study_tfiid_cryoem
    title: "TFIID Cryo-EM Study"
    keywords: ["cryo-EM", "transcription", "TFIID"]

  - id: lambdaber:study_tfiid_saxs
    title: "TFIID Solution Scattering Study"
    keywords: ["SAXS", "transcription", "TFIID"]

samples:
  - id: lambdaber:sample_tfiid
    sample_code: "TFIID-001"
    sample_type: complex
    molecular_weight: 1200.0
    # NO study_ids here - relationships via association tables

  - id: lambdaber:sample_bsa
    sample_code: "REFERENCE-BSA"
    sample_type: protein
    molecular_weight: 66.5

experiment_runs:
  - id: lambdaber:exp_cryoem_001
    experiment_code: "EXP-CRYOEM-001"
    technique: cryo_em
    # NO sample_ids, instrument_ids - via association tables

  - id: lambdaber:exp_saxs_001
    experiment_code: "EXP-SAXS-001"
    technique: saxs

data_files:
  - id: lambdaber:file_micrographs_001
    file_name: "micrographs_001.mrc"
    file_format: mrc

  - id: lambdaber:file_scattering_001
    file_name: "saxs_curve.dat"
    file_format: dat

workflow_runs:
  - id: lambdaber:wf_mc_001
    workflow_code: "WF-MC-001"
    workflow_type: motion_correction
    software_name: "MotionCor2"
    software_version: "1.6.4"

  - id: lambdaber:wf_integration_001
    workflow_code: "WF-INTEGRATE-001"
    workflow_type: data_integration
    software_name: "Custom Pipeline"

# ===== ASSOCIATION TABLES =====

# Sample used in multiple studies (M:N)
study_sample_associations:
  - study_id: lambdaber:study_tfiid_cryoem
    sample_id: lambdaber:sample_tfiid
    role: target

  - study_id: lambdaber:study_tfiid_saxs
    sample_id: lambdaber:sample_tfiid
    role: target

  - study_id: lambdaber:study_tfiid_saxs
    sample_id: lambdaber:sample_bsa
    role: reference

# Experiments belong to studies
study_experiment_associations:
  - study_id: lambdaber:study_tfiid_cryoem
    experiment_id: lambdaber:exp_cryoem_001

  - study_id: lambdaber:study_tfiid_saxs
    experiment_id: lambdaber:exp_saxs_001

# Experiment uses samples (with roles)
experiment_sample_associations:
  - experiment_id: lambdaber:exp_cryoem_001
    sample_id: lambdaber:sample_tfiid
    role: target

  - experiment_id: lambdaber:exp_saxs_001
    sample_id: lambdaber:sample_tfiid
    role: target

  - experiment_id: lambdaber:exp_saxs_001
    sample_id: lambdaber:sample_bsa
    role: buffer_blank

# Experiment uses instruments
experiment_instrument_associations:
  - experiment_id: lambdaber:exp_cryoem_001
    instrument_id: lambdaber:titan_001
    role: primary

  - experiment_id: lambdaber:exp_saxs_001
    instrument_id: lambdaber:sibyls_001
    role: primary

# Workflow processes experiments (M:N - integration workflow uses both)
workflow_experiment_associations:
  - workflow_id: lambdaber:wf_mc_001
    experiment_id: lambdaber:exp_cryoem_001

  - workflow_id: lambdaber:wf_integration_001
    experiment_id: lambdaber:exp_cryoem_001

  - workflow_id: lambdaber:wf_integration_001
    experiment_id: lambdaber:exp_saxs_001

# Workflow outputs
workflow_output_associations:
  - workflow_id: lambdaber:wf_mc_001
    file_id: lambdaber:file_micrographs_001
    output_type: processed_data
```

### SQL Table Mapping

The above YAML maps directly to SQL tables:

```sql
-- Entity tables
CREATE TABLE samples (id, sample_code, sample_type, molecular_weight, ...);
CREATE TABLE studies (id, title, keywords, ...);
CREATE TABLE experiment_runs (id, experiment_code, technique, ...);

-- Association tables (join tables)
CREATE TABLE study_sample_associations (
  study_id REFERENCES studies(id),
  sample_id REFERENCES samples(id),
  role TEXT,
  PRIMARY KEY (study_id, sample_id)
);

CREATE TABLE experiment_sample_associations (
  experiment_id REFERENCES experiment_runs(id),
  sample_id REFERENCES samples(id),
  role TEXT,
  preparation_id REFERENCES sample_preparations(id),
  PRIMARY KEY (experiment_id, sample_id)
);
```

### Key Relational Features Demonstrated:
1. **Sample reuse**: `sample_tfiid` linked to both studies via separate association rows
2. **Role metadata**: `experiment_sample_associations` captures sample's role (target vs buffer_blank)
3. **Multi-experiment workflows**: `wf_integration_001` linked to both cryo-EM and SAXS experiments
4. **Clean separation**: Entities contain only intrinsic data; relationships are explicit

---

## Impact Assessment

### Breaking Changes
- **Study**: Remove all inlined collections (samples, experiment_runs, etc.)
- **ExperimentRun**: Remove `sample_id`, `instrument_id` slots
- **WorkflowRun**: Remove `experiment_id` slot
- **All existing examples**: Will need to be rewritten

### New Additions
- 8 new association classes for M:N relationships
- 5 new enumerations for role metadata
- Flat entity collection slots on Dataset
- Association table slots on Dataset

### Migration Required
All existing test examples in `tests/data/valid/` will need to be converted to the new relational format with association tables.

### Benefits
- Clean relational model - maps directly to SQL
- M:N relationships properly supported
- Relationship metadata (roles) has a home
- No data duplication
- Simpler entity classes (only intrinsic attributes)

---

## Task Breakdown

1. **Add association classes** - All 8 association classes with their attributes
2. **Add role enumerations** - SampleRoleEnum, ExperimentSampleRoleEnum, etc.
3. **Add flat entity collections to Dataset** - samples, experiment_runs, etc.
4. **Add association table slots to Dataset** - study_sample_associations, etc.
5. **Simplify Study** - Remove all inlined collections
6. **Simplify ExperimentRun** - Remove sample_id, instrument_id
7. **Simplify WorkflowRun** - Remove experiment_id, input/output file refs
8. **Rewrite all test examples** - Convert to relational format
9. **Update documentation** - CLAUDE.md, spec.md
10. **Generate and validate** - Run `make test`

---

## Open Questions

1. **Association class identifiers?**
   - Should association classes have their own `id` field?
   - Or use composite key (study_id + sample_id)?
   - Recommendation: No id - use composite key pattern

2. **Orphan entities?**
   - Allow samples/experiments with no study associations?
   - Recommendation: Yes - enables facility catalogs, standalone data

3. **Cascading semantics?**
   - If Study is deleted, delete associations?
   - Handled at application/database level, not schema

4. **Additional association metadata?**
   - What other attributes might associations need?
   - Examples: `date_added`, `added_by`, `notes`
   - Can add later as needed

5. **Naming convention?**
   - `StudySampleAssociation` vs `study_sample_link` vs `study_sample`?
   - Current: `*Association` for classes, `*_associations` for slots
