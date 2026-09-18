# Schema gap analysis: SerialEM mdoc fields vs lambda-ber-schema

Systematic comparison of every metadata field in the SerialEM mdoc format against the
lambda-ber-schema LinkML schema (`src/lambda_ber_schema/schema/lambda_ber_schema.yaml`).

Coverage values:
- **Full** — schema has a direct slot that maps to this field with equivalent semantics
- **Partial** — schema has related slots but with narrowed scope, wrong level (session vs per-image), or encoding mismatch
- **Missing** — no schema slot captures this field

For field presence across mdoc types see `mdoc_field_comparison.md`.

---

## Field inventory

### Provenance & Context

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `Version` | `mmm1.mrc.mdoc` | Partial | `ExperimentRun.acquisition_software_version` | Schema has a free string; mdoc writes a full build string like `"SerialEM Version 4.2.2 64-bit, built Jun 2 2025 21:45:10"` requiring regex parse to extract the version number | Document parsing convention in loader (e.g. `r"SerialEM Version ([0-9.]+)"`) |
| `DateTime` | `frames/Image_000.tif.mdoc` | Partial | `ExperimentRun.experiment_date` (session-level); `Image.acquisition_date` (per-image string, on base class); `Movie.timestamp` (per-frame string) | mdoc writes per-image DateTime in every block. `Image.acquisition_date` exists on the base class and covers all image types. `Movie.timestamp` also carries this. Session date on `ExperimentRun.experiment_date`. Good coverage but three overlapping slots — needs loader convention for which to populate. | Document loader convention: map mdoc `DateTime` → `Image.acquisition_date` for all image types; `Movie.timestamp` for movies if finer granularity needed |
| `TimeStamp` | `frames/Image_000.tif.mdoc` | Missing | — | Unix epoch integer per image; finer resolution than DateTime; useful for precise interval analysis | Add `unix_timestamp` integer slot to base `Image` class |
| `NavigatorLabel` | `mmm1.mrc.mdoc` | Missing | — | Cross-reference to `[Item = N]` in the `.nav` file; essential provenance linking each image back to its acquisition target | Add `navigator_label` string slot to base `Image` class |
| `ImageFile` | `mmm1.mrc.mdoc` | Full | `DataFile.file_name` | Header-level field pointing to associated MRC; direct mapping | — |

### Optics

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `Voltage` | `C5_LMM_1.mrc.mdoc` | Full | `CryoEMInstrument.accelerating_voltage` | Instrument-level; consistent across session | — |
| `Magnification` | `C5_LMM_1.mrc.mdoc` | Full | `ExperimentRun.magnification` | Direct mapping | — |
| `MagIndex` | `C5_LMM_1.mrc.mdoc` | Missing | — | SerialEM internal magnification LUT index (integer); no standard scientific meaning outside SerialEM | Low priority; no schema equivalent needed |
| `PixelSpacing` | `C5_LMM_1.mrc.mdoc` | Full | `ExperimentRun.calibrated_pixel_size`; also `Image.pixel_size` (per-image slot on base class) and `DataCollectionStrategy.pixel_size_calibrated` | mdoc writes PixelSpacing per block (it repeats the session value for each tile). Session-level: `ExperimentRun.calibrated_pixel_size`. Per-image: `Image.pixel_size`. Both valid targets. | — |
| `FilterSlitAndLoss` | `C5_LMM_1.mrc.mdoc` | Partial | `CryoEMInstrument.energy_filter_slit_width` | Schema has slit width on the instrument class; mdoc writes both slit width AND energy loss offset as a single space-separated string (e.g. `20 0`) per image | Add `energy_filter_slit_width` and `energy_filter_loss_offset` as separate slots on `ExperimentRun` (per-acquisition, not instrument) |
| `ProbeMode` | `C5_LMM_1.mrc.mdoc` | Missing | — | mdoc writes per-image integer (0=nanoprobe, 1=microprobe). `CryoEMInstrument.imaging_mode` exists but its enum values are `{EFTEM, TEM, STEM}` — imaging mode, not condenser lens probe configuration. These are different concepts; no schema equivalent for probe mode. | Add `probe_mode` integer slot to `ExperimentRun` (or `CryoEMInstrument`) with documented values 0=nanoprobe, 1=microprobe |
| `SpotSize` | `mmm1.mrc.mdoc` | Partial | `CryoEMInstrument.spotsize` | Schema has spotsize as a `QuantityValue` on the instrument class; mdoc writes an integer per image and it can differ between survey and high-mag passes | Add `spot_size` integer to `ExperimentRun` for per-acquisition value |

