# PNNL Metadata to Lambda-BER Schema Mapping Overview

This document provides a high-level overview of the structure of PNNL metadata, how it maps to the Lambda-BER schema, identified gaps, and the conversion logic.

## 1. PNNL Metadata Structure

The PNNL metadata is provided in a YAML format with the following top-level sections:

### `metadata.program`
Contains the core experimental parameters and instrument settings.
- **Identifiers**: `proposal_id`, `session_id`, `instrument_id`, `short_sample_name`
- **Instrument Settings**: `voltage`, `cs`, `c2_aperture`, `spot_size`, `phase_plate`, `energy_filter_slit`
- **Detector Settings**: `detector_id`, `detector_physical_pixel_size`, `binning_factor`
- **Acquisition Parameters**: `nominal_pixel_size`, `total_dose`, `nominal_magnification`, `beam_diameter`, `total_exposure`

### `conditions`
Contains sample preparation details.
- `sample_mg/ml`: Concentration
- `sample_buffer`: Buffer composition
- `vitrification_settings`: Freezing details

### `assesments` (sic)
Contains qualitative quality checks (currently unmapped).
- `ice_contamination`
- `ice_quality`
- `particle_concentration`

---

## 2. Mapping Strategy

The conversion script maps PNNL fields to the hierarchical Lambda-BER schema structure: `Dataset` → `Study` → `Sample` / `Instrument` / `ExperimentRun`.

### **Study & Sample**
| PNNL Field                  | Lambda-BER Field            | Notes                     |
| :-------------------------- | :-------------------------- | :------------------------ |
| `program.proposal_id`       | `Study.id`                  | Prefixed with `proposal_` |
| `program.short_sample_name` | `Sample.sample_code`        |                           |
| `conditions.sample_mg/ml`   | `Sample.concentration`      | Parsed as float           |
| `conditions.sample_buffer`  | `Sample.buffer_composition` | Mapped to components list |

### **Instrument (CryoEMInstrument)**
| PNNL Field                             | Lambda-BER Field                          | Notes                |
| :------------------------------------- | :---------------------------------------- | :------------------- |
| `program.instrument_id`                | `CryoEMInstrument.instrument_code`        |                      |
| `program.detector_id`                  | `CryoEMInstrument.model`                  | Fallback mapping     |
| `program.voltage`                      | `CryoEMInstrument.accelerating_voltage`   |                      |
| `program.cs`                           | `CryoEMInstrument.cs`                     | Spherical aberration |
| `program.spot_size`                    | `CryoEMInstrument.spotsize`               |                      |
| `program.c2_aperture`                  | `CryoEMInstrument.c2_aperture`            |                      |
| `program.detector_physical_pixel_size` | `CryoEMInstrument.pixel_size_physical_um` |                      |
| `program.phase_plate`                  | `CryoEMInstrument.phase_plate`            |                      |

### **ExperimentRun & DataCollectionStrategy**
| PNNL Field                      | Lambda-BER Field                      | Notes                                                  |
| :------------------------------ | :------------------------------------ | :----------------------------------------------------- |
| `program.session_id`            | `ExperimentRun.experiment_code`       |                                                        |
| `program.total_dose`            | `DataCollectionStrategy.total_dose`   |                                                        |
| `program.beam_diameter`         | `DataCollectionStrategy.beam_size_um` |                                                        |
| `program.nominal_magnification` | `ExperimentRun.magnification`         |                                                        |
| `program.nominal_pixel_size`    | `ExperimentRun.pixel_size_x`          | **Converted**: Angstroms (PNNL) → Micrometers (Lambda) |
| `program.binning_factor`        | `ExperimentRun.camera_binning`        | **Type Check**: Skipped if not integer                 |

---

## 3. Identified Gaps

### **Missing in Lambda-BER Schema**
The following fields exist in PNNL metadata but have no corresponding home in the current schema:
1.  **Assessments Block**: `ice_contamination`, `ice_quality`, `particle_concentration`.
    *   *Status*: Logged as warnings; data is not preserved in output.
2.  **Specific Acquisition Fields**:
    *   `nominal_dose_rate_eps` (Mapped to `dose_per_frame` as approximation)
    *   `processing_scheme` (SPA/Tomography flag)
    *   `tilting_mode`, `tilt_angle_increment` (Tomography specific)

### **Data Type Mismatches**
1.  **Binning Factor**:
    *   PNNL: Float (e.g., `0.5`, `1.0`)
    *   Lambda-BER: Integer
    *   *Resolution*: Script skips mapping if value is a non-integer float.
2.  **Pixel Size Units**:
    *   PNNL: Angstroms
    *   Lambda-BER: Micrometers
    *   *Resolution*: Script performs conversion (`val * 1e-4`).

---

## 4. Code Overview (`map_pnnl_metadata.py`)

The conversion is handled by a Python script using `pydantic` models generated from the LinkML schema.

### **Key Components**
1.  **Setup**: Imports schema classes from `src/lambda_ber_schema/pydantic.py`.
2.  **Logging**: Custom logger tracks every mapped field (`🔗 [MAP]`), warnings (`⚠️ [WARN]`), and new object creation (`✨ [NEW]`).
3.  **Extraction & Transformation**:
    *   Reads YAML safely.
    *   Handles typo correction (e.g., `assesments` vs `assessments`).
    *   Performs unit conversions (Angstrom → um).
    *   Validates types (e.g., ensuring binning is int).
4.  **Object Construction**: Builds `Study`, `Sample`, `CryoEMInstrument`, and `ExperimentRun` objects and links them.
5.  **Workarounds**:
    *   Manually dumps `instruments` list to JSON/YAML to preserve subclass fields (like `cs`) that Pydantic v2 might otherwise strip when referenced via a base class list.
6.  **Validation**: Runs `linkml-validate` on the generated output to ensure schema compliance.

### **Usage**
```bash
python3 map_pnnl_metadata.py [path_to_metadata.yaml] --verbose
```
