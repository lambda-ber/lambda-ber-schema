"""Tests for the loader base module."""

import pytest

from lambda_ber_schema.loaders.base import UNIPROT_ACCESSION_RE, uniprot_curie


class TestUniprotCurie:
    """uniprot_curie is the one gate every Protein row passes through."""

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("P69905", "uniprot:P69905"),
            ("  P69905\n", "uniprot:P69905"),
            ("p69905", "uniprot:P69905"),
            ("uniprot:P69905", "uniprot:P69905"),
            ("UniProt:P69905", "uniprot:P69905"),
            ("UNIPROT: P69905 ", "uniprot:P69905"),
            ("P69905-2", "uniprot:P69905-2"),  # isoform suffix
            ("A0A101UQ08", "uniprot:A0A101UQ08"),  # ten-character accession
            ("Q9XCL6", "uniprot:Q9XCL6"),
        ],
    )
    def test_normalizes_to_curie(self, raw, expected):
        assert uniprot_curie(raw) == expected

    @pytest.mark.parametrize(
        "raw",
        [
            "entry",  # the trailing URL segment SimpleScattering once mistook for an accession
            "",
            "   ",
            "12345",
            "P6990",  # too short
            "P699055",  # neither six nor ten characters
            "uniprot:",
            "pdb:1HHO",  # a different database's prefix is not silently accepted
            "P69905-",  # isoform suffix without a number
            "ZZZZZZ",
        ],
    )
    def test_rejects_non_accessions(self, raw):
        assert uniprot_curie(raw) is None

    def test_pattern_matches_the_schema_constraint(self):
        """The loader regex and Protein.uniprot_id's pattern must agree, or a loader could
        build a row the model then rejects."""
        from lambda_ber_schema.pydantic import Protein

        for accession in ["P69905", "A0A101UQ08", "P69905-2"]:
            assert UNIPROT_ACCESSION_RE.match(accession)
            Protein(id=f"uniprot:{accession}", uniprot_id=f"uniprot:{accession}")
