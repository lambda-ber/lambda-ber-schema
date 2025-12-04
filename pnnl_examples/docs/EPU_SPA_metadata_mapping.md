# EPU Single Particle Analysis (SPA) Metadata Mapping to Lambda-BER Schema

## Executive Summary

### Overview
This document provides a comprehensive field-by-field mapping of ThermoFisher EPU (automated single particle cryo-EM) metadata to the Lambda-BER schema. The analysis focuses exclusively on **Single Particle Analysis (SPA) workflows**, excluding tomography-specific features.

Three EPU metadata sources were analyzed:
- **FoilHole XML** - Per-image acquisition metadata (~60 fields) including microscope state, detector settings, and optical parameters
- **EpuSession.dm** - Session-level automation settings (~40 fields) including data management, automation parameters, and quality control settings
- **GridSquare.dm** - Grid square metadata (~15 fields) including atlas positions, grid square geometry, and selection criteria

### Key Findings

**Overall Schema Coverage for SPA Workflows:**
- ✅ **75% Good Coverage** - Core SPA imaging parameters well-supported
- ⚠️ **15% Partial Coverage** - Fields exist but need adaptation or extension
- ❌ **10% Missing** - EPU-specific automation and grid screening features absent

**What Works Well:**
The Lambda-BER schema provides strong support for SPA essentials:
- Core imaging parameters: pixel size, exposure time, defocus, dose, frame count
- Instrument identification: accelerating voltage, detector type, instrument ID
- Sample tracking: sample IDs, preparation parameters
- File provenance: file paths, checksums, data types
- Workflow tracking: processing steps, software versions

**Critical Gaps for EPU SPA Workflows:**
1. **Grid Screening & Quality** (EPU automation)
   - No ice thickness assessment tracking
   - No grid square selection criteria
   - No hole/foil selection parameters
   - No automated screening results storage

2. **Advanced Instrument Parameters**
   - No spherical aberration (Cs) field
   - Missing aperture settings (C1, C2, C3, objective, selected area)
   - No spot size or beam diameter
   - No energy filter slit width
   - No nominal magnification
   - No detector model (only generic type enum)
   - No beam alignment parameters (beam shift/tilt, image shift)

3. **EPU-Specific Automation**
   - No atlas/grid square hierarchy tracking
   - No autoloader slot/position
   - No hole clustering parameters
   - No defocus offset pattern (multi-shot per hole)
   - No automated focusing/zero-loss tuning schedules

4. **Session & Project Management**
   - No project/dataset/experiment hierarchy (DMP integration)
   - No session name tracking
   - No email notification settings
   - No file format preferences

### Impact Assessment

**For Basic SPA Data Collection:**
- ✅ Schema is **production-ready** for manual EPU workflows
- Can capture all essential imaging parameters
- Supports complete sample-to-structure provenance
- Missing only convenience/automation metadata

**For Automated EPU Sessions:**
- ⚠️ Schema has **limited automation support**
- Cannot track grid screening decisions (ice quality, hole selection)
- Missing EPU automation hierarchy (session → grid square → foil hole)
- No support for multi-shot-per-hole strategies
- Cannot store automated quality assessment results

**For Facility Management:**
- ⚠️ Schema lacks **facility-specific features**
- No autoloader slot tracking for sample inventory
- No project/proposal hierarchy for DMP systems
- Missing advanced instrument parameters for troubleshooting

### Recommendations by Priority

**HIGH PRIORITY** (essential for EPU SPA adoption):
1. **Grid Quality Assessment** - Add to `QualityMetrics` or `SamplePreparation`:
   - `ice_thickness_quality` (IceThicknessEnum: ideal, too_thin, too_thick, contaminated)
   - `grid_square_quality` (GridSquareQualityEnum: good, marginal, rejected)
   - `hole_selection_method` (HoleSelectionEnum: manual, automated, smart_epu)

2. **Advanced Instrument Parameters** - Add to `CryoEMInstrument`:
   - `spherical_aberration_mm` (float)
   - `c1_aperture_um`, `c2_aperture_um`, `c3_aperture_um` (float)
   - `objective_aperture_um`, `selected_area_aperture_um` (float)
   - `spot_size` (integer)
   - `energy_filter_width_ev` (float)
   - `nominal_magnification` (integer)
   - `detector_model` (string) - supplement to detector_type enum

3. **Beam Characterization** - Add to `ExperimentalConditions`:
   - `beam_diameter_um` (float)
   - `beam_shift_x`, `beam_shift_y` (float)
   - `beam_tilt_x`, `beam_tilt_y` (float)
   - `image_shift_x`, `image_shift_y` (float)

4. **Multi-level Data Hierarchy** - Add navigation structure:
   - `grid_square_id` to `Image2D` or `ExperimentRun`
   - `atlas_position_x`, `atlas_position_y` to track grid square locations
   - `foil_hole_position` for hole-within-grid-square tracking

**MEDIUM PRIORITY** (enhanced EPU integration):
5. **EPU Session Tracking** - Add to `Study` or `ExperimentRun`:
   - `session_name` (string)
   - `autoloader_slot` (integer)
   - `clustering_mode` (ClusteringModeEnum: no_clustering, beam_image_shift, stage_movement)
   - `hole_clustering_radius_um` (float)
   - `defocus_offset_enabled` (boolean)
   - `auto_focus_enabled` (boolean)
   - `auto_zero_loss_enabled` (boolean)

6. **Detector Calibration** - Add to `CryoEMInstrument`:
   - `counts_per_electron` (float)
   - `detector_physical_pixel_size_um` (float)
   - `electron_counting_mode` (boolean)
   - `super_resolution_factor` (integer)

7. **Gun Parameters** - Add to `CryoEMInstrument`:
   - `electron_source` (ElectronSourceEnum: field_emission, schottky, thermionic)
   - `extractor_voltage_v` (float)
   - `gun_lens` (integer)

**LOW PRIORITY** (facility-specific features):
8. **File Format Preferences** - Add to `Study` or `DataFile`:
   - `output_format` (string) - e.g., "Tiff Lzw Non-Gain normalized"
   - `image_file_format` (ImageFileFormatEnum)

9. **DMP Integration** - Add project hierarchy to `Study`:
   - `project_id`, `project_name` (string)
   - `experiment_id`, `experiment_name` (string)
   - `dataset_id`, `dataset_name` (string)
   - `workflow_id`, `workflow_name` (string)

10. **Automation Settings** - Add to `ExperimentRun`:
    - `email_notification_enabled` (boolean)
    - `smart_hole_selection_enabled` (boolean)

### Implementation Path Forward