### Stage

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `StagePosition` | `C5_LMM_1.mrc.mdoc` | Partial | `Movie.stage_position_x`, `Movie.stage_position_y` | Stage XY exists on `Movie` class only; integrating images (LMM, mmm, screening) have no per-image stage position slots | Add `stage_position_x`, `stage_position_y` to base `Image` class (or `Image2D`) — see Design Decision D1 |
| `StageZ` | `C5_LMM_1.mrc.mdoc` | Partial | `Movie.stage_position_z` | Same gap as `StagePosition` | Same fix as `StagePosition` |
| `TiltAngle` | `C5_LMM_1.mrc.mdoc` | Partial | `ExperimentRun.stage_tilt`, `tilt_angle_min`, `tilt_angle_max` | Schema has session-level tilt range; mdoc has actual per-image tilt angle (near 0.004° for SPA) | Add `tilt_angle` float to base `Image` class for per-image actual tilt |
| `RotationAngle` | `C5_LMM_1.mrc.mdoc` | Missing | — | Image rotation relative to stage axes (degrees); not the same as `tilt_axis_angle`; needed for correct image display and downstream alignment | Add `image_rotation_angle` float to base `Image` class |

### Camera & Detector

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `CameraIndex` | `C5_LMM_1.mrc.mdoc` | Partial | `ExperimentRun.detector` (string) | `ExperimentRun.detector` is described as "run-specific detector identifier or detector component"; this can hold camera identification but is a free string, not a typed integer index. CameraIndex=1 (integer) has no direct typed equivalent. | Document convention: map CameraIndex integer to `ExperimentRun.detector` as a string (e.g. `"1"`); or add `camera_index` integer slot for typed storage |
| `Binning` | `C5_LMM_1.mrc.mdoc` | Full | `ExperimentRun.camera_binning` | Direct mapping | — |
| `DividedBy2` | `C5_LMM_1.mrc.mdoc` | Missing | — | SerialEM post-acquisition 2× software binning flag (1 in integrating, 0 in counting); affects effective pixel size | Low priority; document the pixel size correction in loader notes: effective_pixel = PixelSpacing × (2 if DividedBy2 else 1) |
| `CountsPerElectron` | `C5_LMM_1.mrc.mdoc` | Missing | — | Detector gain calibration: 16 e⁻/count (integrating mode), 1 e⁻/count (counting mode); required for accurate dose calculation | Add `counts_per_electron` integer to `CryoEMInstrument` or `ExperimentRun` |
| `OperatingMode` | `C5_LMM_1.mrc.mdoc` | Partial | `CryoEMInstrument.detector_mode` (DetectorModeEnum); also `DataCollectionStrategy.detector_mode` (nested in ExperimentRun) | Schema enum (`counting`, `integrating`, `super_resolution`, `linear`, `correlated_double_sampling`) covers the concept; SerialEM OperatingMode is an integer (1 = normal) not an enum string | Document integer→enum mapping in loader; no schema change required |
| `UsingCDS` | `C5_LMM_1.mrc.mdoc` | Missing | — | Correlated double sampling flag; always 0 in this dataset; Falcon 4i-specific feature. Note: `DetectorModeEnum` includes `correlated_double_sampling` — when UsingCDS=1, it could be expressed via `detector_mode`; but as a separate boolean field it is not captured. | Low priority; no dedicated schema slot; if CDS sessions need tracking, map UsingCDS=1 → `detector_mode = correlated_double_sampling` |

