# PDB Deposition and OneDep

## Overview

This document describes the practical workflow for depositing structures to the Protein Data Bank (PDB) and how lambda-ber-schema relates to the deposition process.

## How Structures Get Deposited

### The Reality: Software-Generated Files

Researchers almost never manually author mmCIF files. The typical workflow:

1. **Structure determination software generates mmCIF**: PHENIX, CCP4, RELION, cryoSPARC, etc. output refined coordinates
2. **OneDep web portal**: Researchers upload files and complete metadata via web forms
3. **Validation and review**: wwPDB staff validate and may request corrections
4. **Release**: Structure becomes publicly available

### OneDep Deposition System

The wwPDB provides [OneDep](https://deposit.wwpdb.org) - the unified deposition portal where researchers:

- Upload coordinate files (mmCIF format)
- Upload experimental data (structure factors, EM maps)
- Fill in metadata through web forms
- Answer questions about sample, methods, funding, authors

OneDep validates everything and helps fix errors interactively. Most experimental metadata is extracted from the coordinate file - OneDep asks researchers to confirm and supplement.

### The Metadata Gap

The disconnect in current practice:

1. Beamline software records data collection parameters
2. Processing software tracks refinement statistics
3. Lab notebooks contain sample preparation details
4. **None of these systems communicate automatically**

Researchers manually transcribe from multiple sources into OneDep forms - an error-prone and tedious process. This is exactly the gap lambda-ber-schema aims to fill.

## Legacy PDB Format vs mmCIF

The PDB historically used a fixed-column text format with specific record types. While mmCIF is now the primary format, many facilities and researchers still reference the legacy record names.

### Legacy PDB Records to mmCIF Mapping

| PDB Record | Contents | mmCIF Equivalent |
|------------|----------|------------------|
| `HEADER` | Classification, date, PDB ID | `_entry`, `_struct_keywords` |
| `TITLE` | Structure title | `_struct.title` |
| `COMPND` | Molecule names, chains | `_entity.pdbx_description` |
| `SOURCE` | Organism, expression system | `_entity_src_gen`, `_entity_src_nat` |
| `KEYWDS` | Search keywords | `_struct_keywords.text` |
| `EXPDTA` | Experimental method | `_exptl.method` |
| `AUTHOR` | Depositor names | `_audit_author` |
| `REVDAT` | Revision history | `_pdbx_audit_revision_history` |
| `JRNL` | Publication citation | `_citation` |
| `REMARK 200` | Crystallographic data collection | `_diffrn`, `_reflns` |
| `REMARK 280` | Crystal/crystallization conditions | `_exptl_crystal_grow` |
| `REMARK 350` | Biological assembly | `_pdbx_struct_assembly` |
| `REMARK 465` | Missing residues | `_pdbx_unobs_or_zero_occ_residues` |
| `CRYST1` | Unit cell, space group | `_cell`, `_symmetry` |
| `ORIGX1/2/3` | Original coordinate transforms | `_database_PDB_matrix` |
| `SCALE1/2/3` | Fractional coordinate transforms | `_atom_sites.fract_transf_*` |

### REMARK 200: Data Collection Details

REMARK 200 is particularly important as it contains extensive data collection metadata:

- Wavelength
- Temperature
- Detector type and distance
- Resolution limits
- Beamline/source information
- Data collection date

This maps to lambda-ber-schema's `ExperimentRun` class and the X-ray specific fields.

## Facility Metadata Requirements

Different synchrotron facilities track similar metadata for PDB deposition. A typical checklist includes:

| Category | Property | Notes |
|----------|----------|-------|
| PDB_Headers | HEADER | Entry classification |
| PDB_Headers | TITLE | Structure title |
| PDB_Headers | COMPND | Compound description |
| PDB_Headers | SOURCE | Biological source |
| PDB_Headers | KEYWDS | Keywords |
| PDB_Headers | EXPDTA | Experimental method |
| PDB_Headers | AUTHOR | Author list |
| PDB_Headers | REVDAT | Revision dates |
| PDB_Headers | JRNL | Journal reference |
| PDB_Headers | REMARK_200 | Data collection parameters |
| PDB_Headers | REMARK_280 | Crystallization conditions |
| PDB_Headers | REMARK_350 | Biological assembly |
| PDB_Headers | REMARK_465 | Missing residues |
| PDB_Headers | CRYST1 | Unit cell parameters |
| PDB_Headers | ORIGX1/2/3 | Origin transforms |
| PDB_Headers | SCALE1/2/3 | Scale transforms |

## PDB Headers to Schema Mapping

The following table shows how each PDB header record maps to specific classes and slots in lambda-ber-schema.

### HEADER - Entry Information

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Classification | `Dataset` | `keywords` | Entry classification terms |
| Deposition date | `WorkflowRun` | `deposited_to_pdb`, `end_date` | Tracked as workflow completion |
| PDB ID | `WorkflowRun` | `pdb_id` | Assigned accession code |

### TITLE - Structure Title

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Title | `Study` | `title`, `description` | Human-readable structure title |

### COMPND - Compound/Molecule

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Molecule name | `Sample` | `protein_name` | Protein/molecule name |
| Chain IDs | `Sample` | `molecular_composition` | Chain assignments |
| EC number | `Sample` | (via ontology terms) | Enzyme classification |
| Engineered | `Sample` | `construct`, `tag`, `mutations` | Construct details |

### SOURCE - Biological Source

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Organism scientific | `Sample` | `organism` | Source organism (OntologyTerm) |
| Organism taxid | `Sample` | `ncbi_taxid` | NCBI taxonomy ID |
| Expression system | `Sample` | `expression_system` | Recombinant expression host |
| Expression system taxid | `SamplePreparation` | `expression_system` | Host organism details |
| Gene | `Sample` | `gene_synthesis_vendor`, `codon_optimization_organism` | Gene information |
| Strain | `SamplePreparation` | `cell_line` | Strain/cell line used |

### KEYWDS - Keywords

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Keywords | `Dataset` | `keywords` | Searchable terms (multivalued) |

### EXPDTA - Experimental Method

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Method | `ExperimentRun` | `technique` | TechniqueEnum value |

### AUTHOR - Depositor Information

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Authors | `Study` | `contributors` | Author list |

### JRNL - Citation

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Citation | `Study` | `references` | Publication references |

### REMARK 200 - Data Collection

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Wavelength | `ExperimentRun` | `wavelength` | X-ray wavelength in Å |
| Temperature | `ExperimentRun` | `temperature_k` | Data collection temperature |
| Detector type | `XRayInstrument` | `detector_technology` | DetectorTechnologyEnum |
| Detector manufacturer | `XRayInstrument` | `detector_manufacturer` | e.g., Dectris, Rayonix |
| Detector model | `XRayInstrument` | `detector_model` | e.g., EIGER2 X 16M |
| Detector distance | `ExperimentRun` | `detector_distance` | Sample-detector distance (mm) |
| Beam center X/Y | `ExperimentRun` | `beam_center_x`, `beam_center_y` | Beam position on detector |
| Oscillation range | `ExperimentRun` | `oscillation_angle` | Rotation per image |
| Number of images | `ExperimentRun` | `number_of_images` | Total frames collected |
| Synchrotron | `XRayInstrument` | `facility_id` | FacilityEnum value |
| Beamline | `ExperimentRun` | `beamline` | Beamline identifier |
| Resolution range | `WorkflowRun` | `resolution_high`, `resolution_low` | Resolution limits |
| Completeness | `WorkflowRun` | `completeness_percent` | Data completeness |
| Rmerge | `WorkflowRun` | `rmerge` | Merging R-factor |
| I/sigmaI | `WorkflowRun` | `i_over_sigma` | Signal-to-noise ratio |
| Redundancy | `WorkflowRun` | `multiplicity` | Data redundancy |

### REMARK 280 - Crystallization

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Crystallization method | `CrystallizationConditions` | `method` | Vapor diffusion, batch, etc. |
| pH | `CrystallizationConditions` | `ph` | Crystallization pH |
| Temperature | `CrystallizationConditions` | `temperature_celsius` | Growth temperature |
| Precipitant | `CrystallizationConditions` | `precipitant_type`, `precipitant_concentration` | Main precipitant |
| Buffer | `CrystallizationConditions` | `buffer`, `buffer_concentration` | Buffer system |
| Salt | `CrystallizationConditions` | `salt`, `salt_concentration` | Added salts |
| Additives | `CrystallizationConditions` | `additives` | Other components |

### REMARK 350 - Biological Assembly

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Biological unit | `Sample` | `oligomeric_state` | Assembly state |
| Symmetry operators | - | Not directly modeled | Assembly transforms |

### CRYST1 - Unit Cell

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| a, b, c | `WorkflowRun` | `unit_cell_a`, `unit_cell_b`, `unit_cell_c` | Cell dimensions (Å) |
| alpha, beta, gamma | `WorkflowRun` | `unit_cell_alpha`, `unit_cell_beta`, `unit_cell_gamma` | Cell angles (°) |
| Space group | `WorkflowRun` | `space_group` | Hermann-Mauguin symbol |
| Z value | - | Not directly modeled | Molecules per unit cell |

### ORIGX / SCALE - Coordinate Transforms

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Transform matrices | - | Not modeled | Coordinate transformations stored in coordinate files |

### Refinement Statistics (REMARK 3)

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| R-work | `WorkflowRun` | `rwork` | Working set R-factor |
| R-free | `WorkflowRun` | `rfree` | Free set R-factor |
| RMSD bonds | `WorkflowRun` | `rmsd_bonds` | Bond length deviation |
| RMSD angles | `WorkflowRun` | `rmsd_angles` | Bond angle deviation |
| Ramachandran favored | `WorkflowRun` | `ramachandran_favored` | % in favored regions |
| Ramachandran outliers | `WorkflowRun` | `ramachandran_outliers` | % outliers |
| Clashscore | `WorkflowRun` | `clashscore` | MolProbity clashscore |
| Wilson B | `WorkflowRun` | `wilson_b_factor` | Wilson B-factor estimate |

### Phasing Information

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Phasing method | `WorkflowRun` | `phasing_method` | PhasingMethodEnum (SAD, MAD, MR, etc.) |
| Search model | `WorkflowRun` | `search_model_pdb_id` | MR template PDB ID |

### Deposition Status

| PDB Field | Schema Class | Schema Slot(s) | Notes |
|-----------|--------------|----------------|-------|
| Deposited | `WorkflowRun` | `deposited_to_pdb` | Boolean flag |
| PDB ID | `WorkflowRun` | `pdb_id` | Assigned accession |
| Validation report | `WorkflowRun` | `validation_report_path` | Path to validation PDF |

## Coverage Summary

The schema provides structured capture for the majority of PDB deposition metadata:

| PDB Section | Coverage | Notes |
|-------------|----------|-------|
| HEADER/TITLE/KEYWDS | ✅ Full | Dataset and Study metadata |
| COMPND/SOURCE | ✅ Full | Sample class with NSLS2 extensions |
| EXPDTA/AUTHOR | ✅ Full | ExperimentRun and Study |
| REMARK 200 (data collection) | ✅ Full | ExperimentRun + XRayInstrument |
| REMARK 280 (crystallization) | ✅ Full | CrystallizationConditions class |
| REMARK 3 (refinement) | ✅ Full | WorkflowRun refinement slots |
| CRYST1 (unit cell) | ✅ Full | WorkflowRun crystallographic slots |
| REMARK 350 (assembly) | ⚠️ Partial | oligomeric_state only |
| ORIGX/SCALE (transforms) | ❌ None | Stored in coordinate files |
| ATOM/HETATM (coordinates) | ❌ None | Schema tracks files, not coordinates |

## Integration Strategy

### Pre-Deposition: Use lambda-ber-schema

1. Capture sample metadata at preparation time
2. Record instrument and experimental parameters automatically from beamline
3. Track processing workflows with software versions and parameters
4. Maintain complete provenance from sample to structure

### Deposition: Export to OneDep

1. Generate metadata summary from lambda-ber-schema records
2. Use as reference when completing OneDep forms
3. Future: automated export to OneDep-compatible format

### Post-Deposition: Link Records

1. Update `WorkflowRun.pdb_id` with assigned accession
2. Set `WorkflowRun.deposited_to_pdb = true`
3. Maintain bidirectional links between local records and PDB entry

## OneDep Validation Categories

OneDep performs extensive validation before accepting a deposition. Understanding these checks helps ensure lambda-ber-schema captures the right metadata.

### Geometry Validation
| Check | What It Validates | Schema Support |
|-------|-------------------|----------------|
| Bond lengths | Deviations from ideal geometry | `WorkflowRun.rmsd_bonds` |
| Bond angles | Deviations from ideal angles | `WorkflowRun.rmsd_angles` |
| Ramachandran | Backbone dihedral angles | `WorkflowRun.ramachandran_favored`, `ramachandran_outliers` |
| Rotamers | Side chain conformations | (in coordinate file) |
| Clashes | Steric overlaps | `WorkflowRun.clashscore` |

### Data Quality Validation
| Check | What It Validates | Schema Support |
|-------|-------------------|----------------|
| Resolution | Claimed vs actual resolution | `WorkflowRun.resolution_high` |
| Completeness | Data completeness | `WorkflowRun.completeness_percent` |
| R-factors | Rwork/Rfree gap | `WorkflowRun.rwork`, `rfree` |
| B-factors | Temperature factor distribution | `WorkflowRun.wilson_b_factor` |

### Metadata Validation
| Check | What It Validates | Schema Support |
|-------|-------------------|----------------|
| Sequence match | Coordinates match deposited sequence | `Sample.molecular_composition` |
| Ligand identity | Chemical component dictionary match | `Sample` ligand fields |
| Source organism | Taxonomy ID validity | `Sample.ncbi_taxid`, `organism` |
| Expression system | Host organism consistency | `Sample.expression_system` |

## Common Deposition Issues

These are frequent problems researchers encounter during deposition, and how lambda-ber-schema helps prevent them:

### 1. Missing or Inconsistent Metadata
**Problem**: Data collection parameters don't match between coordinate file and deposition form.

**Schema Solution**: Single source of truth in `ExperimentRun`:
```yaml
ExperimentRun:
  wavelength: 0.9792        # Captured at beamline
  temperature_k: 100        # Recorded automatically
  detector_distance: 250.0  # From beamline metadata
  beamline: "FMX"           # Facility identifier
```

### 2. Lost Sample Provenance
**Problem**: Can't remember expression system or crystallization conditions months after data collection.

**Schema Solution**: Captured at preparation time in `Sample` and `CrystallizationConditions`:
```yaml
Sample:
  protein_name: "Lysozyme"
  organism: NCBITaxon:9031  # Gallus gallus
  expression_system: "E. coli BL21(DE3)"

CrystallizationConditions:
  method: "vapor_diffusion_hanging_drop"
  precipitant_type: "NaCl"
  precipitant_concentration: "1.0 M"
  ph: 4.5
```

### 3. Processing Statistics Mismatch
**Problem**: Reported statistics come from different processing runs.

**Schema Solution**: `WorkflowRun` links statistics to specific processing:
```yaml
WorkflowRun:
  workflow_code: "lysozyme-processing-v2"
  software_name: "XDS"
  software_version: "March 2024"
  resolution_high: 1.64
  rmerge: 0.082
  completeness_percent: 99.8
  # All stats from same processing run
```

### 4. Incorrect Phasing Attribution
**Problem**: Phasing method or search model not properly documented.

**Schema Solution**: Explicit phasing tracking:
```yaml
WorkflowRun:
  phasing_method: sad  # PhasingMethodEnum
  # or for molecular replacement:
  phasing_method: molecular_replacement
  search_model_pdb_id: "1LYZ"
```

## Example: Schema to OneDep Export

Conceptual example of generating OneDep-ready metadata from lambda-ber-schema:

```python
def generate_onedep_metadata(study: Study) -> dict:
    """Extract OneDep form data from lambda-ber-schema Study."""

    sample = study.samples[0]
    experiment = study.experiment_runs[0]
    workflow = study.workflow_runs[0]
    instrument = get_instrument(experiment.instrument_id)

    return {
        # TITLE
        "structure_title": study.title,

        # SOURCE
        "source_organism": sample.organism,
        "source_taxid": sample.ncbi_taxid,
        "expression_system": sample.expression_system,

        # COMPND
        "molecule_name": sample.protein_name,

        # REMARK 200 - Data Collection
        "wavelength": experiment.wavelength,
        "temperature": experiment.temperature_k,
        "detector": instrument.detector_model,
        "beamline": experiment.beamline,
        "synchrotron": instrument.facility_id,

        # CRYST1
        "space_group": workflow.space_group,
        "unit_cell": {
            "a": workflow.unit_cell_a,
            "b": workflow.unit_cell_b,
            "c": workflow.unit_cell_c,
            "alpha": workflow.unit_cell_alpha,
            "beta": workflow.unit_cell_beta,
            "gamma": workflow.unit_cell_gamma,
        },

        # Data quality
        "resolution": workflow.resolution_high,
        "rmerge": workflow.rmerge,
        "completeness": workflow.completeness_percent,

        # Refinement
        "rwork": workflow.rwork,
        "rfree": workflow.rfree,

        # Phasing
        "phasing_method": workflow.phasing_method,
        "search_model": workflow.search_model_pdb_id,
    }
```

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        STRUCTURE DETERMINATION WORKFLOW                      │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   SAMPLE    │───▶│   DATA      │───▶│ PROCESSING  │───▶│ REFINEMENT  │
│ PREPARATION │    │ COLLECTION  │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │                  │
      ▼                  ▼                  ▼                  ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Sample    │    │ Experiment  │    │ WorkflowRun │    │ WorkflowRun │
│   + Cryst   │    │    Run      │    │ (indexing)  │    │(refinement) │
│ Conditions  │    │             │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │                  │
      │                  │                  │                  │
      └──────────────────┴──────────────────┴──────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │    lambda-ber-schema         │
                    │    (unified metadata)        │
                    └──────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
         ┌─────────────────┐           ┌─────────────────┐
         │  OneDep Forms   │           │  Local Archive  │
         │  (deposition)   │           │  (provenance)   │
         └─────────────────┘           └─────────────────┘
                    │
                    ▼
         ┌─────────────────┐
         │      PDB        │
         │   (public)      │
         └─────────────────┘
```

## Related Standards

| Standard | Scope | Relationship to Schema |
|----------|-------|------------------------|
| **mmCIF/PDBx** | Atomic coordinates, structure metadata | Schema maps to mmCIF categories via `exact_mappings` |
| **IHMCIF** | Integrative/hybrid methods | Future alignment for multi-technique studies |
| **SIFTS** | Sequence-structure mapping | `Sample.molecular_composition` alignment |
| **UniProt** | Protein sequences | `Sample` protein identifiers |
| **NCBI Taxonomy** | Organism classification | `Sample.organism`, `ncbi_taxid` |

## References

- [wwPDB OneDep](https://deposit.wwpdb.org) - Unified deposition portal
- [mmCIF Dictionary](https://mmcif.wwpdb.org/) - Official mmCIF/PDBx dictionary
- [PDB File Format](https://www.wwpdb.org/documentation/file-format) - Legacy format documentation
- [PDB Validation](https://validate.wwpdb.org/) - Standalone validation server
- [wwPDB Validation Reports](https://www.wwpdb.org/validation/validation-reports) - Understanding validation output
- [PDB Data Harvesting](https://www.wwpdb.org/deposition/data-harvesting) - Automatic metadata extraction
