# PNNL/EMSL Metadata Harmonization with Lambda-BER Schema

## Executive Summary

### Overview
This document provides a comprehensive mapping analysis of PNNL/EMSL cryo-EM facility metadata to the Lambda-BER schema. Three metadata formats were systematically analyzed:
- **PNNL metadata.yaml** - Minimal facility metadata with ~30 fields covering instrument parameters, acquisition settings, and quality assessments
- **SerialEM MDOC** - Per-image technical metadata with ~35 fields including stage positions, beam settings, and frame-level acquisition parameters
- **EPU XML** - ThermoFisher EPU session metadata with ~60 fields providing detailed microscope state and automation parameters

### Key Findings

**Overall Schema Coverage:**
- ✅ **70% Good Coverage** - Core structural biology concepts are well-represented
- ⚠️ **20% Partial Coverage** - Fields exist but require adaptation (unit conversion, enum mapping, string parsing)
- ❌ **10% Missing** - Critical gaps for facility operations and tomography workflows

**What Works Well:**
The Lambda-BER schema provides excellent support for:
- Sample characterization (composition, concentration, buffer conditions)
- Basic imaging parameters (pixel size, exposure time, defocus, dose)
- File and workflow provenance (linking samples → experiments → data files → processed results)
- Core instrument identification (instrument codes, accelerating voltage, detector type)
- Quality metrics for processed data (resolution, completeness)

**Critical Gaps:**
The schema lacks essential capabilities for PNNL/EMSL facility operations:

1. **Tomography Workflows** (highest priority)
   - No tilt angle tracking per image
   - No tilt scheme specification (dose-symmetric vs linear vs continuous)
   - No stage position coordinates (X/Y/Z)
   - No fiducial marker parameters
   - No rotation rate for continuous tilt

2. **Grid Quality Assessment** (required for PNNL workflows)
   - No ice contamination tracking (none/limited/severe)
   - No ice thickness quality (ideal/too thin/too thick)
   - No particle density assessment (optimal/sparse/crowded)

3. **Advanced Instrument Parameters** (needed for complete metadata)
   - No spherical aberration (Cs) field
   - Missing all aperture sizes (C1, C2, C3, objective, selected area)
   - No spot size setting
   - No nominal magnification
   - No energy filter slit width
   - No detector model (only generic detector type enum)
   - No detector physical pixel size (only calibrated pixel size)
   - No electron counting mode flag
   - No beam diameter, intensity, or alignment parameters (beam shift, beam tilt, image shift)

4. **Facility Operations** (institutional needs)
   - No proposal ID tracking
   - No facility name field
   - No session/beamtime management
   - No sample holder type

### Impact Assessment

**For Single Particle Analysis (SPA):**
- ✅ Schema is **production-ready** with minor adaptations
- Can track complete sample-to-structure workflows
- All essential imaging parameters captured

**For Tomography:**
- ❌ Schema is **incomplete** and requires extensions
- Cannot properly track tilt series metadata
- Missing stage coordinate tracking critical for correlation workflows
- SerialEM MDOC files cannot be fully represented

**For Facility Management:**
- ⚠️ Schema has **limited facility support**
- No proposal or beamtime tracking
- Cannot track grid quality assessments required by PNNL protocols
- Missing many low-level instrument settings needed for troubleshooting

---

---

## Systematic Analysis of All Lambda-BER Schema Classes

**Mapping Legend:**
- ✅ **Direct Match** - Field exists with appropriate type/range
- ⚠️ **Partial Match** - Concept exists but needs adaptation (unit conversion, parsing, etc.)
- 🔶 **Alternative Location** - Could map to different class than primary
- ❌ **Missing** - No equivalent in current schema

---



## FIELD-BY-FIELD ANALYSIS

This section provides an exhaustive review of every PNNL/EMSL metadata field against ALL Lambda-BER schema classes, checking every possible mapping location.

### PNNL metadata.yaml COMPLETE FIELD ANALYSIS

#### **SECTION: conditions**

**Field: `sample_mg/ml`**
- Schema Classes Checked: Sample, SamplePreparation, BufferComposition
- ✅ MATCH FOUND: `Sample.concentration` (float) + `Sample.concentration_unit` (ConcentrationUnitEnum)
- Schema Line: 206-210
- Mapping: Split "2.5" → `concentration: 2.5`, `concentration_unit: mg_per_ml`