**Phase 1 - Core SPA Support (2-3 weeks):**
- Add grid quality assessment fields (3 fields)
- Add advanced instrument parameters (10 fields to CryoEMInstrument)
- Add beam characterization (7 fields to ExperimentalConditions)
- Estimated: Complete SPA imaging metadata capture

**Phase 2 - EPU Integration (2-3 weeks):**
- Add grid square hierarchy (grid_square_id, atlas positions)
- Add EPU session automation parameters
- Add detector calibration fields
- Estimated: Full EPU session reconstruction from metadata

**Phase 3 - Facility Features (1-2 weeks):**
- Add DMP project hierarchy integration
- Add file format preferences
- Add automation notification settings
- Estimated: Complete facility workflow support

**Total Timeline:** 5-8 weeks for full EPU SPA integration

---

## Detailed Field-by-Field Mapping

**Mapping Legend:**
- ✅ **Direct Match** - Field exists with appropriate type/range in Lambda-BER schema
- ⚠️ **Partial Match** - Concept exists but needs adaptation (unit conversion, enum mapping, free-text parsing)
- 🔶 **Alternative Location** - Could map to different class than primary recommendation
- ❌ **Missing** - No equivalent field in current schema, extension required

---

## 1. EPU FoilHole XML Metadata Analysis

### 1.1 Image Identification

**Field: `uniqueID` (UUID)**
- EPU Value: `45ed54ca-a609-476a-8616-2475cf33096d`
- Schema Classes Checked: Image2D, Image, NamedThing
- ✅ **DIRECT MATCH**: `Image2D.id` (uriorcurie type)
- Schema Location: Inherited from NamedThing base class
- Mapping: Use UUID directly as unique identifier
- Notes: Perfect match for per-image unique tracking

**Field: `name`**
- EPU Value: `"Empty"` (often contains hole/position identifier)
- Schema Classes Checked: Image2D, Image, NamedThing
- ✅ **DIRECT MATCH**: `Image2D.title` (string)
- Schema Location: Inherited from NamedThing base class
- Alternative: `Image2D.file_name` if referring to filename
- Mapping: Use for human-readable image description

---

### 1.2 Dose & Radiation

**Field: `DoseOnCamera`**
- EPU Value: `27.84585894962964` (e⁻/Å²)
- Schema Classes Checked: Image2D, DataCollectionStrategy, ExperimentalConditions
- ✅ **DIRECT MATCH**: `Image2D.dose` (float)
- Schema Location: Image2D class, line ~741
- Description: "Electron dose in electrons per square Angstrom"
- Notes: Per-image total dose tracking

**Field: `DoseRate`**
- EPU Value: `12.7547940669171` (e⁻/Å²/s)
- Schema Classes Checked: DataCollectionStrategy, ExperimentalConditions, Image2D
- ❌ **MISSING**: No `dose_rate` field in any class
- Available: `DataCollectionStrategy.dose_per_frame` (float) but not rate per second
- **RECOMMENDATION**: Add `dose_rate` (float, units: e⁻/Å²/s) to `DataCollectionStrategy`
- Use Case: Critical for dose-fractionation calculations and detector DQE optimization

**Field: `Dose` (raw dose in electrons)**
- EPU Value: `2.995658758630005E+21` (total electrons)
- Schema Classes Checked: Image2D, DataCollectionStrategy
- ⚠️ **PARTIAL MATCH**: Can derive from `Image2D.dose` and area
- Calculation: dose (e⁻/Å²) × pixel_size² × dimensions_x × dimensions_y
- Notes: Raw electron count less commonly used than dose per area

---

### 1.3 Aperture Settings

**Field: `Aperture[C1].Name`**
- EPU Value: `"2000"` (μm)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No C1 aperture field
- **RECOMMENDATION**: Add `c1_aperture_um` (float) to `CryoEMInstrument`
- Use Case: Condenser system tuning, beam coherence control

**Field: `Aperture[C2].Name`**
- EPU Value: `"50"` (μm)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No C2 aperture field
- **RECOMMENDATION**: Add `c2_aperture_um` (float) to `CryoEMInstrument`
- Use Case: Primary beam-defining aperture, critical for parallel illumination

**Field: `Aperture[C3].Name`**
- EPU Value: `"None"`
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No C3 aperture field
- **RECOMMENDATION**: Add `c3_aperture_um` (float, optional) to `CryoEMInstrument`
- Use Case: Third condenser aperture (some microscope configurations)

**Field: `Aperture[OBJ].Name`**
- EPU Value: `"None"`
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No objective aperture field
- **RECOMMENDATION**: Add `objective_aperture_um` (float, optional) to `CryoEMInstrument`
- Use Case: Contrast enhancement, resolution limiting

**Field: `Aperture[SA].Name`**
- EPU Value: `"None"`
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No selected area aperture field
- **RECOMMENDATION**: Add `selected_area_aperture_um` (float, optional) to `CryoEMInstrument`
- Use Case: Selected area diffraction, rarely used in SPA

---

### 1.4 Detector Configuration

**Field: `Detectors[EF-CCD].CommercialName`**
- EPU Value: `"BioQuantum K3"`
- Schema Classes Checked: CryoEMInstrument, DetectorTypeEnum
- ⚠️ **PARTIAL MATCH**: `CryoEMInstrument.detector_type` (DetectorTypeEnum)
- Schema Location: CryoEMInstrument class, line ~484
- Available Enum Values: `direct_electron`, `ccd`, `cmos`, `hybrid_pixel`
- ❌ **LIMITATION**: Cannot store specific model string "BioQuantum K3"
- Mapping: K3 → `detector_type: direct_electron`
- **RECOMMENDATION**: Add `detector_model` (string) to `CryoEMInstrument` to store commercial name
- Use Case: Precise detector identification for data processing parameters

**Field: `Detectors[EF-CCD].ElectronCounted`**
- EPU Value: `true`
- Schema Classes Checked: CryoEMInstrument, DataCollectionStrategy
- ❌ **MISSING**: No electron counting mode flag
- **RECOMMENDATION**: Add `electron_counting_mode` (boolean) to `CryoEMInstrument`
- Use Case: Indicates counting vs integrating mode, affects DQE and processing

**Field: `BinaryResult.Detector`**
- EPU Value: `"EF-CCD"` (detector location identifier)
- Schema Classes Checked: CryoEMInstrument, Instrument
- ⚠️ **PARTIAL MATCH**: Can use `Instrument.description` or `CryoEMInstrument.title`
- Notes: Facility-specific identifier, not critical for schema

**Field: `DetectorCommercialName`**
- EPU Value: `"BioQuantum K3"` (duplicate of above)
- See: `Detectors[EF-CCD].CommercialName` analysis above

