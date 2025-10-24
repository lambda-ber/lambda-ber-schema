# lambda-ber-schema and DIALS Alignment Analysis

> **Note**: This document was generated using Claude (Anthropic's AI assistant) through automated analysis of documentation and web sources. While efforts have been made to ensure accuracy, there may be errors or outdated information. Please verify critical details with official DIALS documentation.

## Overview

This document analyzes the alignment between the lambda-ber-schema schema and DIALS (Diffraction Integration for Advanced Light Sources), examining how lambda-ber-schema can integrate with and complement this modern crystallography data processing framework.

## Introduction to DIALS

### What is DIALS?

DIALS is an open-source software framework for processing X-ray diffraction data. Key characteristics:

- **Purpose**: Automated processing of crystallographic diffraction data
- **Architecture**: Modular toolkit written in Python and C++
- **Scope**: Supports synchrotron, XFEL, electron, neutron diffraction
- **Philosophy**: Extensible framework allowing algorithm development
- **Integration**: Built on cctbx crystallographic libraries

### Core Components

1. **dxtbx** (Diffraction Experiment Toolbox)
   - Handles experimental geometry
   - Reads diverse detector formats
   - Manages experimental models

2. **Processing Pipeline**
   - `dials.import`: Import raw images
   - `dials.find_spots`: Spot finding
   - `dials.index`: Lattice determination
   - `dials.refine`: Geometry refinement
   - `dials.integrate`: Intensity extraction
   - `dials.scale`: Data scaling/merging

3. **Data Model**
   - Experiments (.expt): JSON format experimental geometry
   - Reflections (.refl): MessagePack format reflection data
   - Supports any detector/beamline configuration

### Current Status (2024-2025)

- **Adoption**: Standard at many synchrotrons worldwide
- **Extensions**: Laue-DIALS for polychromatic data
- **Electron Diffraction**: 3D ED support for chemical crystallography
- **Serial Crystallography**: SSX and XFEL data processing
- **Integration**: Part of CCP4, conda-forge distributions

## DIALS Data Model

### Experiments File Structure

The `.expt` file contains experimental metadata in JSON:

```json
{
  "experiment": [{
    "identifier": "unique_id",
    "beam": {
      "wavelength": 0.9795,
      "direction": [0.0, 0.0, 1.0]
    },
    "detector": {
      "panels": [{
        "origin": [-100.0, -100.0, -100.0],
        "fast_axis": [1.0, 0.0, 0.0],
        "slow_axis": [0.0, 1.0, 0.0],
        "pixel_size": [0.172, 0.172]
      }]
    },
    "goniometer": {
      "rotation_axis": [1.0, 0.0, 0.0]
    },
    "scan": {
      "oscillation": [0.0, 1.0],
      "image_range": [1, 360]
    },
    "crystal": {
      "unit_cell": [78.84, 78.84, 38.29, 90.0, 90.0, 90.0],
      "space_group": "P43212"
    }
  }],
  "imageset": [{
    "template": "/data/images/image_####.cbf"
  }]
}
```

### Reflections Data Structure

The `.refl` file contains reflection data in MessagePack format with columns:

- **miller_index**: HKL indices
- **xyzobs.px.value**: Observed pixel coordinates
- **intensity.sum.value**: Integrated intensity
- **intensity.sum.variance**: Intensity variance
- **flags**: Processing status flags

## lambda-ber-schema-DIALS Alignment

### Structural Mapping

| DIALS Concept | lambda-ber-schema Equivalent | Alignment Notes |
|---------------|---------------------|-----------------|
| **Experiment** | **ExperimentRun** | ✅ Single data collection session |
| **Beam** | **XRayInstrument.beam_energy** | Wavelength/energy parameters |
| **Detector** | **XRayInstrument.detector_type** | Detector specifications |
| **Goniometer** | **XRayInstrument.goniometer_type** | Rotation apparatus |
| **Crystal** | **Sample + XRayPreparation** | ✅ Crystal properties and preparation |
| **Scan** | **DataCollectionStrategy** | ✅ Oscillation parameters |
| **Reflections** | **DataFile** (type: reflections) | Processed reflection data |
| **ImageSet** | **DataFile** (type: diffraction) | Raw diffraction images |

### Workflow Alignment

#### DIALS Processing Pipeline

```bash
# DIALS workflow
dials.import /data/*.cbf
dials.find_spots imported.expt
dials.index imported.expt strong.refl
dials.refine indexed.expt indexed.refl
dials.integrate refined.expt refined.refl
dials.scale integrated.expt integrated.refl
```

#### lambda-ber-schema Workflow Tracking

```yaml
WorkflowRun:
  - workflow_type: import
    software_name: "DIALS"
    software_version: "3.18.0"
    processing_parameters: "template=/data/*.cbf"
    output_files:
      - file_name: "imported.expt"
        data_type: metadata
        
  - workflow_type: spot_finding
    processing_parameters: "threshold=5 min_spot_size=3"
    output_files:
      - file_name: "strong.refl"
        data_type: spots
        
  - workflow_type: indexing
    processing_parameters: "method=fft3d space_group=P43212"
    output_files:
      - file_name: "indexed.expt"
      - file_name: "indexed.refl"
```

## Key Integration Points

### 1. Experimental Metadata

**DIALS Experiment:**
```python
from dxtbx.model.experiment_list import ExperimentList
experiments = ExperimentList.from_file("indexed.expt")
exp = experiments[0]
wavelength = exp.beam.get_wavelength()
unit_cell = exp.crystal.get_unit_cell()
```

**lambda-ber-schema Mapping:**
```yaml
ExperimentRun:
  technique: xray_crystallography
  instrument_id: "beamline_i04"
  experimental_conditions:
    wavelength: 0.9795  # From exp.beam
    
Sample:
  molecular_composition:
    crystal_parameters:
      unit_cell: [78.84, 78.84, 38.29, 90.0, 90.0, 90.0]
      space_group: "P43212"
```

### 2. Processing Parameters

**DIALS Commands with Options:**
```bash
dials.index imported.expt strong.refl \
  method=fft3d \
  space_group=P43212 \
  unit_cell=78,78,38,90,90,90
```

**lambda-ber-schema Capture:**
```yaml
WorkflowRun:
  workflow_type: indexing
  software_name: "DIALS"
  processing_parameters: |
    method: fft3d
    space_group: P43212
    unit_cell: 78,78,38,90,90,90
  quality_metrics:
    indexed_reflections: 45892
    indexing_rate: 0.92
```

### 3. Quality Metrics

**DIALS Output:**
- Resolution estimates
- Completeness statistics
- R-merge values
- CC1/2 correlation

**lambda-ber-schema Tracking:**
```yaml
QualityMetrics:
  resolution: 1.85
  completeness: 98.5
  r_factor: 0.065  # R-merge
  signal_to_noise: 12.4  # I/sigma
```

## Complementary Strengths

### DIALS Strengths

- **Algorithm Development**: Extensible Python/C++ framework
- **Format Support**: Handles any detector format via dxtbx
- **Modern Architecture**: Clean separation of concerns
- **Active Development**: Regular updates and new features
- **Community Tools**: Integration with CCP4, PHENIX

### lambda-ber-schema Strengths

- **Workflow Context**: Complete experimental history
- **Sample Tracking**: From preparation to structure
- **Multi-technique**: Beyond just crystallography
- **Processing History**: Multiple attempts and optimizations
- **Semantic Integration**: Knowledge graph compatibility

## Integration Strategies

### lambda-ber-schema → DIALS Export

```python
def export_to_dials(experiment_run):
    """Generate DIALS experiment from lambda-ber-schema"""
    from dxtbx.model import Beam, Detector, Goniometer
    
    # Create DIALS models from lambda-ber-schema
    beam = Beam()
    beam.set_wavelength(experiment_run.wavelength)
    
    detector = Detector()
    # Map lambda-ber-schema instrument to detector parameters
    
    experiment = {
        "beam": beam.to_dict(),
        "detector": detector.to_dict(),
        "imageset": {
            "template": experiment_run.raw_data_location
        }
    }
    
    return experiment
```

### DIALS → lambda-ber-schema Import

```python
def import_dials_results(expt_file, refl_file):
    """Import DIALS processing into lambda-ber-schema"""
    from dxtbx.model.experiment_list import ExperimentList
    from dials.array_family import flex
    
    experiments = ExperimentList.from_file(expt_file)
    reflections = flex.reflection_table.from_file(refl_file)
    
    workflow_run = {
        "software_name": "DIALS",
        "workflow_type": "integration",
        "processing_parameters": {
            "n_reflections": len(reflections),
            "unit_cell": experiments[0].crystal.get_unit_cell().parameters()
        },
        "output_files": [
            {"file_name": expt_file, "data_type": "metadata"},
            {"file_name": refl_file, "data_type": "reflections"}
        ]
    }
    
    return workflow_run
```

## Advanced Integration Features

### 1. Serial Crystallography Support

Both DIALS and lambda-ber-schema handle serial data:

```yaml
# lambda-ber-schema serial crystallography
ExperimentRun:
  technique: serial_crystallography
  data_collection_strategy:
    collection_mode: still
    total_frames: 10000
    
WorkflowRun:
  software_name: "DIALS"
  workflow_type: "ssx_processing"
  processing_parameters:
    indexing_method: "sequences"
    multi_lattice: true
```

### 2. Electron Diffraction

3D ED support in both systems:

```yaml
ExperimentRun:
  technique: electron_diffraction
  instrument_id: "tem_instrument"
  
WorkflowRun:
  software_name: "DIALS"
  processing_parameters:
    electron_diffraction: true
    thickness_correction: true
```

### 3. Time-Resolved Studies

Track time-resolved experiments:

```yaml
ExperimentRun:
  technique: time_resolved_crystallography
  metadata:
    pump_probe_delay: "100ps"
    laser_wavelength: 532
    
WorkflowRun:
  processing_parameters:
    reference_dataset: "dark_state.expt"
    difference_maps: true
```

## Comparison with Other Packages

### DIALS vs XDS vs CrystFEL

| Feature | DIALS | XDS | CrystFEL | lambda-ber-schema Role |
|---------|-------|-----|----------|----------------|
| **Architecture** | Modular toolkit | Monolithic | Serial-focused | Workflow tracking |
| **Language** | Python/C++ | Fortran | C | Schema/metadata |
| **Extensibility** | High | Limited | Moderate | Integration layer |
| **Serial Data** | Yes | Limited | Optimized | Unified tracking |
| **Format Support** | Extensive | Standard | Serial formats | Format-agnostic |

### Integration Strategy

lambda-ber-schema can track processing with any package:

```yaml
WorkflowRun:
  - software_name: "XDS"
    workflow_type: "integration"
  - software_name: "DIALS"  
    workflow_type: "integration"
  - software_name: "CrystFEL"
    workflow_type: "serial_merge"
```

## Recommended Workflow

### 1. Data Collection
```
lambda-ber-schema: Track sample, crystal preparation, mounting
         ↓
Collect diffraction data at beamline
         ↓
Store metadata in lambda-ber-schema
```

### 2. Processing Pipeline
```
DIALS: Process diffraction data
         ↓
Track each step in lambda-ber-schema WorkflowRun
         ↓
Capture quality metrics
```

### 3. Structure Solution
```
External tools: Phasing, model building
         ↓
Track in lambda-ber-schema WorkflowRun
         ↓
Link to final coordinates
```

### 4. Deposition
```
Generate mmCIF from DIALS + lambda-ber-schema metadata
         ↓
Deposit to PDB
         ↓
Update lambda-ber-schema with PDB ID
```

## Best Practices

### For Crystallographers

1. **Track Everything**: Use lambda-ber-schema for complete experimental record
2. **Parameter Exploration**: Document multiple processing attempts
3. **Quality Metrics**: Capture resolution, completeness at each stage
4. **Version Control**: Track DIALS version for reproducibility

### For Developers

1. **Use dxtbx Models**: Leverage DIALS geometry descriptions
2. **MessagePack Integration**: Read/write reflection tables
3. **JSON Experiments**: Parse and generate experiment files
4. **Pipeline Automation**: Script DIALS commands with lambda-ber-schema tracking

## Future Opportunities

### Technical Developments

1. **Direct Integration**
   - DIALS plugin for lambda-ber-schema export
   - Automatic workflow capture
   - Real-time metric tracking

2. **Enhanced Metadata**
   - Richer processing provenance
   - Algorithm parameter tracking
   - Decision point documentation

3. **Machine Learning**
   - Processing parameter prediction
   - Quality assessment
   - Automated optimization

### Emerging Techniques

- **Pink-beam Laue**: Laue-DIALS integration
- **MicroED**: Enhanced electron diffraction support
- **Multi-crystal**: Complex merging strategies
- **XFEL**: Improved serial processing

## Conclusion

lambda-ber-schema and DIALS form a **complementary ecosystem** for crystallography data management:

- **DIALS** provides state-of-the-art diffraction data processing with:
  - Modern, extensible architecture
  - Comprehensive format support
  - Active algorithm development
  - Community integration

- **lambda-ber-schema** adds comprehensive experimental context through:
  - Sample-to-structure tracking
  - Multi-technique integration
  - Processing provenance
  - Semantic metadata

The optimal strategy involves:
1. Using DIALS for crystallographic data processing
2. Tracking complete workflows in lambda-ber-schema
3. Maintaining processing parameter history
4. Enabling reproducibility through comprehensive documentation

This integration ensures both the processing pipeline (DIALS) and the experimental context (lambda-ber-schema) are properly captured, enabling reproducible crystallographic research and facilitating method development in structural biology.