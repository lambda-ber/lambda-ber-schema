"""Tests for the PDB loader, against real RCSB Data API responses captured in fixtures/pdb."""

import copy

import pytest

from lambda_ber_schema.loaders.base import dataset_to_dict
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.loaders.pdb import PDBLoader
from lambda_ber_schema.pydantic import (
    CryoEMInstrument,
    Dataset,
    NMRInstrument,
    SAXSInstrument,
    TechniqueEnum,
    XRayInstrument,
)

from .conftest import read_pdb_fixture


def _by_id(rows):
    return {row.id: row for row in rows or []}


def _interactions(ds, subject_title=None):
    titles = {c.id: c.title for c in ds.sample_components}
    return [
        (titles[i.subject_id], i.interaction_type, titles[i.object_id], i)
        for i in ds.sample_component_interactions or []
        if subject_title is None or titles[i.subject_id] == subject_title
    ]


class TestEntryBasics:
    """What every entry gets: ids, the study, dates, keywords, cross-references, files."""

    def test_load_returns_dataset(self, pdb_loader):
        result = pdb_loader.load("1hho")
        assert isinstance(result.dataset, Dataset)
        assert result.dataset.id == "pdb:1HHO"
        assert "OXYHAEMOGLOBIN" in result.dataset.title
        assert result.source_url == "https://www.rcsb.org/structure/1HHO"
        assert result.doi == "https://doi.org/10.2210/pdb1hho/pdb"

    def test_dates_and_revision_are_on_the_dataset(self, pdb_loader):
        ds = pdb_loader.load("7ZYI").dataset
        assert ds.deposition_date == "2022-05-24"
        assert ds.release_date == "2022-07-13"
        assert ds.last_revision_date == "2024-11-13"
        assert ds.revision == "1.4"

    def test_experiment_date_is_never_the_deposition_date(self, pdb_loader):
        """1HHO records no collection date; the deposition date must not stand in for one."""
        ds = pdb_loader.load("1HHO").dataset
        assert ds.experiment_runs[0].experiment_date is None
        assert pdb_loader.load("6BOC").dataset.experiment_runs[0].experiment_date == "2016-12-19"

    def test_keywords(self, pdb_loader):
        study = pdb_loader.load("7ZYI").dataset.studies[0]
        assert "TRANSPORT PROTEIN" in study.keywords
        assert "sodium/bile acid cotransporter" in study.keywords

    def test_cross_references_name_the_pdb_doi_and_the_map(self, pdb_loader):
        refs = {(r.database_name, r.database_id): r for r in pdb_loader.load("7ZYI").dataset.studies[0].database_cross_references}
        assert refs[("pdb", "7ZYI")].database_url == "https://doi.org/10.2210/pdb7zyi/pdb"
        assert ("emdb", "EMD-15024") in refs

    def test_em_entry_lists_the_map_and_no_structure_factors(self, pdb_loader):
        files = {f.id: f for f in pdb_loader.load("7ZYI").dataset.data_files}
        assert "pdb:7ZYI/file/sf" not in files
        emdb_map = files["pdb:7ZYI/file/map-15024"]
        assert emdb_map.file_path == "https://files.wwpdb.org/pub/emdb/structures/EMD-15024/map/emd_15024.map.gz"
        assert emdb_map.data_type == "volume"
        assert files["pdb:7ZYI/file/validation"].file_format == "pdf"

    def test_xray_entry_lists_structure_factors(self, pdb_loader):
        files = _by_id(pdb_loader.load("6BOC").dataset.data_files)
        assert files["pdb:6BOC/file/sf"].file_name == "6boc-sf.cif"


