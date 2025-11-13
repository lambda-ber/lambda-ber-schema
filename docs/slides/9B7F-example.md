---
title: "S-SAD Structure of Lysozyme: NSLS2-BER-LAMBDA Integration"
subtitle: "PDB 9B7F - A Comprehensive Example"
author: "lambda-ber-schema"
date: "2024"
---

# Overview

## S-SAD Phasing of Hen Egg White Lysozyme

**PDB Entry**: 9B7F
**Resolution**: 1.64 Å
**Method**: Sulfur Single-Wavelength Anomalous Diffraction (S-SAD)
**Facility**: NSLS-II FMX Beamline, Brookhaven National Laboratory

**Key Innovation**: Lossless compression of diffraction data while preserving full structural information

**Reference**: Bernstein, H.J. & Jakoncic, J. (2024). *J. Synchrotron Rad.* **31**, 647-654.

---

# The Protein: Hen Egg White Lysozyme

## Why Lysozyme?

- **Most studied protein in crystallography**
  - First enzyme structure solved by X-ray crystallography (1965)
  - Standard test case for new methods
  - Well-characterized reference structure

- **Biological Function**: Hydrolase (EC 3.2.1.17)
  - Catalyzes hydrolysis of bacterial cell wall peptidoglycan
  - Antimicrobial enzyme found in egg white, tears, saliva
  - Also known as "Allergen Gal d IV"

- **Molecular Details**:
  - 129 amino acid residues
  - 14.3 kDa molecular weight
  - 8 methionine + 8 cysteine residues (native sulfur!)
  - Source: *Gallus gallus* (chicken)

---

# Why S-SAD Phasing?

## Traditional vs. Native Phasing

### Traditional Approach:
- Heavy atom derivatives (Se-Met, Hg, Pt)
- Requires special protein expression
- Multiple crystals often needed
- Time-consuming and expensive

### S-SAD Approach (This Structure):
- Uses **native sulfur** atoms (Met, Cys)
- No special preparation needed
- Single native crystal
- Faster and more economical

### Requirements for Success:
✅ High-flux synchrotron beamline (NSLS-II FMX)
✅ Wavelength selection (1.65 Å to maximize f'' from sulfur)
✅ High-quality detector (EIGER X 9M)
✅ Sufficient sulfur atoms (16 in asymmetric unit)

---

# Crystal Growth

## Crystallization Conditions

**Method**: Hanging Drop Vapor Diffusion

**Reservoir Solution**:
- 1000 mM NaCl
- 100 mM Sodium Acetate pH 4.6
- 50 mM Glycerol
- 50 mM Ethylene Glycol

**Drop**: 1 µL protein + 1 µL reservoir
**Temperature**: 298 K (25°C)

**Crystal Properties**:
- Space group: P 43 21 2 (tetragonal)
- Unit cell: a = b = 78.895 Å, c = 36.955 Å
- Matthews coefficient: 2.03 Å³/Da
- Solvent content: 40%
- Diffraction quality: Excellent to 1.64 Å

---

# Data Collection at NSLS-II FMX

## Beamline Specifications

**NSLS-II FMX** (Frontier Macromolecular Crystallography)
- Synchrotron radiation source
- Energy range: 5-20 keV
- High photon flux: 10¹² photons/s/mm²
- Microfocus capability: 1-100 µm beam

**Detector**: Dectris EIGER X 9M
- Hybrid photon counting detector
- 9 megapixel resolution
- Pixel size: 75 µm × 75 µm
- Fast readout, zero noise

---

# Data Collection Strategy

## Optimized for S-SAD

| Parameter | Value | Purpose |
|-----------|-------|---------|
| **Wavelength** | 1.65 Å | Maximize sulfur f'' signal |
| **Detector Distance** | 100 mm | High resolution to 1.64 Å |
| **Oscillation** | 0.4° per image | Fine slicing for completeness |
| **Total Rotation** | 360° | Full data redundancy |
| **Temperature** | 100 K | Cryogenic cooling |
| **Beam Size** | 10 µm | Match to crystal size |

