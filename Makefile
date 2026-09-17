RUN = uv run
SCHEMA := src/lambda_ber_schema/schema/lambda_ber_schema.yaml
RCSCHEMA := src/lambda_ber_schema/schema/lambda_rocrate_core.yaml
RCDIR := assets/rocrate
RCDOC := ROCrateMetadataDocument
DOCDIR := ./docs
ELEMENTSDIR := ./docs/elements
PYDANTIC := src/lambda_ber_schema/pydantic.py

all: gen-project gendoc test-examples gen-pydantic gen-sssom gen-rocrate
# gen-rocrate before test-rocrate: test_generated_artifact_agrees skips when the artifact is
# absent, so without this a tree without generated output would report a pass it did not earn.
test: gen-project gen-rocrate test-examples test-rocrate

gen-project:
	$(RUN) gen-project --config-file config.yaml $(SCHEMA) -d assets

gen-pydantic: $(PYDANTIC)

$(PYDANTIC): $(SCHEMA)
	$(RUN) gen-pydantic $(SCHEMA) > $(PYDANTIC)

test-examples:
	$(RUN) linkml-run-examples -t yaml -t json -t ttl -s $(SCHEMA) -P conf/prefixes.yaml -e tests/data/valid -d examples

# Generate schema documentation to docs/elements/ and copy manual docs
gendoc: $(DOCDIR)
	cp -pr src/docs/* $(DOCDIR)
	mkdir -p $(DOCDIR)/profiles
	cp -p profiles/core/0.3.2/lambda-core-rocrate-profile-v0.3.2.md $(DOCDIR)/profiles/
	$(RUN) gen-doc -d $(ELEMENTSDIR) $(SCHEMA)

gen-sssom: assets/sssom/lambda_ber_schema.sssom.tsv

assets/sssom/lambda_ber_schema.sssom.tsv: $(SCHEMA)
	mkdir -p assets/sssom
	$(RUN) gen-sssom $(SCHEMA) -o $@

# ---- LAMBDA Core RO-Crate profile -------------------------------------------------
# The profile imports the main schema, which also declares a tree_root. gen-project would
# therefore root the generated JSON Schema at Dataset rather than at the crate document, so
# the JSON Schema is regenerated afterwards with the crate document named explicitly.
# The JSON Schema is also copied into the package so that `lambda-ber-schema rocrate validate`
# works from a plain install, where the linkml generators are not present to rebuild it.
RCJSONSCHEMA := $(RCDIR)/jsonschema/lambda_rocrate_core.schema.json
RCPACKAGED := src/lambda_ber_schema/schema/lambda_rocrate_core.schema.json
gen-rocrate:
	$(RUN) gen-project --config-file conf/rocrate-gen-config.yaml $(RCSCHEMA) -d $(RCDIR)
	$(RUN) gen-json-schema --top-class $(RCDOC) $(RCSCHEMA) > $(RCJSONSCHEMA)
	cp -p $(RCJSONSCHEMA) $(RCPACKAGED)
	$(RUN) gen-sssom $(RCSCHEMA) -o $(RCDIR)/lambda_rocrate_core.sssom.tsv

# linkml-validate is not used here: it iterates a data source as a collection of instances, so a
# single JSON object is walked key-by-key, and --legacy-mode routes through gen-python, which cannot
# represent the @-keyword aliases. The checker in src/lambda_ber_schema/rocrate/ validates against
# the generated JSON Schema and adds the per-entity and graph-rule layers on top; the pytest suite
# runs it over the fixtures. Users run the same checker with `lambda-ber-schema rocrate validate`.
test-rocrate:
	$(RUN) pytest tests/test_rocrate_profile.py

# Validate a crate the way a user would: make validate-rocrate CRATE=path/to/ro-crate-metadata.json
validate-rocrate:
	$(RUN) lambda-ber-schema rocrate validate $(CRATE)

serve:
	$(RUN) mkdocs serve
