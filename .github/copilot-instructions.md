# AI Coding Agent Instructions for lambda-ber-schema

This repository contains a LinkML schema for comprehensive structural biology imaging data, from atomic-resolution structures to tissue-level organization. It supports cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and spectroscopic imaging.

## Core Architecture

**Schema Definition**: The main schema is `src/lambda_ber_schema/schema/lambda-ber-schema.yaml` (note underscore in path, not hyphen). This LinkML schema defines hierarchical data structures:
- `Dataset` → `Study` → `Sample`/`SamplePreparation`/`ExperimentRun`/`WorkflowRun`/`DataFile`/`Image`
- Specialized instrument classes: `CryoEMInstrument`, `XRayInstrument`, `SAXSInstrument`
- Rich metadata tracking from biological sample to final processed data

**Generated Artifacts**: The `assets/` directory contains auto-generated files from the schema:
- `lambda-ber-schema.py`: Python dataclasses for programmatic use
- `jsonschema/`, `graphql/`, `owl/`: Multiple format outputs
- Auto-generated via `make gen-project` (uses `gen-project` command from LinkML)

## Essential Development Workflows

**Schema Regeneration**: Always run after schema changes:
```bash
make gen-project  # or: uv run gen-project --config-file config.yaml src/lambda_ber_schema/schema/lambda-ber-schema.yaml -d assets
```

**Validation Testing**: Validates schema + example data files:
```bash
make test  # Runs gen-project + linkml-run-examples against tests/data/valid/
```

**Package Management**: Uses `uv` for Python environment:
```bash
uv sync --dev  # Install dependencies including LinkML tools
uv run <command>  # Run commands in managed environment
```

## Key Project Patterns

**Inlined Collections**: Study objects use `inlined: true` + `inlined_as_list: true` for better JSON/YAML representation of samples, experiments, etc.

**Date Handling**: All date/datetime fields use `string` type (not strict datetime) for real-world data flexibility.

**Required Fields**: Each major class has minimal required fields - check schema for `required: true` annotations.

**Example Data**: `tests/data/valid/` contains 30+ comprehensive examples covering all schema classes. Use these as templates for new features.

**Scientific Notation**: Avoid in YAML (e.g., `2.0e12`) - write as plain numbers (`2000000000000`) due to LinkML JSON Schema generation.

## Critical Dependencies

- **LinkML**: Schema modeling framework - commands like `gen-project`, `linkml-validate`, `linkml-run-examples`
- **uv**: Python package manager (replaces pip/conda for this project)  
- **MkDocs**: Documentation generation with material theme

When modifying schema structure, always regenerate artifacts and validate against existing examples to ensure backward compatibility.