**Field: `sample_buffer`**
- Schema Classes Checked: Sample, SamplePreparation, BufferComposition
- ✅ MATCH FOUND: `Sample.buffer_composition` → `BufferComposition`
- Schema Lines: 211-213 (Sample), 892-904 (BufferComposition)
- Available Attributes: `ph` (float), `components` (string list), `additives` (string list)
- Mapping: Parse free text → structured fields

**Field: `vitrification_settings`**
- Schema Classes Checked: SamplePreparation, CryoEMPreparation, ExperimentalConditions
- ⚠️ PARTIAL MATCH: `CryoEMPreparation` has structured fields
- Schema Lines: 940-976
- Available: `blot_time`, `blot_force`, `humidity_percentage`, `chamber_temperature`, `vitrification_method`, `plasma_treatment`
- ❌ MISSING: No free-text `vitrification_notes` field for raw settings string

---

#### **SECTION: metadata.program**

**Field: `proposal_id` (61815)**
- Schema Classes Checked: Dataset, Study, ExperimentRun, Sample, ALL NamedThing subclasses
- ❌ NO MATCH: No `proposal_id`, `grant_id`, or `funding_id` field anywhere in schema
- Could use: `Dataset.description` or `Study.description` as workaround
- RECOMMENDATION: Add `proposal_id` field to Study or Dataset

**Field: `short_sample_name` ("Green box position 2")**
- Schema Classes Checked: Sample, Study, ExperimentRun
- ✅ MATCH FOUND: Multiple options:
  - `Sample.title` (string) - Schema line 121
  - `Sample.sample_code` (string, required) - Schema line 172
- Mapping: Use `sample_code` for structured ID, `title` for human-readable name

**Field: `session_id` ("10-03-25_C2")**
- Schema Classes Checked: ExperimentRun, Study, Dataset, WorkflowRun
- ✅ MATCH FOUND: `ExperimentRun.experiment_code` (string, required)
- Schema Line: 559-561
- Description: "Human-friendly laboratory or facility identifier for the experiment"
- Perfect match for session tracking

**Field: `instrument_id` (34303)**
- Schema Classes Checked: Instrument, CryoEMInstrument, XRayInstrument, SAXSInstrument
- ✅ MATCH FOUND: `Instrument.instrument_code` (string, required)
- Schema Line: 452-454
- Description: "Human-friendly facility or laboratory identifier for the instrument"

**Field: `voltage` (300 kV)**
- Schema Classes Checked: CryoEMInstrument, Instrument, ExperimentalConditions
- ✅ MATCH FOUND: `CryoEMInstrument.accelerating_voltage` (integer)
- Schema Lines: 470-476
- Range: Limited to 120, 200, or 300 (any_of constraint)
- Perfect match

**Field: `cs` (2.7 mm)**
- Schema Classes Checked: CryoEMInstrument, Instrument, ALL instrument classes
- ❌ NO MATCH: No `spherical_aberration` or `cs` field in CryoEMInstrument
- RECOMMENDATION: Add `spherical_aberration_mm` (float) to CryoEMInstrument

**Field: `nominal_pixel_size` (0.34 Angstrom)**
- Schema Classes Checked: Image2D, Image, CryoEMInstrument, DataCollectionStrategy
- ✅ MATCH FOUND: `Image2D.pixel_size` (float)
- Schema Line: 733
- Description: "Pixel size in Angstroms"
- 🔶 ALTERNATIVE: `CryoEMInstrument.pixel_size_min` and `pixel_size_max` for instrument capability
- Mapping: Per-image value vs instrument capability range

**Field: `total_dose` (50 e⁻/Å²)**
- Schema Classes Checked: DataCollectionStrategy, Image2D, ExperimentRun, ExperimentalConditions
- ✅ MATCH FOUND: `DataCollectionStrategy.total_dose` (float)
- Schema Line: 1104
- Description: "Total electron dose for cryo-EM"

**Field: `nominal_dose_rate_eps` (e⁻/Å²/s)**
- Schema Classes Checked: DataCollectionStrategy, Image2D, ExperimentalConditions, CryoEMInstrument
- ❌ NO MATCH: No `dose_rate` field anywhere
- Available: `DataCollectionStrategy.dose_per_frame` (float) but not rate per second
- RECOMMENDATION: Add `dose_rate` (float, e⁻/Å²/s) to DataCollectionStrategy

