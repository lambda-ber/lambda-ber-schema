# Dynamics Data Expansion for LAMBDA-BER Schema

## Overview
Current structural biology datasets primarily capture static snapshots of molecular structures. However, BER-supported facilities generate rich time-resolved and dynamics data that provides critical insights into molecular function. This document proposes schema expansions to capture dynamics information comprehensively.

## Scientific Background

### Why Dynamics Matter
Proteins are molecular machines that undergo conformational changes to perform their functions. Static structures provide architectural blueprints, but understanding mechanism requires capturing motion across timescales:
- **Femtoseconds to picoseconds**: Bond vibrations, electronic transitions
- **Nanoseconds to microseconds**: Side chain rotations, loop movements
- **Microseconds to milliseconds**: Domain motions, allosteric transitions
- **Milliseconds to seconds**: Enzymatic turnover, folding events

### Temperature-Jump (T-Jump) Experiments
T-jump is a powerful perturbation method that rapidly heats a sample (typically 5-20°C in nanoseconds to microseconds) using:
- **Laser heating**: IR laser absorption by water (most common)
- **Joule heating**: Electric discharge through conductive solution
- **Microwave heating**: Dielectric heating of polar solvents

The rapid temperature change shifts equilibrium populations, allowing observation of:
- Protein folding/unfolding kinetics
- Conformational transitions
- Ligand binding dynamics
- DNA melting and hybridization

Key parameters for T-jump:
- **Rise time**: How fast temperature increases (ns to μs)
- **Final temperature**: Typically 5-20°C above starting
- **Relaxation time**: System's response time to perturbation
- **Probe method**: UV/Vis, fluorescence, IR, X-ray scattering

### pH-Jump Experiments
Rapid pH changes trigger protonation state changes, affecting:
- Enzyme activity
- Protein stability
- Conformational switches
- Proton-coupled processes

Methods include:
- **Caged protons**: UV-activated compounds (e.g., caged sulfate)
- **Rapid mixing**: Stopped-flow or microfluidics
- **Electrochemical**: Local pH changes via electrodes

### Pump-Probe Crystallography
Uses light pulses to initiate reactions in crystals:
1. **Pump pulse**: Triggers reaction (laser, LED)
2. **Time delay**: Controlled delay (fs to ms)
3. **Probe pulse**: X-ray pulse captures structure
4. **Multiple delays**: Build molecular movie

## Motivation
As noted in the LAMBDA presentation (slide 3), "Information about dynamics is in data types that are less well captured, but often supported by BER." This represents a major opportunity to:
- Enable AI models to learn temporal patterns in molecular behavior
- Support breakthrough discoveries in understanding molecular mechanisms
- Capture the full value of time-resolved experiments at light sources

## PDB and Time Series Data: Current State

### How PDB Handles Time-Resolved Structures
The Protein Data Bank faces challenges with time-resolved data:

1. **Individual Snapshots Model**: Each time point gets a separate PDB entry
   - Example: Photoactive Yellow Protein series (PDB: 1TS0-1TS8)
   - 9 separate entries for different time delays after photoactivation
   - Makes it difficult to analyze as a continuous series

2. **Multi-Model PDB Files**: Some use MODEL/ENDMDL records
   - Limited metadata for time information
   - No standardized time annotation
   - Example: PDB 2VH7 contains 20 models but no time metadata

3. **PDBx/mmCIF Extensions**: Partial support via:
   - `_exptl.method` can indicate "TIME-RESOLVED DIFFRACTION"
   - `_exptl.crystals_number` for serial crystallography
   - But no standard fields for time delays or series relationships

4. **Related Databases**:
   - **PDB-Dev**: For integrative models, some time series support
   - **SASBDB**: Small angle scattering, includes some time-resolved
   - **BMRB**: NMR dynamics data, relaxation parameters

### Real Example Datasets

