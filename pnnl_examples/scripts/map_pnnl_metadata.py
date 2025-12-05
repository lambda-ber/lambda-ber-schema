import yaml
import sys
import os

# Ensure src is in path to import lambda_ber_schema
# Assuming this script is run from the root of the repository
sys.path.append(os.path.join(os.getcwd(), "src"))

try:
    from lambda_ber_schema.pydantic import (
        Dataset,
        Study,
        Sample,
        CryoEMInstrument,
        ExperimentRun,
        DataCollectionStrategy,
        ExperimentalConditions,
        TechniqueEnum,
        BufferComposition,
        ConcentrationUnitEnum,
    )
except ImportError as e:
    print(f"Error importing Lambda-BER schema classes: {e}")
    print(
        "Please ensure you are running this script from the repository root and 'src' is in your python path."
    )
    sys.exit(1)


def map_pnnl_metadata(yaml_path: str, verbose: bool = False):
    """
    Maps PNNL metadata.yaml to Lambda-BER Pydantic models.
    """
    import subprocess
    import datetime

    # Generate timestamp and filenames
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_yaml = f"mapped_pnnl_data_{timestamp}.yaml"
    output_log = f"mapped_pnnl_data_{timestamp}.log"

    def log(msg):
        """Log message to file and optionally to console"""
        with open(output_log, "a") as f:
            f.write(msg + "\n")
        if verbose:
            print(msg)

    log(f"Loading metadata from: {yaml_path}")
    log(f"Log file: {output_log}")
    log(f"Output YAML: {output_yaml}")

    try:
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        log(f"File not found: {yaml_path}")
        return

    metadata = data.get("metadata", {})
    program = metadata.get("program", {})
    conditions = data.get("conditions", {})

    missing_fields_log = []

    def log_map(pnnl_field, lambda_field, pnnl_value, lambda_value=None):
        target_val = lambda_value if lambda_value is not None else pnnl_value
        msg = f"🔗 [MAP]  PNNL '{pnnl_field}' ('{pnnl_value}') ➔ Lambda '{lambda_field}' ('{target_val}')"
        log(msg)

    def log_warn(msg):
        full_msg = f"⚠️  [WARN] {msg}"
        log(full_msg)
        missing_fields_log.append(msg)

    def log_new(msg):
        log(f"✨ [NEW]  {msg}")

    # Prioritize the misspelled 'assesments' key as it is currently used in PNNL metadata
    assessments = data.get("assesments")
    if assessments:
        log_warn(
            "Metadata contains misspelled key 'assesments'. Please consider updating to 'assessments'."
        )
    else:
        # Fallback to correct spelling
        assessments = data.get("assessments", {})

    # --- 1. Study ---
    # Mapping proposal_id to Study ID
    proposal_id = str(program.get("proposal_id", "unknown"))
    study = Study(
        id=f"proposal_{proposal_id}",
        title=f"Proposal {proposal_id}",
        description="Imported from PNNL metadata",
    )
    log_map("program.proposal_id", "Study.id", proposal_id)
    log_new(f"Created Study: {study.id}")

    # --- 2. Sample ---
    # Mapping sample info
    sample_name = program.get("short_sample_name", "unknown")
    sample_id = f"sample_{sample_name.replace(' ', '_')}"
    log_map("program.short_sample_name", "Sample.sample_code", sample_name)

    # Buffer composition
    buffer_str = conditions.get("sample_buffer")
    buffer_comp = None
    if buffer_str:
        # Simple mapping: treat the whole string as one component for now
        # In a real scenario, we might parse this string
        buffer_comp = BufferComposition(components=[str(buffer_str)])
        log_map("conditions.sample_buffer", "BufferComposition.components", buffer_str)

    # Concentration
    conc_val = conditions.get("sample_mg/ml")
    concentration = None
    if conc_val is not None:
        try:
            concentration = float(conc_val)
            log_map("conditions.sample_mg/ml", "Sample.concentration", concentration)
        except ValueError:
            log_warn(f"Could not parse concentration '{conc_val}' as float")

    sample = Sample(
        id=sample_id,
        sample_code=sample_name,
        sample_type="protein",  # Defaulting to protein as per context, though not explicit in yaml
        concentration=concentration,
        concentration_unit=ConcentrationUnitEnum.mg_per_ml if concentration else None,
        buffer_composition=buffer_comp,
    )
    log_new(f"Created Sample: {sample.id}")

    # --- 3. Instrument (CryoEM) ---
    # Mapping instrument info
    inst_id_val = program.get("instrument_id", "unknown")
    inst_id = f"inst_{inst_id_val}"
    log_map("program.instrument_id", "CryoEMInstrument.instrument_code", inst_id_val)

    # Detector mapping
    det_id = program.get("detector_id", "")
    log_map("program.detector_id", "CryoEMInstrument.detector_model", det_id)

    # Voltage
    voltage = program.get("voltage")
    if voltage:
        log_map("program.voltage", "CryoEMInstrument.accelerating_voltage", voltage)
    if voltage not in [120, 200, 300]:
        log_warn(
            f"Voltage {voltage} might not match constrained values [120, 200, 300] in schema."
        )

    instrument = CryoEMInstrument(
        id=inst_id,
        instrument_code=str(inst_id_val),
        accelerating_voltage=voltage,
        detector_model=str(
            det_id
        ),  # Mapping detector ID to detector model (e.g., K3, Ceta-D)
        phase_plate=program.get("phase_plate"),
    )
    if program.get("phase_plate") is not None:
        log_map(
            "program.phase_plate",
            "CryoEMInstrument.phase_plate",
            program.get("phase_plate"),
        )

    # CryoEM-specific instrument fields
    if program.get("cs") is not None:
        log_map("program.cs", "CryoEMInstrument.cs", program["cs"])
        instrument.cs = program["cs"]
    if program.get("spot_size") is not None:
        log_map("program.spot_size", "CryoEMInstrument.spotsize", program["spot_size"])
        instrument.spotsize = program["spot_size"]
    if program.get("c2_aperture") is not None:
        log_map(
            "program.c2_aperture",
            "CryoEMInstrument.c2_aperture",
            program["c2_aperture"],
        )
        instrument.c2_aperture = program["c2_aperture"]
    if program.get("detector_physical_pixel_size") is not None:
        log_map(
            "program.detector_physical_pixel_size",
            "CryoEMInstrument.pixel_size_physical_um",
            program["detector_physical_pixel_size"],
        )
        instrument.pixel_size_physical_um = program["detector_physical_pixel_size"]

    log_new(f"Created CryoEMInstrument: {instrument.id}")

    # --- 4. ExperimentRun ---
    session_id = program.get("session_id", "unknown")
    run_id = f"run_{session_id}"
    log_map("program.session_id", "ExperimentRun.experiment_code", session_id)

    # DataCollectionStrategy
    # Note: pydantic.py DataCollectionStrategy seems to lack pixel_size_calibrated.
    # We will use ExperimentRun.pixel_size_x if available, or just warn.

    strategy = DataCollectionStrategy(
        total_dose=program.get("total_dose"),
        frame_rate=program.get("frames_per_second"),
        beam_size_um=program.get("beam_diameter"),
    )
    if program.get("total_dose"):
        log_map(
            "program.total_dose",
            "DataCollectionStrategy.total_dose",
            program.get("total_dose"),
        )
    if program.get("frames_per_second") is not None:
        log_map(
            "program.frames_per_second",
            "DataCollectionStrategy.frame_rate",
            program.get("frames_per_second"),
        )
    if program.get("beam_diameter"):
        log_map(
            "program.beam_diameter",
            "DataCollectionStrategy.beam_size_um",
            program.get("beam_diameter"),
        )

    if "nominal_pixel_size" in program:
        log_warn(
            f"Field 'nominal_pixel_size' ({program['nominal_pixel_size']} A) not found in DataCollectionStrategy Pydantic model."
        )

    # ExperimentalConditions
    exp_conditions = ExperimentalConditions(
        exposure_time=program.get("total_exposure"),
        # Missing:
        # - nominal_camera_Length
    )
    if program.get("total_exposure"):
        log_map(
            "program.total_exposure",
            "ExperimentalConditions.exposure_time",
            program.get("total_exposure"),
        )

    # Handle binning_factor (must be int)
    binning = program.get("binning_factor")
    if binning is not None and isinstance(binning, float) and not binning.is_integer():
        log_warn(
            f"Skipping 'binning_factor' ({binning}) because it is not an integer (required by schema)."
        )
        binning = None
    elif binning is not None:
        binning = int(binning)

    run = ExperimentRun(
        id=run_id,
        experiment_code=str(session_id),
        sample_id=sample.id,
        instrument_id=instrument.id,
        technique=TechniqueEnum.cryo_em,
        data_collection_strategy=strategy,
        experimental_conditions=exp_conditions,
        magnification=program.get("nominal_magnification"),
        camera_binning=binning,
        dose_rate=program.get("nominal_dose_rate_eps"),
        # Mapping pixel size to ExperimentRun fields as fallback if they exist
        pixel_size_x=program.get(
            "nominal_pixel_size"
        ),  # Note: ExperimentRun has pixel_size_x in um? Schema says um. PNNL says Angstrom.
        # Schema pydantic says: pixel_size_x: Optional[float] ... description="Pixel size X dimension in micrometers"
        # PNNL nominal_pixel_size is 0.34 Angstrom.
        # So we need to convert: 0.34 A = 0.000034 um.
    )

    if program.get("nominal_magnification") is not None:
        log_map(
            "program.nominal_magnification",
            "ExperimentRun.magnification",
            program.get("nominal_magnification"),
        )
    if binning is not None:
        log_map("program.binning_factor", "ExperimentRun.camera_binning", binning)
    if program.get("nominal_dose_rate_eps") is not None:
        log_map(
            "program.nominal_dose_rate_eps",
            "ExperimentRun.dose_rate",
            program.get("nominal_dose_rate_eps"),
        )

    # Conversion for pixel size if we map it to ExperimentRun.pixel_size_x
    if program.get("nominal_pixel_size"):
        # 1 Angstrom = 1e-4 micrometers
        run.pixel_size_x = float(program["nominal_pixel_size"]) * 1e-4
        run.pixel_size_y = float(program["nominal_pixel_size"]) * 1e-4
        log_map(
            "program.nominal_pixel_size",
            "ExperimentRun.pixel_size_x/y",
            f"{program['nominal_pixel_size']} A",
            f"{run.pixel_size_x} um",
        )

    log_new(f"Created ExperimentRun: {run.id}")

    # --- 5. Assessments (Missing in Schema) ---
    if assessments:
        log_warn(
            "'assessments' block in metadata (ice_contamination, ice_quality, particle_concentration) has no corresponding classes in the current schema."
        )

    # --- 6. Dataset Assembly ---
    study.samples = [sample]
    study.instrument_runs = [run]

    dataset = Dataset(
        id=f"dataset_{proposal_id}", studies=[study], instruments=[instrument]
    )
    log_new(f"Created Dataset: {dataset.id}")

    # --- 7. Summary & Output ---
    log("\n" + "=" * 30)
    log("MISSING / UNMAPPED FIELDS SUMMARY")
    log("=" * 30)
    if missing_fields_log:
        for msg in missing_fields_log:
            log(f"- {msg}")
    else:
        log("No missing fields detected.")
    log("=" * 30 + "\n")

    # Save to YAML
    log(f"Saving mapped data to {output_yaml}...")
    try:
        data_dict = dataset.model_dump(exclude_none=True)
    except AttributeError:
        data_dict = dataset.dict(exclude_none=True)

    # WORKAROUND: Pydantic v2 with LinkML generated models might strip subclass fields
    # when the list is typed as the base class (List[Instrument]).
    # We manually re-dump the instruments list to ensure all fields (cs, spotsize, etc.) are included.
    if dataset.instruments:
        data_dict["instruments"] = [
            inst.model_dump(exclude_none=True) for inst in dataset.instruments
        ]

    with open(output_yaml, "w") as f:
        yaml.dump(data_dict, f, sort_keys=False)
    log("Save complete.")

    # Validation
    log("\nRunning LinkML validation...")
    schema_path = "src/lambda_ber_schema/schema/lambda-ber-schema.yaml"
    cmd = ["uv", "run", "linkml-validate", "-s", schema_path, output_yaml]
    log(f"Command: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            log("✅ Validation SUCCESSFUL")
        else:
            log("❌ Validation FAILED")
            log(result.stderr)
    except Exception as e:
        log(f"Error running validation: {e}")

    return study, sample, instrument, run


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Map PNNL metadata to Lambda-BER schema"
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="examples/pnnl_examples/Example_Metadata/metadata.yaml",
        help="Path to input YAML metadata",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging to console"
    )

    args = parser.parse_args()

    if os.path.exists(args.input_file):
        map_pnnl_metadata(args.input_file, args.verbose)
    else:
        print(f"Input file not found: {args.input_file}")