**File Format**: CBF with lossless Zstandard compression
**Data Size**: ~2.5 MB per compressed image (vs ~8 MB uncompressed)

---

# The Innovation: Lossless Compression

## Data Compression Challenge

### The Problem:
- Modern detectors generate massive data volumes
- Standard crystallography: 900 images × 8 MB = **7.2 GB** per dataset
- Storage and transfer becomes bottleneck
- Long-term archiving expensive

### The Solution:
**Lossless compression** using Zstandard algorithm

- **Preserves every bit** of diffraction intensity
- **Reduces file size by 70%**: 8 MB → 2.5 MB per image
- **No information loss** for phasing or refinement
- **Fast compression/decompression**

### Key Finding:
**S-SAD phasing successful** with compressed data, proving that compression preserves all structural information!

---

# Data Processing Pipeline

## From Raw Images to Structure

```
1. Data Integration (XDS)
   ├─ Space group determination: P 43 21 2
   ├─ Unit cell refinement: 78.895 × 78.895 × 36.955 Å
   └─ Resolution limit: 1.64 Å

2. Scaling (AIMLESS)
   ├─ Rmerge: 6.3%
   ├─ CC½: 0.998 (excellent!)
   ├─ Completeness: 99.9%
   └─ I/σ(I): 13.1

3. S-SAD Phasing (SHELXDE)
   ├─ Locate 16 sulfur atoms (8 Met + 8 Cys)
   ├─ Calculate anomalous differences
   ├─ Determine experimental phases
   └─ Generate initial electron density map

4. Model Building & Refinement (REFMAC5)
   ├─ Automated building of 129 residues
   ├─ Add 119 water molecules
   ├─ Refine to Rwork = 15.9%, Rfree = 19.8%
   └─ Validate geometry (0 Ramachandran outliers!)
```

---

# Data Quality Metrics

## Exceptional Quality Throughout

### Data Collection
| Metric | Value | Interpretation |
|--------|-------|----------------|
| Resolution | 1.64 Å | Atomic detail |
| Completeness | 88.9% | Nearly complete |
| Multiplicity | ~7× | High redundancy |

### Data Processing
| Metric | Value | Quality |
|--------|-------|---------|
| Rmerge | 6.3% | Excellent |
| Rpim | 3.4% | Very good |
| CC½ | 0.998 | Outstanding correlation |
| I/σ(I) | 13.1 | Strong signal |

### Final Refinement
| Metric | Value | Assessment |
|--------|-------|------------|
| Rwork | 15.92% | Excellent fit |
| Rfree | 19.75% | Good validation |
| RMSD bonds | 0.012 Å | Ideal geometry |
| Ramachandran favored | 98.4% | Excellent |
| Ramachandran outliers | 0.0% | Perfect! |
| Clashscore | 3.2 | Very good |

---

# Final Structure

## Model Composition

**Protein**:
- 1 polypeptide chain (129 residues)
- 0 Ramachandran outliers
- Well-ordered throughout

**Ligands and Ions**:
- 4 ethylene glycol molecules
- 8 chloride ions
- 4 sodium ions

**Solvent**:
- 119 water molecules
- Well-defined hydrogen bonding network

**Total Atoms**: 1,089
**Average B-factor**: 28.5 Å²

---

# NSLS2-BER-LAMBDA Integration

## Complete Metadata Mapping

### What We Captured:

**Sample Level** (NSLS2 → lambda-ber-schema):
- ✅ Protein name, organism, EC number
- ✅ Molecular weight, concentration
- ✅ Buffer composition, storage conditions
- ✅ Construct details (full-length, no tags)

**Crystallization** (NSLS2 Crystallization):
- ✅ Method (hanging drop vapor diffusion)
- ✅ Conditions (salts, pH, additives)
- ✅ Temperature, drop volume
- ✅ Crystal size, Matthews coefficient

---

# NSLS2-BER-LAMBDA Integration (cont.)

## Comprehensive Data Collection Mapping

