"""
ANL LAMBDA API loader.

The Structural Biology Center at Argonne serves its LIMS through the LAMBDA API at
https://sg.bio.anl.gov/lambda (Swagger: https://sg.bio.anl.gov/lambda/swagger/index.html).
Every call needs a Bearer session token, obtained by posting an API key to
``/api/auth/token``. The key is read from, in order: the ``api_key`` argument, the
``ANL_LAMBDA_API_KEY`` environment variable, the ``api_key_file`` argument, the
``ANL_LAMBDA_API_KEY_FILE`` environment variable, and finally a file named
``anl_lambda_token`` in the working directory.

Two views of the same Oracle database are exposed, and this loader covers both:

* **MX experiments** (``/api/mx/...``): one crystallography experiment per uuid, with the
  full ``V_LAM_XTA`` record (target, clone, expression, purification, crystallization,
  PI) and the diffraction frames that were collected. ``load(uuid)`` maps one of these to
  a Dataset; ``list_entries()`` finds uuids that have images.
* **LIMS dataset** (``/api/v1/lims/dataset``): the whole ``V_LAM_LIMS`` view, already
  arranged as a lambda-ber-schema ``Dataset`` by the server. ``load_lims_dataset()`` takes
  it as served and repairs what the server's serializer loses: enums come back as
  integers, every absent field is an explicit null, and the sample organism is a nested
  object. It also lifts a Protein row out of each sample's UniProt cross-reference.

Identifiers are rewritten into the ``anl-lambda:`` namespace registered in the schema,
keeping the server's local part (``lims:experiment:<uuid>`` becomes
``anl-lambda:experiment/<uuid>``), and the MX side emits the same ids for the same rows,
so the two views join.

Two things a consumer should know about the values, neither of which is warned about
at load time because both are how the source records them:

* every ``operator_id`` is a LIMS employee number (``282``), not a name; the API does
  not resolve them;
* ``culture_volume_l`` is served with unit ``L`` but the figure is in mL. The LIMS view
  flags this in ``warnings`` since it is a unit error; the MX view writes ``mL``.
"""

import json
import os
import re
from pathlib import Path
from typing import Any, Iterator

import requests

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult, uniprot_curie
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.pydantic import (
    BufferComposition,
    Dataset,
    DataFile,
    DataTypeEnum,
    ExperimentalMethodEnum,
    ExperimentInstrumentAssociation,
    ExperimentRun,
    ExperimentSampleAssociation,
    ExperimentSampleRoleEnum,
    ExpressionSystemEnum,
    FacilityEnum,
    FileFormatEnum,
    InstrumentCategoryEnum,
    InstrumentRoleEnum,
    PreparationTypeEnum,
    Protein,
    ProteinConstruct,
    QuantityValue,
    Sample,
    SamplePreparation,
    SampleProteinAssociation,
    SampleProteinRoleEnum,
    SampleTypeEnum,
    Study,
    StudyExperimentAssociation,
    StudySampleAssociation,
    StudyWorkflowAssociation,
    TechniqueEnum,
    WorkflowExperimentAssociation,
    WorkflowRun,
    WorkflowTypeEnum,
    XRayInstrument,
    XRaySourceTypeEnum,
)

DEFAULT_BASE_URL = "https://sg.bio.anl.gov/lambda"
API_KEY_ENV = "ANL_LAMBDA_API_KEY"
API_KEY_FILE_ENV = "ANL_LAMBDA_API_KEY_FILE"
DEFAULT_API_KEY_FILE = Path("anl_lambda_token")

#: Largest page the MX endpoints accept for experiments and files respectively.
EXPERIMENTS_PAGE_SIZE = 200
FILES_PAGE_SIZE = 1000
LIMS_PAGE_SIZE = 100

# The server builds its enums from an earlier copy of this schema and serializes them
# by position, so 0 is the first permissible value in that copy. These tables are
# pinned to that order on purpose: reordering or inserting a value in the schema must
# not silently change what an integer decodes to. Values added since (microed on
# TechniqueEnum, the nucleic acid databases on DatabaseNameEnum) come after the
# server's range and never appear.
_ENUM_ORDER: dict[str, list[str]] = {
    "SampleTypeEnum": [
        "protein", "nucleic_acid", "complex", "membrane_protein", "virus", "organelle",
    ],
    "DatabaseNameEnum": [
        "uniprot", "pdb", "pfam", "cath", "scop", "interpro", "chembl", "chebi", "pubchem",
        "drugbank", "omim", "clinvar", "cosmic", "gnomad", "intact", "string", "biogrid",
        "reactome", "kegg", "go",
    ],
    "PreparationTypeEnum": [
        "cryo_em", "xray_crystallography", "saxs", "sans", "protein_expression",
        "protein_purification", "negative_stain",
    ],
    "TechniqueEnum": [
        "cryo_em", "xray_crystallography", "saxs", "waxs", "sans", "cryo_et",
        "electron_microscopy", "mass_spectrometry", "xas", "xanes", "exafs", "xmcd",
        "neutron_crystallography", "fiber_diffraction", "time_resolved_crystallography",
        "xray_tomography",
    ],
    "WorkflowTypeEnum": [
        "motion_correction", "ctf_estimation", "particle_picking", "classification_2d",
        "classification_3d", "refinement", "model_building", "phasing", "integration",
        "scaling", "saxs_analysis", "xas_normalization", "xanes_analysis", "exafs_analysis",
        "em_2d_classification", "mass_spec_deconvolution", "particle_extraction",
        "ab_initio", "postprocessing", "map_validation", "model_refinement",
        "model_validation",
    ],
    "InstrumentCategoryEnum": [
        "SYNCHROTRON_BEAMLINE", "NEUTRON_BEAMLINE", "XFEL_BEAMLINE", "ELECTRON_MICROSCOPE",
        "BENCHTOP_XRAY", "OPTICAL_MICROSCOPE", "SPECTROMETER",
    ],
    "FacilityEnum": [
        "NSLS_II", "ALS", "SSRL", "ESRF", "DIAMOND", "PHOTON_FACTORY", "APS", "SPRING8",
        "PETRA_III", "SOLEIL", "AUSTRALIAN_SYNCHROTRON", "EMSL", "SNS", "HFIR",
    ],
    "SampleRoleEnum": ["target", "control", "reference", "blank"],
    "InstrumentRoleEnum": ["primary", "detector", "sample_handler"],
    "ExperimentSampleRoleEnum": ["target", "buffer_blank", "standard", "size_marker"],
}

