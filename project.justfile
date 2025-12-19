# ============== Schema Development Recipes ==============

# Variables
RUN := "uv run"
SCHEMA := "src/lambda_ber_schema/schema/lambda_ber_schema.yaml"
DOCDIR := "./docs/elements"

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
  {{RUN}} gen-doc -d {{DOCDIR}} {{SCHEMA}}

# Serve documentation locally
[group('schema development')]
serve:
  {{RUN}} mkdocs serve

# Deploy documentation to GitHub Pages
[group('schema development')]
deploy:
  {{RUN}} mkdocs gh-deploy

# ============== Slides Generation Recipes ==============

# Generate all slide decks in docs/slides/
[group('documentation')]
gen-slides:
  #!/usr/bin/env bash
  set -e
  cd docs/slides
  for slide in *.md; do
    if [ -f "$slide" ]; then
      base="${slide%.md}"
      echo "Generating slides for $slide..."
      marp "$slide" --allow-local-files -o "${base}.html"
      marp "$slide" --allow-local-files --pdf -o "${base}.pdf"
      marp "$slide" --allow-local-files --pptx -o "${base}.pptx"
    fi
  done
  echo "All slides generated in docs/slides/"

# Generate a specific slide deck (e.g., just gen-slide overview)
[group('documentation')]
gen-slide deck:
  cd docs/slides && marp {{deck}}.md --allow-local-files -o {{deck}}.html
  cd docs/slides && marp {{deck}}.md --allow-local-files --pdf -o {{deck}}.pdf
  cd docs/slides && marp {{deck}}.md --allow-local-files --pptx -o {{deck}}.pptx
  @echo "Slides generated for {{deck}} in docs/slides/"