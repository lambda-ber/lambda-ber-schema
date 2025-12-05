# lambda-ber-schema

A comprehensive LinkML schema for representing multimodal structural biology imaging data, from atomic-resolution structures to tissue-level organization.

## Documentation

- [Schema Docs](https://lambda-ber.github.io/lambda-ber-schema/)

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
2. Injected into the schema YAML (`src/lambda_ber_schema/schema/lambda-ber-schema.yaml`)

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
