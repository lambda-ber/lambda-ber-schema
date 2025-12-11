# Experiment Outcomes Tracking for LAMBDA-BER Schema

## Overview
This document proposes a lightweight yet comprehensive system for tracking experiment outcomes across all BER structural biology facilities. The goal is to capture outcome information with minimal burden while maximizing scientific value.

## Design Principles

1. **Minimal Burden**: Required fields should be simple and quick to fill
2. **Progressive Detail**: Allow optional detailed information for those willing to provide it
3. **Machine Actionable**: Outcomes should be computationally useful for AI/ML
4. **Human Readable**: Clear semantics for researchers
5. **Technique Agnostic**: Work across all experimental methods

## Core Outcome Model

### Three-Tier Approach

#### Tier 1: Basic (Required)
Just three fields to minimize barrier:

```yaml
ExperimentRun:
  attributes:
    outcome_status:
      range: OutcomeStatusEnum
      required: true
      default: completed
      description: Basic completion status

OutcomeStatusEnum:
  permissible_values:
    completed:     # Experiment ran to completion
    partial:       # Partially completed
    aborted:       # Stopped before completion
    pending:       # Still in progress
```

#### Tier 2: Valuable (Recommended)
Add success evaluation:

```yaml
ExperimentRun:
  attributes:
    outcome_success:
      range: SuccessLevelEnum
      description: Was the experiment successful?

    outcome_usable:
      range: boolean
      description: Is the data usable for analysis?

SuccessLevelEnum:
  permissible_values:
    successful:         # Met all objectives
    mostly_successful:  # Met primary objectives
    partially_successful: # Some objectives met
    unsuccessful:       # Did not meet objectives
    not_applicable:     # Success not relevant (e.g., calibration)
```

#### Tier 3: Detailed (Optional)
Complete outcome characterization:

```yaml
ExperimentRun:
  attributes:
    outcome_metrics:
      range: OutcomeMetrics
      description: Quantitative success metrics

    outcome_narrative:
      range: string
      description: Free text description of outcome
```

## Technique-Specific Outcomes

### Crystallography Outcomes
```yaml
CrystallographyOutcome:
  is_a: OutcomeMetrics
  attributes:
    crystals_observed:
      range: boolean
      required: true

    crystal_count:
      range: integer
      description: Number of crystals

    largest_dimension:
      range: float
      unit: ucum:um

    crystal_quality:
      range: CrystalQualityEnum

    diffraction_resolution:
      range: float
      unit: ucum:Angstrom

CrystalQualityEnum:
  permissible_values:
    single_crystal: "Well-formed single crystal"
    multiple_crystals: "Multiple separate crystals"
    clustered: "Crystal clusters"
    needle: "Needle-shaped crystals"
    plate: "Plate-like crystals"
    microcrystals: "Crystals <10 μm"
    twinned: "Twinned crystals"
    damaged: "Visible damage or cracks"
```

### CryoEM Outcomes
```yaml
CryoEMOutcome:
  is_a: OutcomeMetrics
  attributes:
    ice_thickness:
      range: IceQualityEnum

    particle_distribution:
      range: ParticleDistributionEnum

    particle_count:
      range: integer

    estimated_resolution:
      range: float
      unit: ucum:Angstrom

IceQualityEnum:
  permissible_values:
    optimal: "Optimal ice thickness"
    too_thick: "Ice too thick"
    too_thin: "Ice too thin"
    contaminated: "Ice contamination"
    crystalline: "Crystalline ice"
```

### SAXS/WAXS Outcomes
```yaml
ScatteringOutcome:
  is_a: OutcomeMetrics
  attributes:
    guinier_linearity:
      range: float
      description: R² of Guinier fit

    aggregation_detected:
      range: boolean

    concentration_effects:
      range: boolean

    rg_value:
      range: float
      unit: ucum:Angstrom

    i0_value:
      range: float
```

## Quick Entry Templates

### Success Template
```yaml
outcome_status: completed
outcome_success: successful
outcome_usable: true
```

### Failure Template
```yaml
outcome_status: completed
outcome_success: unsuccessful
outcome_usable: false
outcome_narrative: "No crystals formed after 30 days"
```

### Partial Success Template
```yaml
outcome_status: completed
outcome_success: partially_successful
outcome_usable: true
outcome_narrative: "Crystals formed but too small for data collection"
```

## Outcome Aggregation

### Facility-Level Metrics
```yaml
FacilityOutcomeStats:
  attributes:
    facility_id:
      range: Facility

    time_period:
      range: string

    total_experiments:
      range: integer

    success_rate:
      range: float
      description: Percentage of successful experiments

    partial_success_rate:
      range: float

    common_failure_modes:
      range: string
      multivalued: true
      description: Most frequent failure reasons
```

