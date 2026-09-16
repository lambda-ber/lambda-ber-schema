# Public cryoET metadata examples

Dataset DS-10000, run TS_026 (portal RN-241), retrieved 2026-09-15.

The five YAML files are complete reserializations of the portal's published JSON metadata, not original upstream YAML files and not examples valid against LAMBDA. The source JSON URLs and SHA-256 checksums are recorded in [provenance.yaml](provenance.yaml). JSON-to-YAML round trips were checked for equality. Metadata authorship and dates are retained.

- [Dataset](dataset.yaml), [tomogram](tomogram.yaml), and [alignment](alignment.yaml)
- [Cytosolic ribosome annotation](ribosome.yaml) and [membrane annotation](membrane.yaml)
- [838 ribosome points](ribosome-points.ndjson): the complete, unmodified coordinate file
- [Portal preview](TS_026-preview.png): an unmodified representative image with point overlays

Full image volumes and segmentation masks remain linked remotely in the research report. These reference snapshots are outside `tests/data/valid/` because they use the upstream schema. Portal data are distributed under CC0; see the [AWS registry](https://registry.opendata.aws/cryoet-data-portal/). Credit: Irene de Teresa Trueba, Sara Goetz, and collaborators; [dataset and publication links](https://cryoetdataportal.czscience.com/datasets/10000).
