# lambda-ber-schema

A comprehensive LinkML schema for representing multimodal structural biology imaging data, from atomic-resolution structures to tissue-level organization.

## Documentation

- [Schema Docs](https://lambda-ber.github.io/lambda-ber-schema/)

## Validating an RO-Crate

A LAMBDA data package is an [RO-Crate](https://www.researchobject.org/ro-crate/) whose
`ro-crate-metadata.json` conforms to the
[LAMBDA Core profile](profiles/core/0.3.1/lambda-core-rocrate-profile-v0.3.1.md). One command
checks it:

```bash
# pip install lambda-ber-schema   (or `uv sync` in a checkout and prefix with `uv run`)
lambda-ber-schema rocrate validate path/to/ro-crate-metadata.json
# or point at the crate directory
lambda-ber-schema rocrate validate path/to/crate/
```

The exit code is 0 when the crate conforms, 1 when it does not, and 2 when it could not be read.
Every finding is tagged with the layer that produced it: `[document]` for the overall shape,
`[entity]` for a term or value a profile class does not allow, and `[graph]` for a rule about
relationships between entities (a dangling `hasPart`, an undeclared absence, and so on).
`--json` gives a machine-readable report, `--layer` restricts the check to one or more layers,
and `--schema` swaps in a different generated JSON Schema.

`linkml-validate` alone cannot do this. It walks a crate as a collection of instances rather than
one document, and it has no way to express the per-entity dispatch on `@type` or the graph rules.
The checker is importable too, as `lambda_ber_schema.rocrate.validate_path` and
`validate_crate`.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/lambda-ber/lambda-ber-schema.git
cd lambda-ber-schema

# Install dependencies with uv
uv sync --dev
```

### Generate Schema Artifacts

```bash
make gen-project
```

### Run Tests

```bash
make test
```

## Making a New Release

This project uses **dynamic versioning** from git tags. The version is automatically:
1. Set in the Python package metadata
2. Injected into the schema YAML (`src/lambda_ber_schema/schema/lambda_ber_schema.yaml`)

### Release Process

1. **Ensure all changes are merged to `main`**
   
2. **Create a GitHub Release:**
   - Go to [Releases](https://github.com/lambda-ber/lambda-ber-schema/releases)
   - Click "Draft a new release"
   - Create a new tag following semantic versioning: `v1.0.0`, `v1.1.0`, `v2.0.0`, etc.
   - Add release notes describing the changes
   - Click "Publish release"

3. **Automatic Publishing:**
   - The GitHub Action workflow will automatically:
     - Build the package with the version from the git tag
     - Inject the version into the schema YAML
     - Publish to PyPI (if Trusted Publisher is configured)

### Version Format

- Tags must start with `v` followed by a semantic version: `v1.2.3`
- The `v` prefix is stripped for the actual version: `1.2.3`
- Development versions (commits after a tag) look like: `1.2.3.post5.dev0+abc1234`

### Local Build Testing

To test the build locally:

```bash
uv build
```

This will show you the version that would be generated based on your current git state.
