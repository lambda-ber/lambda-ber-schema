# emsl-dev/

Development artifacts for the EMSL Science Central ETL integration.

---

## Files

### `swagger.json`

The OpenAPI 2.0 (Swagger) specification for the EMSL Science Central public API, retrieved from `https://api.emsl.pnnl.gov/external/swagger.json`.

Key endpoints documented:

| Endpoint | Auth | Used by loader |
|---|---|---|
| `POST /datasets/by_sample_name` | None | Yes — sample search |
| `GET /projects/{id}` | None | Yes — project/study metadata |
| `GET /resources/{id}` | None | Yes — instrument metadata |
| `GET /datasets/transaction_info/{tx_id}` | None | Yes — file listing |
| `GET /datasets/request/{tx_id}` | JWT | Yes — create download cart |
| `GET /datasets/download/{uuid}` | JWT | Yes — poll cart status |
| `DELETE /datasets/download/{uuid}` | JWT | No — cleanup only |
| `GET /datasets/info/{uuid}` | JWT | No — richer cart status |
| `GET /resources/all` | None | No — full instrument list |
| `GET /resources/grouping` | None | No — instrument classification |
| `GET /projects/data/{id}` | None | No — per-dataset release status |

> **Note:** The swagger schema defines `status` as an untyped string with no enum. Observed real values: `"waiting"` (not ready), `"staging"` (tape recall in progress), `"transfer"` (ready). The swagger's implied values (`"ready"`, `"complete"`) have never been observed in production.

---

### `api-field-inventory.yaml`

A field-by-field inventory of every response value available from the four active endpoints, annotated with:

- `loader_status`: `captured` / `ignored` / `not_used`
- `schema_target`: which schema class and field the value maps to
- `notes`: naming conventions, caveats, and observed examples

Covers:
- `POST /datasets/by_sample_name` — wrapper fields + `SampleTransaction` fields
- `GET /projects/{id}` — project/PI/member fields
- `GET /resources/{id}` — instrument fields
- `GET /datasets/transaction_info/{tx_id}` — file listing fields

Also includes the three unused endpoints (`/resources/all`, `/resources/grouping`, `/projects/data/{id}`) with their available fields and relevance notes.

---

### `api-to-schema-mapping.yaml`

Cross-reference between every API field and the `lambda-ber-schema` schema. Organized into four sections:

| Section | Meaning |
|---|---|
| **A. `captured`** | API field → schema field exists and loader maps it |
| **B. `loader_gaps`** | Schema field exists but loader does not populate it |
| **C. `schema_gaps`** | API field has no matching schema field (schema change needed) |
| **D. `schema_fields_without_api_source`** | Schema field exists but API doesn't expose it |

**Key findings:**

- **Loader currently creates base `Instrument`**, not `CryoEMInstrument` — all 8+ instrument spec fields (`accelerating_voltage`, `detector_model`, `cs`, etc.) are permanently unreachable until this is fixed (Phase 1 work).
- **`resource.active` is always `false`** for observed live instruments — known API bug; reference data should override.
- **`project_members[]`** contains ORCID, name, role, and institution — none is captured; no matching schema field exists at all (`Study.contributors` not yet in schema).
- **`is_released`** (from `/projects/data/{id}`) has no schema equivalent — `Dataset` has no embargo/release-status field.

**Highest-priority schema additions:**

1. `Study.contributors` — list with orcid, name, role, institution
2. `Study.award_doi` — currently stored only on `LoaderResult`, lost after serialization
3. `Dataset.is_released` — boolean or enum (embargoed/public/restricted)
4. `Instrument.website` — promote from `BeamlineInstrument` to base `Instrument`

---

### `metadata-sources.yaml`

Catalogue of metadata sources for the three categories of acquisition/instrument/sample data that the public Science Central API does **not** expose. Each source entry includes: location in the data pipeline, format, access method, available fields, feasibility rating, and implementation notes.

**Acquisition metadata** (magnification, pixel size, dose, defocus, etc.):

| Source | Feasibility | Status |
|---|---|---|
| EPU Session XML (inside `.tar` archives) | High | Implemented (Phase 2) — blocked on tape staging |
| EPU Session Summary YAML | Medium | Unverified — needs confirmation with PNNL |
| SerialEM `.mdoc` files (tomography) | High | Not implemented |
| EMSL AURORA / KriosGPU | Low | Internal systems, not publicly accessible |