class TestPeopleAndPublications:

    def test_primary_citation_is_a_publication(self, pdb_loader):
        ds = pdb_loader.load("7ZYI").dataset
        pub = ds.publications[0]
        assert pub.id == "doi:10.1038/s41422-022-00680-4"
        assert pub.pubmed_id == "pmid:35726088"
        assert pub.journal_abbreviation == "Cell Res."
        assert pub.year == 2022
        assert pub.authors[0] == "Liu, H."
        assert ds.study_publication_associations[0].is_primary is True

    def test_authors_in_order_with_orcids(self, pdb_loader):
        ds = pdb_loader.load("7ZYI").dataset
        persons = _by_id(ds.persons)
        positions = {a.author_position: persons[a.person_id] for a in ds.study_person_associations}
        assert positions[1].full_name == "Liu, H."
        assert positions[9].full_name == "Locher, K.P."
        assert positions[9].orcid == "https://orcid.org/0000-0002-8207-2889"

    def test_funders_with_grant_numbers(self, pdb_loader):
        ds = pdb_loader.load("6BOC").dataset
        org = ds.organizations[0]
        assert org.organization_type == "funding_agency"
        assert org.country == "United States"
        assoc = ds.study_organization_associations[0]
        assert assoc.role == "funder"
        assert assoc.award_number


