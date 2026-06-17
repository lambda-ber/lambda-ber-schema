"""
SSRL macromolecular crystallography (MX) loader.

Consumes a **published LAMBDA RO-Crate package** (the single canonical on-disk metadata produced by
crystals-play / iceflow ``publish_assembly.py``) and maps its semantic graph into the lambda-ber schema.

The crate root is a ``lambda:Experiment`` (the study); the graph carries ``lambda:RawUnit`` (specimens),
``lambda:DerivedProduct`` (processed results), ``CreateAction`` workflow runs (with the parsed run
definition + processing stats inline), ``SoftwareApplication`` and ``File`` entities, plus
``ScholarlyArticle`` / structure citations. crystals-play performs all derivation up front, so this
loader is a pure crate -> schema mapper.

This replaces the previous loader that ingested raw DCSS beamline snapshots + directory-keyed enrichment
files; lambda-ber now ingests SSRL MX data only via published distribution packages.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.pydantic import (
    DataFile,
    DataTypeEnum,
    Dataset,
    ExperimentalConditions,
    ExperimentInstrumentAssociation,
    ExperimentRun,
    ExperimentSampleAssociation,
    FacilityEnum,
    FileFormatEnum,
    InstrumentCategoryEnum,
    OutputTypeEnum,
    QualityMetrics,
    QuantityValue,
    Sample,
    SampleTypeEnum,
    Study,
    StudyExperimentAssociation,
    StudySampleAssociation,
    StudyWorkflowAssociation,
    TechniqueEnum,
    WorkflowExperimentAssociation,
    WorkflowOutputAssociation,
    WorkflowRun,
    WorkflowTypeEnum,
    XRayInstrument,
    XRaySourceTypeEnum,
)

# Canonical LIMS bundle URL for an experiment's output files (a tar archive). `{dataset}` is the DCSS
# file_root (the sample-level name); the experiment UUID disambiguates multiple runs of the same sample.
LIMS_BUNDLE_URL_TEMPLATE = (
    "https://smb.slac.stanford.edu/dev/lims/lambda/experiment/{experiment_uuid}/bundle/{dataset}.tar"
)


def _types(entity: dict[str, Any]) -> list[str]:
    """Normalise an entity's @type to a list (it may be a string or a list)."""
    t = entity.get("@type")
    return [t] if isinstance(t, str) else (t or [])


def _has_type(entity: dict[str, Any], type_name: str) -> bool:
    return type_name in _types(entity)


