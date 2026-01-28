"""
PDB (Protein Data Bank) loader.

API Documentation: https://data.rcsb.org/
"""

import json
from typing import Any

import requests

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.pydantic import (
    DataFile,
    Dataset,
    ExperimentInstrumentAssociation,
    ExperimentRun,
    ExperimentSampleAssociation,
    FileFormatEnum,
    QualityMetrics,
    QuantityValue,
    Sample,
    SampleTypeEnum,
    Study,
    StudyExperimentAssociation,
    StudySampleAssociation,
    TechniqueEnum,
    WorkflowExperimentAssociation,
    WorkflowRun,
    WorkflowTypeEnum,
    XRayInstrument,
)


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
        # Normalize to uppercase
        entry_id = entry_id.upper()

        # Fetch entry data
        entry_data = self._fetch_entry(entry_id)
        warnings: list[str] = []

        # Fetch polymer entities for sample info
        polymer_entities = self._fetch_polymer_entities(
            entry_id, entry_data, warnings)

        # Build the dataset
        dataset_id = self.make_id(entry_id)
        source_url = f"https://www.rcsb.org/structure/{entry_id}"

        # Determine experimental method
        technique = self._determine_technique(entry_data, warnings)

        # Create instrument (if X-ray or relevant technique)
        instrument = self._create_instrument(entry_data, entry_id, warnings)

        # Create samples from polymer entities
        samples = self._create_samples(
            polymer_entities, entry_data, entry_id, warnings
        )

        # Create experiment run
        experiment = self._create_experiment_run(
            entry_data, entry_id, technique, warnings
        )

        # Create data files
        data_files = self._create_data_files(entry_data, entry_id, warnings)

        # Create workflow runs (for refinement)
        workflows = self._create_workflow_runs(entry_data, entry_id, warnings)

        # Create study
        title = entry_data.get("struct", {}).get(
            "title", f"PDB Entry {entry_id}")
        study = Study(
            id=f"{dataset_id}/study",
            title=title,
        )

        # Create association tables
        study_sample_associations = [
            StudySampleAssociation(study_id=study.id, sample_id=s.id) for s in samples
        ]
        study_experiment_associations = [
            StudyExperimentAssociation(
                study_id=study.id, experiment_id=experiment.id)
        ]
        experiment_sample_associations = [
            ExperimentSampleAssociation(
                experiment_id=experiment.id, sample_id=s.id)
            for s in samples
        ]
        experiment_instrument_associations = [
            ExperimentInstrumentAssociation(
                experiment_id=experiment.id, instrument_id=instrument.id
            )
        ]
        workflow_experiment_associations = [
            WorkflowExperimentAssociation(
                workflow_id=wf.id, experiment_id=experiment.id
            )
            for wf in workflows
        ]

        # Create dataset
        dataset = Dataset(
            id=dataset_id,
            title=title,
            studies=[study],
            instruments=[instrument],
            samples=samples,
            experiment_runs=[experiment],
            workflow_runs=workflows,
            data_files=data_files,
            study_sample_associations=study_sample_associations,
            study_experiment_associations=study_experiment_associations,
            experiment_sample_associations=experiment_sample_associations,
            experiment_instrument_associations=experiment_instrument_associations,
            workflow_experiment_associations=workflow_experiment_associations,
        )

        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            source_url=source_url,
            raw_data={"entry": entry_data,
                      "polymer_entities": polymer_entities},
        )

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
        # Build search query
        query: dict[str, Any] = {"type": "terminal", "service": "text"}

        if experimental_method:
            # Map common abbreviations to full method names
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

        # Handle 204 No Content (no results)
        if status_code == 204 or not text:
            return []

        payload = json.loads(text)
        return [hit["identifier"] for hit in payload.get("result_set", [])]

    def _fetch_entry(self, entry_id: str) -> dict[str, Any]:
        """Fetch entry data from PDB API."""
        cache_key = f"pdb/{entry_id}"

        def fetch() -> dict[str, Any]:
            url = f"{self.base_url}/core/entry/{entry_id}"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()

        return self.cache.get_or_fetch(cache_key, fetch)

    def _fetch_polymer_entities(
        self, entry_id: str, entry_data: dict[str, Any], warnings: list[str]
    ) -> list[dict[str, Any]]:
        """Fetch polymer entity data for each entity in the entry."""
        entities = []
        container = entry_data.get("rcsb_entry_container_identifiers", {})
        polymer_ids = container.get("polymer_entity_ids", [])

        for entity_id in polymer_ids:
            cache_key = f"pdb/{entry_id}/polymer_entity/{entity_id}"

            def fetch(eid: str = entity_id) -> dict[str, Any]:
                url = f"{self.base_url}/core/polymer_entity/{entry_id}/{eid}"
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                return response.json()

            entity_data = self.cache.get_or_fetch(cache_key, fetch)
            entities.append(entity_data)

        return entities

    def _determine_technique(
        self, entry_data: dict[str, Any], warnings: list[str]
    ) -> TechniqueEnum:
        """Determine experimental technique from entry data."""
        exptl = entry_data.get("exptl", [])
        if not exptl:
            warnings.append("No experimental method found")
            return TechniqueEnum.xray_crystallography

        method = exptl[0].get("method", "").upper()

        technique_map = {
            "X-RAY DIFFRACTION": TechniqueEnum.xray_crystallography,
            "ELECTRON MICROSCOPY": TechniqueEnum.cryo_em,
            "ELECTRON CRYSTALLOGRAPHY": TechniqueEnum.electron_microscopy,
            "SOLUTION NMR": TechniqueEnum.saxs,  # No NMR in schema, fallback
            "SOLID-STATE NMR": TechniqueEnum.saxs,  # No NMR in schema, fallback
            "NEUTRON DIFFRACTION": TechniqueEnum.sans,
        }

        technique = technique_map.get(method)
        if not technique:
            warnings.append(
                f"Unknown experimental method: {method}, defaulting to X-ray")
            technique = TechniqueEnum.xray_crystallography

        return technique

    def _create_instrument(
        self, entry_data: dict[str, Any], entry_id: str, warnings: list[str]
    ) -> XRayInstrument:
        """Create XRayInstrument from PDB data."""
        # Extract diffraction source info if available
        diffrn_source = entry_data.get("diffrn_source", [{}])[
            0] if entry_data.get("diffrn_source") else {}
        diffrn_detector = entry_data.get("diffrn_detector", [{}])[
            0] if entry_data.get("diffrn_detector") else {}

        source = diffrn_source.get("source", "Unknown")
        pdbx_synchrotron_site = diffrn_source.get("pdbx_synchrotron_site", "")
        pdbx_synchrotron_beamline = diffrn_source.get(
            "pdbx_synchrotron_beamline", "")

        if pdbx_synchrotron_site and pdbx_synchrotron_beamline:
            instrument_code = f"{pdbx_synchrotron_site}-{pdbx_synchrotron_beamline}"
            title = f"{pdbx_synchrotron_site} {pdbx_synchrotron_beamline}"
        else:
            instrument_code = f"PDB-{entry_id}"
            title = source or f"Instrument for {entry_id}"

        detector_type = diffrn_detector.get("type")

        return XRayInstrument(
            id=f"pdb:instrument/{instrument_code.replace(' ', '_').replace('/', '_')}",
            title=title,
            instrument_code=instrument_code.replace(" ", "-"),
            description=f"Detector: {detector_type}" if detector_type else None,
            detector_model=detector_type,
        )

    def _create_samples(
        self,
        polymer_entities: list[dict[str, Any]],
        entry_data: dict[str, Any],
        entry_id: str,
        warnings: list[str],
    ) -> list[Sample]:
        """Create Sample objects from polymer entities."""
        samples = []

        for i, entity in enumerate(polymer_entities, 1):
            entity_poly = entity.get("entity_poly", {})
            source_organisms = entity.get("rcsb_entity_source_organism", [])

            # Determine sample type
            polymer_type = entity_poly.get(
                "rcsb_entity_polymer_type", "").lower()
            if "protein" in polymer_type:
                sample_type = SampleTypeEnum.protein
            elif "dna" in polymer_type or "rna" in polymer_type:
                sample_type = SampleTypeEnum.nucleic_acid
            else:
                sample_type = SampleTypeEnum.complex

            # Get organism
            organism = None
            if source_organisms:
                organism = source_organisms[0].get("scientific_name")

            # Get molecular weight from entity (API returns in kDa)
            mw = entity.get("rcsb_polymer_entity", {}).get("formula_weight")
            molecular_weight = None
            if mw:
                molecular_weight = QuantityValue(
                    numeric_value=round(mw, 2),
                    unit="kDa",
                )

            # Get protein name
            protein_name = entity.get(
                "rcsb_polymer_entity", {}).get("pdbx_description")

            samples.append(
                Sample(
                    id=f"pdb:{entry_id}/sample/{i}",
                    sample_code=f"PDB-{entry_id}-{i}",
                    sample_type=sample_type,
                    title=protein_name,
                    protein_name=protein_name,
                    organism=organism,
                    molecular_weight=molecular_weight,
                    description=(
                        f"Sequence length: {entity_poly.get('rcsb_sample_sequence_length')}"
                        if entity_poly.get("rcsb_sample_sequence_length")
                        else None
                    ),
                )
            )

        # If no polymer entities, create a minimal sample
        if not samples:
            samples.append(
                Sample(
                    id=f"pdb:{entry_id}/sample/1",
                    sample_code=f"PDB-{entry_id}-1",
                    sample_type=SampleTypeEnum.complex,
                    title=entry_data.get("struct", {}).get("title"),
                )
            )

        return samples

    def _create_experiment_run(
        self,
        entry_data: dict[str, Any],
        entry_id: str,
        technique: TechniqueEnum,
        warnings: list[str],
    ) -> ExperimentRun:
        """Create ExperimentRun from PDB data."""
        # Get resolution
        rcsb_info = entry_data.get("rcsb_entry_info", {})
        resolution_values = rcsb_info.get("resolution_combined", [])

        resolution = None
        if resolution_values:
            resolution = QuantityValue(
                numeric_value=resolution_values[0],
                unit="Angstroms",
            )

        # Get wavelength
        diffrn_source = entry_data.get("diffrn_source", [{}])[
            0] if entry_data.get("diffrn_source") else {}
        wavelength = None
        pdbx_wavelength = diffrn_source.get("pdbx_wavelength")
        if pdbx_wavelength:
            wavelength = QuantityValue(
                numeric_value=pdbx_wavelength,
                unit="Angstroms",
            )

        # Get quality metrics
        quality_metrics = self._create_quality_metrics(entry_data, warnings)

        # Get experiment date
        accession_info = entry_data.get("rcsb_accession_info", {})
        deposit_date = accession_info.get("deposit_date")
        if deposit_date:
            # Extract just the date part
            deposit_date = deposit_date.split("T")[0]

        return ExperimentRun(
            id=f"pdb:{entry_id}/experiment",
            experiment_code=f"PDB-{entry_id}-EXP",
            technique=technique,
            experiment_date=deposit_date,
            wavelength=wavelength,
            quality_metrics=quality_metrics,
        )

    def _create_quality_metrics(
        self, entry_data: dict[str, Any], warnings: list[str]
    ) -> QualityMetrics:
        """Create QualityMetrics from PDB refinement data."""
        refine = entry_data.get("refine", [{}])[
            0] if entry_data.get("refine") else {}
        cell = entry_data.get("cell", {})
        symmetry = entry_data.get("symmetry", {})
        rcsb_info = entry_data.get("rcsb_entry_info", {})
        vrpt_geom = entry_data.get("pdbx_vrpt_summary_geometry", [{}])[
            0] if entry_data.get("pdbx_vrpt_summary_geometry") else {}

        # Resolution
        resolution_values = rcsb_info.get("resolution_combined", [])
        resolution = None
        if resolution_values:
            resolution = QuantityValue(
                numeric_value=resolution_values[0], unit="Angstroms")

        # R-factors
        r_work = None
        if refine.get("ls_rfactor_rwork"):
            r_work = QuantityValue(
                numeric_value=refine["ls_rfactor_rwork"], unit="dimensionless")

        r_free = None
        if refine.get("ls_rfactor_rfree"):
            r_free = QuantityValue(
                numeric_value=refine["ls_rfactor_rfree"], unit="dimensionless")

        # Space group
        space_group = symmetry.get("space_group_name_hm")

        # Unit cell parameters
        unit_cell_a = None
        if cell.get("length_a"):
            unit_cell_a = QuantityValue(
                numeric_value=cell["length_a"], unit="Angstroms")

        unit_cell_b = None
        if cell.get("length_b"):
            unit_cell_b = QuantityValue(
                numeric_value=cell["length_b"], unit="Angstroms")

        unit_cell_c = None
        if cell.get("length_c"):
            unit_cell_c = QuantityValue(
                numeric_value=cell["length_c"], unit="Angstroms")

        unit_cell_alpha = None
        if cell.get("angle_alpha"):
            unit_cell_alpha = QuantityValue(
                numeric_value=cell["angle_alpha"], unit="degrees")

        unit_cell_beta = None
        if cell.get("angle_beta"):
            unit_cell_beta = QuantityValue(
                numeric_value=cell["angle_beta"], unit="degrees")

        unit_cell_gamma = None
        if cell.get("angle_gamma"):
            unit_cell_gamma = QuantityValue(
                numeric_value=cell["angle_gamma"], unit="degrees")

        # Geometry validation
        clashscore = None
        if vrpt_geom.get("clashscore"):
            clashscore = QuantityValue(
                numeric_value=vrpt_geom["clashscore"], unit="dimensionless")

        ramachandran_outliers = None
        if vrpt_geom.get("percent_ramachandran_outliers"):
            ramachandran_outliers = QuantityValue(
                numeric_value=vrpt_geom["percent_ramachandran_outliers"], unit="percent"
            )

        return QualityMetrics(
            resolution=resolution,
            r_work=r_work,
            r_free=r_free,
            space_group=space_group,
            unit_cell_a=unit_cell_a,
            unit_cell_b=unit_cell_b,
            unit_cell_c=unit_cell_c,
            unit_cell_alpha=unit_cell_alpha,
            unit_cell_beta=unit_cell_beta,
            unit_cell_gamma=unit_cell_gamma,
            clashscore=clashscore,
            ramachandran_outliers_percent=ramachandran_outliers,
        )

    def _create_workflow_runs(
        self, entry_data: dict[str, Any], entry_id: str, warnings: list[str]
    ) -> list[WorkflowRun]:
        """Create WorkflowRun entries for refinement."""
        workflows = []

        refine = entry_data.get("refine", [])
        for i, ref in enumerate(refine, 1):
            software = entry_data.get("software", [])
            refine_software = next(
                (s for s in software if s.get("classification") == "refinement"), {}
            )

            workflows.append(
                WorkflowRun(
                    id=f"pdb:{entry_id}/workflow/refinement",
                    workflow_code=f"PDB-{entry_id}-REFINE",
                    workflow_type=WorkflowTypeEnum.refinement,
                    software_name=refine_software.get("name", "Unknown"),
                    software_version=refine_software.get("version"),
                    description=(
                        f"Refinement to {ref.get('ls_dres_high')} Å, "
                        f"R-work={ref.get('ls_rfactor_rwork')}"
                        if ref.get("ls_dres_high")
                        else None
                    ),
                )
            )

        return workflows

    def _create_data_files(
        self, entry_data: dict[str, Any], entry_id: str, warnings: list[str]
    ) -> list[DataFile]:
        """Create DataFile entries for PDB files."""
        files = []

        # PDB format file
        files.append(
            DataFile(
                id=f"pdb:{entry_id}/file/pdb",
                file_name=f"{entry_id.lower()}.pdb",
                file_format=FileFormatEnum.pdb,
                file_path=f"https://files.rcsb.org/download/{entry_id}.pdb",
                description="PDB format coordinates",
            )
        )

        # mmCIF format file
        files.append(
            DataFile(
                id=f"pdb:{entry_id}/file/mmcif",
                file_name=f"{entry_id.lower()}.cif",
                file_format=FileFormatEnum.mmcif,
                file_path=f"https://files.rcsb.org/download/{entry_id}.cif",
                description="mmCIF format coordinates",
            )
        )

        # Structure factors if available
        accession_info = entry_data.get("rcsb_accession_info", {})
        if accession_info.get("has_released_experimental_data") == "Y":
            files.append(
                DataFile(
                    id=f"pdb:{entry_id}/file/sf",
                    file_name=f"{entry_id.lower()}-sf.cif",
                    file_format=FileFormatEnum.mmcif,
                    file_path=f"https://files.rcsb.org/download/{entry_id}-sf.cif",
                    description="Structure factors",
                )
            )

        return files