class TestSampleComposition:
    """The specimen is one sample; each entity is a component of it."""

    def test_one_sample_with_a_component_per_entity(self, pdb_loader):
        ds = pdb_loader.load("7ZYI").dataset
        assert [s.id for s in ds.samples] == ["pdb:7ZYI/sample"]
        sample = ds.samples[0]
        assert sample.title == "sodium/bile acid cotransporter (NTCP) in complex with Fab and nanobody"
        assert sample.sample_type == "complex"
        assert [c.component_type for c in ds.sample_components] == [
            "protein", "protein", "protein", "protein", "small_molecule", "small_molecule", "small_molecule",
        ]

    def test_proteins_without_uniprot_get_entry_local_rows(self, pdb_loader):
        """The Fab chains and the nanobody have no UniProt entry; their sequence identifies them."""
        result = pdb_loader.load("7ZYI")
        proteins = _by_id(result.dataset.proteins)
        assert set(proteins) == {
            "uniprot:Q14973", "pdb:7ZYI/protein/2", "pdb:7ZYI/protein/3", "pdb:7ZYI/protein/4",
        }
        nanobody = proteins["pdb:7ZYI/protein/4"]
        assert nanobody.organism == "NCBITaxon:9844"
        assert nanobody.amino_acid_sequence.startswith("VQLQESGGGLVQPGG")
        assert any("no UniProt mapping" in w for w in result.warnings)

    def test_uniprot_protein_carries_annotations(self, pdb_loader):
        ntcp = _by_id(pdb_loader.load("7ZYI").dataset.proteins)["uniprot:Q14973"]
        assert ntcp.gene_name == "SLC10A1"
        assert "GO:0008508" in ntcp.go_terms
        refs = {(r.database_name, r.database_id) for r in ntcp.cross_references}
        assert ("pfam", "PF01758") in refs
        assert ("chembl", "CHEMBL5287") in refs

    def test_construct_holds_the_deposited_sequence_and_expression(self, pdb_loader):
        ds = pdb_loader.load("7ZYI").dataset
        construct = _by_id(ds.protein_constructs)["pdb:7ZYI/construct/1"]
        assert construct.protein_id == "uniprot:Q14973"
        assert construct.amino_acid_sequence.startswith("MEAHNASAPFNFTLPPNFGKRPTDLALSVILVFMLFF")
        assert construct.gene_name == "SLC10A1, NTCP, GIG29"
        expression = _by_id(ds.sample_preparations)["pdb:7ZYI/preparation/expression-1-1"]
        assert expression.expression_system == "mammalian"
        assert expression.host_strain_or_cell_line == "HEK293"
        fab = _by_id(ds.sample_preparations)["pdb:7ZYI/preparation/expression-2-1"]
        assert fab.expression_system == "bacteria"

    def test_ligands_are_small_molecules(self, pdb_loader):
        result = pdb_loader.load("7ZYI")
        molecules = _by_id(result.dataset.small_molecules)
        gcdc = molecules["CHEBI:36274"]
        assert gcdc.pdb_ligand_id == "pdb.ligand:CHO"
        assert gcdc.inchikey == "GHCZAUBVMUEKKP-GYPHWSFCSA-N"
        assert gcdc.molecular_formula == "C26H43NO5"
        assert molecules["pdb.ligand:NA"].chemical_class == "ion"
        # Cholesterol relates to two ChEBI entries, so neither is taken as its identity
        assert "pdb.ligand:CLR" in molecules
        assert any("CLR maps to several ChEBI entries" in w for w in result.warnings)
        components = {c.small_molecule_id: c for c in result.dataset.sample_components if c.small_molecule_id}
        assert components["CHEBI:36274"].role == "ligand"
        assert components["CHEBI:36274"].copy_number == 2

    def test_glycans_are_carbohydrate_components_linked_to_their_chain(self, pdb_loader):
        ds = pdb_loader.load("6VXX").dataset
        glycans = [m for m in ds.small_molecules if m.id.startswith("glytoucan:")]
        assert glycans and all(g.chemical_class == "carbohydrate" for g in glycans)
        linked = [row for row in _interactions(ds) if row[1] == "covalently_linked_to"]
        assert linked

    def test_oligomeric_state_and_assembly_evidence(self, pdb_loader):
        sample = pdb_loader.load("7ZYI").dataset.samples[0]
        assert "Hetero 4-mer" in sample.oligomeric_state
        evidence = [p.value for p in sample.additional_properties
                    if p.attribute.label == "pdbx_struct_assembly_auth_evidence.experimental_support"]
        assert evidence == ["electron microscopy"]

    def test_em_sub_assemblies_are_child_samples(self, pdb_loader):
        ds = pdb_loader.load("6MB3").dataset
        children = [s for s in ds.samples if s.parent_sample_id == "pdb:6MB3/sample"]
        assert {s.title for s in children} == {"shortened CSP", "Fab311"}
        child_components = [c for c in ds.sample_components if c.sample_id == children[0].id]
        assert child_components

    def test_dna_and_protein(self, pdb_loader):
        ds = pdb_loader.load("1AAY").dataset
        strands = _by_id(ds.nucleic_acids)
        strand = strands["pdb:1AAY/nucleic_acid/1"]
        assert strand.nucleic_acid_type == "dna"
        assert strand.nucleotide_sequence == "AGCGTGGGCGT"
        assert strand.nucleic_acid_name.startswith("DNA (5'-D(*AP*GP*CP*GP")
        roles = {a.nucleic_acid_id: a.role for a in ds.sample_nucleic_acid_associations}
        assert set(roles.values()) == {"binding_partner"}
        assert ds.sample_protein_associations[0].role == "target"
        assert [p.id for p in ds.proteins] == ["uniprot:P08046"]

    def test_natural_source_is_an_isolation(self, pdb_loader):
        ds = pdb_loader.load("1WKX").dataset
        isolations = [p for p in ds.sample_preparations if p.preparation_type == "protein_purification"]
        assert isolations and isolations[0].description.startswith("Isolated from")


