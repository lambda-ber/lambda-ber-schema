# Neutron Techniques Expansion for LAMBDA-BER Schema

## Overview
While the current schema includes SANS (Small Angle Neutron Scattering), neutron sources at DOE facilities offer many more techniques that provide unique biological insights. This document proposes comprehensive support for neutron-based structural biology methods.

## Why Neutron Techniques Matter

### Unique Capabilities
1. **Hydrogen Visualization**: Neutrons see hydrogen/deuterium clearly
2. **No Radiation Damage**: Non-ionizing radiation preserves samples
3. **Isotope Sensitivity**: Different scattering from H vs D enables contrast variation
4. **Magnetic Properties**: Sensitivity to magnetic moments
5. **Deep Penetration**: Can probe bulk samples and complex environments

### Biological Applications
- Protein hydration and protonation states
- Membrane protein structure in native-like environments
- Drug binding with hydrogen positions
- Protein-DNA/RNA interactions
- Large complex assemblies via contrast matching
- Dynamics from quasi-elastic scattering

## Current Schema Gaps

### Limited Coverage
- Only SANS is explicitly supported
- No neutron crystallography
- No neutron reflectometry
- No quasi-elastic neutron scattering (QENS)
- No neutron imaging/tomography
- Missing deuteration metadata

### Missing Metadata
- Deuteration levels and strategies
- Contrast variation series
- Neutron flux and wavelength
- Sample environment details
- Activation concerns

## Proposed Extensions

### 1. Neutron Technique Enumeration

#### Expand TechniqueEnum
```yaml
TechniqueEnum:
  permissible_values:
    # Existing...
    sans:
      description: Small-angle neutron scattering

    # New neutron techniques
    neutron_crystallography:
      description: Single crystal neutron diffraction
      meaning: CHMO:0000156

    neutron_powder_diffraction:
      description: Powder neutron diffraction
      meaning: CHMO:0000157

    neutron_reflectometry:
      description: Neutron reflection at interfaces
      meaning: CHMO:0000158

    qens:
      description: Quasi-elastic neutron scattering
      meaning: CHMO:0000159

    neutron_spin_echo:
      description: Neutron spin echo spectroscopy
      meaning: CHMO:0000160

    neutron_imaging:
      description: Neutron radiography/tomography

    inelastic_neutron_scattering:
      description: Inelastic neutron spectroscopy

    neutron_triple_axis:
      description: Triple-axis neutron spectroscopy
```

### 2. Neutron-Specific Instrument Class

#### NeutronInstrument
```yaml
NeutronInstrument:
  is_a: Instrument
  description: Neutron scattering/diffraction instrument
  attributes:
    neutron_source_type:
      range: NeutronSourceEnum
      required: true
      description: Type of neutron source

    moderator_type:
      range: ModeratorTypeEnum
      description: Cold/thermal/hot neutron moderator

    neutron_wavelength:
      range: float
      unit: ucum:Angstrom
      description: Neutron wavelength or range

    wavelength_spread:
      range: float
      description: Wavelength resolution (Δλ/λ)

    neutron_flux:
      range: float
      unit: ucum:cm-2.s-1
      description: Neutron flux at sample

    beam_size_h:
      range: float
      unit: ucum:mm
      description: Horizontal beam size

    beam_size_v:
      range: float
      unit: ucum:mm
      description: Vertical beam size

    chopper_system:
      range: string
      description: Description of chopper system

    detector_type:
      range: NeutronDetectorEnum
      description: Type of neutron detector

    collimation:
      range: string
      description: Collimation configuration

    polarization:
      range: boolean
      description: Polarized neutron capability
```

#### NeutronSourceEnum
```yaml
NeutronSourceEnum:
  permissible_values:
    reactor:
      description: Nuclear reactor source

    spallation:
      description: Spallation neutron source

    compact:
      description: Compact accelerator source

    cf252:
      description: Californium-252 source
```

### 3. Deuteration Metadata

#### DeuterationInfo Class
```yaml
DeuterationInfo:
  description: Information about isotopic labeling
  attributes:
    deuteration_strategy:
      range: DeuterationStrategyEnum
      required: true

    global_deuteration_level:
      range: float
      description: Overall D/(H+D) ratio (0-1)

    per_domain_deuteration:
      range: DomainDeuteration
      multivalued: true
      description: Domain-specific labeling

    d2o_percentage:
      range: float
      description: D2O percentage in buffer

    biosynthetic_method:
      range: string
      description: Method for producing deuterated protein

    exchange_conditions:
      range: string
      description: H/D exchange conditions if applicable

    labile_proton_state:
      range: LabileProtonEnum
      description: State of exchangeable protons
```

