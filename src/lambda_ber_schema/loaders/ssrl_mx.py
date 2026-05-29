"""
SSRL macromolecular crystallography (MX) loader.

Loads data from SSRL's MX beamlines (BL12-2, BL12-1, BL9-2, etc.) into the
lambda-ber-schema. Combines three data sources:

1. DCSS beamline snapshot JSON (from dcss-dump-json) - data collection metadata
2. Sample metadata sidecar JSON - protein names, organism, UniProt/PDB references
3. Processing results sidecar JSON - autoproc/aimless output (space group, unit cell, statistics)

DCSS (Distributed Control System for Synchrotrons) is the control system used at SSRL
to operate the beamlines and capture experimental parameters during data collection.
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

# Conversion constant: wavelength (A) = 12398.419 / energy (eV)
PLANCK_HC_EV_ANGSTROM = 12398.419

# Canonical LIMS URLs for SSRL MX outputs. Points at the SLAC SMB dev LIMS
# (/dev/lims) for now; the production /lims service is locked to existing
# features until a planned upgrade. The URL pattern itself is stable -- when
# production is upgraded, swap "/dev/lims" for "/lims" here and in the schema
# prefix and regenerate examples.
#
# Two collections under each experiment:
#   .../bundle/{dataset}.tar  -- tar archive of every output file (this is
#                                what DataFile.storage_uri points at today)
#   .../files/{dataset}.{ext} -- individual canonical files served directly,
#                                e.g. .mtz, .html, .log (future)
#
# `{dataset}` is the DCSS file_root (e.g. "SA_x4") -- the sample-level name
# scientists use. The experiment UUID disambiguates multiple runs of the same
# sample.
#
# All DataFiles produced by the same experiment share the same storage_uri
# (the tar bundle); individual files are identified within the archive by
# `file_name`. `file_path` continues to hold the actual on-disk location
# for SLAC-internal use.
LIMS_BUNDLE_URL_TEMPLATE = (
    "https://smb.slac.stanford.edu/dev/lims/lambda/experiment/{experiment_uuid}/bundle/{dataset}.tar"
)

# No default sidecar paths. Callers (CLI / tests) must point the loader at
# whatever sidecar files they want to use. With no sidecars, the loader still
# produces a valid Dataset from the DCSS snapshot alone -- just without sample
# enrichment, processing statistics, or output-file metadata.


class SSRLMXLoader(BaseLoader):
    """
    Loader for SSRL macromolecular crystallography (MX) beamline data.

    Parses DCSS (Distributed Control System for Synchrotrons) snapshot JSON
    produced by dcss-dump-json, combined with optional sidecar metadata.

    Supports sidecar metadata files that enrich snapshots with:
    - Protein name and organism
    - UniProt and PDB references
    - Resolution and other processing statistics
    - Collaborator information

    Also supports a processing results sidecar that adds WorkflowRun entities
    with autoproc/aimless output (space group, unit cell, R-factors, etc.).

    Example:
        >>> loader = SSRLMXLoader(beamline_id="BL12-2", facility="SSRL")
        >>> result = loader.load("/path/to/snapshot.json")
        >>> result.dataset.id
        'ssrl-mx:BL12-2/snapshot'

        # With custom metadata file
        >>> loader = SSRLMXLoader(metadata_file="/path/to/metadata.json")
    """

    source_name = "ssrl-mx"
    base_url = None  # File-based, no API
    facility = "SSRL"  # Loader is SSRL-specific; DCSS snapshots only come from SSRL

    def __init__(
        self,
        metadata_file: Path | str | None = None,
        processing_results_file: Path | str | None = None,
    ):
        """
        Initialize the SSRL MX loader.

        The beamline is always read from each snapshot's ``beamlineID`` field
        at load time; there is no constructor-level beamline argument because
        a single loader instance handles snapshots from any SSRL MX beamline
        (BL12-2, BL12-1, BL9-2, ...). Likewise, ``facility`` is fixed to SSRL
        as a class attribute -- DCSS-formatted snapshots only come from SSRL.

        Args:
            metadata_file: Optional path to a sample-metadata sidecar JSON file
                          (protein names, UniProt/PDB refs, study UUIDs, etc.).
                          If None or missing, no metadata enrichment is applied.
            processing_results_file: Optional path to a processing-results sidecar
                          JSON file (autoproc/aimless statistics + output files).
                          If None or missing, no WorkflowRun / DataFile is created.
        """
        self._metadata_file = Path(metadata_file) if metadata_file else None
        self._metadata: dict[str, Any] | None = None
        self._processing_file = Path(processing_results_file) if processing_results_file else None
        self._processing_results: dict[str, Any] | None = None

    def _load_metadata(self) -> dict[str, Any]:
        """Load sidecar metadata file, caching the result."""
        if self._metadata is None:
            if self._metadata_file is not None and self._metadata_file.exists():
                self._metadata = json.loads(self._metadata_file.read_text())
            else:
                self._metadata = {}
        return self._metadata

    def _get_metadata_for_directory(self, directory: str | None) -> dict[str, Any] | None:
        """Look up metadata by data directory path."""
        if not directory:
            return None
        metadata = self._load_metadata()
        return metadata.get(directory)

    def _load_processing_results(self) -> dict[str, Any]:
        """Load processing results file, caching the result."""
        if self._processing_results is None:
            if self._processing_file is not None and self._processing_file.exists():
                self._processing_results = json.loads(self._processing_file.read_text())
            else:
                self._processing_results = {}
        return self._processing_results

    def _get_processing_for_directory(self, directory: str | None) -> dict[str, Any] | None:
        """Look up processing results by data directory path."""
        if not directory:
            return None
        results = self._load_processing_results()
        return results.get(directory)

    def load(self, identifier: str) -> LoaderResult:
        """
        Load a DCSS snapshot by file path.

        Args:
            identifier: Path to the JSON snapshot file

        Returns:
            LoaderResult with populated Dataset

        Raises:
            FileNotFoundError: If the snapshot file doesn't exist
            ValueError: If the JSON is invalid
        """
        snapshot_path = Path(identifier)
        if not snapshot_path.exists():
            raise FileNotFoundError(f"Snapshot file not found: {identifier}")

        raw = json.loads(snapshot_path.read_text())
        warnings: list[str] = []

        # Beamline ID comes from the snapshot itself; DCSS always writes a
        # beamlineID field. Bail out explicitly rather than silently inventing
        # one if a malformed snapshot is missing it.
        beamline_id = self._get_beamline_id(raw)
        if not beamline_id:
            raise ValueError(
                f"DCSS snapshot {snapshot_path} has no `beamlineID`; "
                "cannot determine the source beamline."
            )
        snapshot_name = snapshot_path.stem

        # Build the dataset
        dataset_id = self.make_id(f"{beamline_id}/{snapshot_name}")

        # Create instrument
        instrument = self._create_instrument(raw, beamline_id, warnings)

        # Create experiment runs (only collecting runs)
        # Do this first to get directory paths for metadata lookup
        experiments = self._create_experiment_runs(raw, dataset_id, warnings)

        # Get metadata from first collecting run's directory
        run_metadata = None
        if experiments:
            first_run_dir = experiments[0].raw_data_location
            run_metadata = self._get_metadata_for_directory(first_run_dir)

        # Create sample from crystalStatus, enriched with sidecar metadata
        sample = self._create_sample(raw, dataset_id, run_metadata, warnings)

        # Enrich experiment runs with per-run metadata when available.
        experiments = [
            self._enrich_experiment_with_metadata(
                exp,
                self._get_metadata_for_directory(exp.raw_data_location),
                warnings,
            )
            for exp in experiments
        ]

        # Get processing results and create WorkflowRun + DataFile entities
        workflow_runs: list[WorkflowRun] = []
        data_files: list[DataFile] = []
        workflow_output_associations: list[WorkflowOutputAssociation] = []
        workflow_experiment_associations: list[WorkflowExperimentAssociation] = []
        processing_results = None
        if experiments:
            first_experiment = experiments[0]
            first_run_dir = first_experiment.raw_data_location
            processing_results = self._get_processing_for_directory(first_run_dir)
            if processing_results:
                workflow_run = self._create_workflow_run(
                    processing_results, dataset_id, warnings
                )
                workflow_runs.append(workflow_run)

                experiment_uuid = (
                    run_metadata.get("experiment_id") if run_metadata else None
                )
                files = self._create_data_files(
                    processing_results,
                    workflow_run.id,
                    warnings,
                    experiment_uuid=experiment_uuid,
                    dataset_name=self._get_first_collecting_file_root(raw) or snapshot_name,
                )
                data_files.extend(files)
                workflow_output_associations.extend(
                    WorkflowOutputAssociation(
                        workflow_id=workflow_run.id,
                        file_id=df.id,
                        output_type=OutputTypeEnum.processed_data,
                    )
                    for df in files
                )
                workflow_experiment_associations.append(
                    WorkflowExperimentAssociation(
                        workflow_id=workflow_run.id,
                        experiment_id=first_experiment.id,
                    )
                )

        # Create study: prefer UUID + title + keywords from sidecar metadata, else
        # fall back to a snapshot-derived id. When the metadata supplies a
        # study_id, multiple snapshots that share it can later be merged into a
        # single Study downstream.
        study_uuid = run_metadata.get("study_id") if run_metadata else None
        study_title = run_metadata.get("study_title") if run_metadata else None
        study_keywords = run_metadata.get("study_keywords") if run_metadata else None
        study = Study(
            id=f"{self.source_name}:study/{study_uuid}" if study_uuid else f"{dataset_id}/study",
            title=study_title or f"SSRL MX data collection from {beamline_id}",
            keywords=study_keywords or None,
        )

        # Create association tables
        study_sample_associations = [
            StudySampleAssociation(study_id=study.id, sample_id=sample.id)
        ]
        study_experiment_associations = [
            StudyExperimentAssociation(study_id=study.id, experiment_id=exp.id)
            for exp in experiments
        ]
        experiment_sample_associations = [
            ExperimentSampleAssociation(experiment_id=exp.id, sample_id=sample.id)
            for exp in experiments
        ]
        experiment_instrument_associations = [
            ExperimentInstrumentAssociation(
                experiment_id=exp.id, instrument_id=instrument.id
            )
            for exp in experiments
        ]

        # Create workflow associations
        study_workflow_associations = [
            StudyWorkflowAssociation(study_id=study.id, workflow_id=wf.id)
            for wf in workflow_runs
        ]
        # Create dataset with flat entity collections
        dataset = Dataset(
            id=dataset_id,
            title=f"SSRL MX: {beamline_id}/{snapshot_name}",
            studies=[study],
            instruments=[instrument],
            samples=[sample],
            experiment_runs=experiments,
            workflow_runs=workflow_runs if workflow_runs else None,
            data_files=data_files if data_files else None,
            study_sample_associations=study_sample_associations,
            study_experiment_associations=study_experiment_associations,
            experiment_sample_associations=experiment_sample_associations,
            experiment_instrument_associations=experiment_instrument_associations,
            study_workflow_associations=study_workflow_associations if study_workflow_associations else None,
            workflow_experiment_associations=workflow_experiment_associations if workflow_experiment_associations else None,
            workflow_output_associations=workflow_output_associations if workflow_output_associations else None,
        )

        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            source_url=str(snapshot_path.absolute()),
            raw_data=raw,
        )

    def list_entries(
        self,
        directory: Path | str | None = None,
    ) -> list[str]:
        """
        List available snapshot JSON files in a directory.

        Args:
            directory: Directory to search for .json files.
                      Defaults to tests/data/raw/beamline-snapshots

        Returns:
            List of JSON file paths that can be passed to load()
        """
        if directory is None:
            # Default to the standard snapshot directory
            directory = (
                Path(__file__).parent.parent.parent.parent
                / "tests"
                / "data"
                / "raw"
                / "beamline-snapshots"
            )
        else:
            directory = Path(directory)

        if not directory.exists():
            return []

        return [str(p) for p in sorted(directory.glob("*.json"))]

    def _get_beamline_id(self, raw: dict[str, Any]) -> str | None:
        """Extract beamline ID from snapshot."""
        beamline = raw.get("beamlineID", {})
        if isinstance(beamline, dict):
            return beamline.get("value")
        return None

    def _get_first_collecting_file_root(self, raw: dict[str, Any]) -> str | None:
        """Return the DCSS file_root of the first run with status='collecting'.

        This is the sample-level name scientists use (e.g. 'SA_x4'). It's used
        to build the canonical LIMS URL for the experiment's output bundle.
        """
        for i in range(17):
            run = raw.get(f"run{i}")
            if isinstance(run, dict) and run.get("status") == "collecting":
                file_root = run.get("file_root")
                if file_root:
                    return file_root
        return None

    def _create_instrument(
        self,
        raw: dict[str, Any],
        beamline_id: str,
        warnings: list[str],
    ) -> XRayInstrument:
        """Create XRayInstrument from detector and beamline info."""
        # Get detector type
        detector_type = raw.get("detectorType", {})
        detector_model = None
        if isinstance(detector_type, dict):
            detector_model = detector_type.get("value")

        # Get detector status for wavelength and threshold
        detector_status = raw.get("detectorStatus", {})
        wavelength = None
        if isinstance(detector_status, dict) and detector_status.get("WAVELENGTH"):
            wavelength = QuantityValue(
                numeric_value=detector_status["WAVELENGTH"],
                unit="Angstroms",
            )

        # Map facility name to enum
        facility_enum = None
        if self.facility.upper() == "SSRL":
            facility_enum = FacilityEnum.Stanford_Synchrotron_Radiation_Lightsource

        return XRayInstrument(
            id=f"ssrl-mx:instrument/{beamline_id}",
            title=f"SSRL {beamline_id}",
            instrument_code=beamline_id,
            instrument_category=InstrumentCategoryEnum.SYNCHROTRON_BEAMLINE,
            facility_name=facility_enum,
            beamline_id=beamline_id,
            source_type=XRaySourceTypeEnum.synchrotron,
            detector_model=detector_model,
            detector_manufacturer="Dectris" if detector_model and "EIGER" in detector_model else None,
            crystal_cooling_capability=True,
        )

    def _create_sample(
        self,
        raw: dict[str, Any],
        dataset_id: str,
        metadata: dict[str, Any] | None,
        warnings: list[str],
    ) -> Sample:
        """Create Sample from crystalStatus device, enriched with sidecar metadata."""
        crystal_status = raw.get("crystalStatus", {})

        # Extract sample info from DCSS
        sample_id = crystal_status.get("sampleID")
        current_port = crystal_status.get("current_port")
        protein = crystal_status.get("protein")

        # Build sample code from available info
        if current_port:
            sample_code = current_port
        elif sample_id:
            sample_code = f"SID-{sample_id}"
        else:
            sample_code = "unknown"
            warnings.append("No sample identifier found in crystalStatus")

        # Enrich with sidecar metadata if available
        protein_name = protein
        organism = None
        description_parts = []

        if metadata:
            # Prefer metadata protein_name over DCSS protein field
            protein_name = metadata.get("protein_name") or protein
            # Organism must be a uriorcurie (e.g. NCBITaxon:909626) to satisfy
            # the schema; the human-readable species name lives in organism_label
            # and gets surfaced in the description below.
            organism = metadata.get("organism")

            # Build rich description
            if metadata.get("organism_label"):
                description_parts.append(f"Organism: {metadata['organism_label']}")
            if metadata.get("enzyme_class"):
                description_parts.append(f"Enzyme class: {metadata['enzyme_class']}")
            if metadata.get("uniprot_id"):
                description_parts.append(f"UniProt: {metadata['uniprot_id']}")
            if metadata.get("pdb_code"):
                description_parts.append(f"PDB: {metadata['pdb_code']}")

        if sample_id:
            description_parts.append(f"Sample ID: {sample_id}")
        if current_port:
            description_parts.append(f"Port: {current_port}")

        return Sample(
            id=f"{dataset_id}/sample",
            sample_code=sample_code,
            sample_type=SampleTypeEnum.protein,  # Default to protein for MX
            title=f"Crystal sample {sample_code}" + (f" ({protein_name})" if protein_name else ""),
            protein_name=protein_name if protein_name else None,
            organism=organism,
            description="; ".join(description_parts) if description_parts else None,
        )

    def _enrich_experiment_with_metadata(
        self,
        experiment: ExperimentRun,
        metadata: dict[str, Any] | None,
        warnings: list[str],
    ) -> ExperimentRun:
        """Enrich a single experiment run with its matching sidecar metadata."""
        if not metadata:
            return experiment

        # If metadata supplies a stable experiment UUID, use it as the ExperimentRun.id
        # in CURIE form (ssrl-mx:experiment/<UUID>), matching how other loaders namespace
        # their IDs (e.g. emsl:transaction_NNNN). Fall back to the derived path-style ID.
        experiment_uuid = metadata.get("experiment_id")
        override_id = (
            f"{self.source_name}:experiment/{experiment_uuid}" if experiment_uuid else None
        )

        quality_metrics = None
        if metadata.get("resolution_angstrom"):
            quality_metrics = QualityMetrics(
                resolution=QuantityValue(
                    numeric_value=metadata["resolution_angstrom"],
                    unit="Angstroms",
                )
            )

        return ExperimentRun(
            id=override_id or experiment.id,
            experiment_code=experiment.experiment_code,
            technique=experiment.technique,
            wavelength=experiment.wavelength,
            detector_distance=experiment.detector_distance,
            oscillation_angle=experiment.oscillation_angle,
            start_angle=experiment.start_angle,
            number_of_images=experiment.number_of_images,
            transmission=experiment.transmission,
            raw_data_location=experiment.raw_data_location,
            experimental_conditions=experiment.experimental_conditions,
            quality_metrics=quality_metrics,
            description=experiment.description,
        )

    def _create_experiment_runs(
        self,
        raw: dict[str, Any],
        dataset_id: str,
        warnings: list[str],
    ) -> list[ExperimentRun]:
        """
        Create ExperimentRun entries from run0-run16 devices.

        Only includes runs where status = "collecting".
        """
        runs = []

        for i in range(17):  # run0 through run16
            run_key = f"run{i}"
            run_data = raw.get(run_key)

            if not run_data or not isinstance(run_data, dict):
                continue

            status = run_data.get("status")
            if status != "collecting":
                continue

            experiment = self._parse_run(run_data, i, dataset_id, warnings)
            runs.append(experiment)

        if not runs:
            warnings.append("No actively collecting runs found in snapshot")

        return runs

    def _parse_run(
        self,
        run_data: dict[str, Any],
        run_index: int,
        dataset_id: str,
        warnings: list[str],
    ) -> ExperimentRun:
        """Parse a single run device into an ExperimentRun."""
        # Get energy and convert to wavelength
        energy_ev = run_data.get("energy1_eV")
        wavelength = None
        if energy_ev and energy_ev > 0:
            wavelength_angstrom = self._energy_to_wavelength(energy_ev)
            wavelength = QuantityValue(
                numeric_value=wavelength_angstrom,
                unit="Angstroms",
            )

        # Get detector distance
        detector_distance = None
        if run_data.get("distance_mm"):
            detector_distance = QuantityValue(
                numeric_value=run_data["distance_mm"],
                unit="mm",
            )

        # Get oscillation angle (delta)
        oscillation_angle = None
        if run_data.get("delta"):
            oscillation_angle = QuantityValue(
                numeric_value=run_data["delta"],
                unit="degrees",
            )

        # Get start angle
        start_angle = None
        if run_data.get("start_angle_deg") is not None:
            start_angle = QuantityValue(
                numeric_value=run_data["start_angle_deg"],
                unit="degrees",
            )

        # Calculate number of images from start/end frame
        number_of_images = None
        start_frame = run_data.get("start_frame")
        end_frame = run_data.get("end_frame")
        if start_frame is not None and end_frame is not None:
            number_of_images = QuantityValue(
                numeric_value=end_frame - start_frame + 1,
                unit="images",
            )

        # Get transmission (attenuation_percent is transmission, not attenuation)
        transmission = None
        if run_data.get("attenuation_percent") is not None:
            transmission = QuantityValue(
                numeric_value=run_data["attenuation_percent"],
                unit="percent",
            )

        # Get experimental conditions from global temperature device
        experimental_conditions = self._get_experimental_conditions(
            run_data, warnings
        )

        return ExperimentRun(
            id=f"{dataset_id}/run{run_index}",
            experiment_code=f"DCSS-run{run_index}",
            technique=TechniqueEnum.xray_crystallography,
            wavelength=wavelength,
            detector_distance=detector_distance,
            oscillation_angle=oscillation_angle,
            start_angle=start_angle,
            number_of_images=number_of_images,
            transmission=transmission,
            raw_data_location=run_data.get("directory"),
            experimental_conditions=experimental_conditions,
            description=(
                f"Run {run_index}: {run_data.get('file_root', 'unknown')} "
                f"({run_data.get('start_angle_deg', 0)}-{run_data.get('end_angle_deg', 0)} deg)"
            ),
        )

    def _get_experimental_conditions(
        self,
        run_data: dict[str, Any],
        warnings: list[str],
    ) -> ExperimentalConditions | None:
        """Extract experimental conditions, primarily exposure time."""
        exposure_time = run_data.get("exposure_time_s")
        if exposure_time is None:
            return None

        return ExperimentalConditions(
            exposure_time=QuantityValue(
                numeric_value=exposure_time,
                unit="seconds",
            ),
        )

    @staticmethod
    def _energy_to_wavelength(energy_ev: float) -> float:
        """
        Convert X-ray energy in eV to wavelength in Angstroms.

        Uses the relationship: wavelength (A) = 12398.419 / energy (eV)

        Args:
            energy_ev: Energy in electron volts

        Returns:
            Wavelength in Angstroms
        """
        return PLANCK_HC_EV_ANGSTROM / energy_ev

    def _create_workflow_run(
        self,
        processing: dict[str, Any],
        dataset_id: str,
        warnings: list[str],
    ) -> WorkflowRun:
        """
        Create a WorkflowRun from processing results (autoproc/aimless output).

        Args:
            processing: Processing results dictionary
            dataset_id: Parent dataset ID for generating workflow ID
            warnings: List to append warnings to

        Returns:
            WorkflowRun entity with scaling/integration results
        """
        pipeline = processing.get("pipeline", "autoproc")
        pipeline_version = processing.get("pipeline_version")

        # Extract unit cell parameters
        unit_cell = processing.get("unit_cell", {})
        unit_cell_a = None
        unit_cell_b = None
        unit_cell_c = None
        unit_cell_alpha = None
        unit_cell_beta = None
        unit_cell_gamma = None

        if unit_cell.get("a") is not None:
            unit_cell_a = QuantityValue(numeric_value=unit_cell["a"], unit="Angstroms")
        if unit_cell.get("b") is not None:
            unit_cell_b = QuantityValue(numeric_value=unit_cell["b"], unit="Angstroms")
        if unit_cell.get("c") is not None:
            unit_cell_c = QuantityValue(numeric_value=unit_cell["c"], unit="Angstroms")
        if unit_cell.get("alpha") is not None:
            unit_cell_alpha = QuantityValue(numeric_value=unit_cell["alpha"], unit="degrees")
        if unit_cell.get("beta") is not None:
            unit_cell_beta = QuantityValue(numeric_value=unit_cell["beta"], unit="degrees")
        if unit_cell.get("gamma") is not None:
            unit_cell_gamma = QuantityValue(numeric_value=unit_cell["gamma"], unit="degrees")

        # Extract resolution
        resolution = processing.get("resolution", {})
        refinement_resolution = None
        if isinstance(resolution, dict) and "overall" in resolution:
            # resolution.overall is [low, high], we want high resolution
            res_range = resolution["overall"]
            if isinstance(res_range, (list, tuple)) and len(res_range) >= 2:
                refinement_resolution = QuantityValue(
                    numeric_value=res_range[1],  # High resolution limit
                    unit="Angstroms",
                )

        # Build processing parameters summary
        params = []
        if processing.get("rmerge", {}).get("overall"):
            params.append(f"Rmerge={processing['rmerge']['overall']:.3f}")
        if processing.get("completeness", {}).get("overall"):
            params.append(f"Completeness={processing['completeness']['overall']:.1f}%")
        if processing.get("cc_half", {}).get("overall"):
            params.append(f"CC1/2={processing['cc_half']['overall']:.3f}")
        if processing.get("mean_i_sigma", {}).get("overall"):
            params.append(f"I/σ={processing['mean_i_sigma']['overall']:.1f}")

        # Sanitize pipeline name for use as a URI segment
        pipeline_slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", pipeline).strip("_") or "workflow"

        return WorkflowRun(
            id=f"{dataset_id}/workflow/{pipeline_slug}",
            title=f"{pipeline.upper()} data processing",
            description=f"Automated data processing with {pipeline}",
            workflow_code=f"{pipeline_slug.upper()}-scaling",
            workflow_type=WorkflowTypeEnum.scaling,
            software_name=pipeline,
            software_version=pipeline_version,
            indexer_module=processing.get("indexer"),
            scaler_module=processing.get("scaler"),
            space_group=processing.get("space_group"),
            unit_cell_a=unit_cell_a,
            unit_cell_b=unit_cell_b,
            unit_cell_c=unit_cell_c,
            unit_cell_alpha=unit_cell_alpha,
            unit_cell_beta=unit_cell_beta,
            unit_cell_gamma=unit_cell_gamma,
            refinement_resolution_a=refinement_resolution,
            processing_parameters="; ".join(params) if params else None,
            processing_level=QuantityValue(numeric_value=2, unit="level"),
        )

    def _create_data_files(
        self,
        processing: dict[str, Any],
        workflow_id: str,
        warnings: list[str],
        experiment_uuid: str | None = None,
        dataset_name: str | None = None,
    ) -> list[DataFile]:
        """Create DataFile entities from the processing sidecar's output_files list.

        If both ``experiment_uuid`` and ``dataset_name`` are supplied, every
        DataFile gets the same ``storage_uri`` pointing at the SLAC SMB LIMS
        bundle endpoint (a tar archive containing all of this experiment's
        output files). Individual files are identified within the archive by
        ``file_name``. ``file_path`` continues to hold the actual on-disk
        location.
        """
        files = []
        for entry in processing.get("output_files", []) or []:
            file_name = entry.get("file_name")
            file_format_raw = entry.get("file_format")
            if not file_name or not file_format_raw:
                warnings.append(
                    f"Skipping output_file entry missing file_name or file_format: {entry}"
                )
                continue

            # Coerce enum-typed fields, warning if a value isn't valid
            try:
                file_format = FileFormatEnum(file_format_raw)
            except ValueError:
                warnings.append(
                    f"Unknown file_format '{file_format_raw}' for {file_name}; skipping"
                )
                continue

            data_type = None
            if entry.get("data_type"):
                try:
                    data_type = DataTypeEnum(entry["data_type"])
                except ValueError:
                    warnings.append(
                        f"Unknown data_type '{entry['data_type']}' for {file_name}"
                    )

            file_size = None
            if entry.get("file_size_bytes") is not None:
                file_size = QuantityValue(
                    numeric_value=entry["file_size_bytes"],
                    unit="bytes",
                )

            storage_uri = None
            if experiment_uuid and dataset_name:
                storage_uri = LIMS_BUNDLE_URL_TEMPLATE.format(
                    experiment_uuid=experiment_uuid,
                    dataset=dataset_name,
                )

            files.append(
                DataFile(
                    id=f"{workflow_id}/output/{file_name}",
                    title=file_name,
                    file_name=file_name,
                    file_path=entry.get("file_path"),
                    storage_uri=storage_uri,
                    file_format=file_format,
                    file_size_bytes=file_size,
                    checksum=entry.get("checksum"),
                    creation_date=entry.get("creation_date"),
                    data_type=data_type,
                    file_role=entry.get("file_role"),
                )
            )
        return files
