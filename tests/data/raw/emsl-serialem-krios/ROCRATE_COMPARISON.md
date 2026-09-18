# RO-Crate Mapping: emsl-serialem-krios

**Crate file:** `tests/data/rocrate/valid/emsl-serialem-krios.json`  
**Schema version:** lambda-rocrate-core 0.3.0 / lambda-ber-schema 0.1.2  
**Fixture version:** hackathon branch (SerialEM SPA, Titan Krios at EMSL)  
**Status:** All 4 validation layers pass.

---

## 1. Resolved Mappings

### Root entity (`./`)

| Source | Mapped to | Notes |
|---|---|---|
| `proposal_id: 99999` | `identifier[0].value` (propertyID=EMSL-proposal) | Anonymous fixture value |
| `session_id: 01-01-01` | `identifier[1].value` (propertyID=EMSL-session) | Anonymous fixture value |
| `short_sample_name: Sample grid 1` | `sample_code: "Sample-grid-1"` on root + on SampleEntity | |
| `instrument_id: 99999` | Instrument serial in `#instr-krios.instrument_code` | EMSL resource ID (not chassis serial) |
| `voltage: 300` | `runParameters.acceleratingVoltageKv` | kV |
| `nominal_pixel_size: 0.34` | `runParameters.nominalPixelSizeAngstrom` | Å |
| `total_dose: 50` | `runParameters.totalDoseElectronsPerAngstrom2` | e⁻/Å² |
| `total_exposure: 1.046` | `runParameters.totalExposureS` | seconds |
| `binning_factor: 0.5` | `runParameters.binningFactor` | |
| `nominal_magnification: 130` | `runParameters.nominalMagnificationX` | stored as 130000 (kx → x) |
| `tilting_mode: 1` | `runParameters.tiltingScheme: "dose_symmetric"` | 0=none, 1=dose_symmetric, 2=linear, 3=continuous |
| `c2_aperture: 50` | `runParameters.c2ApertureMicrons` | µm |
| `spot_size: 4` | `runParameters.spotSize` | |
| `beam_diameter: 750` | `runParameters.beamDiameterMicrons` | µm |
| `energy_filter_slit: 20` | `runParameters.energyFilterSlitEv` | eV; also implies Falcon/BioQuantum filter present |
| `phase_plate: false` | `runParameters.phasePlate` | |
| `topaz_model: NA` | `runParameters.topazModel` | Post-processing hint; not a WorkflowRun param |
| `motCorr_bin: 1` | `runParameters.motCorrBin` | Binning during MotionCor2; not a WorkflowRun param |
| `detector_id: K3` | `InstrumentEntity.detector: "K3"` | |
| `detector_physical_pixel_size: 5` | `runParameters.detectorPhysicalPixelSizeUm` | µm; K3 physical pixel |
| `processing_scheme: 1` | `collection_mode: "single_particle"` on ExperimentRunAction | 1=SPA, 2=tomo, 3=microED |
| `ice_contamination: 1` | `runParameters.iceContamination: "none"` | Folded into runParameters; see §3 |
| `ice_quality: 1` | `runParameters.iceQuality: "ideal_range"` | |
| `particle_concentration: 1` | `runParameters.particleConcentration: "just_right"` | |
| `sample_mg/ml: 1mg/ml` | `SampleEntity.concentration: "1 mg/ml"` | |
| Atlas params (mdoc header) | `runParameters.atlasGridColumns/Rows/PixelSpacingAngstrom` | Atlas is one of 3 magnification tiers in session |
| Survey params (mmm1/2 mdoc) | `runParameters.surveyPixelSpacingAngstrom` | |
| `XXXXXXX` (mdoc instrument serial) | `InstrumentEntity.instrument_code` as `EMSL-KRIOS-99999` | See §5: two separate anonymisation tokens |

### File entities

All files listed in `README.md` are present in the crate as `@graph` entities with `sha256` and `contentSize`. `README.md` itself is not included — it is developer documentation, not a data artifact. Real text sidecars carry computed hashes; binary stubs use the empty-file hash `e3b0c44298fc1c149afbf4c8996fb924...` with `contentSize: "0"`.

