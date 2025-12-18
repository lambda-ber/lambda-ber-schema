# VIPS: Volumetric Imaging via Photochemical Sectioning

## Source

- Article: [Berkeley Lab Biosciences - VIPs Pass: New Imaging Method Offers Unprecedented Access](https://biosciences.lbl.gov/2025/12/11/vips-pass-new-imaging-method-offers-unprecedented-access/)
- Date: December 2025

## What VIPS Is

VIPS (Volumetric Imaging via Photochemical Sectioning) is an innovative light microscopy technique developed at Berkeley Lab that enables nanoscale visualization deep within intact tissue specimens.

### Key Features

- **Light sheet microscopy** with photochemical tissue dissolution
- Uses a sheet of light to trigger chemical reactions that dissolve precise tissue layers sequentially
- Dissolved material diffuses away, exposing fresh surfaces for imaging
- Automated, layer-by-layer process builds complete 3D datasets
- Enables nanoscale 3D imaging of **intact tissues** (whole organs, brain structures)
- No mechanical slicing required

### Data Scale

- A complete mouse brain generates **petabytes** of information
- Requires distributed computing (uses NERSC)
- Team developed **PetaKit5D** open-source software for efficient processing

### Applications

- Mapping brain connectome
- Comparing healthy vs neurodegenerative tissue
- Analyzing complex organ systems
- Any intact tissue/organ imaging at cellular precision

## Relationship to lambda-ber-schema

### Current Scope

lambda-ber-schema focuses on molecular/atomic resolution structural biology:
- Cryo-EM
- X-ray crystallography
- SAXS/WAXS
- SANS

### How VIPS Differs

| Aspect | lambda-ber-schema | VIPS |
|--------|-------------------|------|
| Scale | Molecular/atomic (Angstrom) | Tissue/cellular (nanoscale) |
| Techniques | Synchrotron, electron microscopy | Light microscopy |
| Subjects | Proteins, complexes | Organs, tissues |
| Data size | GB-TB per dataset | Petabytes per brain |

## Potential Integration Scenarios

### 1. Correlative/Integrative Studies

Multi-scale imaging pipelines where:
- VIPS provides tissue/organ context
- Cryo-EM or X-ray provides molecular detail

The schema already supports integrative studies (see `Study-integrative.yaml`).

### 2. Shared Infrastructure

Similar data management challenges:
- Large file handling with checksums
- Complex processing workflows
- HPC/distributed computing
- FAIR metadata requirements

Existing classes that could apply:
- `DataFile` - file metadata, checksums
- `WorkflowRun` - computational processing pipelines
- `Sample` - biological specimen metadata

### 3. BER Umbrella Schema

If BER wants a unified biological imaging metadata model, could extend with:
- `LightMicroscopyInstrument` class
- `light_microscopy` or `vips` in `TechniqueEnum`
- Tissue preparation classes (fixation, staining protocols)

### 4. Separate but Related Schema

VIPS might warrant its own schema with:
- Shared imports for common patterns (files, workflows)
- Domain-specific classes for tissue imaging
- Different validation requirements

## Recommendation

**Current assessment**: Out of scope for core lambda-ber-schema

The schema is focused on structural biology at synchrotrons/cryo-EM facilities. VIPS is a different domain (tissue/organ imaging) even though it's from the same institution (Berkeley Lab).

**However**, worth discussing with BER team if they want to:
1. Expand scope to broader "biological imaging"
2. Create a family of related schemas
3. Share common data management patterns

## Next Steps (if pursued)

1. Survey what metadata VIPS generates (PetaKit5D outputs?)
2. Identify overlap with existing schema patterns
3. Discuss with BER stakeholders about scope expansion
4. Consider modular schema architecture for multi-domain support

## Related Links

- PetaKit5D: (need to find repository link)
- NERSC: https://www.nersc.gov/