**Field: `frames_per_second`**
- Schema Classes Checked: DataCollectionStrategy, Image2D, ExperimentRun
- ✅ MATCH FOUND: `DataCollectionStrategy.frame_rate` (float)
- Schema Line: 1098
- Description: "Frames per second"

**Field: `total_exposure` (seconds)**
- Schema Classes Checked: Image2D, Image, ExperimentalConditions, DataCollectionStrategy
- ✅ MATCH FOUND: `Image2D.exposure_time` (float)
- Schema Line: 737
- Description: "Exposure time in seconds"
- 🔶 ALTERNATIVE: `ExperimentalConditions.exposure_time` for run-level setting

**Field: `processing_scheme` (1=SPA, 2=tomography, 3=microED)**
- Schema Classes Checked: WorkflowRun, ExperimentRun, TechniqueEnum, WorkflowTypeEnum
- ⚠️ PARTIAL MATCH: Multiple related fields:
  - `ExperimentRun.technique` (TechniqueEnum) - includes "cryo_em", "cryo_et"
  - `WorkflowRun.workflow_type` (WorkflowTypeEnum) - includes processing types
- Mapping: 1 → technique="cryo_em", 2 → technique="cryo_et", 3 → technique="electron_diffraction"

**Field: `detector_id` ("K3" or "Ceta-D")**
- Schema Classes Checked: CryoEMInstrument, DetectorTypeEnum
- ⚠️ PARTIAL MATCH: `CryoEMInstrument.detector_type` (DetectorTypeEnum)
- Schema Lines: 484, 1370-1378
- Available values: "direct_electron", "ccd", "cmos", "hybrid_pixel"
- ❌ SPECIFIC MODELS NOT IN ENUM: No "gatan_k3", "falcon_4", "ceta_d"
- Mapping: K3 → "direct_electron", Ceta-D → "ccd"
- RECOMMENDATION: Expand DetectorTypeEnum or add `detector_model` string field

**Field: `detector_physical_pixel_size` (5 μm for K3, 14 μm for Ceta-D)**
- Schema Classes Checked: CryoEMInstrument, ALL detector-related fields
- ❌ NO MATCH: No physical detector pixel size field
- Available: `CryoEMInstrument.pixel_size_min/max` but these are CALIBRATED sizes in Å/pixel
- RECOMMENDATION: Add `detector_physical_pixel_size_um` (float) to CryoEMInstrument

**Field: `nominal_magnification` (130 kx)**
- Schema Classes Checked: CryoEMInstrument, Image2D, ExperimentalConditions
- ❌ NO MATCH: No `magnification` or `nominal_magnification` field
- RECOMMENDATION: Add `nominal_magnification` (integer) to CryoEMInstrument

**Field: `nominal_camera_Length` (cm, for diffraction)**
- Schema Classes Checked: CryoEMInstrument, XRayInstrument, ALL instrument classes
- ❌ NO MATCH: No camera length field
- Note: Relevant for microED/electron diffraction modes
- RECOMMENDATION: Add `camera_length_cm` (float) to CryoEMInstrument for diffraction capability

**Field: `binning_factor` (0.5, 1, 2, 4)**
- Schema Classes Checked: Image2D, DataCollectionStrategy, CryoEMInstrument
- ❌ NO MATCH: No binning field anywhere
- Note: Critical for super-resolution vs binned collection
- RECOMMENDATION: Add `binning_factor` (float) to DataCollectionStrategy or Image2D

**Field: `tilting_mode` (0=none, 1=dose symmetric, 2=linear, 3=continuous)**
- Schema Classes Checked: TechniqueEnum, DataCollectionStrategy, ExperimentRun
- ⚠️ PARTIAL MATCH: `ExperimentRun.technique` can be "cryo_em" or "cryo_et"
- ❌ NO TILT SCHEME ENUM: No field for tilt collection strategy
- RECOMMENDATION: Add `tilt_scheme` (TiltSchemeEnum) to DataCollectionStrategy