#: Which enum each integer-valued field decodes with. ``role`` differs by association
#: table, so it is keyed by collection.
_ENUM_FIELDS: dict[str, str] = {
    "sample_type": "SampleTypeEnum",
    "database_name": "DatabaseNameEnum",
    "preparation_type": "PreparationTypeEnum",
    "technique": "TechniqueEnum",
    "workflow_type": "WorkflowTypeEnum",
    "instrument_category": "InstrumentCategoryEnum",
    "facility_name": "FacilityEnum",
}
_ROLE_ENUMS: dict[str, str] = {
    "study_sample_associations": "SampleRoleEnum",
    "experiment_sample_associations": "ExperimentSampleRoleEnum",
    "experiment_instrument_associations": "InstrumentRoleEnum",
}

#: NCBI Taxonomy id of Escherichia coli BL21(DE3), the expression host. The LIMS export
#: writes it as the source organism of every sample, whatever the species label says.
_BL21_DE3_TAXON = "NCBITaxon:469008"

#: What ``Sample.mutations`` holds when the export has put a sequence there: ten or
#: more residue letters and nothing else. A mutation such as ``K282A`` has digits and
#: is left alone. A run of ten or more bare letters with no digit is taken to be a
#: sequence; no LIMS mutation string looks like that.
_AMINO_ACIDS_RE = re.compile(r"^[ACDEFGHIKLMNPQRSTVWYXUBZ]{10,}$")
_LIMS_ID_RE = re.compile(r"^lims:([a-z_]+):(.+)$")
_BEAMLINE_CODE_RE = re.compile(r"beamline_([a-z0-9]+)_(\d+)([a-z]+)$", re.IGNORECASE)


def _clean(value: Any) -> Any:
    """
    Drop the empty values the server writes for every absent field.

    Nulls, empty strings, empty lists and empty objects all mean "not recorded" in the
    export; the pydantic models want them absent. Nested structures are cleaned too.
    ``0`` and ``False`` are values and are kept: the test is equality against the four
    empties, not truthiness.
    """
    if isinstance(value, dict):
        cleaned = {k: _clean(v) for k, v in value.items()}
        return {k: v for k, v in cleaned.items() if v not in (None, "", [], {})}
    if isinstance(value, list):
        return [_clean(v) for v in value]
    return value


def _as_list(value: Any) -> list[Any]:
    """A collapsed V_LAM_XTA column is a scalar for one value and a list for several."""
    if value is None:
        return []
    return list(value) if isinstance(value, list) else [value]


def _first(value: Any) -> Any:
    items = _as_list(value)
    return items[0] if items else None


def _pick(column: list[Any], index: int, count: int) -> Any:
    """
    The value for target ``index`` of ``count`` from a collapsed column.

    A column with one value per target is read by position. A column with a single
    value is shared by every target. An empty column gives None.
    """
    if not column:
        return None
    return column[index] if len(column) == count else column[0]


def _date(value: Any) -> str | None:
    """Keep the calendar date of an Oracle timestamp such as ``2014-10-18T00:00:00``."""
    value = _first(value)
    return str(value)[:10] if value else None


def _text(value: Any) -> str | None:
    value = _first(value)
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _operator(value: Any) -> str | None:
    """
    An ``operator_id`` from a V_LAM_XTA person column.

    The person columns (``crystallographer``, ``platesetupby``, ``batchclone_owner``,
    ``exp_batchclone_owner``) hold the LIMS employee number, such as ``282``, not a
    name. The API does not resolve it and neither does this loader, so the number is
    written as the string the slot allows for a personnel id.
    """
    return _text(value)


def _quantity(value: Any, unit: str, scale: float = 1.0) -> QuantityValue | None:
    value = _first(value)
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(value) * scale
    except (TypeError, ValueError):
        return None
    if number.is_integer():
        number = int(number)
    return QuantityValue(numeric_value=number, unit=unit)


def _instrument_row_id(instrument_code: str) -> str:
    """
    The Instrument row id for a beamline code, shared by both views.

    The LIMS export writes ``lims:instrument:APS|lambdaber:beamline_aps_19id`` and the MX
    view names the same beamline ``lambdaber:beamline_aps_19id``. Both become
    ``anl-lambda:instrument/beamline_aps_19id``: the facility already sits inside the
    code, and a second colon in a CURIE's local part trips some tooling.
    """
    local = instrument_code.split("|")[-1]
    if ":" in local:
        local = local.split(":", 1)[1]
    return f"{ANLLambdaLoader.source_name}:instrument/{local}"


def _beamline_id(instrument_code: str) -> str | None:
    """``lambdaber:beamline_aps_19id`` names beamline 19-ID."""
    match = _BEAMLINE_CODE_RE.search(instrument_code)
    if not match:
        return None
    return f"{match.group(2)}-{match.group(3).upper()}"


