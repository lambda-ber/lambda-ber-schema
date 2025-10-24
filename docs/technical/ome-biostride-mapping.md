# Technical Mapping: OME to lambda-ber-schema

## Overview

This document provides detailed technical mappings between OME (Open Microscopy Environment) data model elements and corresponding lambda-ber-schema schema components, with code examples and implementation guidance.

## Core Entity Mappings

### Image Entities

#### OME Image → lambda-ber-schema Image Classes

**OME XML:**
```xml
<Image ID="Image:0" Name="example.tif">
  <AcquisitionDate>2024-01-15T10:30:00</AcquisitionDate>
  <Description>Sample fluorescence image</Description>
  <Pixels ID="Pixels:0" Type="uint16" SizeX="1024" SizeY="1024" SizeZ="1" SizeC="2" SizeT="1">
    <Channel ID="Channel:0:0" Name="GFP" ExcitationWavelength="488" EmissionWavelength="520"/>
    <Channel ID="Channel:0:1" Name="DAPI" ExcitationWavelength="358" EmissionWavelength="461"/>
  </Pixels>
</Image>
```

**lambda-ber-schema YAML:**
```yaml
images:
  - id: img:fluor-001
    _type: FluorescenceImage
    title: "Sample fluorescence image"
    file_name: "example.tif"
    acquisition_date: "2024-01-15T10:30:00"
    dimensions_x: 1024
    dimensions_y: 1024
    pixel_type: uint16
    excitation_wavelength: 488  # Primary channel
    emission_wavelength: 520
    fluorophore: "GFP"
    channels:  # Extension for multi-channel
      - name: "GFP"
        excitation: 488
        emission: 520
      - name: "DAPI"
        excitation: 358
        emission: 461
```

### Instrument Specifications

#### OME Instrument → lambda-ber-schema Instrument

**OME XML:**
```xml
<Instrument ID="Instrument:0">
  <Microscope Type="Inverted" Model="Nikon Ti-E"/>
  <Objective ID="Objective:0" Model="Plan Apo" NominalMagnification="60" LensNA="1.4"/>
  <Detector ID="Detector:0" Type="sCMOS" Model="Hamamatsu ORCA-Flash4.0"/>
  <LightSource ID="LightSource:0" Type="Laser" Model="Coherent Obis" Power="100" PowerUnit="mW">
    <Laser Wavelength="488"/>
  </LightSource>
</Instrument>
```

**lambda-ber-schema Equivalent (extending for compatibility):**
```yaml
instruments:
  - id: instrument:microscope-001
    _type: OpticalMicroscope  # New subclass for OME compatibility
    instrument_code: "Nikon-Ti-E-001"
    manufacturer: "Nikon"
    model: "Ti-E"
    microscope_type: "Inverted"
    objective:
      model: "Plan Apo"
      magnification: 60
      numerical_aperture: 1.4
    detector_type: cmos  # Maps to OME sCMOS
    detector_model: "Hamamatsu ORCA-Flash4.0"
    light_source:
      type: "Laser"
      model: "Coherent Obis"
      power: 100
      power_unit: "mW"
      wavelength: 488
```

### Sample and Experiment Context

#### OME Experiment → lambda-ber-schema Study/ExperimentRun

**OME XML:**
```xml
<Experiment ID="Experiment:0" Type="FluorescenceLifetime">
  <Description>Time-resolved fluorescence study</Description>
  <Experimenter ID="Experimenter:0" FirstName="Jane" LastName="Doe" Email="jane.doe@example.org"/>
</Experiment>
```

**lambda-ber-schema YAML:**
```yaml
studies:
  - id: study:fluorescence-001
    title: "Time-resolved fluorescence study"
    principal_investigator: "Jane Doe"
    contact_email: "jane.doe@example.org"
    
    experiment_runs:
      - id: exp:fluor-lifetime-001
        experiment_code: "FLIM-2024-001"
        technique: fluorescence_lifetime  # Extended enum
        experimenter: "Jane Doe"
        experimental_conditions:
          temperature: 37
          temperature_unit: celsius
```

## Advanced Mappings

### Multi-Dimensional Data

#### OME 5D Data (XYZCT) → lambda-ber-schema Multi-Frame Images

**OME Representation:**
```xml
<Pixels SizeX="512" SizeY="512" SizeZ="30" SizeC="3" SizeT="100" Type="uint16">
  <Plane TheZ="0" TheC="0" TheT="0" ExposureTime="100" ExposureTimeUnit="ms"/>
  <!-- ... more planes ... -->
</Pixels>
```

**lambda-ber-schema Extension:**
```yaml
images:
  - id: img:timelapse-001
    _type: Image3D  # Or new Image4D/Image5D classes
    dimensions_x: 512
    dimensions_y: 512
    dimensions_z: 30
    dimensions_t: 100  # Time points
    dimensions_c: 3    # Channels
    pixel_type: uint16
    temporal_resolution: 0.1  # seconds between frames
    z_step: 0.5  # micrometers
    channels:
      - {name: "GFP", wavelength: 520}
      - {name: "RFP", wavelength: 580}
      - {name: "DAPI", wavelength: 461}
```