#### 1. Myoglobin CO Photolysis (Classic T-jump)
- **PDB Series**: 1DWR (dark), 2G0S-2G0Z (time points)
- **Time points**: 100 ps, 316 ps, 1 ns, 3.16 ns, etc.
- **Method**: Laue diffraction after laser flash
- **Challenge**: Each structure is separate PDB entry
- **Schema need**: Link related time points, preserve time metadata

#### 2. Bacteriorhodopsin Photocycle
- **PDB Examples**: 1C3W, 1IW6, 1IW9, 1IXF, 1O0A
- **Time range**: Femtoseconds to milliseconds
- **Multiple intermediates**: L, M, N, O states
- **Current issue**: No systematic way to query full photocycle
- **Schema solution**: PhotocycleExperiment subclass with state transitions

#### 3. Ribosome Dynamics (XFEL)
- **PDB**: 6N4V, 6N4W, 6N4X
- **Technique**: Mix-and-inject serial crystallography
- **Time points**: 24 ms, 60 ms, 140 ms after mixing
- **Data volume**: Millions of diffraction patterns per time point
- **Schema need**: Handle massive serial data, mixing protocols

#### 4. Photoactive Yellow Protein (PYP)
- **Complete series**: PDB 1TS0-1TS8 (2003-2004)
- **Time delays**: Dark, 1 ns, 10 ns, 100 ns, 1 μs, 10 μs, 100 μs, 1 ms, 10 ms
- **Resolution**: 1.6 Å throughout series
- **Innovation**: First complete photocycle by time-resolved crystallography
- **Problem**: Finding all related structures requires manual curation

#### 5. Recent XFEL Time-Resolved Studies
- **Photosystem II**: PDB 7RF1-7RF8 (2022)
  - O2 evolution cycle
  - Flash 0, 1F, 2F, 3F states
  - Femtosecond XFEL pulses

- **Cytochrome c oxidase**: PDB 7COH, 7COI, 7COJ (2021)
  - CO photolysis
  - 10 μs, 100 μs, 10 ms time points

### Gap Analysis: PDB vs. Schema Needs

| Feature | PDB Current | Schema Proposed |
|---------|------------|-----------------|
| Time point linking | Manual via REMARK | Explicit time_series_id |
| Time delay metadata | Buried in title/remarks | Structured time_offset field |
| Trigger description | Free text | TriggerTypeEnum |
| Series relationship | None | TimeResolvedExperiment container |
| Kinetic parameters | Not captured | RateConstant class |
| Experimental conditions | Limited | Per-timepoint conditions |

## Current Schema Limitations
1. ExperimentRun focuses on single time points
2. No explicit fields for time series metadata
3. Limited support for pump-probe experiments
4. No standardized way to link sequential measurements
5. Cannot represent PDB time series effectively

## Proposed Expansions

### 1. TimeResolvedExperiment Class
New specialized class extending ExperimentRun:

```yaml
TimeResolvedExperiment:
  is_a: ExperimentRun
  description: Experiments capturing molecular dynamics over time
  attributes:
    time_series_type:
      range: TimeSeriesTypeEnum
      description: Type of time-resolved experiment
      required: true

    time_points:
      range: TimePoint
      multivalued: true
      inlined_as_list: true
      description: Individual measurements in the time series

    time_resolution:
      range: float
      description: Temporal resolution in seconds
      unit: ucum:s

    pump_probe_delay:
      range: float
      description: Delay between pump and probe pulses (for pump-probe experiments)
      unit: ucum:ps

    trigger_type:
      range: TriggerTypeEnum
      description: Method used to initiate the reaction/change

    repetition_rate:
      range: float
      description: Frequency of data collection
      unit: ucum:Hz
```

### 2. TimePoint Class
Represents individual measurements in a time series:

```yaml
TimePoint:
  attributes:
    time_offset:
      range: float
      required: true
      description: Time since experiment start or trigger
      unit: ucum:s

    data_file_id:
      range: DataFile
      description: Reference to the data file for this time point

    quality_score:
      range: float
      description: Quality metric for this time point

    temperature:
      range: float
      unit: ucum:K
      description: Temperature at this time point (for T-jump experiments)

    notes:
      range: string
      description: Time point-specific observations
```

