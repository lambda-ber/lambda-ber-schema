# IR and FTIR Spectroscopy in lambda-ber-schema

## What is FTIR?

**FTIR (Fourier Transform Infrared) spectroscopy** uses infrared light to probe molecular vibrations. When IR light hits a sample, molecules absorb specific wavelengths corresponding to their chemical bonds (C=O, N-H, C-H, etc.), creating a unique "molecular fingerprint."

**Key Parameters** from the schema:
```yaml
FTIRImage:
  wavenumber_min: 800      # cm⁻¹ (far infrared)
  wavenumber_max: 4000     # cm⁻¹ (mid infrared)
  spectral_resolution: 4   # cm⁻¹
  number_of_scans: 32      # Signal averaging
  molecular_signatures:
    - "1650 cm⁻¹ - Amide I (C=O stretch)"    # Protein backbone
    - "1550 cm⁻¹ - Amide II (N-H bend)"      # Protein structure
    - "2920 cm⁻¹ - CH2 stretch (lipids)"     # Lipid membranes
    - "1740 cm⁻¹ - C=O stretch (ester lipids)"
    - "3300 cm⁻¹ - O-H stretch (water)"
```

## Critical Distinction: Lab-based vs Synchrotron FTIR

**FTIR is UNIQUE in this schema - it can be EITHER a general structural biology technique OR a light source technique:**

## 1. Lab-Based FTIR (NOT a Light Source Technique)

**Standard benchtop FTIR microscope:**
- IR source: Globar (silicon carbide heated rod) or tungsten lamp
- Brightness: ~1000x dimmer than synchrotron
- Spatial resolution: ~10-20 μm (diffraction limited)
- Application: General molecular composition mapping

```yaml
# General structural biology - benchtop instrument
FTIRImage:
  file_name: "sample_ftir_map_001.h5"
  pixel_size: 5.5          # micrometers (decent resolution)
  dimensions_x: 128
  dimensions_y: 128
  # No specific light source mentioned
```

**Categorization:** General imaging/structural biology
- Uses conventional IR source
- Similar to optical microscopy in terms of infrastructure
- Lab-accessible, no synchrotron required

## 2. Synchrotron FTIR (Light Source Technique)

**SR-FTIR at ALS beamline (BSISB facility):**
- IR source: **Synchrotron radiation** (bending magnet or edge radiation)
- Brightness: **~1000x brighter** than lab sources
- Beam size: 2-10 μm (standard) down to **20 nm (SINS mode)**
- Advanced capabilities:
  - Time-resolved dynamics (millisecond timescales)
  - 3D FTIR tomography
  - Nano-spectroscopy with AFM coupling

From the BER facilities document:

```yaml
# Light source technique - synchrotron beamline
FTIRImage:
  beamline_id: "ALS-5.4"  # or "ALS-1.4"
  spatial_resolution: 0.02   # micrometers = 20 nm (SINS mode!)
  wavenumber_min: 650
  wavenumber_max: 4000

  # Time-resolved capabilities (unique to synchrotron)
  acquisition_mode: "time_resolved"
  time_points: [0, 10, 20, 30, 60, 120]  # seconds

  # 3D tomography
  tomography_angles: 180
```

**Categorization:** Light source technique
- Uses synchrotron radiation (photons from relativistic electrons)
- Orders of magnitude higher brightness enables:
  - Subcellular spatial resolution
  - Single-cell imaging
  - Time-resolved molecular dynamics

## Schema Representation: Dual Nature

The schema handles both scenarios with the **FTIRImage** class, but distinguishes them contextually:

### Lab-based FTIR flow:
```yaml
Study:
  images:
    - FTIRImage:
        pixel_size: 5.5  # micrometers
        # No instrument reference or generic benchtop FTIR
```

### Synchrotron FTIR flow:
```yaml
Dataset:
  instruments:
    - Instrument:  # Could be specialized SynchrotronInstrument
        instrument_code: "ALS-BSISB-5.4"
        manufacturer: "Lawrence Berkeley National Laboratory"
        # Light source specific attributes

Study:
  instrument_runs:
    - ExperimentRun:
        technique: "ftir_spectroscopy"  # Not in current TechniqueEnum!
        instrument_id: "ALS-BSISB-5.4"

  images:
    - FTIRImage:
        pixel_size: 0.02  # micrometers (nano-resolution)
        molecular_signatures: [...]
```

