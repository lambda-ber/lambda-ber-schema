# lambda-ber-schema and IHMCIF Alignment

## Summary

lambda-ber-schema should align to IHMCIF, not import it as a native submodel.

IHMCIF is the PDB-IHM extension of PDBx/mmCIF for archived integrative and hybrid structural models. It is strongest where the final scientific product is a deposited integrative model: model representations, structural assemblies, model groups, ensembles, spatial restraints, starting models, and multi-state schemes.

lambda-ber-schema has a broader upstream scope. It tracks samples, preparations, instruments, experiment runs, workflow runs, raw and intermediate files, multimodal imaging, and facility or laboratory provenance. Many Lambda records may never become a PDB-IHM deposition.

## Current Dictionary Scale

The IHMCIF extension dictionary inspected for this alignment was `mmcif_ihm_ext.dic` version `1.28`, last updated `2025-03-24`, from the wwPDB dictionary site:

- https://mmcif.wwpdb.org/dictionaries/mmcif_ihm.dic/Index/
- https://mmcif.wwpdb.org/dictionaries/ascii/mmcif_ihm_ext.dic

The extension dictionary contains roughly:

- 83 active IHM categories
- 622 IHM data items
- additional extension items on existing PDBx/mmCIF categories, such as `_atom_site.ihm_model_id`

That size is large enough that directly importing IHMCIF would reshape Lambda around an archive and deposition format. The better approach is to keep Lambda generic and add mappings where concepts correspond.

## Design Decision

Do not import IHMCIF categories as first-class Lambda tables by default.

Instead:

- Keep Lambda concepts generic and workflow-centered.
- Use IHMCIF as an external mapping target.
- Prefer `close_mappings` and `related_mappings` over `exact_mappings` unless a slot has the same semantics as an IHMCIF item.
- Add new Lambda classes only when a concept is broadly useful outside PDB-IHM deposition.

This keeps Lambda useful for local data management, multimodal BER experiments, and pre-deposition provenance while still allowing export to IHMCIF/PDB-IHM when appropriate.

## Conceptual Alignment

| IHMCIF area | Lambda alignment | Mapping strength | Notes |
| --- | --- | --- | --- |
| `_ihm_entry_collection`, `_ihm_dataset_group` | `Dataset`, `Study` | Related | Lambda groups all local research records; IHMCIF groups deposited entries or evidence datasets. |
| `_ihm_dataset_list` | `ExperimentRun`, `DataFile`, workflow input associations | Related/close | Lambda separates runs, files, and workflow links rather than using IHMCIF dataset records directly. |
| `_ihm_external_files`, `_ihm_external_reference_info` | `DataFile` | Close | Lambda file metadata is broader and can include local paths, storage URIs, checksums, and non-deposition files. |
| `_ihm_modeling_protocol`, `_ihm_modeling_protocol_details` | `WorkflowRun` | Close | Lambda workflow runs map well conceptually, but IHMCIF has deposition-specific protocol steps and references. |
| `_ihm_struct_assembly`, `_ihm_struct_assembly_details`, `_ihm_entity_poly_segment` | `Sample`, `MolecularComposition` | Related | Lambda samples are physical/biological inputs; IHMCIF assemblies are modeled structural components. |
| `_ihm_model_representation`, `_ihm_model_list`, `_ihm_model_group`, `_ihm_ensemble_info` | `WorkflowRun`, `RefinementParameters`, `QualityMetrics`, `DataFile` | Related | Lambda can point to model outputs, but does not currently encode IHMCIF's full representation and ensemble model. |
| `_ihm_3dem_restraint`, `_ihm_sas_restraint` | `Image3D`, `SAXSPreparation`, `QualityMetrics`, `DataFile` | Related | Lambda captures source experiments and files; IHMCIF captures how those data constrain a deposited model. |
| Crosslink, HDX, EPR, geometric, predicted-contact, and probe restraints | No direct generic class yet | Gap | A future generic `Evidence` or `Restraint` concept could align here without importing all IHMCIF categories. |
| Multi-state schemes, ordered ensembles, kinetics | Limited or absent | Gap | These should remain future work unless Lambda needs broad dynamic or multi-state modeling support. |

## Schema Changes

The schema now includes an `IHMCIF` prefix:

```yaml
IHMCIF: https://mmcif.wwpdb.org/dictionaries/mmcif_ihm_ext.dic/Items/
```

Mappings were added only to existing Lambda concepts:

- `Dataset` and `Study` relate to IHMCIF entry collections and dataset groups.
- `Sample` and `MolecularComposition` relate to structural assemblies and polymer segments.
- `ExperimentRun` relates to IHMCIF dataset records.
- `WorkflowRun` closely maps to IHMCIF modeling protocol categories.
- `DataFile` closely maps to IHMCIF external file records and relates to dataset references.
- `Image3D`, `SAXSPreparation`, and `QualityMetrics` relate to 3DEM and SAS restraint categories.
- Workflow association tables relate to IHMCIF dataset and model group link categories.

The mappings are intentionally conservative. Lambda should not claim `exact_mappings` for broad concepts that only partially overlap IHMCIF deposition categories.

## Gaps Worth Tracking

If PDB-IHM export becomes a requirement, the highest-value generic additions would be:

1. `ExternalDataset`: a dataset or evidence object distinct from a file.
2. `Evidence`: a generic record connecting an experiment, data file, measurement type, and interpretation.
3. `Restraint`: a generic modeling constraint with type, source data, target features, and confidence.
4. `ModelRepresentation`: a generic description of atomic, coarse-grained, mixed, or ensemble model outputs.
5. `ModelGroup` or `Ensemble`: a generic grouping of output models with representative or clustering metadata.

These should be designed for Lambda first, then mapped to IHMCIF. They should not copy the full IHMCIF category tables unless deposition-grade PDB-IHM support becomes a core objective.

## Export Implications

A future Lambda-to-IHMCIF exporter should:

- use Lambda records as upstream provenance;
- use `DataFile` and workflow associations to populate IHMCIF datasets and external files;
- use `WorkflowRun` records to populate modeling protocol categories;
- map only explicit generic evidence/restraint/model representation records into IHMCIF restraints and model categories;
- use `python-ihm` or a comparable library rather than hand-writing CIF text.

Without additional generic evidence and model-representation classes, Lambda can support partial IHMCIF metadata export, but not complete PDB-IHM deposition.

## References

- PDB-IHM data system: https://data.pdb-ihm.org/
- IHMCIF dictionary index: https://mmcif.wwpdb.org/dictionaries/mmcif_ihm.dic/Index/
- IHMCIF extension dictionary: https://mmcif.wwpdb.org/dictionaries/ascii/mmcif_ihm_ext.dic
- IHMCIF GitHub repository: https://github.com/ihmwg/IHMCIF
