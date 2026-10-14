# RO-Crate Mapping: emsl-serialem-krios

**Crate file:** `tests/data/raw/emsl-serialem-krios/ro-crate-metadata.json`  
**Full record:** `tests/data/valid/Dataset-emsl-serialem-krios.yaml` (lambda-ber-schema `Dataset`)  
**Schema version:** lambda-rocrate-core 0.3.4 / lambda-ber-schema 0.1.2
**Fixture version:** hackathon branch (SerialEM SPA, Titan Krios at EMSL)  
**Status:** All 4 validation layers pass.

---

## 1. Resolved Mappings

### Facility record and typed slots

`metadata.yaml` is copied verbatim into `#exp-serialem-spa.runParameters`: same keys, same
values, same nesting, nulls kept. The profile defines `runParameters` as the facility's own
parameter block, left opaque so a reader can always recover the source record. A few values
are also projected onto typed crate slots:

| Source | Typed slot | Notes |
|---|---|---|
| `proposal_id: 99999` | root `identifier[0].value` (propertyID=EMSL-proposal) | Anonymous fixture value |
| `session_id: 01-01-01` | root `identifier[1].value` (propertyID=EMSL-session) | Anonymous fixture value |
| `short_sample_name: Sample grid 1` | `sample_code: "Sample-grid-1"` on root and on `#sample-grid1` | |
| `instrument_id: 99999` | `#instr-krios.instrument_code` as `EMSL-KRIOS-99999` | EMSL resource ID (not chassis serial); see §5 |
| `detector_id: K3` | `#instr-krios.detector` | |
| `processing_scheme: 1` | `collection_mode: "single_particle"` on `#exp-serialem-spa` | 1=SPA, 2=tomo, 3=microED |
| `sample_mg/ml: 1mg/ml` | `#sample-grid1.concentration: "1 mg/ml"` | |
| SerialEM version (mdoc headers) | `#sw-serialem` (`SoftwareApplication`), named in the run's `instrument` | 4.2.2 |

The session settings themselves are typed on `#exp-serialem-spa` (Core 0.3.4), each the
`ExperimentRun` slot of the same name and a `{numeric_value, unit}` quantity:

| Source (sheet or mdoc) | Typed slot on `#exp-serialem-spa` |
|---|---|
| `detector_id: K3` | `detector` (also on `#instr-krios`) |
| `voltage: 300` | `accelerating_voltage` (kilovolts) |
| `cs: 2.7` | `cs` (millimeters) |
| `nominal_magnification: 130` (kx) | `magnification` 130000 |
| `nominal_pixel_size: 0.34` | `nominal_pixel_size` (Angstroms per pixel) |
| mdoc `PixelSpacing` 0.340292 | `calibrated_pixel_size` (Angstroms per pixel) |
| `binning_factor: 0.5` | `camera_binning` |
| mdoc `NumSubFrames` 49 | `frames_per_movie` |
| `total_exposure: 1.046` | `total_exposure_time` (seconds) |
| `total_dose: 50` | `total_dose` (electrons per Angstrom squared) |
| `spot_size: 4` | `spot_size` |
| `c2_aperture: 50` | `c2_aperture` (micrometers) |
| `beam_diameter: 750` | `beam_diameter` (micrometers) |
| `energy_filter_slit: 20` | `energy_filter_slit_width` (electronvolts) |
| `phase_plate: false` | `phase_plate_used` |
| `tilting_mode: 0` | `tilting_scheme: none` |
| `assessments` (1, 1, 1) | `quality_metrics.grid_quality`: `none`, `ideal`, `optimal` |

Not typed: `topaz_model` and `motCorr_bin`, which configure EMSL's downstream processing rather
than describe the collection (the schema's `ParticlePickingParameters` and
`MotionCorrectionParameters` would hold them on a `WorkflowRun` once one exists), and the sheet's
null fields. Both stay in `runParameters`. The 6 x 8 atlas grid and the survey and screening pixel
spacings stay in the mdoc sidecars and the image files' descriptions.

### File entities

All files listed in `README.md` are present in the crate as `@graph` entities with `sha256` and `contentSize`. `README.md` itself is not included — it is developer documentation, not a data artifact. Real text sidecars carry computed hashes; binary stubs use the empty-file hash `e3b0c44298fc1c149afbf4c8996fb924...` with `contentSize: "0"`.

| File | Hash source | Notes |
|---|---|---|
| `*.mdoc`, `*.nav`, `*.txt`, `metadata.yaml` | Real (computed via sha256sum) | |
| `*.mrc`, `*.tif`, `*.dm4` | Empty-file stub | Hash is canonical for zero-byte file |

---

## 2. Vocabulary Gaps (resolved)

lambda-ber-schema now has every term this crate needs, so the crate declares no `vocabEntry`:

