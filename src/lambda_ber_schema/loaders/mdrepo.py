"""Metadata-only MDRepo import. No trajectory or other payload files are fetched.

The public API is documented at https://mdrepo.org/api/schema/swagger-ui/.
One entry may describe an ensemble; it does not establish individual replicate runs.
"""

import json
import math
import re
from collections import defaultdict
from pathlib import PurePosixPath
from typing import Any

import requests

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult, uniprot_curie
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.pydantic import Dataset, FileFormatEnum


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False)


def _quantity(value: float, unit: str) -> dict:
    return {"numeric_value": value, "unit": unit}


class MDRepoLoader(BaseLoader):
    """Load a public MDRepo entry or convert an archived API response offline."""

    source_name = "mdrepo"
    base_url = "https://mdrepo.org/api/v1"

    def __init__(self, cache: ResponseCache | None = None):
        self.cache = cache or ResponseCache(enabled=False)

    @staticmethod
    def normalize_id(identifier: str) -> int:
        match = re.fullmatch(r"(?:MDR)?([0-9]+)", identifier.strip(), re.IGNORECASE)
        if not match or int(match[1]) <= 0:
            raise ValueError(f"Invalid MDRepo identifier: {identifier!r}")
        return int(match[1])

    def load(self, identifier: str) -> LoaderResult:
        number = self.normalize_id(identifier)

        def fetch():
            response = requests.get(f"{self.base_url}/simulation_view/{number}", timeout=30)
            response.raise_for_status()
            return response.json()

        raw = self.cache.get_or_fetch(f"mdrepo/{number}", fetch)
        if raw.get("id") != number:
            raise ValueError("MDRepo response ID does not match the requested entry")
        return self.convert(raw)

    def list_entries(self, limit: int = 100, **filters: Any) -> list[str]:
        """List at most limit public entries using the API's search/filter parameters."""
        if limit < 0:
            raise ValueError("limit must be non-negative")
        if {"limit", "offset", "ids_only"} & filters.keys():
            raise ValueError("Pagination is managed by list_entries")
        entries = []
        while len(entries) < limit:
            response = requests.get(
                f"{self.base_url}/simulation_list",
                params={**filters, "limit": min(100, limit - len(entries)), "offset": len(entries)},
                timeout=30,
            )
            response.raise_for_status()
            page = response.json()
            rows = page["results"]
            entries.extend(row["slug"] for row in rows)
            if not rows or not page.get("next"):
                break
        return entries[:limit]

    def convert(self, raw: dict[str, Any]) -> LoaderResult:
        """Convert source JSON without network access, retaining it in LoaderResult.raw_data.

        Source-specific metadata stays in descriptions/processing_parameters as JSON.
        No binding interactions, replicate-specific provenance, dates of computation,
        or download URLs are inferred from an entry's inventory.
        """
        number = self.normalize_id(str(raw["id"]))
        slug = f"MDR{number:08d}"
        if raw.get("slug") != slug:
            raise ValueError("MDRepo slug and numeric ID disagree")
        software = raw.get("software") or {}
        if not software.get("name"):
            raise ValueError("MDRepo entry has no simulation software name")
        source_url = f"https://mdrepo.org/explore/{slug}"
        base = f"lambda:mdrepo/{slug}"
        sample, experiment, workflow = (f"{base}/{kind}" for kind in ("sample", "experiment", "workflow"))
        warnings = []
        for flag in ("is_placeholder", "is_deprecated", "is_embargoed", "is_coarse_grained"):
            if raw.get(flag):
                warnings.append(f"Source marks {slug} as {flag}; review before reuse.")
        params: dict[str, Any] = {
            "simulation_engine": software["name"],
            "simulation_engine_version": software.get("version"),
        }
        for source, target, unit in (
            ("duration", "duration_ns", "ns"),
            ("temperature", "temperature", "kelvin"),
            ("integration_timestep_fs", "timestep", "femtosecond"),
        ):
            value = raw.get(source)
            if value is not None:
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                    raise ValueError(f"Invalid {source}: {value!r}")
                if source != "duration" or raw.get("num_replicates") == 1:
                    params[target] = _quantity(value, unit)
        interval, timestep = raw.get("sampling_frequency"), raw.get("integration_timestep_fs")
        if interval is not None:
            if isinstance(interval, bool) or not isinstance(interval, (int, float)) or not math.isfinite(interval) or interval <= 0:
                raise ValueError("sampling_frequency must be a positive interval in ns")
            if timestep and timestep > 0:
                steps = interval * 1_000_000 / timestep
                if math.isclose(steps, round(steps), rel_tol=0, abs_tol=1e-6):
                    params["trajectory_output_interval"] = _quantity(round(steps), "steps")
                else:
                    warnings.append("Sampling interval is not an integral number of integration steps; retained in source parameters.")
            else:
                warnings.append("Sampling interval retained in ns; no positive integration timestep to convert it to steps.")
        if raw.get("water_type"):
            params["water_model"] = raw["water_type"]
        else:
            warnings.append("No structured water model; prose was not interpreted as a structured value.")
        # forcefield can combine protein and ligand models; do not assign it to either.
        source_parameters = {k: raw[k] for k in (
            "num_replicates", "duration", "forcefield", "forcefield_comments", "sampling_frequency",
            "run_commands", "protonation_method", "water_density", "solutes", "pdb",
            "pub", "external_links", "creators", "contributor", "creation_date",
            "is_coarse_grained", "is_placeholder", "is_deprecated", "is_embargoed",
            "superseding_simulation_id",
        ) if k in raw}
        source_parameters["source_url"] = source_url
        source_parameters["duration_unit"] = "ns (source entry value; may aggregate replicates)"
        source_parameters["sampling_frequency_unit"] = "ns between saved frames"
        if (raw.get("num_replicates") or 0) > 1:
            warnings.append(f"Entry describes {raw['num_replicates']} replicates; retained as one ensemble workflow. Source duration is preserved without treating it as per-replicate duration.")
        ds: dict[str, Any] = {
            "id": base,
            "title": raw.get("short_description") or slug,
            "description": f"Metadata imported from {source_url}.\n\n{raw.get('description') or ''}",
            "keywords": ["MDRepo", "molecular dynamics", "metadata-only import"],
            "samples": [{"id": sample, "sample_code": slug,
                         "sample_type": "complex" if raw.get("ligands") or len(raw.get("chains", [])) > 1 else "protein",
                         "description": "Computational molecular system represented using Sample; no physical preparation is asserted."}],
            "experiment_runs": [{"id": experiment, "experiment_code": slug, "technique": "molecular_dynamics"}],
            "workflow_runs": [{"id": workflow, "workflow_code": slug, "workflow_type": "md_production",
                               "software_name": software["name"], "software_version": software.get("version"),
                               "description": raw.get("description"), "md_simulation_params": params,
                               "processing_parameters": _json(source_parameters)}],
            "experiment_sample_associations": [{"experiment_id": experiment, "sample_id": sample}],
            "workflow_experiment_associations": [{"workflow_id": workflow, "experiment_id": experiment}],
        }
        collections = raw.get("collections") or [{"id": number, "name": slug}]
        for collection in collections:
            study = f"lambda:mdrepo/collection/{collection['id']}" if raw.get("collections") else f"{base}/study"
            ds.setdefault("studies", []).append({"id": study, "title": collection["name"]})
            for table, key, value in (
                ("study_sample_associations", "sample_id", sample),
                ("study_experiment_associations", "experiment_id", experiment),
                ("study_workflow_associations", "workflow_id", workflow),
            ):
                ds.setdefault(table, []).append({"study_id": study, key: value})
        self._proteins(raw, ds, base, sample, warnings)
        self._ligands(raw, ds, base, sample)
        self._files(raw, ds, base, experiment, workflow, warnings)
        warnings.append("MD5 hashes are retained in file descriptions; DataFile.checksum is reserved for SHA-256. Payloads were not downloaded or verified.")
        return LoaderResult(dataset=Dataset.model_validate(ds), warnings=warnings,
                            source_url=source_url, raw_data=raw)

    @staticmethod
    def _proteins(raw, ds, base, sample, warnings):
        canonical = {p["uniprot_id"]: p for p in raw.get("uniprot", [])}
        groups = defaultdict(list)
        identities = {}
        for chain in raw.get("chains", []):
            polymer = chain["polymer"]
            if polymer["polymer_type"] != "protein":
                warnings.append(f"Chain {chain['chain_order']} is {polymer['polymer_type']}; retained only in source JSON by this protein pilot.")
                continue
            matches = polymer.get("uniprots") or []
            accession = matches[0]["uniprot"]["uniprot_id"] if len(matches) == 1 else ""
            protein_id = uniprot_curie(accession)
            if protein_id:
                reference = canonical.get(accession, matches[0]["uniprot"])
                identities[protein_id] = {"id": protein_id, "uniprot_id": protein_id,
                                          "protein_name": reference.get("name"),
                                          "amino_acid_sequence": reference.get("sequence")}
            else:
                protein_id = f"{base}/polymer/{polymer['id']}"
                identities[protein_id] = {"id": protein_id, "amino_acid_sequence": polymer.get("sequence")}
                warnings.append(f"Chain {chain['chain_order']} has no single valid UniProt match; kept as a local protein with its simulated sequence.")
            groups[protein_id].append(chain)
        ds["proteins"] = list(identities.values())
        for protein_id, chains in groups.items():
            first = chains[0]
            component_id = f"{base}/component/chain/{first['chain_order']}"
            chain_metadata = [dict(c, polymer={k: v for k, v in c["polymer"].items() if k != "residues"}) for c in chains]
            ds.setdefault("sample_components", []).append({
                "id": component_id, "sample_id": sample, "component_type": "protein",
                "protein_id": protein_id, "copy_number": len(chains), "description": _json(chain_metadata),
            })
            association = {"sample_id": sample, "protein_id": protein_id, "copy_number": len(chains),
                           "chain_ids": [c["chain_label"] for c in chains if c.get("chain_label")]}
            if len({c["polymer"].get("sequence") for c in chains}) == 1:
                construct = f"{base}/construct/{first['chain_order']}"
                ds.setdefault("protein_constructs", []).append({
                    "id": construct, "construct_id": f"{raw['slug']}-chain-{first['chain_order']}",
                    "protein_id": protein_id,
                    "construct_description": "Simulated sequence and source alignment; no cloning or expression history asserted.",
                    "description": _json(chain_metadata),
                })
                association["construct_id"] = construct
            else:
                warnings.append(f"Multiple simulated sequences map to {protein_id}; preserved on the component without choosing one construct.")
            # Alignment coordinates are canonical; source first/last_residue are structure numbering.
            ranges = {(m.get("reference_start"), m.get("reference_end")) for c in chains for m in c["polymer"].get("uniprots", [])}
            if protein_id.startswith("uniprot:") and len(ranges) == 1:
                start, end = next(iter(ranges))
                if start and end and 0 < start <= end:
                    association["residue_range"] = f"{start}-{end}"
            ds.setdefault("sample_protein_associations", []).append(association)

    @staticmethod
    def _ligands(raw, ds, base, sample):
        for index, ligand in enumerate(raw.get("ligands", []), 1):
            # A short ligand name is not proof of a wwPDB CCD identifier.
            molecule = f"{base}/ligand/{index}"
            ds.setdefault("small_molecules", []).append({
                "id": molecule, "small_molecule_name": ligand["name"],
                **{k: ligand[k] for k in ("smiles", "inchi", "inchikey") if ligand.get(k)},
                "description": _json({k: ligand[k] for k in ("declared_identity", "chain") if k in ligand}),
            })
            ds.setdefault("sample_components", []).append({
                "id": f"{base}/component/ligand/{index}", "sample_id": sample,
                "component_type": "small_molecule", "small_molecule_id": molecule,
            })

    @staticmethod
    def _files(raw, ds, base, experiment, workflow, warnings):
        formats = {value.value for value in FileFormatEnum}
        for group in ("uploaded_files", "processed_files"):
            for source in raw.get(group, []):
                extension = PurePosixPath(source["filename"]).suffix.lower().lstrip(".")
                file_format = {"txt": "ascii", "tgz": "gz", "nc": "netcdf"}.get(extension, extension)
                if file_format not in formats:
                    warnings.append(f"Unsupported file format for {source['filename']}; file remains in source JSON.")
                    continue
                file_id = f"{base}/{group}/{source['id']}"
                kind = source["file_type"].lower()
                data_type = None
                if "trajector" in kind:
                    data_type = "trajectory"
                elif "topology" in kind:
                    data_type = "topology"
                elif "structure" in kind:
                    data_type = "model"
                elif kind == "checkpoint":
                    data_type = "restart"
                elif kind in ("metadata", "input"):
                    data_type = "metadata"
                ds.setdefault("data_files", []).append({
                    "id": file_id, "file_name": source["filename"], "file_format": file_format,
                    "file_size_bytes": _quantity(source["file_size_bytes"], "bytes") if source.get("file_size_bytes") is not None else None,
                    "data_type": data_type, "related_entity": experiment,
                    "description": _json({"source_group": group, **source}),
                })
                # Processed derivatives have no exposed processing-run provenance.
                if group == "uploaded_files":
                    if kind in ("topology", "input"):
                        ds.setdefault("workflow_input_associations", []).append({"workflow_id": workflow, "file_id": file_id})
                    elif kind == "trajectory" or kind == "trajectories (all)":
                        ds.setdefault("workflow_output_associations", []).append({"workflow_id": workflow, "file_id": file_id})