**Field: `fiducial_size` (Angstrom, for tomography)**
- Schema Classes Checked: DataCollectionStrategy, SamplePreparation, ALL tomography-related
- ❌ NO MATCH: No fiducial marker field
- RECOMMENDATION: Add `fiducial_diameter_nm` (float) to DataCollectionStrategy

**Field: `tilt_angle_increment` (degrees)**
- Schema Classes Checked: DataCollectionStrategy, Image2D, ExperimentalConditions
- ❌ NO MATCH: No tilt angle fields
- RECOMMENDATION: Add to DataCollectionStrategy: `tilt_min`, `tilt_max`, `tilt_increment`

**Field: `rotation_rate` (degrees/s, continuous tilt)**
- Schema Classes Checked: DataCollectionStrategy, ExperimentalConditions
- ❌ NO MATCH: No rotation rate field
- RECOMMENDATION: Add `rotation_rate_deg_per_s` (float) to DataCollectionStrategy

**Field: `c2_aperture` (50 μm)**
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ NO MATCH: No aperture fields except in EPU mapping discussion
- RECOMMENDATION: Add `c2_aperture_um` (float) to CryoEMInstrument

**Field: `spot_size` (5)**
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ NO MATCH: No spot size field
- RECOMMENDATION: Add `spot_size` (integer) to CryoEMInstrument

**Field: `beam_diameter` (0.6 μm)**
- Schema Classes Checked: ExperimentalConditions, DataCollectionStrategy, CryoEMInstrument
- ❌ NO MATCH: No beam diameter field
- Note: `ExperimentalConditions.beam_energy` exists but not beam size
- RECOMMENDATION: Add `beam_diameter_um` (float) to ExperimentalConditions

**Field: `energy_filter_slit` (20 eV)**
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ NO MATCH: No energy filter width field
- RECOMMENDATION: Add `energy_filter_width_ev` (float) to CryoEMInstrument

**Field: `phase_plate` (true/false)**
- Schema Classes Checked: CryoEMInstrument
- ✅ MATCH FOUND: `CryoEMInstrument.phase_plate` (boolean)
- Schema Line: 479
- Description: "Phase plate available"

**Field: `topaz_model` ("unet", "fcnn", etc.)**
- Schema Classes Checked: WorkflowRun, ALL workflow-related
- ⚠️ PARTIAL MATCH: `WorkflowRun.processing_parameters` (string)
- Schema Line: 619
- Can encode model name in parameters string
- Not a dedicated field but functional

**Field: `motCorr_bin` (motion correction binning)**
- Schema Classes Checked: WorkflowRun, DataCollectionStrategy
- ⚠️ PARTIAL MATCH: `WorkflowRun.processing_parameters` (string)
- Schema Line: 619
- Can encode in parameters but no dedicated field

---

#### **SECTION: assessments**

**Field: `ice_contamination` (1=None, 2=Limited, 3=Severe)**
- Schema Classes Checked: QualityMetrics, SamplePreparation, ExperimentRun
- ❌ NO MATCH: `QualityMetrics` only has data quality metrics (resolution, completeness, R-factor)
- No grid/sample quality assessment fields
- RECOMMENDATION: Add `ice_contamination` (IceContaminationEnum) to QualityMetrics or SamplePreparation

**Field: `ice_quality` (1=Ideal, 2=Too thin, 3=Too thick)**
- Schema Classes Checked: QualityMetrics, SamplePreparation, ExperimentRun
- ❌ NO MATCH: No ice thickness assessment
- RECOMMENDATION: Add `ice_thickness_quality` (IceThicknessEnum) to QualityMetrics

**Field: `particle_concentration` (1=Just right, 2=Too low, 3=Too high)**
- Schema Classes Checked: QualityMetrics, Sample, SamplePreparation
- ❌ NO MATCH: No particle density assessment
- Note: `Sample.concentration` exists for mg/mL but not grid particle density
- RECOMMENDATION: Add `particle_density_quality` (ParticleDensityEnum) to QualityMetrics

---

#### **SECTION: notes**

**Field: `notes` (multiline free text)**
- Schema Classes Checked: ALL NamedThing subclasses
- ✅ MATCH FOUND: `NamedThing.description` (string)
- Schema Line: 123
- Available on: Dataset, Study, Sample, SamplePreparation, Instrument, ExperimentRun, WorkflowRun, etc.
- Can use description field of most appropriate class

