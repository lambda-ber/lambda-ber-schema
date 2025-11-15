---
marp: true
theme: default
paginate: true
---

# Ontologies for Structural Biology Imaging

A Survey of Relevant Ontologies and Their Coverage for lambda-ber-schema

---

## Overview

This presentation surveys ontologies relevant to structural biology and bioimaging:

1. **CHMO** - Chemical Methods Ontology
2. **FBbi** - Biological Imaging Methods Ontology
3. **OBI** - Ontology for Biomedical Investigations
4. **ROR** - Research Organization Registry
5. Coverage comparison and recommendations

---

## CHMO: Chemical Methods Ontology

**Focus**: Analytical chemistry and experimental methods

**Scope**:
- Chemical analysis techniques
- Sample preparation methods
- Instrumentation
- Data collection methods

**Maintainer**: Royal Society of Chemistry (RSC)
**Status**: Active (OBO Foundry)

---

## CHMO: Structural Biology Coverage

**Excellent coverage** for core techniques:

| Technique | CHMO ID | Term |
|-----------|---------|------|
| Cryo-EM | CHMO:0002413 | cryogenic electron microscopy |
| X-ray crystallography | CHMO:0000156 | X-ray diffraction |
| SAXS | CHMO:0000204 | small-angle X-ray scattering |
| WAXS | CHMO:0000207 | wide-angle X-ray scattering |
| SANS | CHMO:0000184 | small-angle neutron scattering |
| Electron microscopy | CHMO:0000068 | electron microscopy |
| Mass spectrometry | CHMO:0000470 | mass spectrometry |

---

## CHMO: Use in lambda-ber-schema

**Currently implemented** for TechniqueEnum and ExperimentalMethodEnum:

```yaml
TechniqueEnum:
  cryo_em:
    description: "Cryo-electron microscopy"
    meaning: CHMO:0002413
  xray_crystallography:
    description: "X-ray crystallography"
    meaning: CHMO:0000156
  saxs:
    description: "Small-angle X-ray scattering"
    meaning: CHMO:0000204
```

✅ **Best choice for analytical techniques**

---

## FBbi: Biological Imaging Methods Ontology

**Focus**: Microscopy and biological imaging workflows

**Scope**: Multi-dimensional imaging metadata covering:
- Sample preparation
- Visualization methods (probes, dyes, FPs)
- Illumination methods
- Detection methods
- Imaged parameters
- Resolution enhancement

**Maintainer**: Originally FlyBase, now community
**Status**: Inactive (last update 2020)

---

## FBbi: 9 Primary Axes

1. **Sample Preparation** - fixation, embedding, sectioning
2. **Visualization Method** - fluorescent proteins, dyes, stains
3. **Imaging Method** - microscopy types
4. **Illumination Method** - photons, electrons, X-rays
5. **Detection Method** - CCD, CMOS, PMT, film
6. **Imaged Parameter** - fluorescence, scattering, absorption
7. **Contrast Enhancement** - methods to improve contrast
8. **Resolution Enhancement** - super-resolution techniques
9. **Source of Contrast** - what creates image contrast

---

## FBbi: Sample Preparation Coverage

**Comprehensive fixation methods**:
- Chemical: formaldehyde, glutaraldehyde, osmium tetroxide
- Cryofixation: FBbi:00000013
- Freeze-substitution: FBbi:00000621

**Embedding**:
- Vitreous ice: FBbi:00000089
- Epoxy resin, wax, paraffin

**Sectioning**:
- Microtome, cryostat, vibratome

**State**: living, fixed, permeabilized

---

## FBbi: Visualization Methods

**Extensive probe coverage**:
- **100+ fluorescent proteins**: GFP variants, RFP, mCherry, tdTomato
- **Chemical dyes**: DAPI, propidium iodide, Alexa Fluors
- **Lipid probes**: DiI, DiA
- **Nucleic acid probes**
- **Electron-dense stains**
- **Radioisotopes**

**Most comprehensive for microscopy probes**

---

## FBbi: Imaging Methods

**Microscopy types**:
- Electron microscopy: FBbi:00000256
  - TEM: FBbi:00000258
  - Scanning-transmission EM: FBbi:00000380
  - High-voltage EM: FBbi:00000622
- Light microscopy: FBbi:00000345
  - Confocal: FBbi:00000251
  - Two-photon: FBbi:00000254
  - Fluorescence: FBbi:00000246
- X-ray microscopy: FBbi:00000260

---

## FBbi: Illumination & Detection

**Illumination sources**:
- Photons: UV/visible/IR (FBbi:00000341)
- Electrons: FBbi:00000273
- X-rays: FBbi:00000342
- Neutrons: FBbi:00000275
- Ions: FBbi:00000276