class TestInteractions:
    """Contacts RCSB reports become SampleComponentInteraction rows."""

    def test_ligands_bind_the_chain_they_sit_on(self, pdb_loader):
        ds = pdb_loader.load("7ZYI").dataset
        rows = {(s, t, o) for s, t, o, _ in _interactions(ds)}
        assert ("GLYCOCHENODEOXYCHOLIC ACID", "binds", "Sodium/bile acid cotransporter") in rows
        assert ("SODIUM ION", "is_coordinated_by", "Sodium/bile acid cotransporter") in rows

    def test_interfaces_say_which_chain_binds_which(self, pdb_loader):
        ds = pdb_loader.load("7ZYI").dataset
        rows = {(s, o): i for s, t, o, i in _interactions(ds) if t == "binds"}
        assert ("heavy chain of Fab", "Sodium/bile acid cotransporter") in rows
        assert ("Nanobody", "light chain of Fab") in rows
        contact = rows[("heavy chain of Fab", "Sodium/bile acid cotransporter")]
        assert contact.interaction_status == "observed"
        assert "Y58" in contact.subject_site
        assert "823 square angstroms" in contact.description

    def test_binding_affinity(self, pdb_loader):
        ds = pdb_loader.load("6BOC").dataset
        measured = [i for _, _, _, i in _interactions(ds) if i.affinity is not None]
        assert measured
        assert measured[0].affinity_type == "kd"
        assert measured[0].affinity.unit == "nM"