### 3. New Enumerations

#### TimeSeriesTypeEnum
```yaml
TimeSeriesTypeEnum:
  permissible_values:
    pump_probe:
      description: Laser pump-probe spectroscopy
    temperature_jump:
      description: Rapid temperature change experiments
    ph_jump:
      description: Rapid pH change experiments
    ligand_mixing:
      description: Rapid mixing/stopped-flow experiments
    time_resolved_crystallography:
      description: Serial crystallography with time delays
    time_resolved_saxs:
      description: SAXS measurements over time
    molecular_dynamics_validation:
      description: Experimental validation of MD simulations
    continuous_flow:
      description: Continuous sample flow with temporal resolution
```

#### TriggerTypeEnum
```yaml
TriggerTypeEnum:
  permissible_values:
    laser_pulse:
      description: Laser-initiated reaction
    temperature_change:
      description: Temperature jump or ramp
    chemical_mixing:
      description: Rapid mixing of reagents
    ph_change:
      description: pH jump via mixing or caged compounds
    pressure_jump:
      description: Rapid pressure change
    electric_field:
      description: Electric field pulse
    caged_compound_release:
      description: UV-activated caged compound
    mechanical_stress:
      description: Mechanical perturbation
```

### 4. Dynamics Workflow Extensions
Add to WorkflowRun class:

```yaml
WorkflowRun:
  attributes:
    # ... existing fields ...

    dynamics_analysis_type:
      range: DynamicsAnalysisEnum
      description: Type of dynamics analysis performed

    kinetic_model:
      range: string
      description: Mathematical model used for kinetics fitting

    rate_constants:
      range: RateConstant
      multivalued: true
      description: Extracted rate constants from dynamics analysis

    principal_components:
      range: integer
      description: Number of principal components in dynamics analysis
```

### 5. Rate Constant Class
```yaml
RateConstant:
  attributes:
    process_name:
      range: string
      required: true
      description: Name of the kinetic process

    k_value:
      range: float
      required: true
      description: Rate constant value

    k_unit:
      range: string
      description: Unit for rate constant (e.g., s^-1, M^-1s^-1)

    error:
      range: float
      description: Uncertainty in rate constant

    temperature:
      range: float
      unit: ucum:K
      description: Temperature at which k was measured
```

## Implementation Considerations

### Data Volume
Time-resolved experiments generate large datasets. Consider:
- Reference-based storage (storing pointers to time series data)
- Hierarchical data organization
- Compression strategies for repetitive metadata

### Interoperability
- Align with existing time-series standards (e.g., NeXuS for neutron/X-ray)
- Support for HDF5 time-series data
- Compatible with molecular dynamics trajectory formats

### Validation
- Ensure time points are properly ordered
- Validate time units consistency
- Check for required fields in pump-probe experiments

## Detailed Use Cases with Real Examples