### ROI (Regions of Interest)

#### OME ROI → lambda-ber-schema Annotation Extension

**OME XML:**
```xml
<ROI ID="ROI:0">
  <Union>
    <Shape ID="Shape:0" Type="Rectangle" X="100" Y="100" Width="50" Height="50"/>
    <Shape ID="Shape:1" Type="Polygon" Points="200,200 250,200 225,250"/>
  </Union>
</ROI>
```

**lambda-ber-schema Proposed Extension:**
```yaml
annotations:  # New field for Study or Image
  - id: roi:001
    type: rectangle
    coordinates: {x: 100, y: 100, width: 50, height: 50}
    label: "Cell nucleus"
  - id: roi:002
    type: polygon
    points: [[200,200], [250,200], [225,250]]
    label: "Mitochondria"
```

## Format Conversions

### OME-TIFF ↔ lambda-ber-schema Integration

```python
# Pseudo-code for conversion
from bioformats import load_image_metadata
from lambda-ber-schema import FluorescenceImage

def ome_to_lambda-ber-schema(ome_tiff_path):
    """Convert OME-TIFF to lambda-ber-schema data model"""
    
    # Read OME-XML from TIFF header
    ome_xml = load_image_metadata(ome_tiff_path)
    
    # Create lambda-ber-schema image
    image = FluorescenceImage(
        id=f"img:{ome_xml.image_id}",
        file_name=ome_tiff_path,
        acquisition_date=ome_xml.acquisition_date,
        dimensions_x=ome_xml.size_x,
        dimensions_y=ome_xml.size_y,
        pixel_type=ome_xml.pixel_type
    )
    
    # Map channels
    if ome_xml.channels:
        primary = ome_xml.channels[0]
        image.excitation_wavelength = primary.excitation
        image.emission_wavelength = primary.emission
        image.fluorophore = primary.name
    
    return image
```

### Bio-Formats Reader Integration

```python
def create_bioformats_reader():
    """Create Bio-Formats reader for lambda-ber-schema images"""
    
    class lambda-ber-schemaReader:
        def read_fluorescence_image(self, lambda-ber-schema_image):
            # Convert to OME model
            ome_image = {
                'ID': lambda-ber-schema_image.id,
                'Name': lambda-ber-schema_image.file_name,
                'AcquisitionDate': lambda-ber-schema_image.acquisition_date,
                'Pixels': {
                    'SizeX': lambda-ber-schema_image.dimensions_x,
                    'SizeY': lambda-ber-schema_image.dimensions_y,
                    'Channels': [{
                        'ExcitationWavelength': lambda-ber-schema_image.excitation_wavelength,
                        'EmissionWavelength': lambda-ber-schema_image.emission_wavelength,
                        'Name': lambda-ber-schema_image.fluorophore
                    }]
                }
            }
            return ome_image
```

## Metadata Harmonization

### Common Fields Mapping Table

| OME Path | lambda-ber-schema Path | Type | Notes |
|----------|----------------|------|-------|
| Image/@ID | Image/id | string | Identifier |
| Image/@Name | Image/title | string | Human-readable name |
| Image/AcquisitionDate | Image/acquisition_date | datetime | ISO 8601 format |
| Pixels/@SizeX | Image/dimensions_x | integer | Width in pixels |
| Pixels/@SizeY | Image/dimensions_y | integer | Height in pixels |
| Pixels/@SizeZ | Image3D/dimensions_z | integer | Depth/slices |
| Pixels/@Type | Image/pixel_type | enum | uint8/uint16/float32 |
| Channel/@ExcitationWavelength | FluorescenceImage/excitation_wavelength | float | Nanometers |
| Channel/@EmissionWavelength | FluorescenceImage/emission_wavelength | float | Nanometers |
| Objective/@NominalMagnification | OpticalImage/magnification | float | Magnification factor |
| Detector/@Type | Instrument/detector_type | enum | CCD/CMOS/PMT |
| Plane/@ExposureTime | ExperimentalConditions/exposure_time | float | With unit |

### Structural Biology Extensions

lambda-ber-schema extends beyond OME for structural biology:

| lambda-ber-schema Path | Purpose | No OME Equivalent |
|----------------|---------|-------------------|
| CryoEMInstrument/voltage | Electron beam voltage | ✓ |
| Image2D/defocus | CTF correction parameter | ✓ |
| SAXSInstrument/q_range_* | Scattering vector range | ✓ |
| WorkflowRun/processing_level | Data processing stage | ✓ |
| MolecularComposition/sequences | Protein/DNA sequences | ✓ |
| Sample/sample_code | Laboratory identifier | Partial (via annotations) |

## Implementation Guidelines

### 1. Creating OME-Compatible lambda-ber-schema Data