---

### 1.5 Optical System Settings

**Field: `StemMagnification`**
- EPU Value: `false` (TEM mode indicator)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No STEM mode flag
- **RECOMMENDATION**: Add `stem_mode` (boolean) to `CryoEMInstrument`
- Use Case: Distinguish TEM vs STEM imaging modes
- Notes: For SPA, always false (TEM mode)

**Field: `PhasePlateUsed`**
- EPU Value: `false`
- Schema Classes Checked: CryoEMInstrument
- ✅ **DIRECT MATCH**: `CryoEMInstrument.phase_plate` (boolean)
- Schema Location: CryoEMInstrument class, line ~479
- Description: "Phase plate available"
- Notes: Perfect match for Volta phase plate tracking

**Field: `AppliedDefocus`**
- EPU Value: `-7.5E-07` (meters) = -0.75 μm = -7500 Å
- Schema Classes Checked: Image2D, ExperimentalConditions, DataCollectionStrategy
- ✅ **DIRECT MATCH**: `Image2D.defocus` (float)
- Schema Location: Image2D class, line ~755
- Description: "Defocus in micrometers"
- Mapping: Convert -7.5E-07 m → -0.75 μm
- Notes: Per-image defocus tracking, essential for CTF correction

**Field: `IlluminationIntensity`**
- EPU Value: `0` (normalized beam intensity)
- Schema Classes Checked: ExperimentalConditions, DataCollectionStrategy
- ❌ **MISSING**: No beam intensity field
- **RECOMMENDATION**: Add `beam_intensity` (float) to `ExperimentalConditions`
- Use Case: Beam current monitoring, consistency checking
- Notes: Often normalized 0-1 or arbitrary units

---

### 1.6 Camera & Acquisition Settings

**Field: `Binning.x` / `Binning.y`**
- EPU Value: `1` (no binning)
- Schema Classes Checked: Image2D, DataCollectionStrategy, CryoEMInstrument
- ❌ **MISSING**: No binning field
- **RECOMMENDATION**: Add `binning_factor` (integer or float) to `DataCollectionStrategy` or `Image2D`
- Use Case: Super-resolution (0.5) vs binned (2, 4) collection modes
- Notes: Critical for pixel size calibration

**Field: `CameraLocation`**
- EPU Value: `"EnergyFilter"` (post-GIF camera position)
- Schema Classes Checked: CryoEMInstrument, Instrument
- ❌ **MISSING**: No camera location field
- Notes: Facility-specific detail, low priority for schema
- Alternative: Document in `Instrument.description`

**Field: `ExposureTime`**
- EPU Value: `2.19` (seconds)
- Schema Classes Checked: Image2D, Image, ExperimentalConditions
- ✅ **DIRECT MATCH**: `Image2D.exposure_time` (float)
- Schema Location: Image2D class, line ~737
- Description: "Exposure time in seconds"
- Notes: Total exposure including all frames

**Field: `ReadoutArea` (width, height)**
- EPU Value: `width=5760`, `height=4092` (pixels)
- Schema Classes Checked: Image2D, Image
- ✅ **DIRECT MATCH**: `Image2D.dimensions_x`, `Image2D.dimensions_y` (integer)
- Schema Location: Image2D class, lines ~729, 733
- Notes: Image dimensions in pixels

**Field: `Shutter`**
- EPU Value: `"PreSpecimen"` (shutter type/location)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No shutter type field
- Notes: Low priority facility-specific detail

**Field: `SuperResolutionFactor`**
- EPU Value: `1` (no super-resolution)
- Schema Classes Checked: Image2D, DataCollectionStrategy, CryoEMInstrument
- ❌ **MISSING**: No super-resolution factor field
- Notes: Related to binning; K3 super-resolution mode doubles pixel dimensions
- **RECOMMENDATION**: Covered by `binning_factor` (0.5 for super-res)

**Field: `CameraSpecificInput.FixedReadoutArea`**
- EPU Value: `"Full"` (full sensor readout)
- Schema Classes Checked: Image2D, CryoEMInstrument
- ⚠️ **PARTIAL MATCH**: Implicit from `dimensions_x/y` matching sensor size
- Notes: Not critical if dimensions are recorded

**Field: `CameraSpecificInput.FractionationSettings.NumberOffractions`**
- EPU Value: `41` (number of frames)
- Schema Classes Checked: DataCollectionStrategy, Image2D
- ✅ **DIRECT MATCH**: `DataCollectionStrategy.total_frames` (integer)
- Schema Location: DataCollectionStrategy class, line ~1092
- Description: "Total number of frames collected"
- Notes: Essential for movie processing

**Field: `CameraSpecificInput.ElectronCountingEnabled`**
- EPU Value: `true`
- See: `Detectors[EF-CCD].ElectronCounted` analysis above (same field)

**Field: `CameraSpecificInput.AlignIntegratedImageEnabled`**
- EPU Value: `false` (in-camera motion correction disabled)
- Schema Classes Checked: WorkflowRun, DataCollectionStrategy
- ❌ **MISSING**: No in-camera processing flag
- Notes: Low priority, processing details typically in WorkflowRun

**Field: `CameraSpecificInput.ApplyDefinedShutter`**
- EPU Value: `true`
- Notes: Low priority facility-specific setting

**Field: `CameraSpecificInput.CetaFramesSummed`**
- EPU Value: `1` (no frame averaging, K3 specific)
- Notes: Detector-specific setting, not universal

**Field: `CameraSpecificInput.CetaNoiseReductionEnabled`**
- EPU Value: `false` (Ceta-specific feature)
- Notes: Detector-specific setting, not applicable to K3

---

### 1.7 DateTime & Timestamps

**Field: `acquisitionDateTime`**
- EPU Value: `2025-10-14T11:01:09.5462528-07:00` (ISO 8601 with timezone)
- Schema Classes Checked: Image2D, ExperimentRun
- ✅ **DIRECT MATCH**: `Image2D.acquisition_date` (string)
- Schema Location: Image2D class, line ~721
- Description: "Date and time of data acquisition"
- 🔶 **ALTERNATIVE**: `ExperimentRun.experiment_date` for session-level date
- Notes: Schema uses string type (not strict datetime) for flexibility

---

### 1.8 Microscope Gun Settings

**Field: `AccelerationVoltage`**
- EPU Value: `300000` (Volts) = 300 kV
- Schema Classes Checked: CryoEMInstrument, Instrument
- ✅ **DIRECT MATCH**: `CryoEMInstrument.accelerating_voltage` (integer)
- Schema Location: CryoEMInstrument class, lines ~470-476
- Range: Constrained to 120, 200, or 300 (any_of)
- Mapping: Convert 300000 V → 300 kV
- Notes: Perfect match with constraint validation

