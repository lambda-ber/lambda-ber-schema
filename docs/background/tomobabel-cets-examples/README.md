# TomoBabel / CETS metadata examples

Companion files for the [TomoBabel / CETS background page](../tomobabel-cets.md), inspected on 2026-09-17.

| File | Origin and scope |
| --- | --- |
| [minimal-cets.yaml](minimal-cets.yaml) | Authored synthetic CETS Dataset, validated against core commit `0c8c4e3c7a2885f29caba551ffcaacde45c00101`. Includes an image, coordinate frames, a point annotation, and a particle-map reference. File paths are fictional. Uses a corner origin, not the centered rigid-converter profile. |
| [empiar-12104-tomogram.excerpt.yaml](empiar-12104-tomogram.excerpt.yaml) | Selected fields from an upstream CETS JSON example. Source values are unchanged; the referenced tilt series is omitted. Includes a real public MRC URL. The full historical source lacks 50 tilt-image IDs required by current core. |
| [portal-10445.excerpt.yaml](portal-10445.excerpt.yaml) | Selected fields from recorded portal converter input. This is not a CETS document. Includes real image URLs and a GO membrane annotation. The selected image and annotation metadata describe different sampling grids. |
| [provenance.yaml](provenance.yaml) | Exact repository revisions, source URLs, source and excerpt checksums, and transformation descriptions. |
| [validation.txt](validation.txt) | Results of local metadata checks against the pinned CETS model. |

The excerpts are reading aids, not complete submission or conformance fixtures. No volume arrays were downloaded for this page. The upstream JSON files remain linked from the provenance manifest; authorship and broader experimental context should be obtained from those sources and their associated archives.

## Reading the synthetic example

The image has 4 Å sampling and a corner-origin physical frame. Its point at `[40, 80, 24]` Å therefore corresponds to array coordinates `[10, 20, 6]`. The particle map's `coord_index: 0` refers to that first point. Its name deliberately makes no biological identification.

The example was validated with the patched Pydantic `Dataset` model from `cets_data_model.models.models`, then serialized to JSON and loaded again. YAML parsing or Pydantic acceptance does not check all referenced files, graph relationships, or spatial conventions. The real-data excerpts must not be mistaken for independently validated, complete CETS documents.