**Data Collection** (CBF headers → ExperimentRun):
- ✅ Wavelength: 1.65 Å
- ✅ Detector: EIGER X 9M
- ✅ Detector distance: 100 mm
- ✅ Beam center: (785.5, 783.4) pixels
- ✅ Pixel size: 75 × 75 µm
- ✅ Oscillation: 0.4° per frame
- ✅ Exposure time: 0.03 s
- ✅ Beamline: FMX

**Data Processing** (PDB mmCIF → WorkflowRun):
- ✅ Space group, unit cell parameters
- ✅ Resolution limits
- ✅ Quality metrics (Rmerge, CC½, I/σ, Wilson B)
- ✅ Completeness, multiplicity

**Refinement** (PDB → WorkflowRun):
- ✅ Rwork, Rfree
- ✅ RMSD bonds/angles
- ✅ Ramachandran statistics
- ✅ Clashscore, model composition

---

# lambda-ber-schema Benefits

## Why Use a Formal Schema?

### 1. **Semantic Consistency**
- Standardized field names across different sources
- `nsls2:Wavelength` maps to CBF `Wavelength` AND PDB `_diffrn_radiation_wavelength.wavelength`
- No ambiguity or data loss in translation

### 2. **Validation**
```bash
$ linkml-validate -s lambda-ber-schema.yaml dataset-9B7F.yaml
✓ No issues found
```
- Automatic checking of data types, ranges, required fields
- Ensures completeness and correctness

### 3. **Interoperability**
- Export to multiple formats: YAML, JSON, RDF, SQL
- Compatible with semantic web standards
- Integrates with knowledge graphs

---

# lambda-ber-schema Benefits (cont.)

## Complete Provenance Tracking

```yaml
workflow_runs:
  - workflow_code: "9B7F-SAD-PHASING-001"
    workflow_type: phasing
    software_name: "SHELXDE"
    software_version: "2018/3"
    phasing_method: sad
    experiment_id: "FMX-2023-11-HEWL-SAD"
    input_data: [integration-001, scaling-001]
    output_files: [phased-mtz, sulfur-sites]
    started_at: "2023-11-15T18:00:00"
    completed_at: "2023-11-15T19:30:00"
    compute_resources:
      cpu_hours: 1.5
      memory_gb: 16
```

**Every step documented**:
- What software (and version)?
- What parameters?
- When was it run?
- What resources were used?
- What were the inputs/outputs?

---

# Use Cases

## Who Benefits?

### 1. **Beamline Scientists**
- Automated metadata extraction from instruments
- Consistent data organization
- Easy handoff to users

### 2. **Structural Biologists**
- Complete experimental record
- Easy data sharing and collaboration
- Publication-ready metadata

### 3. **Database Curators**
- Standardized deposition format
- Rich semantic annotations
- Links to ontologies (UniProt, GO, PDB)

### 4. **Computational Scientists**
- Machine-readable data
- Training datasets for ML/AI
- Reproducible analysis pipelines

---

# Future Directions

## Expanding the Framework

### Immediate Extensions:
1. **Serial crystallography** (SSX, SFX)
   - Time-resolved data
   - Pump-probe experiments
   - XFEL integration

2. **Multi-technique integration**
   - Combine with cryo-EM data
   - SAXS/WAXS solution scattering
   - Complementary techniques

3. **Automated converters**
   - CBF/CIF → lambda-ber-schema
   - Excel templates → schema
   - API integration with beamlines

### Long-term Vision:
- **Unified structural biology database**
- **AI-ready training datasets**
- **Real-time data processing** at beamlines
- **Automated quality assessment**

---

# Technical Implementation

## From CBF to Schema

### Extraction Pipeline:

```python
from lambda_ber_schema import Dataset, ExperimentRun
from nsls2_lambda.metadata import parse_cbf, parse_cif

# Extract from CBF diffraction image
cbf_metadata = parse_cbf("lyso_7500eV.cbf.zst")

# Map to schema
experiment = ExperimentRun(
    experiment_code="FMX-2023-11-HEWL-SAD",
    technique="xray_crystallography",
    wavelength=cbf_metadata['Wavelength'],  # 1.65 Å
    beam_center_x=cbf_metadata['Beam_xy'][0],  # 785.5 px
    beam_center_y=cbf_metadata['Beam_xy'][1],  # 783.4 px
    detector_distance=cbf_metadata['Detector_distance'],  # 100 mm
    pixel_size_x=0.075,  # mm
    pixel_size_y=0.075,  # mm
    oscillation_angle=cbf_metadata['Angle_increment'],  # 0.4°
    start_angle=cbf_metadata['Start_angle'],  # 421°
)

# Validate
experiment.validate()
```