#### DeuterationStrategyEnum
```yaml
DeuterationStrategyEnum:
  permissible_values:
    uniform:
      description: Uniform deuteration throughout

    perdeuterated:
      description: Fully deuterated (>95% D)

    partial:
      description: Partial random deuteration

    segmental:
      description: Specific segments deuterated

    amino_acid_specific:
      description: Specific amino acids labeled

    matched_out:
      description: Deuteration matched to solvent

    triple_isotope:
      description: H/D/T labeling
```

### 4. Neutron Crystallography Extensions

#### NeutronCrystallographyExperiment
```yaml
NeutronCrystallographyExperiment:
  is_a: ExperimentRun
  attributes:
    crystal_volume:
      range: float
      unit: ucum:mm3
      required: true
      description: Crystal volume (neutrons need large crystals)

    data_collection_time:
      range: float
      unit: ucum:h
      description: Total beam time

    hydrogen_occupancy_refined:
      range: boolean
      description: Whether H/D occupancies were refined

    water_orientation_determined:
      range: boolean
      description: Whether water molecule orientations determined

    joint_xn_refinement:
      range: boolean
      description: Joint X-ray/neutron refinement used

    xray_data_id:
      range: DataFile
      description: Corresponding X-ray dataset if joint refinement
```

### 5. Contrast Variation Support

#### ContrastVariationSeries
```yaml
ContrastVariationSeries:
  description: Series of measurements at different contrasts
  attributes:
    series_id:
      range: string
      identifier: true

    contrast_points:
      range: ContrastPoint
      multivalued: true
      inlined_as_list: true

    match_point_determination:
      range: MatchPointAnalysis
      description: Analysis to find contrast match points

    stuhrmann_analysis:
      range: StuhrmannAnalysis
      description: Stuhrmann plot analysis results
```

#### ContrastPoint
```yaml
ContrastPoint:
  attributes:
    d2o_fraction:
      range: float
      required: true
      description: Fraction of D2O in solvent

    sld_solvent:
      range: float
      unit: ucum:10-6.Angstrom-2
      description: Scattering length density of solvent

    experiment_id:
      range: ExperimentRun
      description: Reference to the measurement

    component_visible:
      range: ComponentVisibilityEnum
      description: Which component is highlighted
```

### 6. Neutron Reflectometry

#### NeutronReflectometryExperiment
```yaml
NeutronReflectometryExperiment:
  is_a: ExperimentRun
  attributes:
    substrate_type:
      range: SubstrateEnum
      required: true

    interface_type:
      range: InterfaceEnum
      required: true

    q_range:
      range: float
      multivalued: true
      description: Q-range measured [min, max]

    layer_model:
      range: LayerModel
      description: Model used for fitting

    roughness:
      range: float
      unit: ucum:Angstrom
      description: Interface roughness

    film_thickness:
      range: float
      unit: ucum:Angstrom
      description: Total film thickness
```

### 7. Quasi-Elastic Neutron Scattering

#### QENSExperiment
```yaml
QENSExperiment:
  is_a: ExperimentRun
  attributes:
    energy_resolution:
      range: float
      unit: ucum:ueV
      description: Energy resolution

    energy_range:
      range: float
      multivalued: true
      unit: ucum:meV
      description: Energy transfer range [min, max]

    q_values:
      range: float
      multivalued: true
      description: Momentum transfer values

    temperature_series:
      range: float
      multivalued: true
      unit: ucum:K
      description: Temperatures measured

    dynamics_model:
      range: DynamicsModelEnum
      description: Model used for analysis

    diffusion_coefficient:
      range: float
      unit: ucum:cm2.s-1
      description: Extracted diffusion coefficient

    residence_time:
      range: float
      unit: ucum:ps
      description: Residence time from jump diffusion
```

### 8. Sample Environment

#### NeutronSampleEnvironment
```yaml
NeutronSampleEnvironment:
  attributes:
    environment_type:
      range: EnvironmentTypeEnum
      required: true

    temperature_control:
      range: TemperatureControl
      description: Temperature control system

    pressure:
      range: float
      unit: ucum:bar
      description: Sample pressure

    magnetic_field:
      range: float
      unit: ucum:T
      description: Applied magnetic field

    flow_rate:
      range: float
      unit: ucum:mL.min-1
      description: For flow cells

    windows_material:
      range: WindowMaterialEnum
      description: Material of sample cell windows

    activation_safe:
      range: boolean
      description: Sample checked for activation
```