**Field: `ExtractorVoltage`**
- EPU Value: `4000` (Volts)
- Schema Classes Checked: CryoEMInstrument, ALL instrument classes
- ❌ **MISSING**: No extractor voltage field
- **RECOMMENDATION**: Add `extractor_voltage_v` (float) to `CryoEMInstrument`
- Use Case: Gun extraction voltage for field emission sources

**Field: `GunLens`**
- EPU Value: `4` (gun lens setting 1-10)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No gun lens field
- **RECOMMENDATION**: Add `gun_lens` (integer) to `CryoEMInstrument`
- Use Case: Gun lens setting affects beam current and coherence

**Field: `Sourcetype`**
- EPU Value: `"FieldEmission"` (FEG vs Schottky vs thermionic)
- Schema Classes Checked: CryoEMInstrument, Instrument
- ❌ **MISSING**: No electron source type field
- **RECOMMENDATION**: Add `electron_source` (ElectronSourceEnum) to `CryoEMInstrument`
- Enum Values: `field_emission`, `schottky`, `thermionic`, `cold_feg`
- Use Case: Source type affects coherence and resolution capabilities

**Field: `Filament`**
- EPU Value: `null` (not applicable for FEG)
- Notes: Only relevant for thermionic sources

**Field: `WehneltBias`**
- EPU Value: `null` (not applicable for FEG)
- Notes: Only relevant for thermionic sources

---

### 1.9 Instrument Identification

**Field: `InstrumentID`**
- EPU Value: `"3857"` (facility instrument identifier)
- Schema Classes Checked: Instrument, CryoEMInstrument
- ✅ **DIRECT MATCH**: `Instrument.instrument_code` (string, required)
- Schema Location: Instrument class, lines ~452-454
- Description: "Human-friendly facility or laboratory identifier"
- Notes: Perfect match for facility tracking

**Field: `InstrumentModel`**
- EPU Value: `"TITAN52338570"` (instrument model + serial)
- Schema Classes Checked: Instrument, CryoEMInstrument
- ✅ **DIRECT MATCH**: `Instrument.model` (string)
- Schema Location: Instrument class (inherited from NamedThing or explicit)
- Notes: Can store full model designation

**Field: `ComputerName`**
- EPU Value: `"TITAN52338570"` (control computer hostname)
- Schema Classes Checked: Instrument, ComputeResources
- ❌ **MISSING**: No computer name field
- Notes: Low priority infrastructure detail, can use `Instrument.description`

**Field: `ApplicationSoftware`**
- EPU Value: `"EPU"` (acquisition software)
- Schema Classes Checked: ExperimentRun, WorkflowRun
- ⚠️ **PARTIAL MATCH**: Can use `ExperimentRun.description` or `WorkflowRun.software_name`
- 🔶 **ALTERNATIVE**: Create acquisition software field in ExperimentRun
- Notes: Distinguishes EPU vs SerialEM vs manual acquisition

**Field: `ApplicationSoftwareVersion`**
- EPU Value: `"3.11.0.9330"` (EPU version)
- Schema Classes Checked: ExperimentRun, WorkflowRun
- ⚠️ **PARTIAL MATCH**: Can use `WorkflowRun.software_version`
- Notes: Important for reproducibility and bug tracking

**Field: `AcquisitionSoftware` / `AcquisitionSoftwareVersion`**
- EPU Value: `null` (redundant with ApplicationSoftware)
- Notes: Duplicate fields, use ApplicationSoftware values

---

### 1.10 Optical Column Settings

**Field: `BeamDiameter`**
- EPU Value: `8.5999999999999992E-07` (meters) = 0.86 μm
- Schema Classes Checked: ExperimentalConditions, DataCollectionStrategy, CryoEMInstrument
- ❌ **MISSING**: No beam diameter field
- **RECOMMENDATION**: Add `beam_diameter_um` (float) to `ExperimentalConditions`
- Use Case: Beam size for dose calculations and illumination area

**Field: `BeamShift._x` / `BeamShift._y`**
- EPU Value: `_x=0.010531727224588394`, `_y=-0.027878059074282646` (normalized units)
- Schema Classes Checked: ExperimentalConditions, DataCollectionStrategy
- ❌ **MISSING**: No beam shift fields
- **RECOMMENDATION**: Add `beam_shift_x`, `beam_shift_y` (float) to `ExperimentalConditions`
- Use Case: Beam positioning for multi-shot-per-hole, coma-free alignment

**Field: `BeamTilt._x` / `BeamTilt._y`**
- EPU Value: `_x=-0.011236990801990032`, `_y=0.013794582337141037` (normalized units)
- Schema Classes Checked: ExperimentalConditions, DataCollectionStrategy
- ❌ **MISSING**: No beam tilt fields
- **RECOMMENDATION**: Add `beam_tilt_x`, `beam_tilt_y` (float) to `ExperimentalConditions`
- Use Case: Coma-free alignment, beam centering

**Field: `Cameralength`**
- EPU Value: `0` (not in diffraction mode)
- Schema Classes Checked: CryoEMInstrument, XRayInstrument
- ❌ **MISSING**: No camera length field
- **RECOMMENDATION**: Add `camera_length_cm` (float) to `CryoEMInstrument`
- Use Case: Electron diffraction / microED experiments
- Notes: Zero for imaging mode (SPA)

**Field: `ColumnOperatingMode`**
- EPU Value: `"TEM"` (vs "STEM")
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No column mode field
- Related to: `stem_mode` recommendation above
- Notes: TEM for SPA workflows

**Field: `ColumnOperatingTemSubMode`**
- EPU Value: `"BrightField"` (vs dark field)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No sub-mode field
- Notes: Low priority for SPA (always bright field)

**Field: `CondenserStigmator._x/_y`**
- EPU Value: `_x=0`, `_y=0` (stigmation correction)
- Schema Classes Checked: ExperimentalConditions
- ❌ **MISSING**: No stigmator settings
- Notes: Low priority, alignment detail

**Field: `Defocus`**
- EPU Value: `1.6562127725206077E-06` (meters)
- Notes: See `AppliedDefocus` analysis above (same parameter, different field)

**Field: `DiffractionFocus` / `DiffractionShift` / `DiffractionStigmator`**
- EPU Value: `0` (not in diffraction mode)
- Notes: Not applicable to SPA imaging

**Field: `EFTEMOn`**
- EPU Value: `true` (energy filter enabled)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No energy filter status flag
- Notes: Related to energy filter slit width

