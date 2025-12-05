# PNNL Metadata to Lambda-BER Schema Mapping

## Complete Field-by-Field Mapping

This document provides a line-by-line mapping of PNNL metadata fields to the Lambda-BER schema.

| PNNL Field                                        | Lambda-BER Field                            | Notes                                                                                     |
| :------------------------------------------------ | :------------------------------------------ | :---------------------------------------------------------------------------------------- |
| **metadata.program.proposal_id**                  | `Study.id`                                  | **Transformation**: Prefixed with `"proposal_"` to create study identifier                |
| **metadata.program.short_sample_name**            | `Sample.sample_code`                        | Direct mapping                                                                            |
| **metadata.program.session_id**                   | `ExperimentRun.experiment_code`             | Direct mapping                                                                            |
| **metadata.program.instrument_id**                | `CryoEMInstrument.instrument_code`          | **Transformation**: Converted to string if numeric                                        |
| **metadata.program.voltage**                      | `CryoEMInstrument.accelerating_voltage`     | Direct mapping (kV)                                                                       |
| **metadata.program.cs**                           | `CryoEMInstrument.cs`                       | Direct mapping - spherical aberration in mm                                               |
| **metadata.program.nominal_pixel_size**           | `ExperimentRun.pixel_size_x`                | **Unit Conversion**: Ångström → µm (multiply by 1e-4)                                     |
| **metadata.program.nominal_pixel_size**           | `ExperimentRun.pixel_size_y`                | **Unit Conversion**: Ångström → µm (same value for x/y)                                   |
| **metadata.program.total_dose**                   | `DataCollectionStrategy.total_dose`         | Direct mapping (e⁻/Ų)                                                                     |
| **metadata.program.nominal_dose_rate_eps**        | `DataCollectionStrategy.dose_per_frame`     | **Approximation**: dose_rate used as dose_per_frame proxy                                 |
| **metadata.program.frames_per_second**            | —                                           | **GAP**: No corresponding field in Lambda-BER schema                                      |
| **metadata.program.total_exposure**               | `ExperimentRun.exposure_time`               | Direct mapping (seconds)                                                                  |
| **metadata.program.processing_scheme**            | —                                           | **GAP**: No field for SPA/Tomography/MicroED flag (1/2/3)                                 |
| **metadata.program.detector_id**                  | `CryoEMInstrument.model`                    | **Fallback**: Used when no model specified; values like "K3", "Ceta-D"                    |
| **metadata.program.detector_physical_pixel_size** | `CryoEMInstrument.pixel_size_physical_um`   | Direct mapping (µm)                                                                       |
| **metadata.program.nominal_magnification**        | `ExperimentRun.magnification`               | Direct mapping (kx)                                                                       |
| **metadata.program.nominal_camera_Length**        | —                                           | **GAP**: No corresponding field (used in diffraction/microED)                             |
| **metadata.program.binning_factor**               | `ExperimentRun.camera_binning`              | **Type Coercion**: Only mapped if integer; floats like 0.5 are skipped with warning       |
| **metadata.program.tilting_mode**                 | —                                           | **GAP**: No field for tilt series mode (0=none, 1=dose-symmetric, 2=linear, 3=continuous) |
| **metadata.program.fiducial_size**                | —                                           | **GAP**: No field for fiducial marker size in tomography (Å)                              |
| **metadata.program.tilt_angle_increment**         | —                                           | **GAP**: No field for tilt angle step size (degrees)                                      |
| **metadata.program.rotation_rate**                | —                                           | **GAP**: No field for continuous tilt rotation rate (deg/s)                               |
| **metadata.program.c2_aperture**                  | `CryoEMInstrument.c2_aperture`              | Direct mapping (µm)                                                                       |
| **metadata.program.spot_size**                    | `CryoEMInstrument.spotsize`                 | Direct mapping (spot size setting, typically 1-9)                                         |
| **metadata.program.beam_diameter**                | `DataCollectionStrategy.beam_size_um`       | Direct mapping (µm)                                                                       |
| **metadata.program.energy_filter_slit**           | `CryoEMInstrument.energy_filter_slit_width` | Direct mapping (eV)                                                                       |
| **metadata.program.phase_plate**                  | `CryoEMInstrument.phase_plate`              | Direct mapping (boolean)                                                                  |
| **metadata.program.topaz_model**                  | —                                           | **GAP**: No field for particle picking AI model identifier                                |
| **metadata.program.motCorr_bin**                  | —                                           | **GAP**: No field for motion correction binning parameter                                 |
| **conditions.sample_mg/ml**                       | `Sample.concentration`                      | **Transformation**: Parsed as float if present                                            |
| **conditions.sample_buffer**                      | `Sample.buffer_composition.components`      | **Transformation**: String parsed/split into component list                               |
| **conditions.vitrification_settings**             | `CryoEMPreparation.vitrification_details`   | Direct mapping (free-text description)                                                    |
| **assesments.ice_contamination**                  | —                                           | **GAP**: No quality assessment field (1=None, 2=Limited, 3=Severe)                        |
| **assesments.ice_quality**                        | —                                           | **GAP**: No ice thickness quality field (1=Ideal, 2=Thin, 3=Thick)                        |
| **assesments.particle_concentration**             | —                                           | **GAP**: No particle density field (1=Good, 2=Low, 3=High)                                |
| **notes**                                         | `Study.description`                         | Direct mapping (multiline free-text comments)                                             |

