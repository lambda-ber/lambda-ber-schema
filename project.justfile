# ============== Schema Development Recipes ==============

# Variables
RUN := "uv run"
SCHEMA := "src/lambda_ber_schema/schema/lambda-ber-schema.yaml"
DOCDIR := "./docs"

# Run all schema generation tasks (gen-project, gendoc, test-examples)
[group('schema development')]
all: gen-project gendoc test-examples

# Run schema tests (gen-project and test-examples)
[group('schema development')]
test-schema: gen-project test-examples

# Generate project artifacts from LinkML schema
[group('schema development')]
gen-project:
  {{RUN}} gen-project --config-file config.yaml {{SCHEMA}} -d assets

# Run and validate all example files
[group('schema development')]
test-examples:
  {{RUN}} linkml-run-examples -t yaml -t json -t ttl -s {{SCHEMA}} -P conf/prefixes.yaml -e tests/data/valid -d examples

# Generate documentation from schema
[group('schema development')]
gendoc:
  mkdir -p {{DOCDIR}}
  cp -pr src/docs/* {{DOCDIR}}
  {{RUN}} gen-doc -d {{DOCDIR}} {{SCHEMA}}

# Serve documentation locally
[group('schema development')]
serve:
  {{RUN}} mkdocs serve

# Deploy documentation to GitHub Pages
[group('schema development')]
deploy:
  {{RUN}} mkdocs gh-deploy