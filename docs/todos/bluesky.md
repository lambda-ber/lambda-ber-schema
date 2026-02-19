# Bluesky Integration TODO

## Overview

Bluesky is an event-based data acquisition framework developed at NSLS-II (Brookhaven National Laboratory). It provides a Python-based system for orchestrating experiments, collecting data, and streaming metadata in real-time. Bluesky is increasingly adopted at major synchrotron facilities including ALS, APS, and international sites.

The Bluesky ecosystem includes:
- **bluesky** - Experiment orchestration and run engine
- **ophyd** - Hardware abstraction layer for devices
- **databroker** - Unified data access interface
- **tiled** - Modern data serving with search capabilities
- **event-model** - Core document schema for streaming data

This document tracks integration work to enable interoperability between lambda-ber-schema and the Bluesky event-model.

## References

- [Bluesky Project](https://blueskyproject.io/)
- [Event Model Documentation](https://blueskyproject.io/event-model/)
- [Event Model GitHub](https://github.com/bluesky/event-model)
- [Databroker GitHub](https://github.com/bluesky/databroker)
- [Tiled GitHub](https://github.com/bluesky/tiled)
- [Bluesky Publication](https://doi.org/10.1080/08940886.2019.1608121) - Synchrotron Radiation News, 2019

## Bluesky Document Model

Bluesky uses a streaming document model with these core document types:

| Document | Purpose |
|----------|---------|
| **RunStart** | Marks beginning of a run, contains metadata (plan name, user, sample info, etc.) |
| **RunStop** | Marks end of run, contains exit status and summary |
| **EventDescriptor** | Describes data keys and their properties for a stream |
| **Event** | Contains actual measurement data with timestamps |
| **Resource** | External file reference (HDF5, TIFF, etc.) |
| **Datum** | Pointer into a Resource for specific data |

## Remaining Tasks

### 1. Schema Annotations (Priority: High)

Add `bluesky:` prefix and mappings to enable semantic interoperability.

- [ ] Add `bluesky` prefix to schema (`bluesky: https://blueskyproject.io/event-model/`)
- [ ] Add Bluesky mappings to Study fields (RunStart metadata)
- [ ] Add Bluesky mappings to ExperimentRun fields (Event data)
- [ ] Add Bluesky mappings to DataFile fields (Resource/Datum)

### 2. Bluesky-Compatible Fields (Priority: High)

#### Study (RunStart Metadata)
- [ ] `bluesky_uid` - Unique identifier for the run (maps to RunStart.uid)
- [ ] `plan_name` - Name of the Bluesky plan executed
- [ ] `plan_type` - Type of scan (count, scan, grid_scan, etc.)
- [ ] `scan_id` - Human-readable sequential scan number
- [ ] `time_start` - Unix timestamp of run start

#### ExperimentRun (Event Data)
- [ ] `bluesky_descriptor_uid` - Reference to EventDescriptor
- [ ] `seq_num` - Sequence number within the run
- [ ] `event_timestamp` - Timestamp of the event

#### DataFile (Resource/Datum)
- [ ] `bluesky_resource_uid` - Reference to Resource document
- [ ] `bluesky_datum_id` - Reference to specific Datum
- [ ] `resource_path` - Root path for external files
- [ ] `resource_spec` - Handler specification (e.g., 'AD_HDF5', 'NPY_SEQ')

### 3. Device/Signal Mapping (Priority: Medium)

Map ophyd device hierarchy to Instrument classes:

- [ ] Consider adding generic `device_name` and `signal_name` fields
- [ ] Map motor positions to experimental conditions
- [ ] Map detector configurations to instrument settings
- [ ] Support for area detector (AD) metadata

### 4. Stream Support (Priority: Medium)

Bluesky supports multiple data streams per run (primary, baseline, monitors):

- [ ] Consider how to represent multiple streams in a Study
- [ ] Map baseline readings (pre/post scan snapshots)
- [ ] Support monitor streams (asynchronous readings)

### 5. Validation Examples (Priority: Low)

- [ ] Create example with full Bluesky field coverage
- [ ] Create example from real ALS Bluesky data (SIBYLS is a good candidate - existing examples in repo)
- [ ] Test conversion from databroker export
- [ ] Extend existing `SAXSInstrument-sibyls.yaml` and `BeamlineInstrument-sibyls.yaml` with Bluesky fields

### 6. Conversion Utilities (Priority: Low)

- [ ] Python utility: databroker → lambda-ber-schema YAML export
- [ ] Python utility: lambda-ber-schema → Bluesky documents (for replay)
- [ ] Integration with tiled for serving lambda-ber-schema data

## Entity Mapping Reference

| Bluesky Document | lambda-ber-schema | Notes |
|------------------|-------------------|-------|
| RunStart | Study | Run-level metadata, sample info |
| RunStop | Study | Exit status, num_events summary |
| EventDescriptor | - | Describes data stream schema |
| Event | ExperimentRun | Measurement data points |
| Resource | DataFile | External file references |
| Datum | DataFile | Specific data within Resource |
| - | Sample | Bluesky stores in RunStart metadata |
| - | Instrument | Bluesky stores in RunStart metadata |

## Field Mapping Reference

### RunStart → Study

| Bluesky | lambda-ber-schema | Notes |
|---------|-------------------|-------|
| uid | bluesky_uid | 36-char UUID |
| time | - | Unix timestamp |
| plan_name | plan_name | e.g., "count", "scan" |
| plan_type | plan_type | Plan category |
| scan_id | - | Sequential integer |
| owner | principal_investigator | User who ran scan |
| project | project_code | Project identifier |
| sample | samples[].sample_code | Sample metadata dict |
| detectors | - | List of detector names |
| motors | - | List of motor names |

### Event → ExperimentRun

| Bluesky | lambda-ber-schema | Notes |
|---------|-------------------|-------|
| descriptor | bluesky_descriptor_uid | Reference to schema |
| seq_num | - | Event sequence number |
| time | - | Unix timestamp |
| data | - | Dict of readings |
| timestamps | - | Per-key timestamps |
| filled | - | External data status |

### Resource → DataFile

| Bluesky | lambda-ber-schema | Notes |
|---------|-------------------|-------|
| uid | bluesky_resource_uid | Resource identifier |
| spec | resource_spec | Handler name |
| root | - | Root path |
| resource_path | file_path | Relative path |
| resource_kwargs | - | Handler arguments |

## Integration Considerations

### Event-Based vs. Run-Based Models

Bluesky's event model is inherently streaming/event-based, while lambda-ber-schema is more run-based. Consider:

1. **Aggregation**: Multiple Bluesky Events may map to a single ExperimentRun
2. **Time series**: Bluesky Events with timestamps could map to repeated measurements
3. **Scan types**: Different Bluesky plans (step scan, fly scan, count) may need different mappings

### Metadata Flexibility

Bluesky's RunStart accepts arbitrary user metadata. Consider:

1. **Structured fields**: Map common fields (sample, user, proposal) to schema slots
2. **Extension mechanism**: Handle facility-specific or beamline-specific metadata
3. **Validation**: Balance flexibility with schema validation

### External Data References

Bluesky's Resource/Datum system handles large external files (HDF5, TIFF stacks):

1. **File formats**: Support common area detector formats (HDF5, TIFF, CBF)
2. **Lazy loading**: Maintain references without embedding data
3. **Checksum**: Consider adding checksums for data integrity

## Facility Adoption

Facilities using or adopting Bluesky:

| Facility | Status | Notes |
|----------|--------|-------|
| NSLS-II | Production | Origin of Bluesky development |
| ALS | Production | SIBYLS (12.3.1) and other beamlines |
| APS | Adopting | APS-U upgrade includes Bluesky |
| Diamond | Evaluating | Pilot projects underway |
| ESRF | Evaluating | Some beamlines testing |
| MAX IV | Adopting | Production on some beamlines |

### ALS Beamlines Using Bluesky

| Beamline | Techniques | Notes |
|----------|------------|-------|
| SIBYLS (12.3.1) | SAXS, SEC-SAXS, crystallography | High-throughput with mail-in service |

## Related Work

- **ISPyB integration** (`docs/todos/ispyb.md`): Complementary - ISPyB for MX LIMS, Bluesky for data acquisition
- **NeXus alignment** (`docs/background/nexus.md`): Bluesky can write NeXus/HDF5 via suitcase-nexus
- **NSLS2 integration** (`docs/ideas/nsls2-integration.md`): Overlaps - NSLS2 metadata could come from Bluesky

## Contact

For questions about Bluesky:
- Bluesky project: bluesky@bnl.gov
- NSLS-II Data Science: Dan Allan (dallan@bnl.gov)
- Documentation: https://blueskyproject.io/