### Acquisition Parameters

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `ExposureTime` | `C5_LMM_1.mrc.mdoc` | Full | `ExperimentRun.exposure_time_per_frame`; also `Image.exposure_time` (per-image slot on base class) | Both session-level and per-image slots exist. `ExperimentRun.exposure_time_per_frame` captures the session nominal value; `Image.exposure_time` can hold the per-image measured value (which can vary slightly across tiles). | — |
| `ExposureDose` | `C5_LMM_1.mrc.mdoc` | Partial | `ExperimentRun.total_dose` (session-level); also `Image.dose` (per-image slot on base class) | `ExposureDose = 0` in raw mdoc — SerialEM writes zero at collection time; actual dose must be computed from `DoseRate × ExposureTime × pixel_area`. `Image.dose` is the more natural per-image target but will always be zero from raw mdoc. | Document calculation: `Image.dose = DoseRate × ExposureTime / pixel_area_nm²`; do not ingest the raw `ExposureDose = 0` field directly |
| `DoseRate` | `C5_LMM_1.mrc.mdoc` | Full | `ExperimentRun.dose_rate` | Direct mapping; note: absent from `[FrameSet]` blocks (see field comparison table) | — |
| `Intensity` | `C5_LMM_1.mrc.mdoc` | Missing | — | SerialEM beam intensity dial value; dimensionless internal units; no standard physical meaning across instruments | Low priority; no schema equivalent |
| `LowDoseConSet` | `C5_LMM_1.mrc.mdoc` | Missing | — | SerialEM low-dose mode preset ID (e.g. 4=Record, -8=LMM custom); links image to acquisition parameter preset | Low priority; no schema equivalent |

### Focus & Alignment

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `Defocus` | `C5_LMM_1.mrc.mdoc` | Partial | `Image2D.defocus`, `Movie.nominal_defocus` | Per-image applied defocus (µm, signed). `Image2D.defocus` covers integrating images; `Movie.nominal_defocus` covers movies. Session range also on `ExperimentRun.defocus_range_min/max`. Good overall coverage but two separate slots for logically the same field. | Clarify in loader: map mdoc `Defocus` → `Movie.nominal_defocus` for frames; `Image2D.defocus` for integrating images |
| `TargetDefocus` | `C5_LMM_1.mrc.mdoc` | Full | `ExperimentRun.defocus_target` | Direct mapping | — |
| `ImageShift` | `C5_LMM_1.mrc.mdoc` | Partial | `Movie.beam_shift_x`, `Movie.beam_shift_y` | Beam shift in µm relative to center; exists on `Movie` class only. Integrating images (LMM, mmm, screening) also carry `ImageShift` but have no schema slot for it. | Add `beam_shift_x`, `beam_shift_y` to base `Image` class — see Design Decision D1 |

### Frame / Movie Specific

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `GainReference` | `frames/Image_000.tif.mdoc` | Missing | — | Filename of `.dm4` gain reference used for normalization; written per movie; the same file referenced across all movies in a session | Model as `DataFile` record with `file_role = "gain_reference"` and `file_format = "dm4"` (requires D3 and D4); link from `ExperimentRun` |
| `DefectFile` | `frames/Image_000.tif.mdoc` | Missing | — | Filename of camera defect map (`.txt`); written per movie; shared across all movies in a session | Model as `DataFile` record with `file_role = "defect_map"` and `file_format = "ascii"`; link from `ExperimentRun` |
| `SubFramePath` | `frames/Image_000.tif.mdoc` | Partial | `DataFile.file_path` | `file_path` exists on `DataFile` for the archive location; `SubFramePath` is the acquisition-time path on the Windows acquisition PC (e.g. `X:\DoseFractions\...`); these are different concepts | Add `acquisition_path` string slot to `DataFile` for the original write path — see Design Decision D5 |
| `NumSubFrames` | `frames/Image_000.tif.mdoc` | Full | `ExperimentRun.frames_per_movie` | Direct mapping | — |
| `FrameDosesAndNumber` | `frames/Image_000.tif.mdoc` | Partial | `Movie.dose_per_frame` / `DataCollectionStrategy.dose_per_frame` + `ExperimentRun.frames_per_movie` | mdoc writes both as a single space-separated string `"0 49"` (first value = cumulative dose start, always 0; second = frame count). `dose_per_frame` is NOT on ExperimentRun — it is on `Movie` (per-image) and `DataCollectionStrategy` (nested session-level). `frames_per_movie` IS on ExperimentRun. | Document parsing: split on space → `[dose_start, frame_count]`; `dose_per_frame = dose_rate × exposure_time / frame_count` |