| Value | Enum | Used by |
|---|---|---|
| `mdoc` | `FileFormatEnum` | the eight `.mdoc` sidecars |
| `nav` | `FileFormatEnum` | `C5.nav` |
| `dm4` | `FileFormatEnum` | `frames/SuperRef_Image_000.dm4` |
| `yaml` | `FileFormatEnum` | `metadata.yaml` |
| `gain_reference` | `DataTypeEnum` | `frames/SuperRef_Image_000.dm4` |
| `defect_map` | `DataTypeEnum` | `frames/defects_GS_01_H_01_000.txt` |
| `atlas` | `DataTypeEnum` | `C5_LMM_1.mrc` |
| `screening_image` | `DataTypeEnum` | `mmm1.mrc`, `mmm2.mrc`, `screening/Hole_01.mrc`, `screening/Hole_01_1-1.mrc` |

**Note on `collection_mode`:** The crate uses `"single_particle"`, a valid value in `CollectionModeEnum`.

---

## 3. Schema Gaps

Fields in the source data that had no slot. Status as of lambda-rocrate-core 0.3.4.

### 3a. `quality_metrics` / `grid_quality` — resolved

`ExperimentRunAction` now takes `quality_metrics`, the schema's `QualityMetrics` object. The grid
assessment is in `quality_metrics.grid_quality` with the main schema's enum values
(`IceContaminationEnum: none`, `IceQualityEnum: ideal`, `ParticleConcentrationEnum: optimal`); the
sheet's three-point scales map one to one onto those enums. The raw codes stay in
`runParameters.assessments`.

### 3b. `acquisition_software` — resolved without a slot

SerialEM 4.2.2 is a `SoftwareApplication` entity (`#sw-serialem`) named in the run's `instrument`
list, which schema.org defines to cover both equipment and software. The full record uses
`ExperimentRun.acquisition_software` and `acquisition_software_version`.

### 3c. Per-session optics and Cs — resolved

Accelerating voltage, Cs, spot size, C2 aperture, beam diameter, energy filter slit width and phase
plate use existed in lambda-ber-schema only on `CryoEMInstrument`, one record shared by every
session on the microscope. They are now `ExperimentRun` slots too (`CryoEMInstrument` keeps them as
capabilities and defaults), and Core 0.3.4 carries them on `ExperimentRunAction`. mmCIF records Cs
per imaging session as well (`_em_imaging.nominal_cs`).

### 3d. Instrument-level detail — open

Energy filter presence and model, the detector's physical pixel size (5 µm, sheet field
`detector_physical_pixel_size`) and other `CryoEMInstrument` fields have no `InstrumentEntity` slot,
and cannot appear in a `Dataset` record either: `Dataset.instruments` is typed `Instrument`, and
`linkml-run-examples` loads entries as plain `Instrument`. A type designator on `Instrument` would
fix the Dataset side, but linkml-runtime then files the designator under `unknown_instrument_type`
and the Turtle dump fails. The physical pixel size is in `runParameters`.

### 3e. `sample_buffer: 1xTBS` — in the full record only

`SampleEntity` deliberately carries only the searchable identity layer; the profile puts buffer
detail in the fuller record. The Dataset record has it as `Sample.buffer_composition`.

### 3f. `vitrification_settings` — missing and out of scope

The metadata.yaml field is a placeholder (`'insert setting here'`). Even if populated, this belongs on `SamplePreparation`, which is not part of the rocrate manifest tier. Declared `missing` on the root with `reason: "not-available"`.

### 3g. Null fields omitted

The following fields from metadata.yaml are null in the source and are omitted from the crate (null → absent is the correct mapping):

`nominal_dose_rate_eps`, `frames_per_second`, `fiducial_size`, `tilt_angle_increment`, `rotation_rate`, `nominal_camera_Length`

The last two (`rotation_rate`, `nominal_camera_Length`) are only relevant for tomography and microED respectively. They should remain absent for SPA sessions.

---

## 4. Structural Decisions

### 4a. InstrumentEntity stays narrow; the run carries the settings

The rocrate `InstrumentEntity` carries identity and affiliation, not acquisition parameters,
consistent with the profile's rule that capabilities belong on the instrument and the values used
belong on the run. The settings EMSL records per session are typed on `#exp-serialem-spa`
(Section 1); the sheet itself is in `runParameters`, verbatim.

### 4b. Folder dataset entities (`frames/`, `screening/`)

Both are modeled as `Dataset` entities representing groups of related files. Each lists its files in `hasPart`, with `partCount` equal to that list (8 and 4), and declares `schemaRecord` as `not-applicable` (metadata carried by sidecar mdocs). Each file also has its own `CrateFile` entity with its own `sha256`, so the folders declare no checksum gap; that the movies are stubs is declared once on the root (`raw_frame_series`, `not-deposited`).

### 4c. Multiple magnification tiers