| File | Hash source | Notes |
|---|---|---|
| `*.mdoc`, `*.nav`, `*.txt`, `metadata.yaml` | Real (computed via sha256sum) | |
| `*.mrc`, `*.tif`, `*.dm4` | Empty-file stub | Hash is canonical for zero-byte file |

---

## 2. Vocabulary Gaps

These values are used in the crate but not yet in their respective enums. All are declared via `vocabEntry` on the root entity.

| Value | Enum | Priority | Recommendation |
|---|---|---|---|
| `mdoc` | `FileFormatEnum` | High | SerialEM sidecar is ubiquitous in the cryo-EM community; add alongside `mrc`. |
| `nav` | `FileFormatEnum` | Medium | SerialEM navigator; less widely exchanged than mdoc, still important for reproducibility. |
| `dm4` | `FileFormatEnum` | Low | DigitalMicrograph format for gain references; could alternatively map to `hdf5` or `application/octet-stream` only. |
| `EMSL` | `FacilityEnum` | High | Major DOE user facility; should be a first-class FacilityEnum entry like ALS, SSRL, etc. |

**Note on `collection_mode`:** The crate uses `"single_particle"`. Verify this is the exact enum value in `CollectionModeEnum` — if it is `spa` or `SPA`, update the crate and this doc.

---

## 3. Schema Gaps

Fields present in the source data that have no direct slot in the current rocrate schema.

### 3a. `quality_metrics` / `grid_quality` — no ExperimentRunAction slot

`quality_metrics` is a well-defined field in the main `lambda_ber_schema` (`CryoEMExperimentRun`) but does not appear as an allowed slot on `ExperimentRunAction` in `lambda_rocrate_core`. The three quality assessments from `metadata.yaml` were therefore folded into `runParameters`:

```yaml
iceContamination: "none"
iceQuality: "ideal_range"
particleConcentration: "just_right"
```

**Recommendation:** Add a `quality_metrics` slot to `ExperimentRunAction` in `lambda_rocrate_core` that accepts the same nested object as the main schema. This is the most data-rich part of a cryo-EM session report and belongs in the crate manifest.

### 3b. `acquisition_software` — no ExperimentRunAction slot

The rocrate `ExperimentRunAction` does not have an `acquisition_software` slot (unlike some earlier drafts). Folded into `runParameters.acquisitionSoftware`.

**Recommendation:** Add `acquisition_software` (string) to `ExperimentRunAction`; it is a critical provenance field for cryo-EM reproducibility. Alternatively, a `SoftwareApplicationEntity` could be added and referenced via `instrument` or a new `software` slot.

### 3c. `cs` (spherical aberration) — no InstrumentEntity slot

The rocrate `InstrumentEntity` has no slot for spherical aberration Cs (2.7 mm for Krios FEG). This is used in CTF estimation and affects resolution limits. Stored in `runParameters.sphericalAberrationMm`.

**Recommendation:** Add `spherical_aberration_mm` to `InstrumentEntity` (or `CryoEMInstrumentEntity` if a specialised subtype is introduced).

### 3d. `energy_filter_present` — no InstrumentEntity slot

The rocrate `InstrumentEntity` has no boolean slot for energy filter presence or model (Selectris, BioQuantum, GIF). Presence is implied here by `energy_filter_slit` in runParameters, but is not declared on the instrument.

**Recommendation:** Add `energy_filter` (string, name/model) to `InstrumentEntity`.

### 3e. `sample_buffer: 1xTBS` — no SampleEntity slot

Buffer composition (1x TBS) is in `metadata.yaml` but `SampleEntity` in the rocrate profile has no `buffer_composition` slot.

**Recommendation:** Add `buffer_composition` (free-text or controlled) to `SampleEntity` in the rocrate profile.

### 3f. `vitrification_settings` — missing and out of scope

The metadata.yaml field is a placeholder (`'insert setting here'`). Even if populated, this belongs on `SamplePreparation`, which is not part of the rocrate manifest tier. Declared `missing` on the root with `reason: "not-available"`.

