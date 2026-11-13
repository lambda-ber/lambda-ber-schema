"""
PDB-REDO loader.

PDB-REDO (https://pdb-redo.eu) takes the X-ray entries of the PDB that came with
structure factors and re-refines the deposited model against them with current
methods, rebuilding it where the data support that.

An entry there is the PDB entry's crystal, diffraction data and molecules with a new
model on top, so this loader does not read any of that again. It loads the PDB entry
with PDBLoader, keeps every row that loader builds under its ``pdb:`` id, and adds
what PDB-REDO changed:

- one WorkflowRun for the re-refinement, with the final R, R-free and clashscore, and
  in its notes how the model compares with the deposited one
- a DataFile for each file PDB-REDO serves for the entry
- WorkflowInputAssociation rows from that run to the deposited model and structure
  factors, and WorkflowOutputAssociation rows to its own files
- a WorkflowExperimentAssociation to the PDB entry's experiment

Because the PDB rows keep their ids, the PDB-REDO dataset and the PDB dataset for one
entry share their sample, protein, instrument and experiment rows, and the deposited
refinement and the PDB-REDO one sit side by side.

API: ``https://pdb-redo.eu/db/{pdbid}/data.json`` holds the statistics and
``versions.json`` the software and the PDB revisions it started from. There is no
public entry list, and an entry PDB-REDO did not process answers 500 with
``{"error": "Not Found"}``.
"""

from typing import Any

import requests

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.loaders.pdb import PDBLoader
from lambda_ber_schema.pydantic import (
    DataFile,
    DataTypeEnum,
    FileFormatEnum,
    InputTypeEnum,
    OutputTypeEnum,
    QuantityValue,
    WorkflowExperimentAssociation,
    WorkflowInputAssociation,
    WorkflowOutputAssociation,
    WorkflowRun,
    WorkflowTypeEnum,
)