```yaml
# Template for OME-compatible fluorescence microscopy in lambda-ber-schema
studies:
  - id: study:ome-compatible
    samples:
      - id: sample:cells-001
        sample_code: "HeLa-GFP-001"
        sample_type: complex  # Cell line
        molecular_composition:
          ligands: ["GFP-tagged protein X"]
          
    images:
      - id: img:fluor-001
        _type: FluorescenceImage
        file_name: "hela_gfp_timelapse.ome.tiff"  # OME-TIFF format
        acquisition_date: "2024-01-15T10:30:00Z"
        dimensions_x: 2048
        dimensions_y: 2048
        pixel_type: uint16
        pixel_size: 0.065  # micrometers, maps to OME PhysicalSizeX
        excitation_wavelength: 488
        emission_wavelength: 520
        fluorophore: "eGFP"
        exposure_time: 100  # milliseconds
```

### 2. OMERO Integration Strategy

```python
# Upload lambda-ber-schema images to OMERO
def upload_to_omero(lambda-ber-schema_study):
    import omero.gateway
    
    conn = omero.gateway.BlitzGateway(...)
    
    for image in lambda-ber-schema_study.images:
        if isinstance(image, FluorescenceImage):
            # Direct upload for OME-compatible types
            omero_image = conn.createImageFromFile(image.file_path)
            
            # Add lambda-ber-schema-specific metadata as key-value pairs
            map_ann = omero.gateway.MapAnnotationWrapper()
            map_ann.setValue([
                ["lambda-ber-schema:study_id", lambda-ber-schema_study.id],
                ["lambda-ber-schema:sample_code", image.sample.sample_code],
                ["lambda-ber-schema:technique", "fluorescence"]
            ])
            omero_image.linkAnnotation(map_ann)
```

### 3. Validation Rules

```python
# Ensure OME compatibility
def validate_ome_compatibility(image):
    """Check if lambda-ber-schema image can be exported to OME"""
    
    compatible = True
    issues = []
    
    # Required OME fields
    if not image.dimensions_x or not image.dimensions_y:
        compatible = False
        issues.append("Missing pixel dimensions")
    
    if isinstance(image, FluorescenceImage):
        if not image.excitation_wavelength:
            issues.append("Missing excitation wavelength for fluorescence")
    
    # Pixel type must be OME-compatible
    ome_types = ['uint8', 'uint16', 'uint32', 'float32', 'float64']
    if image.pixel_type not in ome_types:
        compatible = False
        issues.append(f"Pixel type {image.pixel_type} not OME-compatible")
    
    return compatible, issues
```

## Use Cases

### 1. Correlative Light and Electron Microscopy (CLEM)

```yaml
studies:
  - id: study:clem-001
    title: "Correlative fluorescence and cryo-EM study"
    
    samples:
      - id: sample:protein-complex
        sample_code: "RuBisCO-AF488"
        sample_type: complex
        
    images:
      # Fluorescence (OME-compatible)
      - id: img:fluor-rubisco
        _type: FluorescenceImage
        file_name: "rubisco_af488.ome.tiff"
        excitation_wavelength: 488
        emission_wavelength: 520
        fluorophore: "Alexa Fluor 488"
        
      # Cryo-EM (lambda-ber-schema-specific)
      - id: img:cryoem-rubisco
        _type: Image2D
        file_name: "rubisco_micrograph.mrc"
        defocus: -2.5
        pixel_size: 1.06
        
    # Cross-reference between modalities
    correlations:
      - fluorescence_image: img:fluor-rubisco
        cryoem_image: img:cryoem-rubisco
        registration_matrix: [[1,0,0],[0,1,0],[0,0,1]]
```

### 2. High-Content Screening Integration

```yaml
# OME-style plate/well structure in lambda-ber-schema
studies:
  - id: study:hcs-001
    title: "High-content drug screening"
    
    plates:  # Extension for OME Plate/Well model
      - id: plate:001
        rows: 8
        columns: 12
        wells:
          - id: well:A01
            sample_id: sample:compound-001
            images: [img:A01-t00, img:A01-t01, ...]
```

## Future Development

### Proposed Schema Extensions

1. **Add OME-specific image subclass:**
```yaml
classes:
  OMEImage:
    is_a: Image
    description: "OME-compatible microscopy image"
    attributes:
      ome_xml: string  # Embedded OME-XML metadata
      bio_formats_version: string
```

2. **Channel collection for multi-channel imaging:**
```yaml
attributes:
  channels:
    range: Channel
    multivalued: true
    description: "Multiple acquisition channels"
    
classes:
  Channel:
    attributes:
      name: string
      excitation_wavelength: float
      emission_wavelength: float
      exposure_time: float
```

3. **Time series support:**
```yaml
attributes:
  time_points:
    range: TimePoint
    multivalued: true
    
classes:
  TimePoint:
    attributes:
      index: integer
      timestamp: datetime
      delta_t: float  # Seconds from start
```

## Conclusion

This technical mapping demonstrates that lambda-ber-schema can achieve strong interoperability with OME while extending the model for structural biology needs. Key implementation priorities include:

1. Ensuring base compatibility for shared concepts
2. Creating translation layers for format conversion
3. Developing validation tools for OME compliance
4. Building OMERO integration adapters
5. Contributing structural biology extensions back to OME community

The alignment enables researchers to use familiar OME tools while benefiting from lambda-ber-schema's structural biology capabilities.