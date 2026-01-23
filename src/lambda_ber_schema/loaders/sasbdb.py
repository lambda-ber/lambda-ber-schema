"""
SASBDB (Small Angle Scattering Biological Data Bank) loader.

API Documentation: https://www.sasbdb.org/rest-api/docs/
"""

from typing import Any

import requests

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.pydantic import (
    BufferComposition,
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
    SAXSInstrument,
    Study,
    StudyExperimentAssociation,
    StudySampleAssociation,
    TechniqueEnum,
    WorkflowExperimentAssociation,
    WorkflowRun,
    WorkflowTypeEnum,
)


class SASBDBLoader(BaseLoader):
    """
    Loader for SASBDB (Small Angle Scattering Biological Data Bank).

    SASBDB is a curated repository for SAXS/SANS experimental data
    maintained by EMBL Hamburg.

    Example:
        >>> loader = SASBDBLoader()
        >>> result = loader.load("SASDA52")
        >>> result.dataset.id
        'sasbdb:SASDA52'
        >>> result.dataset.studies[0].samples[0].protein_name
        'Alcohol dehydrogenase 1'
    """

    source_name = "sasbdb"
    base_url = "https://www.sasbdb.org/rest-api"

    def __init__(self, cache: ResponseCache | None = None):
        """
        Initialize the SASBDB loader.

        Args:
            cache: Optional response cache for development/testing
        """
        self.cache = cache or ResponseCache(enabled=False)

    def load(self, entry_code: str) -> LoaderResult:
        """
        Load a SASBDB entry by code.

        Args:
            entry_code: SASBDB entry code (e.g., "SASDA52")

        Returns:
            LoaderResult with populated Dataset

        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If the entry is not found
        """
        raw = self._fetch_entry(entry_code)
        warnings: list[str] = []

        # Build the dataset
        dataset_id = self.make_id(entry_code)
        source_url = f"https://www.sasbdb.org/data/{entry_code}/"

        # Create instrument
        instrument = self._create_instrument(raw, warnings)

        # Create sample
        sample = self._create_sample(raw, entry_code, warnings)

        # Create experiment run (no direct sample/instrument refs in relational model)
        experiment = self._create_experiment_run(raw, entry_code, warnings)

        # Create workflow runs for analysis steps
        workflows = self._create_workflow_runs(raw, entry_code, warnings)

        # Create data files
        data_files = self._create_data_files(raw, entry_code, warnings)

        # Create lightweight study (relational model)
        study = Study(
            id=f"{dataset_id}/study",
            title=raw.get("project", {}).get("title", f"SASBDB Entry {entry_code}"),
        )

        # Create association tables to link entities
        study_sample_associations = [
            StudySampleAssociation(study_id=study.id, sample_id=sample.id)
        ]
        study_experiment_associations = [
            StudyExperimentAssociation(study_id=study.id, experiment_id=experiment.id)
        ]
        experiment_sample_associations = [
            ExperimentSampleAssociation(
                experiment_id=experiment.id, sample_id=sample.id
            )
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

        # Create dataset with flat entity collections and associations
        dataset = Dataset(
            id=dataset_id,
            title=raw.get("project", {}).get("title", f"SASBDB Entry {entry_code}"),
            studies=[study],
            instruments=[instrument],
            samples=[sample],
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
            raw_data=raw,
        )

    def list_entries(
        self,
        molecular_type: str | None = None,
        uniprot_code: str | None = None,
        tag: str | None = None,
        limit: int | None = None,
    ) -> list[str]:
        """
        List available SASBDB entry codes.

        Args:
            molecular_type: Filter by type (protein, rna, dna, heterocomplex, other)
            uniprot_code: Filter by UniProt accession
            tag: Filter by classification tag
            limit: Maximum number of entries to return

        Returns:
            List of entry codes
        """
        if uniprot_code:
            url = f"{self.base_url}/entry/codes/uniprot/{uniprot_code}.json"
        elif molecular_type:
            url = f"{self.base_url}/entry/codes/molecular_type/{molecular_type}.json"
        elif tag:
            url = f"{self.base_url}/entry/codes/tags/{tag}.json"
        else:
            url = f"{self.base_url}/entry/codes/all.json"

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        entries = response.json()

        # API may return list of dicts with 'code' key or list of strings
        codes = []
        for entry in entries:
            if isinstance(entry, dict):
                codes.append(entry.get("code", str(entry)))
            else:
                codes.append(entry)

        if limit:
            codes = codes[:limit]

        return codes

    def _fetch_entry(self, entry_code: str) -> dict[str, Any]:
        """Fetch entry data from SASBDB API."""
        cache_key = f"sasbdb/{entry_code}"

        def fetch() -> dict[str, Any]:
            url = f"{self.base_url}/entry/summary/{entry_code}.json"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()

        return self.cache.get_or_fetch(cache_key, fetch)

    def _create_instrument(
        self, raw: dict[str, Any], warnings: list[str]
    ) -> SAXSInstrument:
        """Create SAXSInstrument from SASBDB instrument data."""
        instrument_data = raw.get("experiment", {}).get("instrument", {})

        # Build instrument code from name and beamline
        name = instrument_data.get("name", "Unknown")
        beamline = instrument_data.get("beamline_name", "")
        instrument_code = f"{name}-{beamline}".strip("-") if beamline else name

        # Extract detector info
        detector = instrument_data.get("detector", {})
        detector_name = detector.get("name")
        detector_resolution = detector.get("resolution")

        return SAXSInstrument(
            id=f"sasbdb:instrument/{instrument_code.replace(' ', '_').replace(',', '')}",
            title=f"{name} {beamline}".strip(),
            instrument_code=instrument_code.replace(" ", "-"),
            description=(
                f"Detector: {detector_name} (resolution: {detector_resolution} mm)"
                if detector_name
                else None
            ),
            manufacturer=instrument_data.get("city"),
        )

    def _create_sample(
        self, raw: dict[str, Any], entry_code: str, warnings: list[str]
    ) -> Sample:
        """Create Sample from SASBDB sample/molecule data."""
        sample_data = raw.get("experiment", {}).get("sample", {})
        molecules = sample_data.get("molecule", [])

        # Get first molecule (primary)
        molecule = molecules[0] if molecules else {}

        # Determine sample type from molecular_type field
        mol_type = molecule.get("molecular_type", "protein")
        sample_type_map = {
            "protein": SampleTypeEnum.protein,
            "dna": SampleTypeEnum.nucleic_acid,
            "rna": SampleTypeEnum.nucleic_acid,
            "heterocomplex": SampleTypeEnum.complex,
        }
        sample_type = sample_type_map.get(mol_type, SampleTypeEnum.protein)

        # Extract buffer composition
        buffer_data = sample_data.get("buffer", {})
        buffer_composition = None
        if buffer_data:
            ph_value = None
            if buffer_data.get("ph"):
                ph_value = QuantityValue(
                    numeric_value=buffer_data["ph"],
                    unit="pH",
                )
            buffer_composition = BufferComposition(
                ph=ph_value,
                components=[buffer_data["name"]] if buffer_data.get("name") else None,
            )

        # Get concentration as QuantityValue
        exp_data = raw.get("experiment", {})
        concentration = None
        if exp_data.get("concentration_max"):
            concentration = QuantityValue(
                numeric_value=exp_data["concentration_max"],
                unit=exp_data.get("concentration_unit", "mg/mL"),
            )

        # Get molecular weight as QuantityValue
        molecular_weight = None
        if molecule.get("total_mw"):
            molecular_weight = QuantityValue(
                numeric_value=molecule["total_mw"],
                unit="kDa",
            )

        # Create sample
        return Sample(
            id=f"sasbdb:{entry_code}/sample",
            sample_code=f"SASBDB-{entry_code}",
            sample_type=sample_type,
            title=sample_data.get("name"),
            protein_name=molecule.get("long_name"),
            organism=molecule.get("organism"),
            molecular_weight=molecular_weight,
            concentration=concentration,
            buffer_composition=buffer_composition,
            description=(
                f"UniProt: {molecule.get('uniprot_code')}, "
                f"Oligomerization: {molecule.get('oligomerization')}"
                if molecule.get("uniprot_code")
                else None
            ),
        )

    def _create_experiment_run(
        self,
        raw: dict[str, Any],
        entry_code: str,
        warnings: list[str],
    ) -> ExperimentRun:
        """Create ExperimentRun from SASBDB experiment data."""
        exp_data = raw.get("experiment", {})

        # Extract quality metrics with QuantityValue types
        rg_value = None
        if raw.get("guinier_rg"):
            rg_value = QuantityValue(
                numeric_value=raw["guinier_rg"],
                unit="nm",  # SASBDB Rg is in nm
            )

        i0_value = None
        if raw.get("guinier_i0"):
            i0_value = QuantityValue(
                numeric_value=raw["guinier_i0"],
                unit="arbitrary",
            )

        quality_metrics = QualityMetrics(
            rg=rg_value,
            i_zero=i0_value,
        )

        # Wavelength is in nm in SASBDB, convert to Angstroms with QuantityValue
        wavelength = None
        if exp_data.get("wavelength"):
            wavelength = QuantityValue(
                numeric_value=exp_data["wavelength"] * 10,  # nm to Angstroms
                unit="Angstroms",
            )

        # Detector distance with QuantityValue
        detector_distance = None
        if exp_data.get("sample_detector_distance"):
            detector_distance = QuantityValue(
                numeric_value=exp_data["sample_detector_distance"] * 1000,  # m to mm
                unit="mm",
            )

        return ExperimentRun(
            id=f"sasbdb:{entry_code}/experiment",
            experiment_code=f"SASBDB-{entry_code}-EXP",
            technique=TechniqueEnum.saxs,
            experiment_date=exp_data.get("date"),
            wavelength=wavelength,
            detector_distance=detector_distance,
            quality_metrics=quality_metrics,
        )

    def _create_workflow_runs(
        self,
        raw: dict[str, Any],
        entry_code: str,
        warnings: list[str],
    ) -> list[WorkflowRun]:
        """Create WorkflowRun entries for SAXS analysis."""
        workflows = []

        # GNOM/PDDF analysis
        pddf_software = raw.get("pddf_software")
        if pddf_software:
            workflows.append(
                WorkflowRun(
                    id=f"sasbdb:{entry_code}/workflow/pddf",
                    workflow_code=f"SASBDB-{entry_code}-PDDF",
                    workflow_type=WorkflowTypeEnum.saxs_analysis,
                    software_name=pddf_software,
                    software_version=raw.get("pddf_software_version"),
                    description=(
                        f"PDDF analysis. Rg={raw.get('pddf_rg')}, "
                        f"Dmax={raw.get('pddf_dmax')}, I0={raw.get('pddf_i0')}"
                    ),
                )
            )

        # Model fits
        for i, fit in enumerate(raw.get("fits", []), 1):
            for j, model in enumerate(fit.get("models", []), 1):
                software = model.get("software", "Unknown")
                model_type = model.get("type_of_model", "unknown")

                workflows.append(
                    WorkflowRun(
                        id=f"sasbdb:{entry_code}/workflow/fit{i}_model{j}",
                        workflow_code=f"SASBDB-{entry_code}-FIT{i}-M{j}",
                        workflow_type=WorkflowTypeEnum.saxs_analysis,
                        software_name=software,
                        description=(
                            f"{model_type.capitalize()} model fit. "
                            f"Chi-square: {fit.get('chi_square_value')}"
                        ),
                    )
                )

        return workflows

    def _create_data_files(
        self, raw: dict[str, Any], entry_code: str, warnings: list[str]
    ) -> list[DataFile]:
        """Create DataFile entries for SASBDB data files."""
        files = []

        # Scattering data (.dat)
        if raw.get("intensities_data"):
            files.append(
                DataFile(
                    id=f"sasbdb:{entry_code}/file/intensities",
                    file_name=f"{entry_code}.dat",
                    file_format=FileFormatEnum.ascii,
                    file_path=raw["intensities_data"],
                    description="Scattering intensity data",
                )
            )

        # PDDF data (.out)
        if raw.get("pddf_data"):
            files.append(
                DataFile(
                    id=f"sasbdb:{entry_code}/file/pddf",
                    file_name=f"{entry_code}.out",
                    file_format=FileFormatEnum.ascii,
                    file_path=raw["pddf_data"],
                    description="Pair distance distribution function (PDDF)",
                )
            )

        # sasCIF data
        if raw.get("sascif_data"):
            files.append(
                DataFile(
                    id=f"sasbdb:{entry_code}/file/sascif",
                    file_name=f"{entry_code}.sascif",
                    file_format=FileFormatEnum.ascii,
                    file_path=raw["sascif_data"],
                    description="sasCIF format data",
                )
            )

        # Fit files
        for i, fit in enumerate(raw.get("fits", []), 1):
            if fit.get("fit_data"):
                files.append(
                    DataFile(
                        id=f"sasbdb:{entry_code}/file/fit{i}",
                        file_name=f"{entry_code}_fit{i}.fit",
                        file_format=FileFormatEnum.ascii,
                        file_path=fit["fit_data"],
                        description=f"Fit {i} data",
                    )
                )

            # Model PDB files
            for j, model in enumerate(fit.get("models", []), 1):
                if model.get("model_data"):
                    files.append(
                        DataFile(
                            id=f"sasbdb:{entry_code}/file/fit{i}_model{j}",
                            file_name=f"{entry_code}_fit{i}_model{j}.pdb",
                            file_format=FileFormatEnum.pdb,
                            file_path=model["model_data"],
                            description=f"Model {j} from fit {i}",
                        )
                    )

        return files