class TestTechniques:
    """Each method gets its own runs, instruments, preparations and workflows."""

    def test_single_particle_cryo_em(self, pdb_loader):
        ds = pdb_loader.load("7ZYI").dataset
        run = ds.experiment_runs[0]
        assert run.technique == TechniqueEnum.cryo_em
        assert run.experimental_method == "single_particle_analysis"
        assert run.total_dose.numeric_value == 64.0
        assert run.number_of_images.numeric_value == 13208
        assert run.defocus_range_min.numeric_value == 600.0
        assert run.acquisition_software == "EPU"
        microscope = ds.instruments[0]
        assert isinstance(microscope, CryoEMInstrument)
        assert microscope.model == "TFS KRIOS"
        assert microscope.manufacturer == "Thermo Fisher Scientific"
        assert microscope.accelerating_voltage.numeric_value == 300
        assert microscope.detector_model == "GATAN K3 BIOQUANTUM (6k x 4k)"
        prep = _by_id(ds.sample_preparations)["pdb:7ZYI/preparation/em-specimen"]
        assert prep.cryoem_preparation.vitrification_instrument == "FEI VITROBOT MARK IV"
        assert prep.cryoem_preparation.cryogen == "ETHANE-PROPANE"
        workflows = _by_id(ds.workflow_runs)
        reconstruction = workflows["pdb:7ZYI/workflow/em-reconstruction"]
        assert reconstruction.software_name == "RELION"
        assert reconstruction.refinement_params.number_of_particles == 161093
        assert workflows["pdb:7ZYI/workflow/em-ctf-estimation"].software_name == "Gctf"

    def test_instrument_subclass_fields_survive_serialization(self, pdb_loader):
        data = dataset_to_dict(pdb_loader.load("7ZYI").dataset)
        assert data["instruments"][0]["accelerating_voltage"]["numeric_value"] == 300

    def test_xray_crystallography(self, pdb_loader):
        ds = pdb_loader.load("6BOC").dataset
        run = ds.experiment_runs[0]
        assert run.technique == TechniqueEnum.xray_crystallography
        qm = run.quality_metrics
        assert qm.r_work.numeric_value == 0.2601
        assert qm.space_group == "P 1 2 1"
        beamline = ds.instruments[0]
        assert isinstance(beamline, XRayInstrument)
        assert beamline.facility_name == "ALS"
        assert beamline.beamline_id == "8.3.1"
        assert beamline.detector_model == "DECTRIS PILATUS 6M"
        workflows = _by_id(ds.workflow_runs)
        refinement = workflows["pdb:6BOC/workflow/refinement"]
        assert refinement.software_name == "PHENIX"
        assert refinement.search_model_pdb_id == "4QKM"
        assert refinement.phasing_method == "molecular_replacement"
        assert refinement.rmsd_bonds.numeric_value == 0.028
        scaling = workflows["pdb:6BOC/workflow/scaling"]
        assert scaling.cc_half.numeric_value == 0.957
        assert scaling.resolution_shells[0].resolution_high.numeric_value == 2.25
        crystal = _by_id(ds.sample_preparations)["pdb:6BOC/preparation/crystal-1"].xray_preparation
        assert crystal.crystallization_method == "lcp"
        assert crystal.crystallization_ph == 3.5
        assert "monoolein" in crystal.crystallization_conditions.crystallization_conditions

    def test_refinement_statistics_without_a_named_slot_are_kept(self, pdb_loader):
        refinement = _by_id(pdb_loader.load("6BOC").dataset.workflow_runs)["pdb:6BOC/workflow/refinement"]
        labels = {m.attribute.label: m for m in refinement.additional_metrics}
        probe = labels["refine.pdbx_solvent_vdw_probe_radii"]
        assert probe.attribute.id == "mmCIF:_refine.pdbx_solvent_vdw_probe_radii"
        assert probe.unit == "Angstroms"
        assert labels["refine.ls_number_reflns_obs"].unit == "unspecified"

    def test_joint_xray_and_neutron_are_two_runs(self, pdb_loader):
        ds = pdb_loader.load("6D4L").dataset
        assert {r.technique for r in ds.experiment_runs} == {
            TechniqueEnum.xray_crystallography, TechniqueEnum.neutron_crystallography,
        }
        refinements = [w for w in ds.workflow_runs if w.workflow_type == "refinement"]
        assert len(refinements) == 2

    def test_solution_nmr(self, pdb_loader):
        ds = pdb_loader.load("1D3Z").dataset
        assert {r.technique for r in ds.experiment_runs} == {TechniqueEnum.solution_nmr}
        assert ds.experiment_runs[0].title == "3D_13C-SEPARATED_NOESY"
        assert ds.experiment_runs[0].experimental_conditions.temperature.numeric_value == 308
        spectrometer = ds.instruments[0]
        assert isinstance(spectrometer, NMRInstrument)
        assert spectrometer.field_strength.numeric_value == 600
        solution = _by_id(ds.samples)["pdb:1D3Z/sample/nmr-1"]
        assert solution.parent_sample_id == "pdb:1D3Z/sample"
        assert {a.sample_id for a in ds.experiment_sample_associations} == {solution.id}

    def test_solution_scattering(self, pdb_loader):
        ds = pdb_loader.load("1W2R").dataset
        assert ds.experiment_runs[0].technique in (TechniqueEnum.saxs, TechniqueEnum.sans)
        assert isinstance(ds.instruments[0], SAXSInstrument)
        assert any(w.workflow_type == "saxs_analysis" for w in ds.workflow_runs)

    def test_microed(self, pdb_loader):
        ds = pdb_loader.load("6UOU").dataset
        run = ds.experiment_runs[0]
        assert run.technique == TechniqueEnum.microed
        assert run.quality_metrics.space_group
        assert any(w.resolution_shells for w in ds.workflow_runs)
        assert any(p.preparation_type == "xray_crystallography" for p in ds.sample_preparations)

    def test_helical_reconstruction(self, pdb_loader):
        ds = pdb_loader.load("6TUQ").dataset
        assert ds.experiment_runs[0].experimental_method == "helical_reconstruction"
        params = _by_id(ds.workflow_runs)["pdb:6TUQ/workflow/em-reconstruction"].refinement_params
        assert params.helical_rise is not None and params.helical_twist is not None

    def test_subtomogram_averaging_is_cryo_et(self, pdb_loader):
        run = pdb_loader.load("4BZJ").dataset.experiment_runs[0]
        assert run.technique == TechniqueEnum.cryo_et
        assert run.experimental_method == "subtomogram_averaging"

    def test_serial_crystallography_details_are_kept(self, pdb_loader):
        run = pdb_loader.load("7S4R").dataset.experiment_runs[0]
        labels = {p.attribute.label for p in (run.additional_properties or []) + (run.additional_metrics or [])}
        assert any(label.startswith("pdbx_serial_crystallography_sample_delivery") for label in labels)

    def test_negative_stain(self, pdb_loader):
        ds = pdb_loader.load("2C8I").dataset
        prep = next(p for p in ds.sample_preparations if p.cryoem_preparation)
        assert prep.cryoem_preparation.stain_material


