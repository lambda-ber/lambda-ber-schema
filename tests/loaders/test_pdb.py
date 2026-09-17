"""Tests for PDB loader."""

import pytest

from lambda_ber_schema.loaders.pdb import PDBLoader
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.pydantic import (
    Dataset,
    TechniqueEnum,
    XRayInstrument,
)


@pytest.fixture
def loader(mocker, pdb_1hho_entry_response, pdb_1hho_polymer_entities):
    """Create loader with mocked HTTP client."""
    loader = PDBLoader()
    mocker.patch.object(loader, "_fetch_entry",
                        return_value=pdb_1hho_entry_response)
    mocker.patch.object(
        loader, "_fetch_polymer_entities", return_value=pdb_1hho_polymer_entities
    )
    return loader


def _synthetic_entity(
    entity_id: str, polymer_type: str, poly_type: str, sequence: str, strand: str, length: int | None = None
) -> dict:
    """The few polymer-entity fields the loader reads, for cases no fixture entry covers."""
    return {
        "entity_poly": {
            "rcsb_entity_polymer_type": polymer_type,
            "type": poly_type,
            "pdbx_seq_one_letter_code_can": sequence,
            "pdbx_strand_id": strand,
            "rcsb_sample_sequence_length": length if length is not None else len(sequence),
        },
        "rcsb_polymer_entity": {"pdbx_description": f"Synthetic {polymer_type}", "pdbx_number_of_molecules": 1},
        "rcsb_polymer_entity_container_identifiers": {"entity_id": entity_id},
    }


