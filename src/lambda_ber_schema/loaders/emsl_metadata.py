import yaml
from typing import Any, TypedDict


class ParsedMetadata(TypedDict):
    experiment_run: dict[str, Any]
    instrument: dict[str, Any]
    sample: dict[str, Any]
    workflow_run: dict[str, Any]
    warnings: list[str]
    notes: str | None


def parse_metadata_yaml(content: bytes | str) -> ParsedMetadata:
    """Parse PNNL metadata.yaml content into schema-ready field dicts.

    Returns ParsedMetadata with four sub-dicts keyed by schema field names.
    Numeric fields use {"numeric_value": float, "unit": str} dicts, compatible
    with _build_epu_quantity_values() in emsl.py. Schema gaps are collected in
    warnings rather than raising exceptions.
    """
    empty: ParsedMetadata = {
        "experiment_run": {},
        "instrument": {},
        "sample": {},
        "workflow_run": {},
        "warnings": [],
        "notes": None,
    }
    try:
        return _parse(content, empty)
    except Exception:
        return empty


# ---------------------------------------------------------------------------
# Internal implementation
# ---------------------------------------------------------------------------

_TECHNIQUE_MAP = {1: "cryo_em", 2: "cryo_et", 3: "microed"}


def _qv(v: Any, unit: str) -> dict[str, Any]:
    return {"numeric_value": float(v), "unit": unit}


def _get(d: Any, *keys: str) -> Any:
    for k in keys:
        if not isinstance(d, dict) or k not in d:
            return None
        d = d[k]
    return d


def _parse(content: bytes | str, empty: ParsedMetadata) -> ParsedMetadata:
    if isinstance(content, bytes):
        content = content.decode("utf-8", errors="replace")

    raw = yaml.safe_load(content)
    if not isinstance(raw, dict):
        return empty

    prog: dict = _get(raw, "metadata", "program") or {}
    conditions: dict = raw.get("conditions") or {}
    assessments: dict = raw.get("assessments") or raw.get("assesments") or {}
    notes = raw.get("notes")

    warnings: list[str] = []
    exp: dict[str, Any] = {}
    inst: dict[str, Any] = {}
    samp: dict[str, Any] = {}
    wf: dict[str, Any] = {}

    # --- proposal_id (schema gap: no Study.proposal_id) ---
    if prog.get("proposal_id") is not None:
        warnings.append(
            "proposal_id: no Study.proposal_id field in schema — value collected but not mapped"
        )

    # --- ExperimentRun ---
    if (v := prog.get("session_id")) is not None:
        exp["experiment_code"] = str(v)

    if (v := prog.get("nominal_pixel_size")) is not None:
        exp["calibrated_pixel_size"] = _qv(v, "Å/pixel")

    if (v := prog.get("total_dose")) is not None:
        exp["total_dose"] = _qv(v, "e-/Å²")

    if (v := prog.get("nominal_dose_rate_eps")) is not None:
        exp["dose_rate"] = _qv(v, "e-/Å²/s")

    if (v := prog.get("total_exposure")) is not None:
        # YAML is seconds; schema total_exposure_time description says milliseconds
        exp["total_exposure_time"] = _qv(float(v) * 1000, "ms")

    if (v := prog.get("processing_scheme")) is not None:
        technique = _TECHNIQUE_MAP.get(int(v))
        if technique:
            exp["technique"] = technique
            if v == 3:
                warnings.append(
                    "processing_scheme: 3 (microed) — microed is absent from TechniqueEnum in schema; value stored as string"
                )
        else:
            warnings.append(f"processing_scheme: {v} — unknown value, not mapped")

    if (v := prog.get("nominal_magnification")) is not None:
        # YAML unit is kx; schema magnification uses x
        exp["magnification"] = _qv(float(v) * 1000, "x")

    if (v := prog.get("binning_factor")) is not None:
        exp["camera_binning"] = _qv(v, "")

    # tomo / diffraction gaps — warn if non-null
    _gap_warn(prog, "frames_per_second", warnings, "no ExperimentRun field in schema")
    _gap_warn(prog, "nominal_camera_Length", warnings, "no ExperimentRun.camera_length field in schema")
    _gap_warn(prog, "tilting_mode", warnings, "no ExperimentRun.tilting_scheme field in schema")
    _gap_warn(prog, "tilt_angle_increment", warnings, "no ExperimentRun field in schema")
    _gap_warn(prog, "fiducial_size", warnings, "no ExperimentRun field in schema")
    _gap_warn(prog, "rotation_rate", warnings, "no ExperimentRun field in schema")

    # --- CryoEMInstrument ---
    if (v := prog.get("instrument_id")) is not None:
        inst["instrument_code"] = str(v)

    if (v := prog.get("voltage")) is not None:
        inst["accelerating_voltage"] = _qv(v, "kV")

    if (v := prog.get("cs")) is not None:
        inst["cs"] = _qv(v, "mm")

    if (v := prog.get("detector_id")) is not None:
        # cryo-EM detector identity belongs on CryoEMInstrument.detector_model
        inst["detector_model"] = str(v)

    if (v := prog.get("detector_physical_pixel_size")) is not None:
        inst["pixel_size_physical_um"] = _qv(v, "µm")

    if (v := prog.get("c2_aperture")) is not None:
        inst["c2_aperture"] = _qv(v, "µm")

    if (v := prog.get("spot_size")) is not None:
        inst["spotsize"] = _qv(v, "")

    if (v := prog.get("beam_diameter")) is not None:
        inst["tem_beam_diameter"] = _qv(v, "µm")

    if (v := prog.get("energy_filter_slit")) is not None:
        inst["energy_filter_slit_width"] = _qv(v, "eV")

    if (v := prog.get("phase_plate")) is not None:
        inst["phase_plate"] = bool(v)

    # --- Sample ---
    if (v := prog.get("short_sample_name")) is not None:
        samp["sample_code"] = str(v).strip()

    if (v := conditions.get("sample_mg/ml")) is not None:
        samp["concentration"] = _qv(v, "mg/mL")

    if (v := conditions.get("sample_buffer")) is not None:
        # BufferComposition.components is a multivalued string list
        samp["buffer_composition"] = {"components": [str(v)]}

    if conditions.get("vitrification_settings") is not None:
        warnings.append(
            "vitrification_settings: SamplePreparation.protocol_description exists but requires "
            "preparation_type and sample_id — cannot map without required fields"
        )

    # --- WorkflowRun ---
    if (v := prog.get("motCorr_bin")) is not None:
        wf["motion_correction_params"] = {"binning": _qv(v, "")}

    topaz = prog.get("topaz_model")
    if topaz is not None and str(topaz).strip().upper() != "NA":
        wf["particle_picking_params"] = {"model_name": str(topaz)}

    # --- Assessments (schema gaps) ---
    for field in ("ice_contamination", "ice_quality", "particle_concentration"):
        if assessments.get(field) is not None:
            warnings.append(
                f"{field}: no ExperimentRun field in schema — value collected but not mapped"
            )

    return {
        "experiment_run": exp,
        "instrument": inst,
        "sample": samp,
        "workflow_run": wf,
        "warnings": warnings,
        "notes": str(notes) if notes is not None else None,
    }


def _gap_warn(d: dict, key: str, warnings: list[str], reason: str) -> None:
    if d.get(key) is not None:
        warnings.append(f"{key}: {reason}")