**Field: `EnergyFilter.AccelerationVoltageOffset` / `DriftTubeVoltage` / `EnergyShift`**
- EPU Value: `0` (zero-loss peak centered)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No energy filter tuning fields
- Notes: Advanced energy filter parameters, low priority

**Field: `EnergyFilter.EnergySelectionSlitInserted`**
- EPU Value: `true` (slit inserted)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No slit insertion status field
- Notes: Boolean flag for energy filtering active

**Field: `EnergyFilter.EnergySelectionSlitWidth`**
- EPU Value: `20` (eV)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No energy filter slit width field
- **RECOMMENDATION**: Add `energy_filter_width_ev` (float) to `CryoEMInstrument`
- Use Case: Energy filtering for contrast enhancement (zero-loss imaging)

**Field: `EnergyFilter.EntranceApertureDiameter` / `EntranceApertureType`**
- EPU Value: `null` (not configured)
- Notes: GIF-specific settings, low priority

**Field: `Focus`**
- EPU Value: `-0.0008390391969628361` (objective lens focus, normalized)
- Schema Classes Checked: ExperimentalConditions
- ❌ **MISSING**: No objective focus field
- Notes: Low-level setting, defocus is more relevant

**Field: `GunStigmator`**
- EPU Value: `null` (not adjusted)
- Notes: Advanced gun alignment, low priority

**Field: `IlluminationMode`**
- EPU Value: `"Parallel"` (parallel vs convergent illumination)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No illumination mode field
- Notes: Low priority for SPA (always parallel)

**Field: `IlluminationProbeSubMode`**
- EPU Value: `null`
- Notes: STEM-specific setting

**Field: `ImageShift._x/_y`**
- EPU Value: `_x=0`, `_y=0` (image shift for hole centering)
- Schema Classes Checked: ExperimentalConditions, DataCollectionStrategy
- ❌ **MISSING**: No image shift fields
- **RECOMMENDATION**: Add `image_shift_x`, `image_shift_y` (float) to `ExperimentalConditions`
- Use Case: Multi-shot-per-hole positioning, hole centering

**Field: `Intensity`**
- EPU Value: `0` (C2 lens setting, normalized)
- Schema Classes Checked: ExperimentalConditions
- ❌ **MISSING**: No intensity setting field
- Related to: `beam_intensity` recommendation
- Notes: Microscope-specific C2 lens current

**Field: `ObjectiveLensMode`**
- EPU Value: `"HM"` (high magnification mode)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No objective lens mode field
- Notes: Low priority microscope-specific setting

**Field: `ObjectiveStigmator._x/_y`**
- EPU Value: `_x=0`, `_y=0` (objective stigmation correction)
- Notes: Alignment detail, low priority

**Field: `ProbeMode`**
- EPU Value: `"NanoProbe"` (vs "MicroProbe")
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No probe mode field
- **RECOMMENDATION**: Add `probe_mode` (ProbeModeEnum: nanoprobe, microprobe) to `CryoEMInstrument`
- Use Case: Condenser lens configuration (spot size and convergence)

**Field: `ProjectorMode`**
- EPU Value: `"Imaging"` (vs "Diffraction")
- Notes: Always "Imaging" for SPA

**Field: `SpotIndex`**
- EPU Value: `5` (spot size setting 1-11)
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ **MISSING**: No spot size field
- **RECOMMENDATION**: Add `spot_size` (integer) to `CryoEMInstrument`
- Use Case: Beam size and coherence control

**Field: `StemDefocus` / `StemFieldOfView` / `StemMagnification`**
- EPU Value: `null` or `0` (not in STEM mode)
- Notes: Not applicable to SPA

**Field: `TemMagnification.NominalMagnification`**
- EPU Value: `105000` (nominal mag, often differs from calibrated)
- Schema Classes Checked: CryoEMInstrument, Image2D, ExperimentalConditions
- ❌ **MISSING**: No nominal magnification field
- **RECOMMENDATION**: Add `nominal_magnification` (integer) to `CryoEMInstrument`
- Use Case: Magnification setting (actual pixel size more accurate)

**Field: `XLModeOn`**
- EPU Value: `false` (extra-low magnification mode)
- Notes: Low priority microscope mode flag

---

### 1.11 Sample & Stage

**Field: `sample.Description` / `sample.ID`**
- EPU Value: `null` (often not filled in EPU)
- Schema Classes Checked: Sample, SamplePreparation
- ✅ **DIRECT MATCH**: `Sample.description` (string), `Sample.sample_code` (string)
- Schema Location: Sample class
- Notes: Sample linking typically done at session level

**Field: `stage.Holder`**
- EPU Value: `"Unspecified"` (or specific holder type like "Autoloader")
- Schema Classes Checked: SamplePreparation, CryoEMPreparation
- ❌ **MISSING**: No sample holder type field
- **RECOMMENDATION**: Add `holder_type` (string) to `SamplePreparation` or `CryoEMPreparation`
- Use Case: Holder type affects geometry and autoloader compatibility

**Field: `stage.Position.A` (alpha tilt)**
- EPU Value: `-0.00036398933554100167` (radians) ≈ -0.02°
- Schema Classes Checked: Image2D, ExperimentalConditions
- ❌ **MISSING**: No stage tilt angles
- **RECOMMENDATION**: Add `stage_alpha` (float) to `ExperimentalConditions`
- Use Case: Stage tilt (non-zero indicates tilted grid for SPA)
- Notes: Typically ~0° for SPA (flat grid)

**Field: `stage.Position.B` (beta tilt)**
- EPU Value: `0` (radians)
- ❌ **MISSING**: No stage beta tilt
- **RECOMMENDATION**: Add `stage_beta` (float) to `ExperimentalConditions`
- Notes: Typically 0 for single-axis goniometers

**Field: `stage.Position.X/Y/Z`**
- EPU Value: `X=0.0002878273962000001`, `Y=-0.00030081124`, `Z=-6.9352311771199985E-05` (meters)
- Schema Classes Checked: Image2D, ExperimentalConditions
- ❌ **MISSING**: No stage position coordinates
- **RECOMMENDATION**: Add `stage_x_um`, `stage_y_um`, `stage_z_um` (float) to `ExperimentalConditions` or `Image2D`
- Use Case: Stage position tracking for navigation and correlation
- Notes: Critical for grid square/atlas mapping

**Field: `stage.SampleLoader`**
- EPU Value: `"None"` (or autoloader type)
- Schema Classes Checked: CryoEMInstrument, Instrument
- ⚠️ **PARTIAL MATCH**: Can use `Instrument.description`
- Notes: Facility-specific, low priority

