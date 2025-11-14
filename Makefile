RUN = uv run
SCHEMA := src/lambda_ber_schema/schema/lambda-ber-schema.yaml
DOCDIR := ./docs
PYDANTIC := src/lambda_ber_schema/pydantic.py

all: gen-project gendoc test-examples
test: gen-project test-examples

gen-project:
	$(RUN) gen-project --config-file config.yaml $(SCHEMA) -d assets

gen-pydantic: $(PYDANTIC)

$(PYDANTIC): $(SCHEMA)
	$(RUN) gen-pydantic $(SCHEMA) > $(PYDANTIC)

test-examples:
	$(RUN) linkml-run-examples -t yaml -t json -t ttl -s $(SCHEMA) -P conf/prefixes.yaml -e tests/data/valid -d examples

gendoc: $(DOCDIR)
	cp -pr src/docs/* $(DOCDIR)
	$(RUN) gen-doc ${GEN_DARGS} -d $(DOCDIR) $(SCHEMA)

serve:
	$(RUN) mkdocs serve
