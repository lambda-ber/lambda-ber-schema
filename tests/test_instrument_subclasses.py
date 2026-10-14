"""Instrument subclasses in collections typed Instrument (issue #128).

``Dataset.instruments`` is typed ``Instrument``. The ``instrument_type`` designator is what lets an
entry there be a ``CryoEMInstrument`` (or another subclass) and keep that subclass's fields. These
tests pin it in each generated layer that loads Dataset records: the Pydantic models the loaders
build, and the Python dataclasses plus RDF dump that ``linkml-run-examples`` (``make test``) uses.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from lambda_ber_schema import pydantic as model

REPO = Path(__file__).resolve().parent.parent
SCHEMA = REPO / "src" / "lambda_ber_schema" / "schema" / "lambda_ber_schema.yaml"
EMSL_RECORD = REPO / "tests" / "data" / "valid" / "Dataset-emsl-serialem-krios.yaml"

#: The fields each class requires beyond Instrument's own.
REQUIRED_EXTRAS = {"BeamlineInstrument": {"techniques_supported": ["saxs"]}}

INSTRUMENT_CLASSES = [
    "Instrument",
    "CryoEMInstrument",
    "XRayInstrument",
    "SANSInstrument",
    "SAXSInstrument",
    "BeamlineInstrument",
]


def emsl_record() -> dict:
    return yaml.safe_load(EMSL_RECORD.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------------------
# schema shape
# --------------------------------------------------------------------------------------


def test_designator_is_a_schema_wide_slot():
    """Kept out of Instrument's attributes on purpose.

    As an attribute, LinkML's Python generator emits a stray ``unknown_instrument_type``
    assignment and the RDF dump then fails (linkml/linkml#2107, #3663). Moving it back would pass
    every Pydantic test below and break only ``make test``, so it is pinned here as well.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(SCHEMA))
    assert "instrument_type" in view.schema.slots
    assert view.get_slot("instrument_type").designates_type
    assert "instrument_type" not in (view.get_class("Instrument").attributes or {})
    assert "instrument_type" in view.get_class("Instrument").slots


# --------------------------------------------------------------------------------------
# Pydantic, as the loaders use it
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("class_name", INSTRUMENT_CLASSES)
def test_objects_built_in_code_name_their_own_class(class_name):
    """A loader never has to set instrument_type: the class fills it in."""
    cls = getattr(model, class_name)
    extras = REQUIRED_EXTRAS.get(class_name, {})
    instrument = cls(id=f"lambdaber:{class_name}", instrument_code="X", **extras)
    assert instrument.instrument_type == class_name


def test_dataset_loads_a_cryoem_instrument_with_its_fields():
    dataset = model.Dataset(**emsl_record())
    (krios,) = dataset.instruments
    assert type(krios) is model.CryoEMInstrument
    assert krios.cs.numeric_value == 2.7
    assert krios.detector_model == "K3"


def test_dataset_round_trips_the_subclass():
    dumped = model.Dataset(**emsl_record()).model_dump(exclude_none=True, mode="json")
    assert dumped["instruments"][0]["instrument_type"] == "CryoEMInstrument"
    reloaded = model.Dataset(**dumped)
    assert type(reloaded.instruments[0]) is model.CryoEMInstrument


def test_mixed_instruments_keep_their_classes():
    plain = model.Instrument(id="lambdaber:i1", instrument_code="BENCH-1")
    xray = model.XRayInstrument(id="lambdaber:i2", instrument_code="ALS-8.3.1")
    cryo = model.CryoEMInstrument(id="lambdaber:i3", instrument_code="KRIOS-1")
    dumped = model.Dataset(
        id="lambdaber:mixed", instruments=[plain, xray, cryo]
    ).model_dump(exclude_none=True, mode="json")
    reloaded = model.Dataset(**dumped)
    assert [type(i).__name__ for i in reloaded.instruments] == [
        "Instrument",
        "XRayInstrument",
        "CryoEMInstrument",
    ]


# --------------------------------------------------------------------------------------
# Python dataclasses and RDF, as linkml-run-examples uses them
# --------------------------------------------------------------------------------------


@pytest.fixture(scope="module")
def dataclasses():
    from linkml.generators.pythongen import PythonGenerator

    return PythonGenerator(str(SCHEMA)).compile_module()


def test_dataclasses_load_and_dump_rdf_without_a_stray_slot(dataclasses):
    """The failure #128 was opened for: ``No such slot unknown_instrument_type``."""
    from linkml_runtime.dumpers import rdflib_dumper
    from linkml_runtime.loaders import yaml_loader
    from linkml_runtime.utils.schemaview import SchemaView

    dataset = yaml_loader.load(str(EMSL_RECORD), target_class=dataclasses.Dataset)
    (krios,) = dataset.instruments
    assert type(krios).__name__ == "CryoEMInstrument"
    assert not hasattr(krios, "unknown_instrument_type")

    turtle = rdflib_dumper.dumps(dataset, SchemaView(str(SCHEMA)))
    assert "CryoEMInstrument" in turtle
    assert "detector_model" in turtle


def test_dataclasses_reject_subclass_fields_without_the_designator(dataclasses):
    """Without instrument_type an entry is a plain Instrument, which has no ``cs``.

    This is the behaviour that makes the example runner catch a record that forgot to name its
    class, rather than silently dropping the field.
    """
    from linkml_runtime.loaders import yaml_loader

    record = emsl_record()
    del record["instruments"][0]["instrument_type"]
    with pytest.raises(TypeError, match="unexpected keyword argument"):
        yaml_loader.load_any(record, target_class=dataclasses.Dataset)


def test_pydantic_rejects_another_subclass_fields():
    """The designator picks one class; fields of a sibling class are not quietly accepted."""
    from pydantic import ValidationError

    record = emsl_record()
    record["instruments"][0]["techniques_supported"] = ["cryo_em"]  # a BeamlineInstrument field
    with pytest.raises(ValidationError, match="techniques_supported"):
        model.Dataset(**record)


def test_dataclasses_reject_another_subclass_fields(dataclasses):
    from linkml_runtime.loaders import yaml_loader

    record = emsl_record()
    record["instruments"][0]["techniques_supported"] = ["cryo_em"]
    with pytest.raises(TypeError, match="techniques_supported"):
        yaml_loader.load_any(record, target_class=dataclasses.Dataset)