class TestPDBLoader:
    """Tests for PDBLoader."""

    def test_load_returns_loader_result(self, loader):
        """Test that load() returns a LoaderResult."""
        result = loader.load("1HHO")
        assert result is not None
        assert result.dataset is not None
        assert isinstance(result.dataset, Dataset)

    def test_dataset_has_correct_id(self, loader):
        """Test dataset ID is prefixed and uppercase."""
        result = loader.load("1hho")
        assert result.dataset.id == "pdb:1HHO"

    def test_dataset_has_title(self, loader):
        """Test dataset title is extracted from struct."""
        result = loader.load("1HHO")
        assert "OXYHAEMOGLOBIN" in result.dataset.title

    def test_loader_result_has_source_url(self, loader):
        """Test LoaderResult includes the human-readable PDB structure URL."""
        result = loader.load("1HHO")
        assert result.source_url == "https://www.rcsb.org/structure/1HHO"

    def test_loader_result_has_pdb_doi(self, loader):
        """Test LoaderResult includes the standardized PDB DOI URL."""
        result = loader.load("1HHO")
        assert result.doi == "https://doi.org/10.2210/pdb1hho/pdb"

    def test_samples_created_from_polymer_entities(self, loader):
        """Test Sample objects are created from polymer entities."""
        result = loader.load("1HHO")
        assert len(result.dataset.samples) == 2  # Alpha and Beta chains

        # Check first sample (alpha chain)
        alpha = result.dataset.samples[0]
        assert alpha.sample_code == "PDB-1HHO-1"
        assert alpha.sample_type == "protein"
        assert "ALPHA" in alpha.protein_name

    def test_sample_has_organism(self, loader):
        """Test Sample has organism from source organism, as an NCBITaxon CURIE."""
        result = loader.load("1HHO")
        sample = result.dataset.samples[0]
        assert sample.organism == "NCBITaxon:9606"

    def test_proteins_created_from_uniprot_mappings(self, loader):
        """One Protein per UniProt accession, keyed by CURIE."""
        result = loader.load("1HHO")
        proteins = {p.id: p for p in result.dataset.proteins}
        assert set(proteins) == {"uniprot:P69905", "uniprot:P68871"}

        alpha = proteins["uniprot:P69905"]
        assert alpha.uniprot_id == "uniprot:P69905"
        # UniProt-derived name preferred over the depositor's description
        assert alpha.protein_name == "Hemoglobin subunit alpha"
        assert alpha.organism == "NCBITaxon:9606"
        assert alpha.organism_name == "Homo sapiens"
        assert alpha.pdb_entries == ["pdb:1HHO"]
        # The deposited sequence is the construct, not the canonical one; left for enrichment
        assert alpha.amino_acid_sequence is None

    def test_sample_protein_associations_carry_entity_detail(self, loader):
        """Chain ids, copy number and reference coverage describe this entity, not the protein."""
        result = loader.load("1HHO")
        ds = result.dataset
        assocs = {a.protein_id: a for a in ds.sample_protein_associations}
        assert len(assocs) == 2

        alpha = assocs["uniprot:P69905"]
        assert alpha.sample_id == ds.samples[0].id
        assert alpha.role == "subunit"  # two polymer entities make up the assembly
        assert alpha.chain_ids == ["A"]
        assert alpha.copy_number == 1
        assert alpha.sequence_coverage is not None
        assert 0.99 <= alpha.sequence_coverage <= 1.0

    def test_no_nucleic_acids_for_a_protein_only_entry(self, loader):
        """Hemoglobin has no DNA or RNA entity, so the table is absent rather than empty."""
        result = loader.load("1HHO")
        assert result.dataset.nucleic_acids is None
        assert result.dataset.sample_nucleic_acid_associations is None

    def test_sample_has_molecular_weight(self, loader):
        """Test Sample has molecular weight from entity."""
        result = loader.load("1HHO")
        sample = result.dataset.samples[0]
        assert sample.molecular_weight is not None
        assert sample.molecular_weight.numeric_value > 10  # ~15 kDa
        assert sample.molecular_weight.unit == "kDa"

    def test_instrument_is_xray_instrument(self, loader):
        """Test Instrument is XRayInstrument."""
        result = loader.load("1HHO")
        assert len(result.dataset.instruments) == 1
        instrument = result.dataset.instruments[0]
        assert isinstance(instrument, XRayInstrument)

    def test_experiment_run_has_xray_technique(self, loader):
        """Test ExperimentRun uses X-ray crystallography technique."""
        result = loader.load("1HHO")
        assert len(result.dataset.experiment_runs) == 1
        exp = result.dataset.experiment_runs[0]
        assert exp.technique == TechniqueEnum.xray_crystallography

    def test_experiment_run_has_quality_metrics(self, loader):
        """Test ExperimentRun has quality metrics."""
        result = loader.load("1HHO")
        exp = result.dataset.experiment_runs[0]

        assert exp.quality_metrics is not None
        # Resolution
        assert exp.quality_metrics.resolution is not None
        assert exp.quality_metrics.resolution.numeric_value == 2.1
        assert exp.quality_metrics.resolution.unit == "Angstroms"

        # Space group
        assert exp.quality_metrics.space_group == "P 41 21 2"

    def test_experiment_run_has_unit_cell(self, loader):
        """Test ExperimentRun has unit cell parameters."""
        result = loader.load("1HHO")
        exp = result.dataset.experiment_runs[0]

        assert exp.quality_metrics.unit_cell_a is not None
        assert exp.quality_metrics.unit_cell_a.numeric_value == 53.7
        assert exp.quality_metrics.unit_cell_a.unit == "Angstroms"

    def test_experiment_run_has_r_work(self, loader):
        """Test ExperimentRun has R-work from refinement."""
        result = loader.load("1HHO")
        exp = result.dataset.experiment_runs[0]

        assert exp.quality_metrics.r_work is not None
        assert exp.quality_metrics.r_work.numeric_value == 0.223

    def test_experiment_run_has_date(self, loader):
        """Test ExperimentRun has deposition date."""
        result = loader.load("1HHO")
        exp = result.dataset.experiment_runs[0]
        assert exp.experiment_date == "1983-06-10"

    def test_workflow_runs_created(self, loader):
        """Test WorkflowRuns are created for refinement."""
        result = loader.load("1HHO")
        workflows = result.dataset.workflow_runs

        assert len(workflows) >= 1
        refine = workflows[0]
        assert refine.workflow_type == "refinement"

    def test_data_files_created(self, loader):
        """Test DataFiles are created for PDB files."""
        result = loader.load("1HHO")
        files = result.dataset.data_files

        assert len(files) >= 2
        # Should have PDB format
        pdb_file = next((f for f in files if f.file_format == "pdb"), None)
        assert pdb_file is not None
        assert pdb_file.file_name == "1hho.pdb"

        # Should have mmCIF format
        cif_file = next((f for f in files if f.file_format == "mmcif"), None)
        assert cif_file is not None

    def test_association_tables_created(self, loader):
        """Test association tables link entities."""
        result = loader.load("1HHO")
        ds = result.dataset

        # Study-Sample associations (2 samples)
        assert ds.study_sample_associations is not None
        assert len(ds.study_sample_associations) == 2

        # Study-Experiment association
        assert ds.study_experiment_associations is not None
        assert len(ds.study_experiment_associations) == 1

        # Experiment-Sample associations (2 samples)
        assert ds.experiment_sample_associations is not None
        assert len(ds.experiment_sample_associations) == 2

        # Experiment-Instrument association
        assert ds.experiment_instrument_associations is not None
        assert len(ds.experiment_instrument_associations) == 1

    @pytest.mark.parametrize(
        ("polymer_type", "poly_type", "expected"),
        [
            ("NA-hybrid", "polydeoxyribonucleotide/polyribonucleotide hybrid", "dna_rna_hybrid"),
            ("Other", "peptide nucleic acid", "peptide_nucleic_acid"),
        ],
    )
    def test_nucleic_acid_sample_type_covers_hybrids_and_analogues(
        self, mocker, pdb_1hho_entry_response, polymer_type, poly_type, expected
    ):
        """An NA-hybrid or PNA entity is a nucleic acid sample, not a complex."""
        loader = PDBLoader()
        entity = _synthetic_entity("1", polymer_type, poly_type, "ACGUACGT", "A")
        mocker.patch.object(loader, "_fetch_entry", return_value=pdb_1hho_entry_response)
        mocker.patch.object(loader, "_fetch_polymer_entities", return_value=[entity])
        result = loader.load("1HHO")
        assert result.dataset.samples[0].sample_type == "nucleic_acid"
        assert result.dataset.nucleic_acids[0].nucleic_acid_type == expected
        # A lone strand with no protein in the entry is the target
        assert result.dataset.sample_nucleic_acid_associations[0].role == "target"

    def test_strands_beside_several_proteins_are_subunits(
        self, mocker, pdb_1hho_entry_response, pdb_1hho_polymer_entities
    ):
        """With two protein entities the entry is an assembly and a strand is one subunit of it."""
        loader = PDBLoader()
        strand = _synthetic_entity("3", "DNA", "polydeoxyribonucleotide", "ACGTACGT", "E")
        mocker.patch.object(loader, "_fetch_entry", return_value=pdb_1hho_entry_response)
        mocker.patch.object(
            loader, "_fetch_polymer_entities", return_value=pdb_1hho_polymer_entities + [strand]
        )
        result = loader.load("1HHO")
        assert [a.role for a in result.dataset.sample_protein_associations] == ["subunit", "subunit"]
        assert [a.role for a in result.dataset.sample_nucleic_acid_associations] == ["subunit"]

    def test_sequence_outside_the_alphabet_is_dropped_with_a_warning(
        self, mocker, pdb_1hho_entry_response
    ):
        """A modified residue in house notation leaves the sequence empty; the length still arrives."""
        loader = PDBLoader()
        entity = _synthetic_entity("1", "RNA", "polyribonucleotide", "ACG(5MC)U", "A", length=5)
        mocker.patch.object(loader, "_fetch_entry", return_value=pdb_1hho_entry_response)
        mocker.patch.object(loader, "_fetch_polymer_entities", return_value=[entity])
        result = loader.load("1HHO")
        rna = result.dataset.nucleic_acids[0]
        assert rna.nucleotide_sequence is None
        assert rna.sequence_length == 5
        assert any("nucleotide alphabet" in w for w in result.warnings)

    def test_sequence_length_agrees_with_the_sequence(self, mocker, pdb_1hho_entry_response):
        """When the sequence is on the record its length is measured, not copied from the API."""
        loader = PDBLoader()
        entity = _synthetic_entity("1", "DNA", "polydeoxyribonucleotide", "ACGTACGT", "A", length=99)
        mocker.patch.object(loader, "_fetch_entry", return_value=pdb_1hho_entry_response)
        mocker.patch.object(loader, "_fetch_polymer_entities", return_value=[entity])
        result = loader.load("1HHO")
        assert result.dataset.nucleic_acids[0].sequence_length == 8

    def test_raw_data_contains_entry_and_entities(self, loader):
        """Test raw_data contains entry and polymer entity data."""
        result = loader.load("1HHO")
        assert result.raw_data is not None
        assert "entry" in result.raw_data
        assert "polymer_entities" in result.raw_data

    def test_list_entries_uses_cache(self, mocker, tmp_path):
        """Test list_entries caches responses when enabled."""
        response = mocker.Mock()
        response.status_code = 200
        response.text = '{"result_set":[{"identifier":"1ABC"},{"identifier":"2DEF"}]}'
        response.raise_for_status = mocker.Mock()
        post_mock = mocker.patch(
            "lambda_ber_schema.loaders.pdb.requests.post",
            return_value=response,
        )

        cache = ResponseCache(cache_dir=tmp_path, enabled=True)
        loader = PDBLoader(cache=cache)

        first = loader.list_entries(limit=2)
        second = loader.list_entries(limit=2)

        assert first == ["1ABC", "2DEF"]
        assert second == ["1ABC", "2DEF"]
        assert post_mock.call_count == 1


