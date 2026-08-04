from pathlib import Path
import pytest
from lambda_ber_schema.loaders.emsl_metadata import parse_metadata_yaml

FIXTURE = Path(__file__).parent / "fixtures/emsl/metadata_example.yaml"


@pytest.fixture
def parsed():
    return parse_metadata_yaml(FIXTURE.read_bytes())


# ---------------------------------------------------------------------------
# ExperimentRun fields
# ---------------------------------------------------------------------------


def test_experiment_code(parsed):
    assert parsed["experiment_run"]["experiment_code"] == "10-03-25_C2"


def test_pixel_size(parsed):
    assert parsed["experiment_run"]["calibrated_pixel_size"] == {
        "numeric_value": 0.34,
        "unit": "Å/pixel",
    }


def test_total_dose(parsed):
    assert parsed["experiment_run"]["total_dose"] == {
        "numeric_value": 50.0,
        "unit": "e-/Å²",
    }


def test_null_fields_omitted(parsed):
    # nominal_dose_rate_eps is null in fixture → dose_rate must be absent
    assert "dose_rate" not in parsed["experiment_run"]


def test_total_exposure_ms_conversion():
    # total_exposure is seconds in YAML; schema expects ms
    content = b"""
metadata:
  program:
    session_id: test
    instrument_id: 1
    processing_scheme: 1
    nominal_magnification: 1
    binning_factor: 1
    total_exposure: 2
"""
    result = parse_metadata_yaml(content)
    assert result["experiment_run"]["total_exposure_time"] == {
        "numeric_value": 2000.0,
        "unit": "ms",
    }


def test_magnification_kx_to_x(parsed):
    assert parsed["experiment_run"]["magnification"] == {
        "numeric_value": 130000.0,
        "unit": "x",
    }


def test_binning(parsed):
    assert parsed["experiment_run"]["camera_binning"] == {
        "numeric_value": 0.5,
        "unit": "",
    }


def test_processing_scheme_spa():
    result = parse_metadata_yaml(
        b"metadata:\n  program:\n    processing_scheme: 1\n    session_id: x\n    instrument_id: 1\n    nominal_magnification: 1\n    binning_factor: 1\n"
    )
    assert result["experiment_run"]["technique"] == "cryo_em"


def test_processing_scheme_tomo():
    result = parse_metadata_yaml(
        b"metadata:\n  program:\n    processing_scheme: 2\n    session_id: x\n    instrument_id: 1\n    nominal_magnification: 1\n    binning_factor: 1\n"
    )
    assert result["experiment_run"]["technique"] == "cryo_et"


def test_processing_scheme_microed():
    result = parse_metadata_yaml(
        b"metadata:\n  program:\n    processing_scheme: 3\n    session_id: x\n    instrument_id: 1\n    nominal_magnification: 1\n    binning_factor: 1\n"
    )
    assert result["experiment_run"]["technique"] == "microed"
    assert any("microed" in w.lower() or "processing_scheme" in w for w in result["warnings"])


# ---------------------------------------------------------------------------
# CryoEMInstrument fields
# ---------------------------------------------------------------------------


def test_instrument_code(parsed):
    assert parsed["instrument"]["instrument_code"] == "34303"


def test_voltage(parsed):
    assert parsed["instrument"]["accelerating_voltage"] == {
        "numeric_value": 300.0,
        "unit": "kV",
    }


def test_cs(parsed):
    assert parsed["instrument"]["cs"] == {"numeric_value": 2.7, "unit": "mm"}


def test_detector_model(parsed):
    assert parsed["instrument"]["detector_model"] == "K3"


def test_pixel_size_physical(parsed):
    assert parsed["instrument"]["pixel_size_physical_um"] == {
        "numeric_value": 5.0,
        "unit": "µm",
    }


def test_c2_aperture(parsed):
    assert parsed["instrument"]["c2_aperture"] == {
        "numeric_value": 50.0,
        "unit": "µm",
    }