### 1. Photoactive Yellow Protein Photocycle (Based on PDB 1TS0-1TS8)
```yaml
experiment:
  class_type: TimeResolvedExperiment
  experiment_code: "PYP_photocycle_2004"
  technique: time_resolved_crystallography
  time_series_type: pump_probe
  sample_id: "PYP_crystal_001"
  instrument_id: "ESRF_ID09B"

  # Trigger details
  trigger_type: laser_pulse
  trigger_details:
    wavelength: 450  # nm, blue light
    pulse_duration: 7  # ns
    pulse_energy: 5  # mJ

  # Series metadata
  pdb_series_ids: ["1TS0", "1TS1", "1TS2", "1TS3", "1TS4", "1TS5", "1TS6", "1TS7", "1TS8"]

  time_points:
    - time_offset: -1.0e-6  # -1 μs (dark state)
      data_file_id: "PYP_dark.mtz"
      pdb_id: "1TS0"
      state_name: "pG"  # ground state
      quality_score: 0.95

    - time_offset: 1.0e-9  # 1 ns
      data_file_id: "PYP_1ns.mtz"
      pdb_id: "1TS1"
      state_name: "I0"  # first intermediate
      chromophore_isomerization: "trans_to_cis"
      quality_score: 0.90

    - time_offset: 1.0e-8  # 10 ns
      data_file_id: "PYP_10ns.mtz"
      pdb_id: "1TS2"
      state_name: "I0/pR"  # mixed state
      population_ratio: "70:30"
      quality_score: 0.88

    - time_offset: 1.0e-7  # 100 ns
      data_file_id: "PYP_100ns.mtz"
      pdb_id: "1TS3"
      state_name: "pR1"  # early red-shifted
      quality_score: 0.85

    - time_offset: 1.0e-6  # 1 μs
      data_file_id: "PYP_1us.mtz"
      pdb_id: "1TS4"
      state_name: "pR2"  # late red-shifted
      quality_score: 0.87

    - time_offset: 1.0e-3  # 1 ms
      data_file_id: "PYP_1ms.mtz"
      pdb_id: "1TS8"
      state_name: "pB"  # signaling state
      quality_score: 0.92

  # Kinetic analysis results
  dynamics_analysis:
    kinetic_model: "sequential_irreversible"
    rate_constants:
      - process_name: "pG_to_I0"
        k_value: 1.0e12
        k_unit: "s-1"
        activation_energy: 12.5  # kJ/mol

      - process_name: "I0_to_pR"
        k_value: 5.0e7
        k_unit: "s-1"

      - process_name: "pR_to_pB"
        k_value: 1.0e4
        k_unit: "s-1"

      - process_name: "pB_to_pG"
        k_value: 3.0e2
        k_unit: "s-1"
```

### 2. Temperature-Jump Protein Folding (Hypothetical but realistic)
```yaml
experiment:
  class_type: TimeResolvedExperiment
  experiment_code: "villin_tjump_2024"
  technique: time_resolved_saxs
  time_series_type: temperature_jump

  # T-jump specifications
  trigger_type: laser_pulse
  trigger_details:
    laser_type: "Nd:YAG"
    wavelength: 1900  # nm, absorbed by water
    pulse_duration: 10  # ns
    temperature_rise: 15  # Kelvin

  initial_temperature: 283  # 10°C
  final_temperature: 298    # 25°C

  # Millisecond time resolution for folding
  time_resolution: 0.001  # 1 ms

  time_points:
    - time_offset: -0.001  # -1 ms (before T-jump)
      temperature: 283
      data_file_id: "villin_cold_equilibrium.dat"
      rg_value: 18.5  # Radius of gyration in Å
      state: "unfolded"

    - time_offset: 0.001  # 1 ms
      temperature: 298
      data_file_id: "villin_1ms.dat"
      rg_value: 17.2
      state: "early_intermediate"

    - time_offset: 0.010  # 10 ms
      temperature: 298
      data_file_id: "villin_10ms.dat"
      rg_value: 15.8
      state: "late_intermediate"

    - time_offset: 0.100  # 100 ms
      temperature: 298
      data_file_id: "villin_100ms.dat"
      rg_value: 13.5
      state: "near_native"

    - time_offset: 1.000  # 1 s
      temperature: 298
      data_file_id: "villin_1s.dat"
      rg_value: 12.1
      state: "folded"

  # Folding kinetics
  dynamics_analysis:
    kinetic_model: "two_state_with_intermediate"
    rate_constants:
      - process_name: "unfolded_to_intermediate"
        k_value: 500
        k_unit: "s-1"
        temperature: 298

      - process_name: "intermediate_to_folded"
        k_value: 20
        k_unit: "s-1"
        temperature: 298

    folding_time_constant: 0.05  # seconds
    phi_values:  # For mutation analysis
      - residue: "PHE47"
        phi: 0.3
      - residue: "TRP64"
        phi: 0.8
```