A single SerialEM session typically spans 3–4 magnification tiers (atlas ~135x, survey ~740x, screening ~11500x, acquisition ~130000x). The schema has one `magnification` slot on `ExperimentRun`, which the crate's run carries for the acquisition magnification (130000x, the science-relevant tier). Lower-magnification images are typed `atlas` or `screening_image`, and their magnification is in their mdoc sidecars and file descriptions.

**Recommendation:** Consider a `magnification_tiers` list or per-file `magnification` slot on `CrateFile` for multi-mag sessions.

### 4d. `experiment_date` not in ExperimentRunAction

The compiled schema exposes `experiment_date` on `ExperimentRunAction` (and `collectionDate` on the root), so this is not a schema gap. The crate sets `experiment_date` to the session's first day and `startTime`/`endTime` to the first and last mdoc `DateTime` values (anonymised, 2001-01-01T19:14:12 to 2001-01-02T15:51:29).

---

## 5. Anonymisation Notes

Two distinct identifiers in the source were anonymised, using different tokens:

| Identifier | Anonymised to | Where it appears |
|---|---|---|
| EMSL proposal number | `99999` | `metadata.yaml`, crate root `identifier`, `experiment_code` |
| EMSL session ID | `01-01-01` | `metadata.yaml`, crate root `identifier`, `experiment_code` |
| Krios chassis serial number | `XXXXXXX` | mdoc `[T = ...]` title lines |
| EMSL resource/instrument ID | `99999` | `metadata.yaml:instrument_id` |
| Acquisition dates | `01-Jan-2001` / `02-Jan-2001` | mdoc `DateTime` fields |
| Scientist names | scrubbed | Not present in any fixture file |

The `XXXXXXX` token in mdoc headers is a different real identifier than the `99999` in metadata.yaml. Both are anonymised; they should not be treated as equivalent.

---

## 6. Open Questions

| # | Question | Impact | Recommendation |
|---|---|---|---|
| OQ-1 | Is `collection_mode: "single_particle"` the exact enum value, or is it `spa`? | Resolved: `single_particle` is in `CollectionModeEnum` | No change needed |
| OQ-2 | What licence applies to EMSL fixture data for public distribution? | `license` field on root currently set to CC-BY 4.0 | Confirm with EMSL/data team before publishing |
| OQ-3 | Should `s1Findable: true` require a resolvable identifier? With fake `proposal_id: 99999`, the fixture arguably fails findability. | sufficiency block | Change to `false` or add a note field to sufficiency; current crate uses `false` already |
| OQ-4 | Atlas and survey `.mrc` stubs were `data_type: "micrograph"`. Is this correct for navigational low-mag images? | DataTypeEnum | Resolved: `DataTypeEnum` gained `atlas` and `screening_image`, and the crate uses them |
| OQ-5 | The `assesments` typo in `metadata.yaml` (one 's') — should the fixture preserve source fidelity or be corrected? | Source fidelity vs correctness | Fix the typo since we control the fixture; done in this branch |
| OQ-6 | EPU equivalent: EPU sessions have Atlas/GridSquare/FoilHole nested folders. Would the crate structure differ? | Future fixture scope | Yes — EPU would use nested `Dataset` entities. SerialEM's flat-by-type structure is simpler to map. |
| OQ-7 | `calibratedPixelSizeAngstrom: 0.340292` appears in mdoc headers but not in metadata.yaml. Where should it go? | Data discovery | Resolved: `calibrated_pixel_size` on the run (Core 0.3.4), beside `nominal_pixel_size` from the sheet |

---

## 7. Validation Summary

| Layer | Test | Result |
|---|---|---|
| 1 | `test_document_shape` | PASS |
| 2 | `test_entities_conform` | PASS |
| 3 | `test_graph_rules` | PASS |
| 4 | `test_root_declares_profile_conformance` | PASS |

Notable fixes required during development:
- `is_doe_facility` → `isDoeFacility` (compiled JSON Schema uses camelCase for this slot)
- `file_format: "text"` → `"ascii"` (correct FileFormatEnum value for plain-text files)
- `InstrumentEntity`: removed 9 disallowed slots (`accelerating_voltage`, `cs_corrector`, `detector_manufacturer`, `detector_model`, `energy_filter_present`, `energy_filter_slit_width`, `identifier`, `phase_plate`, `pixel_size_physical_um`); all moved to `runParameters`
- `ExperimentRunAction`: removed `acquisition_software` and `quality_metrics` (not in rocrate schema); folded into `runParameters`
- `OrganizationEntity`: changed `@id` from `https://ror.org/04rc0xn13` to a local `#org-emsl` anchor in early draft (then reverted — ROR URI as `@id` is the preferred pattern per the schema description)
- `missing` declarations on `CrateDatasetPart`: added `blocks` tier to all declarations that lacked it