### Multishot / Hole Targeting

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `MultishotHoleAndPosition` | `screening/Hole_01_1-1.mrc.mdoc` | Partial | `ExperimentRun.shots_per_hole`, `holes_per_group` (counts), `Movie.hole_id`, `Movie.acquisition_group` | Count fields exist on `ExperimentRun`; `Movie.hole_id` covers the hole identifier; but the sub-position string (e.g. `"1-1"` = hole 1, beam position 1) within the multishot pattern is not stored | Add `multishot_position_id` string slot to `Movie` class (or `Image2D`) to capture the beam-position index within the multishot pattern |

### Montage / Tiling

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `Montage` | `C5_LMM_1.mrc.mdoc` | Missing | — | Boolean flag indicating this MRC file is a tile stack requiring stitching rather than a single image | Add `is_montage` boolean to `DataFile`, or introduce a new `MontageImage` concept — see Design Decision D2 |
| `PieceSpacing` | `C5_LMM_1.mrc.mdoc` | Missing | — | Tile step size in pixels (X Y); determines tile overlap for stitching | Part of proposed `MontageParameters` class — see D2 |
| `PieceCoordinates` | `C5_LMM_1.mrc.mdoc` | Missing | — | Per-tile XY pixel position in the montage grid (one value per `[ZValue]` block) | Part of proposed `MontageParameters` class — see D2 |
| `AlignedPieceCoords` | `C5_LMM_1.mrc.mdoc` | Missing | — | Per-tile corrected XY positions after cross-correlation alignment | Part of proposed `MontageParameters` class — see D2 |
| `FullMontSize` | `C5_LMM_1.mrc.mdoc` | Missing | — | Total stitched image dimensions in pixels (e.g. `15840 14352`) | Part of proposed `MontageParameters` class — see D2 |
| `FullMontNumFrames` | `C5_LMM_1.mrc.mdoc` | Missing | — | Tile grid shape (e.g. `6 8` = 6 columns × 8 rows = 48 tiles) | Part of proposed `MontageParameters` class — see D2 |
| `XedgeDxy` / `XedgeMaxSD` | `C5_LMM_1.mrc.mdoc` | Missing | — | Cross-correlation shift and quality metric for X-direction tile edges | Part of `MontageParameters` or a `QualityMetrics` class — see D2 |
| `YedgeDxy` / `YedgeMaxSD` | `C5_LMM_1.mrc.mdoc` | Missing | — | Cross-correlation shift and quality metric for Y-direction tile edges | Part of `MontageParameters` or a `QualityMetrics` class — see D2 |
| `PercentileStats` | `C5_LMM_1.mrc.mdoc` | Missing | — | Per-tile intensity percentile statistics written by SerialEM for QC | Part of `MontageParameters` or image QC metadata — see D2 |

### Montage QC / Control (SerialEM internal — low scientific priority)

These fields appear only in the LMM (atlas) mdoc. They represent SerialEM acquisition
control parameters with no direct scientific equivalent outside SerialEM. Schema coverage
for all is **Missing**. If round-trip fidelity to SerialEM is required, store as an
unstructured metadata blob (e.g. a `serialem_control_metadata` JSON string on `DataFile`).