def _number(value: Any) -> float | int | None:
    """A data.json value as a number, or None for null and for the odd quoted field."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return value


def _quantity(value: Any, unit: str) -> QuantityValue | None:
    number = _number(value)
    return QuantityValue(numeric_value=number, unit=unit) if number is not None else None


def _show(value: Any) -> str:
    return "n/a" if value is None else str(value)


def _not_found(response: requests.Response) -> bool:
    """
    Whether PDB-REDO is saying it has no such entry.

    Its entry endpoints answer an unknown entry with 500 and ``{"error": "Not Found"}``
    rather than 404, so the body decides; any other error is a real failure.
    """
    if response.status_code == 404:
        return True
    if response.status_code < 400:
        return False
    try:
        body = response.json()
    except ValueError:
        return False
    return isinstance(body, dict) and str(body.get("error", "")).lower() == "not found"


class PDBREDOLoader(BaseLoader):
    """
    Loader for the PDB-REDO databank of re-refined X-ray structures.

    Wraps a PDBLoader: the dataset is the PDB entry's, plus the PDB-REDO run and files.

    Example:
        >>> loader = PDBREDOLoader()
        >>> result = loader.load("1CBS")
        >>> result.dataset.id
        'pdb-redo:1CBS'
        >>> result.dataset.workflow_runs[-1].software_name
        'PDB-REDO'
    """

    source_name = "pdb-redo"
    base_url = "https://pdb-redo.eu/db"

    def __init__(self, cache: ResponseCache | None = None, pdb_loader: PDBLoader | None = None):
        """
        Initialize the PDB-REDO loader.

        Args:
            cache: Optional response cache, shared with the PDB loader built here
            pdb_loader: The loader for the underlying PDB entry; one is built if omitted
        """
        self.cache = cache or ResponseCache(enabled=False)
        self.pdb_loader = pdb_loader or PDBLoader(cache=self.cache)

    def load(self, entry_id: str) -> LoaderResult:
        """
        Load the PDB-REDO entry for a PDB entry.

        Args:
            entry_id: PDB entry ID (e.g., "1CBS"), in either case

        Returns:
            LoaderResult with the PDB entry's dataset plus the PDB-REDO run and files

        Raises:
            ValueError: If PDB-REDO has no entry for it, as for NMR and cryo-EM entries
                and X-ray entries deposited without structure factors
            requests.HTTPError: If PDB-REDO or the RCSB API fails otherwise
        """
        entry_id = entry_id.strip().upper()

        # PDB-REDO first: an entry it lacks is ruled out before the RCSB calls
        properties = self._fetch_data(entry_id)
        redo_warnings: list[str] = []
        versions = self._fetch_versions(entry_id, redo_warnings)

        base = self.pdb_loader.load(entry_id)
        pdb_dataset = base.dataset
        warnings = [*base.warnings, *redo_warnings]

        dataset_id = self.make_id(entry_id)
        workflow = self._create_workflow_run(entry_id, dataset_id, properties, versions)
        outputs = self._create_data_files(entry_id, dataset_id, properties)
        files = [data_file for data_file, _ in outputs]

        # The run starts from the deposited model and refines it against the deposited
        # structure factors; PDBLoader names those two DataFiles this way
        pdb_file_ids = {f.id for f in pdb_dataset.data_files or []}
        inputs = []
        for file_id, input_type in (
            (f"pdb:{entry_id}/file/mmcif", InputTypeEnum.structure_prior),
            (f"pdb:{entry_id}/file/sf", InputTypeEnum.raw_data),
        ):
            if file_id in pdb_file_ids:
                inputs.append(
                    WorkflowInputAssociation(
                        workflow_id=workflow.id, file_id=file_id, input_type=input_type
                    )
                )
            else:
                warnings.append(
                    f"{entry_id}: the PDB entry has no {file_id} file; "
                    "the PDB-REDO run is not linked to it"
                )

        output_associations = [
            WorkflowOutputAssociation(
                workflow_id=workflow.id, file_id=data_file.id, output_type=output_type
            )
            for data_file, output_type in outputs
        ]
        experiment_associations = [
            WorkflowExperimentAssociation(workflow_id=workflow.id, experiment_id=run.id)
            for run in pdb_dataset.experiment_runs or []
        ]

        title = pdb_dataset.title or entry_id
        dataset = pdb_dataset.model_copy(
            update={
                "id": dataset_id,
                "title": f"PDB-REDO {entry_id}: {title}",
                "workflow_runs": [*(pdb_dataset.workflow_runs or []), workflow],
                "data_files": [*(pdb_dataset.data_files or []), *files],
                "workflow_input_associations": [
                    *(pdb_dataset.workflow_input_associations or []), *inputs
                ],
                "workflow_output_associations": [
                    *(pdb_dataset.workflow_output_associations or []), *output_associations
                ],
                "workflow_experiment_associations": [
                    *(pdb_dataset.workflow_experiment_associations or []),
                    *experiment_associations,
                ],
            }
        )

        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            source_url=f"{self.base_url}/{entry_id.lower()}",
            raw_data={
                "pdb": base.raw_data,
                "pdb_redo": {"properties": properties, "versions": versions},
            },
        )

    def list_entries(self, limit: int | None = None, **filters: Any) -> list[str]:
        """
        List PDB entries PDB-REDO may hold.

        PDB-REDO publishes no entry list. It covers the X-ray entries of the PDB that
        have structure factors, so this lists X-ray entries from the RCSB search API.
        One that PDB-REDO could not process fails to load with a ValueError naming it.

        Args:
            limit: Maximum number of entries to return
            **filters: Ignored; the method is always X-ray

        Returns:
            List of PDB entry IDs
        """
        return self.pdb_loader.list_entries(experimental_method="X-RAY", limit=limit)

    def _fetch_data(self, entry_id: str) -> dict[str, Any]:
        """The summary statistics of an entry, from data.json."""
        cache_key = f"pdb-redo/{entry_id}/data"

        def fetch() -> dict[str, Any]:
            url = f"{self.base_url}/{entry_id.lower()}/data.json"
            response = requests.get(url, timeout=30)
            if _not_found(response):
                raise ValueError(
                    f"{entry_id} is not in the PDB-REDO databank (it covers X-ray entries "
                    "deposited with structure factors)"
                )
            response.raise_for_status()
            payload = response.json()
            # data.json also lists every residue's phi and psi before and after; only the
            # summary is read, so only the summary is cached
            return {"pdbid": payload.get("pdbid"), "properties": payload.get("properties")}

        properties = self.cache.get_or_fetch(cache_key, fetch).get("properties")
        if not properties:
            raise ValueError(f"PDB-REDO returned no statistics for {entry_id}")
        return properties

    def _fetch_versions(self, entry_id: str, warnings: list[str]) -> dict[str, Any]:
        """Software versions and input revisions from versions.json, or {} when absent."""
        cache_key = f"pdb-redo/{entry_id}/versions"

        def fetch() -> dict[str, Any]:
            url = f"{self.base_url}/{entry_id.lower()}/versions.json"
            response = requests.get(url, timeout=30)
            if _not_found(response):
                return {}
            response.raise_for_status()
            return response.json()

        versions = self.cache.get_or_fetch(cache_key, fetch)
        if not versions:
            warnings.append(
                f"{entry_id}: PDB-REDO has no versions.json; the software list and the "
                "PDB revision the run started from are unknown"
            )
        return versions

    def _create_workflow_run(
        self,
        entry_id: str,
        dataset_id: str,
        properties: dict[str, Any],
        versions: dict[str, Any],
    ) -> WorkflowRun:
        """The re-refinement as one WorkflowRun, with the final model's statistics."""
        p = properties
        software = versions.get("software") or {}
        # versions.json gives the version as a string; data.json as a number, which
        # would turn 8.10 into 8.1
        version = (software.get("pdb-redo") or {}).get("version")
        if version is None and _number(p.get("VERSION")) is not None:
            version = str(p["VERSION"])
        additional_software = "; ".join(
            f"{name} {info['version']}" if info.get("version") else name
            for name, info in software.items()
            if name != "pdb-redo" and info.get("used")
        )

        # A deposited R-free that was refined against, or a test set chosen after the
        # fact, reads low; PDB-REDO then compares with its estimate of the unbiased
        # value, so that estimate is shown beside the recalculated one
        before_free = _show(p.get("RFCAL"))
        if _number(p.get("RFCALUNB")) is not None:
            before_free += f" (estimated unbiased {p['RFCALUNB']})"
        description = (
            f"PDB-REDO re-refinement of PDB {entry_id} against its deposited structure "
            f"factors. Deposited model as recalculated by PDB-REDO -> final model: "
            f"R {_show(p.get('RCAL'))} -> {_show(p.get('RFIN'))}, "
            f"R-free {before_free} -> {_show(p.get('RFFIN'))}."
        )

        return WorkflowRun(
            id=f"{dataset_id}/workflow/re-refinement",
            title=f"PDB-REDO re-refinement of {entry_id}",
            workflow_code=f"PDB-REDO-{entry_id}",
            workflow_type=WorkflowTypeEnum.model_refinement,
            software_name="PDB-REDO",
            software_version=version,
            additional_software=additional_software or None,
            description=description,
            refinement_resolution_a=_quantity(p.get("RESOLUTION"), "Angstroms"),
            space_group=p.get("SPACEGROUP"),
            rwork=_quantity(p.get("RFIN"), "dimensionless"),
            rfree=_quantity(p.get("RFFIN"), "dimensionless"),
            clashscore=_quantity(p.get("FCLASH"), "dimensionless"),
            wilson_b_factor=_quantity(p.get("BWILS"), "Å²"),
            completed_at=p.get("TIME"),
            deposited_to_pdb=False,
            validation_report_path=f"{self.base_url}/{entry_id.lower()}/wf/pdbout.txt",
            processing_notes=self._processing_notes(p, versions),
        )

    def _processing_notes(self, p: dict[str, Any], versions: dict[str, Any]) -> str:
        """
        The comparison the PDB-REDO entry page shows, as text.

        WorkflowRun has slots for the final model's R, R-free and clashscore but none
        for PDB-REDO's Z-scores or for the deposited model's figures it recalculated,
        so those are written out here. O-prefixed keys are the deposited model, F the
        final one.
        """
        notes = [
            (
                f"Deposited header: R {_show(p.get('RFACT'))}, "
                f"R-free {_show(p.get('RFREE'))}."
            ),
        ]
        recalculated = (
            f"Deposited model recalculated by PDB-REDO: R {_show(p.get('RCAL'))}, "
            f"R-free {_show(p.get('RFCAL'))}"
        )
        if _number(p.get("RFCALUNB")) is not None:
            recalculated += f" (estimated unbiased R-free {p['RFCALUNB']})"
        if _number(p.get("RFCALZ")) is not None:
            # High when R-free sits further below its expected value than chance allows
            recalculated += f", R-free Z-score {p['RFCALZ']}"
        notes.append(recalculated + ".")
        notes.append(
            f"Re-refined only (TLS, no rebuilding): R {_show(p.get('RTLS'))}, "
            f"R-free {_show(p.get('RFTLS'))}."
        )
        notes.append(
            f"Re-refined and rebuilt: R {_show(p.get('RFIN'))}, "
            f"R-free {_show(p.get('RFFIN'))}."
        )

        scores = [
            ("bond length RMS Z-score", "OBRMSZ", "FBRMSZ"),
            ("bond angle RMS Z-score", "OARMSZ", "FARMSZ"),
            ("Ramachandran Z-score", "OZRAMA", "FZRAMA"),
            ("rotamer normality Z-score", "OCHI12", "FCHI12"),
            ("coarse packing Z-score", "OZPAK1", "FZPAK1"),
            ("fine packing Z-score", "OZPAK2", "FZPAK2"),
            ("MolProbity clashscore", "OCLASH", "FCLASH"),
            ("hydrogen bond satisfaction", "OHBSAT", "FHBSAT"),
        ]
        shown = [
            f"{label} {_show(p.get(before))} -> {_show(p.get(after))}"
            for label, before, after in scores
            if p.get(before) is not None or p.get(after) is not None
        ]
        if shown:
            notes.append("Validation, deposited -> final: " + "; ".join(shown) + ".")

        changes = [
            ("loops built", "NLOOPS"),
            ("side chains built", "NSCBLT"),
            ("rotamers changed", "NDROTA"),
            ("peptides flipped", "NBBFLIP"),
            ("chiralities fixed", "NCHIRFX"),
            ("waters removed", "NWATDEL"),
            ("residues fitting density better", "RSCCB"),
            ("residues fitting density worse", "RSCCW"),
        ]
        shown = [f"{label} {p[key]}" for label, key in changes if p.get(key) is not None]
        if shown:
            notes.append("Model changes: " + "; ".join(shown) + ".")

        data = versions.get("data") or {}
        major = data.get("coordinates_revision_major_mmCIF")
        minor = data.get("coordinates_revision_minor_mmCIF")
        if major is not None:
            started = f"Started from PDB model revision {major}.{minor or 0}"
            if data.get("reflections_revision"):
                started += f" and reflections revision {data['reflections_revision']}"
            notes.append(started + ".")

        return " ".join(notes)

    def _create_data_files(
        self, entry_id: str, dataset_id: str, properties: dict[str, Any]
    ) -> list[tuple[DataFile, OutputTypeEnum]]:
        """The files PDB-REDO serves for the entry, each with its output type."""
        lower = entry_id.lower()
        url = f"{self.base_url}/{lower}"
        specs = [
            ("final_cif", f"{lower}_final.cif", FileFormatEnum.mmcif, DataTypeEnum.model,
             "final", OutputTypeEnum.model, "Re-refined and rebuilt model (mmCIF)"),
            ("final_pdb", f"{lower}_final.pdb", FileFormatEnum.pdb, DataTypeEnum.model,
             "final", OutputTypeEnum.model, "Re-refined and rebuilt model (PDB format)"),
            ("final_mtz", f"{lower}_final.mtz", FileFormatEnum.mtz,
             DataTypeEnum.processed_data, "final", OutputTypeEnum.processed_data,
             "Reflections and map coefficients for the re-refined and rebuilt model"),
            ("besttls_cif", f"{lower}_besttls.cif.gz", FileFormatEnum.gz, DataTypeEnum.model,
             "intermediate", OutputTypeEnum.model,
             "Re-refined (only) model, before rebuilding (gzipped mmCIF)"),
            ("besttls_mtz", f"{lower}_besttls.mtz.gz", FileFormatEnum.gz,
             DataTypeEnum.processed_data, "intermediate", OutputTypeEnum.processed_data,
             "Reflections and map coefficients for the re-refined (only) model (gzipped MTZ)"),
            ("data", "data.json", FileFormatEnum.json, DataTypeEnum.validation_report,
             "diagnostic", OutputTypeEnum.statistics,
             "Refinement and validation statistics, deposited and final"),
            ("versions", "versions.json", FileFormatEnum.json, DataTypeEnum.metadata,
             "metadata", OutputTypeEnum.metadata,
             "Software versions and the PDB revisions the run started from"),
            ("archive", f"{lower}.zip", FileFormatEnum.zip, DataTypeEnum.processed_data,
             "final", OutputTypeEnum.processed_data, "All PDB-REDO files for the entry"),
        ]
        # The archive is served at /zipped and saved as {id}.zip
        paths = {"archive": f"{url}/zipped"}

        files = []
        for key, name, file_format, data_type, role, output_type, description in specs:
            # NOPDB: the model does not fit the PDB format, so only mmCIF is served
            if key == "final_pdb" and properties.get("NOPDB"):
                continue
            files.append(
                (
                    DataFile(
                        id=f"{dataset_id}/file/{key}",
                        file_name=name,
                        file_format=file_format,
                        file_path=paths.get(key, f"{url}/{name}"),
                        data_type=data_type,
                        file_role=role,
                        description=description,
                    ),
                    output_type,
                )
            )
        return files
