# ISPyB Integration TODO

## Overview

ISPyB (Information System for Protein crystallography Beamlines) is a LIMS used at major synchrotron facilities (ESRF, Diamond, MAX IV, SOLEIL, ALBA). This document tracks integration work to enable interoperability between lambda-ber-schema and ISPyB.

## References

- [ISPyB Database (Diamond)](https://github.com/DiamondLightSource/ispyb-database)
- [ISPyB Database Modeling](https://github.com/ispyb/ispyb-database-modeling)
- [py-ispyb Python API](https://github.com/ispyb/py-ispyb)
- [ISPyB Publication](https://academic.oup.com/bioinformatics/article/27/22/3186/195018)
- [SynchWeb Interface](https://pmc.ncbi.nlm.nih.gov/articles/PMC4453979/)

## ISPyB Variants

There are two main ISPyB implementations that have diverged over time:

| Variant | Repository | Used At | Notes |
|---------|------------|---------|-------|
| **Diamond ISPyB** | `DiamondLightSource/ispyb-database` | Diamond Light Source | Original reference implementation |
| **Community ISPyB** | `ispyb/ispyb-database-modeling` | ESRF, MAX IV, SOLEIL, ALBA | Multi-facility collaboration, more active schema development |

The core schema (DataCollection, AutoProc*, BLSample, etc.) is shared, but extensions and APIs differ. The `py-ispyb` Python API primarily targets the community version.

For lambda-ber-schema integration, the mappings should work with both variants since they target the common core schema elements.

## Completed Tasks

### 1. Schema Annotations (Priority: High) - DONE

Added `ispyb:` prefix and exact_mappings to enable semantic interoperability.

- [x] Add `ispyb` prefix to schema (`ispyb: https://ispyb.github.io/ISPyB/`)
- [x] Add ISPyB mappings to ExperimentRun fields
- [x] Add ISPyB mappings to WorkflowRun fields

### 2. ISPyB-Compatible Fields Added - DONE

#### ExperimentRun (New Fields)
- [x] `transmission` - X-ray beam transmission percentage (0-100)
- [x] `flux` - Photon flux (photons/second)
- [x] `flux_end` - Flux at end of collection
- [x] `slit_gap_horizontal` - Horizontal slit aperture (µm)
- [x] `slit_gap_vertical` - Vertical slit aperture (µm)
- [x] `undulator_gap` - Undulator gap setting (mm)
- [x] `synchrotron_mode` - Storage ring fill mode
- [x] `exposure_time` - Exposure time per image (s)
- [x] `start_time` / `end_time` - Data collection timestamps
- [x] `resolution` - Resolution at detector edge (Å)
- [x] `resolution_at_corner` - Resolution at detector corner (Å)
- [x] `ispyb_data_collection_id` - Cross-reference to ISPyB
- [x] `ispyb_session_id` - Cross-reference to ISPyB session

#### WorkflowRun (New Fields)
- [x] `anomalous_completeness` - Completeness of anomalous data
- [x] `anomalous_multiplicity` - Multiplicity of anomalous data
- [x] `cc_anomalous` - Anomalous correlation coefficient (ccAno)
- [x] `r_anomalous` - Anomalous R-factor (rAnom)
- [x] `sig_anomalous` - Mean anomalous signal (sigAno)
- [x] `n_total_observations` - Total observations before merging
- [x] `n_total_unique` - Total unique reflections
- [x] `ispyb_auto_proc_program_id` - Cross-reference to ISPyB
- [x] `ispyb_auto_proc_scaling_id` - Cross-reference to ISPyB

### 3. ISPyB Mappings Added to Existing Fields - DONE

ExperimentRun fields with new `ispyb:DataCollection.*` mappings:
- wavelength, oscillation_angle, start_angle, number_of_images
- beam_center_x, beam_center_y, detector_distance
- beamline (→ ispyb:BLSession.beamLineName)

WorkflowRun fields with new `ispyb:AutoProcScalingStatistics.*` mappings:
- space_group (→ ispyb:AutoProcScaling.spaceGroup)
- resolution_high, resolution_low
- rmerge, rpim, cc_half, completeness_percent
- i_over_sigma, multiplicity

## Remaining Tasks

### Sample/Container Tracking (Priority: Medium)

Fields for sample logistics (not yet implemented):

- [ ] Container class for sample holders (pucks, plates)
- [ ] Dewar class for shipping containers
- [ ] Shipment tracking metadata
- [ ] Add `ispyb_bl_sample_id` to Sample

### Validation Examples (Priority: Low)

- [ ] Create example with full ISPyB field coverage
- [ ] Test round-trip conversion ISPyB → lambda-ber-schema → ISPyB

### Future: Conversion Utilities (Priority: Low)

- [ ] Python utility: ISPyB SQL → YAML export
- [ ] Python utility: YAML → ISPyB SQL import
- [ ] Integration with py-ispyb API

## Entity Mapping Reference

| ISPyB Table | lambda-ber-schema | Notes |
|-------------|-------------------|-------|
| BLSession | Study | Beamline visit session |
| Protein | ProteinConstruct | Protein metadata |
| Crystal | Sample | Crystal with space group |
| BLSample | Sample | Physical sample |
| DataCollection | ExperimentRun | Data collection run |
| DataCollectionGroup | - | No direct equivalent |
| Image | Image2D/DataFile | Diffraction images |
| AutoProcProgram | WorkflowRun | Processing software |
| AutoProcIntegration | WorkflowRun | Integration results |
| AutoProcScalingStatistics | WorkflowRun | Scaling statistics |
| PhasingStep | WorkflowRun | Phasing workflow |

## Field Mapping Reference

### DataCollection → ExperimentRun

| ISPyB | lambda-ber-schema | Status |
|-------|-------------------|--------|
| wavelength | wavelength | ✅ Mapped |
| detectorDistance | detector_distance | ✅ Mapped |
| numberOfImages | number_of_images | ✅ Mapped |
| axisStart | start_angle | ✅ Mapped |
| axisRange | oscillation_angle | ✅ Mapped |
| xBeam/yBeam | beam_center_x/y | ✅ Mapped |
| resolution | resolution | ✅ Added |
| resolutionAtCorner | resolution_at_corner | ✅ Added |
| exposureTime | exposure_time | ✅ Added |
| transmission | transmission | ✅ Added |
| flux | flux | ✅ Added |
| flux_end | flux_end | ✅ Added |
| slitGapHorizontal | slit_gap_horizontal | ✅ Added |
| slitGapVertical | slit_gap_vertical | ✅ Added |
| undulatorGap1 | undulator_gap | ✅ Added |
| synchrotronMode | synchrotron_mode | ✅ Added |
| startTime | start_time | ✅ Added |
| endTime | end_time | ✅ Added |
| dataCollectionId | ispyb_data_collection_id | ✅ Added |

### AutoProcScalingStatistics → WorkflowRun

| ISPyB | lambda-ber-schema | Status |
|-------|-------------------|--------|
| resolutionLimitLow/High | resolution_low/high | ✅ Mapped |
| rMerge | rmerge | ✅ Mapped |
| rPim | rpim | ✅ Mapped |
| completeness | completeness_percent | ✅ Mapped |
| multiplicity | multiplicity | ✅ Mapped |
| meanIOverSigI | i_over_sigma | ✅ Mapped |
| ccHalf | cc_half | ✅ Mapped |
| anomalousCompleteness | anomalous_completeness | ✅ Added |
| anomalousMultiplicity | anomalous_multiplicity | ✅ Added |
| ccAno | cc_anomalous | ✅ Added |
| rAnom | r_anomalous | ✅ Added |
| sigAno | sig_anomalous | ✅ Added |
| nTotalObservations | n_total_observations | ✅ Added |
| nTotalUniqueObservations | n_total_unique | ✅ Added |
| autoProcProgramId | ispyb_auto_proc_program_id | ✅ Added |
| autoProcScalingId | ispyb_auto_proc_scaling_id | ✅ Added |