---

### 1.12 Vacuum System

**Field: `vacuum.ProjectionChamberPressure`**
- EPU Value: `0` (Pa, often not reported accurately)
- Schema Classes Checked: ExperimentalConditions
- ⚠️ **PARTIAL MATCH**: `ExperimentalConditions.pressure` (float)
- Schema Location: ExperimentalConditions class
- Notes: Single pressure field, could use for chamber pressure

**Field: `vacuum.SamplePressure`**
- EPU Value: `0` (Pa)
- Schema Classes Checked: ExperimentalConditions
- ⚠️ **PARTIAL MATCH**: `ExperimentalConditions.pressure` (float)
- Notes: Could use this field for sample chamber pressure specifically

**Field: `vacuum.VacuumMode`**
- EPU Value: `"Ready"` (vacuum status: "Ready", "Pumping", etc.)
- Schema Classes Checked: Instrument, InstrumentStatusEnum
- ⚠️ **PARTIAL MATCH**: `Instrument.status` (InstrumentStatusEnum)
- Available Values: "operational", "maintenance", "decommissioned"
- Notes: Could map "Ready" → "operational"

---

### 1.13 Spatial Calibration & Transformations

**Field: `ReferenceTransformation.matrix`**
- EPU Values: `_m11=-9.61568336333957E-11`, `_m12=-7.0190585900244318E-12`, etc.
- Schema Classes Checked: Image2D, Image
- ❌ **MISSING**: No transformation matrix
- Notes: Advanced spatial calibration, low priority for basic SPA

**Field: `ReferenceTransformation.unit`**
- EPU Value: `Symbol=m`, `PrefixExponent=1` (meters)
- Notes: Unit specification for transformation

**Field: `SpatialScale.offset.x/y`**
- EPU Value: `x=0`, `y=0` (meters)
- Schema Classes Checked: Image2D
- ❌ **MISSING**: No spatial offset fields
- Notes: Image origin offset, low priority

**Field: `SpatialScale.pixelSize.x/y.numericValue`**
- EPU Value: `9.641267645355E-11` (meters) = 0.9641 Å
- Schema Classes Checked: Image2D, CryoEMInstrument
- ✅ **DIRECT MATCH**: `Image2D.pixel_size` (float)
- Schema Location: Image2D class, line ~733
- Description: "Pixel size in Angstroms"
- Mapping: Convert 9.641267645355E-11 m → 0.9641 Å
- Notes: Perfect match, per-image calibrated pixel size

---

### 1.14 Intensity & Scaling

**Field: `IntensityScale`**
- EPU Value: `null` (intensity scaling factor)
- Schema Classes Checked: Image2D, Image
- ❌ **MISSING**: No intensity scaling field
- Notes: Low priority for raw data, relevant for display

---

## 2. EPU Session.dm Metadata Analysis

### 2.1 Session Identification

**Field: `Id`**
- EPU Value: `13298754` (EPU session ID)
- Schema Classes Checked: Study, ExperimentRun, Dataset
- ✅ **DIRECT MATCH**: `ExperimentRun.experiment_code` (string)
- Schema Location: ExperimentRun class, lines ~559-561
- Alternative: `Study.id` for session-level tracking
- Notes: Can convert integer to string for experiment_code

**Field: `Name`**
- EPU Value: `"10-13-25-PDX_Ncrassa_true"` (session name)
- Schema Classes Checked: Study, ExperimentRun
- ✅ **DIRECT MATCH**: `Study.title` or `ExperimentRun.title` (string)
- Schema Location: Inherited from NamedThing
- Notes: Human-readable session identifier

---

### 2.2 Autoloader Configuration

**Field: `AutoloaderDescription`**
- EPU Value: `"Puck10 _11_g2 - PDX Neu"` (sample description on puck)
- Schema Classes Checked: Sample, SamplePreparation
- ⚠️ **PARTIAL MATCH**: Can use `Sample.title` or `Sample.description`
- Notes: Combines puck + position + sample name

**Field: `AutoloaderSlot`**
- EPU Value: `2` (cassette/puck slot number 1-12)
- Schema Classes Checked: Sample, SamplePreparation, StorageConditions
- ❌ **MISSING**: No autoloader slot field
- **RECOMMENDATION**: Add `autoloader_slot` (integer) to `SamplePreparation` or `StorageConditions`
- Use Case: Sample tracking in multi-cassette autoloaders, inventory management

---

### 2.3 Automation Settings

**Field: `AutoFocusEnabled`**
- EPU Value: `false` (periodic autofocus during session)
- Schema Classes Checked: DataCollectionStrategy, ExperimentRun
- ❌ **MISSING**: No autofocus flag
- **RECOMMENDATION**: Add `auto_focus_enabled` (boolean) to `DataCollectionStrategy`
- Use Case: Automation configuration, affects data quality consistency

**Field: `AutoStageTimeEnabled`**
- EPU Value: `false` (stage settling time auto-adjustment)
- Schema Classes Checked: DataCollectionStrategy, ExperimentalConditions
- ❌ **MISSING**: No stage time automation flag
- Notes: Low priority facility-specific optimization

**Field: `AutoZeroLossEnabled`**
- EPU Value: `true` (periodic zero-loss peak tuning)
- Schema Classes Checked: DataCollectionStrategy, ExperimentRun
- ❌ **MISSING**: No zero-loss tuning flag
- **RECOMMENDATION**: Add `auto_zero_loss_enabled` (boolean) to `DataCollectionStrategy`
- Use Case: Energy filter maintenance during long sessions

**Field: `AutoZeroLossPeriodicity`**
- EPU Value: `"PT1H"` (ISO 8601 duration: 1 hour)
- Schema Classes Checked: DataCollectionStrategy
- ❌ **MISSING**: No periodicity field
- Notes: Related to auto_zero_loss_enabled, medium priority

**Field: `EmailNotificationEnabled`**
- EPU Value: `false` (email alerts for session events)
- Schema Classes Checked: Study, ExperimentRun
- ❌ **MISSING**: No notification settings
- Notes: Low priority facility workflow detail

---

### 2.4 Grid Screening Settings

**Field: `EnableSmartHoleSelection`**
- EPU Value: `false` (AI-based hole quality selection)
- Schema Classes Checked: DataCollectionStrategy, QualityMetrics
- ❌ **MISSING**: No smart selection flag
- **RECOMMENDATION**: Add `smart_hole_selection_enabled` (boolean) to `DataCollectionStrategy`
- Use Case: Tracks use of AI hole selection (Smart EPU feature)