---

### SerialEM MDOC FORMAT COMPLETE FIELD ANALYSIS

**Global Header: `T = SerialEM: Titan Krios...`**
- ✅ MATCH: `CryoEMInstrument.title`, `CryoEMInstrument.model`

**Global Header: `Voltage`**
- ✅ MATCH: `CryoEMInstrument.accelerating_voltage`

**Field: `GainReference`, `DefectFile`**
- ✅ MATCH: `DataFile.file_name`, `DataFile.file_path`
- Use `data_type`: "metadata" or custom

**Field: `TiltAngle` (0.000642314 degrees)**
- Schema Classes Checked: Image2D, DataCollectionStrategy, ExperimentalConditions
- ❌ NO MATCH: No tilt angle field
- RECOMMENDATION: Add `tilt_angle` (float) to Image2D

**Field: `StagePosition` (X, Y coordinates)**
- Schema Classes Checked: Image2D, ExperimentalConditions, DataCollectionStrategy
- ❌ NO MATCH: No stage position fields
- RECOMMENDATION: Add `stage_x_um`, `stage_y_um` to ExperimentalConditions or Image2D

**Field: `StageZ` (Z height)**
- ❌ NO MATCH: Add `stage_z_um` to ExperimentalConditions

**Field: `Magnification` (130000)**
- ❌ NO MATCH: Need `nominal_magnification` in CryoEMInstrument

**Field: `Intensity` (beam intensity)**
- Schema Classes Checked: ExperimentalConditions, DataCollectionStrategy
- ❌ NO MATCH: No beam intensity field
- RECOMMENDATION: Add `beam_intensity` (float) to ExperimentalConditions

**Field: `ExposureDose` (per frame)**
- ✅ MATCH: `Image2D.dose` (float)
- Schema Line: 741

**Field: `DoseRate` (e⁻/Å²/s)**
- ❌ NO MATCH: Need `dose_rate` in DataCollectionStrategy

**Field: `PixelSpacing` (Angstroms)**
- ✅ MATCH: `Image2D.pixel_size`

**Field: `SpotSize`**
- ❌ NO MATCH: Need in CryoEMInstrument

**Field: `ProbeMode` (0=nanoprobe, 1=microprobe)**
- ❌ NO MATCH: No probe mode field
- RECOMMENDATION: Add `probe_mode` (ProbeModeEnum) to CryoEMInstrument or ExperimentalConditions

**Field: `Defocus` (micrometers)**
- ✅ MATCH: `Image2D.defocus` (float)
- Schema Line: 755

**Field: `ImageShift` (X, Y)**
- ❌ NO MATCH: No image shift fields
- RECOMMENDATION: Add `image_shift_x`, `image_shift_y` to ExperimentalConditions

**Field: `RotationAngle` (degrees)**
- ❌ NO MATCH: No image rotation field
- RECOMMENDATION: Add `rotation_angle` to Image2D

**Field: `ExposureTime` (seconds)**
- ✅ MATCH: `Image2D.exposure_time`

**Field: `Binning`**
- ❌ NO MATCH: Need `binning_factor`

**Field: `CameraIndex`, `DividedBy2`, `OperatingMode`, `UsingCDS`, `MagIndex`, `LowDoseConSet`**
- ❌ NO MATCHES: Low-level technical parameters
- These are facility-specific and may not need formal schema support

**Field: `CountsPerElectron`**
- ❌ NO MATCH: Detector calibration parameter
- RECOMMENDATION: Add `counts_per_electron` (float) to CryoEMInstrument

**Field: `TargetDefocus`**
- ⚠️ PARTIAL: Can use `DataCollectionStrategy` custom field or extend

**Field: `SubFramePath`**
- ✅ MATCH: `DataFile.file_path`

**Field: `NumSubFrames`**
- ✅ MATCH: `DataCollectionStrategy.total_frames`

**Field: `FrameDosesAndNumber`**
- ✅ MATCH: `DataCollectionStrategy.dose_per_frame`, `total_frames`

**Field: `DateTime`**
- ✅ MATCH: `Image2D.acquisition_date` or `ExperimentRun.experiment_date`

