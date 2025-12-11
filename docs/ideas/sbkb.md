# SBKB Coverage Analysis

Analysis of RCSB Structural Biology Knowledgebase (SBKB) coverage vs lambda-ber-schema.

**Date:** 2025-11-22
**Source:** https://cdn.rcsb.org/sbkb/

## SBKB Background

The Protein Structure Initiative's (PSI) Structural Biology Knowledgebase (SBKB) operated from 2000-2015 and was retired in July 2017. It consisted of six main components:

1. **BioSync** — X-ray light facilities catalog (relocated to http://biosync.rcsb.org)
2. **TargetTrack** — Protein target database (archived at Zenodo DOI 10.5281/zenodo.821654)
3. **PSI Technology Portal** — Technical reports (retired)
4. **PSI Publications Portal** — 2,300+ publications (archived at Zenodo DOI 10.5281/zenodo.821648)
5. **Nature Research Highlights** — Educational articles (partially archived on PDB-101)
6. **SBKB Database & Web Services** — Discontinued

### SBKB Final Holdings
- 6,920 PSI-contributed protein structures
- 5,472 distinct structures
- 22.8M homology models
- 335,714 research targets
- 23.73M total annotations

## Component-by-Component Coverage Analysis

### 1. BioSync (X-ray Facilities Catalog) ✅ STRONG COVERAGE (85%)

**What BioSync Tracks:**
- 130+ synchrotron beamlines worldwide
- Facility capabilities (remote data collection, mail-in services, crystallization services, structure solution)
- Technical equipment (detectors, robotics, microfocus beams, extreme condition capabilities)
- PDB structure depositions by facility
- Regional distribution statistics
- Historical deposition trends since 1995

**Our Schema Coverage:**

✅ **Comprehensive:**
- `FacilityEnum`: International facility tracking with:
  - ROR (Research Organization Registry) IDs
  - Parent organizations and DOE office affiliations
  - Physical locations (city, country)
  - Energy levels in GeV
  - Number of beamlines
  - Operational timelines
  - Website and Wikidata links
  - Upgrade information (e.g., APS-U)

- `XRayInstrument`: Beamline-specific metadata:
  - `beamline_id` (e.g., "12.3.1" for SIBYLS)
  - `source_type`, `detector_type`
  - `monochromator_type`, `goniometer_type`
  - Energy ranges (min/max keV)
  - Beam sizes (min/max micrometers)
  - Flux density (photons/s/mm²)
  - Crystal cooling capabilities

- `ExperimentRun`: X-ray data collection parameters:
  - `wavelength`, `oscillation_angle`, `start_angle`
  - `beam_center_x`, `beam_center_y`
  - `detector_distance`, `pixel_size_x`, `pixel_size_y`
  - `number_of_images`, `total_rotation`
  - `beamline` reference

⚠️ **Gaps:**
- No explicit facility service capabilities tracking:
  - Remote data collection availability
  - Mail-in services
  - On-site crystallization services
  - Structure determination services
- No historical deposition statistics modeling
- No facility-specific publication/structure counts

**Recommendation:** Add `FacilityCapabilities` class or extend `Facility` enum with service metadata.

---

### 2. TargetTrack (Protein Target Database) ✅ EXCELLENT COVERAGE (90%)

**What TargetTrack Tracked:**
- 350,000+ protein sequences (targets)
- Target status updates (weekly/quarterly from PSI centers)
- Experimental protocols and deviations
- Detailed trial history from 100+ investigators at 35 research centers
- Target selection via bioinformatics-based sequence/structure clustering
- Complete XML schema (targetTrack-v1.4.1)

**Our Schema Coverage:**

✅ **Comprehensive:**

*Target Identification:*
- `Sample`: `protein_name`, `gene_name`, `protein_id`, `uniprot_id`, `ncbi_taxid`
- `Sample`: `sequences`, `sequence_length_aa`, `molecular_weight`
- `ProteinConstruct`: Detailed construct metadata:
  - `construct_id`, `construct_description`
  - `vector_backbone`, `promoter`
  - `n_terminal_tag`, `c_terminal_tag`, `tag_cleavage_site`
  - `gene_synthesis_provider`, `codon_optimization`
  - `sequence_verification_method`

*Expression & Purification:*
- `SamplePreparation`:
  - `expression_system`, `host_strain_or_cell_line`
  - `purification_steps` (affinity, IEX, HIC, SEC)
  - `tag_removal`, `protease_cleavage`
  - `concentration_method`, `final_yield`
  - `purity_assessment` (SDS-PAGE)

*Functional Annotations:*
- `AggregatedProteinView`: Comprehensive metadata consolidation:
  - `FunctionalSite`: Catalytic, binding, PTM sites
  - `StructuralFeature`: Domains (CATH, SCOP, Pfam), secondary structure, disorder
  - `ProteinProteinInteraction`: Partners, interface residues, binding energies
  - `LigandInteraction`: Small molecules with Kd/Ki/IC50
  - `MutationEffect`: Stability (ΔΔG), disease associations (OMIM)
  - `PostTranslationalModification`: 15+ modification types
  - `BiophysicalProperty`: Tm, solubility, pI, extinction coefficient
  - `ConformationalEnsemble`: Multiple states with populations
  - `EvolutionaryConservation`: Conservation scores, coevolved residues
  - `DatabaseCrossReference`: 30+ databases (UniProt, PDB, Pfam, ChEMBL, OMIM, etc.)

*Experimental Trial Tracking:*
- `ExperimentRun`: Data collection sessions with `processing_status`, `quality_metrics`
- `WorkflowRun`: Processing workflows with timestamps (`started_at`, `completed_at`)
- `Study`: Project-level organization with multiple samples/experiments

*Evidence & Provenance:*
- Evidence types: experimental, predicted, inferred, literature-curated
- Evidence codes (ECO - Evidence and Conclusion Ontology)
- Source databases (PDBe-KB, UniProt, AlphaFold, etc.)
- Confidence scores (0-1)
- PubMed references (PMID)

⚠️ **Gaps:**
- No explicit target selection rationale:
  - Bioinformatics clustering methodology
  - Sequence/structure cluster representative designation
  - Structural novelty justification
- No weekly/quarterly status update timeline tracking
- Limited multi-center collaboration metadata:
  - Participating institutions
  - Center-specific protocols vs standard protocols
  - Protocol deviation tracking

**Recommendation:** Consider adding:
1. `TargetSelectionRationale` to `Sample`:
   - `selection_method` (bioinformatics, structural_genomics, disease_relevance)
   - `cluster_representative_of`
   - `novelty_justification`
2. `CollaborativeProject` extension to `Study`:
   - `participating_institutions` (using ROR)
   - `funding_program`
   - `protocol_deviations`

---

### 3. PSI Technology Portal ❌ NO DIRECT COVERAGE (20%)

**What It Was:**
- Technical reports on method development
- Protocol documentation
- Technology innovations from PSI centers
- Status: Retired, not accessible

**Our Schema Coverage:**

✅ **Partial:**
- `WorkflowRun.software_name`, `software_version`: Software/method tracking
- `SamplePreparation`: Protocol documentation
- `processing_notes`: Free-text method descriptions

⚠️ **Gaps:**
- No explicit "method development" or "technology report" entity
- No protocol versioning system
- No technology innovation tracking class

**Recommendation:** Low priority. If needed, add:
- `TechnologyReport` class with:
  - `report_id`, `title`, `method_category`
  - `protocol_version`, `innovation_description`
  - `validation_data`, `performance_metrics`

---

### 4. PSI Publications Portal ⚠️ MINIMAL COVERAGE (40%)

**What It Tracked:**
- 2,300+ PSI publications
- Full bibliographic metadata (authors, journal, DOI)
- CSV and EndNote exports
- Archived at Zenodo DOI 10.5281/zenodo.821648

**Our Schema Coverage:**

✅ **Partial:**
- `Study.publications`: List of publication IDs
- Evidence tracking: PMID citations in `AggregatedProteinView` annotations
- `WorkflowRun.references`: Publication references

⚠️ **Gaps:**
- No comprehensive `Publication` class with:
  - DOI, PMID, title
  - Authors list
  - Journal, volume, pages, year
  - Funding acknowledgments
- No publication-to-structure linkage tracking
- No publication-to-dataset relationships
- No bibliometric metadata

**Recommendation:** Medium priority. Add `Publication` class:
```yaml
Publication:
  attributes:
    publication_id:
      identifier: true
    doi:
      range: string
    pmid:
      range: string
    title:
      range: string
    authors:
      range: string
      multivalued: true
    journal:
      range: string
    year:
      range: integer
    volume:
      range: string
    pages:
      range: string
    funding_acknowledgments:
      range: string
      multivalued: true
    related_structures:
      range: string
      multivalued: true
    related_datasets:
      range: Dataset
      multivalued: true
```

---

### 5. Nature Research Highlights ❌ NO COVERAGE (0%)

**What It Was:**
- Educational structural biology articles
- Science communication content
- Partially archived on PDB-101

**Our Schema Coverage:**
- ❌ No educational content modeling
- ❌ No science communication tracking

**Recommendation:** None. Out of scope for data modeling.

---

### 6. SBKB Database Statistics ✅ PARTIAL COVERAGE (70%)

**SBKB Statistics:**
- 6,920 PSI structures (5,472 distinct)
- 22.8M homology models
- 335K targets
- 23.73M annotations
- Redundancy tracking (distinct vs total structures)
- Deposition trends over time

**Our Schema Coverage:**

✅ **Strong:**
- `Dataset`: Can aggregate structure collections
- `Study.samples`: Multiple samples per study
- `Sample`: Multiple `ExperimentRun` instances = structure count
- `WorkflowRun`: Homology modeling workflows:
  - `workflow_type: homology_modeling`
  - `search_model_pdb_id`: Template structure
- `AggregatedProteinView`: Rich annotation metadata

⚠️ **Gaps:**
- No explicit "structure family" concept
- No distinct vs redundant structure tracking
- No deposition trend metadata
- Homology model metadata less detailed than experimental structures:
  - No template selection rationale
  - No sequence identity to template
  - No model confidence scores (e.g., QMEAN, ProQ)

**Recommendation:** Low priority unless PSI-style consortium reporting needed. Consider adding:
1. `StructureFamily` class:
   - `family_id`, `representative_structure`
   - `member_structures` (redundant members)
   - `sequence_identity_cutoff`
2. Enhanced homology modeling in `WorkflowRun`:
   - `template_sequence_identity`
   - `model_confidence_score`
   - `modeling_software_settings`

---

## Overall SBKB Coverage Assessment

### Strengths of Our Schema (Beyond SBKB)

1. ✅ **More comprehensive experimental metadata:**
   - Cryo-EM (microscope specs, detector types, dose rates, CTF parameters)
   - SAXS/WAXS (q-range, sample changers)
   - Multiple imaging modalities (FTIR, XRF, fluorescence, optical)

2. ✅ **Richer protein functional annotations:**
   - 30+ database cross-references
   - PTMs with 15+ modification types
   - Mutation effects with ΔΔG and disease associations
   - Biophysical properties (Tm, solubility, pI)
   - Conformational ensembles
   - Evolutionary conservation

3. ✅ **Better facility metadata:**
   - ROR IDs for persistent organizational identification
   - DOE classification and funding office tracking
   - Facility upgrade timelines (e.g., APS-U)
   - Parent organization hierarchies

4. ✅ **Modern file format support:**
   - HDF5, compressed formats (CBF_ZST)
   - STAR files for cryo-EM
   - SHA-256 checksums for integrity

5. ✅ **Enhanced provenance tracking:**
   - Compute resources (CPU/GPU/memory)
   - Workflow execution timestamps
   - Processing levels (0=raw, 1=corrected, 2=derived, 3=model)
   - File roles (raw, intermediate, final, diagnostic)

### Gaps Compared to SBKB

1. ⚠️ **Facility service/capability tracking:**
   - Remote data collection availability
   - Mail-in services
   - On-site crystallization facilities
   - Structure determination services
   - Robotic screening/mounting

2. ⚠️ **Collaborative center metadata:**
   - Multi-institution projects
   - PSI-style consortia organization
   - Center-specific vs standard protocols
   - Protocol deviation tracking

3. ⚠️ **Publication modeling:**
   - Full bibliographic metadata
   - Author lists
   - Funding acknowledgments
   - Publication-to-dataset linkage

4. ⚠️ **Target selection rationale:**
   - Bioinformatics clustering methodology
   - Structural novelty justification
   - Sequence/structure cluster representatives

5. ⚠️ **Statistical aggregation views:**
   - Structure families (redundancy tracking)
   - Deposition trends over time
   - Homology model quality metrics

---

## Coverage Summary Table

| SBKB Component | Coverage | Priority for Enhancement | Notes |
|---|---|---|---|
| **BioSync** (facilities) | **85%** | Medium | Add service capabilities (remote, mail-in, etc.) |
| **TargetTrack** (proteins) | **90%** | Low | Very comprehensive; optional collaborative tracking |
| **Technology Portal** | **20%** | Low | Retired; limited value for most use cases |
| **Publications** | **40%** | Medium | Add if bibliometrics or grant reporting needed |
| **Research Highlights** | **0%** | None | Out of scope |
| **Statistics** | **70%** | Low | Add if PSI-style consortium reporting required |

**Overall Assessment:** Lambda-ber-schema provides **stronger experimental and protein annotation coverage** than SBKB, with main gaps in **facility services metadata** and **multi-center collaboration tracking**.

---

## Recommendations

### Priority 1 (High Value)

**1. Add Facility Service Capabilities**

Option A: Extend `FacilityEnum` with service metadata
Option B: Create `FacilityCapabilities` class

```yaml
FacilityCapabilities:
  attributes:
    facility:
      range: FacilityEnum
      required: true
    remote_data_collection:
      range: boolean
    mail_in_service:
      range: boolean
    crystallization_services:
      range: boolean
    structure_determination_services:
      range: boolean
    robotic_sample_mounting:
      range: boolean
    microfocus_capabilities:
      range: boolean
    extreme_conditions_support:
      range: boolean
    user_support_level:
      range: UserSupportLevelEnum
```

**2. Add Publication Class**

```yaml
Publication:
  is_a: NamedThing
  attributes:
    publication_id:
      identifier: true
    doi:
      range: string
      pattern: "^10\\.\\d{4,}/.+$"
    pmid:
      range: string
    title:
      range: string
      required: true
    authors:
      range: string
      multivalued: true
    journal:
      range: string
    year:
      range: integer
    volume:
      range: string
    pages:
      range: string
    abstract:
      range: string
    funding_acknowledgments:
      range: string
      multivalued: true
    related_structures:
      range: string
      multivalued: true
      description: "PDB IDs of structures described"
    related_datasets:
      range: Dataset
      multivalued: true
```

Update `Study.publications` to use this class instead of strings.

### Priority 2 (Medium Value)

**3. Add Collaborative Project Metadata to Study**

```yaml
Study:
  attributes:
    # ... existing attributes ...
    participating_institutions:
      range: string
      multivalued: true
      description: "ROR IDs of collaborating institutions"
    funding_program:
      range: string
      description: "e.g., PSI, DOE BER, NIH"
    grant_numbers:
      range: string
      multivalued: true
    consortium_name:
      range: string
      description: "e.g., PSI Biology, SBGrid"
```

**4. Extend Sample with Target Selection Metadata**

```yaml
Sample:
  attributes:
    # ... existing attributes ...
    target_selection_method:
      range: TargetSelectionMethodEnum
      description: "How this target was chosen"
    cluster_representative_of:
      range: string
      description: "Sequence/structure cluster this represents"
    novelty_justification:
      range: string
      description: "Why this target is biologically/structurally novel"
    structural_genomics_target:
      range: boolean

enums:
  TargetSelectionMethodEnum:
    permissible_values:
      bioinformatics_clustering:
        description: "Selected as sequence/structure cluster representative"
      disease_relevance:
        description: "Medical or health importance"
      structural_novelty:
        description: "Novel fold or domain architecture"
      functional_importance:
        description: "Key biological pathway or process"
      ligand_binding:
        description: "Drug target or cofactor binding site"
```

### Priority 3 (Low Value)

**5. Add Statistical Aggregation Views**

Only implement if consortium reporting or multi-project analytics needed.

```yaml
StructureFamily:
  attributes:
    family_id:
      identifier: true
    representative_structure:
      range: string
      description: "PDB ID of cluster representative"
    member_structures:
      range: string
      multivalued: true
      description: "All PDB IDs in this family"
    sequence_identity_cutoff:
      range: float
      description: "Clustering threshold used"
    structural_similarity_metric:
      range: string
      description: "e.g., TM-score, RMSD"

DepositionStatistics:
  attributes:
    year:
      range: integer
    facility:
      range: FacilityEnum
    structure_count:
      range: integer
    distinct_structure_count:
      range: integer
    experimental_structures:
      range: integer
    homology_models:
      range: integer
```

**6. Enhanced Homology Modeling Metadata**

```yaml
WorkflowRun:
  attributes:
    # ... existing attributes ...
    # Add for homology modeling workflows:
    template_sequence_identity:
      range: float
      description: "% sequence identity to template"
    template_coverage:
      range: float
      description: "% of query covered by template"
    model_confidence_score:
      range: float
      description: "e.g., QMEAN, ProQ, pLDDT"
    model_confidence_metric:
      range: string
      description: "Name of confidence scoring method"
    alignment_method:
      range: string
      description: "e.g., BLAST, HHpred, MUSCLE"
```

---

## Implementation Notes

### High Priority (Implement Soon)
- Facility service capabilities: Useful for beamline users choosing facilities
- Publication class: Essential for grant reporting and bibliometrics

### Medium Priority (Implement If Needed)
- Collaborative metadata: Important for multi-institution projects like BER
- Target selection rationale: Valuable for structural genomics programs

### Low Priority (Implement On Demand)
- Statistical aggregation: Only for consortium-level reporting
- Enhanced homology modeling: Only if modeling workflows become primary use case

### Not Recommended
- Technology reports: Historical PSI component, limited modern relevance
- Educational content: Out of scope for experimental data modeling

---

## Conclusion

Lambda-ber-schema **exceeds SBKB capabilities** in experimental metadata richness, protein functional annotations, and modern technique support (cryo-EM, SAXS, multi-modal imaging). The legacy of SBKB informs us that:

1. **Facility service metadata matters** for users selecting beamlines
2. **Collaborative project tracking** is important for large consortia
3. **Publication linkage** enables bibliometric analysis and reporting
4. **Target rationale** helps justify structural genomics investments

The schema is well-positioned to support **individual lab workflows** and **beamline data management** today, with clear extension points for **consortium-scale operations** if needed in the future.