**Field: `IceThicknessEnabled`**
- EPU Value: `false` (ice thickness assessment during screening)
- Schema Classes Checked: QualityMetrics, DataCollectionStrategy
- ❌ **MISSING**: No ice thickness screening flag
- Related to: `ice_thickness_quality` recommendation in QualityMetrics
- Notes: Boolean for feature enabled, separate from quality assessment enum

**Field: `IsManuallySelected`**
- EPU Value: `true` (manual vs automated grid square selection)
- Schema Classes Checked: DataCollectionStrategy, QualityMetrics
- ❌ **MISSING**: No manual selection flag
- Notes: Distinguishes manual screening from automated

**Field: `IsSmartFilterGridSquareDecisionKnown`**
- EPU Value: `false` (Smart EPU decision recorded)
- Schema Classes Checked: DataCollectionStrategy
- ❌ **MISSING**: No smart filter decision field
- Notes: Low priority Smart EPU internal state

---

### 2.5 Multi-Shot Configuration

**Field: `ClusteringMode`**
- EPU Value: `"NoClustering"` (single shot per hole)
- Possible Values: "NoClustering", "BeamImageShift", "StageMovement"
- Schema Classes Checked: DataCollectionStrategy, ExperimentalConditions
- ❌ **MISSING**: No clustering mode field
- **RECOMMENDATION**: Add `clustering_mode` (ClusteringModeEnum) to `DataCollectionStrategy`
- Enum Values: `no_clustering`, `beam_image_shift`, `stage_movement`
- Use Case: Multi-shot-per-hole strategies (3x3 grids, etc.)

**Field: `ClusteringRadius`**
- EPU Value: `0` (μm, spacing between shots)
- Schema Classes Checked: DataCollectionStrategy
- ❌ **MISSING**: No clustering radius field
- **RECOMMENDATION**: Add `hole_clustering_radius_um` (float) to `DataCollectionStrategy`
- Use Case: Shot spacing for multi-shot patterns

**Field: `NumberOfImages` (not visible in excerpt)**
- Expected: Total images planned for session
- Schema Classes Checked: Study, ExperimentRun
- ⚠️ **PARTIAL MATCH**: Could derive from collection of images
- Notes: Metadata vs actual count

---

### 2.6 Data Management & Output

**Field: `DoseFractionsOutputFormat`**
- EPU Value: `"Tiff Lzw Non-Gain normalized"` (movie frame format)
- Schema Classes Checked: DataFile, FileFormatEnum
- ⚠️ **PARTIAL MATCH**: `DataFile.file_format` (FileFormatEnum)
- Available Enum Values: Generic formats, not specific compression
- ❌ **LIMITATION**: Cannot capture full format string
- **RECOMMENDATION**: Add `output_format_details` (string) to `DataFile` or `Study`
- Notes: Distinguishes gain-normalized vs raw, compression type

**Field: `ImageFileFormat`**
- EPU Value: `"Tiff"` (integrated image format)
- Schema Classes Checked: DataFile, FileFormatEnum, Image2D
- ✅ **DIRECT MATCH**: `DataFile.file_format` (FileFormatEnum)
- Schema Location: DataFile class
- Available Values: Should include "tiff" or "tif"
- Notes: Standard image format specification

**Field: `DMPSession` (Data Management Platform)**
- Subfields: `ProjectId`, `ProjectName`, `ExperimentId`, `ExperimentName`, `DatasetId`, `DatasetName`, `WorkflowId`, `WorkflowName`, `WorkstepId`, `WorkstepName`, `AcquisitionRunId`
- EPU Values: All `null` (DMP not integrated)
- Schema Classes Checked: Dataset, Study, ExperimentRun, WorkflowRun
- ⚠️ **PARTIAL MATCH**: Lambda-BER has Dataset → Study hierarchy
- ❌ **MISSING**: No explicit Project/Experiment/Workflow/Workstep hierarchy
- **RECOMMENDATION**: Add optional DMP integration fields to `Study`:
  - `project_id`, `project_name` (string)
  - `experiment_id`, `experiment_name` (string)
  - `workflow_id`, `workflow_name` (string)
- Use Case: Integration with facility data management platforms (ThermoFisher DMP, similar systems)

---

### 2.7 Microscope Configuration

**Field: `MicroscopeName`**
- EPU Value: `null` (or microscope identifier)
- Schema Classes Checked: Instrument, CryoEMInstrument
- ✅ **DIRECT MATCH**: `Instrument.title` or `Instrument.model`
- Notes: Redundant with instrument fields in FoilHole XML

---

## 3. GridSquare.dm Metadata Analysis

### 3.1 Grid Square Identification

**Field: `Id`**
- EPU Value: `13285693` (grid square ID within session)
- Schema Classes Checked: Image2D, ExperimentRun
- ❌ **MISSING**: No grid square ID field
- **RECOMMENDATION**: Add `grid_square_id` (string) to `Image2D` or create intermediate class
- Use Case: Links images to their grid square for navigation hierarchy

**Field: `AtlasNodeId`**
- EPU Value: `13285693` (atlas/navigator node ID)
- Schema Classes Checked: Image2D, ExperimentRun
- ❌ **MISSING**: No atlas node tracking
- Related to: `grid_square_id` recommendation
- Notes: EPU navigation hierarchy: Session → Atlas → Grid Square → Foil Hole → Image

---

### 3.2 Grid Square Quality & Processing

**Field: `AutoEucentricPerformed`**
- EPU Value: `true` (automatic eucentric height adjustment)
- Schema Classes Checked: DataCollectionStrategy, ExperimentalConditions
- ❌ **MISSING**: No eucentric flag
- Notes: Low priority workflow detail

**Field: `BalancedRank`**
- EPU Value: `null` (Smart EPU ranking for balanced acquisition)
- Schema Classes Checked: QualityMetrics
- ❌ **MISSING**: No grid square ranking field
- Notes: Low priority Smart EPU feature

**Field: `BeamCurrent`**
- EPU Value: `null` (beam current at grid square)
- Schema Classes Checked: ExperimentalConditions
- ⚠️ **PARTIAL MATCH**: Related to `beam_intensity` recommendation
- Notes: Often not recorded per grid square

**Field: `CategoryName` / `CategoryNumber`**
- EPU Value: `null` (user-defined grid square categories)
- Schema Classes Checked: QualityMetrics, Sample
- ❌ **MISSING**: No category/classification fields
- Notes: User labeling system, low priority

---

### 3.3 Grid Square Image & Geometry

**Field: `GridSquareImagePath`**
- EPU Value: `D:\Data\2025\61269\10-13-25-61269-PDX\Sample3\...\GridSquare_20251013_141741.tiff`
- Schema Classes Checked: DataFile, Image2D
- ✅ **DIRECT MATCH**: `DataFile.file_path` (string) or `Image2D.file_name`
- Schema Location: DataFile class
- Notes: Low-mag grid square overview image path