**Instrument metadata** (accelerating voltage, detector model, Cs, etc.):

| Source | Feasibility | Status |
|---|---|---|
| `reference-data/facilities/emsl.yaml` (in-repo) | High | Exists but **currently ignored by loader** — Phase 1 work |
| `/resources/grouping` API call | High | Not called — would replace name-regex heuristics |
| BER Structural Biology Portal (manual curation) | High | Ground-truth for static specs |

**Sample/biological metadata** (organism, buffer, grid prep, etc.):

| Source | Feasibility | Status |
|---|---|---|
| EMSL User Proposal system | Low | Not in public API |
| `project.title` / `project.abstract` (NLP) | Medium | Not implemented |
| EMPIAR / EMDB (deposited datasets only) | Medium | Retroactive enrichment only |

---

### `jwt-auth.yaml`

JWT authentication notes for the download-cart endpoints.

**Auth surface:** Only the download cart and file download endpoints require a token. The four primary metadata endpoints are public (no auth).

**Flow:** OIDC `client_credentials` grant → bearer token → `EMSL_JWT` env var → `--token` CLI flag.

**Observed cart status lifecycle:**

```
waiting / "In Preparation"  →  staging / "File Retrieval"  →  transfer / "File Retrieval"
   (cart created)                (tape recall in progress)        (file ready to download)
```

> **Important API discrepancy:** `/datasets/download/{uuid}` and `/datasets/info/{uuid}` return different data for the same cart. During staging, `/download` shows `success: false, retrieval_url: null`; `/info` shows `success: true, retrieval_url: <path>`. Use `status == "transfer"` (not `success: true`) as the real readiness signal. The retrieval URL base is `/download_tracking/cart/{uuid}`, not `/external/`.

**Tape staging times:** Observed staging duration for a 366 MB single-file transaction is >90 minutes. EMSL uses Spectra Logic tape (HSM). Staging time depends on tape mount queue and whether the file has been recently accessed. The default `--epu-timeout` in the CLI is 30 minutes (1800 s); for cold-storage files increase to 2+ hours.

**Cart lifecycle:** Carts do not auto-cancel. Stale carts in `staging` state are harmless. Once a tape recall completes, the cart transitions to `transfer` and the download URL becomes active. Subsequent carts for the same transaction stage quickly (disk cache hit).

---

## Related Code

| File | Purpose |
|---|---|
| `src/lambda_ber_schema/loaders/emsl.py` | EMSL ETL loader — all API calls, EPU extraction, cart handling |
| `src/lambda_ber_schema/cli.py` | CLI entry point — `etl emsl` command with `--extract-epu`, `--token`, `--epu-timeout` |
| `reference-data/facilities/emsl.yaml` | Static instrument specs for Krios G3i and Aquilos 2 (currently ignored by loader) |
| `examples/Dataset-emsl-tx-*.yaml` | Example outputs from the loader for three PNCC transactions |

## Implementation Roadmap

**Phase 1 (no JWT required):**
- Upgrade loader to create `CryoEMInstrument` instead of base `Instrument`
- Merge `reference-data/facilities/emsl.yaml` at loader init to populate instrument spec fields
- Fix `current_status: offline` bug (override API's `active=false` using reference data)
- Call `/resources/grouping` to replace fragile name-regex instrument classification

**Phase 2 (JWT required — implemented, tape staging blocking demo):**
- EPU session XML extraction from `.tar` archives via download cart
- CLI flags: `--extract-epu`, `--token`, `--epu-timeout`
- Populates 13 `ExperimentRun` acquisition fields (magnification, dose, pixel size, etc.)

**Phase 3 (schema additions):**
- Add `Study.contributors` (orcid, name, role, institution)
- Add `Study.award_doi`
- Add `Dataset.is_released`
- Promote `Instrument.website` from `BeamlineInstrument` to base `Instrument`

**Phase 4 (future):**
- SerialEM `.mdoc` parser for tomography transactions
- NLP extraction of biological context from `project.abstract`
- EMPIAR cross-link for deposited datasets