### 3. Mix-and-Inject Serial Crystallography (Based on ribosome studies)
```yaml
experiment:
  class_type: TimeResolvedExperiment
  experiment_code: "ribosome_ef-tu_binding_xfel"
  technique: time_resolved_crystallography
  time_series_type: ligand_mixing

  # XFEL specific
  facility: "LCLS"
  beamline: "CXI"

  trigger_type: chemical_mixing
  trigger_details:
    mixing_method: "microfluidic_mixer"
    reactant_1: "70S_ribosome"
    reactant_1_concentration: 10  # μM
    reactant_2: "EF-Tu_GTP_aa-tRNA"
    reactant_2_concentration: 50  # μM
    mixing_ratio: "1:1"
    dead_time: 10  # ms

  # Serial crystallography parameters
  serial_parameters:
    crystal_size: 5  # μm
    crystals_per_timepoint: 50000
    hit_rate: 0.15  # 15%
    indexing_rate: 0.08  # 8%

  time_points:
    - time_offset: 0  # mixing point
      data_file_id: "ribosome_t0_unmixed.h5"
      description: "Pre-mixed control"
      structures_collected: 45000

    - time_offset: 0.024  # 24 ms
      data_file_id: "ribosome_24ms.h5"
      pdb_id: "6N4V"
      state: "initial_binding"
      occupancy_ef_tu: 0.3
      structures_collected: 52000

    - time_offset: 0.060  # 60 ms
      data_file_id: "ribosome_60ms.h5"
      pdb_id: "6N4W"
      state: "codon_recognition"
      occupancy_ef_tu: 0.7
      structures_collected: 48000

    - time_offset: 0.140  # 140 ms
      data_file_id: "ribosome_140ms.h5"
      pdb_id: "6N4X"
      state: "GTPase_activated"
      occupancy_ef_tu: 0.9
      structures_collected: 51000

  # Reaction kinetics
  dynamics_analysis:
    kinetic_model: "induced_fit"
    rate_constants:
      - process_name: "initial_binding"
        k_value: 1.0e7
        k_unit: "M-1.s-1"

      - process_name: "codon_recognition"
        k_value: 100
        k_unit: "s-1"

      - process_name: "GTPase_activation"
        k_value: 50
        k_unit: "s-1"
```

### 4. pH-Jump Enzyme Activation
```yaml
experiment:
  class_type: TimeResolvedExperiment
  experiment_code: "lysozyme_ph_jump_2024"
  technique: time_resolved_saxs
  time_series_type: ph_jump

  trigger_type: caged_compound_release
  trigger_details:
    caged_compound: "caged_sulfate"
    uncaging_wavelength: 355  # nm UV
    initial_ph: 7.5
    final_ph: 4.5
    buffer: "sodium_acetate"

  time_points:
    - time_offset: -0.001
      ph_actual: 7.5
      data_file_id: "lyz_neutral.dat"
      enzyme_activity: "inactive"

    - time_offset: 0.001  # 1 ms after UV flash
      ph_actual: 5.8  # partial pH change
      data_file_id: "lyz_1ms.dat"
      enzyme_activity: "activating"

    - time_offset: 0.010
      ph_actual: 4.5  # full pH change
      data_file_id: "lyz_10ms.dat"
      enzyme_activity: "fully_active"
```

## Benefits for AI/ML

1. **Temporal Learning**: AI models can learn transition states and reaction pathways
2. **Dynamics Prediction**: Train models to predict time evolution from initial states
3. **Mechanism Discovery**: Identify reaction intermediates and pathways
4. **Integration with MD**: Validate and improve molecular dynamics simulations
5. **Anomaly Detection**: Identify unusual dynamics patterns in large datasets

## BER Facility Capabilities for Time-Resolved Studies

### Current Infrastructure
BER-supported facilities have unique capabilities for dynamics studies:

#### SLAC (LCLS)
- **Femtosecond XFEL pulses**: Ultimate time resolution
- **Mix-and-inject**: Microfluidic sample delivery
- **Pump-probe**: Synchronized laser systems
- **Data rates**: TB/hour of time-resolved data

#### Berkeley Lab (ALS)
- **COSMIC beamline**: Time-resolved ptychography
- **Infrared beamlines**: Microsecond dynamics
- **Stop-flow SAXS**: Protein folding studies

