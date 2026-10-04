"""
PDB (Protein Data Bank) loader.

API Documentation: https://data.rcsb.org/

An entry is fetched as the RCSB Data API serves it: the entry record, one record per
polymer, non-polymer and branched entity, one per chemical component, one per assembly,
and one per interface of the first assembly. ``pdb_field_map.yaml`` says where every field
of those records goes; ``pdb_coverage.py`` checks that nothing goes unaccounted for.

The deposited specimen becomes one Sample, with a SampleComponent per entity. EM entries
that name sub-assemblies get a child Sample for each, and NMR entries a child Sample per
solution. What RCSB says about which part touches which (interfaces between polymers,
the chain a ligand or glycan sits on) becomes SampleComponentInteraction rows.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

import requests

from lambda_ber_schema.loaders.base import (
    BaseLoader,
    LoaderResult,
    nucleotide_sequence,
    uniprot_curie,
)
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.loaders.pdb_coverage import extra_values, unit_for
from lambda_ber_schema.pydantic import (
    CryoEMInstrument,
    Dataset,
    Instrument,
    NMRInstrument,
    SAXSInstrument,
    XRayInstrument,
)


#: mmCIF _entity_poly.type values for nucleic acid polymers.
_ENTITY_POLY_TYPES = {
    "polydeoxyribonucleotide": "dna",
    "polyribonucleotide": "rna",
    "polydeoxyribonucleotide/polyribonucleotide hybrid": "dna_rna_hybrid",
    "peptide nucleic acid": "peptide_nucleic_acid",
}

#: RCSB's coarser rcsb_entity_polymer_type, used when _entity_poly.type is absent.
_RCSB_POLYMER_TYPES = {
    "dna": "dna",
    "rna": "rna",
    "na-hybrid": "dna_rna_hybrid",
}

#: _exptl.method to the schema's technique.
_TECHNIQUES = {
    "X-RAY DIFFRACTION": "xray_crystallography",
    "NEUTRON DIFFRACTION": "neutron_crystallography",
    "FIBER DIFFRACTION": "fiber_diffraction",
    "POWDER DIFFRACTION": "powder_diffraction",
    "ELECTRON MICROSCOPY": "cryo_em",
    "ELECTRON CRYSTALLOGRAPHY": "microed",
    "SOLUTION NMR": "solution_nmr",
    "SOLID-STATE NMR": "solid_state_nmr",
    "SOLUTION SCATTERING": "saxs",
    "EPR": "epr",
    "FLUORESCENCE TRANSFER": "fluorescence_transfer",
    "INFRARED SPECTROSCOPY": "infrared_spectroscopy",
    "INTEGRATIVE": "integrative_modeling",
}

#: _diffrn_radiation.pdbx_scattering_type to the technique of a diffraction run.
_SCATTERING_TECHNIQUES = {
    "x-ray": "xray_crystallography",
    "neutron": "neutron_crystallography",
    "electron": "microed",
}

#: _em_experiment.reconstruction_method to ExperimentalMethodEnum.
_EM_METHODS = {
    "SINGLE PARTICLE": "single_particle_analysis",
    "HELICAL": "helical_reconstruction",
    "SUBTOMOGRAM AVERAGING": "subtomogram_averaging",
    "TOMOGRAPHY": "electron_tomography",
    "CRYSTALLOGRAPHY": "electron_crystallography",
    "ELECTRON CRYSTALLOGRAPHY": "electron_crystallography",
}

#: _em_entity_assembly.type to SampleTypeEnum.
_EM_SAMPLE_TYPES = {
    "COMPLEX": "complex",
    "VIRUS": "virus",
    "ORGANELLE OR CELLULAR COMPONENT": "organelle",
    "CELL": "cell",
    "TISSUE": "tissue",
}

#: _em_software.category to the workflow stage it belongs to. Categories not named here are
#: listed on the reconstruction workflow as additional software.
_EM_SOFTWARE_STAGES = {
    "PARTICLE SELECTION": "particle_picking",
    "CTF CORRECTION": "ctf_estimation",
    "CLASSIFICATION": "classification_2d",
    "INITIAL EULER ASSIGNMENT": "reconstruction",
    "FINAL EULER ASSIGNMENT": "reconstruction",
    "RECONSTRUCTION": "reconstruction",
    "MODEL FITTING": "model_building",
    "MODEL REFINEMENT": "model_refinement",
}

#: The workflow type of each EM stage.
_EM_STAGE_TYPES = {
    "particle_picking": "particle_picking",
    "ctf_estimation": "ctf_estimation",
    "classification_2d": "classification_2d",
    "reconstruction": "refinement",
    "model_building": "model_building",
    "model_refinement": "model_refinement",
}

#: _software.classification to the diffraction workflow it belongs to.
_XRAY_SOFTWARE_STAGES = {
    "data reduction": "integration",
    "data scaling": "scaling",
    "phasing": "phasing",
    "model building": "model_building",
    "refinement": "refinement",
}

#: _pdbx_nmr_software.classification to the NMR workflow it belongs to.
_NMR_SOFTWARE_STAGES = {
    "refinement": "refinement",
    "structure calculation": "model_building",
    "structure solution": "model_building",
}

#: _refine.pdbx_method_to_determine_struct, lower-cased and prefix-matched, to PhasingMethodEnum.
_PHASING_METHODS = (
    ("molecular replacement", "molecular_replacement"),
    ("siras", "siras"),
    ("miras", "miras"),
    ("sad", "sad"),
    ("mad", "mad"),
    ("sir", "sir"),
    ("mir", "mir"),
)

#: _refine_ls_restr.type values that report bond and angle deviations.
_BOND_RESTRAINTS = {"r_bond_refined_d", "f_bond_d", "x_bond_d", "c_bond_d", "t_bond_d", "s_bond_d"}
_ANGLE_RESTRAINTS = {
    "r_angle_refined_deg",
    "f_angle_d",
    "x_angle_deg",
    "c_angle_deg",
    "t_angle_deg",
    "s_angle_d",
}

#: _diffrn_source.source to XRaySourceTypeEnum.
_XRAY_SOURCES = {
    "SYNCHROTRON": "synchrotron",
    "ROTATING ANODE": "rotating_anode",
    "LIQUID ANODE": "metal_jet",
}

#: _diffrn_source.pdbx_synchrotron_site, upper-cased, to FacilityEnum. Sites not named here are
#: written into the instrument title instead.
_FACILITIES = {
    "NSLS-II": "NSLS_II",
    "NSLS II": "NSLS_II",
    "ALS": "ALS",
    "SSRL": "SSRL",
    "ESRF": "ESRF",
    "DIAMOND": "DIAMOND",
    "PHOTON FACTORY": "PHOTON_FACTORY",
    "APS": "APS",
    "SPRING-8": "SPRING8",
    "SPRING8": "SPRING8",
    "PETRA III, DESY": "PETRA_III",
    "PETRA III, EMBL C/O DESY": "PETRA_III",
    "PETRA III": "PETRA_III",
    "SOLEIL": "SOLEIL",
    "AUSTRALIAN SYNCHROTRON": "AUSTRALIAN_SYNCHROTRON",
    "ORNL SPALLATION NEUTRON SOURCE": "SNS",
    "ORNL HIGH FLUX ISOTOPE REACTOR": "HFIR",
}

#: _diffrn_detector.detector to DetectorTechnologyEnum.
_XRAY_DETECTORS = {
    "CCD": "ccd",
    "PIXEL": "hybrid_photon_counting",
    "IMAGE PLATE": "imaging_plate",
    "CMOS": "cmos",
    "FILM": "film",
}

#: _em_image_recording.detector_mode to DetectorModeEnum.
_EM_DETECTOR_MODES = {
    "COUNTING": "counting",
    "SUPER-RESOLUTION": "super_resolution",
    "INTEGRATING": "integrating",
}

#: Leading words of a microscope or detector model, to the manufacturer.
_MANUFACTURERS = (
    ("TFS", "Thermo Fisher Scientific"),
    ("FEI", "Thermo Fisher Scientific"),
    ("THERMO", "Thermo Fisher Scientific"),
    ("JEOL", "JEOL"),
    ("HITACHI", "Hitachi"),
    ("ZEISS", "Zeiss"),
    ("PHILIPS", "Philips"),
    ("GATAN", "Gatan"),
    ("DIRECT ELECTRON", "Direct Electron"),
    ("TVIPS", "TVIPS"),
    ("DECTRIS", "Dectris"),
)

#: Detector models that are direct electron detectors.
_DIRECT_ELECTRON_MODELS = ("K2", "K3", "FALCON", "DE-", "DE ", "CETA-D", "APOLLO")

#: Host genera, to ExpressionSystemEnum.
_EXPRESSION_SYSTEMS = {
    "bacteria": (
        "Escherichia", "Bacillus", "Lactococcus", "Pseudomonas", "Streptomyces", "Mycobacterium",
        "Corynebacterium", "Thermus", "Vibrio", "Salmonella", "Caulobacter",
    ),
    "yeast": ("Saccharomyces", "Komagataella", "Pichia", "Schizosaccharomyces", "Kluyveromyces"),
    "insect": ("Spodoptera", "Trichoplusia", "Drosophila", "Bombyx"),
    "mammalian": (
        "Homo", "Mus", "Cricetulus", "Chlorocebus", "Rattus", "Mesocricetus", "Cercopithecus",
        "Sus", "Bos", "Canis", "Oryctolagus",
    ),
}

#: _rcsb_binding_affinity.type to BindingAffinityTypeEnum.
_AFFINITY_TYPES = {"Kd": "kd", "Ki": "ki", "IC50": "ic50", "EC50": "ec50", "Ka": "ka", "Km": "km"}

#: rcsb_polymer_entity_annotation.type, and other database names, to DatabaseNameEnum.
_DATABASE_NAMES = {
    "pfam": "pfam",
    "interpro": "interpro",
    "cath": "cath",
    "scop": "scop",
    "scop2": "scop2",
    "scop2b": "scop2",
    "ecod": "ecod",
    "mpstruc": "mpstruc",
    "opm": "opm",
    "pdbtm": "pdbtm",
    "memprotmd": "memprotmd",
    "chembl": "chembl",
    "drugbank": "drugbank",
    "pubchem": "pubchem",
    "chebi": "chebi",
    "uniprot": "uniprot",
    "pdb": "pdb",
    "emdb": "emdb",
    "bmrb": "bmrb",
    "sasbdb": "sasbdb",
    "empiar": "empiar",
    "pdb-ihm": "pdb_ihm",
    "pdbdev": "pdb_ihm",
    "nakb": "nakb",
    "ndb": "ndb",
    "sb grid": "sbgrid",
    "sbgrid": "sbgrid",
    "protein diffraction": "proteindiffraction",
    "olderado": "olderado",
    "glytoucan": "glytoucan",
    "glygen": "glygen",
    "bindingdb": "bindingdb",
    "binding moad": "binding_moad",
    "pdbbind": "pdbbind",
    "genbank": "insdc",
    "embl": "insdc",
    "refseq": "refseq",
    "go": "go",
}

#: Patterns the schema puts on slots the loader fills from free text.
_AMINO_ACIDS = re.compile(r"^[ACDEFGHIKLMNPQRSTVWYBJOUXZ]+$")
_ORCID = re.compile(r"(\d{4}-\d{4}-\d{4}-\d{3}[0-9X])$")


def _nucleic_acid_type(entity: dict[str, Any]) -> str | None:
    """The schema's nucleic acid type for a polymer entity, or None for a protein or other polymer."""
    entity_poly = entity.get("entity_poly", {})
    poly_type = (entity_poly.get("type") or "").lower()
    if poly_type in _ENTITY_POLY_TYPES:
        return _ENTITY_POLY_TYPES[poly_type]
    return _RCSB_POLYMER_TYPES.get((entity_poly.get("rcsb_entity_polymer_type") or "").lower())


def _is_protein(entity: dict[str, Any]) -> bool:
    return "protein" in (entity.get("entity_poly", {}).get("rcsb_entity_polymer_type") or "").lower()


def _rows(record: dict[str, Any], category: str) -> list[dict[str, Any]]:
    """A category's rows as a list, whether RCSB serves it as a list or a single object."""
    value = record.get(category)
    if value is None:
        return []
    if isinstance(value, list):
        return [v for v in value if isinstance(v, dict)]
    return [value] if isinstance(value, dict) else []


def _date(value: Any) -> str | None:
    """An RCSB timestamp trimmed to YYYY-MM-DD."""
    if not value:
        return None
    return str(value).split("T")[0]