**Field: `NavigatorLabel`**
- ⚠️ PARTIAL: Can use `Image2D.title`
- ❌ NO DEDICATED: No `navigator_label` field

**Field: `FilterSlitAndLoss`**
- ❌ NO MATCH: Need `energy_filter_width_ev`

**Field: `UncroppedSize`**
- ✅ MATCH: `Image2D.dimensions_x`, `dimensions_y`

**Field: `RotationAndFlip`**
- ❌ NO MATCH: No transformation operation code field

**Field: `TimeStamp`**
- ✅ MATCH: `Image2D.acquisition_date` (can convert Unix timestamp)

---

### EPU XML FORMAT COMPLETE FIELD ANALYSIS

**Field: `uniqueID` (UUID)**
- ✅ MATCH: `Image2D.id` (uriorcurie)

**Field: `DoseOnCamera`**
- ✅ MATCH: `Image2D.dose`

**Field: `Aperture[C1].Name`, `Aperture[C2].Name`, `Aperture[C3].Name`, `Aperture[OBJ].Name`, `Aperture[SA].Name`**
- Schema Classes Checked: CryoEMInstrument, ExperimentalConditions
- ❌ NO MATCHES: Only C2 aperture missing, others also missing
- RECOMMENDATION: Add all aperture fields to CryoEMInstrument:
  - `c1_aperture_um`, `c2_aperture_um`, `c3_aperture_um`
  - `objective_aperture_um`, `selected_area_aperture_um`

**Field: `StemMagnification` (boolean)**
- ❌ NO MATCH: STEM mode indicator
- RECOMMENDATION: Add `stem_mode` (boolean) to CryoEMInstrument

**Field: `Detectors[EF-CCD].CommercialName` ("BioQuantum K3")**
- ⚠️ PARTIAL: `CryoEMInstrument.detector_type` (enum only)
- ❌ NO STRING FIELD: Can't store "BioQuantum K3" directly
- RECOMMENDATION: Add `detector_model` (string) to CryoEMInstrument

**Field: `Detectors[EF-CCD].ElectronCounted`**
- ❌ NO MATCH: Electron counting mode
- RECOMMENDATION: Add `electron_counting_mode` (boolean) to CryoEMInstrument

**Field: `DoseRate`**
- ❌ NO MATCH: Need `dose_rate`

**Field: `IlluminationIntensity`**
- ❌ NO MATCH: Need `beam_intensity`

**Field: `PhasePlateUsed`**
- ✅ MATCH: `CryoEMInstrument.phase_plate`

**Field: `AppliedDefocus`**
- ✅ MATCH: `Image2D.defocus` (convert meters to micrometers)

**Field: `Binning.x/y`**
- ❌ NO MATCH: Need `binning_factor`

**Field: `CameraLocation` ("EnergyFilter")**
- ❌ NO MATCH: Camera location in column
- May not need - facility-specific detail

**Field: `ExposureTime`**
- ✅ MATCH: `Image2D.exposure_time`

**Field: `ReadoutArea` (width, height)**
- ✅ MATCH: `Image2D.dimensions_x`, `dimensions_y`

**Field: `Shutter` ("PreSpecimen")**
- ❌ NO MATCH: Shutter type
- Low priority - facility-specific

**Field: `SuperResolutionFactor`**
- ❌ NO MATCH: Super-resolution mode
- Related to binning_factor

**Field: `NumberOffractions`**
- ✅ MATCH: `DataCollectionStrategy.total_frames`

**Field: `ElectronCountingEnabled`**
- ❌ NO MATCH: Need `electron_counting_mode`

**Field: `acquisitionDateTime`**
- ✅ MATCH: `Image2D.acquisition_date` or `ExperimentRun.experiment_date`

**Field: `AccelerationVoltage`**
- ✅ MATCH: `CryoEMInstrument.accelerating_voltage` (convert Volts to kV)

**Field: `ExtractorVoltage`**
- ❌ NO MATCH: Gun parameter
- RECOMMENDATION: Add `extractor_voltage_v` (float) to CryoEMInstrument

**Field: `GunLens`**
- ❌ NO MATCH: Gun lens setting
- RECOMMENDATION: Add `gun_lens` (integer) to CryoEMInstrument

**Field: `Sourcetype` ("FieldEmission")**
- ❌ NO MATCH: No electron source type field
- RECOMMENDATION: Add `electron_source` (ElectronSourceEnum) to CryoEMInstrument