#### Brookhaven (NSLS-II)
- **AMX/FMX beamlines**: Serial crystallography
- **LIX beamline**: Time-resolved SAXS
- **XFP beamline**: Pump-probe capabilities

#### Argonne (APS)
- **BioCARS**: Pioneered time-resolved crystallography
- **BioCAT**: Time-resolved muscle diffraction
- **Planned upgrade**: Will enable ps time resolution

### Schema Benefits for BER Facilities

1. **Cross-Facility Queries**: Find all T-jump experiments across facilities
2. **Meta-Analysis**: Combine time series from multiple sources
3. **AI Training Data**: Rich temporal data for dynamics prediction
4. **Reproducibility**: Standardized time series metadata
5. **Discovery**: Link disconnected PDB time points

## Integration with Molecular Dynamics

### Bridging Experiment and Simulation
```yaml
MDValidationExperiment:
  is_a: TimeResolvedExperiment
  attributes:
    md_trajectory_id:
      range: string
      description: Reference to MD simulation

    experimental_observables:
      range: Observable
      multivalued: true
      description: Quantities compared with simulation

    chi_squared:
      range: float
      description: Goodness of fit to simulation
```

### Example: SAXS-Guided MD
```yaml
experiment:
  class_type: MDValidationExperiment
  technique: time_resolved_saxs
  md_trajectory_id: "md_sim_001.xtc"

  experimental_observables:
    - type: "radius_of_gyration"
      experimental: 15.2
      simulated: 15.5
      error: 0.3

    - type: "pair_distance_distribution"
      experimental: "p_r_exp.dat"
      simulated: "p_r_sim.dat"
      correlation: 0.95
```

## Next Steps

1. **Community Engagement**:
   - Workshop at next BER facility users meeting
   - Survey time-resolved data producers
   - Collaborate with PDB on time series annotation

2. **Pilot Implementation**:
   - Partner with one beamline (e.g., BioCARS)
   - Convert existing time-resolved datasets
   - Validate schema with real data

3. **Tool Development**:
   - Time series visualization tools
   - PDB series linking utilities
   - Kinetic analysis pipelines

4. **Standards Alignment**:
   - Coordinate with NeXuS/HDF5 communities
   - Propose PDBx/mmCIF extensions
   - Integrate with MD trajectory formats

5. **AI/ML Applications**:
   - Develop dynamics prediction models
   - Train on schema-compliant data
   - Benchmark against experimental series

## Conclusion

Time-resolved experiments represent a frontier in structural biology where BER facilities excel. This schema extension would:
- Capture the full richness of dynamics data
- Enable AI models to learn temporal patterns
- Connect fragmented PDB time series
- Support next-generation time-resolved techniques
- Position LAMBDA as the standard for dynamics data

The gap between PDB's static snapshots and the continuous molecular movies generated at BER facilities presents both a challenge and an opportunity. By implementing these extensions, we can finally capture the fourth dimension—time—in structural biology data.

## References

- Pearson & Mozzarelli (2011). "Time-resolved X-ray crystallography" *Biochim Biophys Acta*
- Neutze & Moffat (2012). "Time-resolved structural studies at synchrotrons" *Curr Opin Struct Biol*
- Hub (2018). "Interpreting solution X-ray scattering data using MD simulations" *Curr Opin Struct Biol*
- Kern et al. (2018). "Structures of ribosome-bound initiation factor 2" *Nature*
- Pande et al. (2016). "Femtosecond structural dynamics" *Science*
- Schmidt (2019). "Time-resolved crystallography at XFELs" *Advances in Physics: X*
- Hekstra et al. (2016). "Electric-field-stimulated protein mechanics" *Nature*
- NSLS-II time-resolved capabilities: https://www.bnl.gov/nsls2/
- ALS COSMIC beamline: https://als.lbl.gov/beamlines/4-0-3/
- LCLS instruments: https://lcls.slac.stanford.edu/
- BioCARS time-resolved: https://biocars.uchicago.edu/