**Detection methods**:
- CCD, EMCCD, CMOS: FBbi:00000294, 00000301, 00000304
- PMT: FBbi:00000295
- Film: FBbi:00000303
- X-ray photon detection: FBbi:00000379

---

## FBbi: Gaps for Structural Biology

**Missing or limited**:
- ❌ No specific cryo-EM term (only general EM)
- ❌ No X-ray crystallography
- ❌ No SAXS/SANS terms
- ❌ No synchrotron-specific terms
- ❌ Limited scattering terminology

**Best for**: Cellular/subcellular microscopy workflows
**Less suitable for**: Molecular structure determination

---

## OBI: Ontology for Biomedical Investigations

**Focus**: Entire investigation lifecycle

**Scope**:
- Planning and design
- Execution (assays, protocols)
- Materials and reagents
- Instruments and devices
- Data generation and analysis
- Roles and participants

**Maintainer**: OBI Consortium
**Status**: Active (OBO Foundry), 2500+ terms

---

## OBI: Core Structure

**Top-level concepts**:
- **Assay** (OBI:0000070) - experimental procedures
- **Protocol** (OBI:0000272) - planned processes
- **Device** (OBI:0000968) - instruments
- **Material entity** - samples, reagents
- **Data item** - results, measurements
- **Study design** - experimental planning
- **Role** - investigator, manufacturer

**Integration philosophy**: Reuses existing ontologies via MIREOT

---

## OBI: Structural Biology Assays

**3D Structure Determination**:
- X-ray crystallography: OBI:0000912
- Electron microscopy: OBI:0003118
- NMR: OBI:0000182
- Small-angle scattering: OBI:0002108

**Imaging assays**:
- Microscopy assay: OBI:0002119
- Electron microscopy imaging: OBI:0001631
- Widefield microscopy: OBI:0002437
- Lightsheet fluorescence: OBI:0003098

---

## OBI: Specialized Assays

**X-ray crystallography variants**:
- MHC:ligand complex: OBI:0001595
- T cell epitope:MHC:TCR: OBI:0001311
- B cell epitope:antibody: OBI:0001738

**Electron microscopy variants**:
- B cell epitope:antibody: OBI:0001646
- T cell epitope:MHC:TCR: OBI:0003612
- MHC:ligand complex: OBI:0003613

**Focus on immunology applications**

---

## OBI: Devices & Instruments

**Device hierarchy**:
- Measurement device: OBI:0000832
- Image creation device: OBI:0000398
- Material separation device: OBI:0000932
- Environmental control: OBI:0001034
- Cryofixation device: OBI:0001074

**More abstract than equipment catalogs**
**Good for describing roles, not specific models**

---

## OBI: Sample Preparation

**Integration approach**:
- OBI references sample prep terms
- Imports from CHMO for chemical methods
- Imports from other ontologies via MIREOT

**Example**:
- Sample preparation for assay: OBI:0000073
- Specimen collection protocol: OBI:0003070

**Coordinates rather than duplicates**

---

## ROR: Research Organization Registry

**Focus**: Persistent organizational identifiers

**Scope**:
- Research institutions
- Funding organizations
- Facilities
- Universities and labs

**Maintainer**: Community initiative
**Status**: Active, constantly updated

---

## ROR: Use in lambda-ber-schema

**FacilityEnum with ROR mappings**:

```yaml
NSLS_II:
  title: "National Synchrotron Light Source II"
  meaning: ROR:01q47ea17
  annotations:
    parent_ror: "ROR:02ex6cf31"  # Brookhaven
    country: "USA"
    doe_facility: "true"

ESRF:
  title: "European Synchrotron Radiation Facility"
  meaning: ROR:02550n020
  annotations:
    country: "France"
```

---

## ROR: Benefits

✅ **Persistent identifiers** for facilities
✅ **Global coverage** of research organizations
✅ **Hierarchical relationships** (facility → parent lab)
✅ **Regular updates** with new facilities
✅ **API access** for programmatic lookup
✅ **Cross-referencing** with Wikidata, GRID, ISNI

**Ideal for facility/organization identification**

---

## Coverage Comparison Matrix

| Domain | CHMO | FBbi | OBI | ROR |
|--------|------|------|-----|-----|
| Analytical techniques | ★★★ | ★ | ★★ | - |
| Microscopy methods | ★ | ★★★ | ★★ | - |
| Sample preparation | ★★ | ★★★ | ★ | - |
| Instruments/devices | ★ | ★ | ★★ | - |
| Facilities | - | - | - | ★★★ |
| Probes/dyes | - | ★★★ | ★ | - |
| Assay types | ★ | ★ | ★★★ | - |
| Investigation lifecycle | - | - | ★★★ | - |