## Schema Gaps for FTIR

**Missing from TechniqueEnum:**
```yaml
# Should add:
ftir_spectroscopy:
  description: "Fourier Transform Infrared spectroscopy"
sr_ftir:
  description: "Synchrotron radiation FTIR"
```

**No specialized instrument class:**
- Current: Generic `Instrument` class
- Could add: `FTIRInstrument` or `InfraredSpectroscopyInstrument`
  - Lab vs synchrotron source type
  - Detector specifications (MCT, InSb)
  - Coupling modes (transmission, ATR, reflection)

## Comparison with Other Imaging Modalities

| Modality | Light Source? | Schema Class | Source Type |
|----------|---------------|--------------|-------------|
| **FTIR (lab)** | ❌ No | FTIRImage | Globar/tungsten lamp |
| **SR-FTIR (synchrotron)** | ✅ Yes | FTIRImage | Synchrotron radiation |
| XRF | ✅ Yes | XRFImage | X-rays (synchrotron preferred) |
| Fluorescence | ❌ No | FluorescenceImage | Lasers/lamps |
| Optical | ❌ No | OpticalImage | Visible light |
| Cryo-EM | ❌ No | Image2D/3D | Electron beam |
| X-ray diffraction | ✅ Yes | Image2D | X-rays (synchrotron or rotating anode) |

## What Makes Synchrotron FTIR Special?

**Brightness advantage:**
- Lab source: ~10¹³ photons/s/mm²
- Synchrotron: ~10¹⁶ photons/s/mm² (1000x more!)

**Enables unique science:**

1. **Nano-spectroscopy (SINS)**: 20 nm resolution with AFM coupling
   - Map protein aggregates within single cells
   - Identify amyloid fibrils in neurodegenerative disease samples

2. **Time-resolved dynamics**: Protein folding, ligand binding
   - Millisecond time resolution
   - Track conformational changes in real-time

3. **3D FTIR tomography**: Chemical composition in 3D
   - Molecular mapping throughout intact cells/tissues
   - Complement to X-ray tomography

## Use Cases in Structural Biology

From the schema documentation:
> A multimodal plant imaging study might combine:
> 3. **FTIR spectroscopy to identify stress-related molecular changes**

**Example workflow:**
```yaml
Study:
  title: "Heat stress response in Arabidopsis"

  # Step 1: Synchrotron FTIR to map molecular changes
  instrument_runs:
    - ExperimentRun:
        technique: sr_ftir
        instrument_id: "ALS-BSISB-5.4"
  images:
    - FTIRImage:
        molecular_signatures:
          - "Increased 1650 cm⁻¹ (protein misfolding)"
          - "Decreased 1740 cm⁻¹ (membrane disruption)"

  # Step 2: Fluorescence to identify specific proteins
  images:
    - FluorescenceImage:
        fluorophore: "GFP-HSP70"  # Heat shock protein

  # Step 3: Cryo-EM of isolated protein complexes
  instrument_runs:
    - ExperimentRun:
        technique: cryo_em
        sample_id: "hsp70-complex"
```

## Summary

**FTIR in this schema:**

| Aspect | Lab-based | Synchrotron-based |
|--------|-----------|-------------------|
| **Light source?** | ❌ No (general structural biology) | ✅ Yes (light source technique) |
| **IR source** | Globar, tungsten | Synchrotron radiation |
| **Spatial resolution** | 10-20 μm | 2 μm down to 20 nm |
| **Schema class** | `FTIRImage` | `FTIRImage` (same class!) |
| **Distinguisher** | Generic/no instrument | `beamline_id`, high resolution |
| **BER facility** | Various labs | **BSISB at ALS (Berkeley)** |

**FTIR is the bridge modality** - accessible as benchtop instrument but dramatically enhanced by synchrotron light sources, making it both a general structural biology tool AND a light source technique depending on implementation.

## Related Documentation

- [FTIRImage class documentation](FTIRImage.md)
- [BER DOE Facilities - BSISB section](background/ber-doe-facilities.md)
- [Example: FTIR molecular imaging](../tests/data/valid/FTIRImage-molecular.yaml)