class SSRLMXLoader(BaseLoader):
    """Loader for SSRL macromolecular crystallography (MX) distribution packages (RO-Crate)."""

    source_name = "ssrl-mx"
    base_url = None  # File-based, no API
    facility = "SSRL"  # Loader is SSRL-specific

    def load(self, identifier: str) -> LoaderResult:
        """
        Load a published distribution package by path.

        Args:
            identifier: Path to a package directory, or directly to its ``ro-crate-metadata.json``.

        Returns:
            LoaderResult with a populated Dataset.

        Raises:
            FileNotFoundError: If the RO-Crate file doesn't exist.
            ValueError: If the crate has no root ``lambda:Experiment`` entity.
        """
        path = Path(identifier)
        crate_path = path / "ro-crate-metadata.json" if path.is_dir() else path
        if not crate_path.exists():
            raise FileNotFoundError(f"RO-Crate not found: {crate_path}")

        graph: list[dict[str, Any]] = json.loads(crate_path.read_text()).get("@graph", [])
        by_id = {e.get("@id"): e for e in graph if e.get("@id")}
        warnings: list[str] = []

        root = by_id.get("./") or next(
            (e for e in graph if _has_type(e, "lambda:Experiment")), None
        )
        if root is None:
            raise ValueError(f"RO-Crate {crate_path} has no root lambda:Experiment entity")

        study_id = (root.get("identifier") or {}).get("value")
        dataset_id = self.make_id(study_id) if study_id else self.make_id(crate_path.parent.name)

        study = Study(
            id=f"{self.source_name}:study/{study_id}" if study_id else f"{dataset_id}/study",
            title=root.get("name") or f"SSRL MX study {study_id or ''}".strip(),
            keywords=root.get("keywords") or None,
        )

        # One instrument: the root's instrumentName (profile term); fall back to a per-product
        # lambda:beamline for crates produced before that move.
        beamline = root.get("instrumentName") or next(
            (e.get("lambda:beamline") for e in graph
             if _has_type(e, "lambda:DerivedProduct") and e.get("lambda:beamline")),
            None,
        )
        instrument = self._instrument(beamline)

        # RawUnits -> Samples, keyed by crate @id so workflow `object` refs can resolve them.
        sample_by_ruid: dict[str, Sample] = {}
        samples: list[Sample] = []
        for e in graph:
            if _has_type(e, "lambda:RawUnit"):
                s = self._sample(e, dataset_id, root)
                sample_by_ruid[e["@id"]] = s
                samples.append(s)

        software_by_id = {e["@id"]: e for e in graph if _has_type(e, "SoftwareApplication")}

        experiments: list[ExperimentRun] = []
        workflow_runs: list[WorkflowRun] = []
        data_files: list[DataFile] = []
        experiment_sample_assoc: list[ExperimentSampleAssociation] = []
        experiment_instrument_assoc: list[ExperimentInstrumentAssociation] = []
        workflow_experiment_assoc: list[WorkflowExperimentAssociation] = []
        workflow_output_assoc: list[WorkflowOutputAssociation] = []

        # Each CreateAction = one processing run -> an ExperimentRun (acquisition, from the inline run
        # definition) + a WorkflowRun (processing stats + software) + its output DataFiles.
        for wf in [e for e in graph if _has_type(e, "CreateAction")]:
            expid = wf.get("workflowRunId") or wf.get("@id")
            run_def = wf.get("runParameters") or wf.get("lambda:runDefinition") or {}  # back-compat
            exp = self._experiment(expid, run_def)
            experiments.append(exp)

            ru_ref = (wf.get("object") or [{}])[0].get("@id")
            sample = sample_by_ruid.get(ru_ref)
            software = software_by_id.get((wf.get("instrument") or {}).get("@id"), {})
            product = by_id.get((wf.get("result") or [{}])[0].get("@id"), {})

            workflow = self._workflow(wf, software, expid)
            workflow_runs.append(workflow)

            files = self._data_files(product, by_id, workflow.id, expid, run_def.get("fileRoot"), warnings)
            data_files.extend(files)

            if sample is not None:
                experiment_sample_assoc.append(
                    ExperimentSampleAssociation(experiment_id=exp.id, sample_id=sample.id)
                )
            experiment_instrument_assoc.append(
                ExperimentInstrumentAssociation(experiment_id=exp.id, instrument_id=instrument.id)
            )
            workflow_experiment_assoc.append(
                WorkflowExperimentAssociation(workflow_id=workflow.id, experiment_id=exp.id)
            )
            workflow_output_assoc.extend(
                WorkflowOutputAssociation(
                    workflow_id=workflow.id, file_id=df.id, output_type=OutputTypeEnum.processed_data
                )
                for df in files
            )

        study_sample_assoc = [
            StudySampleAssociation(study_id=study.id, sample_id=s.id) for s in samples
        ]
        study_experiment_assoc = [
            StudyExperimentAssociation(study_id=study.id, experiment_id=e.id) for e in experiments
        ]
        study_workflow_assoc = [
            StudyWorkflowAssociation(study_id=study.id, workflow_id=w.id) for w in workflow_runs
        ]

        dataset = Dataset(
            id=dataset_id,
            title=root.get("name") or f"SSRL MX: {study_id}",
            studies=[study],
            instruments=[instrument],
            samples=samples or None,
            experiment_runs=experiments or None,
            workflow_runs=workflow_runs or None,
            data_files=data_files or None,
            study_sample_associations=study_sample_assoc or None,
            study_experiment_associations=study_experiment_assoc or None,
            experiment_sample_associations=experiment_sample_assoc or None,
            experiment_instrument_associations=experiment_instrument_assoc or None,
            study_workflow_associations=study_workflow_assoc or None,
            workflow_experiment_associations=workflow_experiment_assoc or None,
            workflow_output_associations=workflow_output_assoc or None,
        )

        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            source_url=str(crate_path.absolute()),
            raw_data={"@graph": graph},
        )

    def list_entries(self, directory: Path | str | None = None) -> list[str]:
        """List package directories (those containing ``ro-crate-metadata.json``) under ``directory``.

        If ``directory`` is itself a package, returns just that package.
        """
        if directory is None:
            return []
        directory = Path(directory)
        if (directory / "ro-crate-metadata.json").exists():
            return [str(directory)]
        return [str(p.parent) for p in sorted(directory.glob("*/ro-crate-metadata.json"))]

    # --- entity mappers -------------------------------------------------------------------------

    def _instrument(self, beamline_id: str | None) -> XRayInstrument:
        facility_enum = (
            FacilityEnum.Stanford_Synchrotron_Radiation_Lightsource
            if self.facility.upper() == "SSRL"
            else None
        )
        bl = beamline_id or "unknown"
        return XRayInstrument(
            id=f"ssrl-mx:instrument/{bl}",
            title=f"SSRL {bl}",
            instrument_code=bl,
            instrument_category=InstrumentCategoryEnum.SYNCHROTRON_BEAMLINE,
            facility_name=facility_enum,
            beamline_id=bl,
            source_type=XRaySourceTypeEnum.synchrotron,
            crystal_cooling_capability=True,
        )

    def _sample(self, raw_unit: dict[str, Any], dataset_id: str, root: dict[str, Any]) -> Sample:
        ru_id = raw_unit.get("rawUnitId") or re.sub(r"^#rawunit-", "", raw_unit.get("@id", "")) or "unknown"
        protein = root.get("lambda:proteinName")
        parts = []
        for label, key in (("Enzyme class", "lambda:enzymeClass"), ("UniProt", "lambda:uniprotId"),
                           ("PDB", "lambda:pdbCode")):
            if root.get(key):
                parts.append(f"{label}: {root[key]}")
        return Sample(
            id=f"{dataset_id}/sample/{ru_id}",
            sample_code=str(ru_id),
            sample_type=SampleTypeEnum.protein,
            title=f"Crystal sample {ru_id}" + (f" ({protein})" if protein else ""),
            protein_name=protein or None,
            organism=root.get("lambda:organism"),
            description="; ".join(parts) if parts else None,
        )

    def _experiment(self, expid: str, run_def: dict[str, Any]) -> ExperimentRun:
        # run_def is the CreateAction's runParameters (older crates: lambda:runDefinition) — crystals-play's
        # cleaned, camelCase run definition
        # (wavelength already in Angstroms — no energy conversion). Fields are best-effort/optional.
        def q(value: Any, unit: str) -> QuantityValue | None:
            return QuantityValue(numeric_value=value, unit=unit) if value is not None else None

        exposure = run_def.get("exposureTimeS")
        conditions = (
            ExperimentalConditions(exposure_time=q(exposure, "seconds")) if exposure is not None else None
        )
        file_root = run_def.get("fileRoot")
        # Sweep extent: crystals-play emits start + end angle; total rotation is derived when both present.
        start_angle = run_def.get("startAngleDeg")
        end_angle = run_def.get("endAngleDeg")
        total_rotation = (end_angle - start_angle) if (start_angle is not None and end_angle is not None) else None
        return ExperimentRun(
            id=f"{self.source_name}:experiment/{expid}",
            experiment_code=file_root or f"exp-{expid}",
            technique=TechniqueEnum.xray_crystallography,
            wavelength=q(run_def.get("wavelengthAngstrom"), "Angstroms"),
            energy=q(run_def.get("energyEv"), "eV"),
            detector_distance=q(run_def.get("detectorDistanceMm"), "mm"),
            oscillation_angle=q(run_def.get("oscillationDeg"), "degrees"),
            start_angle=q(start_angle, "degrees"),
            sweep_start=q(start_angle, "degrees"),
            sweep_end=q(end_angle, "degrees"),
            total_rotation=q(total_rotation, "degrees"),
            number_of_images=q(run_def.get("numberOfImages"), "images"),
            transmission=q(run_def.get("transmissionPercent"), "percent"),
            raw_data_location=run_def.get("directory"),
            experimental_conditions=conditions,
            description=(f"{file_root} data collection" if file_root else "X-ray data collection"),
        )

    def _workflow(self, wf: dict[str, Any], software: dict[str, Any], expid: str) -> WorkflowRun:
        def q(value: Any, unit: str) -> QuantityValue | None:
            return QuantityValue(numeric_value=value, unit=unit) if value is not None else None

        cell = wf.get("lambda:unitCell") or {}
        params = []
        if wf.get("lambda:completeness") is not None:
            params.append(f"Completeness={wf['lambda:completeness']:.1f}%")
        if wf.get("lambda:ccHalf") is not None:
            params.append(f"CC1/2={wf['lambda:ccHalf']:.3f}")
        if wf.get("lambda:meanISigma") is not None:
            params.append(f"I/σ={wf['lambda:meanISigma']:.1f}")

        sw_name = software.get("name") or "processing"
        slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", sw_name).strip("_") or "workflow"
        return WorkflowRun(
            id=f"{self.source_name}:workflow/{expid}",
            title=f"{sw_name.upper()} data processing",
            description=f"Automated data processing with {sw_name}",
            workflow_code=f"{slug.upper()}-scaling",
            workflow_type=WorkflowTypeEnum.scaling,
            software_name=sw_name,
            software_version=software.get("version"),
            space_group=wf.get("lambda:spaceGroup"),
            unit_cell_a=q(cell.get("a"), "Angstroms"),
            unit_cell_b=q(cell.get("b"), "Angstroms"),
            unit_cell_c=q(cell.get("c"), "Angstroms"),
            unit_cell_alpha=q(cell.get("alpha"), "degrees"),
            unit_cell_beta=q(cell.get("beta"), "degrees"),
            unit_cell_gamma=q(cell.get("gamma"), "degrees"),
            refinement_resolution_a=q(wf.get("lambda:resolutionAngstrom"), "Angstroms"),
            processing_parameters="; ".join(params) if params else None,
            processing_level=QuantityValue(numeric_value=2, unit="level"),
        )

    def _data_files(
        self,
        product: dict[str, Any],
        by_id: dict[str, Any],
        workflow_id: str,
        expid: str | None,
        dataset_name: str | None,
        warnings: list[str],
    ) -> list[DataFile]:
        """Map the File entities under a DerivedProduct.hasPart to DataFiles.

        Only files whose extension maps to a schema FileFormatEnum are described (the primary MTZ and any
        other recognised formats); auxiliary files (html/json provenance) are part of the package but not
        emitted as typed DataFiles.
        """
        # Auxiliary/provenance files live alongside the data products but are not themselves typed
        # DataFiles — skip them so only genuine outputs (the MTZ, etc.) are described.
        AUX_DIRS = ("provenance/", "beamline_state/")
        AUX_EXTS = {"json", "html", "htm", "txt", "log", "md", "csv"}
        files: list[DataFile] = []
        for ref in product.get("hasPart", []) or []:
            rel = ref.get("@id", "")
            fe = by_id.get(rel)
            if not fe or not _has_type(fe, "File"):
                continue
            if rel.startswith(AUX_DIRS):
                continue
            name = fe.get("name")
            if not name or "." not in name:
                continue
            ext = name.rsplit(".", 1)[-1].lower()
            if ext in AUX_EXTS:
                continue
            try:
                file_format = FileFormatEnum(ext)
            except ValueError:
                continue  # only describe files with a known schema data format (e.g. mtz)
            size = None
            if fe.get("contentSize") is not None:
                try:
                    size = QuantityValue(numeric_value=int(fe["contentSize"]), unit="bytes")
                except (TypeError, ValueError):
                    pass
            storage_uri = (
                LIMS_BUNDLE_URL_TEMPLATE.format(experiment_uuid=expid, dataset=dataset_name)
                if expid and dataset_name
                else None
            )
            data_type = DataTypeEnum.diffraction if ext == "mtz" else None
            files.append(
                DataFile(
                    id=f"{workflow_id}/output/{name}",
                    title=name,
                    file_name=name,
                    file_path=fe.get("@id"),
                    storage_uri=storage_uri,
                    file_format=file_format,
                    file_size_bytes=size,
                    checksum=fe.get("sha256"),
                    data_type=data_type,
                    file_role="final" if fe.get("additionalType") == "merged-reflections" else None,
                )
            )
        return files