| Field | Example Fixture File | Notes |
|-------|---------------------|-------|
| `Alpha` | `C5_LMM_1.mrc.mdoc` | Beam tilt offset in SerialEM units; `-999` = not set |
| `BufISXY` | `C5_LMM_1.mrc.mdoc` | Beam shift buffer XY |
| `CameraModes` | `C5_LMM_1.mrc.mdoc` | Camera mode flags |
| `ConSetUsed` | `C5_LMM_1.mrc.mdoc` | Acquisition preset ID used |
| `DriftSettling` | `C5_LMM_1.mrc.mdoc` | Post-move drift wait time (s) |
| `FilterState` | `C5_LMM_1.mrc.mdoc` | Energy filter state (slit in/out, width) |
| `FitToPolyID` | `C5_LMM_1.mrc.mdoc` | Navigator polygon target ID for stage fitting |
| `MontBacklash` | `C5_LMM_1.mrc.mdoc` | Stage backlash correction in X and Y |
| `MoveStage` | `C5_LMM_1.mrc.mdoc` | Whether stage was moved between tiles |
| `ValidBacklash` | `C5_LMM_1.mrc.mdoc` | Backlash correction validity flag |

### Image Metadata

| Field | Example Fixture File | Coverage | Schema Location | Notes | Implementation Plan |
|-------|---------------------|----------|-----------------|-------|---------------------|
| `ImageSize` | `C5_LMM_1.mrc.mdoc` | Full | `Image.dimensions_x`, `Image.dimensions_y` | Direct mapping; absent from `[FrameSet]` blocks (frame mdocs do not repeat image dimensions) | — |
| `UncroppedSize` | `C5_LMM_1.mrc.mdoc` | Missing | — | Original full-sensor pixel dimensions before ROI crop; SerialEM encodes negative values by convention (e.g. `-2880 -2046`); the absolute value is the uncropped size | Low priority; add optional `uncropped_dimensions_x`, `uncropped_dimensions_y` integer slots to `Image` |
| `DataMode` | `C5_LMM_1.mrc.mdoc` | Missing | — | MRC integer data type code: 1=int16, 6=uint16; encoding detail relevant for downstream processing | Low priority; could be noted in `DataFile.data_type` or left to file inspection |
| `MinMaxMean` | `C5_LMM_1.mrc.mdoc` | Missing | — | Per-image intensity statistics (min, max, mean); useful for QC and normalization checks; absent from `[FrameSet]` blocks | Add `intensity_min`, `intensity_max`, `intensity_mean` float slots to base `Image` class |
| `RotationAndFlip` | `C5_LMM_1.mrc.mdoc` | Missing | — | SerialEM integer encoding camera transform (e.g. 6 = 90° + flip); required to orient the image correctly relative to stage coordinates | Add `rotation_and_flip` integer slot to base `Image` class (or document the value-to-transform mapping and store as `image_transform_code`) |

### FileFormatEnum gaps

These file types are produced by every SerialEM session but absent from `FileFormatEnum`.
The EMSL loader currently silently skips any file whose format it cannot recognize.

| Format | Example Fixture File | Coverage | Notes |
|--------|---------------------|----------|-------|
| `mdoc` | `C5_LMM_1.mrc.mdoc` | Missing | SerialEM metadata sidecar for every MRC and TIFF; must be added to ingest session metadata |
| `nav` | `C5.nav` | Missing | SerialEM navigator file; encodes all acquisition targets with stage coordinates and map references |
| `dm4` | `frames/SuperRef_Image_000.dm4` | Missing | DigitalMicrograph 4 gain reference; needed to model GainReference provenance (see D3) |

---

## High-level summary

### Coverage statistics

63 mdoc fields tracked across the five mdoc types (10 MontQC control fields and 3 FileFormatEnum
gaps are included in Missing but listed in abbreviated tables):

| Coverage | Count | % | Notes |
|----------|-------|---|-------|
| Full | 10 | 16% | Session-level SPA parameters well covered |
| Partial | 15 | 24% | Mostly per-image vs per-session scope mismatches |
| Missing | 38 | 60% | Montage/tiling (11), SerialEM QC/control (10), camera/detector (6), image QC (5), frame provenance (2), provenance links (2), file formats (3), others |

