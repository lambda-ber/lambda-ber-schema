# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

lambda-ber-schema is a LinkML schema project for representing structural biological imaging data and experiments. It provides a unified data model for cryo-EM, X-ray crystallography, SAXS/WAXS, and SANS techniques with rich biological context annotations.

## Key Technologies

- **LinkML**: Schema modeling language for biomedical data
- **Python**: Primary implementation language  
- **uv**: Package manager for Python dependencies

## Core Architecture

### Schema Structure
The main schema definition is located at `src/lambda_ber_schema/schema/lambda_ber_schema.yaml`. This LinkML schema uses a **relational design** with flat entity collections and explicit association tables for M:N relationships.

**Entity Tables** (flat collections in Dataset):
- **Study**: Lightweight grouping for related experiments
- **Sample**: Biological samples with molecular composition, buffer conditions, storage details
- **SamplePreparation**: Technique-specific preparation protocols
- **Instrument**: Equipment specifications for CryoEM, XRay, SAXS instruments
- **ExperimentRun**: Data collection sessions with quality metrics
- **WorkflowRun**: Computational processing workflows
- **DataFile**: File metadata with checksums
- **Image/Image2D/Image3D**: Image acquisition data

**Association Tables** (M:N relationships):
- **StudySampleAssociation**, **StudyExperimentAssociation**, **StudyWorkflowAssociation**
- **ExperimentSampleAssociation**, **ExperimentInstrumentAssociation**
- **WorkflowExperimentAssociation**, **WorkflowInputAssociation**, **WorkflowOutputAssociation**

**Supporting classes**: MolecularComposition, BufferComposition, StorageConditions, ExperimentalConditions, etc.

### Generated Assets
The `assets/` directory contains auto-generated outputs from the LinkML schema:
- Python dataclasses (`lambda_ber_schema.py`)
- JSON Schema validation (`jsonschema/`)
- Documentation (`docs/`)
- Multiple serialization formats (GraphQL, OWL, SHACL, etc.)

## Development Commands

### Schema Generation
Generate all downstream artifacts from the LinkML schema:
```bash
make gen-project
# or directly:
uv run gen-project src/lambda_ber_schema/schema/lambda_ber_schema.yaml -d assets
```

### Testing
Run all tests including schema validation and example validation:
```bash
make test
```
This runs:
1. `gen-project` to regenerate artifacts
2. `linkml-run-examples` to validate all examples in `tests/data/valid/`

### Schema Validation
Validate the schema against LinkML metamodel:
```bash
uv run linkml-lint src/lambda_ber_schema/schema/lambda_ber_schema.yaml
```

### Data Validation
Validate data files against the schema:
```bash
uv run linkml-validate -s src/lambda_ber_schema/schema/lambda_ber_schema.yaml <data_file>
```

### Python Environment
Install development dependencies:
```bash
uv sync --dev
```

Run the main entry point:
```bash
uv run lambda-ber-schema
```

## Project Structure

- `src/lambda_ber_schema/schema/lambda_ber_schema.yaml` - Main LinkML schema definition
- `assets/` - Generated artifacts (Python, docs, JSON Schema, etc.)
- `docs/spec.md` - Comprehensive specification for BER structural biology data
- `docs/background.md` - Research on current structural biology data systems
- `tests/data/valid/` - Valid example files for testing
- `pyproject.toml` - Python project configuration with LinkML dependencies
- `Makefile` - Build automation with test targets

## Important Schema Design Decisions

### Date/Time Handling
All date and datetime fields use `string` type rather than strict date/datetime types to avoid validation issues with different formats. This is more forgiving for real-world data.

### Required Fields
Each major class has minimal required fields to ensure data integrity:
- **Sample**: `sample_code`, `sample_type`
- **SamplePreparation**: `preparation_type`, `sample_id`
- **Instrument**: `instrument_code`
- **ExperimentRun**: `experiment_code`, `technique`
- **WorkflowRun**: `workflow_code`, `workflow_type`, `software_name`
- **DataFile**: `file_name`, `file_format`
- **Image**: `file_name`

Note: Relationships (sample↔experiment, experiment↔instrument, etc.) are handled via association tables, not direct FK fields on entities.

### Relational Design
All entity collections live directly in Dataset as flat lists (`inlined_as_list: true`). M:N relationships are modeled via explicit association tables that can carry relationship metadata (e.g., sample's role in an experiment).

### Numeric Types
Scientific notation in YAML (e.g., `2.0e12`) must be written as plain numbers (e.g., `2000000000000`) due to LinkML's JSON Schema generation.

### Enumerations
The schema includes comprehensive enums for controlled vocabularies:
- Sample types, concentration units, temperature units
- Preparation types, grid types, vitrification methods
- Instrument status, detector types, X-ray sources
- Techniques, processing status, workflow types
- File formats, data types, collection modes

## Testing Examples

The `tests/data/valid/` directory contains comprehensive examples covering all schema classes:
- Full datasets with complete workflows (Dataset-berkeley-tfiid.yaml, Dataset-integrative.yaml)
- Individual class examples for all major entities
- Berkeley Lab / ALS beamline-specific examples
- Examples demonstrating association tables for M:N relationships

## Common Pitfalls to Avoid

1. **Don't use scientific notation** in YAML files - write out full numbers
2. **Don't use strict datetime formats** - use strings for dates
3. **Use association tables** for M:N relationships (not direct FK fields on entities)
4. **Include all required fields** even in minimal examples
5. **Use proper enum values** from the defined permissible_values