★★★ = Excellent, ★★ = Good, ★ = Limited, - = Not covered

---

## Strengths by Ontology

**CHMO**:
- ✅ Core structural biology techniques
- ✅ Analytical chemistry methods
- ✅ Simple, focused scope

**FBbi**:
- ✅ Multi-dimensional microscopy metadata
- ✅ Comprehensive probe coverage
- ✅ Sample preparation detail

**OBI**:
- ✅ Investigation context
- ✅ Assay classification
- ✅ Experimental design

**ROR**:
- ✅ Facility identification
- ✅ Institutional metadata

---

## Gaps & Limitations

**CHMO**:
- ❌ Limited microscopy detail
- ❌ No facility information

**FBbi**:
- ⚠️ Inactive (no updates since 2020)
- ❌ Missing cryo-EM, SAXS, crystallography
- ❌ No synchrotron terms

**OBI**:
- ❌ Abstract device terms
- ❌ Limited technique detail
- ⚠️ Complexity overhead

**ROR**:
- ⚠️ Organizations only, not techniques

---

## Current Usage in lambda-ber-schema

**Implemented**:
- ✅ **CHMO** for TechniqueEnum (8 techniques)
- ✅ **CHMO** for ExperimentalMethodEnum
- ✅ **ROR** for FacilityEnum (12 facilities)
- ✅ **Wikidata** for supplementary facility metadata

**Not yet implemented**:
- ⏸️ FBbi for detailed microscopy workflows
- ⏸️ OBI for assay/protocol classification

---

## Recommendations

**For structural biology techniques**:
→ **CHMO** (already implemented) ✅

**For facility identification**:
→ **ROR** (already implemented) ✅

**For detailed microscopy workflows**:
→ Consider **FBbi** if needed

**For investigation context**:
→ Consider **OBI** for assay classification

**For sample types**:
→ Consider **NCBITaxon**, **CL** (Cell Ontology)

---

## Future Enhancements

**Potential additions**:

1. **FBbi mappings** for microscopy-specific enums
   - GridTypeEnum → FBbi grid types
   - VitrificationMethodEnum → FBbi fixation methods

2. **OBI mappings** for workflow/assay types
   - WorkflowTypeEnum → OBI assay terms

3. **NCBITaxon** for expression systems
   - ExpressionSystemEnum → taxonomy IDs

4. **Additional ontologies** for specialized domains

---

## Integration Strategy

**Multi-ontology approach**:

```yaml
cryo_em:
  description: "Cryo-electron microscopy"
  meaning: CHMO:0002413              # Primary: technique
  exact_mappings:
    - OBI:0003118                     # Assay context
    - FBbi:00000256                   # EM method (general)
  annotations:
    typical_facilities:
      - ROR:02jbv0t02                 # Berkeley Lab (ALS)
      - ROR:02ex6cf31                 # Brookhaven (NSLS-II)
```

**Benefits**: Rich semantic connections across domains

---

## Best Practices

1. **Use `meaning:`** for primary ontology mapping
2. **Use `exact_mappings:`** for equivalent terms in other ontologies
3. **Use `broad_mappings:`** for hierarchical relationships
4. **Use `annotations:`** for domain-specific metadata
5. **Document** ontology sources in comments
6. **Validate** mappings using OAK or OLS
7. **Keep updated** with ontology releases

---

## Resources

**Ontology browsers**:
- OBO Foundry: http://obofoundry.org
- BioPortal: https://bioportal.bioontology.org
- OLS (EBI): https://www.ebi.ac.uk/ols4
- Ontobee: https://ontobee.org

**Tools**:
- OAK (Ontology Access Kit): https://github.com/INCATools/ontology-access-kit
- ROBOT: http://robot.obolibrary.org

**Registries**:
- ROR: https://ror.org

---

## Summary

**Key takeaways**:

1. **CHMO** provides excellent coverage for analytical techniques ✅
2. **FBbi** offers rich microscopy detail but is inactive ⚠️
3. **OBI** gives investigation context and assay classification 🔬
4. **ROR** enables persistent facility identification 🏢
5. **Multi-ontology approach** maximizes semantic richness 🌐

**Current implementation**: CHMO + ROR meets core needs

**Future**: Consider FBbi/OBI for specialized workflows

---

## Questions?

**Contact**:
- lambda-ber-schema repository: https://github.com/lambda-ber/lambda-ber-schema
- Issues: https://github.com/lambda-ber/lambda-ber-schema/issues

**Generated**: 2025-01-14
**Schema version**: Based on current main branch