### Where the schema is strong

The schema is well-designed for **session-level single-particle acquisition parameters**:
core optics (`Voltage`, `PixelSpacing`, `Magnification`, `Binning`), dose
(`DoseRate`, `ExposureTime`), and focus targeting (`TargetDefocus`, `frames_per_movie`,
`camera_binning`) all have direct mappings. The `ExperimentRun` class covers the standard
cryoSPARC/RELION experiment configuration space well.

### Where the schema has gaps

**1. Per-image spatial metadata on non-Movie classes.** `Movie` has stage position, beam
shift, and nominal defocus as per-image slots. `Image2D` and the base `Image` class do
not. Yet every integrating image (atlas tile, grid square survey, screening micrograph) in
SerialEM carries per-image `StagePosition`, `ImageShift`, `TiltAngle`, and `NavigatorLabel`.
These are essential for spatial reconstruction (where on the grid was this image taken?) and
provenance tracking.

**2. Montage / tiling has no schema representation at all.** Atlas and medium-mag survey
images are tile stacks, not single images. Tile positions, stitching parameters, and
tile-edge QC metrics are absent. This is a significant structural gap: the schema currently
cannot distinguish a montage from a single image, let alone represent its spatial layout.

**3. Frame provenance files are not modeled.** `GainReference` and `DefectFile` are
referenced by name in every movie mdoc. The files exist in the fixture (`SuperRef_*.dm4`,
`defects_*.txt`) but there is no schema mechanism to represent them as first-class entities
linked to the experiment. This breaks downstream processing pipeline provenance.

**4. FileFormatEnum is missing `mdoc` (P0), and conditionally `dm4` and `nav`.** `mdoc` is
a hard blocker — the EMSL loader silently skips all metadata sidecars without it. `dm4` is
only needed if gain reference files are modeled as first-class `DataFile` records (D3).
`nav` is optional — the `NavigatorLabel` string cross-reference can be stored on `Image`
without registering the nav file itself.

---

## Design decisions to elevate to schema group

### D1 — Per-image vs per-session metadata scope (structural decision)

**Problem:** The schema models most acquisition fields at `ExperimentRun` (session) level.
`Movie` is the only class with per-image spatial slots (`stage_position_x/y/z`,
`beam_shift_x/y`, `nominal_defocus`). `Image2D` and base `Image` have none. SerialEM
writes all of these fields per-image for every image type — integrating survey images
need them as much as movies do.

**Decision needed:** Should `stage_position_x/y/z`, `tilt_angle`, `beam_shift_x/y`,
`navigator_label`, and `unix_timestamp` live on the **base `Image` class** (available
to all image types) or remain **`Movie`-only**?

**Implications:**
- Moving to base `Image`: enables full per-image provenance for atlas/mmm/screening;
  requires schema change to `Image` (low risk — additive)
- Keeping on `Movie`: integrating survey images lose per-image spatial context;
  downstream tools cannot determine where on the grid a screening image was acquired

**Recommendation:** Add to base `Image`. These fields are intrinsic to any acquired image,
not specific to dose-fractionated movies.

---

### D2 — Montage as a first-class schema concept

**Problem:** Atlas montages and MMM surveys are spatially-composite tile stacks. The mdoc
carries 11 montage-specific fields (`PieceCoordinates`, `FullMontSize`, edge-correlation
QC metrics, etc.) with no schema equivalent. The current schema cannot distinguish a
montage file from a single image.

**Decision needed:** How should montage data be modeled? Options:

- **(a) New `MontageImage` subclass** of `Image3D` or `Image2D` with a nested
  `MontageParameters` class carrying tile layout and QC fields. Clean OOP model; requires
  a new class hierarchy branch.
- **(b) `MontageParameters` class attached to `DataFile`** via an optional slot.
  Keeps the image class hierarchy flat; montage metadata is on the file record.
- **(c) Individual tile `Image2D` records** with a `montage_id` grouping key.
  Tiles are modeled as first-class images; stitching is downstream. Consistent with how
  EMPIAR stores multi-frame data. Requires many more records per acquisition.