def test_spot_size(parsed):
    assert parsed["instrument"]["spotsize"] == {"numeric_value": 5.0, "unit": ""}


def test_beam_diameter(parsed):
    assert parsed["instrument"]["tem_beam_diameter"] == {
        "numeric_value": 0.6,
        "unit": "µm",
    }


def test_energy_filter_slit(parsed):
    assert parsed["instrument"]["energy_filter_slit_width"] == {
        "numeric_value": 20.0,
        "unit": "eV",
    }


def test_phase_plate_false(parsed):
    assert parsed["instrument"]["phase_plate"] is False


# ---------------------------------------------------------------------------
# Sample fields
# ---------------------------------------------------------------------------


def test_sample_code(parsed):
    assert parsed["sample"]["sample_code"] == "my sample name"


# ---------------------------------------------------------------------------
# WorkflowRun fields
# ---------------------------------------------------------------------------


def test_motcorr_bin(parsed):
    assert parsed["workflow_run"]["motion_correction_params"]["binning"] == {
        "numeric_value": 1.0,
        "unit": "",
    }


def test_topaz_model_na_omitted(parsed):
    # fixture has topaz_model: NA → should be omitted
    assert "particle_picking_params" not in parsed["workflow_run"]


def test_topaz_model_set():
    content = b"""
metadata:
  program:
    session_id: x
    instrument_id: 1
    processing_scheme: 1
    nominal_magnification: 1
    binning_factor: 1
    motCorr_bin: 1
    topaz_model: unet
"""
    result = parse_metadata_yaml(content)
    assert result["workflow_run"]["particle_picking_params"]["model_name"] == "unet"


# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------


def test_notes(parsed):
    assert parsed["notes"] == "multiline comments can be inserted here"


# ---------------------------------------------------------------------------
# Assessments section (typo tolerance + gap warnings)
# ---------------------------------------------------------------------------


def test_assesments_typo_accepted(parsed):
    # fixture spells it 'assesments' (one s) — must not raise, must produce warnings
    assert "warnings" in parsed
    assert any("ice_contamination" in w for w in parsed["warnings"])


def test_assessments_canonical_accepted():
    content = b"""
metadata:
  program:
    session_id: x
    instrument_id: 1
    processing_scheme: 1
    nominal_magnification: 1
    binning_factor: 1
assessments:
  ice_contamination: 1
  ice_quality: 2
  particle_concentration: 3
"""
    result = parse_metadata_yaml(content)
    assert any("ice_contamination" in w for w in result["warnings"])


# ---------------------------------------------------------------------------
# Gap warnings
# ---------------------------------------------------------------------------


def test_gap_warning_proposal_id(parsed):
    assert any("proposal_id" in w for w in parsed["warnings"])


def test_gap_warning_ice_contamination(parsed):
    assert any("ice_contamination" in w for w in parsed["warnings"])


def test_gap_warning_tilting_mode(parsed):
    assert any("tilting_mode" in w for w in parsed["warnings"])


# ---------------------------------------------------------------------------
# Robustness
# ---------------------------------------------------------------------------


def test_empty_yaml():
    result = parse_metadata_yaml(b"")
    assert result["experiment_run"] == {}
    assert result["instrument"] == {}
    assert result["sample"] == {}
    assert result["workflow_run"] == {}
    assert result["warnings"] == []
    assert result["notes"] is None


def test_invalid_yaml():
    result = parse_metadata_yaml(b"{")
    assert result["experiment_run"] == {}
    assert result["instrument"] == {}
    assert result["sample"] == {}
    assert result["workflow_run"] == {}
    assert result["notes"] is None


def test_partial_yaml():
    result = parse_metadata_yaml(b"metadata:\n  program:\n    voltage: 300\n")
    assert result["instrument"]["accelerating_voltage"] == {
        "numeric_value": 300.0,
        "unit": "kV",
    }
    assert "experiment_code" not in result["experiment_run"]