### 3g. Null fields omitted

The following fields from metadata.yaml are null in the source and are omitted from the crate (null → absent is the correct mapping):

`nominal_dose_rate_eps`, `frames_per_second`, `fiducial_size`, `tilt_angle_increment`, `rotation_rate`, `nominal_camera_Length`

The last two (`rotation_rate`, `nominal_camera_Length`) are only relevant for tomography and microED respectively. They should remain absent for SPA sessions.

---

## 4. Structural Decisions

### 4a. InstrumentEntity is restricted vs main schema

The rocrate `InstrumentEntity` is intentionally narrow — it carries only identity and affiliation fields, not acquisition parameters. Fields like `accelerating_voltage`, `detector_manufacturer`, `cs_corrector`, `pixel_size_physical_um`, and `phase_plate` exist on `CryoEMInstrument` in the main schema but are not allowed on the rocrate `InstrumentEntity`.

**Decision:** All cryo-EM-specific acquisition parameters are in `runParameters`. This is consistent with the rocrate profile design intent. If per-instrument parameters are needed, they belong in a linked instrument record, not the crate manifest.

### 4b. Folder dataset entities (`frames/`, `screening/`)

Both are modeled as `Dataset` entities representing groups of related files. They carry `missing` declarations for `sha256` (binary stubs) and `schemaRecord` (metadata carried by sidecar mdocs). Each individual file within the folder also has its own `CrateFile` entity — the dataset entity is a navigational grouping, not a replacement.

### 4c. Multiple magnification tiers

A single SerialEM session typically spans 3–4 magnification tiers (atlas ~135x, survey ~740x, screening ~11500x, acquisition ~130000x). The schema has one `magnification` slot on `ExperimentRun` — used here for the acquisition magnification (130000x, the science-relevant tier). Lower magnification images are included as files but their magnification is captured only in their mdoc sidecars and in `runParameters`.

**Recommendation:** Consider a `magnification_tiers` list or per-file `magnification` slot on `CrateFile` for multi-mag sessions.

### 4d. `experiment_date` not in ExperimentRunAction

`experiment_date` does not appear as an allowed slot on `ExperimentRunAction` in the compiled schema (though it is in the YAML definition). The crate does not include it. The session date is anonymised as `2001-01-01` in the mdoc `DateTime` fields regardless.

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
| OQ-1 | Is `collection_mode: "single_particle"` the exact enum value, or is it `spa`? | Layer 2 validation could re-fail if wrong | Grep CollectionModeEnum in main schema and verify |
| OQ-2 | What licence applies to EMSL fixture data for public distribution? | `license` field on root currently set to CC-BY 4.0 | Confirm with EMSL/data team before publishing |
| OQ-3 | Should `s1Findable: true` require a resolvable identifier? With fake `proposal_id: 99999`, the fixture arguably fails findability. | sufficiency block | Change to `false` or add a note field to sufficiency; current crate uses `false` already |
| OQ-4 | Atlas and survey `.mrc` stubs are `data_type: "micrograph"`. Is this correct for navigational low-mag images, or should a new term (e.g. `atlas_tile`, `survey_image`) be added? | FileFormatEnum / data_type enum | Discuss with schema team; `micrograph` is defensible but imprecise |
| OQ-5 | The `assesments` typo in `metadata.yaml` (one 's') — should the fixture preserve source fidelity or be corrected? | Source fidelity vs correctness | Fix the typo since we control the fixture; done in this branch |
| OQ-6 | EPU equivalent: EPU sessions have Atlas/GridSquare/FoilHole nested folders. Would the crate structure differ? | Future fixture scope | Yes — EPU would use nested `Dataset` entities. SerialEM's flat-by-type structure is simpler to map. |
| OQ-7 | `calibratedPixelSizeAngstrom: 0.340292` appears in mdoc headers but not in metadata.yaml. Should it be a CrateFile-level annotation or stay in runParameters? | Data discovery | Consider adding `calibrated_pixel_size` as a slot on CrateFile for micrograph/movie files |

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
