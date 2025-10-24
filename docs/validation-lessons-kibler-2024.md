# Lessons Learned: Validating Real-World Data with lambda-ber-schema

## Case Study: Kibler et al. 2024 - Pseudosymmetric Protein Hetero-oligomers

This document captures lessons learned from annotating a real scientific paper (Kibler et al., Nature Communications 2024) using the lambda-ber-schema LinkML schema.

## Key Validation Issues Encountered

### 1. Missing Required Fields
**Issue**: All entities inheriting from `NamedThing` require an `id` field
- **Solution**: Add unique identifiers following a consistent pattern (e.g., `sample:BGL0`, `exp:saxs-main`)
- **Recommendation**: Consider making `id` auto-generated or providing clear guidance on ID formats

### 2. Enum Value Restrictions
**Issue**: Real-world data uses many terms not in the base schema enums:
- Sample types: `protein_complex` not in enum (only `complex` exists)
- Preparation types: `protein_expression`, `protein_purification`, `negative_stain` not in enum
- Techniques: `electron_microscopy`, `mass_spectrometry` not in enum
- Workflow types: `saxs_analysis`, `em_2d_classification`, `mass_spec_analysis` not in enum
- File formats: `ascii`, `dat`, `raw` not in enum
- Data types: `raw_data`, `processed_data` not in enum
- Collection modes: `batch`, `sec_saxs`, `single_particle` not in enum

**Solution**: Either map to closest existing values or extend the schema
**Recommendation**: Create an extended schema with commonly used values

### 3. Structured Data in String Fields
**Issue**: `processing_parameters` expects a string but complex parameters need structure
- **Solution**: Convert dictionaries to JSON strings
- **Recommendation**: Consider allowing structured data or provide JSON schema for parameters

### 4. Missing Technique-Specific Fields
**Issue**: Different techniques need different experimental condition fields:
- SAXS: `beam_energy`, `exposure_time`, `number_of_frames`
- EM: `accelerating_voltage`, `magnification`, `pixel_size`, `stain`
- MS: `buffer`, `capillary_temperature`, `source_voltage`
- SEC-SAXS: `flow_rate`, `frame_rate`, `column_type`

**Solution**: Create extended classes or use generic key-value pairs
**Recommendation**: Add technique-specific subclasses of `ExperimentalConditions`

### 5. Missing Quality Metrics
**Issue**: Different techniques have different quality metrics:
- SAXS: `i_zero`, `rg`, `dmax`
- EM: `particles_picked`, `classes_generated`
- MS: `mass_accuracy`, `measured_mass`, `charge_state_range`
- SEC-SAXS: `elution_volume`, `peak_symmetry`

**Solution**: Similar to experimental conditions
**Recommendation**: Add technique-specific subclasses of `QualityMetrics`

## Solutions Implemented

### 1. Fixed Version (Minimal Changes)
Created `Dataset-kibler-2024-hetero-oligomers-fixed.yaml`:
- Added all required `id` fields
- Mapped to closest existing enum values
- Removed unsupported fields
- Converted structured data to JSON strings
- **Result**: Validates successfully with base schema

### 2. Extended Schema
Created `lambda-ber-schema-extended.yaml`:
- Extended all enums with real-world values
- Added technique-specific fields to `ExperimentalConditions`
- Added technique-specific fields to `QualityMetrics`
- Maintained backward compatibility with base schema

### 3. Extended Version (Using Extended Schema)
Created `Dataset-kibler-2024-hetero-oligomers-extended.yaml`:
- Uses all original values from the paper
- References extended schema
- Provides more accurate representation of the experiment

## Recommendations for Schema Evolution

### 1. Core Schema Improvements
- **Auto-generate IDs**: Consider making `id` fields auto-generated or optional
- **Flexible enums**: Add `other` option with description field for uncommon values
- **Structured parameters**: Allow JSON/YAML structures in parameter fields
- **Documentation**: Add examples for each entity type

### 2. Technique-Specific Extensions
Create technique-specific modules that extend base classes:
```yaml
SAXSExperimentalConditions:
  is_a: ExperimentalConditions
  attributes:
    beam_energy: float
    q_range: string
    exposure_protocol: string

CryoEMExperimentalConditions:
  is_a: ExperimentalConditions
  attributes:
    accelerating_voltage: float
    dose_per_frame: float
    pixel_size: float
```

### 3. Validation Levels
Implement multiple validation levels:
- **Strict**: Only base schema values (for standardized repositories)
- **Extended**: Include common extensions (for real-world data)
- **Permissive**: Allow additional properties (for exploration)

### 4. Migration Tools
Develop tools to:
- Auto-map common terms to standard enums
- Suggest closest matches for unknown values
- Generate schema extensions from data

## Benefits of This Exercise

1. **Schema Testing**: Real-world data reveals schema limitations
2. **Documentation**: Creates concrete examples for users
3. **Interoperability**: Shows how to map between different terminologies
4. **Evolution Path**: Identifies priorities for schema development

## Conclusion

The lambda-ber-schema schema successfully captures the core structure of multi-technique structural biology experiments. However, real-world data requires:
- More comprehensive enum values
- Technique-specific field extensions
- Flexible validation approaches
- Clear documentation and examples

The two-phase approach (fix data to match schema, then extend schema to match data) provides a practical path forward that maintains compatibility while improving expressiveness.