class ANLLambdaClient:
    """
    Thin HTTP client for the LAMBDA API: key exchange, Bearer sessions, paging, caching.

    The session token lives an hour. A 401 on a data call is taken as an expired token:
    the key is exchanged again once and the call retried. The token is never written to
    the response cache, and a cached GET is served without any auth call at all.
    """

    def __init__(
        self,
        api_key: str | None = None,
        api_key_file: Path | str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        cache: ResponseCache | None = None,
        session: requests.Session | None = None,
        timeout: float = 120.0,
    ):
        self.base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._api_key_file = Path(api_key_file) if api_key_file else None
        self.cache = cache or ResponseCache(enabled=False)
        self.session = session or requests.Session()
        self.timeout = timeout
        self._session_token: str | None = None

    def resolve_api_key(self) -> str:
        """Find the API key, or raise ValueError saying where one was looked for."""
        if self._api_key:
            return self._api_key.strip()
        env_key = os.environ.get(API_KEY_ENV)
        if env_key and env_key.strip():
            return env_key.strip()
        candidates: list[Path] = []
        if self._api_key_file:
            candidates.append(self._api_key_file)
        env_file = os.environ.get(API_KEY_FILE_ENV)
        if env_file:
            candidates.append(Path(env_file))
        candidates.append(DEFAULT_API_KEY_FILE)
        for path in candidates:
            if path.is_file():
                key = path.read_text().strip()
                if key:
                    return key
        raise ValueError(
            "No ANL LAMBDA API key: pass api_key, set "
            f"{API_KEY_ENV}, or put the key in a file named by {API_KEY_FILE_ENV} "
            f"or at ./{DEFAULT_API_KEY_FILE}"
        )

    def authenticate(self) -> str:
        """Exchange the API key for a session token and remember it."""
        response = self.session.post(
            f"{self.base_url}/api/auth/token",
            json={"apiKey": self.resolve_api_key()},
            timeout=self.timeout,
        )
        if response.status_code == 401:
            raise ValueError("ANL LAMBDA rejected the API key (HTTP 401)")
        response.raise_for_status()
        token = response.json().get("session_token")
        if not token:
            raise ValueError("ANL LAMBDA token exchange returned no session_token")
        self._session_token = token
        return token

    def _headers(self) -> dict[str, str]:
        token = self._session_token or self.authenticate()
        return {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    def get_json(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        GET a JSON document under the API base, through the cache.

        A 404 raises ValueError so the CLI reports "not found" rather than a bare HTTP
        failure; any other error status raises requests.HTTPError with the server's
        ``ProblemDetails`` detail attached to the message.
        """
        query = {k: v for k, v in (params or {}).items() if v is not None}
        key = path + ("?" + "&".join(f"{k}={v}" for k, v in sorted(query.items())) if query else "")
        return self.cache.get_or_fetch(f"anl-lambda/{key}", lambda: self._fetch(path, query))

    def _fetch(self, path: str, query: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = self.session.get(url, params=query, headers=self._headers(), timeout=self.timeout)
        if response.status_code == 401 and self._session_token:
            self._session_token = None
            response = self.session.get(
                url, params=query, headers=self._headers(), timeout=self.timeout
            )
        if response.status_code == 404:
            raise ValueError(f"ANL LAMBDA has no record at {path}: {self._detail(response)}")
        if not response.ok:
            raise requests.HTTPError(
                f"ANL LAMBDA {path} returned HTTP {response.status_code}: "
                f"{self._detail(response)}",
                response=response,
            )
        return response.json()

    @staticmethod
    def _detail(response: requests.Response) -> str:
        try:
            body = response.json()
        except ValueError:
            return response.text[:200]
        if isinstance(body, dict):
            return str(body.get("detail") or body.get("title") or body)[:200]
        return str(body)[:200]

    def pages(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        page_size: int = 100,
        items_key: str = "data",
        limit: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Walk a paged endpoint, yielding items until ``total_pages`` or ``limit`` is reached."""
        page = 1
        yielded = 0
        while True:
            body = self.get_json(path, {**(params or {}), "page": page, "page_size": page_size})
            items = body.get(items_key) or []
            for item in items:
                if limit is not None and yielded >= limit:
                    return
                yield item
                yielded += 1
            total_pages = body.get("total_pages") or 1
            if page >= total_pages or not items:
                return
            page += 1


class ANLLambdaLoader(BaseLoader):
    """
    Loader for the ANL LAMBDA API (Structural Biology Center, Argonne).

    Example:
        >>> loader = ANLLambdaLoader(api_key="...")
        >>> result = loader.load("e22fc16d-4e38-43f3-ad9b-50eea6b8ac69")
        >>> result.dataset.id
        'anl-lambda:experiment/e22fc16d-4e38-43f3-ad9b-50eea6b8ac69'
        >>> lims = loader.load_lims_dataset()
        >>> len(lims.dataset.samples)
        60
    """

    source_name = "anl-lambda"
    # base_url is set per instance in __init__, since a test server may replace it.

    def __init__(
        self,
        api_key: str | None = None,
        api_key_file: Path | str | None = None,
        cache: ResponseCache | None = None,
        client: ANLLambdaClient | None = None,
        include_files: bool = True,
        base_url: str = DEFAULT_BASE_URL,
    ):
        """
        Args:
            api_key: The API key. Otherwise resolved from the environment or a key file.
            api_key_file: A file holding the key, used when ``api_key`` is not given.
            cache: Response cache for development and batch runs (never holds the token).
            client: A prebuilt client, mainly for tests.
            include_files: Fetch every diffraction frame of an MX experiment as a
                DataFile. With False only the first page is fetched, for the frame
                header that fills the ExperimentRun, and no DataFile rows are made.
            base_url: API base, for a test server.
        """
        self.base_url = base_url.rstrip("/")
        self.client = client or ANLLambdaClient(
            api_key=api_key,
            api_key_file=api_key_file,
            base_url=self.base_url,
            cache=cache or ResponseCache(enabled=False),
        )
        self.include_files = include_files

    @property
    def _cache(self) -> ResponseCache:
        """The client's cache; BatchLoader swaps this for a long-lived one."""
        return self.client.cache

    @_cache.setter
    def _cache(self, cache: ResponseCache) -> None:
        self.client.cache = cache

    # ------------------------------------------------------------------ MX experiments

    def list_entries(
        self,
        protein_name: str | None = None,
        pi_name: str | None = None,
        limit: int | None = None,
        **filters: Any,
    ) -> list[str]:
        """
        List MX experiment uuids that have diffraction images.

        Any extra keyword is passed through as a ``V_LAM_XTA`` column filter, e.g.
        ``buffer_name="Tris"``; the server answers 400 for a column it does not know.
        """
        params = {"protein_name": protein_name, "pi_name": pi_name, **filters}
        return [
            record["experiment_id"]
            for record in self.client.pages(
                "api/mx/experiments", params, page_size=EXPERIMENTS_PAGE_SIZE, limit=limit
            )
            if record.get("experiment_id")
        ]

    def load(self, identifier: str) -> LoaderResult:
        """
        Load one MX experiment by uuid into a Dataset.

        Raises:
            ValueError: the uuid is unknown, or not visible to this key.
            requests.HTTPError: any other API failure.
        """
        uuid = identifier.strip()
        record = _clean(self.client.get_json(f"api/mx/experiments/{uuid}").get("data") or {})
        if not record:
            raise ValueError(f"ANL LAMBDA returned an empty record for experiment {uuid}")
        sets = [
            _clean(s) for s in self.client.pages(f"api/mx/experiments/{uuid}/sets", page_size=200)
        ]
        files, total_files = self._fetch_files(uuid)
        warnings: list[str] = []

        dataset_id = f"{self.source_name}:experiment/{uuid}"
        multi_valued = set(_as_list(record.get("multi_valued")))
        if multi_valued:
            warnings.append(
                f"Columns collapsed from {record.get('row_count')} view rows carry several "
                f"values: {', '.join(sorted(multi_valued))}"
            )

        instrument = self._create_instrument(record, files)
        sample = self._create_sample(record, warnings)
        proteins, constructs, sample_protein_associations = self._create_proteins(
            record, sample, warnings
        )
        preparations = self._create_preparations(record, sample, uuid)
        crystallization = next(
            (p for p in preparations if p.preparation_type == PreparationTypeEnum.xray_crystallography),
            None,
        )
        experiment = self._create_experiment_run(record, uuid, sets, files, total_files, warnings)
        data_files = self._create_data_files(files, experiment.id) if self.include_files else []
        workflows = self._create_workflows(record)

        pi_name = _text(record.get("pi_name"))
        rcsb_id = _text(record.get("rcsb_id"))
        study = Study(
            id=f"{dataset_id}/study",
            title=f"ANL SBC MX experiment {record.get('ha_id', uuid)}"
            + (f" ({rcsb_id})" if rcsb_id else ""),
            description=self._pi_description(record),
            keywords=[k for k in ("crystallography", pi_name) if k],
        )

        dataset = Dataset(
            id=dataset_id,
            title=f"{_text(record.get('target_annotation')) or 'MX experiment'} at "
            f"{_text(record.get('facility')) or 'ANL'} {_beamline_id(instrument.instrument_code) or ''}".strip(),
            description=f"Mapped from ANL LAMBDA V_LAM_XTA record {uuid}",
            studies=[study],
            instruments=[instrument],
            proteins=proteins or None,
            protein_constructs=constructs or None,
            samples=[sample],
            sample_preparations=preparations or None,
            experiment_runs=[experiment],
            workflow_runs=workflows or None,
            data_files=data_files or None,
            study_sample_associations=[StudySampleAssociation(study_id=study.id, sample_id=sample.id)],
            study_experiment_associations=[
                StudyExperimentAssociation(study_id=study.id, experiment_id=experiment.id)
            ],
            study_workflow_associations=[
                StudyWorkflowAssociation(study_id=study.id, workflow_id=wf.id) for wf in workflows
            ] or None,
            experiment_sample_associations=[
                ExperimentSampleAssociation(
                    experiment_id=experiment.id,
                    sample_id=sample.id,
                    role=ExperimentSampleRoleEnum.target,
                    preparation_id=crystallization.id if crystallization else None,
                )
            ],
            experiment_instrument_associations=[
                ExperimentInstrumentAssociation(
                    experiment_id=experiment.id,
                    instrument_id=instrument.id,
                    role=InstrumentRoleEnum.primary,
                )
            ],
            sample_protein_associations=sample_protein_associations or None,
            workflow_experiment_associations=[
                WorkflowExperimentAssociation(workflow_id=wf.id, experiment_id=experiment.id)
                for wf in workflows
            ] or None,
        )
        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            source_url=f"{self.base_url}/api/mx/experiments/{uuid}",
            raw_data={"record": record, "sets": sets, "files": files},
        )

    def _fetch_files(self, uuid: str) -> tuple[list[dict[str, Any]], int]:
        """
        The frame listing and the server's total.

        When files are not wanted only the first frame is fetched: its header fills the
        beam geometry of the ExperimentRun, and the page's ``total_count`` gives the
        frame count. The server returns ``total_count`` on a one-item page.
        """
        path = f"api/mx/experiments/{uuid}/files"
        if self.include_files:
            files = [_clean(f) for f in self.client.pages(path, page_size=FILES_PAGE_SIZE)]
            return files, len(files)
        body = self.client.get_json(path, {"page": 1, "page_size": 1})
        return [_clean(f) for f in body.get("data") or []], int(body.get("total_count") or 0)

    @staticmethod
    def _pi_description(record: dict[str, Any]) -> str | None:
        parts = []
        if _text(record.get("pi_name")):
            parts.append(f"PI: {_text(record.get('pi_name'))}")
        if _text(record.get("pi_institute")):
            parts.append(_text(record.get("pi_institute")))
        if _text(record.get("pi_orcid")):
            parts.append(f"ORCID {_text(record.get('pi_orcid'))}")
        return "; ".join(parts) or None

    def _create_instrument(self, record: dict[str, Any], files: list[dict[str, Any]]) -> XRayInstrument:
        code = _text(record.get("instrument")) or "unknown"
        facility = _text(record.get("facility"))
        facility_enum = None
        if facility and facility.upper() in _ENUM_ORDER["FacilityEnum"]:
            facility_enum = FacilityEnum(facility.upper())
        detector = _text(files[0].get("detector_type")) if files else None
        return XRayInstrument(
            id=_instrument_row_id(code),
            title=f"{facility or 'ANL'} {_beamline_id(code) or code}",
            instrument_code=code,
            instrument_category=InstrumentCategoryEnum.SYNCHROTRON_BEAMLINE,
            facility_name=facility_enum,
            beamline_id=_beamline_id(code),
            source_type=XRaySourceTypeEnum.synchrotron,
            detector_model=detector,
        )

    def _create_sample(self, record: dict[str, Any], warnings: list[str]) -> Sample:
        clone_id = _text(record.get("clone_id"))
        sample_code = _text(record.get("local_clone_id_public")) or clone_id or _text(record.get("xta_uuid"))
        sample_type = SampleTypeEnum.protein
        raw_type = _text(record.get("sample_type"))
        if raw_type:
            try:
                sample_type = SampleTypeEnum(raw_type.lower())
            except ValueError:
                warnings.append(f"Unknown sample_type {raw_type!r}; recorded as protein")
        names = [n for n in _as_list(record.get("target_annotation")) if n and n != "na"]
        taxon = _first(record.get("taxonid"))
        buffer = _text(record.get("buffer_content"))
        return Sample(
            id=f"{self.source_name}:sample/{clone_id or sample_code}",
            title=sample_code,
            description=", ".join(str(n) for n in names) or None,
            sample_code=sample_code,
            sample_type=sample_type,
            protein_name=", ".join(str(n) for n in names) or None,
            concentration=_quantity(record.get("prot_conc"), "mg/mL"),
            buffer_composition=BufferComposition(description=buffer) if buffer else None,
            organism=f"NCBITaxon:{taxon}" if taxon else None,
        )

    def _create_proteins(
        self, record: dict[str, Any], sample: Sample, warnings: list[str]
    ) -> tuple[list[Protein], list[ProteinConstruct], list[SampleProteinAssociation]]:
        """
        One Protein, ProteinConstruct and association per target in the crystal.

        A complex collapses into parallel lists on the target columns. They are zipped
        by position when they agree in length; otherwise only the first target is
        taken and the rest is left in the warning.
        """
        accessions = _as_list(record.get("uniprotid"))
        names = _as_list(record.get("target_annotation"))
        sequences = _as_list(record.get("target_protein_seq"))
        taxa = _as_list(record.get("taxonid"))
        species = _as_list(record.get("species_name"))
        lengths = _as_list(record.get("target_length"))
        seguids = _as_list(record.get("target_protein_seguid"))
        genes = _as_list(record.get("target_dna_header"))
        count = len(accessions)
        columns = [names, sequences, taxa, species, lengths, seguids, genes]
        if any(len(c) not in (0, 1, count) for c in columns):
            warnings.append(
                "Target columns disagree in length; only the first target is recorded"
            )
            count = min(count, 1)

        rcsb_id = _text(record.get("rcsb_id"))
        proteins: list[Protein] = []
        constructs: list[ProteinConstruct] = []
        associations: list[SampleProteinAssociation] = []
        for index in range(count):
            curie = uniprot_curie(str(accessions[index]))
            if curie is None:
                warnings.append(
                    f"uniprotid {accessions[index]!r} is not a UniProt accession; no Protein row"
                )
                continue
            taxon = _pick(taxa, index, count)
            name = _text(_pick(names, index, count))
            sequence = _text(_pick(sequences, index, count))
            seguid = _text(_pick(seguids, index, count))
            length = _pick(lengths, index, count)
            proteins.append(
                Protein(
                    id=curie,
                    uniprot_id=curie,
                    title=name,
                    protein_name=name,
                    gene_name=_text(_pick(genes, index, count)),
                    description=f"SEGUID {seguid}" if seguid else None,
                    organism=f"NCBITaxon:{taxon}" if taxon else None,
                    organism_name=_text(_pick(species, index, count)),
                    amino_acid_sequence=sequence,
                    sequence_length=int(length) if length else (len(sequence) if sequence else None),
                    pdb_entries=[f"pdb:{rcsb_id}"] if rcsb_id else None,
                )
            )
            construct = self._create_construct(record, curie, index, count)
            if construct:
                constructs.append(construct)
            associations.append(
                SampleProteinAssociation(
                    sample_id=sample.id,
                    protein_id=curie,
                    role=SampleProteinRoleEnum.target if count == 1 else SampleProteinRoleEnum.subunit,
                    construct_id=construct.construct_id if construct else None,
                )
            )
        return proteins, constructs, associations

    def _create_construct(
        self, record: dict[str, Any], protein_curie: str, index: int, count: int
    ) -> ProteinConstruct | None:
        def col(name: str) -> Any:
            return _pick(_as_list(record.get(name)), index, count)

        clone_id = _text(col("clone_id"))
        construct_id = _text(col("clone_id_f")) or clone_id
        if not construct_id:
            return None
        cleavage_enzyme = _text(col("cleavage_enzyme"))
        cleavage_site = _text(col("cleavage_site"))
        nterm = _text(col("nterm_cut"))
        taxon = col("taxonid")
        length = col("target_length")
        return ProteinConstruct(
            id=f"{self.source_name}:construct/{clone_id or construct_id}",
            title=_text(col("vector_name")),
            description=_text(col("vector_description")),
            construct_id=construct_id,
            protein_id=protein_curie,
            uniprot_id=protein_curie,
            gene_name=_text(col("target_dna_header")),
            ncbi_taxid=str(taxon) if taxon else None,
            sequence_length_aa=_quantity(length, "aa"),
            construct_description=_text(col("vector_description")),
            vector_name=_text(col("vector_name")),
            promoter=_text(col("promoter")),
            cleavage_site=" ".join(p for p in (cleavage_enzyme, cleavage_site) if p) or None,
            selectable_marker=_text(col("selectable_marker")),
            cloning_method=_text(col("protocolname")),
            insert_boundaries=f"N:{nterm} C:" if nterm else None,
            verification_notes=_text(col("protocoldetails")),
        )

    def _create_preparations(
        self, record: dict[str, Any], sample: Sample, uuid: str
    ) -> list[SamplePreparation]:
        """
        Expression, purification and crystallization, each keyed the way the LIMS view is.

        The LIMS export folds expression and purification into one "expression prep"
        keyed on the purification batch; here they are two rows, keyed on their own
        batch ids. The crystallization prep keeps the LIMS key (``pla_prodbatch_pl_id``)
        because ExperimentSampleAssociation.preparation_id points at it in both views.
        """
        preparations: list[SamplePreparation] = []

        expression_key = _first(record.get("exp_prodbatchclones_id"))
        if expression_key or _text(record.get("expression_media")):
            host = _text(record.get("exp_organism"))
            expression_system = (
                ExpressionSystemEnum.bacteria if host and "coli" in host.lower() else None
            )
            preparations.append(
                SamplePreparation(
                    id=f"{self.source_name}:expr_prep/{expression_key or uuid}",
                    title=f"Large-scale expression {expression_key or ''}".strip(),
                    preparation_type=PreparationTypeEnum.protein_expression,
                    sample_id=sample.id,
                    preparation_date=_date(record.get("epbc_experiment_date_start")),
                    operator_id=_operator(record.get("exp_batchclone_owner")),
                    expression_system=expression_system,
                    host_strain_or_cell_line=" ".join(
                        p for p in (host, _text(record.get("exp_strain"))) if p
                    ) or None,
                    # media_volume is recorded in millilitres (1000 for a litre culture).
                    culture_volume_l=_quantity(record.get("media_volume"), "mL"),
                    medium=_text(record.get("expression_media")),
                    growth_temperature_c=_quantity(record.get("growth_temperature"), "°C"),
                    induction_agent=_text(record.get("induction_reagent")),
                    induction_temperature_c=_quantity(record.get("induction_temperature"), "°C"),
                )
            )

        purification_key = _first(record.get("pur_prodbatchclones_id"))
        workflow_name = _text(record.get("workflow_name"))
        if purification_key or workflow_name:
            protocol = ": ".join(
                p for p in (workflow_name, _text(record.get("workflow_desc"))) if p
            )
            preparations.append(
                SamplePreparation(
                    id=f"{self.source_name}:pur_prep/{purification_key or uuid}",
                    title=f"Purification {workflow_name or purification_key}",
                    preparation_type=PreparationTypeEnum.protein_purification,
                    sample_id=sample.id,
                    preparation_date=_date(record.get("experiment_date_start")),
                    operator_id=_operator(record.get("batchclone_owner")),
                    protocol_description=protocol or None,
                    final_buffer=_text(record.get("buffer_content")),
                    final_concentration_mg_per_ml=_quantity(record.get("prot_conc"), "mg/mL"),
                )
            )

        crystallization_key = _first(record.get("pla_prodbatch_pl_id"))
        chemistry = _text(record.get("chemical_summary"))
        if crystallization_key or chemistry:
            screen = _text(record.get("screen_name"))
            cryo = _text(record.get("cryo_name"))
            preparations.append(
                SamplePreparation(
                    id=f"{self.source_name}:cryst_prep/{crystallization_key or uuid}",
                    title=_text(record.get("display_name")) or f"Crystallization {crystallization_key}",
                    description=self._crystallization_details(record),
                    preparation_type=PreparationTypeEnum.xray_crystallography,
                    sample_id=sample.id,
                    preparation_date=_date(record.get("plate_setup_date")),
                    operator_id=_operator(record.get("platesetupby")),
                    protocol_description="; ".join(p for p in (screen, chemistry, cryo) if p) or None,
                    growth_temperature_c=_quantity(record.get("crystallization_temp"), "°C"),
                )
            )
        return preparations

    @staticmethod
    def _crystallization_details(record: dict[str, Any]) -> str | None:
        """
        The crystallization description: screen and vendor, well, drop volumes, cryo.

        Each part is left out when its column is empty, e.g.
        ``Screen MCSG-1 (Anatrace); well B5; drop 200 nL protein + 200 nL reservoir;
        cryo 10% Glycerol``.
        """
        details: list[str] = []
        screen = _text(record.get("screen_name"))
        vendor = _text(record.get("screen_vendor"))
        if screen:
            details.append(f"Screen {screen}" + (f" ({vendor})" if vendor else ""))
        well = _text(record.get("screen_item"))
        if well:
            details.append(f"well {well}")
        drop = _first(record.get("drop_vol"))
        protein = _first(record.get("drop_prot_vol"))
        if drop is not None and protein is not None:
            details.append(f"drop {protein} nL protein + {drop} nL reservoir")
        elif drop is not None:
            details.append(f"drop {drop} nL reservoir")
        elif protein is not None:
            details.append(f"drop {protein} nL protein")
        cryo = _text(record.get("cryo_name"))
        if cryo:
            details.append(f"cryo {cryo}")
        return "; ".join(details) or None

    def _create_experiment_run(
        self,
        record: dict[str, Any],
        uuid: str,
        sets: list[dict[str, Any]],
        files: list[dict[str, Any]],
        total_files: int,
        warnings: list[str],
    ) -> ExperimentRun:
        """
        The data collection, with beam and sweep geometry read off the frame headers.

        Frame headers give distances in metres (``detector_distance`` 0.3, pixel size
        0.0001024); they are converted to mm and µm, the units the schema names. Beam
        centre is in mm as ADSC headers write it.
        """
        header = files[0] if files else {}
        minimal: dict[str, Any] = {}
        if header.get("minimal_schema_json"):
            try:
                minimal = json.loads(header["minimal_schema_json"])
            except (TypeError, ValueError):
                warnings.append("Frame header minimal_schema_json is not valid JSON")
        pixel = minimal.get("pixel_size") or {}
        sweep = self._sweep_geometry(files, total_files)
        complete = len(files) >= total_files

        technique = TechniqueEnum.xray_crystallography
        raw_technique = _text(record.get("technique"))
        if raw_technique and raw_technique.upper() != "MX":
            warnings.append(f"Technique {raw_technique!r} recorded as xray_crystallography")

        ha_id = _first(record.get("ha_id"))
        base_dir = _text(sets[0].get("base_dir")) if sets else None
        return ExperimentRun(
            id=f"{self.source_name}:experiment/{uuid}",
            title=str(ha_id) if ha_id is not None else uuid,
            description=_text(record.get("score_description")),
            experiment_code=str(ha_id) if ha_id is not None else uuid,
            technique=technique,
            experimental_method=ExperimentalMethodEnum.x_ray_diffraction,
            experiment_date=_date(record.get("test_date")),
            operator_id=_operator(record.get("crystallographer")),
            detector=_text(header.get("detector_type")),
            wavelength=_quantity(header.get("wavelength"), "Å"),
            detector_distance=_quantity(header.get("detector_distance"), "mm", scale=1000),
            beam_center_x=_quantity(header.get("beam_center_x"), "mm"),
            beam_center_y=_quantity(header.get("beam_center_y"), "mm"),
            pixel_size_x=_quantity(pixel.get("x"), "µm", scale=1_000_000),
            pixel_size_y=_quantity(pixel.get("y"), "µm", scale=1_000_000),
            exposure_time=_quantity(header.get("exposure_time"), "seconds"),
            oscillation_angle=_quantity(sweep["increment"], "degrees"),
            start_angle=_quantity(sweep["start"], "degrees"),
            sweep_start=_quantity(sweep["start"], "degrees"),
            sweep_end=_quantity(sweep["end"], "degrees"),
            total_rotation=_quantity(sweep["total_rotation"], "degrees"),
            number_of_images=_quantity(total_files or None, "images"),
            resolution=_quantity(record.get("resolution"), "Å"),
            raw_data_location=f"{base_dir}/{uuid}" if base_dir else None,
            start_time=_text(header.get("file_timestamp")),
            end_time=_text(files[-1].get("file_timestamp")) if complete and len(files) > 1 else None,
        )

    @staticmethod
    def _sweep_geometry(files: list[dict[str, Any]], total_files: int) -> dict[str, Any]:
        """
        Oscillation increment, sweep start and end, and total rotation, in degrees.

        With every frame in hand the sweep runs from the smallest ``osc_start`` to the
        end of the frame with the largest. A run of several sweeps with a gap between
        them still gets one start and one end; the gap is not subtracted, and
        total_rotation counts frames, not degrees swept. With only the first frame in
        hand (``include_files=False``) the run is taken as one contiguous sweep of
        ``total_files`` frames.
        """
        header = files[0] if files else {}
        increment = header.get("osc_increment")
        osc_starts = [f["osc_start"] for f in files if f.get("osc_start") is not None]
        start = min(osc_starts) if osc_starts else None
        end = None
        if osc_starts and increment is not None:
            if len(files) >= total_files:
                end = max(osc_starts) + increment
            else:
                end = start + total_files * increment
        total_rotation = total_files * increment if total_files and increment is not None else None
        return {"increment": increment, "start": start, "end": end, "total_rotation": total_rotation}

    def _create_data_files(self, files: list[dict[str, Any]], experiment_id: str) -> list[DataFile]:
        data_files: list[DataFile] = []
        for entry in files:
            name = _text(entry.get("filename"))
            file_id = entry.get("id")
            if not name or file_id is None:
                continue
            extension = name.rsplit(".", 1)[-1].lower() if "." in name else ""
            try:
                file_format = FileFormatEnum(extension)
            except ValueError:
                file_format = FileFormatEnum.img
            data_files.append(
                DataFile(
                    id=f"{self.source_name}:file/{file_id}",
                    title=name,
                    file_name=name,
                    file_path=_text(entry.get("source_file")),
                    file_format=file_format,
                    file_size_bytes=_quantity(entry.get("file_size"), "bytes"),
                    creation_date=_text(entry.get("file_timestamp")),
                    data_type=DataTypeEnum.diffraction,
                    file_role="raw",
                    storage_uri=f"{self.base_url}/api/mx/files/{file_id}/file",
                    related_entity=experiment_id,
                )
            )
        return data_files

    def _create_workflows(self, record: dict[str, Any]) -> list[WorkflowRun]:
        """The deposited structure, keyed on its PDB code as the LIMS view keys it."""
        rcsb_id = _text(record.get("rcsb_id"))
        if not rcsb_id:
            return []
        return [
            WorkflowRun(
                id=f"{self.source_name}:workflow/{rcsb_id}",
                title=f"Structure determination {rcsb_id}",
                description=f"Structure deposited as PDB {rcsb_id}",
                workflow_code=f"structure_{rcsb_id}",
                workflow_type=WorkflowTypeEnum.model_refinement,
                software_name="Unknown",
                pdb_id=rcsb_id,
                deposited_to_pdb=True,
                refinement_resolution_a=_quantity(record.get("resolution"), "Å"),
                processing_notes=_text(record.get("score_description")),
            )
        ]

    # ------------------------------------------------------------------- LIMS dataset

    def load_lims_dataset(self) -> LoaderResult:
        """
        Load the whole LIMS export as one Dataset.

        The server has already arranged ``V_LAM_LIMS`` into this schema's collections and
        association tables. What is done here is repair and enrichment, in this order:

        1. empty values dropped, ``lims:`` ids moved into the ``anl-lambda:`` namespace;
        2. integer enums decoded by position (see ``_ENUM_ORDER``);
        3. ``Sample.organism``, served as an object whose id is always the expression
           host, reduced to its species label and moved onto the Protein row;
        4. the amino acid sequence the export writes into ``Sample.mutations`` moved to
           ``Protein.amino_acid_sequence``;
        5. a Protein row lifted from each sample's UniProt cross-reference, linked back
           through SampleProteinAssociation, with the construct of the same accession;
        6. UniProt accessions on constructs written as CURIEs, ``protein_id`` set;
        7. workflow rows the export repeats (one per experiment sharing a PDB code)
           reduced to one.
        """
        body = self.client.get_json("api/v1/lims/dataset")
        raw = body.get("data") or {}
        warnings: list[str] = []
        data = self._rewrite_ids(_clean(raw))
        self._decode_enums(data)

        constructs_by_protein = self._repair_constructs(data.get("protein_constructs") or [], warnings)
        proteins, associations = self._lift_proteins(data, constructs_by_protein, warnings)
        if proteins:
            data["proteins"] = proteins
            data["sample_protein_associations"] = associations
        self._dedupe_workflows(data, warnings)
        self._check_units(data, warnings)

        # The served id is a fresh uuid per request, so it names the response, not the
        # data. Pin the id and keep the request's uuid in the description.
        export_id = data.get("id")
        data["id"] = f"{self.source_name}:dataset/lims"
        data.setdefault("title", "ANL LAMBDA LIMS export")
        if export_id:
            data["description"] = (
                f"{data.get('description') or 'ANL LAMBDA LIMS export'} (export {export_id})"
            )
        dataset = Dataset(**data)
        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            source_url=f"{self.base_url}/api/v1/lims/dataset",
            raw_data=raw,
        )

    def list_lims_samples(self, limit: int | None = None) -> list[str]:
        """Sample codes in the LIMS export, from its paged samples endpoint."""
        return [
            s["sample_code"]
            for s in self.client.pages(
                "api/v1/lims/dataset/samples", page_size=LIMS_PAGE_SIZE, limit=limit
            )
            if s.get("sample_code")
        ]

    def _rewrite_ids(self, value: Any) -> Any:
        """``lims:<kind>:<local>`` becomes ``anl-lambda:<kind>/<local>`` wherever it appears."""
        if isinstance(value, dict):
            return {k: self._rewrite_ids(v) for k, v in value.items()}
        if isinstance(value, list):
            return [self._rewrite_ids(v) for v in value]
        if isinstance(value, str):
            match = _LIMS_ID_RE.match(value)
            if match:
                kind, local = match.groups()
                if kind == "instrument":
                    return _instrument_row_id(local)
                return f"{self.source_name}:{kind}/{local}"
        return value

    @staticmethod
    def _decode_enums(data: dict[str, Any]) -> None:
        """
        Replace positional integers with permissible value names, in place.

        The field-keyed enums apply at any depth. The role enum applies only to the rows
        of the association table it belongs to, not to objects nested inside a row.
        """

        def decode(obj: Any, role_enum: str | None) -> None:
            if isinstance(obj, list):
                for item in obj:
                    decode(item, role_enum)
                return
            if not isinstance(obj, dict):
                return
            for key, value in list(obj.items()):
                enum_name = _ENUM_FIELDS.get(key)
                if key == "role" and role_enum:
                    enum_name = role_enum
                if enum_name and isinstance(value, int) and not isinstance(value, bool):
                    names = _ENUM_ORDER[enum_name]
                    if 0 <= value < len(names):
                        obj[key] = names[value]
                    else:
                        del obj[key]
                else:
                    decode(value, None)

        for collection, value in data.items():
            decode(value, _ROLE_ENUMS.get(collection))

    def _repair_constructs(
        self, constructs: list[dict[str, Any]], warnings: list[str]
    ) -> dict[str, dict[str, Any]]:
        """
        Write construct accessions as CURIEs and set protein_id; index them by protein.

        The construct dicts are edited in place: they are the rows of the cleaned,
        rewritten ``data`` that becomes the Dataset, and the index returned holds the
        same objects, so a later edit through the index shows in the Dataset.
        """
        by_protein: dict[str, dict[str, Any]] = {}
        for construct in constructs:
            accession = construct.pop("uniprot_id", None)
            if not accession:
                continue
            curie = uniprot_curie(str(accession))
            if curie is None:
                warnings.append(
                    f"Construct {construct.get('construct_id')} uniprot_id {accession!r} "
                    "is not a UniProt accession; left unlinked"
                )
                continue
            construct["uniprot_id"] = curie
            construct["protein_id"] = curie
            by_protein.setdefault(curie, construct)
        return by_protein

    def _lift_proteins(
        self,
        data: dict[str, Any],
        constructs_by_protein: dict[str, dict[str, Any]],
        warnings: list[str],
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        """One Protein row per UniProt accession named by a sample; see load_lims_dataset."""
        proteins: dict[str, dict[str, Any]] = {}
        associations: list[dict[str, Any]] = []
        host_taxon_seen = False
        sequence_moved = 0
        organism_dropped: list[str] = []
        disagreeing: set[str] = set()

        for sample in data.get("samples") or []:
            organism = sample.pop("organism", None)
            label = None
            if isinstance(organism, dict):
                label = _text(organism.get("label"))
                if organism.get("id") == _BL21_DE3_TAXON:
                    host_taxon_seen = True
            elif isinstance(organism, str):
                sample["organism"] = organism

            sequence = None
            mutations = sample.get("mutations")
            if isinstance(mutations, str) and _AMINO_ACIDS_RE.match(mutations.strip().upper()):
                sequence = sample.pop("mutations").strip().upper()
                sequence_moved += 1

            curies = []
            for xref in sample.get("database_cross_references") or []:
                if xref.get("database_name") == "uniprot" and xref.get("database_id"):
                    curie = uniprot_curie(str(xref["database_id"]))
                    if curie:
                        curies.append(curie)
            if not curies:
                if label:
                    organism_dropped.append(sample.get("id") or sample.get("sample_code", "?"))
                continue

            for curie in curies:
                construct = constructs_by_protein.get(curie)
                protein = proteins.get(curie)
                if protein is None:
                    protein = {"id": curie, "uniprot_id": curie}
                    if sample.get("protein_name"):
                        protein["protein_name"] = sample["protein_name"]
                        protein["title"] = sample["protein_name"]
                    if label:
                        protein["organism_name"] = label
                    if construct and construct.get("ncbi_taxid"):
                        protein["organism"] = f"NCBITaxon:{construct['ncbi_taxid']}"
                    if sequence:
                        protein["amino_acid_sequence"] = sequence
                        protein["sequence_length"] = len(sequence)
                    proteins[curie] = protein
                elif sequence and protein.get("amino_acid_sequence") not in (None, sequence):
                    disagreeing.add(curie)
                association = {
                    "sample_id": sample["id"],
                    "protein_id": curie,
                    "role": SampleProteinRoleEnum.target.value,
                }
                if construct:
                    association["construct_id"] = construct["construct_id"]
                associations.append(association)

        if host_taxon_seen:
            warnings.append(
                f"Sample.organism.id is {_BL21_DE3_TAXON} (E. coli BL21(DE3), the expression "
                "host) on every sample; the species label was kept as Protein.organism_name "
                "and the id dropped"
            )
        if sequence_moved:
            warnings.append(
                f"Sample.mutations held an amino acid sequence on {sequence_moved} samples; "
                "moved to Protein.amino_acid_sequence"
            )
        if organism_dropped:
            warnings.append(
                "No UniProt cross-reference, so the organism label had nowhere to go on: "
                + ", ".join(organism_dropped)
            )
        # Two samples of one accession with different sequences are two constructs of
        # it (domains of a polyprotein, say). Neither is the protein's sequence.
        for curie in sorted(disagreeing):
            proteins[curie].pop("amino_acid_sequence", None)
            proteins[curie].pop("sequence_length", None)
            warnings.append(
                f"Samples sharing {curie} carry different sequences, so they are construct "
                "sequences; none recorded on the Protein row"
            )
        return list(proteins.values()), associations

    @staticmethod
    def _dedupe_workflows(data: dict[str, Any], warnings: list[str]) -> None:
        """
        Keep one row per workflow id.

        The export writes the structure row once per experiment that shares its PDB
        code. When the copies differ, the first one served is kept, so the result
        follows the server's row order; there is no better tie-break in the data.
        """
        seen: dict[str, dict[str, Any]] = {}
        dropped: list[str] = []
        for workflow in data.get("workflow_runs") or []:
            if workflow["id"] in seen:
                if workflow != seen[workflow["id"]]:
                    warnings.append(
                        f"Workflow {workflow['id']} repeated with different content; kept the first"
                    )
                dropped.append(workflow["id"])
                continue
            seen[workflow["id"]] = workflow
        if dropped:
            data["workflow_runs"] = list(seen.values())
            warnings.append(
                f"Removed {len(dropped)} repeated workflow rows: "
                + ", ".join(sorted(set(dropped)))
            )

    @staticmethod
    def _check_units(data: dict[str, Any], warnings: list[str]) -> None:
        """The export labels culture volume in litres; 1000 of them is a millilitre figure."""
        suspect = [
            p.get("id")
            for p in data.get("sample_preparations") or []
            if (p.get("culture_volume_l") or {}).get("unit") == "L"
            and (p.get("culture_volume_l") or {}).get("numeric_value", 0) >= 100
        ]
        if suspect:
            warnings.append(
                f"culture_volume_l of 100 L or more on {len(suspect)} preparations; the "
                "LIMS records this figure in mL and the unit is left as served"
            )