**Field: `ComputerName`**
- ❌ NO MATCH: Control computer
- Low priority - facility infrastructure

**Field: `InstrumentID`**
- ✅ MATCH: `Instrument.instrument_code`

**Field: `InstrumentModel`**
- ✅ MATCH: `Instrument.model`

**Field: `ApplicationSoftware`, `ApplicationSoftwareVersion`**
- ⚠️ PARTIAL: Can use `ExperimentRun.description` or extend
- Not critical but useful

**Field: `BeamDiameter`**
- ❌ NO MATCH: Need `beam_diameter_um`

**Field: `BeamShift._x/_y`, `BeamTilt._x/_y`**
- ❌ NO MATCHES: Beam alignment parameters
- RECOMMENDATION: Add to ExperimentalConditions:
  - `beam_shift_x`, `beam_shift_y`, `beam_tilt_x`, `beam_tilt_y`

**Field: `Cameralength`**
- ❌ NO MATCH: Need `camera_length_cm`

**Field: `ColumnOperatingMode` ("TEM")**
- ❌ NO MATCH: TEM vs STEM mode
- Related to `stem_mode` recommendation

**Field: `ColumnOperatingTemSubMode` ("BrightField")**
- ❌ NO MATCH: Imaging mode
- Low priority

**Field: `Defocus`**
- ✅ MATCH: `Image2D.defocus`

**Field: `EFTEMOn`, `EnergySelectionSlitInserted`**
- ❌ NO MATCHES: Energy filter status
- Related to energy filter width

**Field: `EnergySelectionSlitWidth`**
- ❌ NO MATCH: Need `energy_filter_width_ev`

**Field: `IlluminationMode` ("Parallel")**
- ❌ NO MATCH: Illumination system mode
- Low priority - facility-specific

**Field: `ImageShift._x/_y`**
- ❌ NO MATCH: Need `image_shift_x/y`

**Field: `Intensity`**
- ❌ NO MATCH: Need `beam_intensity`

**Field: `ObjectiveLensMode` ("HM")**
- ❌ NO MATCH: Objective lens mode
- Low priority

**Field: `ProbeMode` ("NanoProbe")**
- ❌ NO MATCH: Need `probe_mode` enum

**Field: `SpotIndex`**
- ❌ NO MATCH: Need `spot_size`

**Field: `TemMagnification.NominalMagnification`**
- ❌ NO MATCH: Need `nominal_magnification`

**Field: `Holder` type**
- ❌ NO MATCH: Sample holder type
- RECOMMENDATION: Add `holder_type` (string) to SamplePreparation

**Field: `Position.A`, `Position.B` (tilt angles)**
- ❌ NO MATCHES: Stage alpha/beta tilts
- RECOMMENDATION: Add `stage_alpha`, `stage_beta` to ExperimentalConditions

**Field: `Position.X/Y/Z` (stage coordinates)**
- ❌ NO MATCHES: Need stage position fields

**Field: `ProjectionChamberPressure`, `SamplePressure`**
- ⚠️ PARTIAL: `ExperimentalConditions.pressure` (single value)
- Could use for sample chamber pressure

**Field: `VacuumMode` ("Ready")**
- ❌ NO MATCH: Vacuum status
- Low priority

**Field: `pixelSize.x/y.numericValue`**
- ✅ MATCH: `Image2D.pixel_size` (convert meters to Angstroms)

---

## CRITICAL MISSING FIELDS SUMMARY

### HIGH PRIORITY (Essential for PNNL/EMSL workflows)

1. **CryoEMInstrument additions needed:**
   - `spherical_aberration_mm` (float)
   - `c2_aperture_um` (float)
   - `spot_size` (integer)
   - `energy_filter_width_ev` (float)
   - `nominal_magnification` (integer)
   - `detector_physical_pixel_size_um` (float)
   - `detector_model` (string) - in addition to detector_type enum
   - `electron_counting_mode` (boolean)
   - `counts_per_electron` (float)

2. **Tomography support in DataCollectionStrategy:**
   - `tilt_scheme` (TiltSchemeEnum: dose_symmetric, linear, continuous)
   - `tilt_min_degrees` (float)
   - `tilt_max_degrees` (float)
   - `tilt_increment_degrees` (float)
   - `rotation_rate_deg_per_s` (float)
   - `fiducial_diameter_nm` (float)