class TestSyntheticEntities:
    """Polymer types no captured entry has, built by editing a captured entity."""

    @staticmethod
    def _loader_with(entity_patch):
        class PatchedLoader(PDBLoader):
            def _get(self, path, cache_key=None):
                record = read_pdb_fixture(path)
                if path == "core/polymer_entity/1D3Z/1":
                    record = copy.deepcopy(record)
                    entity_patch(record)
                return record

        return PatchedLoader()

    @pytest.mark.parametrize(
        ("polymer_type", "poly_type", "expected"),
        [
            ("NA-hybrid", "polydeoxyribonucleotide/polyribonucleotide hybrid", "dna_rna_hybrid"),
            ("Other", "peptide nucleic acid", "peptide_nucleic_acid"),
        ],
    )
    def test_hybrids_and_analogues_are_nucleic_acids(self, polymer_type, poly_type, expected):
        def patch(record):
            record["entity_poly"].update(
                rcsb_entity_polymer_type=polymer_type, type=poly_type, pdbx_seq_one_letter_code_can="ACGUACGT"
            )

        ds = self._loader_with(patch).load("1D3Z").dataset
        assert ds.samples[0].sample_type == "nucleic_acid"
        assert ds.nucleic_acids[0].nucleic_acid_type == expected
        assert ds.sample_nucleic_acid_associations[0].role == "target"

    def test_sequence_outside_the_alphabet_is_dropped_with_a_warning(self):
        def patch(record):
            record["entity_poly"].update(
                rcsb_entity_polymer_type="RNA", type="polyribonucleotide",
                pdbx_seq_one_letter_code_can="ACG(5MC)U", rcsb_sample_sequence_length=5,
            )

        result = self._loader_with(patch).load("1D3Z")
        rna = result.dataset.nucleic_acids[0]
        assert rna.nucleotide_sequence is None
        assert rna.sequence_length == 5
        assert any("nucleotide alphabet" in w for w in result.warnings)


def test_raw_data_is_keyed_by_record_kind(pdb_loader):
    raw = pdb_loader.load("7ZYI").raw_data
    assert set(raw) == {
        "entry", "polymer_entity", "nonpolymer_entity", "branched_entity", "chemcomp", "assembly", "interface",
    }
    assert len(raw["interface"]) == 4


def test_list_entries_uses_cache(mocker, tmp_path):
    response = mocker.Mock()
    response.status_code = 200
    response.text = '{"result_set":[{"identifier":"1ABC"},{"identifier":"2DEF"}]}'
    response.raise_for_status = mocker.Mock()
    post_mock = mocker.patch("lambda_ber_schema.loaders.pdb.requests.post", return_value=response)

    loader = PDBLoader(cache=ResponseCache(cache_dir=tmp_path, enabled=True))
    assert loader.list_entries(limit=2) == ["1ABC", "2DEF"]
    assert loader.list_entries(limit=2) == ["1ABC", "2DEF"]
    assert post_mock.call_count == 1


def test_missing_record_is_none_not_an_error(mocker):
    response = mocker.Mock(status_code=404)
    mocker.patch("lambda_ber_schema.loaders.pdb.requests.get", return_value=response)
    assert PDBLoader()._get("core/chemcomp/XXX") is None


@pytest.mark.integration
@pytest.mark.slow
class TestPDBLoaderIntegration:
    """Integration tests that hit the real PDB API."""

    def test_load_real_entry(self):
        result = PDBLoader().load("7ZYI")
        assert result.dataset.id == "pdb:7ZYI"

    def test_list_entries_by_method(self):
        entries = PDBLoader().list_entries(experimental_method="X-RAY", limit=5)
        assert len(entries) == 5
