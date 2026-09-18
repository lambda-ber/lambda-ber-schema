"""Tests for the ANL LAMBDA loader."""

import json
from pathlib import Path
from typing import Any

import pytest
import requests
import responses

from lambda_ber_schema.loaders.anl_lambda import (
    API_KEY_ENV,
    API_KEY_FILE_ENV,
    ANLLambdaClient,
    ANLLambdaLoader,
    _beamline_id,
    _instrument_row_id,
)
from lambda_ber_schema.pydantic import (
    Dataset,
    FacilityEnum,
    PreparationTypeEnum,
    SampleProteinRoleEnum,
    TechniqueEnum,
    WorkflowTypeEnum,
)

FIXTURES = Path(__file__).parent / "fixtures" / "anl_lambda"
BASE = "https://sg.bio.anl.gov/lambda"
UUID = "e22fc16d-4e38-43f3-ad9b-50eea6b8ac69"


def fixture(name: str) -> dict[str, Any]:
    return json.loads((FIXTURES / name).read_text())


class FakeClient:
    """Serves the fixtures by path, recording every call."""

    def __init__(self, overrides: dict[str, dict[str, Any]] | None = None):
        self.calls: list[tuple[str, dict[str, Any] | None]] = []
        self.routes = {
            f"api/mx/experiments/{UUID}": fixture("mx_experiment.json"),
            f"api/mx/experiments/{UUID}/sets": fixture("mx_sets.json"),
            f"api/mx/experiments/{UUID}/files": fixture("mx_files.json"),
            "api/v1/lims/dataset": fixture("lims_dataset.json"),
        }
        self.routes.update(overrides or {})

    def get_json(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        self.calls.append((path, params))
        if path == "api/mx/experiments":
            page = (params or {}).get("page", 1)
            return fixture(f"mx_experiments_page{page}.json")
        try:
            return self.routes[path]
        except KeyError:
            raise ValueError(f"no fixture for {path}") from None

    def pages(self, path, params=None, page_size=100, items_key="data", limit=None):
        page = 1
        yielded = 0
        while True:
            body = self.get_json(path, {**(params or {}), "page": page, "page_size": page_size})
            for item in body.get(items_key) or []:
                if limit is not None and yielded >= limit:
                    return
                yield item
                yielded += 1
            if page >= (body.get("total_pages") or 1):
                return
            page += 1


@pytest.fixture
def loader() -> ANLLambdaLoader:
    return ANLLambdaLoader(client=FakeClient())


# --------------------------------------------------------------------------- client


class TestClientAuth:
    def test_api_key_argument_wins(self, monkeypatch):
        monkeypatch.setenv(API_KEY_ENV, "from-env")
        assert ANLLambdaClient(api_key=" from-arg ").resolve_api_key() == "from-arg"

    def test_env_key_before_file(self, monkeypatch, tmp_path):
        key_file = tmp_path / "key"
        key_file.write_text("from-file\n")
        monkeypatch.setenv(API_KEY_ENV, "from-env")
        assert ANLLambdaClient(api_key_file=key_file).resolve_api_key() == "from-env"

    def test_key_file_argument(self, monkeypatch, tmp_path):
        monkeypatch.delenv(API_KEY_ENV, raising=False)
        key_file = tmp_path / "key"
        key_file.write_text("from-file\n")
        assert ANLLambdaClient(api_key_file=key_file).resolve_api_key() == "from-file"

    def test_key_file_env(self, monkeypatch, tmp_path):
        monkeypatch.delenv(API_KEY_ENV, raising=False)
        key_file = tmp_path / "elsewhere"
        key_file.write_text("from-env-file")
        monkeypatch.setenv(API_KEY_FILE_ENV, str(key_file))
        assert ANLLambdaClient().resolve_api_key() == "from-env-file"

    def test_default_file_in_working_directory(self, monkeypatch, tmp_path):
        monkeypatch.delenv(API_KEY_ENV, raising=False)
        monkeypatch.delenv(API_KEY_FILE_ENV, raising=False)
        monkeypatch.chdir(tmp_path)
        (tmp_path / "anl_lambda_token").write_text("from-cwd")
        assert ANLLambdaClient().resolve_api_key() == "from-cwd"

    def test_missing_key_names_every_place_it_looked(self, monkeypatch, tmp_path):
        monkeypatch.delenv(API_KEY_ENV, raising=False)
        monkeypatch.delenv(API_KEY_FILE_ENV, raising=False)
        monkeypatch.chdir(tmp_path)
        with pytest.raises(ValueError, match="ANL_LAMBDA_API_KEY.*anl_lambda_token"):
            ANLLambdaClient().resolve_api_key()

    @responses.activate
    def test_token_exchange_posts_the_key_and_sends_bearer(self):
        responses.post(f"{BASE}/api/auth/token", json={"session_token": "tok-1", "expires_in": 3600})
        responses.get(f"{BASE}/api/auth/verify", json={"authenticated": True})
        client = ANLLambdaClient(api_key="secret")
        body = client.get_json("api/auth/verify")
        assert body == {"authenticated": True}
        assert json.loads(responses.calls[0].request.body) == {"apiKey": "secret"}
        assert responses.calls[1].request.headers["Authorization"] == "Bearer tok-1"

    @responses.activate
    def test_rejected_key_is_a_value_error(self):
        responses.post(f"{BASE}/api/auth/token", json={"title": "Unauthorized"}, status=401)
        with pytest.raises(ValueError, match="rejected the API key"):
            ANLLambdaClient(api_key="bad").authenticate()

    @responses.activate
    def test_expired_session_is_renewed_once(self):
        responses.post(f"{BASE}/api/auth/token", json={"session_token": "tok-1"})
        responses.get(f"{BASE}/api/mx/columns", json={"detail": "expired"}, status=401)
        responses.post(f"{BASE}/api/auth/token", json={"session_token": "tok-2"})
        responses.get(f"{BASE}/api/mx/columns", json={"data": {"total_columns": 1}})
        client = ANLLambdaClient(api_key="secret")
        assert client.get_json("api/mx/columns") == {"data": {"total_columns": 1}}
        assert [c.request.headers.get("Authorization") for c in responses.calls] == [
            None, "Bearer tok-1", None, "Bearer tok-2",
        ]

    @responses.activate
    def test_not_found_is_a_value_error_with_the_server_detail(self):
        responses.post(f"{BASE}/api/auth/token", json={"session_token": "tok"})
        responses.get(
            f"{BASE}/api/mx/experiments/nope",
            json={"title": "Not Found", "detail": "No experiment nope is available."},
            status=404,
        )
        with pytest.raises(ValueError, match="No experiment nope"):
            ANLLambdaClient(api_key="secret").get_json("api/mx/experiments/nope")

    @responses.activate
    def test_server_error_is_an_http_error(self):
        responses.post(f"{BASE}/api/auth/token", json={"session_token": "tok"})
        responses.get(f"{BASE}/api/v1/lims/dataset", json={"detail": "ORA-12345"}, status=500)
        with pytest.raises(requests.HTTPError, match="HTTP 500: ORA-12345"):
            ANLLambdaClient(api_key="secret").get_json("api/v1/lims/dataset")

    @responses.activate
    def test_pages_walks_total_pages_and_honours_limit(self):
        responses.post(f"{BASE}/api/auth/token", json={"session_token": "tok"})
        responses.get(
            f"{BASE}/api/mx/experiments",
            json={"data": [{"experiment_id": "a"}, {"experiment_id": "b"}], "total_pages": 2},
            match=[responses.matchers.query_param_matcher({"page": "1", "page_size": "2"})],
        )
        responses.get(
            f"{BASE}/api/mx/experiments",
            json={"data": [{"experiment_id": "c"}], "total_pages": 2},
            match=[responses.matchers.query_param_matcher({"page": "2", "page_size": "2"})],
        )
        client = ANLLambdaClient(api_key="secret")
        assert [r["experiment_id"] for r in client.pages("api/mx/experiments", page_size=2)] == [
            "a", "b", "c",
        ]
        assert [
            r["experiment_id"] for r in client.pages("api/mx/experiments", page_size=2, limit=1)
        ] == ["a"]


# --------------------------------------------------------------------- id helpers


def test_instrument_row_id_is_the_same_from_both_views():
    lims = _instrument_row_id("APS|lambdaber:beamline_aps_19id")
    mx = _instrument_row_id("lambdaber:beamline_aps_19id")
    assert lims == mx == "anl-lambda:instrument/beamline_aps_19id"


def test_beamline_id_reads_the_code():
    assert _beamline_id("lambdaber:beamline_aps_19id") == "19-ID"
    assert _beamline_id("something else") is None


# ------------------------------------------------------------------ MX experiments


class TestListEntries:
    def test_walks_pages_and_passes_filters(self):
        client = FakeClient()
        loader = ANLLambdaLoader(client=client)
        uuids = loader.list_entries(protein_name="EspG2", pi_name="Joachimiak")
        assert uuids == [UUID, "1215379f-cef4-449c-ae29-bf90d3d0687a"]
        path, params = client.calls[0]
        assert path == "api/mx/experiments"
        assert params["protein_name"] == "EspG2"
        assert params["pi_name"] == "Joachimiak"

    def test_limit(self):
        assert ANLLambdaLoader(client=FakeClient()).list_entries(limit=1) == [UUID]


class TestLoadExperiment:
    def test_dataset_validates_and_ids_join_the_lims_view(self, loader):
        result = loader.load(UUID)
        ds = result.dataset
        assert result.warnings == []
        assert ds.id == f"anl-lambda:experiment/{UUID}"
        assert ds.experiment_runs[0].id == f"anl-lambda:experiment/{UUID}"
        assert ds.samples[0].id == "anl-lambda:sample/APC109958"
        assert ds.workflow_runs[0].id == "anl-lambda:workflow/5DU2"
        assert ds.instruments[0].id == "anl-lambda:instrument/beamline_aps_19id"
        assert ds.experiment_sample_associations[0].preparation_id == "anl-lambda:cryst_prep/14291"
        # Round trip through the model with nothing dropped
        Dataset(**ds.model_dump(exclude_none=True, mode="json"))
        assert result.source_url == f"{BASE}/api/mx/experiments/{UUID}"

    def test_instrument(self, loader):
        instrument = loader.load(UUID).dataset.instruments[0]
        assert instrument.instrument_code == "lambdaber:beamline_aps_19id"
        assert instrument.facility_name == FacilityEnum.Advanced_Photon_Source
        assert instrument.beamline_id == "19-ID"
        assert instrument.detector_model == "TH7899"

    def test_sample(self, loader):
        sample = loader.load(UUID).dataset.samples[0]
        assert sample.sample_code == "APC109958.102"
        assert sample.sample_type == "protein"
        assert sample.protein_name == "EspG2-Glycosyltransferase"
        assert sample.organism == "NCBITaxon:46165"
        assert sample.concentration.numeric_value == 33.33
        assert sample.concentration.unit == "mg/mL"
        assert sample.buffer_composition.description == "20 mM HEPES pH 8.0, 250 mM NaCl, 2 mM DTT"

    def test_protein_and_construct(self, loader):
        ds = loader.load(UUID).dataset
        protein = ds.proteins[0]
        assert protein.id == protein.uniprot_id == "uniprot:A0A0R4I999"
        assert protein.organism == "NCBITaxon:46165"
        assert protein.organism_name == "Actinomadura verrucosospora"
        assert protein.amino_acid_sequence.startswith("MRSAAAHRIALVNVANHG")
        assert protein.sequence_length == 399
        assert protein.pdb_entries == ["pdb:5DU2"]
        assert protein.description == "SEGUID H16yWXbkvpz8QqdQHv+HTHdiiY4"

        construct = ds.protein_constructs[0]
        assert construct.construct_id == "APC109958.1-399.F..pMCSG68"
        assert construct.protein_id == "uniprot:A0A0R4I999"
        assert construct.vector_name == "pMCSG68"
        assert construct.cleavage_site == "TEV ENLYFQS"
        assert construct.ncbi_taxid == "46165"
        assert construct.sequence_length_aa.numeric_value == 399

        assoc = ds.sample_protein_associations[0]
        assert assoc.sample_id == ds.samples[0].id
        assert assoc.protein_id == "uniprot:A0A0R4I999"
        assert assoc.role == SampleProteinRoleEnum.target
        assert assoc.construct_id == construct.construct_id

    def test_three_preparations(self, loader):
        preps = {p.preparation_type: p for p in loader.load(UUID).dataset.sample_preparations}
        assert set(preps) == {
            PreparationTypeEnum.protein_expression,
            PreparationTypeEnum.protein_purification,
            PreparationTypeEnum.xray_crystallography,
        }
        expression = preps[PreparationTypeEnum.protein_expression]
        assert expression.id == "anl-lambda:expr_prep/9300"
        assert expression.preparation_date == "2014-07-28"
        assert expression.expression_system == "bacteria"
        assert expression.host_strain_or_cell_line == "E. coli BL21-Gold(DE3)"
        assert expression.culture_volume_l.unit == "mL"
        assert expression.induction_temperature_c.numeric_value == 18

        purification = preps[PreparationTypeEnum.protein_purification]
        assert purification.id == "anl-lambda:pur_prep/8440"
        assert purification.protocol_description.startswith("IMAC-I, IMAC-II: Two-step")
        assert purification.final_concentration_mg_per_ml.numeric_value == 33.33

        crystallization = preps[PreparationTypeEnum.xray_crystallography]
        assert crystallization.id == "anl-lambda:cryst_prep/14291"
        assert crystallization.preparation_date == "2014-08-08"
        assert crystallization.growth_temperature_c.numeric_value == 16
        assert "MCSG-1" in crystallization.protocol_description
        assert "cryo 10% Glycerol" in crystallization.description

    def test_experiment_run_reads_the_frame_headers_in_schema_units(self, loader):
        run = loader.load(UUID).dataset.experiment_runs[0]
        assert run.experiment_code == "5191"
        assert run.technique == TechniqueEnum.xray_crystallography
        assert run.experiment_date == "2014-10-18"
        assert run.operator_id == "282"
        assert run.resolution.numeric_value == 2.7
        assert run.resolution.unit == "Å"
        assert run.wavelength.numeric_value == pytest.approx(0.9791827)
        # metres in the header, mm and µm in the schema
        assert (run.detector_distance.numeric_value, run.detector_distance.unit) == (300, "mm")
        assert (run.pixel_size_x.numeric_value, run.pixel_size_x.unit) == (pytest.approx(102.4), "µm")
        assert run.beam_center_x.numeric_value == 157.8
        assert run.exposure_time.numeric_value == 2
        assert run.oscillation_angle.numeric_value == 1
        assert run.start_angle.numeric_value == -45
        assert run.sweep_end.numeric_value == -42
        assert run.total_rotation.numeric_value == 3
        assert run.number_of_images.numeric_value == 3
        assert run.detector == "TH7899"
        assert run.start_time == "2014-10-19T22:23:18"
        assert run.end_time == "2014-10-19T22:23:22"
        assert run.raw_data_location == f"/backup1/globus/lambda-ber-anl01/APS_LAMBDA/MX/{UUID}"

    def test_data_files_one_per_frame(self, loader):
        ds = loader.load(UUID).dataset
        assert len(ds.data_files) == 3
        first = ds.data_files[0]
        assert first.id == "anl-lambda:file/11584"
        assert first.file_name == "ESPG2_M1_B5_x3_data.0001.img"
        assert first.file_format == "img"
        assert first.data_type == "diffraction"
        assert first.file_size_bytes.numeric_value == 18881024
        assert first.storage_uri == f"{BASE}/api/mx/files/11584/file"
        assert first.related_entity == ds.experiment_runs[0].id

    def test_workflow_and_study(self, loader):
        ds = loader.load(UUID).dataset
        workflow = ds.workflow_runs[0]
        assert workflow.workflow_type == WorkflowTypeEnum.model_refinement
        assert workflow.pdb_id == "5DU2"
        assert workflow.deposited_to_pdb is True
        assert workflow.refinement_resolution_a.numeric_value == 2.7
        assert ds.workflow_experiment_associations[0].workflow_id == workflow.id
        assert ds.study_workflow_associations[0].workflow_id == workflow.id
        study = ds.studies[0]
        assert "5191" in study.title and "5DU2" in study.title
        assert "Andrzej Joachimiak" in study.description
        assert "0000-0003-2535-6209" in study.description

    def test_without_files_still_fills_the_run_from_the_first_page(self):
        client = FakeClient()
        loader = ANLLambdaLoader(client=client, include_files=False)
        ds = loader.load(UUID).dataset
        assert ds.data_files is None
        assert ds.experiment_runs[0].wavelength.numeric_value == pytest.approx(0.9791827)
        assert ds.experiment_runs[0].number_of_images.numeric_value == 3
        files_calls = [c for c in client.calls if c[0].endswith("/files")]
        assert len(files_calls) == 1

    def test_no_structure_means_no_workflow(self):
        record = fixture("mx_experiment.json")
        record["data"]["rcsb_id"] = None
        loader = ANLLambdaLoader(client=FakeClient({f"api/mx/experiments/{UUID}": record}))
        ds = loader.load(UUID).dataset
        assert ds.workflow_runs is None
        assert ds.workflow_experiment_associations is None
        assert ds.proteins[0].pdb_entries is None

    def test_complex_becomes_one_protein_per_target(self):
        record = fixture("mx_experiment.json")
        data = record["data"]
        data.update(
            {
                "uniprotid": ["A0A0R4I999", "P69905"],
                "target_annotation": ["EspG2-Glycosyltransferase", "Hemoglobin alpha"],
                "target_protein_seq": ["MRSAAAHRIALV", "MVLSPADKTNVK"],
                "taxonid": [46165, 9606],
                "species_name": ["Actinomadura verrucosospora", "Homo sapiens"],
                "target_length": [399, 142],
                "target_protein_seguid": ["seg1", "seg2"],
                "target_dna_header": ["EspG2", "HBA1"],
                "clone_id": ["APC109958", "APC109959"],
                "clone_id_f": ["APC109958.F", "APC109959.F"],
                "row_count": 2,
                "multi_valued": ["uniprotid", "target_annotation", "clone_id"],
            }
        )
        loader = ANLLambdaLoader(client=FakeClient({f"api/mx/experiments/{UUID}": record}))
        result = loader.load(UUID)
        ds = result.dataset
        assert [p.id for p in ds.proteins] == ["uniprot:A0A0R4I999", "uniprot:P69905"]
        assert ds.proteins[1].organism == "NCBITaxon:9606"
        assert [c.construct_id for c in ds.protein_constructs] == ["APC109958.F", "APC109959.F"]
        assert {a.role for a in ds.sample_protein_associations} == {SampleProteinRoleEnum.subunit}
        assert ds.samples[0].protein_name == "EspG2-Glycosyltransferase, Hemoglobin alpha"
        assert any("several values" in w for w in result.warnings)

    def test_bad_accession_is_warned_not_recorded(self):
        record = fixture("mx_experiment.json")
        record["data"]["uniprotid"] = "not-an-accession"
        loader = ANLLambdaLoader(client=FakeClient({f"api/mx/experiments/{UUID}": record}))
        result = loader.load(UUID)
        assert result.dataset.proteins is None
        assert result.dataset.sample_protein_associations is None
        assert any("not a UniProt accession" in w for w in result.warnings)


# -------------------------------------------------------------------- LIMS export


class TestLoadLimsDataset:
    @pytest.fixture
    def result(self, loader):
        return loader.load_lims_dataset()

    def test_validates_with_no_lims_prefix_left(self, result):
        dumped = result.dataset.model_dump(exclude_none=True, mode="json")
        Dataset(**dumped)
        assert "lims:" not in json.dumps(dumped)
        assert result.dataset.id == "anl-lambda:dataset/lims"
        assert "b7ff79da" in result.dataset.description

    def test_enums_decoded_by_position(self, result):
        ds = result.dataset
        assert ds.samples[0].sample_type == "protein"
        assert ds.samples[0].database_cross_references[0].database_name == "uniprot"
        assert ds.instruments[0].instrument_category == "SYNCHROTRON_BEAMLINE"
        assert ds.instruments[0].facility_name == FacilityEnum.Advanced_Photon_Source
        assert ds.experiment_runs[0].technique == TechniqueEnum.xray_crystallography
        assert ds.workflow_runs[0].workflow_type == WorkflowTypeEnum.model_refinement
        assert {p.preparation_type for p in ds.sample_preparations} == {
            PreparationTypeEnum.protein_expression,
            PreparationTypeEnum.xray_crystallography,
        }
        assert ds.experiment_sample_associations[0].role == "target"
        assert ds.experiment_instrument_associations[0].role == "primary"

    def test_ids_rewritten(self, result):
        ds = result.dataset
        assert ds.samples[0].id == "anl-lambda:sample/APC100327"
        assert ds.instruments[0].id == "anl-lambda:instrument/beamline_aps_19id"
        assert ds.experiment_instrument_associations[0].instrument_id == ds.instruments[0].id
        assert ds.experiment_sample_associations[0].preparation_id == "anl-lambda:cryst_prep/1342"
        assert ds.sample_preparations[0].sample_id == ds.samples[0].id
        assert ds.experiment_runs[0].id == (
            "anl-lambda:experiment/e4853b4e-1f6b-478b-8f55-e44c3b7de7bf"
        )

    def test_protein_lifted_from_cross_reference(self, result):
        ds = result.dataset
        proteins = {p.id: p for p in ds.proteins}
        assert set(proteins) == {"uniprot:C8WTQ0", "uniprot:P0DTD1"}
        c8 = proteins["uniprot:C8WTQ0"]
        assert c8.organism_name == "Alicyclobacillus acidocaldarius subsp. acidocaldarius DSM 446"
        assert c8.organism == "NCBITaxon:521098"  # from the construct, not the stuck sample id
        assert c8.amino_acid_sequence.startswith("MSQLVTHAFDD")
        assert c8.sequence_length == 82
        assoc = [a for a in ds.sample_protein_associations if a.protein_id == "uniprot:C8WTQ0"]
        assert len(assoc) == 1
        assert assoc[0].sample_id == "anl-lambda:sample/APC100327"
        assert assoc[0].construct_id == "1"
        assert assoc[0].role == SampleProteinRoleEnum.target

    def test_sample_keeps_no_sequence_and_no_stuck_organism(self, result):
        for sample in result.dataset.samples:
            assert sample.mutations is None
            assert sample.organism is None
        assert any("BL21(DE3)" in w for w in result.warnings)
        assert any("moved to Protein.amino_acid_sequence" in w for w in result.warnings)

    def test_shared_accession_with_two_sequences_records_neither(self, result):
        ds = result.dataset
        p0 = next(p for p in ds.proteins if p.id == "uniprot:P0DTD1")
        assert p0.amino_acid_sequence is None
        assert p0.organism == "NCBITaxon:2697049"
        assert len([a for a in ds.sample_protein_associations if a.protein_id == p0.id]) == 2
        assert any("construct sequences" in w for w in result.warnings)

    def test_sample_without_accession_is_warned(self, result):
        assert any("anl-lambda:sample/CPX300104" in w for w in result.warnings)

    def test_constructs_get_curies_and_protein_id(self, result):
        constructs = {c.construct_id: c for c in result.dataset.protein_constructs}
        assert constructs["1"].uniprot_id == "uniprot:C8WTQ0"
        assert constructs["1"].protein_id == "uniprot:C8WTQ0"
        assert constructs["381"].uniprot_id is None
        assert constructs["381"].protein_id is None

    def test_repeated_workflow_reduced_to_one(self, result):
        ds = result.dataset
        assert [w.id for w in ds.workflow_runs] == [
            "anl-lambda:workflow/3RQB", "anl-lambda:workflow/7UV5",
        ]
        assert len(ds.workflow_experiment_associations) == 3
        assert any("repeated workflow rows" in w for w in result.warnings)
        assert any("different content" in w for w in result.warnings)

    def test_litre_figures_are_flagged_not_changed(self, result):
        expression = next(
            p for p in result.dataset.sample_preparations
            if p.preparation_type == PreparationTypeEnum.protein_expression
        )
        assert expression.culture_volume_l.numeric_value == 1000
        assert expression.culture_volume_l.unit == "L"
        assert any("culture_volume_l" in w for w in result.warnings)

    def test_list_lims_samples(self):
        page = {
            "data": [{"sample_code": "APC100327.102"}, {"sample_code": "IDP52003.668"}],
            "total_pages": 1,
        }
        loader = ANLLambdaLoader(client=FakeClient({"api/v1/lims/dataset/samples": page}))
        assert loader.list_lims_samples() == ["APC100327.102", "IDP52003.668"]