**Recommendation:** Option (a) — `MontageImage` subclass with `MontageParameters`. The
tile positions and edge-correlation QC are intrinsic to the composite; they cannot
meaningfully live on a flat `DataFile` record.

---

### D3 — Gain reference and defect map as first-class `DataFile` records

**Problem:** `GainReference` and `DefectFile` are named in every `[FrameSet]` mdoc block.
They are shared dependencies across all movies in a session. Currently no schema mechanism
exists to represent them as linked entities.

**Decision needed:** How should correction files be modeled?

- **(a) Formalize `FileRoleEnum`** with values: `raw`, `gain_reference`, `defect_map`,
  `intermediate`, `final`, `metadata`. Create `DataFile` records with the appropriate role;
  link them from `ExperimentRun` via an explicit `correction_files` list slot.
- **(b) Keep `file_role` as a plain `string`** (current state — verified in schema: `file_role`
  is a `string` slot on `DataFile` with no enum defined) and document conventions by
  establishing a controlled vocabulary in the loader. Lower barrier to adoption; looser
  interoperability; no schema change required.

**Prerequisite:** `dm4` must be added to `FileFormatEnum` (see D4). `ascii` already exists
for defect text files.

**Recommendation:** Option (a) — `FileRoleEnum`. The schema already uses controlled
vocabulary enums for all other categorization; inconsistency here would reduce validation
value. A small, well-defined enum is easy to extend later.

---

### D4 — FileFormatEnum gaps: `mdoc` (P0), `dm4` (conditional), `nav` (optional)

**Problem:** Three file types produced by every SerialEM session are absent from
`FileFormatEnum`. The EMSL loader silently skips files with unrecognized formats.

**Priority is not uniform across the three:**

- **`mdoc`** — P0 blocker. Every MRC and TIFF has a sidecar mdoc carrying all acquisition
  metadata. No SerialEM ETL can proceed without this.
- **`dm4`** — conditional on D3. Only needed if gain reference files are modeled as first-class
  `DataFile` records. If `GainReference` is stored as a plain string on `ExperimentRun`,
  no `DataFile` record is created for the dm4 and this enum value is never used.
- **`nav`** — optional. The navigator file matters for provenance, but the schema fix for
  `NavigatorLabel` is adding a string slot to `Image` (D1), not necessarily ingesting the
  nav file itself as a `DataFile` record. SerialEM metadata ingestion can be fully
  implemented without registering the nav file in the schema.

**Recommendation:** Add `mdoc` now as a P0 patch. Add `dm4` alongside D3 if D3 is
approved. Defer `nav` until there is a concrete use case for tracking the nav file itself.

---

### D6 — Image class hierarchy: `Movie`, integrating images, and montages

**Problem:** The current image hierarchy has two concrete subclasses of `Image2D`: `Movie`
(dose-fractionated) and `Micrograph` (post-motion-correction with CTF fields). This leaves
three SerialEM image types with no natural home:

- **Screening / hole survey images** — single integrating exposures at mid/high mag. They
  share acquisition metadata with movies (stage position, beam shift, navigator label) but
  produce no frames and carry no CTF fields. Currently they would fall into plain `Image2D`,
  losing all per-image spatial metadata.
- **Atlas and MMM montages** — MRC tile stacks requiring stitching. Spatially and
  structurally different from any single image. `Image2D` cannot represent the tile
  layout; 48 separate `Image2D` records per atlas loses the composite structure.
- **`Movie` naming** — "Movie" is standard cryoEM terminology (used in cryoSPARC, RELION,
  EMDB) and should not be renamed. The issue is not naming but coverage.

**Three decisions interact here:**

1. **Rename `Movie`?** No — community term, renaming breaks convention.
2. **Add an `IntegratingImage` class for screening/survey?** The D1 fix (per-image slots
   on base `Image`) is necessary regardless. Whether that also warrants a dedicated class
   depends on whether integrating images need fields that don't belong on all `Image2D`
   subclasses (e.g. montage membership, `ConSetUsed`).