---

# Key Takeaways

## What We Learned from 9B7F

### Scientific Achievement:
✅ **S-SAD phasing works** with native sulfur (no heavy atoms needed)
✅ **Lossless compression preserves** all structural information
✅ **High-quality structure** (Rwork=15.9%, Rfree=19.8%, 0 outliers)

### Metadata Success:
✅ **Complete mapping** from raw data to PDB deposition
✅ **All 11 NSLS2 categories** represented in schema
✅ **Bidirectional compatibility** (CBF ↔ Schema ↔ PDB)
✅ **Validation successful** - schema is production-ready

### Broader Impact:
✅ **Template for future datasets** at NSLS-II and other facilities
✅ **Demonstrates FAIR principles** (Findable, Accessible, Interoperable, Reusable)
✅ **Enables AI/ML applications** through standardized metadata
✅ **Foundation for integrative structural biology**

---

# Resources

## Where to Learn More

### Code & Documentation:
- **lambda-ber-schema**: https://github.com/lambda-ber/lambda-ber-schema
- **NSLS2-BER-LAMBDA**: https://github.com/NSLS2/BER-LAMBDA
- **Schema Documentation**: https://w3id.org/lambda-ber-schema/

### Example Files:
- **9B7F Example**: `examples/Dataset-nsls2-9B7F.yaml`
- **Raw Data**: `tests/data/raw/9B7F.cif`
- **Integration Guide**: `docs/nsls2-integration.md`

### References:
- **PDB Entry 9B7F**: https://www.rcsb.org/structure/9B7F
- **Publication**: Bernstein & Jakoncic (2024) *J. Synchrotron Rad.* 31:647-654
  - DOI: 10.1107/S160057752400359X
  - PubMed: 38838167

### Contacts:
- **NSLS-II Beamline**: Jean Jakoncic (jjakoncic@bnl.gov)
- **NSLS2-BER-LAMBDA**: Shekar V (vshekar1@bnl.gov)

---

# Thank You!

## Questions?

**This presentation demonstrates:**
- Complete crystallographic workflow (crystallization → structure)
- S-SAD phasing with native sulfur atoms
- Lossless compression of diffraction data
- Comprehensive metadata integration (NSLS2 ↔ lambda-ber-schema)
- FAIR data principles in structural biology

**Next Steps:**
1. Explore the example: `examples/Dataset-nsls2-9B7F.yaml`
2. Read the integration guide: `docs/nsls2-integration.md`
3. Try the validation: `linkml-validate -s schema.yaml your-data.yaml`
4. Contribute to the schema: https://github.com/lambda-ber/lambda-ber-schema

---

**Appendix: Complete Workflow Summary**

```
Sample Preparation
├─ Hen egg white lysozyme (14.3 kDa, 129 residues)
├─ Crystallization (hanging drop, pH 4.6, 298 K)
└─ Crystals: P 43 21 2, 78.9 × 78.9 × 37.0 Å

Data Collection (NSLS-II FMX)
├─ EIGER X 9M detector
├─ 1.65 Å wavelength (optimized for sulfur)
├─ 900 images, 0.4° oscillation
├─ Lossless compression (70% size reduction)
└─ Resolution: 1.64 Å

Processing
├─ Integration (XDS): 99.9% complete, CC½=0.998
├─ Scaling (AIMLESS): Rmerge=6.3%, I/σ=13.1
├─ S-SAD Phasing (SHELXDE): 16 sulfur sites located
└─ Refinement (REFMAC5): Rwork=15.9%, Rfree=19.8%

Result
├─ High-quality structure (0 outliers)
├─ PDB deposition: 9B7F
├─ Publication: J. Synchrotron Rad. (2024)
└─ Complete metadata in lambda-ber-schema format
```