## Integration with Existing Schema

### Sample Preparation Extensions
```yaml
SamplePreparation:
  attributes:
    # Add to existing class
    deuteration_info:
      range: DeuterationInfo
      description: Deuteration/labeling information

    neutron_activation_check:
      range: boolean
      description: Checked for neutron activation
```

### Data File Extensions
```yaml
DataFile:
  attributes:
    # Add neutron-specific formats
    file_format:
      # Add to existing enum:
      # - nxs (NeXuS)
      # - xye (powder diffraction)
      # - refl (reflectometry)
```

## Facility-Specific Implementations

### ORNL (SNS/HFIR)
- Support for SNS instrument names
- Time-of-flight metadata
- Event-mode data handling

### NIST NCNR
- Support for reactor-based instruments
- Cold neutron metadata
- Activation protocols

### LANL (LANSCE)
- Pulsed source specifics
- Protein crystallography beamline
- Dynamics instruments

## Use Cases

### Use Case 1: Joint X-ray/Neutron Refinement
```yaml
study:
  experiments:
    - technique: x_ray_crystallography
      experiment_code: "xray_001"
      resolution_achieved: 1.5
    - technique: neutron_crystallography
      experiment_code: "neutron_001"
      crystal_volume: 0.5
      joint_xn_refinement: true
      xray_data_id: "xray_001_data.mtz"
      hydrogen_occupancy_refined: true
```

### Use Case 2: Membrane Protein Contrast Variation
```yaml
contrast_series:
  series_id: "memb_protein_contrast"
  contrast_points:
    - d2o_fraction: 0.0
      component_visible: detergent_only
    - d2o_fraction: 0.21
      component_visible: protein_only
    - d2o_fraction: 0.42
      component_visible: both
    - d2o_fraction: 0.86
      component_visible: membrane_only
    - d2o_fraction: 1.0
      component_visible: all_components
```

### Use Case 3: Protein Dynamics by QENS
```yaml
qens_experiment:
  technique: qens
  energy_resolution: 0.9  # μeV
  temperature_series: [280, 290, 300, 310, 320]
  dynamics_model: jump_diffusion
  diffusion_coefficient: 1.2e-5
  residence_time: 15  # ps
```

## Benefits

### Scientific Impact
1. **Complete Hydrogen Picture**: See all hydrogens, including at active sites
2. **Native Conditions**: Study proteins in D2O-based native environments
3. **Dynamics Integration**: Connect structure with motion
4. **Contrast Magic**: Selectively visualize components in complexes

### For LAMBDA Goals
1. **Comprehensive Coverage**: All BER neutron capabilities represented
2. **Cross-Facility**: Standardized across SNS, HFIR, NCNR, LANSCE
3. **AI-Ready**: Rich metadata for machine learning on neutron data
4. **Multimodal**: Enables joint X-ray/neutron approaches

## Implementation Considerations

### Data Volume
- Neutron experiments often have lower data rates
- But longer collection times mean careful metadata tracking
- Event-mode data at SNS requires special handling

### Safety
- Activation checks required
- Sample shipping protocols
- Deuterated compound handling

### Specialized Knowledge
- Require good documentation
- Facility-specific guides
- Training materials for contrast variation

## Roadmap

### Phase 1: Core Neutron Support (Q1 2025)
- Basic NeutronInstrument class
- Neutron crystallography support
- Deuteration metadata

### Phase 2: Advanced Techniques (Q2 2025)
- QENS and dynamics
- Reflectometry
- Contrast variation series

### Phase 3: Integration (Q3 2025)
- Joint refinement workflows
- Cross-technique correlation
- Facility-specific adaptations

### Phase 4: AI/ML Features (Q4 2025)
- Hydrogen prediction models
- Dynamics extraction
- Automated contrast analysis

## Success Metrics

1. **Coverage**: % of neutron techniques supported
2. **Adoption**: Number of neutron datasets using schema
3. **Integration**: Joint X-ray/neutron studies captured
4. **Quality**: Completeness of deuteration metadata
5. **Impact**: Publications using neutron data from schema

## Conclusion

Comprehensive neutron technique support will position LAMBDA-BER as the definitive schema for multimodal structural biology. By capturing the unique aspects of neutron scattering alongside other techniques, we enable discoveries that leverage the full capabilities of DOE user facilities.