3. **`MontageImage` class for atlas/MMM?** D2 almost certainly requires a new class.
   A montage tile is an integrating image with spatial tiling metadata, and that is hard
   to represent cleanly as a plain `Image2D`.

**Implication:** D1 and D2 should be designed together. Any `MontageImage` class needs to
inherit the same per-image slots that D1 promotes to base `Image`. A likely target
hierarchy:

```
Image (base)
  + stage_position_x/y/z, beam_shift_x/y, tilt_angle,
    navigator_label, rotation_angle, unix_timestamp  ← D1 additions

  Image2D
    Movie          — dose-fractionated (frames, dose_per_frame, …)
    Micrograph     — motion-corrected (CTF fields, …)
    IntegratingImage (new, optional) — single-exposure non-movie
      MontageImage (new) — tile stack with MontageParameters  ← D2
```

**Recommendation:** Treat D1 and D2 as a single combined schema group discussion.
`IntegratingImage` is optional if the base `Image` additions (D1) are sufficient for
screening images; `MontageImage` is likely required for atlas/MMM.

---

### D5 — Acquisition path vs archive path on `DataFile`

**Problem:** `SubFramePath` in the mdoc records where frames were written on the acquisition
PC at collection time (a Windows `X:\DoseFractions\...` path). `DataFile.file_path`
records the archival path. These are semantically different: the acquisition path identifies
the original write location (useful for tracing data provenance back to the instrument),
while the archive path locates the file in the repository.

**Decision needed:** How should acquisition-time paths be stored?

- **(a) Add `acquisition_path` string slot to `DataFile`** for the original write path.
  Clean semantic separation; explicit in the schema.
- **(b) Use `storage_uri` for the archive URI and `file_path` for the acquisition path**
  (documented convention). No schema change; relies on loader discipline.

**Recommendation:** Option (a) — explicit `acquisition_path`. Option (b) re-uses
`file_path` in a non-obvious way that would confuse schema consumers and makes validation
impossible.

---

## Questions for microscopists

Questions to ask SerialEM users to validate the schema design decisions above and surface
gaps not visible from file analysis alone.

### Workflow and image types
- Do you ever go back to re-image grid squares or holes after initial screening, or is acquisition always linear? *(affects how sessions and runs are scoped)*
- How often do you use multishot patterns — is it always the same pattern within a session or does it vary per hole?
- Do you ever run SerialEM in a mode where the atlas or MMM is skipped? *(affects whether montage is always present)*

### Montage (D2)
- Do you ever use the stitched atlas image directly for analysis, or is it purely navigational? *(affects how much fidelity the schema needs to preserve)*
- How do you actually open and inspect the atlas — in SerialEM itself, or exported? *(helps assess whether per-tile metadata matters downstream)*

### Per-image metadata (D1/D6)
- Do you ever need to go back from a processed particle to the original screening image that selected that hole? *(tests whether `NavigatorLabel` cross-reference is scientifically needed or just bookkeeping)*
- Does stage position per image matter to you after acquisition, or is it only used during collection?

### Gain reference and defects (D3)
- How often does the gain reference change within a session or across sessions? *(affects whether it belongs on the instrument, session, or per-movie)*
- Who generates the defect file — SerialEM automatically, or a separate calibration step?

### Probe mode and beam configuration
- Do you typically switch between nanoprobe and microprobe within a single session, or is it set once at the start? *(determines whether probe mode belongs on `ExperimentRun` or `CryoEMInstrument`)*
- Is probe mode something you'd want to filter or search datasets by?

### Schema design
- When you hand data off to a computing person for processing, what metadata do they always ask you for that isn't in the TIFF/MRC file itself? *(surfaces gaps from the user side)*
- Do you use any external LIMS or spreadsheet to track sessions alongside SerialEM? If so, what fields do you track there that SerialEM doesn't record? *(may reveal gaps not visible in file analysis)*
- Are there fields in the mdoc you never look at and wouldn't miss?