@pytest.mark.integration
@pytest.mark.slow
@pytest.fixture
def dna_loader(mocker, pdb_1aay_entry_response, pdb_1aay_polymer_entities):
    """Loader for 1AAY: Zif268 zinc finger bound to an 11-bp DNA duplex."""
    loader = PDBLoader()
    mocker.patch.object(loader, "_fetch_entry", return_value=pdb_1aay_entry_response)
    mocker.patch.object(
        loader, "_fetch_polymer_entities", return_value=pdb_1aay_polymer_entities
    )
    return loader


class TestPDBLoaderNucleicAcids:
    """A protein-DNA complex: one Protein row, two NucleicAcid rows, three samples."""

    def test_samples_typed_by_polymer(self, dna_loader):
        result = dna_loader.load("1AAY")
        types = [s.sample_type for s in result.dataset.samples]
        assert types == ["nucleic_acid", "nucleic_acid", "protein"]

    def test_protein_name_is_for_protein_samples_only(self, dna_loader):
        """A DNA strand's description is its title, not a protein name."""
        result = dna_loader.load("1AAY")
        strand, _, protein = result.dataset.samples
        assert strand.title.startswith("DNA (5'-D(*AP*GP*CP*GP")
        assert strand.protein_name is None
        assert protein.protein_name == "PROTEIN (ZIF268 ZINC FINGER PEPTIDE)"

    def test_nucleic_acids_created_from_dna_entities(self, dna_loader):
        """Each DNA entity is one NucleicAcid, named by entry and entity, with its sequence."""
        result = dna_loader.load("1AAY")
        ds = result.dataset
        assert [n.id for n in ds.nucleic_acids] == [
            "pdb:1AAY/nucleic_acid/1",
            "pdb:1AAY/nucleic_acid/2",
        ]
        strand = ds.nucleic_acids[0]
        assert strand.nucleic_acid_type == "dna"
        assert strand.nucleic_acid_name.startswith("DNA (5'-D(*AP*GP*CP*GP")
        # The deposited sequence is the molecule itself for a synthetic strand
        assert strand.nucleotide_sequence == "AGCGTGGGCGT"
        assert strand.sequence_length == 11
        assert strand.pdb_entries == ["pdb:1AAY"]
        # This 1997 entry gives the oligonucleotides no source organism
        assert strand.organism is None
        assert not [w for w in result.warnings if "nucleotide alphabet" in w]

    def test_protein_still_created_alongside(self, dna_loader):
        result = dna_loader.load("1AAY")
        assert [p.id for p in result.dataset.proteins] == ["uniprot:P08046"]
        # The lone protein entity is the target
        assert result.dataset.sample_protein_associations[0].role == "target"

    def test_strands_are_binding_partners_of_the_lone_protein(self, dna_loader):
        """With exactly one protein entity, the strands are its binding partners."""
        result = dna_loader.load("1AAY")
        ds = result.dataset
        assocs = {a.nucleic_acid_id: a for a in ds.sample_nucleic_acid_associations}
        assert set(assocs) == {"pdb:1AAY/nucleic_acid/1", "pdb:1AAY/nucleic_acid/2"}
        first = assocs["pdb:1AAY/nucleic_acid/1"]
        assert first.sample_id == ds.samples[0].id
        assert first.role == "binding_partner"
        assert first.chain_ids == ["B"]
        assert first.copy_number == 1
        assert assocs["pdb:1AAY/nucleic_acid/2"].chain_ids == ["C"]

    def test_dataset_validates_against_schema(self, dna_loader):
        """The pydantic model accepts what the loader built, including the new tables."""
        result = dna_loader.load("1AAY")
        assert isinstance(result.dataset, Dataset)
        assert result.dataset.model_dump(exclude_none=True)["nucleic_acids"]


class TestPDBLoaderIntegration:
    """Integration tests that hit the real PDB API."""

    def test_load_real_entry(self):
        """Test loading a real PDB entry."""
        loader = PDBLoader()
        result = loader.load("1HHO")

        assert result.dataset is not None
        assert result.dataset.id == "pdb:1HHO"

    def test_load_cryo_em_entry(self):
        """Test loading a cryo-EM PDB entry."""
        loader = PDBLoader()
        # EMD-23908 / PDB 7MLZ - SARS-CoV-2 spike protein
        result = loader.load("7MLZ")

        assert result.dataset is not None
        exp = result.dataset.experiment_runs[0]
        assert exp.technique == TechniqueEnum.cryo_em

    def test_list_entries(self):
        """Test listing entries from PDB."""
        loader = PDBLoader()
        entries = loader.list_entries(limit=5)

        assert len(entries) == 5
        # Each entry should be a 4-character code
        assert all(len(e) == 4 for e in entries)

    def test_list_entries_by_method(self):
        """Test listing entries filtered by method."""
        loader = PDBLoader()
        entries = loader.list_entries(experimental_method="X-RAY", limit=5)

        assert len(entries) == 5