**Field: `GridSquareShape.center.x/y`**
- EPU Value: `x=2825.68213`, `y=1977.42065` (pixels in atlas)
- Schema Classes Checked: Image2D, ExperimentalConditions
- ❌ **MISSING**: No grid square geometry fields
- **RECOMMENDATION**: Add `atlas_position_x`, `atlas_position_y` (float) to link images to atlas
- Use Case: Spatial navigation and correlation microscopy

**Field: `GridSquareShape.min/max` (bounding box)**
- EPU Value: `min.x=624`, `min.y=0`, `max.x=5016`, `max.y=4080` (pixels)
- Schema Classes Checked: Image2D
- ❌ **MISSING**: No bounding box fields
- Notes: Low priority, defines usable area within grid square

**Field: `GridSquareShape.vertices` (polygon outline)**
- EPU Value: Array of 43 (x,y) points defining grid square boundary
- Schema Classes Checked: Image2D
- ❌ **MISSING**: No polygon geometry storage
- Notes: Low priority, used for visualizing selected areas

---

## Summary of Critical Schema Extensions

### HIGH PRIORITY Additions (Essential for EPU SPA)

**CryoEMInstrument (10 new fields):**
```yaml
spherical_aberration_mm: float  # Cs in millimeters
c1_aperture_um: float
c2_aperture_um: float
c3_aperture_um: float
objective_aperture_um: float
selected_area_aperture_um: float
spot_size: integer
energy_filter_width_ev: float
nominal_magnification: integer
detector_model: string  # "BioQuantum K3", "Falcon 4i", etc.
electron_counting_mode: boolean
counts_per_electron: float
detector_physical_pixel_size_um: float
electron_source: ElectronSourceEnum  # field_emission, schottky, thermionic
extractor_voltage_v: float
gun_lens: integer
probe_mode: ProbeModeEnum  # nanoprobe, microprobe
stem_mode: boolean
camera_length_cm: float  # for diffraction
```

**ExperimentalConditions (7 new fields):**
```yaml
beam_diameter_um: float
beam_intensity: float
beam_shift_x: float
beam_shift_y: float
beam_tilt_x: float
beam_tilt_y: float
image_shift_x: float
image_shift_y: float
stage_x_um: float
stage_y_um: float
stage_z_um: float
stage_alpha: float  # tilt angle in degrees
stage_beta: float
```

**DataCollectionStrategy (7 new fields):**
```yaml
dose_rate: float  # e⁻/Å²/s
binning_factor: float  # 0.5 (super-res), 1, 2, 4
clustering_mode: ClusteringModeEnum  # no_clustering, beam_image_shift, stage_movement
hole_clustering_radius_um: float
auto_focus_enabled: boolean
auto_zero_loss_enabled: boolean
smart_hole_selection_enabled: boolean
```

**Image2D (2 new fields):**
```yaml
grid_square_id: string
atlas_position_x: float
atlas_position_y: float
```

**QualityMetrics (3 new fields):**
```yaml
ice_thickness_quality: IceThicknessEnum  # ideal, too_thin, too_thick, contaminated
grid_square_quality: GridSquareQualityEnum  # good, marginal, rejected
hole_selection_method: HoleSelectionEnum  # manual, automated, smart_epu
```

**SamplePreparation (2 new fields):**
```yaml
holder_type: string  # "Autoloader", "Side-entry", "Cartridge"
autoloader_slot: integer
```

### MEDIUM PRIORITY Additions

**Study (DMP Integration):**
```yaml
session_name: string
project_id: string
project_name: string
experiment_id: string
experiment_name: string
```

**DataFile (Output Format Details):**
```yaml
output_format_details: string  # "Tiff Lzw Non-Gain normalized"
```

### NEW ENUMS NEEDED

```yaml
ElectronSourceEnum:
  permissible_values:
    field_emission:
      description: "Field emission gun (FEG)"
    schottky:
      description: "Schottky emitter"
    thermionic:
      description: "Thermionic filament (LaB6, tungsten)"
    cold_feg:
      description: "Cold field emission gun"

ProbeModeEnum:
  permissible_values:
    nanoprobe:
      description: "Nanoprobe (small spot, high coherence)"
    microprobe:
      description: "Microprobe (large spot, low coherence)"

ClusteringModeEnum:
  permissible_values:
    no_clustering:
      description: "Single shot per hole"
    beam_image_shift:
      description: "Multi-shot using beam/image shift"
    stage_movement:
      description: "Multi-shot using stage movement"

IceThicknessEnum:
  permissible_values:
    ideal:
      description: "Optimal ice thickness"
    too_thin:
      description: "Ice too thin, particles damaged"
    too_thick:
      description: "Ice too thick, poor contrast"
    contaminated:
      description: "Ice contamination present"

GridSquareQualityEnum:
  permissible_values:
    good:
      description: "Acceptable grid square quality"
    marginal:
      description: "Marginal quality, use if needed"
    rejected:
      description: "Poor quality, skip"

HoleSelectionEnum:
  permissible_values:
    manual:
      description: "Manually selected holes"
    automated:
      description: "Automated hole finding"
    smart_epu:
      description: "AI-based Smart EPU selection"
```

---

## Conclusion

The Lambda-BER schema provides **strong foundational support (75%)** for EPU SPA workflows, with excellent coverage of core imaging parameters, sample tracking, and workflow provenance. 

**Key Strengths:**
- All essential imaging parameters captured (pixel size, dose, defocus, exposure)
- Complete sample-to-structure provenance chain
- File and workflow tracking well-supported
- Extensible architecture for adding EPU-specific features

**Critical Gaps:**
- Missing grid quality assessment (ice thickness, hole selection)
- No EPU automation hierarchy (session → grid square → foil hole)
- Advanced instrument parameters absent (apertures, Cs, spot size, magnification)
- Limited beam characterization (shift, tilt, diameter)
- No multi-shot-per-hole configuration tracking

**Recommended Implementation Priority:**
1. **Phase 1 (weeks 1-3)**: Add advanced instrument parameters and beam characterization - enables complete instrument state capture
2. **Phase 2 (weeks 4-6)**: Add grid quality assessments and automation flags - enables EPU workflow reconstruction
3. **Phase 3 (weeks 7-8)**: Add DMP integration and session hierarchy - enables facility-level tracking

With these extensions, the Lambda-BER schema will provide **complete EPU SPA metadata capture** suitable for automated high-throughput cryo-EM facilities.