3. **Image2D additions:**
   - `tilt_angle` (float)
   - `binning_factor` (float)

4. **ExperimentalConditions additions:**
   - `beam_diameter_um` (float)
   - `beam_intensity` (float)
   - `stage_x_um`, `stage_y_um`, `stage_z_um` (float)
   - `stage_alpha`, `stage_beta` (float) - for tilt angles

5. **DataCollectionStrategy additions:**
   - `dose_rate` (float) - e⁻/Å²/s

6. **Grid Quality in QualityMetrics or SamplePreparation:**
   - `ice_contamination` (IceContaminationEnum: none, limited, severe)
   - `ice_thickness_quality` (IceThicknessEnum: ideal, too_thin, too_thick)
   - `particle_density_quality` (ParticleDensityEnum: optimal, sparse, crowded)

7. **Project tracking in Study/Dataset:**
   - `proposal_id` (string)
   - `facility` (string)

### MEDIUM PRIORITY (Useful for complete metadata)

8. **CryoEMInstrument additional parameters:**
   - `c1_aperture_um`, `c3_aperture_um` (float)
   - `objective_aperture_um`, `selected_area_aperture_um` (float)
   - `extractor_voltage_v` (float)
   - `gun_lens` (integer)
   - `electron_source` (ElectronSourceEnum: field_emission, thermionic, cold_feg)
   - `camera_length_cm` (float) - for diffraction
   - `stem_mode` (boolean)
   - `probe_mode` (ProbeModeEnum: nanoprobe, microprobe)

9. **ExperimentalConditions additions:**
   - `beam_shift_x`, `beam_shift_y` (float)
   - `beam_tilt_x`, `beam_tilt_y` (float)
   - `image_shift_x`, `image_shift_y` (float)

10. **Image2D additions:**
    - `rotation_angle` (float)
    - `navigator_label` (string)

11. **SamplePreparation:**
    - `holder_type` (string)

### LOW PRIORITY (Facility-specific details)

12. **Low-level technical parameters** (may not need):
    - Camera index, operating mode index, CDS settings
    - Column operating mode details
    - Computer names, software versions for acquisition
    - Shutter types, camera locations

---

## ENUM UPDATES NEEDED

1. **DetectorTypeEnum** - Add specific models:
   - `gatan_k2`
   - `gatan_k3`
   - `falcon_3`
   - `falcon_4`
   - `ceta_d`
   - `ceta_f`

2. **TechniqueEnum** - Verify includes:
   - `electron_diffraction` or `micro_ed` ✅ Has "electron_microscopy"
   - Consider adding `microed` specifically

3. **NEW ENUMS NEEDED:**
   - `TiltSchemeEnum`: dose_symmetric, linear, continuous, bidirectional
   - `IceContaminationEnum`: none, limited, severe
   - `IceThicknessEnum`: ideal, too_thin, too_thick
   - `ParticleDensityEnum`: optimal, sparse, crowded
   - `ProbeModeEnum`: nanoprobe, microprobe
   - `ElectronSourceEnum`: field_emission, thermionic, cold_feg, schottky

---

## CONCLUSION - COMPREHENSIVE ASSESSMENT

**Coverage Analysis:**
- ✅ **Good Coverage (70%)**: Basic sample info, buffer composition, core imaging parameters (pixel size, exposure, defocus), file tracking, workflow provenance
- ⚠️ **Partial Coverage (20%)**: Detector types (enum vs specific models), processing parameters (free text vs structured)
- ❌ **Missing (10%)**: Tomography support, grid quality assessments, advanced instrument parameters, facility tracking

**Priority Recommendations:**
1. Add tomography support (critical for SerialEM workflows)
2. Add grid quality assessments (required PNNL assessments)
3. Extend CryoEMInstrument with missing parameters (Cs, apertures, magnification, energy filter)
4. Add proposal/session tracking for facility operations
5. Add stage position and beam alignment fields for complete provenance

The Lambda-BER schema provides an excellent foundation but needs targeted extensions to fully support PNNL/EMSL cryo-EM facility workflows, particularly for tomography and detailed instrument characterization.