### Project-Level Tracking
```yaml
ProjectOutcomeSummary:
  attributes:
    project_id:
      range: Study

    experiments_attempted:
      range: integer

    experiments_successful:
      range: integer

    cumulative_success_rate:
      range: float

    improving_trend:
      range: boolean
      description: Is success rate improving over time?
```

## Automated Outcome Detection

### Rule-Based Classification
```python
def classify_crystallography_outcome(experiment):
    if experiment.crystals_observed:
        if experiment.diffraction_resolution < 3.0:
            return "successful"
        elif experiment.diffraction_resolution < 4.0:
            return "partially_successful"
        else:
            return "mostly_successful"
    else:
        return "unsuccessful"
```

### ML-Based Classification
Train classifiers to predict outcomes from experimental parameters:
- Input: Buffer conditions, protein concentration, temperature
- Output: Predicted outcome probability
- Use case: Optimize experimental design

## Integration with Workflow Systems

### Automatic Population
```yaml
WorkflowRun:
  attributes:
    propagate_outcome:
      range: boolean
      description: Auto-populate experiment outcome from workflow

    workflow_outcome_rules:
      range: string
      description: Rules for determining outcome from workflow metrics
```

### Example Rules
```yaml
rules:
  - if: "resolution < 2.0 AND completeness > 95"
    then: "outcome_success = successful"
  - if: "resolution > 4.0 OR completeness < 80"
    then: "outcome_success = unsuccessful"
  - else: "outcome_success = partially_successful"
```

## Privacy Levels

```yaml
OutcomePrivacyEnum:
  permissible_values:
    public:
      description: Outcome fully public

    summary_only:
      description: Only aggregate statistics public

    embargoed:
      description: Outcome hidden until embargo date

    private:
      description: Outcome never public

    anonymous:
      description: Outcome public but attribution removed
```

## Outcome Dashboards

### Real-Time Monitoring
- Current experiment status distribution
- Success rate trends over time
- Common failure mode alerts
- Parameter correlation analysis

### Historical Analysis
- Seasonal patterns in outcomes
- Operator-specific success rates
- Protocol evolution tracking
- Cross-facility comparisons

## Incentive Structures

### Outcome Badges
- "Transparent Reporter": Reports all outcomes
- "Failure Explorer": Documents 50+ failed experiments
- "Replication Champion": Performs validation experiments
- "Method Developer": Improves success rates

### Credit Systems
- DOI for valuable negative results
- Citation tracking for outcome data reuse
- Contribution scores for completeness

## Implementation Roadmap

### Phase 1: Basic Tracking (Months 1-3)
- Implement Tier 1 required fields
- Deploy at single facility
- Gather user feedback

### Phase 2: Enhanced Tracking (Months 4-6)
- Add Tier 2 recommended fields
- Implement technique-specific outcomes
- Create dashboard visualizations

### Phase 3: Automation (Months 7-9)
- Develop outcome detection algorithms
- Integrate with workflow systems
- Add privacy controls

### Phase 4: Analysis (Months 10-12)
- Deploy ML outcome predictors
- Generate outcome reports
- Cross-facility analytics

## Success Metrics

1. **Adoption Rate**: % experiments with outcomes reported
2. **Detail Level**: % using Tier 2/3 fields
3. **Accuracy**: Validation of self-reported vs. detected outcomes
4. **Utility**: Number of decisions influenced by outcome data
5. **Time Saved**: Reduction in repeated failed experiments

## Example Implementation

### Minimal Entry
```yaml
experiment:
  experiment_code: "exp_001"
  outcome_status: completed
```

### Typical Entry
```yaml
experiment:
  experiment_code: "exp_002"
  outcome_status: completed
  outcome_success: partially_successful
  outcome_usable: true
  outcome_narrative: "Diffraction to 3.5Å, sufficient for MR"
```

### Detailed Entry
```yaml
experiment:
  experiment_code: "exp_003"
  outcome_status: completed
  outcome_success: successful
  outcome_usable: true
  outcome_metrics:
    crystals_observed: true
    crystal_count: 12
    largest_dimension: 200
    crystal_quality: single_crystal
    diffraction_resolution: 1.8
  outcome_narrative: "Excellent crystals, ready for data collection"
```

## Conclusion

This tiered approach to outcome tracking balances comprehensive data capture with practical usability. By making basic tracking mandatory but simple, and detailed tracking optional but valuable, we can build a complete picture of experimental outcomes across BER facilities while maintaining researcher buy-in.