def _qv(value: Any, unit: str, **extra: Any) -> dict[str, Any] | None:
    """A QuantityValue dict, or None when there is no number."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, str):
        try:
            value = float(value.split(",")[0].strip())
        except ValueError:
            return None
    return {"numeric_value": value, "unit": unit, **extra}


def _text(*parts: Any, sep: str = "; ") -> str | None:
    """Join the non-empty parts, dropping repeats, or None when nothing is left."""
    seen: list[str] = []
    for part in parts:
        if part is None:
            continue
        text = str(part).strip()
        if text and text not in seen:
            seen.append(text)
    return sep.join(seen) if seen else None


def _slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()


def _manufacturer(model: str | None) -> str | None:
    if not model:
        return None
    upper = model.upper()
    for prefix, name in _MANUFACTURERS:
        if upper.startswith(prefix):
            return name
    return None


def _expression_system(scientific_name: str | None) -> str | None:
    if not scientific_name:
        return None
    genus = scientific_name.split()[0]
    for system, genera in _EXPRESSION_SYSTEMS.items():
        if genus in genera:
            return system
    return None


def _database_name(name: str | None) -> str:
    return _DATABASE_NAMES.get((name or "").strip().lower(), "other")


def _residue_ranges(numbers: list[int]) -> str:
    """Residue numbers written compactly: [1, 2, 3, 7] becomes '1-3,7'."""
    out: list[str] = []
    numbers = sorted(set(numbers))
    start: int | None = None
    prev: int | None = None
    for n in numbers:
        if start is None:
            start = prev = n
        elif prev is not None and n == prev + 1:
            prev = n
        else:
            out.append(f"{start}-{prev}" if start != prev else f"{start}")
            start = prev = n
    if start is not None:
        out.append(f"{start}-{prev}" if start != prev else f"{start}")
    return ",".join(out)


@dataclass
class RawPDBEntry:
    """Everything fetched for one entry, by kind of record."""

    entry: dict[str, Any]
    polymer_entities: list[dict[str, Any]] = field(default_factory=list)
    nonpolymer_entities: list[dict[str, Any]] = field(default_factory=list)
    branched_entities: list[dict[str, Any]] = field(default_factory=list)
    chemcomps: dict[str, dict[str, Any]] = field(default_factory=dict)
    assemblies: list[dict[str, Any]] = field(default_factory=list)
    interfaces: list[dict[str, Any]] = field(default_factory=list)

    def by_kind(self) -> dict[str, list[dict[str, Any]]]:
        """The records keyed by the kind names pdb_coverage uses."""
        return {
            "entry": [self.entry],
            "polymer_entity": self.polymer_entities,
            "nonpolymer_entity": self.nonpolymer_entities,
            "branched_entity": self.branched_entities,
            "chemcomp": list(self.chemcomps.values()),
            "assembly": self.assemblies,
            "interface": self.interfaces,
        }


class PDBLoader(BaseLoader):
    """
    Loader for PDB (Protein Data Bank).

    PDB is the worldwide repository for 3D structural data of biological
    macromolecules determined by X-ray crystallography, NMR, and cryo-EM.

    Example:
        >>> loader = PDBLoader()
        >>> result = loader.load("1HHO")
        >>> result.dataset.id
        'pdb:1HHO'
        >>> result.dataset.title
        'STRUCTURE OF HUMAN OXYHAEMOGLOBIN AT 2.1 ANGSTROMS RESOLUTION'
    """

    source_name = "pdb"
    base_url = "https://data.rcsb.org/rest/v1"

    #: Interfaces fetched per entry at most; a virus capsid has thousands.
    max_interfaces = 60

    def __init__(self, cache: ResponseCache | None = None):
        """
        Initialize the PDB loader.

        Args:
            cache: Optional response cache for development/testing
        """
        self.cache = cache or ResponseCache(enabled=False)

    def load(self, entry_id: str) -> LoaderResult:
        """
        Load a PDB entry by ID.

        Args:
            entry_id: PDB entry ID (e.g., "1HHO", "7S4S")

        Returns:
            LoaderResult with populated Dataset

        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If the entry is not found
        """
        entry_id = entry_id.upper()
        warnings: list[str] = []
        raw = self.fetch(entry_id, warnings)
        builder = _DatasetBuilder(entry_id, raw, warnings)
        dataset = builder.build()
        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            source_url=f"https://www.rcsb.org/structure/{entry_id}",
            doi=f"https://doi.org/10.2210/pdb{entry_id.lower()}/pdb",
            raw_data=raw.by_kind(),
        )

    def fetch(self, entry_id: str, warnings: list[str] | None = None) -> RawPDBEntry:
        """Fetch the entry and every record it points to."""
        warnings = warnings if warnings is not None else []
        entry_id = entry_id.upper()
        entry = self._get(f"core/entry/{entry_id}", cache_key=f"pdb/{entry_id}")
        if entry is None:
            raise ValueError(f"PDB entry {entry_id} not found")
        raw = RawPDBEntry(entry=entry)
        ids = entry.get("rcsb_entry_container_identifiers", {})
        for eid in ids.get("polymer_entity_ids") or []:
            record = self._get(
                f"core/polymer_entity/{entry_id}/{eid}",
                cache_key=f"pdb/{entry_id}/polymer_entity/{eid}",
            )
            if record is not None:
                raw.polymer_entities.append(record)
        for eid in ids.get("non_polymer_entity_ids") or []:
            record = self._get(f"core/nonpolymer_entity/{entry_id}/{eid}")
            if record is None:
                continue
            raw.nonpolymer_entities.append(record)
            comp_id = record.get("pdbx_entity_nonpoly", {}).get("comp_id")
            if comp_id and comp_id not in raw.chemcomps:
                comp = self._get(f"core/chemcomp/{comp_id}")
                if comp is not None:
                    raw.chemcomps[comp_id] = comp
        for eid in ids.get("branched_entity_ids") or []:
            record = self._get(f"core/branched_entity/{entry_id}/{eid}")
            if record is not None:
                raw.branched_entities.append(record)
        for n, aid in enumerate(ids.get("assembly_ids") or []):
            assembly = self._get(f"core/assembly/{entry_id}/{aid}")
            if assembly is None:
                continue
            raw.assemblies.append(assembly)
            if n:
                continue
            interface_ids = (
                assembly.get("rcsb_assembly_container_identifiers", {}).get("interface_ids") or []
            )
            if len(interface_ids) > self.max_interfaces:
                warnings.append(
                    f"Assembly {aid} has {len(interface_ids)} interfaces; only the first "
                    f"{self.max_interfaces} were fetched"
                )
            for iid in interface_ids[: self.max_interfaces]:
                record = self._get(f"core/interface/{entry_id}/{aid}/{iid}")
                if record is not None:
                    raw.interfaces.append(record)
        return raw

    def _get(self, path: str, cache_key: str | None = None) -> dict[str, Any] | None:
        """GET one Data API record, through the cache; None when RCSB answers 404."""

        def fetch() -> dict[str, Any]:
            response = requests.get(f"{self.base_url}/{path}", timeout=30)
            if response.status_code == 404:
                return {"_not_found": True}
            response.raise_for_status()
            return response.json()

        result = self.cache.get_or_fetch(cache_key or f"pdb/{path}", fetch)
        if not result or result.get("_not_found"):
            return None
        return result

    def list_entries(
        self,
        experimental_method: str | None = None,
        organism: str | None = None,
        limit: int | None = None,
    ) -> list[str]:
        """
        List available PDB entry IDs.

        Uses the RCSB search API to query entries.

        Args:
            experimental_method: Filter by method (X-RAY, EM, NMR, etc.)
            organism: Filter by organism scientific name
            limit: Maximum number of entries to return

        Returns:
            List of PDB entry IDs
        """
        query: dict[str, Any] = {"type": "terminal", "service": "text"}

        if experimental_method:
            method_map = {
                "X-RAY": "X-RAY DIFFRACTION",
                "XRAY": "X-RAY DIFFRACTION",
                "EM": "ELECTRON MICROSCOPY",
                "CRYO-EM": "ELECTRON MICROSCOPY",
                "NMR": "SOLUTION NMR",
            }
            method_value = method_map.get(
                experimental_method.upper(), experimental_method.upper()
            )
            query = {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "exptl.method",
                    "operator": "exact_match",
                    "value": method_value,
                },
            }
        elif organism:
            query = {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "rcsb_entity_source_organism.scientific_name",
                    "operator": "exact_match",
                    "value": organism,
                },
            }

        search_request = {
            "query": query,
            "return_type": "entry",
            "request_options": {
                "paginate": {"start": 0, "rows": limit or 100},
                "sort": [{"sort_by": "rcsb_accession_info.deposit_date", "direction": "desc"}],
            },
        }

        cache_key = f"pdb/search/{json.dumps(search_request, sort_keys=True)}"

        def fetch() -> dict[str, Any]:
            response = requests.post(
                "https://search.rcsb.org/rcsbsearch/v2/query",
                json=search_request,
                timeout=30,
            )
            response.raise_for_status()
            return {"status_code": response.status_code, "text": response.text}

        result = self.cache.get_or_fetch(cache_key, fetch)
        status_code = result.get("status_code")
        text = result.get("text", "")

        if status_code == 204 or not text:
            return []

        payload = json.loads(text)
        return [hit["identifier"] for hit in payload.get("result_set", [])]


class _DatasetBuilder:
    """Turns one RawPDBEntry into a Dataset. Rows are built as dicts and validated at the end."""

    def __init__(self, entry_id: str, raw: RawPDBEntry, warnings: list[str]):
        self.entry_id = entry_id
        self.raw = raw
        self.entry = raw.entry
        self.warnings = warnings
        self.base = f"pdb:{entry_id}"
        self.study_id = f"{self.base}/study"
        self.sample_id = f"{self.base}/sample"

        self.persons: list[dict] = []
        self.organizations: list[dict] = []
        self.publications: list[dict] = []
        self.instruments: list[Instrument] = []
        self.proteins: dict[str, dict] = {}
        self.constructs: list[dict] = []
        self.nucleic_acids: list[dict] = []
        self.small_molecules: dict[str, dict] = {}
        self.samples: list[dict] = []
        self.components: list[dict] = []
        self.preparations: list[dict] = []
        self.runs: list[dict] = []
        self.workflows: dict[str, dict] = {}
        self.refinement_workflows: list[dict] = []
        self.data_files: list[dict] = []
        self.sample_protein: list[dict] = []
        self.sample_nucleic_acid: list[dict] = []
        self.interactions: list[dict] = []
        self.experiment_samples: list[dict] = []
        self.experiment_instruments: list[dict] = []
        self.workflow_experiments: list[dict] = []
        self.study_persons: list[dict] = []
        self.study_organizations: list[dict] = []
        self.study_publications: list[dict] = []

        # entity id -> component id on the main sample, and author chain -> entity id
        self.component_by_entity: dict[str, str] = {}
        self.entity_by_chain: dict[str, str] = {}
        self.entity_weight: dict[str, float] = {}
        self.entity_sequence: dict[str, str] = {}
        self.methods = [row.get("method", "").upper() for row in _rows(self.entry, "exptl")]

    # ---- helpers -------------------------------------------------------------------

    def rows(self, category: str) -> list[dict[str, Any]]:
        return _rows(self.entry, category)

    def extras(self, target: dict, kind: str, record: dict, prefix: str, qualifier: str | None = None) -> None:
        """Append the record's metric fields to the target's additional_metrics and _properties."""
        metrics, properties = extra_values(kind, record, prefix)
        if qualifier:
            for item in metrics + properties:
                category, _, rest = item["attribute"]["label"].partition(".")
                item["attribute"]["label"] = f"{category}[{qualifier}].{rest}"
        if metrics:
            target.setdefault("additional_metrics", []).extend(metrics)
        if properties:
            target.setdefault("additional_properties", []).extend(properties)

    def add_property(self, target: dict, label: str, value: Any, attribute_id: str | None = None) -> None:
        if value is None or value == "":
            return
        target.setdefault("additional_properties", []).append(
            {"attribute": {"id": attribute_id or f"rcsb:{label}", "label": label}, "value": str(value)}
        )

    def workflow(self, key: str, workflow_type: str, title: str, **fields: Any) -> dict:
        """The workflow with this key, created on first use."""
        if key not in self.workflows:
            self.workflows[key] = {
                "id": f"{self.base}/workflow/{key}",
                "workflow_code": f"PDB-{self.entry_id}-{key.upper()}",
                "workflow_type": workflow_type,
                "title": title,
                "software_name": "Unknown",
                **fields,
            }
        return self.workflows[key]

    @staticmethod
    def add_software(workflow: dict, name: str | None, version: Any = None, note: str | None = None) -> None:
        """Name a program on a workflow: the first becomes software_name, the rest additional_software."""
        if not name:
            return
        if workflow.get("software_name") in (None, "Unknown") and not note:
            workflow["software_name"] = name
            if version:
                workflow["software_version"] = str(version)
            return
        label = _text(name, version, sep=" ")
        if note:
            label = f"{label} ({note.lower()})"
        workflow["additional_software"] = _text(workflow.get("additional_software"), label, sep=", ")

    @staticmethod
    def append_description(target: dict, *parts: Any) -> None:
        target["description"] = _text(target.get("description"), *parts)

    # ---- build -----------------------------------------------------------------------

    def build(self) -> Dataset:
        self.build_people_and_publications()
        self.build_molecules()
        self.build_samples()
        self.build_interactions()
        self.build_runs()
        self.build_workflows()
        self.build_data_files()
        return self.assemble()

    # ---- study, people, organizations, publications ---------------------------------------

    def study(self) -> dict:
        struct = self.entry.get("struct", {})
        keywords: list[str] = []
        kw = self.entry.get("struct_keywords", {})
        for word in [kw.get("pdbx_keywords")] + (kw.get("text") or "").split(","):
            if word and word.strip() and word.strip() not in keywords:
                keywords.append(word.strip())
        category = self.entry.get("pdbx_database_status", {}).get("methods_development_category")
        if category:
            keywords.append(category)
        study: dict[str, Any] = {
            "id": self.study_id,
            "title": struct.get("title") or f"PDB Entry {self.entry_id}",
            "description": _text(
                struct.get("pdbx_descriptor"),
                struct.get("pdbx_model_details"),
                struct.get("pdbx_model_type_details"),
            ),
            "keywords": keywords or None,
            "database_cross_references": self.cross_references() or None,
        }
        return study

    def cross_references(self) -> list[dict]:
        refs: dict[tuple[str, str], dict] = {}

        def add(name: str, identifier: Any, url: str | None = None, description: str | None = None) -> None:
            if not identifier:
                return
            key = (name, str(identifier))
            ref = refs.setdefault(key, {"database_name": name, "database_id": str(identifier)})
            if url and not ref.get("database_url"):
                ref["database_url"] = url
            ref["description"] = _text(ref.get("description"), description)

        for row in self.rows("database_2"):
            db = row.get("database_id")
            doi = row.get("pdbx_DOI")
            add(
                _database_name(db),
                row.get("database_code"),
                f"https://doi.org/{doi}" if doi else None,
                f"{db} identifier" if _database_name(db) == "other" else None,
            )
        ids = self.entry.get("rcsb_entry_container_identifiers", {})
        for emdb in ids.get("emdb_ids") or []:
            add("emdb", emdb, f"https://www.ebi.ac.uk/emdb/{emdb}", "map of this entry")
        for emdb in ids.get("related_emdb_ids") or []:
            add("emdb", emdb, f"https://www.ebi.ac.uk/emdb/{emdb}", "related map")
        for row in self.rows("rcsb_external_references"):
            add(_database_name(row.get("type")), row.get("id"), row.get("link"), row.get("type"))
        for row in self.rows("pdbx_database_related"):
            add(
                _database_name(row.get("db_name")),
                row.get("db_id"),
                None,
                _text(row.get("db_name"), row.get("content_type"), row.get("details")),
            )
        for row in self.rows("pdbx_database_PDB_obs_spr"):
            verb = "supersedes" if row.get("id") == "SPRSDE" else "obsoleted by"
            for code in (row.get("replace_pdb_id") or "").split():
                add("pdb", code, f"https://www.rcsb.org/structure/{code}", _text(
                    f"{row.get('pdb_id')} {verb} {code}", _date(row.get("date")), row.get("details")))
        for row in self.rows("pdbx_deposit_group"):
            add(
                "other",
                row.get("group_id"),
                f"https://www.rcsb.org/groups/{row.get('group_id')}",
                _text("PDB deposition group", row.get("group_type"), row.get("group_title"),
                      row.get("group_description")),
            )
        for row in self.rows("ihm_entry_collection_mapping"):
            add("pdb_ihm", row.get("collection_id"), None, "PDB-IHM collection")
        for row in self.rows("rcsb_ihm_dataset_source_db_reference"):
            add(_database_name(row.get("db_name")), row.get("accession_code"), None,
                _text(row.get("db_name"), "integrative modelling input"))
        return list(refs.values())

    def build_people_and_publications(self) -> None:
        primary = self.entry.get("rcsb_primary_citation", {})
        orcid_by_name = {}
        for name, orcid in zip(primary.get("rcsb_authors") or [], primary.get("rcsb_ORCID_identifiers") or []):
            match = _ORCID.search(orcid or "")
            if match:
                orcid_by_name[name] = f"https://orcid.org/{match.group(1)}"

        names_done: set[str] = set()
        for row in self.rows("audit_author"):
            name = row.get("name")
            if not name:
                continue
            position = row.get("pdbx_ordinal")
            person_id = f"{self.base}/person/{position or len(self.persons) + 1}"
            match = _ORCID.search(row.get("identifier_ORCID") or "")
            person = {
                "id": person_id,
                "title": name,
                "full_name": name,
                "orcid": f"https://orcid.org/{match.group(1)}" if match else orcid_by_name.get(name),
            }
            self.persons.append(person)
            names_done.add(name)
            self.study_persons.append(
                {"study_id": self.study_id, "person_id": person_id, "role": "author",
                 "author_position": position}
            )
        # Citation authors who are not deposition authors keep their ORCID through a Person row;
        # the publication's author list names them.
        for name, orcid in orcid_by_name.items():
            if name in names_done:
                continue
            self.persons.append({
                "id": f"{self.base}/person/citation-{len(self.persons) + 1}",
                "title": name,
                "full_name": name,
                "orcid": orcid,
                "description": "Author of the primary citation",
            })

        for row in self.rows("citation"):
            doi = row.get("pdbx_database_id_DOI")
            pmid = row.get("pdbx_database_id_PubMed")
            if row.get("id") == "primary" and not pmid:
                pmid = self.entry.get("rcsb_entry_container_identifiers", {}).get("pubmed_id")
            pub_id = (
                f"doi:{doi}" if doi else f"pmid:{pmid}" if pmid else f"{self.base}/citation/{row.get('id')}"
            )
            if any(p["id"] == pub_id for p in self.publications):
                continue
            self.publications.append({
                "id": pub_id,
                "title": row.get("title"),
                "doi": f"doi:{doi}" if doi else None,
                "pubmed_id": f"pmid:{pmid}" if pmid else None,
                "authors": row.get("rcsb_authors"),
                "journal": row.get("journal_full"),
                "journal_abbreviation": row.get("journal_abbrev"),
                "journal_issn": row.get("journal_id_ISSN"),
                "journal_country": row.get("country"),
                "volume": row.get("journal_volume"),
                "issue": row.get("journal_issue"),
                "page_first": row.get("page_first"),
                "page_last": row.get("page_last"),
                "year": row.get("year"),
                "language": row.get("language"),
                "book_title": row.get("book_title"),
                "book_publisher": row.get("book_publisher"),
                "book_publisher_city": row.get("book_publisher_city"),
                "book_isbn": row.get("book_id_ISBN"),
                "unpublished": True if row.get("unpublished_flag") == "Y" else None,
            })
            self.study_publications.append({
                "study_id": self.study_id,
                "publication_id": pub_id,
                "is_primary": row.get("id") == "primary" or row.get("rcsb_is_primary") == "Y",
            })

        for row in self.rows("pdbx_audit_support"):
            name = row.get("funding_organization")
            if not name:
                continue
            org_id = f"pdb:organization/{_slug(name)}"
            if not any(o["id"] == org_id for o in self.organizations):
                self.organizations.append({
                    "id": org_id,
                    "title": name,
                    "organization_type": "funding_agency",
                    "country": row.get("country"),
                })
            self.study_organizations.append({
                "study_id": self.study_id,
                "organization_id": org_id,
                "role": "funder",
                "award_number": row.get("grant_number"),
            })
        for row in self.rows("pdbx_SG_project"):
            name = row.get("full_name_of_center")
            if not name:
                continue
            org_id = f"pdb:organization/{_slug(name)}"
            if not any(o["id"] == org_id for o in self.organizations):
                self.organizations.append({
                    "id": org_id,
                    "title": name,
                    "acronym": row.get("initial_of_center"),
                    "organization_type": "consortium",
                    "description": row.get("project_name"),
                })
            self.study_organizations.append(
                {"study_id": self.study_id, "organization_id": org_id, "role": "collaborating_institution"}
            )

    # ---- molecules ---------------------------------------------------------------------

    def protein_role(self) -> str:
        count = sum(1 for e in self.raw.polymer_entities if _is_protein(e))
        return "target" if count == 1 else "subunit"

    def nucleic_acid_role(self) -> str:
        proteins = sum(1 for e in self.raw.polymer_entities if _is_protein(e))
        acids = sum(1 for e in self.raw.polymer_entities if _nucleic_acid_type(e) is not None)
        if proteins == 0:
            return "target" if acids == 1 else "subunit"
        return "binding_partner" if proteins == 1 else "subunit"

    def build_molecules(self) -> None:
        for entity in self.raw.polymer_entities:
            ids = entity.get("rcsb_polymer_entity_container_identifiers", {})
            eid = str(ids.get("entity_id") or entity.get("rcsb_id", "").split("_")[-1])
            poly = entity.get("entity_poly", {})
            chains = ids.get("auth_asym_ids") or [
                c.strip() for c in (poly.get("pdbx_strand_id") or "").split(",") if c.strip()
            ]
            for chain in chains:
                self.entity_by_chain[chain] = eid
            weight = entity.get("rcsb_polymer_entity", {}).get("formula_weight")
            if weight:
                self.entity_weight[eid] = weight
            self.entity_sequence[eid] = poly.get("pdbx_seq_one_letter_code_can") or ""
            if _nucleic_acid_type(entity) is not None:
                self.add_nucleic_acid(entity, eid, chains)
            elif _is_protein(entity):
                self.add_protein(entity, eid, chains)
            else:
                self.add_other_polymer(entity, eid)
        for entity in self.raw.nonpolymer_entities:
            self.add_nonpolymer(entity)
        for entity in self.raw.branched_entities:
            self.add_branched(entity)

    def entity_component(self, eid: str, component_type: str, title: str | None, **fields: Any) -> dict:
        component: dict[str, Any] = {
            "id": f"{self.base}/component/{eid}",
            "sample_id": self.sample_id,
            "component_type": component_type,
            "title": title,
            **fields,
        }
        self.components.append(component)
        self.component_by_entity[eid] = component["id"]
        return component

    @staticmethod
    def source_organism(entity: dict) -> tuple[str | None, str | None]:
        """(NCBITaxon CURIE, scientific name) of the first source row of any kind."""
        for category, taxid_key, name_key in (
            ("entity_src_gen", "pdbx_gene_src_ncbi_taxonomy_id", "pdbx_gene_src_scientific_name"),
            ("entity_src_nat", "pdbx_ncbi_taxonomy_id", "pdbx_organism_scientific"),
            ("pdbx_entity_src_syn", "ncbi_taxonomy_id", "organism_scientific"),
        ):
            for row in entity.get(category) or []:
                taxid = row.get(taxid_key)
                if taxid or row.get(name_key):
                    taxid = str(taxid).split(",")[0].strip() if taxid else None
                    return (f"NCBITaxon:{taxid}" if taxid else None, row.get(name_key))
        for row in entity.get("rcsb_entity_source_organism") or []:
            taxid = row.get("ncbi_taxonomy_id")
            return (f"NCBITaxon:{taxid}" if taxid else None, row.get("scientific_name"))
        return None, None

    @staticmethod
    def residue_range(entity: dict) -> str | None:
        for category in ("entity_src_gen", "entity_src_nat", "pdbx_entity_src_syn"):
            for row in entity.get(category) or []:
                begin, end = row.get("pdbx_beg_seq_num"), row.get("pdbx_end_seq_num")
                if begin is not None and end is not None:
                    return f"{begin}-{end}"
        return None

    def component_description(self, entity: dict, prd_id: str | None) -> str | None:
        parts: list[Any] = []
        if prd_id:
            parts.append(f"BIRD {prd_id}")
            for row in self.rows("pdbx_molecule_features"):
                if row.get("prd_id") == prd_id:
                    parts += [row.get("name"), row.get("class"), row.get("type"), row.get("details")]
        return _text(*parts)

    def add_protein(self, entity: dict, eid: str, chains: list[str]) -> None:
        ids = entity.get("rcsb_polymer_entity_container_identifiers", {})
        poly = entity.get("entity_poly", {})
        polymer = entity.get("rcsb_polymer_entity", {})
        description = polymer.get("pdbx_description")
        organism, organism_name = self.source_organism(entity)

        names = (polymer.get("rcsb_polymer_name_combined") or {}).get("names") or []
        protein_name = names[0] if names else description
        gene_name = None
        genes_full = None
        for row in entity.get("entity_src_gen") or []:
            if row.get("pdbx_gene_src_gene"):
                genes_full = row["pdbx_gene_src_gene"]
                gene_name = genes_full.split(",")[0].strip()
                break
        if gene_name is None:
            for row in entity.get("rcsb_entity_source_organism") or []:
                for gene in row.get("rcsb_gene_name") or []:
                    gene_name = gene.get("value")
                    break
                if gene_name:
                    break

        # UniProt accessions, preferring an isoform where the mapping names one
        isoforms = {}
        coverage = {}
        other_refs: list[dict] = []
        for ref in ids.get("reference_sequence_identifiers") or []:
            name = (ref.get("database_name") or "").lower()
            acc = ref.get("database_accession")
            if name == "uniprot":
                if ref.get("database_isoform"):
                    isoforms[acc] = ref["database_isoform"]
                coverage[acc] = ref.get("reference_sequence_coverage")
            elif acc:
                other_refs.append({"database_name": _database_name(name), "database_id": acc,
                                   "description": ref.get("database_name")})
        accessions = list(ids.get("uniprot_ids") or [])
        for acc in coverage:
            if acc not in accessions:
                accessions.append(acc)

        go_terms: list[str] = []
        cross_refs: list[dict] = list(other_refs)
        for ann in entity.get("rcsb_polymer_entity_annotation") or []:
            ann_type = ann.get("type") or ""
            ann_id = ann.get("annotation_id")
            if ann_type == "GO" and ann_id:
                if ann_id not in go_terms:
                    go_terms.append(ann_id)
            elif ann_id:
                cross_refs.append({
                    "database_name": _database_name(ann_type),
                    "database_id": ann_id,
                    "description": _text(ann_type if _database_name(ann_type) == "other" else None,
                                         ann.get("name"), ann.get("description")),
                })
        for ref in entity.get("rcsb_related_target_references") or []:
            if ref.get("related_target_id"):
                cross_refs.append({
                    "database_name": _database_name(ref.get("related_resource_name")),
                    "database_id": str(ref["related_target_id"]),
                    "description": _text(ref.get("related_resource_name"), "target record"),
                })
        ec_numbers = [e.strip() for e in (polymer.get("pdbx_ec") or "").split(",") if e.strip()]

        protein_ids: list[str] = []
        uniprot_ids: list[str] = []
        for acc in accessions:
            curie = uniprot_curie(isoforms.get(acc) or acc)
            if curie is None:
                self.warnings.append(
                    f"Polymer entity {eid} lists {acc!r}, which is not a UniProt accession; skipped"
                )
                continue
            protein_ids.append(curie)
            uniprot_ids.append(curie)
            if curie not in self.proteins:
                self.proteins[curie] = {
                    "id": curie,
                    "uniprot_id": curie,
                    "protein_name": protein_name,
                    "title": protein_name,
                    "gene_name": gene_name,
                    "organism": organism,
                    "organism_name": organism_name,
                    "ec_numbers": ec_numbers or None,
                    "go_terms": go_terms or None,
                    "cross_references": cross_refs or None,
                    "pdb_entries": [self.base],
                }
        sequence = poly.get("pdbx_seq_one_letter_code_can") or ""
        sequence = sequence.replace("\n", "")
        if not protein_ids:
            # No UniProt record: an antibody, a designed protein, a synthetic peptide. The
            # deposited sequence is then the best description of the protein there is.
            local_id = f"{self.base}/protein/{eid}"
            self.warnings.append(
                f"Polymer entity {eid} has no UniProt mapping; Protein {local_id} is local to the entry"
            )
            self.proteins[local_id] = {
                "id": local_id,
                "protein_name": protein_name,
                "title": description,
                "gene_name": gene_name,
                "organism": organism,
                "organism_name": organism_name,
                "amino_acid_sequence": sequence if _AMINO_ACIDS.match(sequence) else None,
                "sequence_length": len(sequence) if sequence else None,
                "ec_numbers": ec_numbers or None,
                "go_terms": go_terms or None,
                "cross_references": cross_refs or None,
                "pdb_entries": [self.base],
            }
            protein_ids.append(local_id)

        construct_id = f"{self.base}/construct/{eid}"
        src_gen = (entity.get("entity_src_gen") or [{}])[0]
        syn = (entity.get("pdbx_entity_src_syn") or [{}])[0]
        construct: dict[str, Any] = {
            "id": construct_id,
            "construct_id": construct_id,
            "title": description,
            "protein_id": protein_ids[0],
            "uniprot_id": uniprot_ids[0] if uniprot_ids else None,
            "gene_name": genes_full or gene_name,
            "ncbi_taxid": organism.split(":")[1] if organism else None,
            "sequence_length_aa": _qv(poly.get("rcsb_sample_sequence_length"), "residues"),
            "construct_description": _text(
                polymer.get("pdbx_fragment"), polymer.get("details"),
                syn.get("details"), "chemically synthesized" if syn else None,
            ),
            "mutations": polymer.get("pdbx_mutation"),
            "amino_acid_sequence": sequence if _AMINO_ACIDS.match(sequence) else None,
            "vector_name": src_gen.get("plasmid_name"),
            "vector_backbone": src_gen.get("pdbx_host_org_vector"),
        }
        self.extras(construct, "polymer_entity", poly, "entity_poly")
        self.extras(construct, "polymer_entity", polymer, "rcsb_polymer_entity")
        for row in entity.get("rcsb_polymer_entity_name_com") or []:
            self.extras(construct, "polymer_entity", row, "rcsb_polymer_entity_name_com[]")
        for row in entity.get("rcsb_polymer_entity_name_sys") or []:
            self.extras(construct, "polymer_entity", row, "rcsb_polymer_entity_name_sys[]")
        for ref in ids.get("reference_sequence_identifiers") or []:
            self.extras(construct, "polymer_entity", ref,
                        "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers[]",
                        qualifier=ref.get("database_accession"))
        for row in entity.get("entity_src_gen") or []:
            self.extras(construct, "polymer_entity", row, "entity_src_gen[]")
        self.constructs.append(construct)

        modifications = list(dict.fromkeys(
            (poly.get("rcsb_non_std_monomers") or []) + (ids.get("chem_comp_nstd_monomers") or [])
        ))
        role = self.protein_role()
        copies = polymer.get("pdbx_number_of_molecules")
        residue_range = self.residue_range(entity)
        for protein_id in protein_ids:
            acc = protein_id.split(":", 1)[1].split("-")[0] if protein_id.startswith("uniprot:") else None
            cov = coverage.get(acc) if acc else None
            self.sample_protein.append({
                "sample_id": self.sample_id,
                "protein_id": protein_id,
                "role": role,
                "construct_id": construct_id,
                "copy_number": copies,
                "chain_ids": chains or None,
                "residue_range": residue_range,
                "sequence_coverage": cov,
                "modifications": modifications or None,
            })
        prd = poly.get("rcsb_prd_id") or ids.get("prd_id")
        self.entity_component(
            eid, "protein", description,
            protein_id=protein_ids[0], role=role, copy_number=copies,
            description=self.component_description(entity, prd),
        )
        self.add_source_preparations(entity, eid, description)

    def add_nucleic_acid(self, entity: dict, eid: str, chains: list[str]) -> None:
        poly = entity.get("entity_poly", {})
        polymer = entity.get("rcsb_polymer_entity", {})
        ids = entity.get("rcsb_polymer_entity_container_identifiers", {})
        description = polymer.get("pdbx_description")
        name = description
        raw_sequence = poly.get("pdbx_seq_one_letter_code_can")
        sequence = nucleotide_sequence(raw_sequence)
        if raw_sequence and sequence is None:
            self.warnings.append(
                f"Polymer entity {eid} has a sequence with characters outside the "
                "nucleotide alphabet; nucleotide_sequence left empty"
            )
        organism, organism_name = self.source_organism(entity)
        gene_name = None
        for row in entity.get("entity_src_gen") or []:
            if row.get("pdbx_gene_src_gene"):
                gene_name = row["pdbx_gene_src_gene"].split(",")[0].strip()
                break
        acid: dict[str, Any] = {
            "id": f"{self.base}/nucleic_acid/{eid}",
            "nucleic_acid_type": _nucleic_acid_type(entity),
            "nucleic_acid_name": name,
            "title": description or name,
            "gene_name": gene_name,
            "organism": organism,
            "organism_name": organism_name,
            "nucleotide_sequence": sequence,
            "sequence_length": len(sequence) if sequence else poly.get("rcsb_sample_sequence_length"),
            "molecular_weight_theoretical": _qv(polymer.get("formula_weight"), "kDa"),
            "pdb_entries": [self.base],
            "description": _text(polymer.get("pdbx_fragment"), polymer.get("details"),
                                 polymer.get("pdbx_mutation")),
        }
        self.extras(acid, "polymer_entity", poly, "entity_poly")
        self.extras(acid, "polymer_entity", polymer, "rcsb_polymer_entity")
        for category in ("rcsb_polymer_entity_name_com", "rcsb_polymer_entity_name_sys", "entity_src_gen"):
            for row in entity.get(category) or []:
                self.extras(acid, "polymer_entity", row, f"{category}[]")
        self.nucleic_acids.append(acid)
        modifications = list(dict.fromkeys(
            (poly.get("rcsb_non_std_monomers") or []) + (ids.get("chem_comp_nstd_monomers") or [])
        ))
        role = self.nucleic_acid_role()
        copies = polymer.get("pdbx_number_of_molecules")
        self.sample_nucleic_acid.append({
            "sample_id": self.sample_id,
            "nucleic_acid_id": acid["id"],
            "role": role,
            "copy_number": copies,
            "chain_ids": chains or None,
            "residue_range": self.residue_range(entity),
            "modifications": modifications or None,
        })
        prd = poly.get("rcsb_prd_id") or ids.get("prd_id")
        self.entity_component(
            eid, "nucleic_acid", description or name, nucleic_acid_id=acid["id"], role=role, copy_number=copies,
            description=self.component_description(entity, prd),
        )
        self.add_source_preparations(entity, eid, description or name)

    def add_other_polymer(self, entity: dict, eid: str) -> None:
        poly = entity.get("entity_poly", {})
        polymer = entity.get("rcsb_polymer_entity", {})
        name = polymer.get("pdbx_description")
        self.warnings.append(
            f"Polymer entity {eid} is {poly.get('type') or 'of unknown type'}; listed as an 'other' component"
        )
        self.entity_component(
            eid, "other", name, copy_number=polymer.get("pdbx_number_of_molecules"),
            description=_text(poly.get("type"), poly.get("pdbx_seq_one_letter_code"),
                              poly.get("rcsb_prd_id")),
        )

    def add_source_preparations(self, entity: dict, eid: str, name: str | None) -> None:
        """An expression preparation per engineered source row, an isolation per natural one."""
        for row in entity.get("entity_src_gen") or []:
            host = row.get("pdbx_host_org_scientific_name")
            prep: dict[str, Any] = {
                "id": f"{self.base}/preparation/expression-{eid}-{row.get('pdbx_src_id', 1)}",
                "preparation_type": "protein_expression",
                "sample_id": self.sample_id,
                "title": f"Expression of {name or 'entity ' + eid}",
                "description": _text(f"Expressed in {host}" if host else None),
                "expression_system": _expression_system(host),
                "host_strain_or_cell_line": _text(
                    row.get("pdbx_host_org_strain"), row.get("pdbx_host_org_cell_line"),
                    row.get("pdbx_host_org_cell"),
                ),
            }
            taxid = row.get("pdbx_host_org_ncbi_taxonomy_id")
            if taxid:
                self.add_property(prep, "entity_src_gen.pdbx_host_org_ncbi_taxonomy_id",
                                  f"NCBITaxon:{taxid}", "mmCIF:_entity_src_gen.pdbx_host_org_ncbi_taxonomy_id")
            self.extras(prep, "polymer_entity", row, "entity_src_gen[]")
            # The construct already carries the gene-source fields; keep only host fields here.
            prep["additional_properties"] = [
                p for p in prep.get("additional_properties", []) if "host_org" in p["attribute"]["label"]
                or p["attribute"]["label"].endswith("ncbi_taxonomy_id")
            ] or None
            prep["additional_metrics"] = [
                m for m in prep.get("additional_metrics", []) if "host_org" in m["attribute"]["label"]
            ] or None
            self.preparations.append(prep)
        for row in entity.get("entity_src_nat") or []:
            organism = row.get("pdbx_organism_scientific")
            prep = {
                "id": f"{self.base}/preparation/isolation-{eid}-{row.get('pdbx_src_id', 1)}",
                "preparation_type": "protein_purification",
                "sample_id": self.sample_id,
                "title": f"Isolation of {name or 'entity ' + eid}",
                "description": f"Isolated from {organism}" if organism else None,
            }
            self.extras(prep, "polymer_entity", row, "entity_src_nat[]")
            self.preparations.append(prep)

    def small_molecule_from_chemcomp(self, comp_id: str) -> dict:
        comp = self.raw.chemcomps.get(comp_id, {})
        cc = comp.get("chem_comp", {})
        desc = comp.get("rcsb_chem_comp_descriptor", {})
        chebis: list[str] = []
        refs: list[dict] = []
        for rel in comp.get("rcsb_chem_comp_related") or []:
            name, acc = rel.get("resource_name"), rel.get("resource_accession_code")
            if not acc:
                continue
            if (name or "").lower() == "chebi":
                chebis.append(acc if acc.upper().startswith("CHEBI:") else f"CHEBI:{acc}")
            refs.append({"database_name": _database_name(name), "database_id": acc,
                         "description": name if _database_name(name) == "other" else None})
        # RCSB sometimes relates a component to several ChEBI entries (a compound and its
        # conjugate acid, two stereo forms). Only an unambiguous one becomes the identity.
        chebi = chebis[0] if len(set(chebis)) == 1 else None
        if len(set(chebis)) > 1:
            self.warnings.append(
                f"Chemical component {comp_id} maps to several ChEBI entries ({', '.join(chebis)}); "
                f"identified as pdb.ligand:{comp_id}"
            )
        ids = comp.get("rcsb_chem_comp_container_identifiers", {})
        if ids.get("drugbank_id") and not any(r["database_id"] == ids["drugbank_id"] for r in refs):
            refs.append({"database_name": "drugbank", "database_id": ids["drugbank_id"]})
        for code in ids.get("atc_codes") or []:
            refs.append({"database_name": "atc", "database_id": code})
        if ids.get("prd_id"):
            refs.append({"database_name": "pdb", "database_id": ids["prd_id"], "description": "BIRD"})
        formula = (cc.get("formula") or "").replace(" ", "") or None
        molecule: dict[str, Any] = {
            "id": chebi or f"pdb.ligand:{comp_id}",
            "small_molecule_name": cc.get("name"),
            "title": cc.get("name"),
            "chebi_id": chebi,
            "pdb_ligand_id": f"pdb.ligand:{comp_id}",
            "chemical_class": self.chemical_class(comp),
            "molecular_formula": formula,
            "smiles": desc.get("SMILES_stereo") or desc.get("SMILES"),
            "inchi": desc.get("InChI"),
            "inchikey": desc.get("InChIKey"),
            "molecular_weight_theoretical": _qv(cc.get("formula_weight"), "Da"),
            "cross_references": refs or None,
        }
        self.extras(molecule, "chemcomp", cc, "chem_comp")
        self.extras(molecule, "chemcomp", ids, "rcsb_chem_comp_container_identifiers")
        for row in comp.get("pdbx_chem_comp_identifier") or []:
            self.extras(molecule, "chemcomp", row, "pdbx_chem_comp_identifier[]",
                        qualifier=_text(row.get("type"), row.get("program"), sep=" "))
        for row in comp.get("pdbx_chem_comp_feature") or []:
            self.extras(molecule, "chemcomp", row, "pdbx_chem_comp_feature[]",
                        qualifier=_text(row.get("type"), row.get("source"), sep=" "))
        return molecule

    @staticmethod
    def chemical_class(comp: dict) -> str | None:
        cc = comp.get("chem_comp", {})
        comp_type = (cc.get("type") or "").lower()
        info = comp.get("rcsb_chem_comp_info", {})
        if info.get("atom_count_heavy") == 1 and cc.get("pdbx_formal_charge"):
            return "ion"
        if "saccharide" in comp_type:
            return "carbohydrate"
        if "peptide" in comp_type:
            return "amino_acid"
        if "dna" in comp_type or "rna" in comp_type:
            return "nucleotide"
        return None

    def add_nonpolymer(self, entity: dict) -> None:
        nonpoly = entity.get("pdbx_entity_nonpoly", {})
        record = entity.get("rcsb_nonpolymer_entity", {})
        ids = entity.get("rcsb_nonpolymer_entity_container_identifiers", {})
        eid = str(nonpoly.get("entity_id") or ids.get("entity_id"))
        comp_id = nonpoly.get("comp_id") or ids.get("nonpolymer_comp_id")
        if not comp_id:
            return
        molecule = self.small_molecule_from_chemcomp(comp_id)
        for name, acc in zip(ids.get("reference_chemical_identifiers_resource_name") or [],
                             ids.get("reference_chemical_identifiers_resource_accession") or []):
            refs = molecule.setdefault("cross_references", []) or []
            if not any(r["database_id"] == acc for r in refs):
                refs.append({"database_name": _database_name(name), "database_id": acc,
                             "description": name if _database_name(name) == "other" else None})
            molecule["cross_references"] = refs
        for row in entity.get("rcsb_nonpolymer_entity_name_com") or []:
            self.extras(molecule, "nonpolymer_entity", row, "rcsb_nonpolymer_entity_name_com[]")
        self.small_molecules.setdefault(molecule["id"], molecule)

        annotations = entity.get("rcsb_nonpolymer_entity_annotation") or []
        subject_of_investigation = any(a.get("type") == "SUBJECT_OF_INVESTIGATION" for a in annotations)
        prd = nonpoly.get("rcsb_prd_id") or ids.get("prd_id")
        component = self.entity_component(
            eid, "small_molecule", record.get("pdbx_description") or nonpoly.get("name"),
            small_molecule_id=molecule["id"],
            role="ligand" if subject_of_investigation else None,
            copy_number=record.get("pdbx_number_of_molecules"),
            description=_text(
                *(_text(a.get("type"), a.get("description"), sep=": ") for a in annotations),
                record.get("details"), self.component_description(entity, prd),
            ),
        )
        bound = set(self.entry.get("rcsb_entry_info", {}).get("nonpolymer_bound_components") or [])
        if comp_id in bound:
            interaction_type = "is_coordinated_by" if molecule.get("chemical_class") == "ion" else "covalently_linked_to"
        else:
            interaction_type = "binds"
        self.chain_interactions(component, ids.get("auth_asym_ids") or [], interaction_type)
        self.add_affinities(component, comp_id)

    def add_branched(self, entity: dict) -> None:
        record = entity.get("rcsb_branched_entity", {})
        ids = entity.get("rcsb_branched_entity_container_identifiers", {})
        branch = entity.get("pdbx_entity_branch", {})
        eid = str(ids.get("entity_id"))
        refs = []
        glytoucan = None
        for ref in ids.get("reference_identifiers") or []:
            name, acc = ref.get("resource_name"), ref.get("resource_accession")
            if not acc:
                continue
            if (name or "").lower() == "glytoucan" and glytoucan is None:
                glytoucan = acc
            refs.append({"database_name": _database_name(name), "database_id": acc,
                         "description": name if _database_name(name) == "other" else None})
        name = record.get("pdbx_description")
        molecule: dict[str, Any] = {
            "id": f"glytoucan:{glytoucan}" if glytoucan else f"{self.base}/glycan/{eid}",
            "small_molecule_name": name,
            "title": name,
            "chemical_class": "carbohydrate" if "saccharide" in (branch.get("type") or "").lower() else None,
            "molecular_weight_theoretical": _qv(record.get("formula_weight"), "kDa"),
            "cross_references": refs or None,
        }
        for row in entity.get("pdbx_entity_branch_descriptor") or []:
            self.extras(molecule, "branched_entity", row, "pdbx_entity_branch_descriptor[]",
                        qualifier=_text(row.get("type"), row.get("program"), sep=" "))
        for category in ("rcsb_branched_entity_name_com", "rcsb_branched_entity_name_sys"):
            for row in _rows(entity, category):
                self.extras(molecule, "branched_entity", row, f"{category}[]" if isinstance(entity.get(category), list) else category)
        self.small_molecules.setdefault(molecule["id"], molecule)
        component = self.entity_component(
            eid, "small_molecule", name, small_molecule_id=molecule["id"],
            copy_number=record.get("pdbx_number_of_molecules"),
            description=_text(branch.get("type"), record.get("details"), ids.get("prd_id")),
        )
        self.chain_interactions(component, ids.get("auth_asym_ids") or [], "covalently_linked_to")

    def chain_interactions(self, component: dict, chains: list[str], interaction_type: str) -> None:
        """One interaction from a ligand or glycan to each polymer whose chain it is assigned to."""
        targets: list[str] = []
        for chain in chains:
            eid = self.entity_by_chain.get(chain)
            if eid and eid not in targets:
                targets.append(eid)
        for eid in targets:
            obj = self.component_by_entity.get(eid)
            if not obj:
                continue
            on = ", ".join(c for c in chains if self.entity_by_chain.get(c) == eid)
            self.interactions.append({
                "sample_id": self.sample_id,
                "subject_id": component["id"],
                "object_id": obj,
                "interaction_type": interaction_type,
                "interaction_status": "observed",
                "evidence": ["experimental"],
                "description": f"Modelled on chain {on} in the deposited structure",
            })

    def add_affinities(self, component: dict, comp_id: str) -> None:
        rows = [r for r in self.rows("rcsb_binding_affinity") if r.get("comp_id") == comp_id]
        if not rows:
            return
        structural = [i for i in self.interactions if i["subject_id"] == component["id"]]
        objects = [i["object_id"] for i in structural] or list(self.component_by_entity.values())[:1]
        for n, row in enumerate(rows):
            note = _text(
                f"{row.get('type')} {row.get('symbol') or '='} {row.get('value')} {row.get('unit')}",
                f"from {row.get('provenance_code')}" if row.get("provenance_code") else None,
                row.get("link"),
                f"reference sequence identity {row.get('reference_sequence_identity')}%"
                if row.get("reference_sequence_identity") is not None else None,
            )
            affinity: dict[str, Any] = {
                "affinity": _qv(row.get("value"), row.get("unit") or "dimensionless"),
                "affinity_type": _AFFINITY_TYPES.get(row.get("type") or ""),
            }
            if n == 0 and structural:
                structural[0].update(affinity)
                self.append_description(structural[0], note)
            elif objects:
                self.interactions.append({
                    "sample_id": self.sample_id,
                    "subject_id": component["id"],
                    "object_id": objects[0],
                    "interaction_type": "binds",
                    "interaction_status": "observed",
                    "evidence": ["experimental"],
                    "description": note,
                    **affinity,
                })

    # ---- samples -----------------------------------------------------------------------

    def build_samples(self) -> None:
        main: dict[str, Any] = {
            "id": self.sample_id,
            "sample_code": f"PDB-{self.entry_id}",
            "sample_type": self.main_sample_type(),
            "title": None,
            "molecular_weight": _qv(self.entry.get("rcsb_entry_info", {}).get("molecular_weight"), "kDa"),
        }
        assemblies = self.rows("em_entity_assembly")
        top = [a for a in assemblies if str(a.get("parent_id", "0")) in ("0", "")]
        if top:
            self.describe_em_assembly(main, top[0])
        main["title"] = (
            main.get("title")
            or self.entry.get("struct", {}).get("pdbx_descriptor")
            or self.entry.get("struct", {}).get("title")
        )
        for row in self.rows("em_specimen"):
            if row.get("concentration") is not None:
                main["concentration"] = _qv(row["concentration"], "mg/mL")
        self.describe_assembly(main)
        for n, row in enumerate(self.rows("pdbx_soln_scatter")):
            if n == 0:
                buffer = {"ph": row.get("sample_pH"),
                          "components": [row["buffer_name"]] if row.get("buffer_name") else None}
                if any(buffer.values()):
                    main["buffer_composition"] = buffer
            self.extras(main, "entry", row, "pdbx_soln_scatter[]", qualifier=str(row.get("id")))
        self.samples.append(main)

        # EM sub-assemblies become child samples, each listing its own components
        sample_by_assembly = {str(a.get("id")): self.sample_id for a in top[:1]}
        for assembly in assemblies:
            aid = str(assembly.get("id"))
            if aid in sample_by_assembly:
                continue
            child: dict[str, Any] = {
                "id": f"{self.base}/sample/assembly-{aid}",
                "sample_code": f"PDB-{self.entry_id}-A{aid}",
                "sample_type": _EM_SAMPLE_TYPES.get((assembly.get("type") or "").upper(), "complex"),
            }
            parent = str(assembly.get("parent_id", "0"))
            if parent not in ("0", ""):
                child["parent_sample_id"] = sample_by_assembly.get(parent, self.sample_id)
            else:
                child["parent_sample_id"] = self.sample_id
            self.describe_em_assembly(child, assembly)
            sample_by_assembly[aid] = child["id"]
            self.samples.append(child)
            for eid in assembly.get("entity_id_list") or []:
                parent_component = next(
                    (c for c in self.components if c["id"] == self.component_by_entity.get(str(eid))), None
                )
                if parent_component is None:
                    continue
                component = {k: v for k, v in parent_component.items() if k not in ("id", "sample_id")}
                component["id"] = f"{child['id']}/component/{eid}"
                component["sample_id"] = child["id"]
                self.components.append(component)

        # NMR solutions are child samples of the specimen
        for row in self.rows("pdbx_nmr_sample_details"):
            sid = row.get("solution_id")
            child = {
                "id": f"{self.base}/sample/nmr-{sid}",
                "sample_code": f"PDB-{self.entry_id}-NMR{sid}",
                "sample_type": main["sample_type"],
                "parent_sample_id": self.sample_id,
                "title": row.get("label") or f"NMR sample {sid}",
                "description": _text(row.get("contents"), row.get("details")),
                "buffer_composition": {"components": [row["solvent_system"]]} if row.get("solvent_system") else None,
            }
            self.extras(child, "entry", row, "pdbx_nmr_sample_details[]")
            self.samples.append(child)

    def describe_em_assembly(self, sample: dict, assembly: dict) -> None:
        sample["title"] = assembly.get("name") or sample.get("title")
        sample_type = _EM_SAMPLE_TYPES.get((assembly.get("type") or "").upper())
        if sample_type and sample_type != "complex":
            sample["sample_type"] = sample_type
        if assembly.get("oligomeric_details"):
            sample["oligomeric_state"] = assembly["oligomeric_details"]
        sample["description"] = _text(sample.get("description"), assembly.get("synonym"), assembly.get("details"))
        self.extras(sample, "entry", assembly, "em_entity_assembly[]")

    def describe_assembly(self, sample: dict) -> None:
        """The first assembly: oligomeric state, symmetry and the evidence for it."""
        if not self.raw.assemblies:
            return
        assembly = self.raw.assemblies[0]
        struct = assembly.get("pdbx_struct_assembly", {})
        symmetry = [s for s in assembly.get("rcsb_struct_symmetry") or [] if s.get("kind") == "Global Symmetry"]
        states = [s.get("oligomeric_state") for s in symmetry if s.get("oligomeric_state")]
        sample["oligomeric_state"] = _text(
            sample.get("oligomeric_state"), *states, struct.get("oligomeric_details"),
        )
        self.extras(sample, "assembly", struct, "pdbx_struct_assembly")
        for row in assembly.get("pdbx_struct_assembly_auth_evidence") or []:
            self.extras(sample, "assembly", row, "pdbx_struct_assembly_auth_evidence[]")
        for row in assembly.get("pdbx_struct_assembly_prop") or []:
            self.extras(sample, "assembly", row, "pdbx_struct_assembly_prop[]", qualifier=row.get("type"))
        for row in assembly.get("rcsb_struct_symmetry") or []:
            kind = row.get("kind") or "symmetry"
            self.extras(sample, "assembly", row, "rcsb_struct_symmetry[]", qualifier=kind)
            if kind != "Global Symmetry" and row.get("oligomeric_state"):
                self.add_property(sample, f"rcsb_struct_symmetry[{kind}].oligomeric_state",
                                  row["oligomeric_state"], "rcsb:rcsb_struct_symmetry.oligomeric_state")

    def main_sample_type(self) -> str:
        polymers = self.raw.polymer_entities
        proteins = [e for e in polymers if _is_protein(e)]
        acids = [e for e in polymers if _nucleic_acid_type(e) is not None]
        if len(polymers) == 1 and len(proteins) == 1:
            membrane = any(
                (a.get("type") or "").lower() in ("mpstruc", "opm", "pdbtm", "memprotmd")
                for a in proteins[0].get("rcsb_polymer_entity_annotation") or []
            )
            return "membrane_protein" if membrane else "protein"
        if len(polymers) == 1 and len(acids) == 1:
            return "nucleic_acid"
        return "complex"

    # ---- interactions between polymers ----------------------------------------------

    def build_interactions(self) -> None:
        pairs: dict[tuple[str, str], dict] = {}
        for interface in self.raw.interfaces:
            partners = interface.get("rcsb_interface_partner") or []
            if len(partners) != 2:
                continue
            eids = [str(p.get("interface_partner_identifier", {}).get("entity_id")) for p in partners]
            if not all(e in self.component_by_entity for e in eids):
                continue
            sites = [self.buried_residues(p, eid) for p, eid in zip(partners, eids)]
            # The smaller partner binds the larger one
            order = sorted(range(2), key=lambda i: self.entity_weight.get(eids[i], 0))
            subject, obj = eids[order[0]], eids[order[1]]
            key = (subject, obj)
            row = pairs.setdefault(key, {
                "sample_id": self.sample_id,
                "subject_id": self.component_by_entity[subject],
                "object_id": self.component_by_entity[obj],
                "interaction_type": "binds",
                "interaction_status": "observed",
                "evidence": ["experimental"],
                "_subject_residues": set(),
                "_object_residues": set(),
                "_notes": [],
            })
            row["_subject_residues"] |= sites[order[0]]
            row["_object_residues"] |= sites[order[1]]
            info = interface.get("rcsb_interface_info", {})
            iid = interface.get("rcsb_interface_container_identifiers", {}).get("interface_id")
            area = info.get("interface_area")
            row["_notes"].append(
                f"interface {iid}: {round(area) if area is not None else '?'} square angstroms buried, "
                f"{info.get('num_interface_residues')} interface residues "
                f"({info.get('num_core_interface_residues')} core)"
            )
        for (subject, obj), row in pairs.items():
            row["subject_site"] = self.site(subject, row.pop("_subject_residues")) or None
            row["object_site"] = self.site(obj, row.pop("_object_residues")) or None
            notes = row.pop("_notes")
            homomeric = "Homomeric contact between copies of one entity; " if subject == obj else ""
            row["description"] = f"{homomeric}Contact in the first assembly: " + "; ".join(notes)
            self.interactions.append(row)

    @staticmethod
    def buried_residues(partner: dict, eid: str) -> set[int]:
        """Residue numbers whose solvent-accessible area drops when the partner binds."""
        areas: dict[str, dict[int, float]] = {}
        for feature in partner.get("interface_partner_feature") or []:
            per_residue = areas.setdefault(feature.get("type"), {})
            for pos in feature.get("feature_positions") or []:
                begin = pos.get("beg_seq_id")
                for offset, value in enumerate(pos.get("values") or []):
                    if begin is not None and value is not None:
                        per_residue[begin + offset] = value
        bound = areas.get("ASA_BOUND", {})
        unbound = areas.get("ASA_UNBOUND", {})
        return {n for n, value in unbound.items() if value - bound.get(n, value) > 1.0}

    def site(self, eid: str, residues: set[int]) -> str:
        sequence = self.entity_sequence.get(eid) or ""
        if not residues:
            return ""
        if len(residues) > 40 or not sequence:
            return _residue_ranges(list(residues))
        return ",".join(
            f"{sequence[n - 1] if 0 < n <= len(sequence) else 'X'}{n}" for n in sorted(residues)
        )

    # ---- instruments and experiment runs --------------------------------------------

    def quality_metrics(self, refine: dict | None, technique: str) -> dict:
        info = self.entry.get("rcsb_entry_info", {})
        resolution = (refine or {}).get("ls_d_res_high")
        if resolution is None and info.get("resolution_combined"):
            resolution = info["resolution_combined"][0]
        geometry = (self.rows("pdbx_vrpt_summary_geometry") or [{}])[0]
        metrics: dict[str, Any] = {
            "resolution": _qv(resolution, "Angstroms"),
            "clashscore": _qv(geometry.get("clashscore"), "dimensionless"),
            "ramachandran_outliers_percent": _qv(geometry.get("percent_ramachandran_outliers"), "percent"),
        }
        if refine:
            metrics["r_work"] = _qv(refine.get("ls_R_factor_R_work"), "dimensionless")
            metrics["r_free"] = _qv(refine.get("ls_R_factor_R_free"), "dimensionless")
            metrics["average_b_factor_a2"] = _qv(refine.get("B_iso_mean"), "Angstroms^2")
        if technique in ("xray_crystallography", "neutron_crystallography", "microed", "fiber_diffraction",
                         "powder_diffraction"):
            cell = self.entry.get("cell", {})
            for axis in ("a", "b", "c"):
                metrics[f"unit_cell_{axis}"] = _qv(cell.get(f"length_{axis}"), "Angstroms")
            for angle in ("alpha", "beta", "gamma"):
                metrics[f"unit_cell_{angle}"] = _qv(cell.get(f"angle_{angle}"), "degrees")
            metrics["space_group"] = self.entry.get("symmetry", {}).get("space_group_name_H_M")
        return {k: v for k, v in metrics.items() if v is not None}

    def refine_for(self, method: str) -> dict | None:
        for row in self.rows("refine"):
            if (row.get("pdbx_refine_id") or "").upper() == method:
                return row
        rows = self.rows("refine")
        return rows[0] if len(rows) == 1 else None

    def new_run(self, suffix: str, technique: str, method: str, **fields: Any) -> dict:
        run = {
            "id": f"{self.base}/experiment/{suffix}",
            "experiment_code": f"PDB-{self.entry_id}-{suffix.upper()}",
            "technique": technique,
            "_method": method,
            **fields,
        }
        for row in self.rows("exptl"):
            if (row.get("method") or "").upper() == method:
                self.extras(run, "entry", row, "exptl[]")
                self.append_description(run, row.get("method_details"), row.get("details"))
        self.runs.append(run)
        return run

    def link_run(self, run: dict, instrument_id: str | None, sample_id: str | None = None,
                 preparation_id: str | None = None) -> None:
        self.experiment_samples.append({
            "experiment_id": run["id"],
            "sample_id": sample_id or self.sample_id,
            "preparation_id": preparation_id,
        })
        if instrument_id:
            self.experiment_instruments.append({"experiment_id": run["id"], "instrument_id": instrument_id})

    def build_runs(self) -> None:
        done_methods: set[str] = set()
        for method in self.methods:
            if method in done_methods:
                continue
            done_methods.add(method)
            technique = _TECHNIQUES.get(method)
            if technique is None:
                self.warnings.append(f"Unknown experimental method {method!r}; recorded as integrative_modeling")
                technique = "integrative_modeling"
            if method == "ELECTRON MICROSCOPY" or (method == "ELECTRON CRYSTALLOGRAPHY" and self.rows("em_imaging")):
                self.em_runs(method, technique)
            elif method in ("X-RAY DIFFRACTION", "NEUTRON DIFFRACTION", "FIBER DIFFRACTION",
                            "POWDER DIFFRACTION", "ELECTRON CRYSTALLOGRAPHY"):
                self.diffraction_runs(method, technique)
            elif method in ("SOLUTION NMR", "SOLID-STATE NMR"):
                self.nmr_runs(method, technique)
            elif method == "SOLUTION SCATTERING":
                self.scattering_runs(method)
            else:
                run = self.new_run(_slug(method), technique, method,
                                   quality_metrics=self.quality_metrics(self.refine_for(method), technique))
                self.link_run(run, None)
        if not self.runs:
            self.warnings.append("No experimental method found")
        # A lone run keeps the short id
        if len(self.runs) == 1:
            old = self.runs[0]["id"]
            self.runs[0]["id"] = f"{self.base}/experiment"
            self.runs[0]["experiment_code"] = f"PDB-{self.entry_id}-EXP"
            for assoc in self.experiment_samples + self.experiment_instruments:
                if assoc["experiment_id"] == old:
                    assoc["experiment_id"] = self.runs[0]["id"]

    def diffraction_runs(self, method: str, technique: str) -> None:
        scattering = {
            "X-RAY DIFFRACTION": "x-ray", "FIBER DIFFRACTION": "x-ray", "POWDER DIFFRACTION": "x-ray",
            "NEUTRON DIFFRACTION": "neutron", "ELECTRON CRYSTALLOGRAPHY": "electron",
        }[method]
        radiation = {str(r.get("diffrn_id")): r for r in self.rows("diffrn_radiation")}
        diffrns = [
            d for d in self.rows("diffrn")
            if (radiation.get(str(d.get("id")), {}).get("pdbx_scattering_type") or scattering).lower() == scattering
        ]
        if not diffrns and len(self.methods) == 1:
            diffrns = self.rows("diffrn")
        refine = self.refine_for(method)
        if not diffrns:
            run = self.new_run(_slug(method), technique, method,
                               quality_metrics=self.quality_metrics(refine, technique))
            self.link_run(run, None, preparation_id=self.crystal_preparation(None))
            return
        for diffrn in diffrns:
            did = str(diffrn.get("id"))
            run = self.new_run(f"diffrn-{did}", technique, method, quality_metrics=self.quality_metrics(refine, technique))
            run["_diffrn_id"] = did
            self.fill_diffraction_run(run, diffrn, did)
            instrument_id = self.diffraction_instrument(did, technique)
            self.link_run(run, instrument_id, preparation_id=self.crystal_preparation(diffrn))

    def fill_diffraction_run(self, run: dict, diffrn: dict, did: str) -> None:
        conditions: dict[str, Any] = {
            "temperature": _qv(diffrn.get("ambient_temp"), "K"),
            "pressure": _qv(diffrn.get("ambient_pressure"), "kPa"),
            "description": diffrn.get("ambient_temp_details"),
        }
        if any(conditions.values()):
            run["experimental_conditions"] = {k: v for k, v in conditions.items() if v is not None}
        self.append_description(run, diffrn.get("details"))
        self.extras(run, "entry", diffrn, "diffrn[]")
        for row in self.rows("diffrn_detector"):
            if str(row.get("diffrn_id")) == did:
                run["experiment_date"] = _date(row.get("pdbx_collection_date")) or run.get("experiment_date")
                self.extras(run, "entry", row, "diffrn_detector[]")
        for row in self.rows("diffrn_radiation"):
            if str(row.get("diffrn_id")) == did:
                if row.get("pdbx_diffrn_protocol"):
                    run["data_collection_strategy"] = {"strategy_notes": row["pdbx_diffrn_protocol"]}
                self.extras(run, "entry", row, "diffrn_radiation[]")
        for row in self.rows("diffrn_source"):
            if str(row.get("diffrn_id")) == did:
                wavelength = row.get("pdbx_wavelength") or row.get("pdbx_wavelength_list")
                run["wavelength"] = _qv(wavelength, "Angstroms")
                if row.get("pdbx_wavelength_list") and "," in str(row["pdbx_wavelength_list"]):
                    self.add_property(run, "diffrn_source.pdbx_wavelength_list", row["pdbx_wavelength_list"],
                                      "mmCIF:_diffrn_source.pdbx_wavelength_list")
        crystal_id = str(diffrn.get("crystal_id")) if diffrn.get("crystal_id") is not None else None
        for row in self.rows("exptl_crystal"):
            if crystal_id is None or str(row.get("id")) == crystal_id:
                self.extras(run, "entry", row, "exptl_crystal[]")
        cell = self.entry.get("cell")
        if cell:
            self.extras(run, "entry", cell, "cell")
        for category in (
            "pdbx_serial_crystallography_measurement",
            "pdbx_serial_crystallography_sample_delivery",
            "pdbx_serial_crystallography_sample_delivery_fixed_target",
            "pdbx_serial_crystallography_sample_delivery_injection",
        ):
            for row in self.rows(category):
                if str(row.get("diffrn_id")) == did:
                    self.extras(run, "entry", row, f"{category}[]")

    def diffraction_instrument(self, did: str, technique: str) -> str | None:
        source = next((r for r in self.rows("diffrn_source") if str(r.get("diffrn_id")) == did), None)
        detector = next((r for r in self.rows("diffrn_detector") if str(r.get("diffrn_id")) == did), {})
        radiation = next((r for r in self.rows("diffrn_radiation") if str(r.get("diffrn_id")) == did), {})
        if source is None and not detector:
            return None
        source = source or {}
        site = source.get("pdbx_synchrotron_site")
        beamline = source.get("pdbx_synchrotron_beamline")
        if site and beamline:
            code = f"{site}-{beamline}"
            instrument_id = f"pdb:instrument/{code.replace(' ', '_').replace('/', '_')}"
        else:
            code = f"PDB-{self.entry_id}-D{did}"
            instrument_id = f"{self.base}/instrument/diffrn-{did}"
        if any(i.id == instrument_id for i in self.instruments):
            return instrument_id
        description = _text(
            f"Detector: {detector.get('detector')}" if detector.get("detector") else None,
            detector.get("details"), source.get("details"),
            f"Monochromator: {radiation.get('monochromator')}" if radiation.get("monochromator") else None,
        )
        common = {
            "id": instrument_id,
            "title": _text(site and beamline and f"{site} {beamline}", source.get("source"),
                           sep=" / ") or f"Instrument for {self.entry_id}",
            "instrument_code": code.replace(" ", "-"),
            "description": _text(description, source.get("source")),
            "facility_name": _FACILITIES.get((site or "").upper()),
            "beamline_id": beamline,
            "model": source.get("type"),
            "manufacturer": _manufacturer(source.get("type")),
        }
        if technique == "xray_crystallography" or technique in ("fiber_diffraction", "powder_diffraction"):
            instrument: Instrument = XRayInstrument(
                **common,
                source_type=_XRAY_SOURCES.get((source.get("source") or "").upper()),
                detector_model=detector.get("type"),
                detector_manufacturer=_manufacturer(detector.get("type")),
                detector_technology=_XRAY_DETECTORS.get((detector.get("detector") or "").upper()),
                monochromator_type=radiation.get("monochromator"),
            )
        else:
            common["description"] = _text(common["description"], f"Detector model: {detector.get('type')}"
                                           if detector.get("type") else None)
            instrument = Instrument(**common)
        self.instruments.append(instrument)
        return instrument_id

    def crystal_preparation(self, diffrn: dict | None) -> str | None:
        """The crystallization preparation for the crystal a diffraction run used."""
        crystal_id = str(diffrn.get("crystal_id")) if diffrn and diffrn.get("crystal_id") is not None else None
        crystals = self.rows("exptl_crystal")
        grows = self.rows("exptl_crystal_grow")
        if not crystals and not grows:
            return None
        crystal = next((c for c in crystals if crystal_id is None or str(c.get("id")) == crystal_id), {})
        cid = str(crystal.get("id") or crystal_id or "1")
        prep_id = f"{self.base}/preparation/crystal-{cid}"
        if any(p["id"] == prep_id for p in self.preparations):
            return prep_id
        grow = next((g for g in grows if str(g.get("crystal_id")) == cid), grows[0] if len(grows) == 1 else {})
        xray: dict[str, Any] = {
            "description": grow.get("method"),
            "crystallization_method": self.crystallization_method(grow.get("method")),
            "crystallization_ph": grow.get("pH"),
            "temperature_c": _qv(grow.get("temp"), "K"),
            "crystallization_conditions": {
                "crystallization_conditions": grow.get("pdbx_details"),
                "crystal_id": cid,
            } if grow.get("pdbx_details") else None,
            "crystal_notes": _text(grow.get("details"), crystal.get("colour"), crystal.get("description"),
                                   crystal.get("preparation")),
            "matthews_coefficient": _qv(crystal.get("density_Matthews"), "Angstroms^3/Da"),
            "solvent_content_percent": crystal.get("density_percent_sol"),
        }
        supports = [d.get("crystal_support") for d in self.rows("diffrn")
                    if d.get("crystal_support") and (crystal_id is None or str(d.get("crystal_id")) == cid)]
        if supports:
            xray["mounting_method"] = supports[0]
        prep: dict[str, Any] = {
            "id": prep_id,
            "preparation_type": "xray_crystallography",
            "sample_id": self.sample_id,
            "title": f"Crystal {cid}",
            "xray_preparation": {k: v for k, v in xray.items() if v is not None},
        }
        self.extras(prep, "entry", grow, "exptl_crystal_grow[]")
        self.extras(prep, "entry", crystal, "exptl_crystal[]")
        self.preparations.append(prep)
        return prep_id

    @staticmethod
    def crystallization_method(method: str | None) -> str | None:
        text = (method or "").lower()
        if "hanging" in text:
            return "vapor_diffusion_hanging"
        if "sitting" in text:
            return "vapor_diffusion_sitting"
        if "lipidic" in text or "lcp" in text or "cubic phase" in text:
            return "lcp"
        if "microbatch" in text:
            return "microbatch"
        if "batch" in text:
            return "batch"
        if "dialysis" in text:
            return "dialysis"
        if "free interface" in text or "counter" in text:
            return "free_interface_diffusion"
        return None

    def em_runs(self, method: str, technique: str) -> None:
        experiment = self.entry.get("em_experiment", {})
        reconstruction = (experiment.get("reconstruction_method") or "").upper()
        if reconstruction in ("SUBTOMOGRAM AVERAGING", "TOMOGRAPHY"):
            technique = "cryo_et"
        if reconstruction in ("CRYSTALLOGRAPHY", "ELECTRON CRYSTALLOGRAPHY") or method == "ELECTRON CRYSTALLOGRAPHY":
            technique = "microed"
        refine = self.refine_for(method)
        prep_id = self.em_preparation()
        imagings = self.rows("em_imaging") or [{}]
        for imaging in imagings:
            iid = str(imaging.get("id", "1"))
            run = self.new_run(f"em-{iid}", technique, method,
                               experimental_method=_EM_METHODS.get(reconstruction),
                               quality_metrics=self.quality_metrics(refine, technique))
            self.extras(run, "entry", experiment, "em_experiment")
            self.fill_em_run(run, imaging, iid)
            instrument_id = self.em_instrument(imaging, iid)
            self.link_run(run, instrument_id, preparation_id=prep_id)
        # MicroED entries also carry diffraction-style rows; they describe the same collection
        if technique == "microed":
            run = self.runs[-1]
            for diffrn in self.rows("diffrn"):
                did = str(diffrn.get("id"))
                self.fill_diffraction_run(run, diffrn, did)
                crystal = self.crystal_preparation(diffrn)
                if crystal:
                    self.link_run(run, None, preparation_id=crystal)
                source = next((r for r in self.rows("diffrn_source") if str(r.get("diffrn_id")) == did), {})
                detector = next((r for r in self.rows("diffrn_detector") if str(r.get("diffrn_id")) == did), {})
                self.append_description(
                    run,
                    _text(source.get("source"), source.get("type"), source.get("details"), sep=", "),
                    _text(detector.get("detector"), detector.get("type"), detector.get("details"), sep=", "),
                )

    def fill_em_run(self, run: dict, imaging: dict, iid: str) -> None:
        run["experiment_date"] = _date(imaging.get("date"))
        run["magnification"] = _qv(imaging.get("nominal_magnification"), "x")
        run["defocus_range_min"] = _qv(imaging.get("nominal_defocus_min"), "nanometers")
        run["defocus_range_max"] = _qv(imaging.get("nominal_defocus_max"), "nanometers")
        run["tilt_angle_min"] = _qv(imaging.get("tilt_angle_min"), "degrees")
        run["tilt_angle_max"] = _qv(imaging.get("tilt_angle_max"), "degrees")
        run["detector_distance"] = _qv(imaging.get("detector_distance"), "mm")
        temperature = _qv(imaging.get("temperature"), "K") or {}
        if imaging.get("recording_temperature_minimum") is not None:
            temperature.setdefault("unit", "K")
            temperature["minimum_numeric_value"] = imaging["recording_temperature_minimum"]
        if imaging.get("recording_temperature_maximum") is not None:
            temperature.setdefault("unit", "K")
            temperature["maximum_numeric_value"] = imaging["recording_temperature_maximum"]
        if temperature:
            run["experimental_conditions"] = {"temperature": temperature}
        self.append_description(run, imaging.get("details"))
        self.extras(run, "entry", imaging, "em_imaging[]")
        for row in self.rows("em_image_recording"):
            if str(row.get("imaging_id", iid)) != iid:
                continue
            run["total_exposure_time"] = _qv(row.get("average_exposure_time"), "s")
            run["total_dose"] = _qv(row.get("avg_electron_dose_per_image"), "e-/Angstrom^2")
            images = row.get("num_real_images") or row.get("num_diffraction_images")
            run["number_of_images"] = _qv(images, "images")
            if row.get("num_real_images") and row.get("num_diffraction_images"):
                self.add_property(run, "em_image_recording.num_diffraction_images",
                                  row["num_diffraction_images"], "mmCIF:_em_image_recording.num_diffraction_images")
            self.append_description(run, row.get("details"))
            self.extras(run, "entry", row, "em_image_recording[]")
        for row in self.rows("em_diffraction"):
            if str(row.get("imaging_id", iid)) == iid:
                run["camera_length"] = _qv(row.get("camera_length"), "mm")
                self.extras(run, "entry", row, "em_diffraction[]")
        for category in ("em_2d_crystal_entity", "em_3d_crystal_entity"):
            for row in self.rows(category):
                qm = run.setdefault("quality_metrics", {})
                for axis in ("a", "b", "c"):
                    if row.get(f"length_{axis}") is not None:
                        qm[f"unit_cell_{axis}"] = _qv(row[f"length_{axis}"], "Angstroms")
                for angle in ("alpha", "beta", "gamma"):
                    if row.get(f"angle_{angle}") is not None:
                        qm[f"unit_cell_{angle}"] = _qv(row[f"angle_{angle}"], "degrees")
                group = row.get("space_group_name_H_M") or row.get("space_group_name")
                if group:
                    qm["space_group"] = group
                self.extras(run, "entry", row, f"{category}[]")
        for row in self.rows("em_software"):
            if (row.get("category") or "").upper() == "IMAGE ACQUISITION" and row.get("name"):
                run["acquisition_software"] = _text(run.get("acquisition_software"), row["name"], sep=", ")
                if row.get("version"):
                    run["acquisition_software_version"] = str(row["version"])

    def em_instrument(self, imaging: dict, iid: str) -> str | None:
        if not imaging:
            return None
        recording = next(
            (r for r in self.rows("em_image_recording") if str(r.get("imaging_id", iid)) == iid), {}
        )
        detector = recording.get("film_or_detector_model")
        model = imaging.get("microscope_model")
        instrument_id = f"{self.base}/instrument/em-{iid}"
        detector_upper = (detector or "").upper()
        instrument = CryoEMInstrument(
            id=instrument_id,
            title=model or f"Microscope for {self.entry_id}",
            instrument_code=f"PDB-{self.entry_id}-EM{iid}",
            model=model,
            manufacturer=_manufacturer(model),
            accelerating_voltage=_qv(imaging.get("accelerating_voltage"), "kV"),
            cs=_qv(imaging.get("nominal_cs"), "mm"),
            c2_aperture=_qv(imaging.get("c2_aperture_diameter"), "micrometers"),
            electron_source=imaging.get("electron_source"),
            illumination_mode=imaging.get("illumination_mode"),
            specimen_holder_model=imaging.get("specimen_holder_model"),
            detector_model=detector,
            detector_manufacturer=_manufacturer(detector),
            detector_technology="direct_electron_detector"
            if any(m in detector_upper for m in _DIRECT_ELECTRON_MODELS) else None,
            detector_mode=_EM_DETECTOR_MODES.get((recording.get("detector_mode") or "").upper()),
            energy_filter_present=True if "BIOQUANTUM" in detector_upper or "QUANTUM" in detector_upper else None,
        )
        self.instruments.append(instrument)
        return instrument_id

    def em_preparation(self) -> str | None:
        vitrification = self.rows("em_vitrification")
        staining = self.rows("em_staining")
        embedding = self.rows("em_embedding")
        specimen = self.rows("em_specimen")
        if not (vitrification or staining or embedding or specimen):
            return None
        vit = vitrification[0] if vitrification else {}
        stain = staining[0] if staining else {}
        embed = embedding[0] if embedding else {}
        em: dict[str, Any] = {
            "cryogen": vit.get("cryogen_name"),
            "humidity_percentage": _qv(vit.get("humidity"), "percent"),
            "vitrification_instrument": vit.get("instrument"),
            "chamber_temperature": _qv(vit.get("chamber_temperature"), "K"),
            "ethane_temperature": _qv(vit.get("temp"), "K"),
            "stain_material": stain.get("material"),
            "stain_type": stain.get("type"),
            "embedding_material": embed.get("material"),
            "description": _text(vit.get("method"), vit.get("details"), stain.get("details"), embed.get("details")),
        }
        prep: dict[str, Any] = {
            "id": f"{self.base}/preparation/em-specimen",
            "preparation_type": "negative_stain" if staining and not vitrification else "cryo_em",
            "sample_id": self.sample_id,
            "title": "EM specimen preparation",
            "protocol_description": _text(*(s.get("details") for s in specimen)),
            "cryoem_preparation": {k: v for k, v in em.items() if v is not None} or None,
        }
        for row in specimen:
            self.extras(prep, "entry", row, "em_specimen[]")
        for row in vitrification:
            self.extras(prep, "entry", row, "em_vitrification[]")
        self.preparations.append(prep)
        return prep["id"]

    def nmr_runs(self, method: str, technique: str) -> None:
        conditions = {str(r.get("conditions_id")): r for r in self.rows("pdbx_nmr_exptl_sample_conditions")}
        spectrometers = {}
        for row in self.rows("pdbx_nmr_spectrometer"):
            sid = str(row.get("spectrometer_id"))
            instrument = NMRInstrument(
                id=f"{self.base}/instrument/nmr-{sid}",
                title=_text(row.get("manufacturer"), row.get("model"), sep=" ") or f"Spectrometer {sid}",
                instrument_code=f"PDB-{self.entry_id}-NMR{sid}",
                manufacturer=row.get("manufacturer"),
                model=row.get("model"),
                field_strength=_qv(row.get("field_strength"), "MHz"),
                spectrometer_type=row.get("type"),
                description=row.get("details"),
            )
            self.instruments.append(instrument)
            spectrometers[sid] = instrument.id
        experiments = self.rows("pdbx_nmr_exptl")
        refine = self.refine_for(method)
        if not experiments:
            run = self.new_run(_slug(method), technique, method,
                               quality_metrics=self.quality_metrics(refine, technique))
            self.link_run(run, next(iter(spectrometers.values()), None))
            return
        for row in experiments:
            xid = str(row.get("experiment_id"))
            run = self.new_run(f"nmr-{xid}", technique, method, title=row.get("type"),
                               quality_metrics=self.quality_metrics(refine, technique))
            self.extras(run, "entry", row, "pdbx_nmr_exptl[]")
            cond = conditions.get(str(row.get("conditions_id")))
            if cond:
                pressure = _qv(cond.get("pressure"), cond.get("pressure_units") or "atm")
                ec: dict[str, Any] = {
                    "temperature": _qv(cond.get("temperature"), cond.get("temperature_units") or "K"),
                    "pressure": pressure,
                    "description": _text(
                        cond.get("details"),
                        f"pressure {cond['pressure']}" if cond.get("pressure") and pressure is None else None,
                    ),
                }
                run["experimental_conditions"] = {k: v for k, v in ec.items() if v is not None} or None
                self.extras(run, "entry", cond, "pdbx_nmr_exptl_sample_conditions[]")
            solution = row.get("solution_id")
            sample_id = f"{self.base}/sample/nmr-{solution}"
            if not any(s["id"] == sample_id for s in self.samples):
                sample_id = self.sample_id
            self.link_run(run, spectrometers.get(str(row.get("spectrometer_id"))), sample_id=sample_id)

    def scattering_runs(self, method: str) -> None:
        rows = self.rows("pdbx_soln_scatter")
        if not rows:
            run = self.new_run("saxs", "saxs", method, quality_metrics=self.quality_metrics(None, "saxs"))
            self.link_run(run, None)
            return
        for row in rows:
            sid = str(row.get("id"))
            technique = "sans" if "neutron" in (row.get("type") or "").lower() else "saxs"
            qm = self.quality_metrics(None, technique)
            if row.get("mean_guiner_radius") is not None:
                qm["rg"] = _qv(row["mean_guiner_radius"], unit_for("entry", "pdbx_soln_scatter[].mean_guiner_radius"))
            run = self.new_run(f"scatter-{sid}", technique, method, quality_metrics=qm)
            run["experimental_conditions"] = {"temperature": _qv(row.get("temperature"), "K")} \
                if row.get("temperature") is not None else None
            self.extras(run, "entry", row, "pdbx_soln_scatter[]")
            # The sample-level fields were put on the sample; keep only the run's own here
            run["additional_metrics"] = [m for m in run.get("additional_metrics", [])
                                         if "concentration" not in m["attribute"]["label"]
                                         and "protein_length" not in m["attribute"]["label"]] or None
            instrument = SAXSInstrument(
                id=f"{self.base}/instrument/scatter-{sid}",
                title=row.get("source_type") or f"Scattering instrument for {self.entry_id}",
                instrument_code=f"PDB-{self.entry_id}-S{sid}",
                beamline_id=row.get("source_beamline"),
                model=row.get("source_beamline_instrument"),
                description=_text(row.get("source_class"), row.get("detector_type"), row.get("detector_specific")),
            )
            self.instruments.append(instrument)
            self.link_run(run, instrument.id)

    # ---- workflows ---------------------------------------------------------------------

    def runs_for_method(self, method: str | None) -> list[dict]:
        if method is None:
            return self.runs
        return [r for r in self.runs if r["_method"] == method.upper()] or self.runs

    def link_workflow(self, workflow: dict, runs: list[dict]) -> None:
        workflow.setdefault("_runs", [])
        for run in runs:
            if run["id"] not in workflow["_runs"]:
                workflow["_runs"].append(run["id"])

    def build_workflows(self) -> None:
        self.diffraction_workflows()
        self.em_workflows()
        self.nmr_workflows()
        self.scattering_workflows()
        self.validation_workflow()
        self.integrative_workflow()
        self.starting_models()

    def diffraction_workflows(self) -> None:
        refines = self.rows("refine")
        diffraction_methods = [m for m in self.methods if m in (
            "X-RAY DIFFRACTION", "NEUTRON DIFFRACTION", "FIBER DIFFRACTION", "POWDER DIFFRACTION",
            "ELECTRON CRYSTALLOGRAPHY")]
        refine_ids = {(r.get("pdbx_refine_id") or "").upper() for c in ("refine", "refine_hist", "refine_ls_restr",
                      "refine_analyze") for r in self.rows(c)}
        many = len(refine_ids) > 1
        refinement_by_method: dict[str, dict] = {}

        def refinement(method: str) -> dict:
            method = method.upper()
            if method not in refinement_by_method:
                if method == "ELECTRON MICROSCOPY":
                    wf = self.workflow("em-model-refinement", "model_refinement", "Model refinement")
                else:
                    key = f"refinement-{_slug(method)}" if many else "refinement"
                    wf = self.workflow(key, "refinement", f"Refinement against {method.lower() or 'the data'}")
                refinement_by_method[method] = wf
                self.link_workflow(wf, self.runs_for_method(method or None))
            return refinement_by_method[method]

        for row in refines:
            method = (row.get("pdbx_refine_id") or "").upper()
            wf = refinement(method)
            wf["rwork"] = _qv(row.get("ls_R_factor_R_work"), "dimensionless")
            wf["rfree"] = _qv(row.get("ls_R_factor_R_free"), "dimensionless")
            wf["resolution_high"] = _qv(row.get("ls_d_res_high"), "Angstroms")
            wf["resolution_low"] = _qv(row.get("ls_d_res_low"), "Angstroms")
            wf["refinement_resolution_a"] = _qv(row.get("ls_d_res_high"), "Angstroms")
            wf["description"] = _text(row.get("pdbx_method_to_determine_struct"), row.get("details"))
            wf["phasing_method"] = self.phasing_method(row.get("pdbx_method_to_determine_struct"))
            if row.get("pdbx_TLS_residual_ADP_flag"):
                wf["tls_used"] = True
            self.extras(wf, "entry", row, "refine[]")
            self.link_workflow(wf, self.runs_for_method(method))
        for row in self.rows("refine_hist"):
            wf = refinement(row.get("pdbx_refine_id") or "")
            wf["number_of_waters"] = _qv(row.get("number_atoms_solvent"), "molecules")
            self.extras(wf, "entry", row, "refine_hist[]", qualifier=str(row.get("cycle_id")))
        for row in self.rows("refine_ls_restr"):
            wf = refinement(row.get("pdbx_refine_id") or "")
            restraint = row.get("type")
            if restraint in _BOND_RESTRAINTS and row.get("dev_ideal") is not None:
                wf["rmsd_bonds"] = _qv(row["dev_ideal"], "Angstroms")
            if restraint in _ANGLE_RESTRAINTS and row.get("dev_ideal") is not None:
                wf["rmsd_angles"] = _qv(row["dev_ideal"], "degrees")
            self.extras(wf, "entry", row, "refine_ls_restr[]", qualifier=restraint)
        for row in self.rows("refine_analyze"):
            self.extras(refinement(row.get("pdbx_refine_id") or ""), "entry", row, "refine_analyze[]")

        # Data reduction and scaling, one workflow per reflns row
        reflns = self.rows("reflns")
        scaling: list[dict] = []
        for n, row in enumerate(reflns):
            key = f"scaling-{n + 1}" if len(reflns) > 1 else "scaling"
            wf = self.workflow(key, "scaling", "Data scaling and merging")
            wf["resolution_high"] = _qv(row.get("d_resolution_high"), "Angstroms")
            wf["resolution_low"] = _qv(row.get("d_resolution_low"), "Angstroms")
            wf["rmerge"] = _qv(row.get("pdbx_Rmerge_I_obs"), "dimensionless")
            wf["rpim"] = _qv(row.get("pdbx_Rpim_I_all"), "dimensionless")
            wf["cc_half"] = _qv(row.get("pdbx_CC_half"), "dimensionless")
            wf["completeness_percent"] = _qv(row.get("percent_possible_obs"), "percent")
            wf["i_over_sigma"] = _qv(row.get("pdbx_netI_over_sigmaI"), "dimensionless")
            wf["multiplicity"] = _qv(row.get("pdbx_redundancy"), "dimensionless")
            wf["wilson_b_factor"] = _qv(row.get("B_iso_Wilson_estimate"), "Angstroms^2")
            wf["n_total_unique"] = _qv(row.get("number_obs"), "reflections")
            wf["n_total_observations"] = _qv(row.get("pdbx_number_measured_all"), "reflections")
            self.extras(wf, "entry", row, "reflns[]")
            wf["_diffrn_ids"] = [str(d) for d in row.get("pdbx_diffrn_id") or []]
            runs = [r for r in self.runs if r.get("_diffrn_id") in wf["_diffrn_ids"]] or self.runs_for_method(
                diffraction_methods[0] if diffraction_methods else None)
            self.link_workflow(wf, runs)
            scaling.append(wf)
        for row in self.rows("reflns_shell"):
            ids = [str(d) for d in row.get("pdbx_diffrn_id") or []]
            shell_wf = next(
                (w for w in scaling if set(ids) & set(w["_diffrn_ids"])), scaling[0] if scaling else None)
            if shell_wf is None:
                shell_wf = self.workflow("scaling", "scaling", "Data scaling and merging")
                shell_wf["_diffrn_ids"] = ids
                scaling.append(shell_wf)
            shell: dict[str, Any] = {
                "resolution_high": _qv(row.get("d_res_high"), "Angstroms"),
                "resolution_low": _qv(row.get("d_res_low"), "Angstroms"),
                "completeness_percent": _qv(row.get("percent_possible_all"), "percent"),
                "multiplicity": _qv(row.get("pdbx_redundancy"), "dimensionless"),
                "i_over_sigma": _qv(row.get("meanI_over_sigI_obs"), "dimensionless"),
                "rmerge": _qv(row.get("Rmerge_I_obs"), "dimensionless"),
                "rpim": _qv(row.get("pdbx_Rpim_I_all"), "dimensionless"),
                "cc_half": _qv(row.get("pdbx_CC_half"), "dimensionless"),
                "n_unique": _qv(row.get("number_unique_obs"), "reflections"),
                "n_observations": _qv(row.get("number_measured_obs"), "reflections"),
            }
            shell = {k: v for k, v in shell.items() if v is not None}
            self.extras(shell, "entry", row, "reflns_shell[]")
            shell.pop("additional_properties", None)
            shell_wf.setdefault("resolution_shells", []).append(shell)
        for row in self.rows("pdbx_reflns_twin"):
            wf = scaling[0] if scaling else self.workflow("scaling", "scaling", "Data scaling and merging")
            self.extras(wf, "entry", row, "pdbx_reflns_twin[]", qualifier=row.get("operator"))
        for row in self.rows("pdbx_serial_crystallography_data_reduction"):
            wf = self.workflow("integration", "integration", "Serial crystallography data reduction")
            self.extras(wf, "entry", row, "pdbx_serial_crystallography_data_reduction[]")
            self.link_workflow(wf, [r for r in self.runs if r.get("_diffrn_id") == str(row.get("diffrn_id"))]
                               or self.runs_for_method("X-RAY DIFFRACTION"))

        # Software
        for row in self.rows("software"):
            classification = (row.get("classification") or "").lower()
            name = row.get("name")
            target: dict[str, Any] | None
            if classification == "data collection":
                for run in self.runs_for_method(diffraction_methods[0] if diffraction_methods else None):
                    run["acquisition_software"] = _text(run.get("acquisition_software"), name, sep=", ")
                    if row.get("version"):
                        run["acquisition_software_version"] = str(row["version"])
                target = None
            else:
                stage = _XRAY_SOFTWARE_STAGES.get(classification)
                if stage == "refinement":
                    target = next(iter(refinement_by_method.values()), None) or self.workflow(
                        "refinement", "refinement", "Refinement")
                    self.add_software(target, name, row.get("version"))
                elif stage == "scaling" and scaling:
                    target = scaling[0]
                    self.add_software(target, name, row.get("version"))
                elif stage:
                    titles = {"integration": "Data reduction", "scaling": "Data scaling and merging",
                              "phasing": "Phasing", "model_building": "Model building"}
                    target = self.workflow(stage, stage, titles[stage])
                    self.add_software(target, name, row.get("version"))
                    if stage == "phasing":
                        method = next((r.get("pdbx_method_to_determine_struct") for r in refines
                                       if r.get("pdbx_method_to_determine_struct")), None)
                        target["phasing_method"] = self.phasing_method(method)
                else:
                    target = next(iter(refinement_by_method.values()), None) or self.workflow(
                        "refinement", "refinement", "Refinement")
                    self.add_software(target, name, row.get("version"), note=row.get("classification") or "other")
            if target is not None:
                self.extras(target, "entry", row, "software[]", qualifier=name)
                self.link_workflow(target, self.runs_for_method(diffraction_methods[0] if diffraction_methods else None))

        self.refinement_workflows = list(refinement_by_method.values())

    def starting_models(self) -> None:
        """Starting models go on the step that used them: refinement, else EM model building."""
        for row in self.rows("pdbx_initial_refinement_model"):
            wf = next(iter(self.refinement_workflows), None)
            for key in ("em-model-building", "em-model-refinement", "refinement"):
                if wf is None and key in self.workflows:
                    wf = self.workflows[key]
            if wf is None:
                wf = self.workflow("refinement", "refinement", "Refinement")
                self.link_workflow(wf, self.runs)
            if row.get("accession_code") and (row.get("source_name") or "PDB").upper() == "PDB" \
                    and not wf.get("search_model_pdb_id"):
                wf["search_model_pdb_id"] = row["accession_code"]
            elif row.get("accession_code"):
                self.add_property(wf, "pdbx_initial_refinement_model.accession_code", row["accession_code"],
                                  "mmCIF:_pdbx_initial_refinement_model.accession_code")
            self.extras(wf, "entry", row, "pdbx_initial_refinement_model[]", qualifier=str(row.get("id")))

    @staticmethod
    def phasing_method(text: str | None) -> str | None:
        lower = (text or "").lower()
        for prefix, value in _PHASING_METHODS:
            if lower.startswith(prefix) or (prefix in ("molecular replacement",) and prefix in lower):
                return value
        return None

    def em_workflows(self) -> None:
        if not any(self.rows(c) for c in ("em_software", "em_3d_reconstruction", "em_ctf_correction",
                                          "em_particle_selection", "em_3d_fitting", "em_diffraction_stats")):
            return
        em_runs = [r for r in self.runs if r["technique"] in ("cryo_em", "cryo_et", "microed")] or self.runs
        titles = {
            "particle_picking": "Particle picking",
            "ctf_estimation": "CTF estimation and correction",
            "classification_2d": "Classification",
            "reconstruction": "3D reconstruction",
            "model_building": "Model fitting",
            "model_refinement": "Model refinement",
        }

        def stage(name: str) -> dict:
            wf = self.workflow(f"em-{name.replace('_', '-')}", _EM_STAGE_TYPES[name], titles[name])
            self.link_workflow(wf, em_runs)
            return wf

        for row in self.rows("em_ctf_correction"):
            wf = stage("ctf_estimation")
            self.append_description(wf, row.get("type"), row.get("details"))
        for row in self.rows("em_particle_selection"):
            wf = stage("particle_picking")
            params = wf.setdefault("particle_picking_params", {})
            if row.get("num_particles_selected") is not None:
                params["number_of_particles_selected"] = row["num_particles_selected"]
            self.append_description(wf, row.get("details"))
        for n, row in enumerate(self.rows("em_3d_reconstruction")):
            wf = stage("reconstruction")
            params = wf.setdefault("refinement_params", {})
            if row.get("num_particles") is not None:
                params["number_of_particles"] = row["num_particles"]
            if row.get("actual_pixel_size") is not None:
                params["pixel_size"] = _qv(row["actual_pixel_size"], "Angstroms")
            if row.get("resolution") is not None:
                wf["resolution_high"] = _qv(row["resolution"], "Angstroms")
                if "0.143" in (row.get("resolution_method") or ""):
                    params["resolution_0_143"] = _qv(row["resolution"], "Angstroms")
            self.append_description(wf, row.get("details"))
            self.extras(wf, "entry", row, "em_3d_reconstruction[]", qualifier=str(row.get("id")) if n else None)
        for row in self.rows("em_single_particle_entity"):
            wf = stage("reconstruction")
            params = wf.setdefault("refinement_params", {})
            symmetry = (row.get("point_symmetry") or "").strip()
            if symmetry in ("C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "D2", "D3", "D4", "D5",
                            "D6", "D7", "D8", "D9", "D10", "T", "O", "I"):
                params["symmetry"] = symmetry
            elif symmetry:
                params["description"] = _text(params.get("description"), f"point symmetry {symmetry}")
        for row in self.rows("em_helical_entity"):
            wf = stage("reconstruction")
            params = wf.setdefault("refinement_params", {})
            params["helical_rise"] = _qv(row.get("axial_rise_per_subunit"), "Angstroms")
            params["helical_twist"] = _qv(row.get("angular_rotation_per_subunit"), "degrees")
            params["axial_symmetry"] = row.get("axial_symmetry")
            params["description"] = _text(params.get("description"), row.get("details"))
        for row in self.rows("em_3d_fitting"):
            wf = stage("model_building")
            self.append_description(wf, row.get("details"))
            self.extras(wf, "entry", row, "em_3d_fitting[]", qualifier=str(row.get("id")))
        for row in self.rows("em_3d_fitting_list"):
            wf = stage("model_building")
            if row.get("pdb_entry_id") and not wf.get("search_model_pdb_id"):
                wf["search_model_pdb_id"] = row["pdb_entry_id"]
            elif row.get("pdb_entry_id"):
                self.add_property(wf, "em_3d_fitting_list.pdb_entry_id", row["pdb_entry_id"],
                                  "mmCIF:_em_3d_fitting_list.pdb_entry_id")
            self.extras(wf, "entry", row, "em_3d_fitting_list[]", qualifier=row.get("pdb_entry_id"))
        for row in self.rows("em_diffraction_stats"):
            wf = self.workflow("em-scaling", "scaling", "Electron diffraction data merging")
            self.link_workflow(wf, em_runs)
            wf["resolution_high"] = _qv(row.get("high_resolution"), "Angstroms")
            wf["rmerge"] = _qv(row.get("r_merge"), "dimensionless")
            wf["completeness_percent"] = _qv(row.get("fourier_space_coverage"), "percent")
            wf["n_total_observations"] = _qv(row.get("num_intensities_measured"), "reflections")
            wf["n_total_unique"] = _qv(row.get("num_structure_factors"), "reflections")
            self.append_description(wf, row.get("details"))
            self.extras(wf, "entry", row, "em_diffraction_stats[]")
        for row in self.rows("em_diffraction_shell"):
            wf = self.workflow("em-scaling", "scaling", "Electron diffraction data merging")
            self.link_workflow(wf, em_runs)
            shell: dict[str, Any] = {
                "resolution_high": _qv(row.get("high_resolution"), "Angstroms"),
                "resolution_low": _qv(row.get("low_resolution"), "Angstroms"),
                "completeness_percent": _qv(row.get("fourier_space_coverage"), "percent"),
                "multiplicity": _qv(row.get("multiplicity"), "dimensionless"),
                "n_unique": _qv(row.get("num_structure_factors"), "reflections"),
            }
            shell = {k: v for k, v in shell.items() if v is not None}
            self.extras(shell, "entry", row, "em_diffraction_shell[]")
            shell.pop("additional_properties", None)
            wf.setdefault("resolution_shells", []).append(shell)
        for row in self.rows("em_software"):
            category = (row.get("category") or "").upper()
            name = row.get("name")
            if not name or category == "IMAGE ACQUISITION":
                continue
            name_stage = _EM_SOFTWARE_STAGES.get(category)
            wf = stage(name_stage or "reconstruction")
            self.add_software(wf, name, row.get("version"), note=None if name_stage else category)
            if row.get("details"):
                self.append_description(wf, row["details"])

    def nmr_workflows(self) -> None:
        nmr = [m for m in self.methods if "NMR" in m]
        if not nmr:
            return
        runs = self.runs_for_method(nmr[0])
        wf = self.workflow("refinement", "refinement", "NMR structure calculation and refinement")
        self.link_workflow(wf, runs)
        for row in self.rows("pdbx_nmr_refine"):
            self.append_description(wf, row.get("method"), row.get("details"))
        details = self.entry.get("pdbx_nmr_details", {}).get("text")
        self.append_description(wf, details)
        for category in ("pdbx_nmr_ensemble", "pdbx_nmr_representative"):
            record = self.entry.get(category)
            if isinstance(record, dict):
                self.extras(wf, "entry", record, category)
        for row in self.rows("pdbx_nmr_software"):
            classification = (row.get("classification") or "").lower()
            stage = _NMR_SOFTWARE_STAGES.get(classification)
            if classification == "collection":
                for run in runs:
                    run["acquisition_software"] = _text(run.get("acquisition_software"), row.get("name"), sep=", ")
                target = wf
            elif stage == "model_building":
                target = self.workflow("model-building", "model_building", "NMR structure calculation")
                self.link_workflow(target, runs)
                self.add_software(target, row.get("name"), row.get("version"))
            elif stage == "refinement":
                target = wf
                self.add_software(wf, row.get("name"), row.get("version"))
            else:
                target = wf
                self.add_software(wf, row.get("name"), row.get("version"), note=row.get("classification") or "other")
            self.extras(target, "entry", row, "pdbx_nmr_software[]", qualifier=row.get("name"))

    def scattering_workflows(self) -> None:
        models = self.rows("pdbx_soln_scatter_model")
        for row in self.rows("pdbx_soln_scatter"):
            sid = str(row.get("id"))
            wf = self.workflow(f"saxs-{sid}", "saxs_analysis", "Scattering data reduction and analysis")
            self.link_workflow(wf, [r for r in self.runs if r["id"].endswith(f"scatter-{sid}")] or self.runs)
            analysis = row.get("data_analysis_software_list")
            reduction = row.get("data_reduction_software_list")
            if analysis:
                self.add_software(wf, analysis)
            if reduction:
                self.add_software(wf, reduction, note="data reduction")
            for model in models:
                if str(model.get("scatter_id")) != sid:
                    continue
                if model.get("software_list"):
                    self.add_software(wf, model["software_list"], note="modelling")
                self.append_description(wf, model.get("details"))
                self.extras(wf, "entry", model, "pdbx_soln_scatter_model[]", qualifier=str(model.get("id")))

    def validation_workflow(self) -> None:
        categories = [c for c in ("pdbx_vrpt_summary", "pdbx_vrpt_summary_geometry", "pdbx_vrpt_summary_diffraction",
                                  "pdbx_vrpt_summary_em", "pdbx_vrpt_summary_nmr") if self.entry.get(c)]
        if not categories:
            return
        wf = self.workflow("validation", "model_validation", "wwPDB validation report",
                           software_name="wwPDB validation pipeline")
        wf["validation_report_path"] = self.validation_report_url()
        wf["completed_at"] = self.entry.get("pdbx_vrpt_summary", {}).get("report_creation_date")
        for category in categories:
            record = self.entry[category]
            if isinstance(record, list):
                for row in record:
                    self.extras(wf, "entry", row, f"{category}[]")
            else:
                self.extras(wf, "entry", record, category)
        self.link_workflow(wf, self.runs)

    def validation_report_url(self) -> str:
        lower = self.entry_id.lower()
        return (f"https://files.rcsb.org/pub/pdb/validation_reports/{lower[1:3]}/{lower}/"
                f"{lower}_full_validation.pdf.gz")

    def integrative_workflow(self) -> None:
        rows = self.rows("rcsb_ihm_dataset_list")
        if not rows:
            return
        wf = self.workflow("integrative-modeling", "model_building", "Integrative modelling")
        for row in rows:
            self.extras(wf, "entry", row, "rcsb_ihm_dataset_list[]", qualifier=row.get("name"))
        self.link_workflow(wf, self.runs)

    # ---- files -------------------------------------------------------------------------

    def build_data_files(self) -> None:
        upper, lower = self.entry_id, self.entry_id.lower()
        status = self.entry.get("pdbx_database_status", {})
        released = self.entry.get("rcsb_accession_info", {}).get("has_released_experimental_data") == "Y"

        def add(key: str, name: str, url: str, fmt: str, description: str, data_type: str | None = None) -> None:
            self.data_files.append({
                "id": f"{self.base}/file/{key}",
                "file_name": name,
                "file_path": url,
                "file_format": fmt,
                "description": description,
                "data_type": data_type,
            })

        if status.get("pdb_format_compatible", "Y") != "N":
            add("pdb", f"{lower}.pdb", f"https://files.rcsb.org/download/{upper}.pdb", "pdb",
                "PDB format coordinates", "model")
        add("mmcif", f"{lower}.cif", f"https://files.rcsb.org/download/{upper}.cif", "mmcif",
            "mmCIF format coordinates", "model")
        if released and status.get("status_code_sf") == "REL":
            add("sf", f"{lower}-sf.cif", f"https://files.rcsb.org/download/{upper}-sf.cif", "mmcif",
                "Structure factors", "processed_data")
        if released and status.get("status_code_mr") == "REL":
            add("mr", f"{lower}.mr", f"https://files.rcsb.org/download/{upper}.mr", "ascii",
                "NMR restraints", "processed_data")
        if released and status.get("status_code_cs") == "REL":
            add("cs", f"{lower}_cs.str", f"https://files.rcsb.org/download/{upper}_cs.str", "nmr_star",
                "NMR chemical shifts", "processed_data")
        for emdb in self.entry.get("rcsb_entry_container_identifiers", {}).get("emdb_ids") or []:
            number = emdb.split("-")[-1]
            add(f"map-{number}", f"emd_{number}.map.gz",
                f"https://files.wwpdb.org/pub/emdb/structures/{emdb}/map/emd_{number}.map.gz", "mrc",
                f"{emdb} primary map", "volume")
        if any(self.entry.get(c) for c in ("pdbx_vrpt_summary", "pdbx_vrpt_summary_geometry")):
            add("validation", f"{lower}_full_validation.pdf.gz", self.validation_report_url(), "pdf",
                "wwPDB full validation report", "validation_report")
        for n, row in enumerate(self.rows("pdbx_related_exp_data_set"), 1):
            reference = row.get("data_reference") or ""
            url = f"https://doi.org/{reference}" if reference.startswith("10.") else reference
            self.data_files.append({
                "id": f"{self.base}/file/raw-{n}",
                "file_name": reference or f"dataset {n}",
                "file_path": url or None,
                "file_format": "other",
                "data_type": "raw_data",
                "description": _text(row.get("data_set_type"), row.get("db_source"), row.get("details"),
                                     row.get("metadata_reference")),
            })
        for n, row in enumerate(self.rows("ihm_external_reference_info"), 1):
            url = row.get("associated_url")
            self.data_files.append({
                "id": f"{self.base}/file/ihm-{n}",
                "file_name": (url or f"reference {n}").rstrip("/").split("/")[-1],
                "file_path": url,
                "file_format": "other",
                "description": _text(row.get("reference_provider"), row.get("reference")),
            })

    # ---- assemble ------------------------------------------------------------------------

    def assemble(self) -> Dataset:
        study = self.study()
        info = self.entry.get("rcsb_accession_info", {})
        revision = None
        if info.get("major_revision") is not None:
            revision = f"{info['major_revision']}.{info.get('minor_revision', 0)}"

        workflows = []
        workflow_experiments = []
        for wf in self.workflows.values():
            for run_id in wf.pop("_runs", []):
                workflow_experiments.append({"workflow_id": wf["id"], "experiment_id": run_id})
            wf.pop("_diffrn_ids", None)
            workflows.append(wf)
        for run in self.runs:
            run.pop("_method", None)
            run.pop("_diffrn_id", None)

        samples = self.samples
        dataset = {
            "id": self.base,
            "title": study["title"],
            "keywords": study.get("keywords"),
            "deposition_date": _date(info.get("deposit_date")),
            "release_date": _date(info.get("initial_release_date")),
            "last_revision_date": _date(info.get("revision_date")),
            "revision": revision,
            "studies": [study],
            "persons": self.persons or None,
            "organizations": self.organizations or None,
            "publications": self.publications or None,
            "instruments": self.instruments or None,
            "proteins": list(self.proteins.values()) or None,
            "protein_constructs": self.constructs or None,
            "nucleic_acids": self.nucleic_acids or None,
            "small_molecules": list(self.small_molecules.values()) or None,
            "samples": samples,
            "sample_components": self.components or None,
            "sample_preparations": self.preparations or None,
            "experiment_runs": self.runs,
            "workflow_runs": workflows,
            "data_files": self.data_files,
            "study_sample_associations": [{"study_id": self.study_id, "sample_id": s["id"]} for s in samples],
            "study_experiment_associations": [
                {"study_id": self.study_id, "experiment_id": r["id"]} for r in self.runs
            ],
            "study_workflow_associations": [
                {"study_id": self.study_id, "workflow_id": w["id"]} for w in workflows
            ] or None,
            "experiment_sample_associations": self.experiment_samples or None,
            "experiment_instrument_associations": self.experiment_instruments or None,
            "sample_protein_associations": self.sample_protein or None,
            "sample_nucleic_acid_associations": self.sample_nucleic_acid or None,
            "sample_component_interactions": self.interactions or None,
            "workflow_experiment_associations": workflow_experiments,
            "study_person_associations": self.study_persons or None,
            "study_organization_associations": self.study_organizations or None,
            "study_publication_associations": self.study_publications or None,
        }
        return Dataset(**_prune(dataset))


def _prune(value: Any) -> Any:
    """Drop None values and empty containers from nested dicts and lists, leaving models alone."""
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            item = _prune(item)
            if item is None or (isinstance(item, (list, dict)) and not item):
                continue
            out[key] = item
        return out
    if isinstance(value, list):
        return [p for p in (_prune(v) for v in value) if p is not None and p != {} and p != []]
    return value