---

## Key Transformations & Issues

### ✅ **Unit Conversions**
- **Pixel Size**: PNNL uses Ångströms; Lambda-BER uses micrometers (`value * 1e-4`)

### ⚠️ **Type Coercions**
- **camera_binning**: Lambda-BER requires integer; PNNL has float values (0.5, 1.0, 2.0)
  - **Script Behavior**: Skips mapping if not a whole number (e.g., 0.5 triggers warning)
  - **Rationale**: Binning factor 0.5 likely refers to super-resolution mode, not traditional binning

### ❌ **Schema Gaps (Unmapped Fields)**
The following PNNL fields have no home in Lambda-BER schema:

| Missing Field            | PNNL Value Example                     | Use Case                                     |
| :----------------------- | :------------------------------------- | :------------------------------------------- |
| `frames_per_second`      | `null`                                 | Movie acquisition frame rate                 |
| `processing_scheme`      | `1` (SPA) / `2` (Tomo) / `3` (MicroED) | Data collection modality flag                |
| `nominal_camera_Length`  | `null` (cm)                            | Diffraction camera length for microED        |
| `tilting_mode`           | `0` (none) / `1-3` (tilt modes)        | Tomography tilt strategy                     |
| `fiducial_size`          | `null` (Å)                             | Gold fiducial marker size for tilt alignment |
| `tilt_angle_increment`   | `null` (degrees)                       | Tilt series angular step                     |
| `rotation_rate`          | `null` (deg/s)                         | Continuous tilt rotation speed               |
| `topaz_model`            | `"NA"` / `"unet"`                      | Topaz AI model for particle picking          |
| `motCorr_bin`            | `1`                                    | MotionCor2 binning factor                    |
| `ice_contamination`      | `1-3` (enum)                           | Qualitative ice contamination assessment     |
| `ice_quality`            | `1-3` (enum)                           | Qualitative ice thickness assessment         |
| `particle_concentration` | `1-3` (enum)                           | Qualitative particle density assessment      |

### 🔄 **Approximations**
- **nominal_dose_rate_eps → dose_per_frame**: Dose rate (e⁻/Ų/s) used as proxy for per-frame dose when frames_per_second not provided

### 📝 **String Parsing**
- **sample_buffer**: Free-text buffer string split on common delimiters (`,`, `;`, `\n`) to populate `BufferComposition.components` list

---

## Usage

The mapping is implemented in `map_pnnl_metadata.py`:

```bash
python3 map_pnnl_metadata.py pnnl_examples/Example_Metadata/metadata.yaml --verbose
```

**Output**: 
- YAML file: `output_YYYYMMDD_HHMMSS.yaml`
- Log file: `mapping_YYYYMMDD_HHMMSS.log`
- Validation: Automatically runs `linkml-validate` on output
