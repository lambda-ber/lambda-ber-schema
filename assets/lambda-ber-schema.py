# Auto generated from lambda-ber-schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-13T11:50:15
# Schema: lambda-ber-schema
#
# id: https://w3id.org/lambda-ber-schema/
# description: lambda-ber-schema is a comprehensive schema for representing multimodal structural biology imaging data,
#   from atomic-resolution structures to tissue-level organization. It supports diverse experimental
#   techniques including cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and
#   spectroscopic imaging.
#
#   ## Schema Organization
#
#   The schema follows a hierarchical structure that mirrors how structural biology research is organized:
#
#   The top-level entity is a [Dataset](Dataset.md), which serves as a container for related research.
#   A dataset might represent all data from a specific grant, collaboration, or publication.
#
#   Each dataset contains one or more [Studies](Study.md), which are focused investigations of specific
#   biological questions. For example, a study might investigate "Heat stress response in Arabidopsis"
#   or "Structure of the human ribosome under different conditions."
#
#   Within each study, you'll find:
#
#   ### Biological Materials
#   - [Samples](Sample.md): The biological specimens being studied (proteins, nucleic acids, complexes,
#     cells, tissues). Each sample includes detailed molecular composition, buffer conditions, and
#     storage information. For example, a purified protein with its sequence, concentration, and buffer pH.
#
#   - [Sample Preparations](SamplePreparation.md): How samples were prepared for specific techniques.
#     This includes cryo-EM grid preparation (vitrification parameters), crystallization conditions for
#     X-ray studies, or staining protocols for fluorescence microscopy.
#
#   ### Data Collection
#   - [Instruments](Instrument.md): The equipment used, from Titan Krios microscopes to synchrotron
#     beamlines. Each instrument type ([CryoEMInstrument](CryoEMInstrument.md),
#     [XRayInstrument](XRayInstrument.md), [SAXSInstrument](SAXSInstrument.md)) has specific parameters
#     like accelerating voltage, detector type, or beam energy.
#
#   - [Experiment Runs](ExperimentRun.md): Individual data collection sessions that link samples to
#     instruments. An experiment run captures when, how, and under what conditions data was collected,
#     including quality metrics like resolution and completeness.
#
#   ### Data Processing
#   - [Workflow Runs](WorkflowRun.md): Computational processing steps applied to raw data. This includes
#     motion correction for cryo-EM movies, 3D reconstruction, model building, or phase determination
#     for crystallography. Each workflow tracks the software used, parameters, and computational resources.
#
#   ### Data Products
#   - [Data Files](DataFile.md): Any files generated or used, from raw data to final models. Each file
#     is tracked with checksums for data integrity and typed (micrograph, particles, volume, model).
#
#   - [Images](Image.md): Specialized classes for different imaging modalities:
#     - [Image2D](Image2D.md): Micrographs, diffraction patterns
#     - [Image3D](Image3D.md): 3D reconstructions, tomograms
#     - [FTIRImage](FTIRImage.md): Molecular composition maps from infrared spectroscopy
#     - [FluorescenceImage](FluorescenceImage.md): Fluorophore-labeled cellular components
#     - [OpticalImage](OpticalImage.md): Brightfield/phase contrast microscopy
#     - [XRFImage](XRFImage.md): Elemental distribution maps
#
#   ## Example Usage
#
#   A typical cryo-EM study of a protein complex would include:
#   1. Sample records for the purified complex with molecular weight and buffer composition
#   2. Grid preparation details with vitrification parameters
#   3. Microscope specifications and data collection parameters
#   4. Processing workflows from motion correction through 3D refinement
#   5. Final reconstructed volumes and fitted atomic models
#
#   A multimodal plant imaging study might combine:
#   1. Whole plant optical imaging for morphology
#   2. XRF imaging to map nutrient distribution
#   3. FTIR spectroscopy to identify stress-related molecular changes
#   4. Fluorescence microscopy to track specific protein responses
#   5. Cryo-EM of isolated organelles for ultrastructural details
#
#   ## Key Features
#
#   - **Technique-agnostic core**: The same schema handles data from any structural biology method
#   - **Rich metadata**: Comprehensive tracking from sample to structure
#   - **Workflow provenance**: Complete computational reproducibility
#   - **Multimodal support**: Seamlessly integrate data across scales and techniques
#   - **Standards-compliant**: Follows FAIR principles and integrates with existing ontologies
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
ROR = CurieNamespace('ROR', 'https://ror.org/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
IMGCIF = CurieNamespace('imgCIF', 'https://github.com/dials/cbflib/blob/main/doc/cif_img_1.8.6.dic#')
LAMBDABER = CurieNamespace('lambdaber', 'https://w3id.org/lambda-ber-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MMCIF = CurieNamespace('mmCIF', 'http://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
NSLS2 = CurieNamespace('nsls2', 'https://github.com/NSLS2/BER-LAMBDA/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WIKIDATA = CurieNamespace('wikidata', 'http://www.wikidata.org/entity/')
DEFAULT_ = LAMBDABER


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class DatasetId(NamedThingId):
    pass


class StudyId(NamedThingId):
    pass


class SampleId(NamedThingId):
    pass


class ProteinConstructId(NamedThingId):
    pass


class SamplePreparationId(NamedThingId):
    pass


class InstrumentId(NamedThingId):
    pass


class CryoEMInstrumentId(InstrumentId):
    pass


class XRayInstrumentId(InstrumentId):
    pass


class SAXSInstrumentId(InstrumentId):
    pass


class ExperimentRunId(NamedThingId):
    pass


class WorkflowRunId(NamedThingId):
    pass


class DataFileId(NamedThingId):
    pass


class ImageId(NamedThingId):
    pass


class Image2DId(ImageId):
    pass


class Image3DId(ImageId):
    pass


class FTIRImageId(ImageId):
    pass


class FluorescenceImageId(Image2DId):
    pass


class OpticalImageId(Image2DId):
    pass


class XRFImageId(Image2DId):
    pass


class OntologyTermId(NamedThingId):
    pass


class ProteinAnnotationId(NamedThingId):
    pass


class FunctionalSiteId(ProteinAnnotationId):
    pass


class StructuralFeatureId(ProteinAnnotationId):
    pass


class ProteinProteinInteractionId(ProteinAnnotationId):
    pass


class MutationEffectId(ProteinAnnotationId):
    pass


class ConformationalEnsembleId(NamedThingId):
    pass


class PostTranslationalModificationId(ProteinAnnotationId):
    pass


class EvolutionaryConservationId(ProteinAnnotationId):
    pass


class AggregatedProteinViewId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A named thing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["NamedThing"]
    class_class_curie: ClassVar[str] = "lambdaber:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.NamedThing

    id: Union[str, NamedThingId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttributeGroup(YAMLRoot):
    """
    A grouping of related data attributes that form a logical unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["AttributeGroup"]
    class_class_curie: ClassVar[str] = "lambdaber:AttributeGroup"
    class_name: ClassVar[str] = "AttributeGroup"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.AttributeGroup

    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(NamedThing):
    """
    A collection of studies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["Dataset"]
    class_class_curie: ClassVar[str] = "lambdaber:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.Dataset

    id: Union[str, DatasetId] = None
    keywords: Optional[Union[str, list[str]]] = empty_list()
    instruments: Optional[Union[dict[Union[str, InstrumentId], Union[dict, "Instrument"]], list[Union[dict, "Instrument"]]]] = empty_dict()
    studies: Optional[Union[dict[Union[str, StudyId], Union[dict, "Study"]], list[Union[dict, "Study"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        self._normalize_inlined_as_list(slot_name="instruments", slot_type=Instrument, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(NamedThing):
    """
    A focused research investigation that groups related samples, experiments, and data collection around a specific
    biological question or hypothesis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["Study"]
    class_class_curie: ClassVar[str] = "lambdaber:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.Study

    id: Union[str, StudyId] = None
    protein_constructs: Optional[Union[dict[Union[str, ProteinConstructId], Union[dict, "ProteinConstruct"]], list[Union[dict, "ProteinConstruct"]]]] = empty_dict()
    samples: Optional[Union[dict[Union[str, SampleId], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()
    sample_preparations: Optional[Union[dict[Union[str, SamplePreparationId], Union[dict, "SamplePreparation"]], list[Union[dict, "SamplePreparation"]]]] = empty_dict()
    instrument_runs: Optional[Union[dict[Union[str, ExperimentRunId], Union[dict, "ExperimentRun"]], list[Union[dict, "ExperimentRun"]]]] = empty_dict()
    workflow_runs: Optional[Union[dict[Union[str, WorkflowRunId], Union[dict, "WorkflowRun"]], list[Union[dict, "WorkflowRun"]]]] = empty_dict()
    data_files: Optional[Union[dict[Union[str, DataFileId], Union[dict, "DataFile"]], list[Union[dict, "DataFile"]]]] = empty_dict()
    images: Optional[Union[dict[Union[str, ImageId], Union[dict, "Image"]], list[Union[dict, "Image"]]]] = empty_dict()
    aggregated_protein_views: Optional[Union[dict[Union[str, AggregatedProteinViewId], Union[dict, "AggregatedProteinView"]], list[Union[dict, "AggregatedProteinView"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        self._normalize_inlined_as_list(slot_name="protein_constructs", slot_type=ProteinConstruct, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sample_preparations", slot_type=SamplePreparation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="instrument_runs", slot_type=ExperimentRun, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="workflow_runs", slot_type=WorkflowRun, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_files", slot_type=DataFile, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="images", slot_type=Image, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aggregated_protein_views", slot_type=AggregatedProteinView, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(NamedThing):
    """
    A biological sample used in structural biology experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["Sample"]
    class_class_curie: ClassVar[str] = "lambdaber:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.Sample

    id: Union[str, SampleId] = None
    sample_code: str = None
    sample_type: Union[str, "SampleTypeEnum"] = None
    molecular_composition: Optional[Union[dict, "MolecularComposition"]] = None
    molecular_weight: Optional[float] = None
    concentration: Optional[float] = None
    concentration_unit: Optional[Union[str, "ConcentrationUnitEnum"]] = None
    buffer_composition: Optional[Union[dict, "BufferComposition"]] = None
    preparation_method: Optional[str] = None
    storage_conditions: Optional[Union[dict, "StorageConditions"]] = None
    organism: Optional[Union[str, OntologyTermId]] = None
    anatomy: Optional[Union[str, OntologyTermId]] = None
    cell_type: Optional[Union[str, OntologyTermId]] = None
    parent_sample_id: Optional[Union[str, SampleId]] = None
    purity_percentage: Optional[float] = None
    quality_metrics: Optional[str] = None
    functional_sites: Optional[Union[dict[Union[str, FunctionalSiteId], Union[dict, "FunctionalSite"]], list[Union[dict, "FunctionalSite"]]]] = empty_dict()
    structural_features: Optional[Union[dict[Union[str, StructuralFeatureId], Union[dict, "StructuralFeature"]], list[Union[dict, "StructuralFeature"]]]] = empty_dict()
    protein_interactions: Optional[Union[dict[Union[str, ProteinProteinInteractionId], Union[dict, "ProteinProteinInteraction"]], list[Union[dict, "ProteinProteinInteraction"]]]] = empty_dict()
    ligand_interactions: Optional[Union[Union[dict, "LigandInteraction"], list[Union[dict, "LigandInteraction"]]]] = empty_list()
    mutation_effects: Optional[Union[dict[Union[str, MutationEffectId], Union[dict, "MutationEffect"]], list[Union[dict, "MutationEffect"]]]] = empty_dict()
    ptm_annotations: Optional[Union[dict[Union[str, PostTranslationalModificationId], Union[dict, "PostTranslationalModification"]], list[Union[dict, "PostTranslationalModification"]]]] = empty_dict()
    biophysical_properties: Optional[Union[Union[dict, "BiophysicalProperty"], list[Union[dict, "BiophysicalProperty"]]]] = empty_list()
    evolutionary_conservation: Optional[Union[dict, "EvolutionaryConservation"]] = None
    conformational_ensemble: Optional[Union[dict, "ConformationalEnsemble"]] = None
    database_cross_references: Optional[Union[Union[dict, "DatabaseCrossReference"], list[Union[dict, "DatabaseCrossReference"]]]] = empty_list()
    protein_name: Optional[str] = None
    construct: Optional[str] = None
    tag: Optional[str] = None
    mutations: Optional[str] = None
    expression_system: Optional[str] = None
    ligand: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self._is_empty(self.sample_code):
            self.MissingRequiredField("sample_code")
        if not isinstance(self.sample_code, str):
            self.sample_code = str(self.sample_code)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.molecular_composition is not None and not isinstance(self.molecular_composition, MolecularComposition):
            self.molecular_composition = MolecularComposition(**as_dict(self.molecular_composition))

        if self.molecular_weight is not None and not isinstance(self.molecular_weight, float):
            self.molecular_weight = float(self.molecular_weight)

        if self.concentration is not None and not isinstance(self.concentration, float):
            self.concentration = float(self.concentration)

        if self.concentration_unit is not None and not isinstance(self.concentration_unit, ConcentrationUnitEnum):
            self.concentration_unit = ConcentrationUnitEnum(self.concentration_unit)

        if self.buffer_composition is not None and not isinstance(self.buffer_composition, BufferComposition):
            self.buffer_composition = BufferComposition(**as_dict(self.buffer_composition))

        if self.preparation_method is not None and not isinstance(self.preparation_method, str):
            self.preparation_method = str(self.preparation_method)

        if self.storage_conditions is not None and not isinstance(self.storage_conditions, StorageConditions):
            self.storage_conditions = StorageConditions(**as_dict(self.storage_conditions))

        if self.organism is not None and not isinstance(self.organism, OntologyTermId):
            self.organism = OntologyTermId(self.organism)

        if self.anatomy is not None and not isinstance(self.anatomy, OntologyTermId):
            self.anatomy = OntologyTermId(self.anatomy)

        if self.cell_type is not None and not isinstance(self.cell_type, OntologyTermId):
            self.cell_type = OntologyTermId(self.cell_type)

        if self.parent_sample_id is not None and not isinstance(self.parent_sample_id, SampleId):
            self.parent_sample_id = SampleId(self.parent_sample_id)

        if self.purity_percentage is not None and not isinstance(self.purity_percentage, float):
            self.purity_percentage = float(self.purity_percentage)

        if self.quality_metrics is not None and not isinstance(self.quality_metrics, str):
            self.quality_metrics = str(self.quality_metrics)

        self._normalize_inlined_as_list(slot_name="functional_sites", slot_type=FunctionalSite, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="structural_features", slot_type=StructuralFeature, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="protein_interactions", slot_type=ProteinProteinInteraction, key_name="id", keyed=True)

        if not isinstance(self.ligand_interactions, list):
            self.ligand_interactions = [self.ligand_interactions] if self.ligand_interactions is not None else []
        self.ligand_interactions = [v if isinstance(v, LigandInteraction) else LigandInteraction(**as_dict(v)) for v in self.ligand_interactions]

        self._normalize_inlined_as_list(slot_name="mutation_effects", slot_type=MutationEffect, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ptm_annotations", slot_type=PostTranslationalModification, key_name="id", keyed=True)

        if not isinstance(self.biophysical_properties, list):
            self.biophysical_properties = [self.biophysical_properties] if self.biophysical_properties is not None else []
        self.biophysical_properties = [v if isinstance(v, BiophysicalProperty) else BiophysicalProperty(**as_dict(v)) for v in self.biophysical_properties]

        if self.evolutionary_conservation is not None and not isinstance(self.evolutionary_conservation, EvolutionaryConservation):
            self.evolutionary_conservation = EvolutionaryConservation(**as_dict(self.evolutionary_conservation))

        if self.conformational_ensemble is not None and not isinstance(self.conformational_ensemble, ConformationalEnsemble):
            self.conformational_ensemble = ConformationalEnsemble(**as_dict(self.conformational_ensemble))

        if not isinstance(self.database_cross_references, list):
            self.database_cross_references = [self.database_cross_references] if self.database_cross_references is not None else []
        self.database_cross_references = [v if isinstance(v, DatabaseCrossReference) else DatabaseCrossReference(**as_dict(v)) for v in self.database_cross_references]

        if self.protein_name is not None and not isinstance(self.protein_name, str):
            self.protein_name = str(self.protein_name)

        if self.construct is not None and not isinstance(self.construct, str):
            self.construct = str(self.construct)

        if self.tag is not None and not isinstance(self.tag, str):
            self.tag = str(self.tag)

        if self.mutations is not None and not isinstance(self.mutations, str):
            self.mutations = str(self.mutations)

        if self.expression_system is not None and not isinstance(self.expression_system, str):
            self.expression_system = str(self.expression_system)

        if self.ligand is not None and not isinstance(self.ligand, str):
            self.ligand = str(self.ligand)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinConstruct(NamedThing):
    """
    Detailed information about a protein construct including cloning and sequence design
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["ProteinConstruct"]
    class_class_curie: ClassVar[str] = "lambdaber:ProteinConstruct"
    class_name: ClassVar[str] = "ProteinConstruct"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ProteinConstruct

    id: Union[str, ProteinConstructId] = None
    construct_id: str = None
    uniprot_id: Optional[str] = None
    gene_name: Optional[str] = None
    ncbi_taxid: Optional[str] = None
    sequence_length_aa: Optional[int] = None
    construct_description: Optional[str] = None
    gene_synthesis_provider: Optional[str] = None
    codon_optimization_organism: Optional[str] = None
    vector_backbone: Optional[str] = None
    vector_name: Optional[str] = None
    promoter: Optional[str] = None
    tag_nterm: Optional[str] = None
    tag_cterm: Optional[str] = None
    cleavage_site: Optional[str] = None
    signal_peptide: Optional[str] = None
    selectable_marker: Optional[str] = None
    cloning_method: Optional[str] = None
    insert_boundaries: Optional[str] = None
    sequence_file_path: Optional[str] = None
    sequence_verified_by: Optional[str] = None
    verification_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinConstructId):
            self.id = ProteinConstructId(self.id)

        if self._is_empty(self.construct_id):
            self.MissingRequiredField("construct_id")
        if not isinstance(self.construct_id, str):
            self.construct_id = str(self.construct_id)

        if self.uniprot_id is not None and not isinstance(self.uniprot_id, str):
            self.uniprot_id = str(self.uniprot_id)

        if self.gene_name is not None and not isinstance(self.gene_name, str):
            self.gene_name = str(self.gene_name)

        if self.ncbi_taxid is not None and not isinstance(self.ncbi_taxid, str):
            self.ncbi_taxid = str(self.ncbi_taxid)

        if self.sequence_length_aa is not None and not isinstance(self.sequence_length_aa, int):
            self.sequence_length_aa = int(self.sequence_length_aa)

        if self.construct_description is not None and not isinstance(self.construct_description, str):
            self.construct_description = str(self.construct_description)

        if self.gene_synthesis_provider is not None and not isinstance(self.gene_synthesis_provider, str):
            self.gene_synthesis_provider = str(self.gene_synthesis_provider)

        if self.codon_optimization_organism is not None and not isinstance(self.codon_optimization_organism, str):
            self.codon_optimization_organism = str(self.codon_optimization_organism)

        if self.vector_backbone is not None and not isinstance(self.vector_backbone, str):
            self.vector_backbone = str(self.vector_backbone)

        if self.vector_name is not None and not isinstance(self.vector_name, str):
            self.vector_name = str(self.vector_name)

        if self.promoter is not None and not isinstance(self.promoter, str):
            self.promoter = str(self.promoter)

        if self.tag_nterm is not None and not isinstance(self.tag_nterm, str):
            self.tag_nterm = str(self.tag_nterm)

        if self.tag_cterm is not None and not isinstance(self.tag_cterm, str):
            self.tag_cterm = str(self.tag_cterm)

        if self.cleavage_site is not None and not isinstance(self.cleavage_site, str):
            self.cleavage_site = str(self.cleavage_site)

        if self.signal_peptide is not None and not isinstance(self.signal_peptide, str):
            self.signal_peptide = str(self.signal_peptide)

        if self.selectable_marker is not None and not isinstance(self.selectable_marker, str):
            self.selectable_marker = str(self.selectable_marker)

        if self.cloning_method is not None and not isinstance(self.cloning_method, str):
            self.cloning_method = str(self.cloning_method)

        if self.insert_boundaries is not None and not isinstance(self.insert_boundaries, str):
            self.insert_boundaries = str(self.insert_boundaries)

        if self.sequence_file_path is not None and not isinstance(self.sequence_file_path, str):
            self.sequence_file_path = str(self.sequence_file_path)

        if self.sequence_verified_by is not None and not isinstance(self.sequence_verified_by, str):
            self.sequence_verified_by = str(self.sequence_verified_by)

        if self.verification_notes is not None and not isinstance(self.verification_notes, str):
            self.verification_notes = str(self.verification_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplePreparation(NamedThing):
    """
    A process that prepares a sample for imaging
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["SamplePreparation"]
    class_class_curie: ClassVar[str] = "lambdaber:SamplePreparation"
    class_name: ClassVar[str] = "SamplePreparation"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.SamplePreparation

    id: Union[str, SamplePreparationId] = None
    preparation_type: Union[str, "PreparationTypeEnum"] = None
    sample_id: str = None
    preparation_date: Optional[str] = None
    operator_id: Optional[str] = None
    protocol_description: Optional[str] = None
    expression_system: Optional[Union[str, "ExpressionSystemEnum"]] = None
    host_strain_or_cell_line: Optional[str] = None
    culture_volume_l: Optional[float] = None
    medium: Optional[str] = None
    antibiotic_selection: Optional[str] = None
    growth_temperature_c: Optional[float] = None
    induction_agent: Optional[str] = None
    inducer_concentration: Optional[str] = None
    induction_temperature_c: Optional[float] = None
    induction_time_h: Optional[float] = None
    od600_at_induction: Optional[float] = None
    harvest_timepoint: Optional[str] = None
    lysis_method: Optional[str] = None
    protease_inhibitors: Optional[str] = None
    purification_steps: Optional[Union[Union[str, "PurificationStepEnum"], list[Union[str, "PurificationStepEnum"]]]] = empty_list()
    affinity_type: Optional[str] = None
    affinity_column: Optional[str] = None
    lysis_buffer: Optional[str] = None
    wash_buffer: Optional[str] = None
    elution_buffer: Optional[str] = None
    tag_removal: Optional[Union[bool, Bool]] = None
    protease: Optional[str] = None
    protease_ratio: Optional[str] = None
    cleavage_time_h: Optional[float] = None
    cleavage_temperature_c: Optional[float] = None
    second_affinity_reverse: Optional[str] = None
    iex_column: Optional[str] = None
    hic_column: Optional[str] = None
    sec_column: Optional[str] = None
    sec_buffer: Optional[str] = None
    concentration_method: Optional[str] = None
    final_buffer: Optional[str] = None
    final_concentration_mg_per_ml: Optional[float] = None
    yield_mg: Optional[float] = None
    purity_by_sds_page_percent: Optional[float] = None
    aggregation_assessment: Optional[str] = None
    aliquoting: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplePreparationId):
            self.id = SamplePreparationId(self.id)

        if self._is_empty(self.preparation_type):
            self.MissingRequiredField("preparation_type")
        if not isinstance(self.preparation_type, PreparationTypeEnum):
            self.preparation_type = PreparationTypeEnum(self.preparation_type)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self.preparation_date is not None and not isinstance(self.preparation_date, str):
            self.preparation_date = str(self.preparation_date)

        if self.operator_id is not None and not isinstance(self.operator_id, str):
            self.operator_id = str(self.operator_id)

        if self.protocol_description is not None and not isinstance(self.protocol_description, str):
            self.protocol_description = str(self.protocol_description)

        if self.expression_system is not None and not isinstance(self.expression_system, ExpressionSystemEnum):
            self.expression_system = ExpressionSystemEnum(self.expression_system)

        if self.host_strain_or_cell_line is not None and not isinstance(self.host_strain_or_cell_line, str):
            self.host_strain_or_cell_line = str(self.host_strain_or_cell_line)

        if self.culture_volume_l is not None and not isinstance(self.culture_volume_l, float):
            self.culture_volume_l = float(self.culture_volume_l)

        if self.medium is not None and not isinstance(self.medium, str):
            self.medium = str(self.medium)

        if self.antibiotic_selection is not None and not isinstance(self.antibiotic_selection, str):
            self.antibiotic_selection = str(self.antibiotic_selection)

        if self.growth_temperature_c is not None and not isinstance(self.growth_temperature_c, float):
            self.growth_temperature_c = float(self.growth_temperature_c)

        if self.induction_agent is not None and not isinstance(self.induction_agent, str):
            self.induction_agent = str(self.induction_agent)

        if self.inducer_concentration is not None and not isinstance(self.inducer_concentration, str):
            self.inducer_concentration = str(self.inducer_concentration)

        if self.induction_temperature_c is not None and not isinstance(self.induction_temperature_c, float):
            self.induction_temperature_c = float(self.induction_temperature_c)

        if self.induction_time_h is not None and not isinstance(self.induction_time_h, float):
            self.induction_time_h = float(self.induction_time_h)

        if self.od600_at_induction is not None and not isinstance(self.od600_at_induction, float):
            self.od600_at_induction = float(self.od600_at_induction)

        if self.harvest_timepoint is not None and not isinstance(self.harvest_timepoint, str):
            self.harvest_timepoint = str(self.harvest_timepoint)

        if self.lysis_method is not None and not isinstance(self.lysis_method, str):
            self.lysis_method = str(self.lysis_method)

        if self.protease_inhibitors is not None and not isinstance(self.protease_inhibitors, str):
            self.protease_inhibitors = str(self.protease_inhibitors)

        if not isinstance(self.purification_steps, list):
            self.purification_steps = [self.purification_steps] if self.purification_steps is not None else []
        self.purification_steps = [v if isinstance(v, PurificationStepEnum) else PurificationStepEnum(v) for v in self.purification_steps]

        if self.affinity_type is not None and not isinstance(self.affinity_type, str):
            self.affinity_type = str(self.affinity_type)

        if self.affinity_column is not None and not isinstance(self.affinity_column, str):
            self.affinity_column = str(self.affinity_column)

        if self.lysis_buffer is not None and not isinstance(self.lysis_buffer, str):
            self.lysis_buffer = str(self.lysis_buffer)

        if self.wash_buffer is not None and not isinstance(self.wash_buffer, str):
            self.wash_buffer = str(self.wash_buffer)

        if self.elution_buffer is not None and not isinstance(self.elution_buffer, str):
            self.elution_buffer = str(self.elution_buffer)

        if self.tag_removal is not None and not isinstance(self.tag_removal, Bool):
            self.tag_removal = Bool(self.tag_removal)

        if self.protease is not None and not isinstance(self.protease, str):
            self.protease = str(self.protease)

        if self.protease_ratio is not None and not isinstance(self.protease_ratio, str):
            self.protease_ratio = str(self.protease_ratio)

        if self.cleavage_time_h is not None and not isinstance(self.cleavage_time_h, float):
            self.cleavage_time_h = float(self.cleavage_time_h)

        if self.cleavage_temperature_c is not None and not isinstance(self.cleavage_temperature_c, float):
            self.cleavage_temperature_c = float(self.cleavage_temperature_c)

        if self.second_affinity_reverse is not None and not isinstance(self.second_affinity_reverse, str):
            self.second_affinity_reverse = str(self.second_affinity_reverse)

        if self.iex_column is not None and not isinstance(self.iex_column, str):
            self.iex_column = str(self.iex_column)

        if self.hic_column is not None and not isinstance(self.hic_column, str):
            self.hic_column = str(self.hic_column)

        if self.sec_column is not None and not isinstance(self.sec_column, str):
            self.sec_column = str(self.sec_column)

        if self.sec_buffer is not None and not isinstance(self.sec_buffer, str):
            self.sec_buffer = str(self.sec_buffer)

        if self.concentration_method is not None and not isinstance(self.concentration_method, str):
            self.concentration_method = str(self.concentration_method)

        if self.final_buffer is not None and not isinstance(self.final_buffer, str):
            self.final_buffer = str(self.final_buffer)

        if self.final_concentration_mg_per_ml is not None and not isinstance(self.final_concentration_mg_per_ml, float):
            self.final_concentration_mg_per_ml = float(self.final_concentration_mg_per_ml)

        if self.yield_mg is not None and not isinstance(self.yield_mg, float):
            self.yield_mg = float(self.yield_mg)

        if self.purity_by_sds_page_percent is not None and not isinstance(self.purity_by_sds_page_percent, float):
            self.purity_by_sds_page_percent = float(self.purity_by_sds_page_percent)

        if self.aggregation_assessment is not None and not isinstance(self.aggregation_assessment, str):
            self.aggregation_assessment = str(self.aggregation_assessment)

        if self.aliquoting is not None and not isinstance(self.aliquoting, str):
            self.aliquoting = str(self.aliquoting)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Instrument(NamedThing):
    """
    An instrument used to collect data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["Instrument"]
    class_class_curie: ClassVar[str] = "lambdaber:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.Instrument

    id: Union[str, InstrumentId] = None
    instrument_code: str = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    installation_date: Optional[str] = None
    current_status: Optional[Union[str, "InstrumentStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstrumentId):
            self.id = InstrumentId(self.id)

        if self._is_empty(self.instrument_code):
            self.MissingRequiredField("instrument_code")
        if not isinstance(self.instrument_code, str):
            self.instrument_code = str(self.instrument_code)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.installation_date is not None and not isinstance(self.installation_date, str):
            self.installation_date = str(self.installation_date)

        if self.current_status is not None and not isinstance(self.current_status, InstrumentStatusEnum):
            self.current_status = InstrumentStatusEnum(self.current_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CryoEMInstrument(Instrument):
    """
    Cryo-EM microscope specifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["CryoEMInstrument"]
    class_class_curie: ClassVar[str] = "lambdaber:CryoEMInstrument"
    class_name: ClassVar[str] = "CryoEMInstrument"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.CryoEMInstrument

    id: Union[str, CryoEMInstrumentId] = None
    instrument_code: str = None
    accelerating_voltage: Optional[int] = None
    cs_corrector: Optional[Union[bool, Bool]] = None
    phase_plate: Optional[Union[bool, Bool]] = None
    detector_technology: Optional[Union[str, "DetectorTechnologyEnum"]] = None
    detector_manufacturer: Optional[str] = None
    detector_model: Optional[str] = None
    detector_mode: Optional[Union[str, "DetectorModeEnum"]] = None
    detector_position: Optional[str] = None
    detector_dimensions: Optional[str] = None
    pixel_size_physical_um: Optional[float] = None
    autoloader_capacity: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CryoEMInstrumentId):
            self.id = CryoEMInstrumentId(self.id)

        if self.accelerating_voltage is not None and not isinstance(self.accelerating_voltage, int):
            self.accelerating_voltage = int(self.accelerating_voltage)

        if self.cs_corrector is not None and not isinstance(self.cs_corrector, Bool):
            self.cs_corrector = Bool(self.cs_corrector)

        if self.phase_plate is not None and not isinstance(self.phase_plate, Bool):
            self.phase_plate = Bool(self.phase_plate)

        if self.detector_technology is not None and not isinstance(self.detector_technology, DetectorTechnologyEnum):
            self.detector_technology = DetectorTechnologyEnum(self.detector_technology)

        if self.detector_manufacturer is not None and not isinstance(self.detector_manufacturer, str):
            self.detector_manufacturer = str(self.detector_manufacturer)

        if self.detector_model is not None and not isinstance(self.detector_model, str):
            self.detector_model = str(self.detector_model)

        if self.detector_mode is not None and not isinstance(self.detector_mode, DetectorModeEnum):
            self.detector_mode = DetectorModeEnum(self.detector_mode)

        if self.detector_position is not None and not isinstance(self.detector_position, str):
            self.detector_position = str(self.detector_position)

        if self.detector_dimensions is not None and not isinstance(self.detector_dimensions, str):
            self.detector_dimensions = str(self.detector_dimensions)

        if self.pixel_size_physical_um is not None and not isinstance(self.pixel_size_physical_um, float):
            self.pixel_size_physical_um = float(self.pixel_size_physical_um)

        if self.autoloader_capacity is not None and not isinstance(self.autoloader_capacity, int):
            self.autoloader_capacity = int(self.autoloader_capacity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRayInstrument(Instrument):
    """
    X-ray diffractometer or synchrotron beamline specifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["XRayInstrument"]
    class_class_curie: ClassVar[str] = "lambdaber:XRayInstrument"
    class_name: ClassVar[str] = "XRayInstrument"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.XRayInstrument

    id: Union[str, XRayInstrumentId] = None
    instrument_code: str = None
    source_type: Optional[Union[str, "XRaySourceTypeEnum"]] = None
    detector_technology: Optional[Union[str, "DetectorTechnologyEnum"]] = None
    detector_manufacturer: Optional[str] = None
    detector_model: Optional[str] = None
    beamline_id: Optional[str] = None
    energy_min: Optional[float] = None
    energy_max: Optional[float] = None
    beam_size_min: Optional[float] = None
    beam_size_max: Optional[float] = None
    flux_density: Optional[float] = None
    monochromator_type: Optional[str] = None
    goniometer_type: Optional[str] = None
    crystal_cooling_capability: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRayInstrumentId):
            self.id = XRayInstrumentId(self.id)

        if self.source_type is not None and not isinstance(self.source_type, XRaySourceTypeEnum):
            self.source_type = XRaySourceTypeEnum(self.source_type)

        if self.detector_technology is not None and not isinstance(self.detector_technology, DetectorTechnologyEnum):
            self.detector_technology = DetectorTechnologyEnum(self.detector_technology)

        if self.detector_manufacturer is not None and not isinstance(self.detector_manufacturer, str):
            self.detector_manufacturer = str(self.detector_manufacturer)

        if self.detector_model is not None and not isinstance(self.detector_model, str):
            self.detector_model = str(self.detector_model)

        if self.beamline_id is not None and not isinstance(self.beamline_id, str):
            self.beamline_id = str(self.beamline_id)

        if self.energy_min is not None and not isinstance(self.energy_min, float):
            self.energy_min = float(self.energy_min)

        if self.energy_max is not None and not isinstance(self.energy_max, float):
            self.energy_max = float(self.energy_max)

        if self.beam_size_min is not None and not isinstance(self.beam_size_min, float):
            self.beam_size_min = float(self.beam_size_min)

        if self.beam_size_max is not None and not isinstance(self.beam_size_max, float):
            self.beam_size_max = float(self.beam_size_max)

        if self.flux_density is not None and not isinstance(self.flux_density, float):
            self.flux_density = float(self.flux_density)

        if self.monochromator_type is not None and not isinstance(self.monochromator_type, str):
            self.monochromator_type = str(self.monochromator_type)

        if self.goniometer_type is not None and not isinstance(self.goniometer_type, str):
            self.goniometer_type = str(self.goniometer_type)

        if self.crystal_cooling_capability is not None and not isinstance(self.crystal_cooling_capability, Bool):
            self.crystal_cooling_capability = Bool(self.crystal_cooling_capability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SAXSInstrument(Instrument):
    """
    SAXS/WAXS instrument specifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["SAXSInstrument"]
    class_class_curie: ClassVar[str] = "lambdaber:SAXSInstrument"
    class_name: ClassVar[str] = "SAXSInstrument"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.SAXSInstrument

    id: Union[str, SAXSInstrumentId] = None
    instrument_code: str = None
    q_range_min: Optional[float] = None
    q_range_max: Optional[float] = None
    detector_distance_min: Optional[float] = None
    detector_distance_max: Optional[float] = None
    sample_changer_capacity: Optional[int] = None
    temperature_control_range: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SAXSInstrumentId):
            self.id = SAXSInstrumentId(self.id)

        if self.q_range_min is not None and not isinstance(self.q_range_min, float):
            self.q_range_min = float(self.q_range_min)

        if self.q_range_max is not None and not isinstance(self.q_range_max, float):
            self.q_range_max = float(self.q_range_max)

        if self.detector_distance_min is not None and not isinstance(self.detector_distance_min, float):
            self.detector_distance_min = float(self.detector_distance_min)

        if self.detector_distance_max is not None and not isinstance(self.detector_distance_max, float):
            self.detector_distance_max = float(self.detector_distance_max)

        if self.sample_changer_capacity is not None and not isinstance(self.sample_changer_capacity, int):
            self.sample_changer_capacity = int(self.sample_changer_capacity)

        if self.temperature_control_range is not None and not isinstance(self.temperature_control_range, str):
            self.temperature_control_range = str(self.temperature_control_range)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentRun(NamedThing):
    """
    An experimental data collection session
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["ExperimentRun"]
    class_class_curie: ClassVar[str] = "lambdaber:ExperimentRun"
    class_name: ClassVar[str] = "ExperimentRun"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ExperimentRun

    id: Union[str, ExperimentRunId] = None
    experiment_code: str = None
    sample_id: str = None
    instrument_id: Union[str, InstrumentId] = None
    technique: Union[str, "TechniqueEnum"] = None
    experiment_date: Optional[str] = None
    operator_id: Optional[str] = None
    experimental_method: Optional[Union[str, "ExperimentalMethodEnum"]] = None
    experimental_conditions: Optional[Union[dict, "ExperimentalConditions"]] = None
    data_collection_strategy: Optional[Union[dict, "DataCollectionStrategy"]] = None
    quality_metrics: Optional[Union[dict, "QualityMetrics"]] = None
    raw_data_location: Optional[str] = None
    processing_status: Optional[Union[str, "ProcessingStatusEnum"]] = None
    wavelength: Optional[float] = None
    oscillation_angle: Optional[float] = None
    start_angle: Optional[float] = None
    number_of_images: Optional[int] = None
    beam_center_x: Optional[float] = None
    beam_center_y: Optional[float] = None
    detector_distance: Optional[float] = None
    pixel_size_x: Optional[float] = None
    pixel_size_y: Optional[float] = None
    total_rotation: Optional[float] = None
    beamline: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentRunId):
            self.id = ExperimentRunId(self.id)

        if self._is_empty(self.experiment_code):
            self.MissingRequiredField("experiment_code")
        if not isinstance(self.experiment_code, str):
            self.experiment_code = str(self.experiment_code)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self._is_empty(self.instrument_id):
            self.MissingRequiredField("instrument_id")
        if not isinstance(self.instrument_id, InstrumentId):
            self.instrument_id = InstrumentId(self.instrument_id)

        if self._is_empty(self.technique):
            self.MissingRequiredField("technique")
        if not isinstance(self.technique, TechniqueEnum):
            self.technique = TechniqueEnum(self.technique)

        if self.experiment_date is not None and not isinstance(self.experiment_date, str):
            self.experiment_date = str(self.experiment_date)

        if self.operator_id is not None and not isinstance(self.operator_id, str):
            self.operator_id = str(self.operator_id)

        if self.experimental_method is not None and not isinstance(self.experimental_method, ExperimentalMethodEnum):
            self.experimental_method = ExperimentalMethodEnum(self.experimental_method)

        if self.experimental_conditions is not None and not isinstance(self.experimental_conditions, ExperimentalConditions):
            self.experimental_conditions = ExperimentalConditions(**as_dict(self.experimental_conditions))

        if self.data_collection_strategy is not None and not isinstance(self.data_collection_strategy, DataCollectionStrategy):
            self.data_collection_strategy = DataCollectionStrategy(**as_dict(self.data_collection_strategy))

        if self.quality_metrics is not None and not isinstance(self.quality_metrics, QualityMetrics):
            self.quality_metrics = QualityMetrics(**as_dict(self.quality_metrics))

        if self.raw_data_location is not None and not isinstance(self.raw_data_location, str):
            self.raw_data_location = str(self.raw_data_location)

        if self.processing_status is not None and not isinstance(self.processing_status, ProcessingStatusEnum):
            self.processing_status = ProcessingStatusEnum(self.processing_status)

        if self.wavelength is not None and not isinstance(self.wavelength, float):
            self.wavelength = float(self.wavelength)

        if self.oscillation_angle is not None and not isinstance(self.oscillation_angle, float):
            self.oscillation_angle = float(self.oscillation_angle)

        if self.start_angle is not None and not isinstance(self.start_angle, float):
            self.start_angle = float(self.start_angle)

        if self.number_of_images is not None and not isinstance(self.number_of_images, int):
            self.number_of_images = int(self.number_of_images)

        if self.beam_center_x is not None and not isinstance(self.beam_center_x, float):
            self.beam_center_x = float(self.beam_center_x)

        if self.beam_center_y is not None and not isinstance(self.beam_center_y, float):
            self.beam_center_y = float(self.beam_center_y)

        if self.detector_distance is not None and not isinstance(self.detector_distance, float):
            self.detector_distance = float(self.detector_distance)

        if self.pixel_size_x is not None and not isinstance(self.pixel_size_x, float):
            self.pixel_size_x = float(self.pixel_size_x)

        if self.pixel_size_y is not None and not isinstance(self.pixel_size_y, float):
            self.pixel_size_y = float(self.pixel_size_y)

        if self.total_rotation is not None and not isinstance(self.total_rotation, float):
            self.total_rotation = float(self.total_rotation)

        if self.beamline is not None and not isinstance(self.beamline, str):
            self.beamline = str(self.beamline)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkflowRun(NamedThing):
    """
    A computational processing workflow execution
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["WorkflowRun"]
    class_class_curie: ClassVar[str] = "lambdaber:WorkflowRun"
    class_name: ClassVar[str] = "WorkflowRun"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.WorkflowRun

    id: Union[str, WorkflowRunId] = None
    workflow_code: str = None
    workflow_type: Union[str, "WorkflowTypeEnum"] = None
    experiment_id: str = None
    software_name: str = None
    processing_level: Optional[int] = None
    software_version: Optional[str] = None
    additional_software: Optional[str] = None
    processing_parameters: Optional[str] = None
    parameters_file_path: Optional[str] = None
    indexer_module: Optional[str] = None
    integrator_module: Optional[str] = None
    scaler_module: Optional[str] = None
    outlier_rejection_method: Optional[str] = None
    phasing_method: Optional[Union[str, "PhasingMethodEnum"]] = None
    search_model_pdb_id: Optional[str] = None
    tls_used: Optional[Union[bool, Bool]] = None
    ncs_used: Optional[Union[bool, Bool]] = None
    restraints_other: Optional[str] = None
    ligands_cofactors: Optional[str] = None
    number_of_waters: Optional[int] = None
    refinement_resolution_a: Optional[float] = None
    deposited_to_pdb: Optional[Union[bool, Bool]] = None
    pdb_id: Optional[str] = None
    validation_report_path: Optional[str] = None
    space_group: Optional[str] = None
    unit_cell_a: Optional[float] = None
    unit_cell_b: Optional[float] = None
    unit_cell_c: Optional[float] = None
    unit_cell_alpha: Optional[float] = None
    unit_cell_beta: Optional[float] = None
    unit_cell_gamma: Optional[float] = None
    resolution_high: Optional[float] = None
    resolution_low: Optional[float] = None
    rmerge: Optional[float] = None
    rpim: Optional[float] = None
    cc_half: Optional[float] = None
    completeness_percent: Optional[float] = None
    i_over_sigma: Optional[float] = None
    wilson_b_factor: Optional[float] = None
    multiplicity: Optional[float] = None
    rwork: Optional[float] = None
    rfree: Optional[float] = None
    rmsd_bonds: Optional[float] = None
    rmsd_angles: Optional[float] = None
    ramachandran_favored: Optional[float] = None
    ramachandran_outliers: Optional[float] = None
    clashscore: Optional[float] = None
    processing_notes: Optional[str] = None
    compute_resources: Optional[Union[dict, "ComputeResources"]] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    output_files: Optional[Union[Union[str, DataFileId], list[Union[str, DataFileId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowRunId):
            self.id = WorkflowRunId(self.id)

        if self._is_empty(self.workflow_code):
            self.MissingRequiredField("workflow_code")
        if not isinstance(self.workflow_code, str):
            self.workflow_code = str(self.workflow_code)

        if self._is_empty(self.workflow_type):
            self.MissingRequiredField("workflow_type")
        if not isinstance(self.workflow_type, WorkflowTypeEnum):
            self.workflow_type = WorkflowTypeEnum(self.workflow_type)

        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self._is_empty(self.software_name):
            self.MissingRequiredField("software_name")
        if not isinstance(self.software_name, str):
            self.software_name = str(self.software_name)

        if self.processing_level is not None and not isinstance(self.processing_level, int):
            self.processing_level = int(self.processing_level)

        if self.software_version is not None and not isinstance(self.software_version, str):
            self.software_version = str(self.software_version)

        if self.additional_software is not None and not isinstance(self.additional_software, str):
            self.additional_software = str(self.additional_software)

        if self.processing_parameters is not None and not isinstance(self.processing_parameters, str):
            self.processing_parameters = str(self.processing_parameters)

        if self.parameters_file_path is not None and not isinstance(self.parameters_file_path, str):
            self.parameters_file_path = str(self.parameters_file_path)

        if self.indexer_module is not None and not isinstance(self.indexer_module, str):
            self.indexer_module = str(self.indexer_module)

        if self.integrator_module is not None and not isinstance(self.integrator_module, str):
            self.integrator_module = str(self.integrator_module)

        if self.scaler_module is not None and not isinstance(self.scaler_module, str):
            self.scaler_module = str(self.scaler_module)

        if self.outlier_rejection_method is not None and not isinstance(self.outlier_rejection_method, str):
            self.outlier_rejection_method = str(self.outlier_rejection_method)

        if self.phasing_method is not None and not isinstance(self.phasing_method, PhasingMethodEnum):
            self.phasing_method = PhasingMethodEnum(self.phasing_method)

        if self.search_model_pdb_id is not None and not isinstance(self.search_model_pdb_id, str):
            self.search_model_pdb_id = str(self.search_model_pdb_id)

        if self.tls_used is not None and not isinstance(self.tls_used, Bool):
            self.tls_used = Bool(self.tls_used)

        if self.ncs_used is not None and not isinstance(self.ncs_used, Bool):
            self.ncs_used = Bool(self.ncs_used)

        if self.restraints_other is not None and not isinstance(self.restraints_other, str):
            self.restraints_other = str(self.restraints_other)

        if self.ligands_cofactors is not None and not isinstance(self.ligands_cofactors, str):
            self.ligands_cofactors = str(self.ligands_cofactors)

        if self.number_of_waters is not None and not isinstance(self.number_of_waters, int):
            self.number_of_waters = int(self.number_of_waters)

        if self.refinement_resolution_a is not None and not isinstance(self.refinement_resolution_a, float):
            self.refinement_resolution_a = float(self.refinement_resolution_a)

        if self.deposited_to_pdb is not None and not isinstance(self.deposited_to_pdb, Bool):
            self.deposited_to_pdb = Bool(self.deposited_to_pdb)

        if self.pdb_id is not None and not isinstance(self.pdb_id, str):
            self.pdb_id = str(self.pdb_id)

        if self.validation_report_path is not None and not isinstance(self.validation_report_path, str):
            self.validation_report_path = str(self.validation_report_path)

        if self.space_group is not None and not isinstance(self.space_group, str):
            self.space_group = str(self.space_group)

        if self.unit_cell_a is not None and not isinstance(self.unit_cell_a, float):
            self.unit_cell_a = float(self.unit_cell_a)

        if self.unit_cell_b is not None and not isinstance(self.unit_cell_b, float):
            self.unit_cell_b = float(self.unit_cell_b)

        if self.unit_cell_c is not None and not isinstance(self.unit_cell_c, float):
            self.unit_cell_c = float(self.unit_cell_c)

        if self.unit_cell_alpha is not None and not isinstance(self.unit_cell_alpha, float):
            self.unit_cell_alpha = float(self.unit_cell_alpha)

        if self.unit_cell_beta is not None and not isinstance(self.unit_cell_beta, float):
            self.unit_cell_beta = float(self.unit_cell_beta)

        if self.unit_cell_gamma is not None and not isinstance(self.unit_cell_gamma, float):
            self.unit_cell_gamma = float(self.unit_cell_gamma)

        if self.resolution_high is not None and not isinstance(self.resolution_high, float):
            self.resolution_high = float(self.resolution_high)

        if self.resolution_low is not None and not isinstance(self.resolution_low, float):
            self.resolution_low = float(self.resolution_low)

        if self.rmerge is not None and not isinstance(self.rmerge, float):
            self.rmerge = float(self.rmerge)

        if self.rpim is not None and not isinstance(self.rpim, float):
            self.rpim = float(self.rpim)

        if self.cc_half is not None and not isinstance(self.cc_half, float):
            self.cc_half = float(self.cc_half)

        if self.completeness_percent is not None and not isinstance(self.completeness_percent, float):
            self.completeness_percent = float(self.completeness_percent)

        if self.i_over_sigma is not None and not isinstance(self.i_over_sigma, float):
            self.i_over_sigma = float(self.i_over_sigma)

        if self.wilson_b_factor is not None and not isinstance(self.wilson_b_factor, float):
            self.wilson_b_factor = float(self.wilson_b_factor)

        if self.multiplicity is not None and not isinstance(self.multiplicity, float):
            self.multiplicity = float(self.multiplicity)

        if self.rwork is not None and not isinstance(self.rwork, float):
            self.rwork = float(self.rwork)

        if self.rfree is not None and not isinstance(self.rfree, float):
            self.rfree = float(self.rfree)

        if self.rmsd_bonds is not None and not isinstance(self.rmsd_bonds, float):
            self.rmsd_bonds = float(self.rmsd_bonds)

        if self.rmsd_angles is not None and not isinstance(self.rmsd_angles, float):
            self.rmsd_angles = float(self.rmsd_angles)

        if self.ramachandran_favored is not None and not isinstance(self.ramachandran_favored, float):
            self.ramachandran_favored = float(self.ramachandran_favored)

        if self.ramachandran_outliers is not None and not isinstance(self.ramachandran_outliers, float):
            self.ramachandran_outliers = float(self.ramachandran_outliers)

        if self.clashscore is not None and not isinstance(self.clashscore, float):
            self.clashscore = float(self.clashscore)

        if self.processing_notes is not None and not isinstance(self.processing_notes, str):
            self.processing_notes = str(self.processing_notes)

        if self.compute_resources is not None and not isinstance(self.compute_resources, ComputeResources):
            self.compute_resources = ComputeResources(**as_dict(self.compute_resources))

        if self.started_at is not None and not isinstance(self.started_at, str):
            self.started_at = str(self.started_at)

        if self.completed_at is not None and not isinstance(self.completed_at, str):
            self.completed_at = str(self.completed_at)

        if not isinstance(self.output_files, list):
            self.output_files = [self.output_files] if self.output_files is not None else []
        self.output_files = [v if isinstance(v, DataFileId) else DataFileId(v) for v in self.output_files]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataFile(NamedThing):
    """
    A data file generated or used in the study
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["DataFile"]
    class_class_curie: ClassVar[str] = "lambdaber:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.DataFile

    id: Union[str, DataFileId] = None
    file_name: str = None
    file_format: Union[str, "FileFormatEnum"] = None
    file_path: Optional[str] = None
    file_size_bytes: Optional[int] = None
    checksum: Optional[str] = None
    creation_date: Optional[str] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataFileId):
            self.id = DataFileId(self.id)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.file_format):
            self.MissingRequiredField("file_format")
        if not isinstance(self.file_format, FileFormatEnum):
            self.file_format = FileFormatEnum(self.file_format)

        if self.file_path is not None and not isinstance(self.file_path, str):
            self.file_path = str(self.file_path)

        if self.file_size_bytes is not None and not isinstance(self.file_size_bytes, int):
            self.file_size_bytes = int(self.file_size_bytes)

        if self.checksum is not None and not isinstance(self.checksum, str):
            self.checksum = str(self.checksum)

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeEnum):
            self.data_type = DataTypeEnum(self.data_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image(NamedThing):
    """
    An image file from structural biology experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["Image"]
    class_class_curie: ClassVar[str] = "lambdaber:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.Image

    id: Union[str, ImageId] = None
    file_name: str = None
    acquisition_date: Optional[str] = None
    pixel_size: Optional[float] = None
    dimensions_x: Optional[int] = None
    dimensions_y: Optional[int] = None
    exposure_time: Optional[float] = None
    dose: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImageId):
            self.id = ImageId(self.id)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.acquisition_date is not None and not isinstance(self.acquisition_date, str):
            self.acquisition_date = str(self.acquisition_date)

        if self.pixel_size is not None and not isinstance(self.pixel_size, float):
            self.pixel_size = float(self.pixel_size)

        if self.dimensions_x is not None and not isinstance(self.dimensions_x, int):
            self.dimensions_x = int(self.dimensions_x)

        if self.dimensions_y is not None and not isinstance(self.dimensions_y, int):
            self.dimensions_y = int(self.dimensions_y)

        if self.exposure_time is not None and not isinstance(self.exposure_time, float):
            self.exposure_time = float(self.exposure_time)

        if self.dose is not None and not isinstance(self.dose, float):
            self.dose = float(self.dose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image2D(Image):
    """
    A 2D image (micrograph, diffraction pattern)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["Image2D"]
    class_class_curie: ClassVar[str] = "lambdaber:Image2D"
    class_name: ClassVar[str] = "Image2D"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.Image2D

    id: Union[str, Image2DId] = None
    file_name: str = None
    defocus: Optional[float] = None
    astigmatism: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Image2DId):
            self.id = Image2DId(self.id)

        if self.defocus is not None and not isinstance(self.defocus, float):
            self.defocus = float(self.defocus)

        if self.astigmatism is not None and not isinstance(self.astigmatism, float):
            self.astigmatism = float(self.astigmatism)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image3D(Image):
    """
    A 3D volume or tomogram
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["Image3D"]
    class_class_curie: ClassVar[str] = "lambdaber:Image3D"
    class_name: ClassVar[str] = "Image3D"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.Image3D

    id: Union[str, Image3DId] = None
    file_name: str = None
    dimensions_z: Optional[int] = None
    voxel_size: Optional[float] = None
    reconstruction_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Image3DId):
            self.id = Image3DId(self.id)

        if self.dimensions_z is not None and not isinstance(self.dimensions_z, int):
            self.dimensions_z = int(self.dimensions_z)

        if self.voxel_size is not None and not isinstance(self.voxel_size, float):
            self.voxel_size = float(self.voxel_size)

        if self.reconstruction_method is not None and not isinstance(self.reconstruction_method, str):
            self.reconstruction_method = str(self.reconstruction_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FTIRImage(Image):
    """
    Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational
    spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["FTIRImage"]
    class_class_curie: ClassVar[str] = "lambdaber:FTIRImage"
    class_name: ClassVar[str] = "FTIRImage"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.FTIRImage

    id: Union[str, FTIRImageId] = None
    file_name: str = None
    wavenumber_min: Optional[float] = None
    wavenumber_max: Optional[float] = None
    spectral_resolution: Optional[float] = None
    number_of_scans: Optional[int] = None
    apodization_function: Optional[str] = None
    molecular_signatures: Optional[Union[str, list[str]]] = empty_list()
    background_correction: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FTIRImageId):
            self.id = FTIRImageId(self.id)

        if self.wavenumber_min is not None and not isinstance(self.wavenumber_min, float):
            self.wavenumber_min = float(self.wavenumber_min)

        if self.wavenumber_max is not None and not isinstance(self.wavenumber_max, float):
            self.wavenumber_max = float(self.wavenumber_max)

        if self.spectral_resolution is not None and not isinstance(self.spectral_resolution, float):
            self.spectral_resolution = float(self.spectral_resolution)

        if self.number_of_scans is not None and not isinstance(self.number_of_scans, int):
            self.number_of_scans = int(self.number_of_scans)

        if self.apodization_function is not None and not isinstance(self.apodization_function, str):
            self.apodization_function = str(self.apodization_function)

        if not isinstance(self.molecular_signatures, list):
            self.molecular_signatures = [self.molecular_signatures] if self.molecular_signatures is not None else []
        self.molecular_signatures = [v if isinstance(v, str) else str(v) for v in self.molecular_signatures]

        if self.background_correction is not None and not isinstance(self.background_correction, str):
            self.background_correction = str(self.background_correction)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FluorescenceImage(Image2D):
    """
    Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["FluorescenceImage"]
    class_class_curie: ClassVar[str] = "lambdaber:FluorescenceImage"
    class_name: ClassVar[str] = "FluorescenceImage"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.FluorescenceImage

    id: Union[str, FluorescenceImageId] = None
    file_name: str = None
    excitation_wavelength: Optional[float] = None
    emission_wavelength: Optional[float] = None
    excitation_filter: Optional[str] = None
    emission_filter: Optional[str] = None
    fluorophore: Optional[str] = None
    channel_name: Optional[str] = None
    laser_power: Optional[float] = None
    pinhole_size: Optional[float] = None
    quantum_yield: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FluorescenceImageId):
            self.id = FluorescenceImageId(self.id)

        if self.excitation_wavelength is not None and not isinstance(self.excitation_wavelength, float):
            self.excitation_wavelength = float(self.excitation_wavelength)

        if self.emission_wavelength is not None and not isinstance(self.emission_wavelength, float):
            self.emission_wavelength = float(self.emission_wavelength)

        if self.excitation_filter is not None and not isinstance(self.excitation_filter, str):
            self.excitation_filter = str(self.excitation_filter)

        if self.emission_filter is not None and not isinstance(self.emission_filter, str):
            self.emission_filter = str(self.emission_filter)

        if self.fluorophore is not None and not isinstance(self.fluorophore, str):
            self.fluorophore = str(self.fluorophore)

        if self.channel_name is not None and not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self.laser_power is not None and not isinstance(self.laser_power, float):
            self.laser_power = float(self.laser_power)

        if self.pinhole_size is not None and not isinstance(self.pinhole_size, float):
            self.pinhole_size = float(self.pinhole_size)

        if self.quantum_yield is not None and not isinstance(self.quantum_yield, float):
            self.quantum_yield = float(self.quantum_yield)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpticalImage(Image2D):
    """
    Visible light optical microscopy or photography image
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["OpticalImage"]
    class_class_curie: ClassVar[str] = "lambdaber:OpticalImage"
    class_name: ClassVar[str] = "OpticalImage"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.OpticalImage

    id: Union[str, OpticalImageId] = None
    file_name: str = None
    illumination_type: Optional[Union[str, "IlluminationTypeEnum"]] = None
    magnification: Optional[float] = None
    numerical_aperture: Optional[float] = None
    color_channels: Optional[Union[str, list[str]]] = empty_list()
    white_balance: Optional[str] = None
    contrast_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OpticalImageId):
            self.id = OpticalImageId(self.id)

        if self.illumination_type is not None and not isinstance(self.illumination_type, IlluminationTypeEnum):
            self.illumination_type = IlluminationTypeEnum(self.illumination_type)

        if self.magnification is not None and not isinstance(self.magnification, float):
            self.magnification = float(self.magnification)

        if self.numerical_aperture is not None and not isinstance(self.numerical_aperture, float):
            self.numerical_aperture = float(self.numerical_aperture)

        if not isinstance(self.color_channels, list):
            self.color_channels = [self.color_channels] if self.color_channels is not None else []
        self.color_channels = [v if isinstance(v, str) else str(v) for v in self.color_channels]

        if self.white_balance is not None and not isinstance(self.white_balance, str):
            self.white_balance = str(self.white_balance)

        if self.contrast_method is not None and not isinstance(self.contrast_method, str):
            self.contrast_method = str(self.contrast_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRFImage(Image2D):
    """
    X-ray fluorescence (XRF) image showing elemental distribution
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["XRFImage"]
    class_class_curie: ClassVar[str] = "lambdaber:XRFImage"
    class_name: ClassVar[str] = "XRFImage"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.XRFImage

    id: Union[str, XRFImageId] = None
    file_name: str = None
    beam_energy: Optional[float] = None
    beam_size: Optional[float] = None
    dwell_time: Optional[float] = None
    elements_measured: Optional[Union[str, list[str]]] = empty_list()
    source_type: Optional[Union[str, "XRaySourceTypeEnum"]] = None
    detector_technology: Optional[Union[str, "DetectorTechnologyEnum"]] = None
    detector_model: Optional[str] = None
    flux: Optional[float] = None
    calibration_standard: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRFImageId):
            self.id = XRFImageId(self.id)

        if self.beam_energy is not None and not isinstance(self.beam_energy, float):
            self.beam_energy = float(self.beam_energy)

        if self.beam_size is not None and not isinstance(self.beam_size, float):
            self.beam_size = float(self.beam_size)

        if self.dwell_time is not None and not isinstance(self.dwell_time, float):
            self.dwell_time = float(self.dwell_time)

        if not isinstance(self.elements_measured, list):
            self.elements_measured = [self.elements_measured] if self.elements_measured is not None else []
        self.elements_measured = [v if isinstance(v, str) else str(v) for v in self.elements_measured]

        if self.source_type is not None and not isinstance(self.source_type, XRaySourceTypeEnum):
            self.source_type = XRaySourceTypeEnum(self.source_type)

        if self.detector_technology is not None and not isinstance(self.detector_technology, DetectorTechnologyEnum):
            self.detector_technology = DetectorTechnologyEnum(self.detector_technology)

        if self.detector_model is not None and not isinstance(self.detector_model, str):
            self.detector_model = str(self.detector_model)

        if self.flux is not None and not isinstance(self.flux, float):
            self.flux = float(self.flux)

        if self.calibration_standard is not None and not isinstance(self.calibration_standard, str):
            self.calibration_standard = str(self.calibration_standard)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImageFeature(AttributeGroup):
    """
    Semantic annotations describing features identified in images using controlled vocabulary terms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["ImageFeature"]
    class_class_curie: ClassVar[str] = "lambdaber:ImageFeature"
    class_name: ClassVar[str] = "ImageFeature"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ImageFeature

    terms: Optional[Union[str, OntologyTermId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.terms is not None and not isinstance(self.terms, OntologyTermId):
            self.terms = OntologyTermId(self.terms)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyTerm(NamedThing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["OntologyTerm"]
    class_class_curie: ClassVar[str] = "lambdaber:OntologyTerm"
    class_name: ClassVar[str] = "OntologyTerm"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.OntologyTerm

    id: Union[str, OntologyTermId] = None
    label: Optional[str] = None
    definition: Optional[str] = None
    ontology: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyTermId):
            self.id = OntologyTermId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.ontology is not None and not isinstance(self.ontology, str):
            self.ontology = str(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularComposition(AttributeGroup):
    """
    Molecular composition of a sample
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["MolecularComposition"]
    class_class_curie: ClassVar[str] = "lambdaber:MolecularComposition"
    class_name: ClassVar[str] = "MolecularComposition"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.MolecularComposition

    sequences: Optional[Union[str, list[str]]] = empty_list()
    modifications: Optional[Union[str, list[str]]] = empty_list()
    ligands: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.sequences, list):
            self.sequences = [self.sequences] if self.sequences is not None else []
        self.sequences = [v if isinstance(v, str) else str(v) for v in self.sequences]

        if not isinstance(self.modifications, list):
            self.modifications = [self.modifications] if self.modifications is not None else []
        self.modifications = [v if isinstance(v, str) else str(v) for v in self.modifications]

        if not isinstance(self.ligands, list):
            self.ligands = [self.ligands] if self.ligands is not None else []
        self.ligands = [v if isinstance(v, str) else str(v) for v in self.ligands]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BufferComposition(AttributeGroup):
    """
    Buffer composition for sample storage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["BufferComposition"]
    class_class_curie: ClassVar[str] = "lambdaber:BufferComposition"
    class_name: ClassVar[str] = "BufferComposition"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.BufferComposition

    ph: Optional[float] = None
    components: Optional[Union[str, list[str]]] = empty_list()
    additives: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, str) else str(v) for v in self.components]

        if not isinstance(self.additives, list):
            self.additives = [self.additives] if self.additives is not None else []
        self.additives = [v if isinstance(v, str) else str(v) for v in self.additives]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageConditions(AttributeGroup):
    """
    Storage conditions for samples
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["StorageConditions"]
    class_class_curie: ClassVar[str] = "lambdaber:StorageConditions"
    class_name: ClassVar[str] = "StorageConditions"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.StorageConditions

    temperature: Optional[float] = None
    temperature_unit: Optional[Union[str, "TemperatureUnitEnum"]] = None
    duration: Optional[str] = None
    atmosphere: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        if self.temperature_unit is not None and not isinstance(self.temperature_unit, TemperatureUnitEnum):
            self.temperature_unit = TemperatureUnitEnum(self.temperature_unit)

        if self.duration is not None and not isinstance(self.duration, str):
            self.duration = str(self.duration)

        if self.atmosphere is not None and not isinstance(self.atmosphere, str):
            self.atmosphere = str(self.atmosphere)

        super().__post_init__(**kwargs)


class TechniqueSpecificPreparation(AttributeGroup):
    """
    Base class for technique-specific preparation details
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["TechniqueSpecificPreparation"]
    class_class_curie: ClassVar[str] = "lambdaber:TechniqueSpecificPreparation"
    class_name: ClassVar[str] = "TechniqueSpecificPreparation"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.TechniqueSpecificPreparation


@dataclass(repr=False)
class CryoEMPreparation(TechniqueSpecificPreparation):
    """
    Cryo-EM specific sample preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["CryoEMPreparation"]
    class_class_curie: ClassVar[str] = "lambdaber:CryoEMPreparation"
    class_name: ClassVar[str] = "CryoEMPreparation"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.CryoEMPreparation

    grid_type: Optional[Union[str, "GridTypeEnum"]] = None
    support_film: Optional[str] = None
    hole_size: Optional[float] = None
    vitrification_method: Optional[Union[str, "VitrificationMethodEnum"]] = None
    blot_time: Optional[float] = None
    blot_force: Optional[int] = None
    humidity_percentage: Optional[float] = None
    chamber_temperature: Optional[float] = None
    plasma_treatment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.grid_type is not None and not isinstance(self.grid_type, GridTypeEnum):
            self.grid_type = GridTypeEnum(self.grid_type)

        if self.support_film is not None and not isinstance(self.support_film, str):
            self.support_film = str(self.support_film)

        if self.hole_size is not None and not isinstance(self.hole_size, float):
            self.hole_size = float(self.hole_size)

        if self.vitrification_method is not None and not isinstance(self.vitrification_method, VitrificationMethodEnum):
            self.vitrification_method = VitrificationMethodEnum(self.vitrification_method)

        if self.blot_time is not None and not isinstance(self.blot_time, float):
            self.blot_time = float(self.blot_time)

        if self.blot_force is not None and not isinstance(self.blot_force, int):
            self.blot_force = int(self.blot_force)

        if self.humidity_percentage is not None and not isinstance(self.humidity_percentage, float):
            self.humidity_percentage = float(self.humidity_percentage)

        if self.chamber_temperature is not None and not isinstance(self.chamber_temperature, float):
            self.chamber_temperature = float(self.chamber_temperature)

        if self.plasma_treatment is not None and not isinstance(self.plasma_treatment, str):
            self.plasma_treatment = str(self.plasma_treatment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrystallizationConditions(AttributeGroup):
    """
    Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization mapping)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["CrystallizationConditions"]
    class_class_curie: ClassVar[str] = "lambdaber:CrystallizationConditions"
    class_name: ClassVar[str] = "CrystallizationConditions"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.CrystallizationConditions

    method: Optional[Union[str, "CrystallizationMethodEnum"]] = None
    crystallization_conditions: Optional[str] = None
    drop_volume: Optional[float] = None
    protein_concentration: Optional[float] = None
    crystal_size_um: Optional[str] = None
    cryo_protectant: Optional[str] = None
    crystal_id: Optional[str] = None
    screen_name: Optional[str] = None
    temperature_c: Optional[float] = None
    drop_ratio_protein_to_reservoir: Optional[str] = None
    reservoir_volume_ul: Optional[float] = None
    seeding_type: Optional[str] = None
    seed_stock_dilution: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.method is not None and not isinstance(self.method, CrystallizationMethodEnum):
            self.method = CrystallizationMethodEnum(self.method)

        if self.crystallization_conditions is not None and not isinstance(self.crystallization_conditions, str):
            self.crystallization_conditions = str(self.crystallization_conditions)

        if self.drop_volume is not None and not isinstance(self.drop_volume, float):
            self.drop_volume = float(self.drop_volume)

        if self.protein_concentration is not None and not isinstance(self.protein_concentration, float):
            self.protein_concentration = float(self.protein_concentration)

        if self.crystal_size_um is not None and not isinstance(self.crystal_size_um, str):
            self.crystal_size_um = str(self.crystal_size_um)

        if self.cryo_protectant is not None and not isinstance(self.cryo_protectant, str):
            self.cryo_protectant = str(self.cryo_protectant)

        if self.crystal_id is not None and not isinstance(self.crystal_id, str):
            self.crystal_id = str(self.crystal_id)

        if self.screen_name is not None and not isinstance(self.screen_name, str):
            self.screen_name = str(self.screen_name)

        if self.temperature_c is not None and not isinstance(self.temperature_c, float):
            self.temperature_c = float(self.temperature_c)

        if self.drop_ratio_protein_to_reservoir is not None and not isinstance(self.drop_ratio_protein_to_reservoir, str):
            self.drop_ratio_protein_to_reservoir = str(self.drop_ratio_protein_to_reservoir)

        if self.reservoir_volume_ul is not None and not isinstance(self.reservoir_volume_ul, float):
            self.reservoir_volume_ul = float(self.reservoir_volume_ul)

        if self.seeding_type is not None and not isinstance(self.seeding_type, str):
            self.seeding_type = str(self.seeding_type)

        if self.seed_stock_dilution is not None and not isinstance(self.seed_stock_dilution, str):
            self.seed_stock_dilution = str(self.seed_stock_dilution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRayPreparation(TechniqueSpecificPreparation):
    """
    X-ray crystallography specific preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["XRayPreparation"]
    class_class_curie: ClassVar[str] = "lambdaber:XRayPreparation"
    class_name: ClassVar[str] = "XRayPreparation"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.XRayPreparation

    protein_concentration_mg_per_ml: Optional[float] = None
    protein_buffer: Optional[str] = None
    additives: Optional[str] = None
    crystallization_method: Optional[Union[str, "CrystallizationMethodEnum"]] = None
    crystallization_conditions: Optional[Union[dict, CrystallizationConditions]] = None
    screen_name: Optional[str] = None
    temperature_c: Optional[float] = None
    drop_ratio_protein_to_reservoir: Optional[str] = None
    drop_volume_nl: Optional[float] = None
    reservoir_volume_ul: Optional[float] = None
    seeding_type: Optional[str] = None
    seed_stock_dilution: Optional[str] = None
    initial_hit_condition: Optional[str] = None
    optimization_strategy: Optional[str] = None
    optimized_condition: Optional[str] = None
    crystal_size_um: Optional[str] = None
    cryoprotectant: Optional[str] = None
    cryoprotectant_concentration: Optional[float] = None
    soak_compound: Optional[str] = None
    soak_conditions: Optional[str] = None
    mounting_method: Optional[str] = None
    flash_cooling_method: Optional[str] = None
    crystal_notes: Optional[str] = None
    loop_size: Optional[float] = None
    mounting_temperature: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.protein_concentration_mg_per_ml is not None and not isinstance(self.protein_concentration_mg_per_ml, float):
            self.protein_concentration_mg_per_ml = float(self.protein_concentration_mg_per_ml)

        if self.protein_buffer is not None and not isinstance(self.protein_buffer, str):
            self.protein_buffer = str(self.protein_buffer)

        if self.additives is not None and not isinstance(self.additives, str):
            self.additives = str(self.additives)

        if self.crystallization_method is not None and not isinstance(self.crystallization_method, CrystallizationMethodEnum):
            self.crystallization_method = CrystallizationMethodEnum(self.crystallization_method)

        if self.crystallization_conditions is not None and not isinstance(self.crystallization_conditions, CrystallizationConditions):
            self.crystallization_conditions = CrystallizationConditions(**as_dict(self.crystallization_conditions))

        if self.screen_name is not None and not isinstance(self.screen_name, str):
            self.screen_name = str(self.screen_name)

        if self.temperature_c is not None and not isinstance(self.temperature_c, float):
            self.temperature_c = float(self.temperature_c)

        if self.drop_ratio_protein_to_reservoir is not None and not isinstance(self.drop_ratio_protein_to_reservoir, str):
            self.drop_ratio_protein_to_reservoir = str(self.drop_ratio_protein_to_reservoir)

        if self.drop_volume_nl is not None and not isinstance(self.drop_volume_nl, float):
            self.drop_volume_nl = float(self.drop_volume_nl)

        if self.reservoir_volume_ul is not None and not isinstance(self.reservoir_volume_ul, float):
            self.reservoir_volume_ul = float(self.reservoir_volume_ul)

        if self.seeding_type is not None and not isinstance(self.seeding_type, str):
            self.seeding_type = str(self.seeding_type)

        if self.seed_stock_dilution is not None and not isinstance(self.seed_stock_dilution, str):
            self.seed_stock_dilution = str(self.seed_stock_dilution)

        if self.initial_hit_condition is not None and not isinstance(self.initial_hit_condition, str):
            self.initial_hit_condition = str(self.initial_hit_condition)

        if self.optimization_strategy is not None and not isinstance(self.optimization_strategy, str):
            self.optimization_strategy = str(self.optimization_strategy)

        if self.optimized_condition is not None and not isinstance(self.optimized_condition, str):
            self.optimized_condition = str(self.optimized_condition)

        if self.crystal_size_um is not None and not isinstance(self.crystal_size_um, str):
            self.crystal_size_um = str(self.crystal_size_um)

        if self.cryoprotectant is not None and not isinstance(self.cryoprotectant, str):
            self.cryoprotectant = str(self.cryoprotectant)

        if self.cryoprotectant_concentration is not None and not isinstance(self.cryoprotectant_concentration, float):
            self.cryoprotectant_concentration = float(self.cryoprotectant_concentration)

        if self.soak_compound is not None and not isinstance(self.soak_compound, str):
            self.soak_compound = str(self.soak_compound)

        if self.soak_conditions is not None and not isinstance(self.soak_conditions, str):
            self.soak_conditions = str(self.soak_conditions)

        if self.mounting_method is not None and not isinstance(self.mounting_method, str):
            self.mounting_method = str(self.mounting_method)

        if self.flash_cooling_method is not None and not isinstance(self.flash_cooling_method, str):
            self.flash_cooling_method = str(self.flash_cooling_method)

        if self.crystal_notes is not None and not isinstance(self.crystal_notes, str):
            self.crystal_notes = str(self.crystal_notes)

        if self.loop_size is not None and not isinstance(self.loop_size, float):
            self.loop_size = float(self.loop_size)

        if self.mounting_temperature is not None and not isinstance(self.mounting_temperature, float):
            self.mounting_temperature = float(self.mounting_temperature)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SAXSPreparation(TechniqueSpecificPreparation):
    """
    SAXS/WAXS specific preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["SAXSPreparation"]
    class_class_curie: ClassVar[str] = "lambdaber:SAXSPreparation"
    class_name: ClassVar[str] = "SAXSPreparation"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.SAXSPreparation

    concentration_series: Optional[Union[float, list[float]]] = empty_list()
    buffer_matching_protocol: Optional[str] = None
    sample_cell_type: Optional[str] = None
    cell_path_length: Optional[float] = None
    temperature_control: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.concentration_series, list):
            self.concentration_series = [self.concentration_series] if self.concentration_series is not None else []
        self.concentration_series = [v if isinstance(v, float) else float(v) for v in self.concentration_series]

        if self.buffer_matching_protocol is not None and not isinstance(self.buffer_matching_protocol, str):
            self.buffer_matching_protocol = str(self.buffer_matching_protocol)

        if self.sample_cell_type is not None and not isinstance(self.sample_cell_type, str):
            self.sample_cell_type = str(self.sample_cell_type)

        if self.cell_path_length is not None and not isinstance(self.cell_path_length, float):
            self.cell_path_length = float(self.cell_path_length)

        if self.temperature_control is not None and not isinstance(self.temperature_control, str):
            self.temperature_control = str(self.temperature_control)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalConditions(AttributeGroup):
    """
    Environmental and experimental conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["ExperimentalConditions"]
    class_class_curie: ClassVar[str] = "lambdaber:ExperimentalConditions"
    class_name: ClassVar[str] = "ExperimentalConditions"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ExperimentalConditions

    temperature: Optional[float] = None
    humidity: Optional[float] = None
    pressure: Optional[float] = None
    atmosphere: Optional[str] = None
    beam_energy: Optional[float] = None
    exposure_time: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        if self.humidity is not None and not isinstance(self.humidity, float):
            self.humidity = float(self.humidity)

        if self.pressure is not None and not isinstance(self.pressure, float):
            self.pressure = float(self.pressure)

        if self.atmosphere is not None and not isinstance(self.atmosphere, str):
            self.atmosphere = str(self.atmosphere)

        if self.beam_energy is not None and not isinstance(self.beam_energy, float):
            self.beam_energy = float(self.beam_energy)

        if self.exposure_time is not None and not isinstance(self.exposure_time, float):
            self.exposure_time = float(self.exposure_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataCollectionStrategy(AttributeGroup):
    """
    Strategy for data collection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["DataCollectionStrategy"]
    class_class_curie: ClassVar[str] = "lambdaber:DataCollectionStrategy"
    class_name: ClassVar[str] = "DataCollectionStrategy"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.DataCollectionStrategy

    collection_mode: Optional[Union[str, "CollectionModeEnum"]] = None
    total_frames: Optional[int] = None
    frame_rate: Optional[float] = None
    total_dose: Optional[float] = None
    dose_per_frame: Optional[float] = None
    wavelength_a: Optional[float] = None
    detector_mode: Optional[Union[str, "DetectorModeEnum"]] = None
    pixel_size_calibrated: Optional[float] = None
    detector_distance_mm: Optional[float] = None
    beam_center_x_px: Optional[int] = None
    beam_center_y_px: Optional[int] = None
    beam_size_um: Optional[float] = None
    flux_photons_per_s: Optional[float] = None
    transmission_percent: Optional[float] = None
    attenuator: Optional[str] = None
    temperature_k: Optional[float] = None
    oscillation_per_image_deg: Optional[float] = None
    total_rotation_deg: Optional[float] = None
    strategy_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.collection_mode is not None and not isinstance(self.collection_mode, CollectionModeEnum):
            self.collection_mode = CollectionModeEnum(self.collection_mode)

        if self.total_frames is not None and not isinstance(self.total_frames, int):
            self.total_frames = int(self.total_frames)

        if self.frame_rate is not None and not isinstance(self.frame_rate, float):
            self.frame_rate = float(self.frame_rate)

        if self.total_dose is not None and not isinstance(self.total_dose, float):
            self.total_dose = float(self.total_dose)

        if self.dose_per_frame is not None and not isinstance(self.dose_per_frame, float):
            self.dose_per_frame = float(self.dose_per_frame)

        if self.wavelength_a is not None and not isinstance(self.wavelength_a, float):
            self.wavelength_a = float(self.wavelength_a)

        if self.detector_mode is not None and not isinstance(self.detector_mode, DetectorModeEnum):
            self.detector_mode = DetectorModeEnum(self.detector_mode)

        if self.pixel_size_calibrated is not None and not isinstance(self.pixel_size_calibrated, float):
            self.pixel_size_calibrated = float(self.pixel_size_calibrated)

        if self.detector_distance_mm is not None and not isinstance(self.detector_distance_mm, float):
            self.detector_distance_mm = float(self.detector_distance_mm)

        if self.beam_center_x_px is not None and not isinstance(self.beam_center_x_px, int):
            self.beam_center_x_px = int(self.beam_center_x_px)

        if self.beam_center_y_px is not None and not isinstance(self.beam_center_y_px, int):
            self.beam_center_y_px = int(self.beam_center_y_px)

        if self.beam_size_um is not None and not isinstance(self.beam_size_um, float):
            self.beam_size_um = float(self.beam_size_um)

        if self.flux_photons_per_s is not None and not isinstance(self.flux_photons_per_s, float):
            self.flux_photons_per_s = float(self.flux_photons_per_s)

        if self.transmission_percent is not None and not isinstance(self.transmission_percent, float):
            self.transmission_percent = float(self.transmission_percent)

        if self.attenuator is not None and not isinstance(self.attenuator, str):
            self.attenuator = str(self.attenuator)

        if self.temperature_k is not None and not isinstance(self.temperature_k, float):
            self.temperature_k = float(self.temperature_k)

        if self.oscillation_per_image_deg is not None and not isinstance(self.oscillation_per_image_deg, float):
            self.oscillation_per_image_deg = float(self.oscillation_per_image_deg)

        if self.total_rotation_deg is not None and not isinstance(self.total_rotation_deg, float):
            self.total_rotation_deg = float(self.total_rotation_deg)

        if self.strategy_notes is not None and not isinstance(self.strategy_notes, str):
            self.strategy_notes = str(self.strategy_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualityMetrics(AttributeGroup):
    """
    Quality metrics for experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["QualityMetrics"]
    class_class_curie: ClassVar[str] = "lambdaber:QualityMetrics"
    class_name: ClassVar[str] = "QualityMetrics"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.QualityMetrics

    resolution: Optional[float] = None
    resolution_high_shell_a: Optional[float] = None
    resolution_low_a: Optional[float] = None
    completeness: Optional[float] = None
    completeness_high_res_shell_percent: Optional[float] = None
    signal_to_noise: Optional[float] = None
    mean_i_over_sigma_i: Optional[float] = None
    space_group: Optional[str] = None
    unit_cell_a: Optional[float] = None
    unit_cell_b: Optional[float] = None
    unit_cell_c: Optional[float] = None
    unit_cell_alpha: Optional[float] = None
    unit_cell_beta: Optional[float] = None
    unit_cell_gamma: Optional[float] = None
    multiplicity: Optional[float] = None
    cc_half: Optional[float] = None
    r_merge: Optional[float] = None
    r_pim: Optional[float] = None
    wilson_b_factor_a2: Optional[float] = None
    anomalous_used: Optional[Union[bool, Bool]] = None
    anom_corr: Optional[float] = None
    anom_sig_ano: Optional[float] = None
    r_work: Optional[float] = None
    r_free: Optional[float] = None
    ramachandran_favored_percent: Optional[float] = None
    ramachandran_outliers_percent: Optional[float] = None
    clashscore: Optional[float] = None
    molprobity_score: Optional[float] = None
    average_b_factor_a2: Optional[float] = None
    i_zero: Optional[float] = None
    rg: Optional[float] = None
    r_factor: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.resolution is not None and not isinstance(self.resolution, float):
            self.resolution = float(self.resolution)

        if self.resolution_high_shell_a is not None and not isinstance(self.resolution_high_shell_a, float):
            self.resolution_high_shell_a = float(self.resolution_high_shell_a)

        if self.resolution_low_a is not None and not isinstance(self.resolution_low_a, float):
            self.resolution_low_a = float(self.resolution_low_a)

        if self.completeness is not None and not isinstance(self.completeness, float):
            self.completeness = float(self.completeness)

        if self.completeness_high_res_shell_percent is not None and not isinstance(self.completeness_high_res_shell_percent, float):
            self.completeness_high_res_shell_percent = float(self.completeness_high_res_shell_percent)

        if self.signal_to_noise is not None and not isinstance(self.signal_to_noise, float):
            self.signal_to_noise = float(self.signal_to_noise)

        if self.mean_i_over_sigma_i is not None and not isinstance(self.mean_i_over_sigma_i, float):
            self.mean_i_over_sigma_i = float(self.mean_i_over_sigma_i)

        if self.space_group is not None and not isinstance(self.space_group, str):
            self.space_group = str(self.space_group)

        if self.unit_cell_a is not None and not isinstance(self.unit_cell_a, float):
            self.unit_cell_a = float(self.unit_cell_a)

        if self.unit_cell_b is not None and not isinstance(self.unit_cell_b, float):
            self.unit_cell_b = float(self.unit_cell_b)

        if self.unit_cell_c is not None and not isinstance(self.unit_cell_c, float):
            self.unit_cell_c = float(self.unit_cell_c)

        if self.unit_cell_alpha is not None and not isinstance(self.unit_cell_alpha, float):
            self.unit_cell_alpha = float(self.unit_cell_alpha)

        if self.unit_cell_beta is not None and not isinstance(self.unit_cell_beta, float):
            self.unit_cell_beta = float(self.unit_cell_beta)

        if self.unit_cell_gamma is not None and not isinstance(self.unit_cell_gamma, float):
            self.unit_cell_gamma = float(self.unit_cell_gamma)

        if self.multiplicity is not None and not isinstance(self.multiplicity, float):
            self.multiplicity = float(self.multiplicity)

        if self.cc_half is not None and not isinstance(self.cc_half, float):
            self.cc_half = float(self.cc_half)

        if self.r_merge is not None and not isinstance(self.r_merge, float):
            self.r_merge = float(self.r_merge)

        if self.r_pim is not None and not isinstance(self.r_pim, float):
            self.r_pim = float(self.r_pim)

        if self.wilson_b_factor_a2 is not None and not isinstance(self.wilson_b_factor_a2, float):
            self.wilson_b_factor_a2 = float(self.wilson_b_factor_a2)

        if self.anomalous_used is not None and not isinstance(self.anomalous_used, Bool):
            self.anomalous_used = Bool(self.anomalous_used)

        if self.anom_corr is not None and not isinstance(self.anom_corr, float):
            self.anom_corr = float(self.anom_corr)

        if self.anom_sig_ano is not None and not isinstance(self.anom_sig_ano, float):
            self.anom_sig_ano = float(self.anom_sig_ano)

        if self.r_work is not None and not isinstance(self.r_work, float):
            self.r_work = float(self.r_work)

        if self.r_free is not None and not isinstance(self.r_free, float):
            self.r_free = float(self.r_free)

        if self.ramachandran_favored_percent is not None and not isinstance(self.ramachandran_favored_percent, float):
            self.ramachandran_favored_percent = float(self.ramachandran_favored_percent)

        if self.ramachandran_outliers_percent is not None and not isinstance(self.ramachandran_outliers_percent, float):
            self.ramachandran_outliers_percent = float(self.ramachandran_outliers_percent)

        if self.clashscore is not None and not isinstance(self.clashscore, float):
            self.clashscore = float(self.clashscore)

        if self.molprobity_score is not None and not isinstance(self.molprobity_score, float):
            self.molprobity_score = float(self.molprobity_score)

        if self.average_b_factor_a2 is not None and not isinstance(self.average_b_factor_a2, float):
            self.average_b_factor_a2 = float(self.average_b_factor_a2)

        if self.i_zero is not None and not isinstance(self.i_zero, float):
            self.i_zero = float(self.i_zero)

        if self.rg is not None and not isinstance(self.rg, float):
            self.rg = float(self.rg)

        if self.r_factor is not None and not isinstance(self.r_factor, float):
            self.r_factor = float(self.r_factor)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputeResources(AttributeGroup):
    """
    Computational resources used
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["ComputeResources"]
    class_class_curie: ClassVar[str] = "lambdaber:ComputeResources"
    class_name: ClassVar[str] = "ComputeResources"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ComputeResources

    cpu_hours: Optional[float] = None
    gpu_hours: Optional[float] = None
    memory_gb: Optional[float] = None
    storage_gb: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cpu_hours is not None and not isinstance(self.cpu_hours, float):
            self.cpu_hours = float(self.cpu_hours)

        if self.gpu_hours is not None and not isinstance(self.gpu_hours, float):
            self.gpu_hours = float(self.gpu_hours)

        if self.memory_gb is not None and not isinstance(self.memory_gb, float):
            self.memory_gb = float(self.memory_gb)

        if self.storage_gb is not None and not isinstance(self.storage_gb, float):
            self.storage_gb = float(self.storage_gb)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinAnnotation(NamedThing):
    """
    Base class for all protein-related functional and structural annotations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/ProteinAnnotation"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/ProteinAnnotation"
    class_name: ClassVar[str] = "ProteinAnnotation"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ProteinAnnotation

    id: Union[str, ProteinAnnotationId] = None
    protein_id: str = None
    pdb_entry: Optional[str] = None
    chain_id: Optional[str] = None
    residue_range: Optional[str] = None
    confidence_score: Optional[float] = None
    evidence_type: Optional[Union[str, "EvidenceTypeEnum"]] = None
    evidence_code: Optional[Union[str, URIorCURIE]] = None
    source_database: Optional[Union[str, "AnnotationSourceEnum"]] = None
    annotation_method: Optional[str] = None
    publication_ids: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinAnnotationId):
            self.id = ProteinAnnotationId(self.id)

        if self._is_empty(self.protein_id):
            self.MissingRequiredField("protein_id")
        if not isinstance(self.protein_id, str):
            self.protein_id = str(self.protein_id)

        if self.pdb_entry is not None and not isinstance(self.pdb_entry, str):
            self.pdb_entry = str(self.pdb_entry)

        if self.chain_id is not None and not isinstance(self.chain_id, str):
            self.chain_id = str(self.chain_id)

        if self.residue_range is not None and not isinstance(self.residue_range, str):
            self.residue_range = str(self.residue_range)

        if self.confidence_score is not None and not isinstance(self.confidence_score, float):
            self.confidence_score = float(self.confidence_score)

        if self.evidence_type is not None and not isinstance(self.evidence_type, EvidenceTypeEnum):
            self.evidence_type = EvidenceTypeEnum(self.evidence_type)

        if self.evidence_code is not None and not isinstance(self.evidence_code, URIorCURIE):
            self.evidence_code = URIorCURIE(self.evidence_code)

        if self.source_database is not None and not isinstance(self.source_database, AnnotationSourceEnum):
            self.source_database = AnnotationSourceEnum(self.source_database)

        if self.annotation_method is not None and not isinstance(self.annotation_method, str):
            self.annotation_method = str(self.annotation_method)

        if not isinstance(self.publication_ids, list):
            self.publication_ids = [self.publication_ids] if self.publication_ids is not None else []
        self.publication_ids = [v if isinstance(v, str) else str(v) for v in self.publication_ids]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalSite(ProteinAnnotation):
    """
    Functional sites including catalytic, binding, and regulatory sites
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/FunctionalSite"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/FunctionalSite"
    class_name: ClassVar[str] = "FunctionalSite"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.FunctionalSite

    id: Union[str, FunctionalSiteId] = None
    protein_id: str = None
    site_type: Union[str, "FunctionalSiteTypeEnum"] = None
    site_name: Optional[str] = None
    residues: Optional[Union[str, list[str]]] = empty_list()
    ligand_interactions: Optional[Union[Union[dict, "LigandInteraction"], list[Union[dict, "LigandInteraction"]]]] = empty_list()
    conservation_score: Optional[float] = None
    functional_importance: Optional[str] = None
    go_terms: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    ec_number: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalSiteId):
            self.id = FunctionalSiteId(self.id)

        if self._is_empty(self.site_type):
            self.MissingRequiredField("site_type")
        if not isinstance(self.site_type, FunctionalSiteTypeEnum):
            self.site_type = FunctionalSiteTypeEnum(self.site_type)

        if self.site_name is not None and not isinstance(self.site_name, str):
            self.site_name = str(self.site_name)

        if not isinstance(self.residues, list):
            self.residues = [self.residues] if self.residues is not None else []
        self.residues = [v if isinstance(v, str) else str(v) for v in self.residues]

        if not isinstance(self.ligand_interactions, list):
            self.ligand_interactions = [self.ligand_interactions] if self.ligand_interactions is not None else []
        self.ligand_interactions = [v if isinstance(v, LigandInteraction) else LigandInteraction(**as_dict(v)) for v in self.ligand_interactions]

        if self.conservation_score is not None and not isinstance(self.conservation_score, float):
            self.conservation_score = float(self.conservation_score)

        if self.functional_importance is not None and not isinstance(self.functional_importance, str):
            self.functional_importance = str(self.functional_importance)

        if not isinstance(self.go_terms, list):
            self.go_terms = [self.go_terms] if self.go_terms is not None else []
        self.go_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.go_terms]

        if self.ec_number is not None and not isinstance(self.ec_number, str):
            self.ec_number = str(self.ec_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StructuralFeature(ProteinAnnotation):
    """
    Structural features and properties of protein regions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/StructuralFeature"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/StructuralFeature"
    class_name: ClassVar[str] = "StructuralFeature"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.StructuralFeature

    id: Union[str, StructuralFeatureId] = None
    protein_id: str = None
    feature_type: Union[str, "StructuralFeatureTypeEnum"] = None
    secondary_structure: Optional[Union[str, "SecondaryStructureEnum"]] = None
    solvent_accessibility: Optional[float] = None
    backbone_flexibility: Optional[float] = None
    disorder_probability: Optional[float] = None
    conformational_state: Optional[Union[str, "ConformationalStateEnum"]] = None
    structural_motif: Optional[str] = None
    domain_assignment: Optional[str] = None
    domain_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StructuralFeatureId):
            self.id = StructuralFeatureId(self.id)

        if self._is_empty(self.feature_type):
            self.MissingRequiredField("feature_type")
        if not isinstance(self.feature_type, StructuralFeatureTypeEnum):
            self.feature_type = StructuralFeatureTypeEnum(self.feature_type)

        if self.secondary_structure is not None and not isinstance(self.secondary_structure, SecondaryStructureEnum):
            self.secondary_structure = SecondaryStructureEnum(self.secondary_structure)

        if self.solvent_accessibility is not None and not isinstance(self.solvent_accessibility, float):
            self.solvent_accessibility = float(self.solvent_accessibility)

        if self.backbone_flexibility is not None and not isinstance(self.backbone_flexibility, float):
            self.backbone_flexibility = float(self.backbone_flexibility)

        if self.disorder_probability is not None and not isinstance(self.disorder_probability, float):
            self.disorder_probability = float(self.disorder_probability)

        if self.conformational_state is not None and not isinstance(self.conformational_state, ConformationalStateEnum):
            self.conformational_state = ConformationalStateEnum(self.conformational_state)

        if self.structural_motif is not None and not isinstance(self.structural_motif, str):
            self.structural_motif = str(self.structural_motif)

        if self.domain_assignment is not None and not isinstance(self.domain_assignment, str):
            self.domain_assignment = str(self.domain_assignment)

        if self.domain_id is not None and not isinstance(self.domain_id, str):
            self.domain_id = str(self.domain_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LigandInteraction(AttributeGroup):
    """
    Small molecule/ligand interactions with proteins
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/LigandInteraction"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/LigandInteraction"
    class_name: ClassVar[str] = "LigandInteraction"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.LigandInteraction

    ligand_id: str = None
    ligand_name: str = None
    ligand_smiles: Optional[str] = None
    binding_affinity: Optional[float] = None
    binding_affinity_type: Optional[Union[str, "BindingAffinityTypeEnum"]] = None
    binding_affinity_unit: Optional[Union[str, "AffinityUnitEnum"]] = None
    interaction_type: Optional[Union[str, "InteractionTypeEnum"]] = None
    binding_site_residues: Optional[Union[str, list[str]]] = empty_list()
    is_cofactor: Optional[Union[bool, Bool]] = None
    is_drug_like: Optional[Union[bool, Bool]] = None
    druggability_score: Optional[float] = None
    interaction_distance: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ligand_id):
            self.MissingRequiredField("ligand_id")
        if not isinstance(self.ligand_id, str):
            self.ligand_id = str(self.ligand_id)

        if self._is_empty(self.ligand_name):
            self.MissingRequiredField("ligand_name")
        if not isinstance(self.ligand_name, str):
            self.ligand_name = str(self.ligand_name)

        if self.ligand_smiles is not None and not isinstance(self.ligand_smiles, str):
            self.ligand_smiles = str(self.ligand_smiles)

        if self.binding_affinity is not None and not isinstance(self.binding_affinity, float):
            self.binding_affinity = float(self.binding_affinity)

        if self.binding_affinity_type is not None and not isinstance(self.binding_affinity_type, BindingAffinityTypeEnum):
            self.binding_affinity_type = BindingAffinityTypeEnum(self.binding_affinity_type)

        if self.binding_affinity_unit is not None and not isinstance(self.binding_affinity_unit, AffinityUnitEnum):
            self.binding_affinity_unit = AffinityUnitEnum(self.binding_affinity_unit)

        if self.interaction_type is not None and not isinstance(self.interaction_type, InteractionTypeEnum):
            self.interaction_type = InteractionTypeEnum(self.interaction_type)

        if not isinstance(self.binding_site_residues, list):
            self.binding_site_residues = [self.binding_site_residues] if self.binding_site_residues is not None else []
        self.binding_site_residues = [v if isinstance(v, str) else str(v) for v in self.binding_site_residues]

        if self.is_cofactor is not None and not isinstance(self.is_cofactor, Bool):
            self.is_cofactor = Bool(self.is_cofactor)

        if self.is_drug_like is not None and not isinstance(self.is_drug_like, Bool):
            self.is_drug_like = Bool(self.is_drug_like)

        if self.druggability_score is not None and not isinstance(self.druggability_score, float):
            self.druggability_score = float(self.druggability_score)

        if self.interaction_distance is not None and not isinstance(self.interaction_distance, float):
            self.interaction_distance = float(self.interaction_distance)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinProteinInteraction(ProteinAnnotation):
    """
    Protein-protein interactions and interfaces
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/ProteinProteinInteraction"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/ProteinProteinInteraction"
    class_name: ClassVar[str] = "ProteinProteinInteraction"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ProteinProteinInteraction

    id: Union[str, ProteinProteinInteractionId] = None
    protein_id: str = None
    partner_protein_id: str = None
    partner_chain_id: Optional[str] = None
    interface_residues: Optional[Union[str, list[str]]] = empty_list()
    partner_interface_residues: Optional[Union[str, list[str]]] = empty_list()
    interface_area: Optional[float] = None
    binding_energy: Optional[float] = None
    dissociation_constant: Optional[float] = None
    complex_stability: Optional[Union[str, "ComplexStabilityEnum"]] = None
    biological_assembly: Optional[Union[bool, Bool]] = None
    interaction_evidence: Optional[Union[Union[str, "InteractionEvidenceEnum"], list[Union[str, "InteractionEvidenceEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinProteinInteractionId):
            self.id = ProteinProteinInteractionId(self.id)

        if self._is_empty(self.partner_protein_id):
            self.MissingRequiredField("partner_protein_id")
        if not isinstance(self.partner_protein_id, str):
            self.partner_protein_id = str(self.partner_protein_id)

        if self.partner_chain_id is not None and not isinstance(self.partner_chain_id, str):
            self.partner_chain_id = str(self.partner_chain_id)

        if not isinstance(self.interface_residues, list):
            self.interface_residues = [self.interface_residues] if self.interface_residues is not None else []
        self.interface_residues = [v if isinstance(v, str) else str(v) for v in self.interface_residues]

        if not isinstance(self.partner_interface_residues, list):
            self.partner_interface_residues = [self.partner_interface_residues] if self.partner_interface_residues is not None else []
        self.partner_interface_residues = [v if isinstance(v, str) else str(v) for v in self.partner_interface_residues]

        if self.interface_area is not None and not isinstance(self.interface_area, float):
            self.interface_area = float(self.interface_area)

        if self.binding_energy is not None and not isinstance(self.binding_energy, float):
            self.binding_energy = float(self.binding_energy)

        if self.dissociation_constant is not None and not isinstance(self.dissociation_constant, float):
            self.dissociation_constant = float(self.dissociation_constant)

        if self.complex_stability is not None and not isinstance(self.complex_stability, ComplexStabilityEnum):
            self.complex_stability = ComplexStabilityEnum(self.complex_stability)

        if self.biological_assembly is not None and not isinstance(self.biological_assembly, Bool):
            self.biological_assembly = Bool(self.biological_assembly)

        if not isinstance(self.interaction_evidence, list):
            self.interaction_evidence = [self.interaction_evidence] if self.interaction_evidence is not None else []
        self.interaction_evidence = [v if isinstance(v, InteractionEvidenceEnum) else InteractionEvidenceEnum(v) for v in self.interaction_evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MutationEffect(ProteinAnnotation):
    """
    Effects of mutations and variants on protein structure and function
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/MutationEffect"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/MutationEffect"
    class_name: ClassVar[str] = "MutationEffect"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.MutationEffect

    id: Union[str, MutationEffectId] = None
    protein_id: str = None
    mutation: str = None
    mutation_type: Optional[Union[str, "MutationTypeEnum"]] = None
    effect_on_stability: Optional[Union[str, "StabilityEffectEnum"]] = None
    delta_delta_g: Optional[float] = None
    effect_on_function: Optional[Union[str, "FunctionalEffectEnum"]] = None
    functional_impact_description: Optional[str] = None
    disease_association: Optional[str] = None
    omim_id: Optional[str] = None
    clinical_significance: Optional[Union[str, "ClinicalSignificanceEnum"]] = None
    allele_frequency: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MutationEffectId):
            self.id = MutationEffectId(self.id)

        if self._is_empty(self.mutation):
            self.MissingRequiredField("mutation")
        if not isinstance(self.mutation, str):
            self.mutation = str(self.mutation)

        if self.mutation_type is not None and not isinstance(self.mutation_type, MutationTypeEnum):
            self.mutation_type = MutationTypeEnum(self.mutation_type)

        if self.effect_on_stability is not None and not isinstance(self.effect_on_stability, StabilityEffectEnum):
            self.effect_on_stability = StabilityEffectEnum(self.effect_on_stability)

        if self.delta_delta_g is not None and not isinstance(self.delta_delta_g, float):
            self.delta_delta_g = float(self.delta_delta_g)

        if self.effect_on_function is not None and not isinstance(self.effect_on_function, FunctionalEffectEnum):
            self.effect_on_function = FunctionalEffectEnum(self.effect_on_function)

        if self.functional_impact_description is not None and not isinstance(self.functional_impact_description, str):
            self.functional_impact_description = str(self.functional_impact_description)

        if self.disease_association is not None and not isinstance(self.disease_association, str):
            self.disease_association = str(self.disease_association)

        if self.omim_id is not None and not isinstance(self.omim_id, str):
            self.omim_id = str(self.omim_id)

        if self.clinical_significance is not None and not isinstance(self.clinical_significance, ClinicalSignificanceEnum):
            self.clinical_significance = ClinicalSignificanceEnum(self.clinical_significance)

        if self.allele_frequency is not None and not isinstance(self.allele_frequency, float):
            self.allele_frequency = float(self.allele_frequency)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiophysicalProperty(AttributeGroup):
    """
    Measured or calculated biophysical properties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/BiophysicalProperty"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/BiophysicalProperty"
    class_name: ClassVar[str] = "BiophysicalProperty"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.BiophysicalProperty

    property_type: Union[str, "BiophysicalPropertyEnum"] = None
    value: float = None
    unit: str = None
    error: Optional[float] = None
    measurement_conditions: Optional[str] = None
    temperature: Optional[float] = None
    ph: Optional[float] = None
    ionic_strength: Optional[float] = None
    experimental_method: Optional[Union[str, "BiophysicalMethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.property_type):
            self.MissingRequiredField("property_type")
        if not isinstance(self.property_type, BiophysicalPropertyEnum):
            self.property_type = BiophysicalPropertyEnum(self.property_type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.error is not None and not isinstance(self.error, float):
            self.error = float(self.error)

        if self.measurement_conditions is not None and not isinstance(self.measurement_conditions, str):
            self.measurement_conditions = str(self.measurement_conditions)

        if self.temperature is not None and not isinstance(self.temperature, float):
            self.temperature = float(self.temperature)

        if self.ph is not None and not isinstance(self.ph, float):
            self.ph = float(self.ph)

        if self.ionic_strength is not None and not isinstance(self.ionic_strength, float):
            self.ionic_strength = float(self.ionic_strength)

        if self.experimental_method is not None and not isinstance(self.experimental_method, BiophysicalMethodEnum):
            self.experimental_method = BiophysicalMethodEnum(self.experimental_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConformationalEnsemble(NamedThing):
    """
    Ensemble of conformational states for a protein
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/ConformationalEnsemble"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/ConformationalEnsemble"
    class_name: ClassVar[str] = "ConformationalEnsemble"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ConformationalEnsemble

    id: Union[str, ConformationalEnsembleId] = None
    protein_id: str = None
    conformational_states: Optional[Union[Union[dict, "ConformationalState"], list[Union[dict, "ConformationalState"]]]] = empty_list()
    clustering_method: Optional[str] = None
    rmsd_threshold: Optional[float] = None
    transition_pathways: Optional[str] = None
    energy_landscape: Optional[str] = None
    principal_motions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConformationalEnsembleId):
            self.id = ConformationalEnsembleId(self.id)

        if self._is_empty(self.protein_id):
            self.MissingRequiredField("protein_id")
        if not isinstance(self.protein_id, str):
            self.protein_id = str(self.protein_id)

        if not isinstance(self.conformational_states, list):
            self.conformational_states = [self.conformational_states] if self.conformational_states is not None else []
        self.conformational_states = [v if isinstance(v, ConformationalState) else ConformationalState(**as_dict(v)) for v in self.conformational_states]

        if self.clustering_method is not None and not isinstance(self.clustering_method, str):
            self.clustering_method = str(self.clustering_method)

        if self.rmsd_threshold is not None and not isinstance(self.rmsd_threshold, float):
            self.rmsd_threshold = float(self.rmsd_threshold)

        if self.transition_pathways is not None and not isinstance(self.transition_pathways, str):
            self.transition_pathways = str(self.transition_pathways)

        if self.energy_landscape is not None and not isinstance(self.energy_landscape, str):
            self.energy_landscape = str(self.energy_landscape)

        if not isinstance(self.principal_motions, list):
            self.principal_motions = [self.principal_motions] if self.principal_motions is not None else []
        self.principal_motions = [v if isinstance(v, str) else str(v) for v in self.principal_motions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConformationalState(AttributeGroup):
    """
    Individual conformational state
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/ConformationalState"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/ConformationalState"
    class_name: ClassVar[str] = "ConformationalState"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.ConformationalState

    state_id: str = None
    state_name: Optional[str] = None
    pdb_entries: Optional[Union[str, list[str]]] = empty_list()
    population: Optional[float] = None
    free_energy: Optional[float] = None
    rmsd_from_reference: Optional[float] = None
    characteristic_features: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state_id):
            self.MissingRequiredField("state_id")
        if not isinstance(self.state_id, str):
            self.state_id = str(self.state_id)

        if self.state_name is not None and not isinstance(self.state_name, str):
            self.state_name = str(self.state_name)

        if not isinstance(self.pdb_entries, list):
            self.pdb_entries = [self.pdb_entries] if self.pdb_entries is not None else []
        self.pdb_entries = [v if isinstance(v, str) else str(v) for v in self.pdb_entries]

        if self.population is not None and not isinstance(self.population, float):
            self.population = float(self.population)

        if self.free_energy is not None and not isinstance(self.free_energy, float):
            self.free_energy = float(self.free_energy)

        if self.rmsd_from_reference is not None and not isinstance(self.rmsd_from_reference, float):
            self.rmsd_from_reference = float(self.rmsd_from_reference)

        if not isinstance(self.characteristic_features, list):
            self.characteristic_features = [self.characteristic_features] if self.characteristic_features is not None else []
        self.characteristic_features = [v if isinstance(v, str) else str(v) for v in self.characteristic_features]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTranslationalModification(ProteinAnnotation):
    """
    Post-translational modifications observed or predicted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/PostTranslationalModification"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/PostTranslationalModification"
    class_name: ClassVar[str] = "PostTranslationalModification"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.PostTranslationalModification

    id: Union[str, PostTranslationalModificationId] = None
    protein_id: str = None
    modification_type: Union[str, "PTMTypeEnum"] = None
    modified_residue: str = None
    modification_group: Optional[str] = None
    mass_shift: Optional[float] = None
    functional_effect: Optional[str] = None
    regulatory_role: Optional[str] = None
    enzyme: Optional[str] = None
    removal_enzyme: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostTranslationalModificationId):
            self.id = PostTranslationalModificationId(self.id)

        if self._is_empty(self.modification_type):
            self.MissingRequiredField("modification_type")
        if not isinstance(self.modification_type, PTMTypeEnum):
            self.modification_type = PTMTypeEnum(self.modification_type)

        if self._is_empty(self.modified_residue):
            self.MissingRequiredField("modified_residue")
        if not isinstance(self.modified_residue, str):
            self.modified_residue = str(self.modified_residue)

        if self.modification_group is not None and not isinstance(self.modification_group, str):
            self.modification_group = str(self.modification_group)

        if self.mass_shift is not None and not isinstance(self.mass_shift, float):
            self.mass_shift = float(self.mass_shift)

        if self.functional_effect is not None and not isinstance(self.functional_effect, str):
            self.functional_effect = str(self.functional_effect)

        if self.regulatory_role is not None and not isinstance(self.regulatory_role, str):
            self.regulatory_role = str(self.regulatory_role)

        if self.enzyme is not None and not isinstance(self.enzyme, str):
            self.enzyme = str(self.enzyme)

        if self.removal_enzyme is not None and not isinstance(self.removal_enzyme, str):
            self.removal_enzyme = str(self.removal_enzyme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatabaseCrossReference(AttributeGroup):
    """
    Cross-references to external databases
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/DatabaseCrossReference"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/DatabaseCrossReference"
    class_name: ClassVar[str] = "DatabaseCrossReference"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.DatabaseCrossReference

    database_name: Union[str, "DatabaseNameEnum"] = None
    database_id: str = None
    database_url: Optional[Union[str, URI]] = None
    last_updated: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.database_name):
            self.MissingRequiredField("database_name")
        if not isinstance(self.database_name, DatabaseNameEnum):
            self.database_name = DatabaseNameEnum(self.database_name)

        if self._is_empty(self.database_id):
            self.MissingRequiredField("database_id")
        if not isinstance(self.database_id, str):
            self.database_id = str(self.database_id)

        if self.database_url is not None and not isinstance(self.database_url, URI):
            self.database_url = URI(self.database_url)

        if self.last_updated is not None and not isinstance(self.last_updated, str):
            self.last_updated = str(self.last_updated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvolutionaryConservation(ProteinAnnotation):
    """
    Evolutionary conservation information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/EvolutionaryConservation"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/EvolutionaryConservation"
    class_name: ClassVar[str] = "EvolutionaryConservation"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.EvolutionaryConservation

    id: Union[str, EvolutionaryConservationId] = None
    protein_id: str = None
    conservation_score: Optional[float] = None
    conserved_residues: Optional[Union[str, list[str]]] = empty_list()
    variable_residues: Optional[Union[str, list[str]]] = empty_list()
    conservation_method: Optional[str] = None
    alignment_depth: Optional[int] = None
    taxonomic_range: Optional[str] = None
    coevolved_residues: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvolutionaryConservationId):
            self.id = EvolutionaryConservationId(self.id)

        if self.conservation_score is not None and not isinstance(self.conservation_score, float):
            self.conservation_score = float(self.conservation_score)

        if not isinstance(self.conserved_residues, list):
            self.conserved_residues = [self.conserved_residues] if self.conserved_residues is not None else []
        self.conserved_residues = [v if isinstance(v, str) else str(v) for v in self.conserved_residues]

        if not isinstance(self.variable_residues, list):
            self.variable_residues = [self.variable_residues] if self.variable_residues is not None else []
        self.variable_residues = [v if isinstance(v, str) else str(v) for v in self.variable_residues]

        if self.conservation_method is not None and not isinstance(self.conservation_method, str):
            self.conservation_method = str(self.conservation_method)

        if self.alignment_depth is not None and not isinstance(self.alignment_depth, int):
            self.alignment_depth = int(self.alignment_depth)

        if self.taxonomic_range is not None and not isinstance(self.taxonomic_range, str):
            self.taxonomic_range = str(self.taxonomic_range)

        if not isinstance(self.coevolved_residues, list):
            self.coevolved_residues = [self.coevolved_residues] if self.coevolved_residues is not None else []
        self.coevolved_residues = [v if isinstance(v, str) else str(v) for v in self.coevolved_residues]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AggregatedProteinView(NamedThing):
    """
    Aggregated view of all structural and functional data for a protein
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LAMBDABER["functional_annotation/AggregatedProteinView"]
    class_class_curie: ClassVar[str] = "lambdaber:functional_annotation/AggregatedProteinView"
    class_name: ClassVar[str] = "AggregatedProteinView"
    class_model_uri: ClassVar[URIRef] = LAMBDABER.AggregatedProteinView

    id: Union[str, AggregatedProteinViewId] = None
    uniprot_id: str = None
    protein_name: str = None
    organism: Optional[str] = None
    organism_id: Optional[int] = None
    pdb_entries: Optional[Union[str, list[str]]] = empty_list()
    functional_sites: Optional[Union[dict[Union[str, FunctionalSiteId], Union[dict, FunctionalSite]], list[Union[dict, FunctionalSite]]]] = empty_dict()
    structural_features: Optional[Union[dict[Union[str, StructuralFeatureId], Union[dict, StructuralFeature]], list[Union[dict, StructuralFeature]]]] = empty_dict()
    protein_interactions: Optional[Union[dict[Union[str, ProteinProteinInteractionId], Union[dict, ProteinProteinInteraction]], list[Union[dict, ProteinProteinInteraction]]]] = empty_dict()
    ligand_interactions: Optional[Union[Union[dict, LigandInteraction], list[Union[dict, LigandInteraction]]]] = empty_list()
    mutations: Optional[Union[dict[Union[str, MutationEffectId], Union[dict, MutationEffect]], list[Union[dict, MutationEffect]]]] = empty_dict()
    ptms: Optional[Union[dict[Union[str, PostTranslationalModificationId], Union[dict, PostTranslationalModification]], list[Union[dict, PostTranslationalModification]]]] = empty_dict()
    biophysical_properties: Optional[Union[Union[dict, BiophysicalProperty], list[Union[dict, BiophysicalProperty]]]] = empty_list()
    conformational_ensemble: Optional[Union[dict, ConformationalEnsemble]] = None
    evolutionary_conservation: Optional[Union[dict, EvolutionaryConservation]] = None
    cross_references: Optional[Union[Union[dict, DatabaseCrossReference], list[Union[dict, DatabaseCrossReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AggregatedProteinViewId):
            self.id = AggregatedProteinViewId(self.id)

        if self._is_empty(self.uniprot_id):
            self.MissingRequiredField("uniprot_id")
        if not isinstance(self.uniprot_id, str):
            self.uniprot_id = str(self.uniprot_id)

        if self._is_empty(self.protein_name):
            self.MissingRequiredField("protein_name")
        if not isinstance(self.protein_name, str):
            self.protein_name = str(self.protein_name)

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        if self.organism_id is not None and not isinstance(self.organism_id, int):
            self.organism_id = int(self.organism_id)

        if not isinstance(self.pdb_entries, list):
            self.pdb_entries = [self.pdb_entries] if self.pdb_entries is not None else []
        self.pdb_entries = [v if isinstance(v, str) else str(v) for v in self.pdb_entries]

        self._normalize_inlined_as_list(slot_name="functional_sites", slot_type=FunctionalSite, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="structural_features", slot_type=StructuralFeature, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="protein_interactions", slot_type=ProteinProteinInteraction, key_name="id", keyed=True)

        if not isinstance(self.ligand_interactions, list):
            self.ligand_interactions = [self.ligand_interactions] if self.ligand_interactions is not None else []
        self.ligand_interactions = [v if isinstance(v, LigandInteraction) else LigandInteraction(**as_dict(v)) for v in self.ligand_interactions]

        self._normalize_inlined_as_list(slot_name="mutations", slot_type=MutationEffect, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ptms", slot_type=PostTranslationalModification, key_name="id", keyed=True)

        if not isinstance(self.biophysical_properties, list):
            self.biophysical_properties = [self.biophysical_properties] if self.biophysical_properties is not None else []
        self.biophysical_properties = [v if isinstance(v, BiophysicalProperty) else BiophysicalProperty(**as_dict(v)) for v in self.biophysical_properties]

        if self.conformational_ensemble is not None and not isinstance(self.conformational_ensemble, ConformationalEnsemble):
            self.conformational_ensemble = ConformationalEnsemble(**as_dict(self.conformational_ensemble))

        if self.evolutionary_conservation is not None and not isinstance(self.evolutionary_conservation, EvolutionaryConservation):
            self.evolutionary_conservation = EvolutionaryConservation(**as_dict(self.evolutionary_conservation))

        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references] if self.cross_references is not None else []
        self.cross_references = [v if isinstance(v, DatabaseCrossReference) else DatabaseCrossReference(**as_dict(v)) for v in self.cross_references]

        super().__post_init__(**kwargs)


# Enumerations
class FacilityEnum(EnumDefinitionImpl):
    """
    Major synchrotron and structural biology research facilities worldwide
    """
    NSLS_II = PermissibleValue(
        text="NSLS_II",
        title="National Synchrotron Light Source II",
        description="Fourth-generation synchrotron light source at Brookhaven National Laboratory, Upton, NY, USA",
        meaning=ROR["01q47ea17"])
    ALS = PermissibleValue(
        text="ALS",
        title="Advanced Light Source",
        description="""Third-generation synchrotron light source at Lawrence Berkeley National Laboratory, Berkeley, CA, USA""")
    SSRL = PermissibleValue(
        text="SSRL",
        title="Stanford Synchrotron Radiation Lightsource",
        description="Synchrotron radiation facility at SLAC National Accelerator Laboratory, Menlo Park, CA, USA")
    ESRF = PermissibleValue(
        text="ESRF",
        title="European Synchrotron Radiation Facility",
        description="High-energy synchrotron facility in Grenoble, France - world's most intense X-ray source",
        meaning=ROR["02550n020"])
    DIAMOND = PermissibleValue(
        text="DIAMOND",
        title="Diamond Light Source",
        description="""UK's national synchrotron science facility at Harwell Science and Innovation Campus, Oxfordshire, UK""",
        meaning=ROR["05etxs293"])
    PHOTON_FACTORY = PermissibleValue(
        text="PHOTON_FACTORY",
        title="Photon Factory",
        description="""Synchrotron radiation facility at KEK (High Energy Accelerator Research Organization), Tsukuba, Japan""")
    APS = PermissibleValue(
        text="APS",
        title="Advanced Photon Source",
        description="High-energy synchrotron at Argonne National Laboratory, Lemont, IL, USA")
    SPRING8 = PermissibleValue(
        text="SPRING8",
        title="SPring-8",
        description="Large-scale synchrotron radiation facility in Harima Science Park City, Hyogo, Japan")
    PETRA_III = PermissibleValue(
        text="PETRA_III",
        title="PETRA III",
        description="High-brilliance synchrotron radiation source at DESY, Hamburg, Germany")
    SOLEIL = PermissibleValue(
        text="SOLEIL",
        title="Synchrotron SOLEIL",
        description="French national synchrotron facility near Paris, France",
        meaning=ROR["01ydb3330"])
    AUSTRALIAN_SYNCHROTRON = PermissibleValue(
        text="AUSTRALIAN_SYNCHROTRON",
        title="Australian Synchrotron",
        description="Australia's national synchrotron facility in Melbourne, Victoria",
        meaning=ROR["03vk18a84"])
    SIBYLS = PermissibleValue(
        text="SIBYLS",
        title="SIBYLS Beamline 12.3.1",
        description="""Integrated structural biology beamline at ALS for SAXS, X-ray crystallography, and fiber diffraction""")

    _defn = EnumDefinition(
        name="FacilityEnum",
        description="Major synchrotron and structural biology research facilities worldwide",
    )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological samples
    """
    protein = PermissibleValue(
        text="protein",
        description="Protein sample")
    nucleic_acid = PermissibleValue(
        text="nucleic_acid",
        description="Nucleic acid sample (DNA or RNA)")
    complex = PermissibleValue(
        text="complex",
        description="Protein-protein or protein-nucleic acid complex")
    membrane_protein = PermissibleValue(
        text="membrane_protein",
        description="Membrane protein sample")
    virus = PermissibleValue(
        text="virus",
        description="Viral particle")
    organelle = PermissibleValue(
        text="organelle",
        description="Cellular organelle")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological samples",
    )

class ConcentrationUnitEnum(EnumDefinitionImpl):
    """
    Units for concentration measurement
    """
    mg_per_ml = PermissibleValue(
        text="mg_per_ml",
        description="Milligrams per milliliter")
    micromolar = PermissibleValue(
        text="micromolar",
        description="Micromolar")
    millimolar = PermissibleValue(
        text="millimolar",
        description="Millimolar")
    nanomolar = PermissibleValue(
        text="nanomolar",
        description="Nanomolar")

    _defn = EnumDefinition(
        name="ConcentrationUnitEnum",
        description="Units for concentration measurement",
    )

class TemperatureUnitEnum(EnumDefinitionImpl):
    """
    Units for temperature measurement
    """
    celsius = PermissibleValue(
        text="celsius",
        description="Degrees Celsius")
    kelvin = PermissibleValue(
        text="kelvin",
        description="Kelvin")
    fahrenheit = PermissibleValue(
        text="fahrenheit",
        description="Degrees Fahrenheit")

    _defn = EnumDefinition(
        name="TemperatureUnitEnum",
        description="Units for temperature measurement",
    )

class PreparationTypeEnum(EnumDefinitionImpl):
    """
    Types of sample preparation
    """
    cryo_em = PermissibleValue(
        text="cryo_em",
        description="Cryo-EM preparation")
    xray_crystallography = PermissibleValue(
        text="xray_crystallography",
        description="X-ray crystallography preparation")
    saxs = PermissibleValue(
        text="saxs",
        description="SAXS/WAXS preparation")
    sans = PermissibleValue(
        text="sans",
        description="SANS preparation")
    protein_expression = PermissibleValue(
        text="protein_expression",
        description="Protein expression in host cells")
    protein_purification = PermissibleValue(
        text="protein_purification",
        description="Protein purification")
    negative_stain = PermissibleValue(
        text="negative_stain",
        description="Negative stain EM preparation")

    _defn = EnumDefinition(
        name="PreparationTypeEnum",
        description="Types of sample preparation",
    )

class GridTypeEnum(EnumDefinitionImpl):
    """
    Types of EM grids
    """
    c_flat = PermissibleValue(
        text="c_flat",
        description="C-flat holey carbon grid")
    quantifoil = PermissibleValue(
        text="quantifoil",
        description="Quantifoil holey carbon grid")
    lacey_carbon = PermissibleValue(
        text="lacey_carbon",
        description="Lacey carbon grid")
    ultrathin_carbon = PermissibleValue(
        text="ultrathin_carbon",
        description="Ultrathin carbon film")
    gold = PermissibleValue(
        text="gold",
        description="Gold grid")

    _defn = EnumDefinition(
        name="GridTypeEnum",
        description="Types of EM grids",
    )

class VitrificationMethodEnum(EnumDefinitionImpl):
    """
    Methods for vitrification
    """
    plunge_freezing = PermissibleValue(
        text="plunge_freezing",
        description="Plunge freezing in liquid ethane")
    high_pressure_freezing = PermissibleValue(
        text="high_pressure_freezing",
        description="High pressure freezing")
    slam_freezing = PermissibleValue(
        text="slam_freezing",
        description="Slam freezing")

    _defn = EnumDefinition(
        name="VitrificationMethodEnum",
        description="Methods for vitrification",
    )

class CrystallizationMethodEnum(EnumDefinitionImpl):
    """
    Methods for protein crystallization
    """
    vapor_diffusion_hanging = PermissibleValue(
        text="vapor_diffusion_hanging",
        description="Vapor diffusion hanging drop")
    vapor_diffusion_sitting = PermissibleValue(
        text="vapor_diffusion_sitting",
        description="Vapor diffusion sitting drop")
    batch = PermissibleValue(
        text="batch",
        description="Batch crystallization")
    microbatch = PermissibleValue(
        text="microbatch",
        description="Microbatch under oil")
    lcp = PermissibleValue(
        text="lcp",
        description="Lipidic cubic phase (LCP)")
    dialysis = PermissibleValue(
        text="dialysis",
        description="Dialysis method")
    free_interface_diffusion = PermissibleValue(
        text="free_interface_diffusion",
        description="Free interface diffusion")

    _defn = EnumDefinition(
        name="CrystallizationMethodEnum",
        description="Methods for protein crystallization",
    )

class InstrumentStatusEnum(EnumDefinitionImpl):
    """
    Operational status of instruments
    """
    operational = PermissibleValue(
        text="operational",
        description="Instrument is operational")
    maintenance = PermissibleValue(
        text="maintenance",
        description="Instrument under maintenance")
    offline = PermissibleValue(
        text="offline",
        description="Instrument is offline")
    commissioning = PermissibleValue(
        text="commissioning",
        description="Instrument being commissioned")

    _defn = EnumDefinition(
        name="InstrumentStatusEnum",
        description="Operational status of instruments",
    )

class DetectorTypeEnum(EnumDefinitionImpl):
    """
    DEPRECATED: Use DetectorTechnologyEnum instead. Legacy enum mixing technologies and brands.
    """
    direct_electron = PermissibleValue(
        text="direct_electron",
        description="Direct electron detector")
    ccd = PermissibleValue(
        text="ccd",
        description="CCD camera")
    cmos = PermissibleValue(
        text="cmos",
        description="CMOS detector")
    hybrid_pixel = PermissibleValue(
        text="hybrid_pixel",
        description="Hybrid pixel detector")
    eiger = PermissibleValue(
        text="eiger",
        description="Dectris EIGER detector (hybrid photon counting)")
    pilatus = PermissibleValue(
        text="pilatus",
        description="Dectris PILATUS detector")
    rayonix = PermissibleValue(
        text="rayonix",
        description="Rayonix CCD detector")
    adsc = PermissibleValue(
        text="adsc",
        description="ADSC CCD detector")
    mar = PermissibleValue(
        text="mar",
        description="MAR CCD or imaging plate detector")

    _defn = EnumDefinition(
        name="DetectorTypeEnum",
        description="DEPRECATED: Use DetectorTechnologyEnum instead. Legacy enum mixing technologies and brands.",
    )

class DetectorTechnologyEnum(EnumDefinitionImpl):
    """
    Generic detector technologies for structural biology imaging
    """
    direct_electron_detector = PermissibleValue(
        text="direct_electron_detector",
        description="""Direct electron detector for cryo-EM (e.g., Gatan K2/K3, ThermoFisher Falcon, DirectElectron DE-64)""")
    ccd = PermissibleValue(
        text="ccd",
        description="Charge-coupled device camera")
    cmos = PermissibleValue(
        text="cmos",
        description="Complementary metal-oxide-semiconductor detector")
    hybrid_photon_counting = PermissibleValue(
        text="hybrid_photon_counting",
        description="Hybrid pixel photon counting detector for X-ray crystallography")
    scintillator_coupled = PermissibleValue(
        text="scintillator_coupled",
        description="Scintillator-coupled indirect detection")
    imaging_plate = PermissibleValue(
        text="imaging_plate",
        description="Imaging plate detector")
    film = PermissibleValue(
        text="film",
        description="Photographic film")

    _defn = EnumDefinition(
        name="DetectorTechnologyEnum",
        description="Generic detector technologies for structural biology imaging",
    )

class DetectorModeEnum(EnumDefinitionImpl):
    """
    Operating modes for detectors during data collection
    """
    counting = PermissibleValue(
        text="counting",
        description="Electron/photon counting mode")
    integrating = PermissibleValue(
        text="integrating",
        description="Integrating mode (analog)")
    super_resolution = PermissibleValue(
        text="super_resolution",
        description="Super-resolution mode with oversampling")
    linear = PermissibleValue(
        text="linear",
        description="Linear response mode")
    correlated_double_sampling = PermissibleValue(
        text="correlated_double_sampling",
        description="Correlated double sampling mode")

    _defn = EnumDefinition(
        name="DetectorModeEnum",
        description="Operating modes for detectors during data collection",
    )

class XRaySourceTypeEnum(EnumDefinitionImpl):
    """
    Types of X-ray sources
    """
    synchrotron = PermissibleValue(
        text="synchrotron",
        description="Synchrotron radiation source")
    rotating_anode = PermissibleValue(
        text="rotating_anode",
        description="Rotating anode generator")
    microfocus = PermissibleValue(
        text="microfocus",
        description="Microfocus sealed tube")
    metal_jet = PermissibleValue(
        text="metal_jet",
        description="Liquid metal jet source")

    _defn = EnumDefinition(
        name="XRaySourceTypeEnum",
        description="Types of X-ray sources",
    )

class TechniqueEnum(EnumDefinitionImpl):
    """
    Structural biology techniques
    """
    cryo_em = PermissibleValue(
        text="cryo_em",
        description="Cryo-electron microscopy")
    xray_crystallography = PermissibleValue(
        text="xray_crystallography",
        description="X-ray crystallography")
    saxs = PermissibleValue(
        text="saxs",
        description="Small-angle X-ray scattering")
    waxs = PermissibleValue(
        text="waxs",
        description="Wide-angle X-ray scattering")
    sans = PermissibleValue(
        text="sans",
        description="Small-angle neutron scattering")
    cryo_et = PermissibleValue(
        text="cryo_et",
        description="Cryo-electron tomography")
    electron_microscopy = PermissibleValue(
        text="electron_microscopy",
        description="General electron microscopy")
    mass_spectrometry = PermissibleValue(
        text="mass_spectrometry",
        description="Mass spectrometry")

    _defn = EnumDefinition(
        name="TechniqueEnum",
        description="Structural biology techniques",
    )

class ProcessingStatusEnum(EnumDefinitionImpl):
    """
    Processing status
    """
    raw = PermissibleValue(
        text="raw",
        description="Raw data")
    preprocessing = PermissibleValue(
        text="preprocessing",
        description="Being preprocessed")
    processing = PermissibleValue(
        text="processing",
        description="Being processed")
    completed = PermissibleValue(
        text="completed",
        description="Processing completed")
    failed = PermissibleValue(
        text="failed",
        description="Processing failed")

    _defn = EnumDefinition(
        name="ProcessingStatusEnum",
        description="Processing status",
    )

class WorkflowTypeEnum(EnumDefinitionImpl):
    """
    Types of processing workflows
    """
    motion_correction = PermissibleValue(
        text="motion_correction",
        description="Motion correction for cryo-EM")
    ctf_estimation = PermissibleValue(
        text="ctf_estimation",
        description="CTF estimation")
    particle_picking = PermissibleValue(
        text="particle_picking",
        description="Particle picking")
    classification_2d = PermissibleValue(
        text="classification_2d",
        description="2D classification")
    classification_3d = PermissibleValue(
        text="classification_3d",
        description="3D classification")
    refinement = PermissibleValue(
        text="refinement",
        description="3D refinement")
    model_building = PermissibleValue(
        text="model_building",
        description="Atomic model building")
    phasing = PermissibleValue(
        text="phasing",
        description="Phase determination")
    integration = PermissibleValue(
        text="integration",
        description="Data integration")
    scaling = PermissibleValue(
        text="scaling",
        description="Data scaling")
    saxs_analysis = PermissibleValue(
        text="saxs_analysis",
        description="SAXS data analysis")
    em_2d_classification = PermissibleValue(
        text="em_2d_classification",
        description="EM 2D classification")
    mass_spec_deconvolution = PermissibleValue(
        text="mass_spec_deconvolution",
        description="Mass spectrometry deconvolution")

    _defn = EnumDefinition(
        name="WorkflowTypeEnum",
        description="Types of processing workflows",
    )

class FileFormatEnum(EnumDefinitionImpl):
    """
    File formats
    """
    mrc = PermissibleValue(
        text="mrc",
        description="MRC format for EM data")
    tiff = PermissibleValue(
        text="tiff",
        description="TIFF image format")
    hdf5 = PermissibleValue(
        text="hdf5",
        description="HDF5 hierarchical data format")
    star = PermissibleValue(
        text="star",
        description="STAR format for metadata")
    pdb = PermissibleValue(
        text="pdb",
        description="PDB coordinate format")
    mmcif = PermissibleValue(
        text="mmcif",
        description="mmCIF format")
    mtz = PermissibleValue(
        text="mtz",
        description="MTZ reflection format")
    cbf = PermissibleValue(
        text="cbf",
        description="Crystallographic Binary Format")
    cbf_zst = PermissibleValue(
        text="cbf_zst",
        description="Zstandard-compressed CBF format")
    img = PermissibleValue(
        text="img",
        description="Generic diffraction image format")
    h5 = PermissibleValue(
        text="h5",
        description="HDF5 format (alternative extension)")
    ascii = PermissibleValue(
        text="ascii",
        description="ASCII text format")
    thermo_raw = PermissibleValue(
        text="thermo_raw",
        description="Thermo Fisher RAW format")
    zip = PermissibleValue(
        text="zip",
        description="ZIP compressed archive")
    gz = PermissibleValue(
        text="gz",
        description="Gzip compressed format")

    _defn = EnumDefinition(
        name="FileFormatEnum",
        description="File formats",
    )

class DataTypeEnum(EnumDefinitionImpl):
    """
    Types of data
    """
    micrograph = PermissibleValue(
        text="micrograph",
        description="Electron micrograph")
    diffraction = PermissibleValue(
        text="diffraction",
        description="Diffraction pattern")
    scattering = PermissibleValue(
        text="scattering",
        description="Scattering data")
    particles = PermissibleValue(
        text="particles",
        description="Particle stack")
    volume = PermissibleValue(
        text="volume",
        description="3D volume")
    model = PermissibleValue(
        text="model",
        description="Atomic model")
    metadata = PermissibleValue(
        text="metadata",
        description="Metadata file")
    raw_data = PermissibleValue(
        text="raw_data",
        description="Raw experimental data")
    processed_data = PermissibleValue(
        text="processed_data",
        description="Processed data")

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Types of data",
    )

class CollectionModeEnum(EnumDefinitionImpl):
    """
    Data collection modes
    """
    counting = PermissibleValue(
        text="counting",
        description="Counting mode")
    super_resolution = PermissibleValue(
        text="super_resolution",
        description="Super-resolution mode")
    continuous = PermissibleValue(
        text="continuous",
        description="Continuous collection")
    oscillation = PermissibleValue(
        text="oscillation",
        description="Oscillation method")
    still = PermissibleValue(
        text="still",
        description="Still images")
    batch = PermissibleValue(
        text="batch",
        description="Batch mode collection")
    sec_saxs = PermissibleValue(
        text="sec_saxs",
        description="SEC-SAXS collection mode")
    single_particle = PermissibleValue(
        text="single_particle",
        description="Single particle analysis mode")

    _defn = EnumDefinition(
        name="CollectionModeEnum",
        description="Data collection modes",
    )

class IlluminationTypeEnum(EnumDefinitionImpl):
    """
    Types of illumination for optical microscopy
    """
    brightfield = PermissibleValue(
        text="brightfield",
        description="Brightfield illumination")
    darkfield = PermissibleValue(
        text="darkfield",
        description="Darkfield illumination")
    phase_contrast = PermissibleValue(
        text="phase_contrast",
        description="Phase contrast microscopy")
    dic = PermissibleValue(
        text="dic",
        description="Differential interference contrast (DIC/Nomarski)")
    fluorescence = PermissibleValue(
        text="fluorescence",
        description="Fluorescence illumination")
    confocal = PermissibleValue(
        text="confocal",
        description="Confocal laser scanning")
    polarized = PermissibleValue(
        text="polarized",
        description="Polarized light microscopy")
    oblique = PermissibleValue(
        text="oblique",
        description="Oblique illumination")

    _defn = EnumDefinition(
        name="IlluminationTypeEnum",
        description="Types of illumination for optical microscopy",
    )

class ExpressionSystemEnum(EnumDefinitionImpl):
    """
    Expression systems for recombinant protein production
    """
    bacteria = PermissibleValue(
        text="bacteria",
        description="Bacterial expression (e.g., E. coli)")
    yeast = PermissibleValue(
        text="yeast",
        description="Yeast expression (e.g., S. cerevisiae, P. pastoris)")
    insect = PermissibleValue(
        text="insect",
        description="Insect cell expression (e.g., Sf9, High Five)")
    mammalian = PermissibleValue(
        text="mammalian",
        description="Mammalian cell expression (e.g., HEK293, CHO)")
    cell_free = PermissibleValue(
        text="cell_free",
        description="Cell-free expression system")

    _defn = EnumDefinition(
        name="ExpressionSystemEnum",
        description="Expression systems for recombinant protein production",
    )

class PurificationStepEnum(EnumDefinitionImpl):
    """
    Protein purification steps and methods
    """
    affinity_ni_nta = PermissibleValue(
        text="affinity_ni_nta",
        description="Affinity chromatography using Ni-NTA resin")
    affinity_co_nta = PermissibleValue(
        text="affinity_co_nta",
        description="Affinity chromatography using Co-NTA resin")
    affinity_strep = PermissibleValue(
        text="affinity_strep",
        description="Affinity chromatography using Strep-tag")
    affinity_mbp = PermissibleValue(
        text="affinity_mbp",
        description="Affinity chromatography using maltose-binding protein (MBP)")
    affinity_gst = PermissibleValue(
        text="affinity_gst",
        description="Affinity chromatography using glutathione S-transferase (GST)")
    tag_cleavage = PermissibleValue(
        text="tag_cleavage",
        description="Proteolytic cleavage of purification tags")
    ion_exchange = PermissibleValue(
        text="ion_exchange",
        description="Ion-exchange chromatography (IEX)")
    hydrophobic_interaction = PermissibleValue(
        text="hydrophobic_interaction",
        description="Hydrophobic interaction chromatography (HIC)")
    size_exclusion = PermissibleValue(
        text="size_exclusion",
        description="Size-exclusion chromatography (SEC)")
    dialysis = PermissibleValue(
        text="dialysis",
        description="Dialysis or buffer exchange")

    _defn = EnumDefinition(
        name="PurificationStepEnum",
        description="Protein purification steps and methods",
    )

class PhasingMethodEnum(EnumDefinitionImpl):
    """
    Methods for phase determination in X-ray crystallography
    """
    molecular_replacement = PermissibleValue(
        text="molecular_replacement",
        description="Molecular replacement (MR)")
    sad = PermissibleValue(
        text="sad",
        description="Single-wavelength anomalous diffraction (SAD)")
    mad = PermissibleValue(
        text="mad",
        description="Multi-wavelength anomalous diffraction (MAD)")
    sir = PermissibleValue(
        text="sir",
        description="Single isomorphous replacement (SIR)")
    mir = PermissibleValue(
        text="mir",
        description="Multiple isomorphous replacement (MIR)")
    siras = PermissibleValue(
        text="siras",
        description="Single isomorphous replacement with anomalous scattering (SIRAS)")
    miras = PermissibleValue(
        text="miras",
        description="Multiple isomorphous replacement with anomalous scattering (MIRAS)")
    fragile_mr = PermissibleValue(
        text="fragile_mr",
        description="Fragile molecular replacement or ensemble-based MR")

    _defn = EnumDefinition(
        name="PhasingMethodEnum",
        description="Methods for phase determination in X-ray crystallography",
    )

class ExperimentalMethodEnum(EnumDefinitionImpl):
    """
    Experimental methods for structure determination
    """
    x_ray_diffraction = PermissibleValue(
        text="x_ray_diffraction",
        description="X-ray diffraction")
    neutron_diffraction = PermissibleValue(
        text="neutron_diffraction",
        description="Neutron diffraction")
    electron_diffraction = PermissibleValue(
        text="electron_diffraction",
        description="Electron diffraction (e.g., microED)")
    fiber_diffraction = PermissibleValue(
        text="fiber_diffraction",
        description="Fiber diffraction")

    _defn = EnumDefinition(
        name="ExperimentalMethodEnum",
        description="Experimental methods for structure determination",
    )

class FunctionalSiteTypeEnum(EnumDefinitionImpl):
    """
    Types of functional sites in proteins
    """
    active_site = PermissibleValue(
        text="active_site",
        description="Enzyme active site")
    catalytic_site = PermissibleValue(
        text="catalytic_site",
        description="Catalytic residues")
    binding_site = PermissibleValue(
        text="binding_site",
        description="General binding site")
    allosteric_site = PermissibleValue(
        text="allosteric_site",
        description="Allosteric regulation site")
    substrate_binding = PermissibleValue(
        text="substrate_binding",
        description="Substrate binding site")
    cofactor_binding = PermissibleValue(
        text="cofactor_binding",
        description="Cofactor binding site")
    inhibitor_binding = PermissibleValue(
        text="inhibitor_binding",
        description="Inhibitor binding site")
    metal_binding = PermissibleValue(
        text="metal_binding",
        description="Metal ion binding site")
    nucleotide_binding = PermissibleValue(
        text="nucleotide_binding",
        description="Nucleotide binding site")
    phosphorylation_site = PermissibleValue(
        text="phosphorylation_site",
        description="Phosphorylation site")
    glycosylation_site = PermissibleValue(
        text="glycosylation_site",
        description="Glycosylation site")
    ubiquitination_site = PermissibleValue(
        text="ubiquitination_site",
        description="Ubiquitination site")
    sumoylation_site = PermissibleValue(
        text="sumoylation_site",
        description="SUMOylation site")
    acetylation_site = PermissibleValue(
        text="acetylation_site",
        description="Acetylation site")
    methylation_site = PermissibleValue(
        text="methylation_site",
        description="Methylation site")
    protein_binding = PermissibleValue(
        text="protein_binding",
        description="Protein-protein interaction site")
    dna_binding = PermissibleValue(
        text="dna_binding",
        description="DNA binding site")
    rna_binding = PermissibleValue(
        text="rna_binding",
        description="RNA binding site")
    lipid_binding = PermissibleValue(
        text="lipid_binding",
        description="Lipid binding site")

    _defn = EnumDefinition(
        name="FunctionalSiteTypeEnum",
        description="Types of functional sites in proteins",
    )

class StructuralFeatureTypeEnum(EnumDefinitionImpl):
    """
    Types of structural features
    """
    alpha_helix = PermissibleValue(
        text="alpha_helix",
        description="Alpha helix")
    beta_sheet = PermissibleValue(
        text="beta_sheet",
        description="Beta sheet")
    beta_strand = PermissibleValue(
        text="beta_strand",
        description="Beta strand")
    turn = PermissibleValue(
        text="turn",
        description="Turn structure")
    coil = PermissibleValue(
        text="coil",
        description="Random coil")
    disordered_region = PermissibleValue(
        text="disordered_region",
        description="Intrinsically disordered region")
    transmembrane_helix = PermissibleValue(
        text="transmembrane_helix",
        description="Transmembrane helix")
    signal_peptide = PermissibleValue(
        text="signal_peptide",
        description="Signal peptide")
    transit_peptide = PermissibleValue(
        text="transit_peptide",
        description="Transit peptide")
    domain = PermissibleValue(
        text="domain",
        description="Protein domain")
    repeat = PermissibleValue(
        text="repeat",
        description="Sequence repeat")
    zinc_finger = PermissibleValue(
        text="zinc_finger",
        description="Zinc finger motif")
    zinc_binding = PermissibleValue(
        text="zinc_binding",
        description="Zinc binding site")
    coiled_coil = PermissibleValue(
        text="coiled_coil",
        description="Coiled coil")
    motif = PermissibleValue(
        text="motif",
        description="Structural motif")
    cavity = PermissibleValue(
        text="cavity",
        description="Structural cavity")
    channel = PermissibleValue(
        text="channel",
        description="Molecular channel")
    pore = PermissibleValue(
        text="pore",
        description="Molecular pore")
    hinge = PermissibleValue(
        text="hinge",
        description="Hinge region")
    linker = PermissibleValue(
        text="linker",
        description="Linker region")

    _defn = EnumDefinition(
        name="StructuralFeatureTypeEnum",
        description="Types of structural features",
    )

class SecondaryStructureEnum(EnumDefinitionImpl):
    """
    Secondary structure types
    """
    helix = PermissibleValue(
        text="helix",
        description="Helix structure")
    sheet = PermissibleValue(
        text="sheet",
        description="Beta sheet")
    turn = PermissibleValue(
        text="turn",
        description="Turn")
    coil = PermissibleValue(
        text="coil",
        description="Random coil")
    helix_310 = PermissibleValue(
        text="helix_310",
        description="3-10 helix")
    helix_pi = PermissibleValue(
        text="helix_pi",
        description="Pi helix")
    bend = PermissibleValue(
        text="bend",
        description="Bend")
    bridge = PermissibleValue(
        text="bridge",
        description="Beta bridge")

    _defn = EnumDefinition(
        name="SecondaryStructureEnum",
        description="Secondary structure types",
    )

class ConformationalStateEnum(EnumDefinitionImpl):
    """
    Conformational states
    """
    open = PermissibleValue(
        text="open",
        description="Open conformation")
    closed = PermissibleValue(
        text="closed",
        description="Closed conformation")
    intermediate = PermissibleValue(
        text="intermediate",
        description="Intermediate state")
    active = PermissibleValue(
        text="active",
        description="Active conformation")
    inactive = PermissibleValue(
        text="inactive",
        description="Inactive conformation")
    apo = PermissibleValue(
        text="apo",
        description="Apo form")
    holo = PermissibleValue(
        text="holo",
        description="Holo form")
    substrate_bound = PermissibleValue(
        text="substrate_bound",
        description="Substrate-bound")
    product_bound = PermissibleValue(
        text="product_bound",
        description="Product-bound")
    inhibitor_bound = PermissibleValue(
        text="inhibitor_bound",
        description="Inhibitor-bound")
    partially_open = PermissibleValue(
        text="partially_open",
        description="Partially open")
    partially_closed = PermissibleValue(
        text="partially_closed",
        description="Partially closed")
    disordered = PermissibleValue(
        text="disordered",
        description="Disordered state")

    _defn = EnumDefinition(
        name="ConformationalStateEnum",
        description="Conformational states",
    )

class InteractionTypeEnum(EnumDefinitionImpl):
    """
    Types of molecular interactions
    """
    covalent = PermissibleValue(
        text="covalent",
        description="Covalent bond")
    hydrogen_bond = PermissibleValue(
        text="hydrogen_bond",
        description="Hydrogen bond")
    ionic = PermissibleValue(
        text="ionic",
        description="Ionic interaction")
    van_der_waals = PermissibleValue(
        text="van_der_waals",
        description="Van der Waals interaction")
    hydrophobic = PermissibleValue(
        text="hydrophobic",
        description="Hydrophobic interaction")
    aromatic = PermissibleValue(
        text="aromatic",
        description="Aromatic interaction")
    pi_stacking = PermissibleValue(
        text="pi_stacking",
        description="Pi-pi stacking")
    cation_pi = PermissibleValue(
        text="cation_pi",
        description="Cation-pi interaction")
    metal_coordination = PermissibleValue(
        text="metal_coordination",
        description="Metal coordination")
    disulfide = PermissibleValue(
        text="disulfide",
        description="Disulfide bond")

    _defn = EnumDefinition(
        name="InteractionTypeEnum",
        description="Types of molecular interactions",
    )

class BindingAffinityTypeEnum(EnumDefinitionImpl):
    """
    Types of binding affinity measurements
    """
    kd = PermissibleValue(
        text="kd",
        description="Dissociation constant")
    ki = PermissibleValue(
        text="ki",
        description="Inhibition constant")
    ic50 = PermissibleValue(
        text="ic50",
        description="Half maximal inhibitory concentration")
    ec50 = PermissibleValue(
        text="ec50",
        description="Half maximal effective concentration")
    ka = PermissibleValue(
        text="ka",
        description="Association constant")
    km = PermissibleValue(
        text="km",
        description="Michaelis constant")

    _defn = EnumDefinition(
        name="BindingAffinityTypeEnum",
        description="Types of binding affinity measurements",
    )

class AffinityUnitEnum(EnumDefinitionImpl):
    """
    Units for affinity measurements
    """
    molar = PermissibleValue(
        text="molar",
        description="Molar (M)")
    millimolar = PermissibleValue(
        text="millimolar",
        description="Millimolar (mM)")
    micromolar = PermissibleValue(
        text="micromolar",
        description="Micromolar (µM)")
    nanomolar = PermissibleValue(
        text="nanomolar",
        description="Nanomolar (nM)")
    picomolar = PermissibleValue(
        text="picomolar",
        description="Picomolar (pM)")

    _defn = EnumDefinition(
        name="AffinityUnitEnum",
        description="Units for affinity measurements",
    )

class ComplexStabilityEnum(EnumDefinitionImpl):
    """
    Stability of protein complexes
    """
    stable = PermissibleValue(
        text="stable",
        description="Stable complex")
    transient = PermissibleValue(
        text="transient",
        description="Transient interaction")
    weak = PermissibleValue(
        text="weak",
        description="Weak interaction")
    strong = PermissibleValue(
        text="strong",
        description="Strong interaction")
    obligate = PermissibleValue(
        text="obligate",
        description="Obligate complex")
    non_obligate = PermissibleValue(
        text="non_obligate",
        description="Non-obligate complex")

    _defn = EnumDefinition(
        name="ComplexStabilityEnum",
        description="Stability of protein complexes",
    )

class InteractionEvidenceEnum(EnumDefinitionImpl):
    """
    Evidence for interactions
    """
    experimental = PermissibleValue(
        text="experimental",
        description="Experimental evidence")
    predicted = PermissibleValue(
        text="predicted",
        description="Computational prediction")
    homology = PermissibleValue(
        text="homology",
        description="Homology-based")
    coexpression = PermissibleValue(
        text="coexpression",
        description="Co-expression data")
    colocalization = PermissibleValue(
        text="colocalization",
        description="Co-localization")
    genetic = PermissibleValue(
        text="genetic",
        description="Genetic evidence")
    physical = PermissibleValue(
        text="physical",
        description="Physical interaction")
    functional = PermissibleValue(
        text="functional",
        description="Functional association")

    _defn = EnumDefinition(
        name="InteractionEvidenceEnum",
        description="Evidence for interactions",
    )

class MutationTypeEnum(EnumDefinitionImpl):
    """
    Types of mutations
    """
    missense = PermissibleValue(
        text="missense",
        description="Missense mutation")
    nonsense = PermissibleValue(
        text="nonsense",
        description="Nonsense mutation")
    frameshift = PermissibleValue(
        text="frameshift",
        description="Frameshift mutation")
    deletion = PermissibleValue(
        text="deletion",
        description="Deletion")
    insertion = PermissibleValue(
        text="insertion",
        description="Insertion")
    duplication = PermissibleValue(
        text="duplication",
        description="Duplication")
    substitution = PermissibleValue(
        text="substitution",
        description="Substitution")

    _defn = EnumDefinition(
        name="MutationTypeEnum",
        description="Types of mutations",
    )

class StabilityEffectEnum(EnumDefinitionImpl):
    """
    Effect on protein stability
    """
    stabilizing = PermissibleValue(
        text="stabilizing",
        description="Increases stability")
    destabilizing = PermissibleValue(
        text="destabilizing",
        description="Decreases stability")
    neutral = PermissibleValue(
        text="neutral",
        description="No significant effect")
    highly_stabilizing = PermissibleValue(
        text="highly_stabilizing",
        description="Strongly increases stability")
    highly_destabilizing = PermissibleValue(
        text="highly_destabilizing",
        description="Strongly decreases stability")

    _defn = EnumDefinition(
        name="StabilityEffectEnum",
        description="Effect on protein stability",
    )

class FunctionalEffectEnum(EnumDefinitionImpl):
    """
    Effect on protein function
    """
    loss_of_function = PermissibleValue(
        text="loss_of_function",
        description="Loss of function")
    gain_of_function = PermissibleValue(
        text="gain_of_function",
        description="Gain of function")
    altered_function = PermissibleValue(
        text="altered_function",
        description="Altered function")
    no_effect = PermissibleValue(
        text="no_effect",
        description="No functional effect")
    partial_loss = PermissibleValue(
        text="partial_loss",
        description="Partial loss of function")
    enhanced_function = PermissibleValue(
        text="enhanced_function",
        description="Enhanced function")

    _defn = EnumDefinition(
        name="FunctionalEffectEnum",
        description="Effect on protein function",
    )

class ClinicalSignificanceEnum(EnumDefinitionImpl):
    """
    Clinical significance of variants
    """
    pathogenic = PermissibleValue(
        text="pathogenic",
        description="Pathogenic")
    likely_pathogenic = PermissibleValue(
        text="likely_pathogenic",
        description="Likely pathogenic")
    benign = PermissibleValue(
        text="benign",
        description="Benign")
    likely_benign = PermissibleValue(
        text="likely_benign",
        description="Likely benign")
    uncertain_significance = PermissibleValue(
        text="uncertain_significance",
        description="Uncertain significance")

    _defn = EnumDefinition(
        name="ClinicalSignificanceEnum",
        description="Clinical significance of variants",
    )

class BiophysicalPropertyEnum(EnumDefinitionImpl):
    """
    Types of biophysical properties
    """
    melting_temperature = PermissibleValue(
        text="melting_temperature",
        description="Melting temperature (Tm)")
    stability = PermissibleValue(
        text="stability",
        description="Thermodynamic stability")
    folding_rate = PermissibleValue(
        text="folding_rate",
        description="Folding rate")
    unfolding_rate = PermissibleValue(
        text="unfolding_rate",
        description="Unfolding rate")
    aggregation_propensity = PermissibleValue(
        text="aggregation_propensity",
        description="Aggregation propensity")
    solubility = PermissibleValue(
        text="solubility",
        description="Solubility")
    hydrophobicity = PermissibleValue(
        text="hydrophobicity",
        description="Hydrophobicity")
    isoelectric_point = PermissibleValue(
        text="isoelectric_point",
        description="Isoelectric point (pI)")
    extinction_coefficient = PermissibleValue(
        text="extinction_coefficient",
        description="Extinction coefficient")
    molecular_weight = PermissibleValue(
        text="molecular_weight",
        description="Molecular weight")
    diffusion_coefficient = PermissibleValue(
        text="diffusion_coefficient",
        description="Diffusion coefficient")
    sedimentation_coefficient = PermissibleValue(
        text="sedimentation_coefficient",
        description="Sedimentation coefficient")
    radius_of_gyration = PermissibleValue(
        text="radius_of_gyration",
        description="Radius of gyration")
    hydrodynamic_radius = PermissibleValue(
        text="hydrodynamic_radius",
        description="Hydrodynamic radius")

    _defn = EnumDefinition(
        name="BiophysicalPropertyEnum",
        description="Types of biophysical properties",
    )

class BiophysicalMethodEnum(EnumDefinitionImpl):
    """
    Methods for biophysical measurements
    """
    differential_scanning_calorimetry = PermissibleValue(
        text="differential_scanning_calorimetry",
        description="DSC")
    isothermal_titration_calorimetry = PermissibleValue(
        text="isothermal_titration_calorimetry",
        description="ITC")
    circular_dichroism = PermissibleValue(
        text="circular_dichroism",
        description="CD spectroscopy")
    fluorescence_spectroscopy = PermissibleValue(
        text="fluorescence_spectroscopy",
        description="Fluorescence")
    surface_plasmon_resonance = PermissibleValue(
        text="surface_plasmon_resonance",
        description="SPR")
    dynamic_light_scattering = PermissibleValue(
        text="dynamic_light_scattering",
        description="DLS")
    analytical_ultracentrifugation = PermissibleValue(
        text="analytical_ultracentrifugation",
        description="AUC")
    nuclear_magnetic_resonance = PermissibleValue(
        text="nuclear_magnetic_resonance",
        description="NMR")
    mass_spectrometry = PermissibleValue(
        text="mass_spectrometry",
        description="MS")

    _defn = EnumDefinition(
        name="BiophysicalMethodEnum",
        description="Methods for biophysical measurements",
    )

class PTMTypeEnum(EnumDefinitionImpl):
    """
    Types of post-translational modifications
    """
    phosphorylation = PermissibleValue(
        text="phosphorylation",
        description="Phosphorylation")
    acetylation = PermissibleValue(
        text="acetylation",
        description="Acetylation")
    methylation = PermissibleValue(
        text="methylation",
        description="Methylation")
    ubiquitination = PermissibleValue(
        text="ubiquitination",
        description="Ubiquitination")
    sumoylation = PermissibleValue(
        text="sumoylation",
        description="SUMOylation")
    glycosylation = PermissibleValue(
        text="glycosylation",
        description="Glycosylation")
    palmitoylation = PermissibleValue(
        text="palmitoylation",
        description="Palmitoylation")
    myristoylation = PermissibleValue(
        text="myristoylation",
        description="Myristoylation")
    prenylation = PermissibleValue(
        text="prenylation",
        description="Prenylation")
    nitrosylation = PermissibleValue(
        text="nitrosylation",
        description="Nitrosylation")
    oxidation = PermissibleValue(
        text="oxidation",
        description="Oxidation")
    hydroxylation = PermissibleValue(
        text="hydroxylation",
        description="Hydroxylation")
    proteolysis = PermissibleValue(
        text="proteolysis",
        description="Proteolytic cleavage")
    deamidation = PermissibleValue(
        text="deamidation",
        description="Deamidation")
    adp_ribosylation = PermissibleValue(
        text="adp_ribosylation",
        description="ADP-ribosylation")

    _defn = EnumDefinition(
        name="PTMTypeEnum",
        description="Types of post-translational modifications",
    )

class EvidenceTypeEnum(EnumDefinitionImpl):
    """
    Types of evidence
    """
    experimental = PermissibleValue(
        text="experimental",
        description="Direct experimental evidence")
    predicted = PermissibleValue(
        text="predicted",
        description="Computational prediction")
    inferred = PermissibleValue(
        text="inferred",
        description="Inferred from homology")
    literature = PermissibleValue(
        text="literature",
        description="Literature curation")
    author_statement = PermissibleValue(
        text="author_statement",
        description="Author statement")
    curator_inference = PermissibleValue(
        text="curator_inference",
        description="Curator inference")

    _defn = EnumDefinition(
        name="EvidenceTypeEnum",
        description="Types of evidence",
    )

class AnnotationSourceEnum(EnumDefinitionImpl):
    """
    Sources of functional annotations
    """
    pdbe = PermissibleValue(
        text="pdbe",
        description="PDBe")
    pdbe_kb = PermissibleValue(
        text="pdbe_kb",
        description="PDBe-KB")
    uniprot = PermissibleValue(
        text="uniprot",
        description="UniProt")
    pfam = PermissibleValue(
        text="pfam",
        description="Pfam")
    cath = PermissibleValue(
        text="cath",
        description="CATH")
    scop = PermissibleValue(
        text="scop",
        description="SCOP")
    interpro = PermissibleValue(
        text="interpro",
        description="InterPro")
    channelsdb = PermissibleValue(
        text="channelsdb",
        description="ChannelsDB")
    dynamine = PermissibleValue(
        text="dynamine",
        description="DynaMine")
    foldx = PermissibleValue(
        text="foldx",
        description="FoldX")
    p2rank = PermissibleValue(
        text="p2rank",
        description="P2rank")
    arpeggio = PermissibleValue(
        text="arpeggio",
        description="Arpeggio")
    covalentizer = PermissibleValue(
        text="covalentizer",
        description="Covalentizer")
    depth = PermissibleValue(
        text="depth",
        description="DEPTH")
    elmpdb = PermissibleValue(
        text="elmpdb",
        description="ELM-PDB")
    frustration = PermissibleValue(
        text="frustration",
        description="Frustration")
    kincore = PermissibleValue(
        text="kincore",
        description="KinCore")
    membranome = PermissibleValue(
        text="membranome",
        description="Membranome")
    missense3d = PermissibleValue(
        text="missense3d",
        description="Missense3D")
    mobi = PermissibleValue(
        text="mobi",
        description="MobiDB")
    nucleos = PermissibleValue(
        text="nucleos",
        description="Nucleos")
    akid = PermissibleValue(
        text="akid",
        description="AKID")
    camkinet = PermissibleValue(
        text="camkinet",
        description="CamKiNet")
    cansar = PermissibleValue(
        text="cansar",
        description="canSAR")
    credo = PermissibleValue(
        text="credo",
        description="CREDO")
    klifs = PermissibleValue(
        text="klifs",
        description="KLIFS")
    m_csm = PermissibleValue(
        text="m_csm",
        description="mCSM")
    moondb = PermissibleValue(
        text="moondb",
        description="MoonDB")
    pocketome = PermissibleValue(
        text="pocketome",
        description="Pocketome")
    propka = PermissibleValue(
        text="propka",
        description="PROPKA")
    proteins_api = PermissibleValue(
        text="proteins_api",
        description="Proteins API")
    validation = PermissibleValue(
        text="validation",
        description="Validation")
    alphafold = PermissibleValue(
        text="alphafold",
        description="AlphaFold")
    modbase = PermissibleValue(
        text="modbase",
        description="ModBase")
    swiss_model = PermissibleValue(
        text="swiss_model",
        description="SWISS-MODEL")
    intact = PermissibleValue(
        text="intact",
        description="IntAct")
    cosmic = PermissibleValue(
        text="cosmic",
        description="COSMIC")
    clinvar = PermissibleValue(
        text="clinvar",
        description="ClinVar")

    _defn = EnumDefinition(
        name="AnnotationSourceEnum",
        description="Sources of functional annotations",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "3dligandsite",
            PermissibleValue(
                text="3dligandsite",
                description="3D-LigandSite"))
        setattr(cls, "14_3_3_pred",
            PermissibleValue(
                text="14_3_3_pred",
                description="14-3-3-Pred"))

class DatabaseNameEnum(EnumDefinitionImpl):
    """
    External database names
    """
    uniprot = PermissibleValue(
        text="uniprot",
        description="UniProt")
    pdb = PermissibleValue(
        text="pdb",
        description="Protein Data Bank")
    pfam = PermissibleValue(
        text="pfam",
        description="Pfam")
    cath = PermissibleValue(
        text="cath",
        description="CATH")
    scop = PermissibleValue(
        text="scop",
        description="SCOP")
    interpro = PermissibleValue(
        text="interpro",
        description="InterPro")
    chembl = PermissibleValue(
        text="chembl",
        description="ChEMBL")
    chebi = PermissibleValue(
        text="chebi",
        description="ChEBI")
    pubchem = PermissibleValue(
        text="pubchem",
        description="PubChem")
    drugbank = PermissibleValue(
        text="drugbank",
        description="DrugBank")
    omim = PermissibleValue(
        text="omim",
        description="OMIM")
    clinvar = PermissibleValue(
        text="clinvar",
        description="ClinVar")
    cosmic = PermissibleValue(
        text="cosmic",
        description="COSMIC")
    gnomad = PermissibleValue(
        text="gnomad",
        description="gnomAD")
    intact = PermissibleValue(
        text="intact",
        description="IntAct")
    string = PermissibleValue(
        text="string",
        description="STRING")
    biogrid = PermissibleValue(
        text="biogrid",
        description="BioGRID")
    reactome = PermissibleValue(
        text="reactome",
        description="Reactome")
    kegg = PermissibleValue(
        text="kegg",
        description="KEGG")
    go = PermissibleValue(
        text="go",
        description="Gene Ontology")

    _defn = EnumDefinition(
        name="DatabaseNameEnum",
        description="External database names",
    )

# Slots
class slots:
    pass

slots.namedThing__id = Slot(uri=LAMBDABER.id, name="namedThing__id", curie=LAMBDABER.curie('id'),
                   model_uri=LAMBDABER.namedThing__id, domain=None, range=URIRef)

slots.namedThing__title = Slot(uri=DCTERMS.title, name="namedThing__title", curie=DCTERMS.curie('title'),
                   model_uri=LAMBDABER.namedThing__title, domain=None, range=Optional[str])

slots.namedThing__description = Slot(uri=LAMBDABER.description, name="namedThing__description", curie=LAMBDABER.curie('description'),
                   model_uri=LAMBDABER.namedThing__description, domain=None, range=Optional[str])

slots.attributeGroup__description = Slot(uri=LAMBDABER.description, name="attributeGroup__description", curie=LAMBDABER.curie('description'),
                   model_uri=LAMBDABER.attributeGroup__description, domain=None, range=Optional[str])

slots.dataset__keywords = Slot(uri=LAMBDABER.keywords, name="dataset__keywords", curie=LAMBDABER.curie('keywords'),
                   model_uri=LAMBDABER.dataset__keywords, domain=None, range=Optional[Union[str, list[str]]])

slots.dataset__instruments = Slot(uri=LAMBDABER.instruments, name="dataset__instruments", curie=LAMBDABER.curie('instruments'),
                   model_uri=LAMBDABER.dataset__instruments, domain=None, range=Optional[Union[dict[Union[str, InstrumentId], Union[dict, Instrument]], list[Union[dict, Instrument]]]])

slots.dataset__studies = Slot(uri=LAMBDABER.studies, name="dataset__studies", curie=LAMBDABER.curie('studies'),
                   model_uri=LAMBDABER.dataset__studies, domain=None, range=Optional[Union[dict[Union[str, StudyId], Union[dict, Study]], list[Union[dict, Study]]]])

slots.study__protein_constructs = Slot(uri=LAMBDABER.protein_constructs, name="study__protein_constructs", curie=LAMBDABER.curie('protein_constructs'),
                   model_uri=LAMBDABER.study__protein_constructs, domain=None, range=Optional[Union[dict[Union[str, ProteinConstructId], Union[dict, ProteinConstruct]], list[Union[dict, ProteinConstruct]]]])

slots.study__samples = Slot(uri=LAMBDABER.samples, name="study__samples", curie=LAMBDABER.curie('samples'),
                   model_uri=LAMBDABER.study__samples, domain=None, range=Optional[Union[dict[Union[str, SampleId], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.study__sample_preparations = Slot(uri=LAMBDABER.sample_preparations, name="study__sample_preparations", curie=LAMBDABER.curie('sample_preparations'),
                   model_uri=LAMBDABER.study__sample_preparations, domain=None, range=Optional[Union[dict[Union[str, SamplePreparationId], Union[dict, SamplePreparation]], list[Union[dict, SamplePreparation]]]])

slots.study__instrument_runs = Slot(uri=LAMBDABER.instrument_runs, name="study__instrument_runs", curie=LAMBDABER.curie('instrument_runs'),
                   model_uri=LAMBDABER.study__instrument_runs, domain=None, range=Optional[Union[dict[Union[str, ExperimentRunId], Union[dict, ExperimentRun]], list[Union[dict, ExperimentRun]]]])

slots.study__workflow_runs = Slot(uri=LAMBDABER.workflow_runs, name="study__workflow_runs", curie=LAMBDABER.curie('workflow_runs'),
                   model_uri=LAMBDABER.study__workflow_runs, domain=None, range=Optional[Union[dict[Union[str, WorkflowRunId], Union[dict, WorkflowRun]], list[Union[dict, WorkflowRun]]]])

slots.study__data_files = Slot(uri=LAMBDABER.data_files, name="study__data_files", curie=LAMBDABER.curie('data_files'),
                   model_uri=LAMBDABER.study__data_files, domain=None, range=Optional[Union[dict[Union[str, DataFileId], Union[dict, DataFile]], list[Union[dict, DataFile]]]])

slots.study__images = Slot(uri=LAMBDABER.images, name="study__images", curie=LAMBDABER.curie('images'),
                   model_uri=LAMBDABER.study__images, domain=None, range=Optional[Union[dict[Union[str, ImageId], Union[dict, Image]], list[Union[dict, Image]]]])

slots.study__aggregated_protein_views = Slot(uri=LAMBDABER.aggregated_protein_views, name="study__aggregated_protein_views", curie=LAMBDABER.curie('aggregated_protein_views'),
                   model_uri=LAMBDABER.study__aggregated_protein_views, domain=None, range=Optional[Union[dict[Union[str, AggregatedProteinViewId], Union[dict, AggregatedProteinView]], list[Union[dict, AggregatedProteinView]]]])

slots.sample__sample_code = Slot(uri=LAMBDABER.sample_code, name="sample__sample_code", curie=LAMBDABER.curie('sample_code'),
                   model_uri=LAMBDABER.sample__sample_code, domain=None, range=str)

slots.sample__sample_type = Slot(uri=LAMBDABER.sample_type, name="sample__sample_type", curie=LAMBDABER.curie('sample_type'),
                   model_uri=LAMBDABER.sample__sample_type, domain=None, range=Union[str, "SampleTypeEnum"])

slots.sample__molecular_composition = Slot(uri=LAMBDABER.molecular_composition, name="sample__molecular_composition", curie=LAMBDABER.curie('molecular_composition'),
                   model_uri=LAMBDABER.sample__molecular_composition, domain=None, range=Optional[Union[dict, MolecularComposition]])

slots.sample__molecular_weight = Slot(uri=LAMBDABER.molecular_weight, name="sample__molecular_weight", curie=LAMBDABER.curie('molecular_weight'),
                   model_uri=LAMBDABER.sample__molecular_weight, domain=None, range=Optional[float])

slots.sample__concentration = Slot(uri=LAMBDABER.concentration, name="sample__concentration", curie=LAMBDABER.curie('concentration'),
                   model_uri=LAMBDABER.sample__concentration, domain=None, range=Optional[float])

slots.sample__concentration_unit = Slot(uri=LAMBDABER.concentration_unit, name="sample__concentration_unit", curie=LAMBDABER.curie('concentration_unit'),
                   model_uri=LAMBDABER.sample__concentration_unit, domain=None, range=Optional[Union[str, "ConcentrationUnitEnum"]])

slots.sample__buffer_composition = Slot(uri=LAMBDABER.buffer_composition, name="sample__buffer_composition", curie=LAMBDABER.curie('buffer_composition'),
                   model_uri=LAMBDABER.sample__buffer_composition, domain=None, range=Optional[Union[dict, BufferComposition]])

slots.sample__preparation_method = Slot(uri=LAMBDABER.preparation_method, name="sample__preparation_method", curie=LAMBDABER.curie('preparation_method'),
                   model_uri=LAMBDABER.sample__preparation_method, domain=None, range=Optional[str])

slots.sample__storage_conditions = Slot(uri=LAMBDABER.storage_conditions, name="sample__storage_conditions", curie=LAMBDABER.curie('storage_conditions'),
                   model_uri=LAMBDABER.sample__storage_conditions, domain=None, range=Optional[Union[dict, StorageConditions]])

slots.sample__organism = Slot(uri=LAMBDABER.organism, name="sample__organism", curie=LAMBDABER.curie('organism'),
                   model_uri=LAMBDABER.sample__organism, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__anatomy = Slot(uri=LAMBDABER.anatomy, name="sample__anatomy", curie=LAMBDABER.curie('anatomy'),
                   model_uri=LAMBDABER.sample__anatomy, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__cell_type = Slot(uri=LAMBDABER.cell_type, name="sample__cell_type", curie=LAMBDABER.curie('cell_type'),
                   model_uri=LAMBDABER.sample__cell_type, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__parent_sample_id = Slot(uri=LAMBDABER.parent_sample_id, name="sample__parent_sample_id", curie=LAMBDABER.curie('parent_sample_id'),
                   model_uri=LAMBDABER.sample__parent_sample_id, domain=None, range=Optional[Union[str, SampleId]])

slots.sample__purity_percentage = Slot(uri=LAMBDABER.purity_percentage, name="sample__purity_percentage", curie=LAMBDABER.curie('purity_percentage'),
                   model_uri=LAMBDABER.sample__purity_percentage, domain=None, range=Optional[float])

slots.sample__quality_metrics = Slot(uri=LAMBDABER.quality_metrics, name="sample__quality_metrics", curie=LAMBDABER.curie('quality_metrics'),
                   model_uri=LAMBDABER.sample__quality_metrics, domain=None, range=Optional[str])

slots.sample__functional_sites = Slot(uri=LAMBDABER.functional_sites, name="sample__functional_sites", curie=LAMBDABER.curie('functional_sites'),
                   model_uri=LAMBDABER.sample__functional_sites, domain=None, range=Optional[Union[dict[Union[str, FunctionalSiteId], Union[dict, FunctionalSite]], list[Union[dict, FunctionalSite]]]])

slots.sample__structural_features = Slot(uri=LAMBDABER.structural_features, name="sample__structural_features", curie=LAMBDABER.curie('structural_features'),
                   model_uri=LAMBDABER.sample__structural_features, domain=None, range=Optional[Union[dict[Union[str, StructuralFeatureId], Union[dict, StructuralFeature]], list[Union[dict, StructuralFeature]]]])

slots.sample__protein_interactions = Slot(uri=LAMBDABER.protein_interactions, name="sample__protein_interactions", curie=LAMBDABER.curie('protein_interactions'),
                   model_uri=LAMBDABER.sample__protein_interactions, domain=None, range=Optional[Union[dict[Union[str, ProteinProteinInteractionId], Union[dict, ProteinProteinInteraction]], list[Union[dict, ProteinProteinInteraction]]]])

slots.sample__ligand_interactions = Slot(uri=LAMBDABER.ligand_interactions, name="sample__ligand_interactions", curie=LAMBDABER.curie('ligand_interactions'),
                   model_uri=LAMBDABER.sample__ligand_interactions, domain=None, range=Optional[Union[Union[dict, LigandInteraction], list[Union[dict, LigandInteraction]]]])

slots.sample__mutation_effects = Slot(uri=LAMBDABER.mutation_effects, name="sample__mutation_effects", curie=LAMBDABER.curie('mutation_effects'),
                   model_uri=LAMBDABER.sample__mutation_effects, domain=None, range=Optional[Union[dict[Union[str, MutationEffectId], Union[dict, MutationEffect]], list[Union[dict, MutationEffect]]]])

slots.sample__ptm_annotations = Slot(uri=LAMBDABER.ptm_annotations, name="sample__ptm_annotations", curie=LAMBDABER.curie('ptm_annotations'),
                   model_uri=LAMBDABER.sample__ptm_annotations, domain=None, range=Optional[Union[dict[Union[str, PostTranslationalModificationId], Union[dict, PostTranslationalModification]], list[Union[dict, PostTranslationalModification]]]])

slots.sample__biophysical_properties = Slot(uri=LAMBDABER.biophysical_properties, name="sample__biophysical_properties", curie=LAMBDABER.curie('biophysical_properties'),
                   model_uri=LAMBDABER.sample__biophysical_properties, domain=None, range=Optional[Union[Union[dict, BiophysicalProperty], list[Union[dict, BiophysicalProperty]]]])

slots.sample__evolutionary_conservation = Slot(uri=LAMBDABER.evolutionary_conservation, name="sample__evolutionary_conservation", curie=LAMBDABER.curie('evolutionary_conservation'),
                   model_uri=LAMBDABER.sample__evolutionary_conservation, domain=None, range=Optional[Union[dict, EvolutionaryConservation]])

slots.sample__conformational_ensemble = Slot(uri=LAMBDABER.conformational_ensemble, name="sample__conformational_ensemble", curie=LAMBDABER.curie('conformational_ensemble'),
                   model_uri=LAMBDABER.sample__conformational_ensemble, domain=None, range=Optional[Union[dict, ConformationalEnsemble]])

slots.sample__database_cross_references = Slot(uri=LAMBDABER.database_cross_references, name="sample__database_cross_references", curie=LAMBDABER.curie('database_cross_references'),
                   model_uri=LAMBDABER.sample__database_cross_references, domain=None, range=Optional[Union[Union[dict, DatabaseCrossReference], list[Union[dict, DatabaseCrossReference]]]])

slots.sample__protein_name = Slot(uri=NSLS2.Protein_Name, name="sample__protein_name", curie=NSLS2.curie('Protein_Name'),
                   model_uri=LAMBDABER.sample__protein_name, domain=None, range=Optional[str])

slots.sample__construct = Slot(uri=NSLS2.Construct, name="sample__construct", curie=NSLS2.curie('Construct'),
                   model_uri=LAMBDABER.sample__construct, domain=None, range=Optional[str])

slots.sample__tag = Slot(uri=NSLS2.Tag, name="sample__tag", curie=NSLS2.curie('Tag'),
                   model_uri=LAMBDABER.sample__tag, domain=None, range=Optional[str])

slots.sample__mutations = Slot(uri=NSLS2.Mutations, name="sample__mutations", curie=NSLS2.curie('Mutations'),
                   model_uri=LAMBDABER.sample__mutations, domain=None, range=Optional[str])

slots.sample__expression_system = Slot(uri=NSLS2.Expression_System, name="sample__expression_system", curie=NSLS2.curie('Expression_System'),
                   model_uri=LAMBDABER.sample__expression_system, domain=None, range=Optional[str])

slots.sample__ligand = Slot(uri=NSLS2.Ligand, name="sample__ligand", curie=NSLS2.curie('Ligand'),
                   model_uri=LAMBDABER.sample__ligand, domain=None, range=Optional[str])

slots.proteinConstruct__construct_id = Slot(uri=LAMBDABER.construct_id, name="proteinConstruct__construct_id", curie=LAMBDABER.curie('construct_id'),
                   model_uri=LAMBDABER.proteinConstruct__construct_id, domain=None, range=str)

slots.proteinConstruct__uniprot_id = Slot(uri=LAMBDABER.uniprot_id, name="proteinConstruct__uniprot_id", curie=LAMBDABER.curie('uniprot_id'),
                   model_uri=LAMBDABER.proteinConstruct__uniprot_id, domain=None, range=Optional[str])

slots.proteinConstruct__gene_name = Slot(uri=LAMBDABER.gene_name, name="proteinConstruct__gene_name", curie=LAMBDABER.curie('gene_name'),
                   model_uri=LAMBDABER.proteinConstruct__gene_name, domain=None, range=Optional[str])

slots.proteinConstruct__ncbi_taxid = Slot(uri=LAMBDABER.ncbi_taxid, name="proteinConstruct__ncbi_taxid", curie=LAMBDABER.curie('ncbi_taxid'),
                   model_uri=LAMBDABER.proteinConstruct__ncbi_taxid, domain=None, range=Optional[str])

slots.proteinConstruct__sequence_length_aa = Slot(uri=LAMBDABER.sequence_length_aa, name="proteinConstruct__sequence_length_aa", curie=LAMBDABER.curie('sequence_length_aa'),
                   model_uri=LAMBDABER.proteinConstruct__sequence_length_aa, domain=None, range=Optional[int])

slots.proteinConstruct__construct_description = Slot(uri=LAMBDABER.construct_description, name="proteinConstruct__construct_description", curie=LAMBDABER.curie('construct_description'),
                   model_uri=LAMBDABER.proteinConstruct__construct_description, domain=None, range=Optional[str])

slots.proteinConstruct__gene_synthesis_provider = Slot(uri=LAMBDABER.gene_synthesis_provider, name="proteinConstruct__gene_synthesis_provider", curie=LAMBDABER.curie('gene_synthesis_provider'),
                   model_uri=LAMBDABER.proteinConstruct__gene_synthesis_provider, domain=None, range=Optional[str])

slots.proteinConstruct__codon_optimization_organism = Slot(uri=LAMBDABER.codon_optimization_organism, name="proteinConstruct__codon_optimization_organism", curie=LAMBDABER.curie('codon_optimization_organism'),
                   model_uri=LAMBDABER.proteinConstruct__codon_optimization_organism, domain=None, range=Optional[str])

slots.proteinConstruct__vector_backbone = Slot(uri=LAMBDABER.vector_backbone, name="proteinConstruct__vector_backbone", curie=LAMBDABER.curie('vector_backbone'),
                   model_uri=LAMBDABER.proteinConstruct__vector_backbone, domain=None, range=Optional[str])

slots.proteinConstruct__vector_name = Slot(uri=LAMBDABER.vector_name, name="proteinConstruct__vector_name", curie=LAMBDABER.curie('vector_name'),
                   model_uri=LAMBDABER.proteinConstruct__vector_name, domain=None, range=Optional[str])

slots.proteinConstruct__promoter = Slot(uri=LAMBDABER.promoter, name="proteinConstruct__promoter", curie=LAMBDABER.curie('promoter'),
                   model_uri=LAMBDABER.proteinConstruct__promoter, domain=None, range=Optional[str])

slots.proteinConstruct__tag_nterm = Slot(uri=LAMBDABER.tag_nterm, name="proteinConstruct__tag_nterm", curie=LAMBDABER.curie('tag_nterm'),
                   model_uri=LAMBDABER.proteinConstruct__tag_nterm, domain=None, range=Optional[str])

slots.proteinConstruct__tag_cterm = Slot(uri=LAMBDABER.tag_cterm, name="proteinConstruct__tag_cterm", curie=LAMBDABER.curie('tag_cterm'),
                   model_uri=LAMBDABER.proteinConstruct__tag_cterm, domain=None, range=Optional[str])

slots.proteinConstruct__cleavage_site = Slot(uri=LAMBDABER.cleavage_site, name="proteinConstruct__cleavage_site", curie=LAMBDABER.curie('cleavage_site'),
                   model_uri=LAMBDABER.proteinConstruct__cleavage_site, domain=None, range=Optional[str])

slots.proteinConstruct__signal_peptide = Slot(uri=LAMBDABER.signal_peptide, name="proteinConstruct__signal_peptide", curie=LAMBDABER.curie('signal_peptide'),
                   model_uri=LAMBDABER.proteinConstruct__signal_peptide, domain=None, range=Optional[str])

slots.proteinConstruct__selectable_marker = Slot(uri=LAMBDABER.selectable_marker, name="proteinConstruct__selectable_marker", curie=LAMBDABER.curie('selectable_marker'),
                   model_uri=LAMBDABER.proteinConstruct__selectable_marker, domain=None, range=Optional[str])

slots.proteinConstruct__cloning_method = Slot(uri=LAMBDABER.cloning_method, name="proteinConstruct__cloning_method", curie=LAMBDABER.curie('cloning_method'),
                   model_uri=LAMBDABER.proteinConstruct__cloning_method, domain=None, range=Optional[str])

slots.proteinConstruct__insert_boundaries = Slot(uri=LAMBDABER.insert_boundaries, name="proteinConstruct__insert_boundaries", curie=LAMBDABER.curie('insert_boundaries'),
                   model_uri=LAMBDABER.proteinConstruct__insert_boundaries, domain=None, range=Optional[str])

slots.proteinConstruct__sequence_file_path = Slot(uri=LAMBDABER.sequence_file_path, name="proteinConstruct__sequence_file_path", curie=LAMBDABER.curie('sequence_file_path'),
                   model_uri=LAMBDABER.proteinConstruct__sequence_file_path, domain=None, range=Optional[str])

slots.proteinConstruct__sequence_verified_by = Slot(uri=LAMBDABER.sequence_verified_by, name="proteinConstruct__sequence_verified_by", curie=LAMBDABER.curie('sequence_verified_by'),
                   model_uri=LAMBDABER.proteinConstruct__sequence_verified_by, domain=None, range=Optional[str])

slots.proteinConstruct__verification_notes = Slot(uri=LAMBDABER.verification_notes, name="proteinConstruct__verification_notes", curie=LAMBDABER.curie('verification_notes'),
                   model_uri=LAMBDABER.proteinConstruct__verification_notes, domain=None, range=Optional[str])

slots.samplePreparation__preparation_type = Slot(uri=LAMBDABER.preparation_type, name="samplePreparation__preparation_type", curie=LAMBDABER.curie('preparation_type'),
                   model_uri=LAMBDABER.samplePreparation__preparation_type, domain=None, range=Union[str, "PreparationTypeEnum"])

slots.samplePreparation__sample_id = Slot(uri=LAMBDABER.sample_id, name="samplePreparation__sample_id", curie=LAMBDABER.curie('sample_id'),
                   model_uri=LAMBDABER.samplePreparation__sample_id, domain=None, range=str)

slots.samplePreparation__preparation_date = Slot(uri=LAMBDABER.preparation_date, name="samplePreparation__preparation_date", curie=LAMBDABER.curie('preparation_date'),
                   model_uri=LAMBDABER.samplePreparation__preparation_date, domain=None, range=Optional[str])

slots.samplePreparation__operator_id = Slot(uri=LAMBDABER.operator_id, name="samplePreparation__operator_id", curie=LAMBDABER.curie('operator_id'),
                   model_uri=LAMBDABER.samplePreparation__operator_id, domain=None, range=Optional[str])

slots.samplePreparation__protocol_description = Slot(uri=LAMBDABER.protocol_description, name="samplePreparation__protocol_description", curie=LAMBDABER.curie('protocol_description'),
                   model_uri=LAMBDABER.samplePreparation__protocol_description, domain=None, range=Optional[str])

slots.samplePreparation__expression_system = Slot(uri=LAMBDABER.expression_system, name="samplePreparation__expression_system", curie=LAMBDABER.curie('expression_system'),
                   model_uri=LAMBDABER.samplePreparation__expression_system, domain=None, range=Optional[Union[str, "ExpressionSystemEnum"]])

slots.samplePreparation__host_strain_or_cell_line = Slot(uri=LAMBDABER.host_strain_or_cell_line, name="samplePreparation__host_strain_or_cell_line", curie=LAMBDABER.curie('host_strain_or_cell_line'),
                   model_uri=LAMBDABER.samplePreparation__host_strain_or_cell_line, domain=None, range=Optional[str])

slots.samplePreparation__culture_volume_l = Slot(uri=LAMBDABER.culture_volume_l, name="samplePreparation__culture_volume_l", curie=LAMBDABER.curie('culture_volume_l'),
                   model_uri=LAMBDABER.samplePreparation__culture_volume_l, domain=None, range=Optional[float])

slots.samplePreparation__medium = Slot(uri=LAMBDABER.medium, name="samplePreparation__medium", curie=LAMBDABER.curie('medium'),
                   model_uri=LAMBDABER.samplePreparation__medium, domain=None, range=Optional[str])

slots.samplePreparation__antibiotic_selection = Slot(uri=LAMBDABER.antibiotic_selection, name="samplePreparation__antibiotic_selection", curie=LAMBDABER.curie('antibiotic_selection'),
                   model_uri=LAMBDABER.samplePreparation__antibiotic_selection, domain=None, range=Optional[str])

slots.samplePreparation__growth_temperature_c = Slot(uri=LAMBDABER.growth_temperature_c, name="samplePreparation__growth_temperature_c", curie=LAMBDABER.curie('growth_temperature_c'),
                   model_uri=LAMBDABER.samplePreparation__growth_temperature_c, domain=None, range=Optional[float])

slots.samplePreparation__induction_agent = Slot(uri=LAMBDABER.induction_agent, name="samplePreparation__induction_agent", curie=LAMBDABER.curie('induction_agent'),
                   model_uri=LAMBDABER.samplePreparation__induction_agent, domain=None, range=Optional[str])

slots.samplePreparation__inducer_concentration = Slot(uri=LAMBDABER.inducer_concentration, name="samplePreparation__inducer_concentration", curie=LAMBDABER.curie('inducer_concentration'),
                   model_uri=LAMBDABER.samplePreparation__inducer_concentration, domain=None, range=Optional[str])

slots.samplePreparation__induction_temperature_c = Slot(uri=LAMBDABER.induction_temperature_c, name="samplePreparation__induction_temperature_c", curie=LAMBDABER.curie('induction_temperature_c'),
                   model_uri=LAMBDABER.samplePreparation__induction_temperature_c, domain=None, range=Optional[float])

slots.samplePreparation__induction_time_h = Slot(uri=LAMBDABER.induction_time_h, name="samplePreparation__induction_time_h", curie=LAMBDABER.curie('induction_time_h'),
                   model_uri=LAMBDABER.samplePreparation__induction_time_h, domain=None, range=Optional[float])

slots.samplePreparation__od600_at_induction = Slot(uri=LAMBDABER.od600_at_induction, name="samplePreparation__od600_at_induction", curie=LAMBDABER.curie('od600_at_induction'),
                   model_uri=LAMBDABER.samplePreparation__od600_at_induction, domain=None, range=Optional[float])

slots.samplePreparation__harvest_timepoint = Slot(uri=LAMBDABER.harvest_timepoint, name="samplePreparation__harvest_timepoint", curie=LAMBDABER.curie('harvest_timepoint'),
                   model_uri=LAMBDABER.samplePreparation__harvest_timepoint, domain=None, range=Optional[str])

slots.samplePreparation__lysis_method = Slot(uri=LAMBDABER.lysis_method, name="samplePreparation__lysis_method", curie=LAMBDABER.curie('lysis_method'),
                   model_uri=LAMBDABER.samplePreparation__lysis_method, domain=None, range=Optional[str])

slots.samplePreparation__protease_inhibitors = Slot(uri=LAMBDABER.protease_inhibitors, name="samplePreparation__protease_inhibitors", curie=LAMBDABER.curie('protease_inhibitors'),
                   model_uri=LAMBDABER.samplePreparation__protease_inhibitors, domain=None, range=Optional[str])

slots.samplePreparation__purification_steps = Slot(uri=LAMBDABER.purification_steps, name="samplePreparation__purification_steps", curie=LAMBDABER.curie('purification_steps'),
                   model_uri=LAMBDABER.samplePreparation__purification_steps, domain=None, range=Optional[Union[Union[str, "PurificationStepEnum"], list[Union[str, "PurificationStepEnum"]]]])

slots.samplePreparation__affinity_type = Slot(uri=LAMBDABER.affinity_type, name="samplePreparation__affinity_type", curie=LAMBDABER.curie('affinity_type'),
                   model_uri=LAMBDABER.samplePreparation__affinity_type, domain=None, range=Optional[str])

slots.samplePreparation__affinity_column = Slot(uri=LAMBDABER.affinity_column, name="samplePreparation__affinity_column", curie=LAMBDABER.curie('affinity_column'),
                   model_uri=LAMBDABER.samplePreparation__affinity_column, domain=None, range=Optional[str])

slots.samplePreparation__lysis_buffer = Slot(uri=LAMBDABER.lysis_buffer, name="samplePreparation__lysis_buffer", curie=LAMBDABER.curie('lysis_buffer'),
                   model_uri=LAMBDABER.samplePreparation__lysis_buffer, domain=None, range=Optional[str])

slots.samplePreparation__wash_buffer = Slot(uri=LAMBDABER.wash_buffer, name="samplePreparation__wash_buffer", curie=LAMBDABER.curie('wash_buffer'),
                   model_uri=LAMBDABER.samplePreparation__wash_buffer, domain=None, range=Optional[str])

slots.samplePreparation__elution_buffer = Slot(uri=LAMBDABER.elution_buffer, name="samplePreparation__elution_buffer", curie=LAMBDABER.curie('elution_buffer'),
                   model_uri=LAMBDABER.samplePreparation__elution_buffer, domain=None, range=Optional[str])

slots.samplePreparation__tag_removal = Slot(uri=LAMBDABER.tag_removal, name="samplePreparation__tag_removal", curie=LAMBDABER.curie('tag_removal'),
                   model_uri=LAMBDABER.samplePreparation__tag_removal, domain=None, range=Optional[Union[bool, Bool]])

slots.samplePreparation__protease = Slot(uri=LAMBDABER.protease, name="samplePreparation__protease", curie=LAMBDABER.curie('protease'),
                   model_uri=LAMBDABER.samplePreparation__protease, domain=None, range=Optional[str])

slots.samplePreparation__protease_ratio = Slot(uri=LAMBDABER.protease_ratio, name="samplePreparation__protease_ratio", curie=LAMBDABER.curie('protease_ratio'),
                   model_uri=LAMBDABER.samplePreparation__protease_ratio, domain=None, range=Optional[str])

slots.samplePreparation__cleavage_time_h = Slot(uri=LAMBDABER.cleavage_time_h, name="samplePreparation__cleavage_time_h", curie=LAMBDABER.curie('cleavage_time_h'),
                   model_uri=LAMBDABER.samplePreparation__cleavage_time_h, domain=None, range=Optional[float])

slots.samplePreparation__cleavage_temperature_c = Slot(uri=LAMBDABER.cleavage_temperature_c, name="samplePreparation__cleavage_temperature_c", curie=LAMBDABER.curie('cleavage_temperature_c'),
                   model_uri=LAMBDABER.samplePreparation__cleavage_temperature_c, domain=None, range=Optional[float])

slots.samplePreparation__second_affinity_reverse = Slot(uri=LAMBDABER.second_affinity_reverse, name="samplePreparation__second_affinity_reverse", curie=LAMBDABER.curie('second_affinity_reverse'),
                   model_uri=LAMBDABER.samplePreparation__second_affinity_reverse, domain=None, range=Optional[str])

slots.samplePreparation__iex_column = Slot(uri=LAMBDABER.iex_column, name="samplePreparation__iex_column", curie=LAMBDABER.curie('iex_column'),
                   model_uri=LAMBDABER.samplePreparation__iex_column, domain=None, range=Optional[str])

slots.samplePreparation__hic_column = Slot(uri=LAMBDABER.hic_column, name="samplePreparation__hic_column", curie=LAMBDABER.curie('hic_column'),
                   model_uri=LAMBDABER.samplePreparation__hic_column, domain=None, range=Optional[str])

slots.samplePreparation__sec_column = Slot(uri=LAMBDABER.sec_column, name="samplePreparation__sec_column", curie=LAMBDABER.curie('sec_column'),
                   model_uri=LAMBDABER.samplePreparation__sec_column, domain=None, range=Optional[str])

slots.samplePreparation__sec_buffer = Slot(uri=LAMBDABER.sec_buffer, name="samplePreparation__sec_buffer", curie=LAMBDABER.curie('sec_buffer'),
                   model_uri=LAMBDABER.samplePreparation__sec_buffer, domain=None, range=Optional[str])

slots.samplePreparation__concentration_method = Slot(uri=LAMBDABER.concentration_method, name="samplePreparation__concentration_method", curie=LAMBDABER.curie('concentration_method'),
                   model_uri=LAMBDABER.samplePreparation__concentration_method, domain=None, range=Optional[str])

slots.samplePreparation__final_buffer = Slot(uri=LAMBDABER.final_buffer, name="samplePreparation__final_buffer", curie=LAMBDABER.curie('final_buffer'),
                   model_uri=LAMBDABER.samplePreparation__final_buffer, domain=None, range=Optional[str])

slots.samplePreparation__final_concentration_mg_per_ml = Slot(uri=LAMBDABER.final_concentration_mg_per_ml, name="samplePreparation__final_concentration_mg_per_ml", curie=LAMBDABER.curie('final_concentration_mg_per_ml'),
                   model_uri=LAMBDABER.samplePreparation__final_concentration_mg_per_ml, domain=None, range=Optional[float])

slots.samplePreparation__yield_mg = Slot(uri=LAMBDABER.yield_mg, name="samplePreparation__yield_mg", curie=LAMBDABER.curie('yield_mg'),
                   model_uri=LAMBDABER.samplePreparation__yield_mg, domain=None, range=Optional[float])

slots.samplePreparation__purity_by_sds_page_percent = Slot(uri=LAMBDABER.purity_by_sds_page_percent, name="samplePreparation__purity_by_sds_page_percent", curie=LAMBDABER.curie('purity_by_sds_page_percent'),
                   model_uri=LAMBDABER.samplePreparation__purity_by_sds_page_percent, domain=None, range=Optional[float])

slots.samplePreparation__aggregation_assessment = Slot(uri=LAMBDABER.aggregation_assessment, name="samplePreparation__aggregation_assessment", curie=LAMBDABER.curie('aggregation_assessment'),
                   model_uri=LAMBDABER.samplePreparation__aggregation_assessment, domain=None, range=Optional[str])

slots.samplePreparation__aliquoting = Slot(uri=LAMBDABER.aliquoting, name="samplePreparation__aliquoting", curie=LAMBDABER.curie('aliquoting'),
                   model_uri=LAMBDABER.samplePreparation__aliquoting, domain=None, range=Optional[str])

slots.instrument__instrument_code = Slot(uri=LAMBDABER.instrument_code, name="instrument__instrument_code", curie=LAMBDABER.curie('instrument_code'),
                   model_uri=LAMBDABER.instrument__instrument_code, domain=None, range=str)

slots.instrument__manufacturer = Slot(uri=LAMBDABER.manufacturer, name="instrument__manufacturer", curie=LAMBDABER.curie('manufacturer'),
                   model_uri=LAMBDABER.instrument__manufacturer, domain=None, range=Optional[str])

slots.instrument__model = Slot(uri=LAMBDABER.model, name="instrument__model", curie=LAMBDABER.curie('model'),
                   model_uri=LAMBDABER.instrument__model, domain=None, range=Optional[str])

slots.instrument__installation_date = Slot(uri=LAMBDABER.installation_date, name="instrument__installation_date", curie=LAMBDABER.curie('installation_date'),
                   model_uri=LAMBDABER.instrument__installation_date, domain=None, range=Optional[str])

slots.instrument__current_status = Slot(uri=LAMBDABER.current_status, name="instrument__current_status", curie=LAMBDABER.curie('current_status'),
                   model_uri=LAMBDABER.instrument__current_status, domain=None, range=Optional[Union[str, "InstrumentStatusEnum"]])

slots.cryoEMInstrument__accelerating_voltage = Slot(uri=LAMBDABER.accelerating_voltage, name="cryoEMInstrument__accelerating_voltage", curie=LAMBDABER.curie('accelerating_voltage'),
                   model_uri=LAMBDABER.cryoEMInstrument__accelerating_voltage, domain=None, range=Optional[int])

slots.cryoEMInstrument__cs_corrector = Slot(uri=LAMBDABER.cs_corrector, name="cryoEMInstrument__cs_corrector", curie=LAMBDABER.curie('cs_corrector'),
                   model_uri=LAMBDABER.cryoEMInstrument__cs_corrector, domain=None, range=Optional[Union[bool, Bool]])

slots.cryoEMInstrument__phase_plate = Slot(uri=LAMBDABER.phase_plate, name="cryoEMInstrument__phase_plate", curie=LAMBDABER.curie('phase_plate'),
                   model_uri=LAMBDABER.cryoEMInstrument__phase_plate, domain=None, range=Optional[Union[bool, Bool]])

slots.cryoEMInstrument__detector_technology = Slot(uri=LAMBDABER.detector_technology, name="cryoEMInstrument__detector_technology", curie=LAMBDABER.curie('detector_technology'),
                   model_uri=LAMBDABER.cryoEMInstrument__detector_technology, domain=None, range=Optional[Union[str, "DetectorTechnologyEnum"]])

slots.cryoEMInstrument__detector_manufacturer = Slot(uri=LAMBDABER.detector_manufacturer, name="cryoEMInstrument__detector_manufacturer", curie=LAMBDABER.curie('detector_manufacturer'),
                   model_uri=LAMBDABER.cryoEMInstrument__detector_manufacturer, domain=None, range=Optional[str])

slots.cryoEMInstrument__detector_model = Slot(uri=LAMBDABER.detector_model, name="cryoEMInstrument__detector_model", curie=LAMBDABER.curie('detector_model'),
                   model_uri=LAMBDABER.cryoEMInstrument__detector_model, domain=None, range=Optional[str])

slots.cryoEMInstrument__detector_mode = Slot(uri=LAMBDABER.detector_mode, name="cryoEMInstrument__detector_mode", curie=LAMBDABER.curie('detector_mode'),
                   model_uri=LAMBDABER.cryoEMInstrument__detector_mode, domain=None, range=Optional[Union[str, "DetectorModeEnum"]])

slots.cryoEMInstrument__detector_position = Slot(uri=LAMBDABER.detector_position, name="cryoEMInstrument__detector_position", curie=LAMBDABER.curie('detector_position'),
                   model_uri=LAMBDABER.cryoEMInstrument__detector_position, domain=None, range=Optional[str])

slots.cryoEMInstrument__detector_dimensions = Slot(uri=LAMBDABER.detector_dimensions, name="cryoEMInstrument__detector_dimensions", curie=LAMBDABER.curie('detector_dimensions'),
                   model_uri=LAMBDABER.cryoEMInstrument__detector_dimensions, domain=None, range=Optional[str])

slots.cryoEMInstrument__pixel_size_physical_um = Slot(uri=LAMBDABER.pixel_size_physical_um, name="cryoEMInstrument__pixel_size_physical_um", curie=LAMBDABER.curie('pixel_size_physical_um'),
                   model_uri=LAMBDABER.cryoEMInstrument__pixel_size_physical_um, domain=None, range=Optional[float])

slots.cryoEMInstrument__autoloader_capacity = Slot(uri=LAMBDABER.autoloader_capacity, name="cryoEMInstrument__autoloader_capacity", curie=LAMBDABER.curie('autoloader_capacity'),
                   model_uri=LAMBDABER.cryoEMInstrument__autoloader_capacity, domain=None, range=Optional[int])

slots.xRayInstrument__source_type = Slot(uri=LAMBDABER.source_type, name="xRayInstrument__source_type", curie=LAMBDABER.curie('source_type'),
                   model_uri=LAMBDABER.xRayInstrument__source_type, domain=None, range=Optional[Union[str, "XRaySourceTypeEnum"]])

slots.xRayInstrument__detector_technology = Slot(uri=NSLS2.Detector, name="xRayInstrument__detector_technology", curie=NSLS2.curie('Detector'),
                   model_uri=LAMBDABER.xRayInstrument__detector_technology, domain=None, range=Optional[Union[str, "DetectorTechnologyEnum"]])

slots.xRayInstrument__detector_manufacturer = Slot(uri=LAMBDABER.detector_manufacturer, name="xRayInstrument__detector_manufacturer", curie=LAMBDABER.curie('detector_manufacturer'),
                   model_uri=LAMBDABER.xRayInstrument__detector_manufacturer, domain=None, range=Optional[str])

slots.xRayInstrument__detector_model = Slot(uri=LAMBDABER.detector_model, name="xRayInstrument__detector_model", curie=LAMBDABER.curie('detector_model'),
                   model_uri=LAMBDABER.xRayInstrument__detector_model, domain=None, range=Optional[str])

slots.xRayInstrument__beamline_id = Slot(uri=NSLS2.Beamline, name="xRayInstrument__beamline_id", curie=NSLS2.curie('Beamline'),
                   model_uri=LAMBDABER.xRayInstrument__beamline_id, domain=None, range=Optional[str])

slots.xRayInstrument__energy_min = Slot(uri=LAMBDABER.energy_min, name="xRayInstrument__energy_min", curie=LAMBDABER.curie('energy_min'),
                   model_uri=LAMBDABER.xRayInstrument__energy_min, domain=None, range=Optional[float])

slots.xRayInstrument__energy_max = Slot(uri=LAMBDABER.energy_max, name="xRayInstrument__energy_max", curie=LAMBDABER.curie('energy_max'),
                   model_uri=LAMBDABER.xRayInstrument__energy_max, domain=None, range=Optional[float])

slots.xRayInstrument__beam_size_min = Slot(uri=LAMBDABER.beam_size_min, name="xRayInstrument__beam_size_min", curie=LAMBDABER.curie('beam_size_min'),
                   model_uri=LAMBDABER.xRayInstrument__beam_size_min, domain=None, range=Optional[float])

slots.xRayInstrument__beam_size_max = Slot(uri=LAMBDABER.beam_size_max, name="xRayInstrument__beam_size_max", curie=LAMBDABER.curie('beam_size_max'),
                   model_uri=LAMBDABER.xRayInstrument__beam_size_max, domain=None, range=Optional[float])

slots.xRayInstrument__flux_density = Slot(uri=LAMBDABER.flux_density, name="xRayInstrument__flux_density", curie=LAMBDABER.curie('flux_density'),
                   model_uri=LAMBDABER.xRayInstrument__flux_density, domain=None, range=Optional[float])

slots.xRayInstrument__monochromator_type = Slot(uri=LAMBDABER.monochromator_type, name="xRayInstrument__monochromator_type", curie=LAMBDABER.curie('monochromator_type'),
                   model_uri=LAMBDABER.xRayInstrument__monochromator_type, domain=None, range=Optional[str])

slots.xRayInstrument__goniometer_type = Slot(uri=LAMBDABER.goniometer_type, name="xRayInstrument__goniometer_type", curie=LAMBDABER.curie('goniometer_type'),
                   model_uri=LAMBDABER.xRayInstrument__goniometer_type, domain=None, range=Optional[str])

slots.xRayInstrument__crystal_cooling_capability = Slot(uri=LAMBDABER.crystal_cooling_capability, name="xRayInstrument__crystal_cooling_capability", curie=LAMBDABER.curie('crystal_cooling_capability'),
                   model_uri=LAMBDABER.xRayInstrument__crystal_cooling_capability, domain=None, range=Optional[Union[bool, Bool]])

slots.sAXSInstrument__q_range_min = Slot(uri=LAMBDABER.q_range_min, name="sAXSInstrument__q_range_min", curie=LAMBDABER.curie('q_range_min'),
                   model_uri=LAMBDABER.sAXSInstrument__q_range_min, domain=None, range=Optional[float])

slots.sAXSInstrument__q_range_max = Slot(uri=LAMBDABER.q_range_max, name="sAXSInstrument__q_range_max", curie=LAMBDABER.curie('q_range_max'),
                   model_uri=LAMBDABER.sAXSInstrument__q_range_max, domain=None, range=Optional[float])

slots.sAXSInstrument__detector_distance_min = Slot(uri=LAMBDABER.detector_distance_min, name="sAXSInstrument__detector_distance_min", curie=LAMBDABER.curie('detector_distance_min'),
                   model_uri=LAMBDABER.sAXSInstrument__detector_distance_min, domain=None, range=Optional[float])

slots.sAXSInstrument__detector_distance_max = Slot(uri=LAMBDABER.detector_distance_max, name="sAXSInstrument__detector_distance_max", curie=LAMBDABER.curie('detector_distance_max'),
                   model_uri=LAMBDABER.sAXSInstrument__detector_distance_max, domain=None, range=Optional[float])

slots.sAXSInstrument__sample_changer_capacity = Slot(uri=LAMBDABER.sample_changer_capacity, name="sAXSInstrument__sample_changer_capacity", curie=LAMBDABER.curie('sample_changer_capacity'),
                   model_uri=LAMBDABER.sAXSInstrument__sample_changer_capacity, domain=None, range=Optional[int])

slots.sAXSInstrument__temperature_control_range = Slot(uri=LAMBDABER.temperature_control_range, name="sAXSInstrument__temperature_control_range", curie=LAMBDABER.curie('temperature_control_range'),
                   model_uri=LAMBDABER.sAXSInstrument__temperature_control_range, domain=None, range=Optional[str])

slots.experimentRun__experiment_code = Slot(uri=LAMBDABER.experiment_code, name="experimentRun__experiment_code", curie=LAMBDABER.curie('experiment_code'),
                   model_uri=LAMBDABER.experimentRun__experiment_code, domain=None, range=str)

slots.experimentRun__sample_id = Slot(uri=LAMBDABER.sample_id, name="experimentRun__sample_id", curie=LAMBDABER.curie('sample_id'),
                   model_uri=LAMBDABER.experimentRun__sample_id, domain=None, range=str)

slots.experimentRun__instrument_id = Slot(uri=LAMBDABER.instrument_id, name="experimentRun__instrument_id", curie=LAMBDABER.curie('instrument_id'),
                   model_uri=LAMBDABER.experimentRun__instrument_id, domain=None, range=Union[str, InstrumentId])

slots.experimentRun__experiment_date = Slot(uri=LAMBDABER.experiment_date, name="experimentRun__experiment_date", curie=LAMBDABER.curie('experiment_date'),
                   model_uri=LAMBDABER.experimentRun__experiment_date, domain=None, range=Optional[str])

slots.experimentRun__operator_id = Slot(uri=LAMBDABER.operator_id, name="experimentRun__operator_id", curie=LAMBDABER.curie('operator_id'),
                   model_uri=LAMBDABER.experimentRun__operator_id, domain=None, range=Optional[str])

slots.experimentRun__technique = Slot(uri=LAMBDABER.technique, name="experimentRun__technique", curie=LAMBDABER.curie('technique'),
                   model_uri=LAMBDABER.experimentRun__technique, domain=None, range=Union[str, "TechniqueEnum"])

slots.experimentRun__experimental_method = Slot(uri=LAMBDABER.experimental_method, name="experimentRun__experimental_method", curie=LAMBDABER.curie('experimental_method'),
                   model_uri=LAMBDABER.experimentRun__experimental_method, domain=None, range=Optional[Union[str, "ExperimentalMethodEnum"]])

slots.experimentRun__experimental_conditions = Slot(uri=LAMBDABER.experimental_conditions, name="experimentRun__experimental_conditions", curie=LAMBDABER.curie('experimental_conditions'),
                   model_uri=LAMBDABER.experimentRun__experimental_conditions, domain=None, range=Optional[Union[dict, ExperimentalConditions]])

slots.experimentRun__data_collection_strategy = Slot(uri=LAMBDABER.data_collection_strategy, name="experimentRun__data_collection_strategy", curie=LAMBDABER.curie('data_collection_strategy'),
                   model_uri=LAMBDABER.experimentRun__data_collection_strategy, domain=None, range=Optional[Union[dict, DataCollectionStrategy]])

slots.experimentRun__quality_metrics = Slot(uri=LAMBDABER.quality_metrics, name="experimentRun__quality_metrics", curie=LAMBDABER.curie('quality_metrics'),
                   model_uri=LAMBDABER.experimentRun__quality_metrics, domain=None, range=Optional[Union[dict, QualityMetrics]])

slots.experimentRun__raw_data_location = Slot(uri=LAMBDABER.raw_data_location, name="experimentRun__raw_data_location", curie=LAMBDABER.curie('raw_data_location'),
                   model_uri=LAMBDABER.experimentRun__raw_data_location, domain=None, range=Optional[str])

slots.experimentRun__processing_status = Slot(uri=LAMBDABER.processing_status, name="experimentRun__processing_status", curie=LAMBDABER.curie('processing_status'),
                   model_uri=LAMBDABER.experimentRun__processing_status, domain=None, range=Optional[Union[str, "ProcessingStatusEnum"]])

slots.experimentRun__wavelength = Slot(uri=LAMBDABER.wavelength, name="experimentRun__wavelength", curie=LAMBDABER.curie('wavelength'),
                   model_uri=LAMBDABER.experimentRun__wavelength, domain=None, range=Optional[float])

slots.experimentRun__oscillation_angle = Slot(uri=LAMBDABER.oscillation_angle, name="experimentRun__oscillation_angle", curie=LAMBDABER.curie('oscillation_angle'),
                   model_uri=LAMBDABER.experimentRun__oscillation_angle, domain=None, range=Optional[float])

slots.experimentRun__start_angle = Slot(uri=LAMBDABER.start_angle, name="experimentRun__start_angle", curie=LAMBDABER.curie('start_angle'),
                   model_uri=LAMBDABER.experimentRun__start_angle, domain=None, range=Optional[float])

slots.experimentRun__number_of_images = Slot(uri=LAMBDABER.number_of_images, name="experimentRun__number_of_images", curie=LAMBDABER.curie('number_of_images'),
                   model_uri=LAMBDABER.experimentRun__number_of_images, domain=None, range=Optional[int])

slots.experimentRun__beam_center_x = Slot(uri=LAMBDABER.beam_center_x, name="experimentRun__beam_center_x", curie=LAMBDABER.curie('beam_center_x'),
                   model_uri=LAMBDABER.experimentRun__beam_center_x, domain=None, range=Optional[float])

slots.experimentRun__beam_center_y = Slot(uri=LAMBDABER.beam_center_y, name="experimentRun__beam_center_y", curie=LAMBDABER.curie('beam_center_y'),
                   model_uri=LAMBDABER.experimentRun__beam_center_y, domain=None, range=Optional[float])

slots.experimentRun__detector_distance = Slot(uri=LAMBDABER.detector_distance, name="experimentRun__detector_distance", curie=LAMBDABER.curie('detector_distance'),
                   model_uri=LAMBDABER.experimentRun__detector_distance, domain=None, range=Optional[float])

slots.experimentRun__pixel_size_x = Slot(uri=LAMBDABER.pixel_size_x, name="experimentRun__pixel_size_x", curie=LAMBDABER.curie('pixel_size_x'),
                   model_uri=LAMBDABER.experimentRun__pixel_size_x, domain=None, range=Optional[float])

slots.experimentRun__pixel_size_y = Slot(uri=LAMBDABER.pixel_size_y, name="experimentRun__pixel_size_y", curie=LAMBDABER.curie('pixel_size_y'),
                   model_uri=LAMBDABER.experimentRun__pixel_size_y, domain=None, range=Optional[float])

slots.experimentRun__total_rotation = Slot(uri=LAMBDABER.total_rotation, name="experimentRun__total_rotation", curie=LAMBDABER.curie('total_rotation'),
                   model_uri=LAMBDABER.experimentRun__total_rotation, domain=None, range=Optional[float])

slots.experimentRun__beamline = Slot(uri=LAMBDABER.beamline, name="experimentRun__beamline", curie=LAMBDABER.curie('beamline'),
                   model_uri=LAMBDABER.experimentRun__beamline, domain=None, range=Optional[str])

slots.workflowRun__workflow_code = Slot(uri=LAMBDABER.workflow_code, name="workflowRun__workflow_code", curie=LAMBDABER.curie('workflow_code'),
                   model_uri=LAMBDABER.workflowRun__workflow_code, domain=None, range=str)

slots.workflowRun__workflow_type = Slot(uri=LAMBDABER.workflow_type, name="workflowRun__workflow_type", curie=LAMBDABER.curie('workflow_type'),
                   model_uri=LAMBDABER.workflowRun__workflow_type, domain=None, range=Union[str, "WorkflowTypeEnum"])

slots.workflowRun__experiment_id = Slot(uri=LAMBDABER.experiment_id, name="workflowRun__experiment_id", curie=LAMBDABER.curie('experiment_id'),
                   model_uri=LAMBDABER.workflowRun__experiment_id, domain=None, range=str)

slots.workflowRun__processing_level = Slot(uri=LAMBDABER.processing_level, name="workflowRun__processing_level", curie=LAMBDABER.curie('processing_level'),
                   model_uri=LAMBDABER.workflowRun__processing_level, domain=None, range=Optional[int])

slots.workflowRun__software_name = Slot(uri=LAMBDABER.software_name, name="workflowRun__software_name", curie=LAMBDABER.curie('software_name'),
                   model_uri=LAMBDABER.workflowRun__software_name, domain=None, range=str)

slots.workflowRun__software_version = Slot(uri=LAMBDABER.software_version, name="workflowRun__software_version", curie=LAMBDABER.curie('software_version'),
                   model_uri=LAMBDABER.workflowRun__software_version, domain=None, range=Optional[str])

slots.workflowRun__additional_software = Slot(uri=LAMBDABER.additional_software, name="workflowRun__additional_software", curie=LAMBDABER.curie('additional_software'),
                   model_uri=LAMBDABER.workflowRun__additional_software, domain=None, range=Optional[str])

slots.workflowRun__processing_parameters = Slot(uri=LAMBDABER.processing_parameters, name="workflowRun__processing_parameters", curie=LAMBDABER.curie('processing_parameters'),
                   model_uri=LAMBDABER.workflowRun__processing_parameters, domain=None, range=Optional[str])

slots.workflowRun__parameters_file_path = Slot(uri=LAMBDABER.parameters_file_path, name="workflowRun__parameters_file_path", curie=LAMBDABER.curie('parameters_file_path'),
                   model_uri=LAMBDABER.workflowRun__parameters_file_path, domain=None, range=Optional[str])

slots.workflowRun__indexer_module = Slot(uri=LAMBDABER.indexer_module, name="workflowRun__indexer_module", curie=LAMBDABER.curie('indexer_module'),
                   model_uri=LAMBDABER.workflowRun__indexer_module, domain=None, range=Optional[str])

slots.workflowRun__integrator_module = Slot(uri=LAMBDABER.integrator_module, name="workflowRun__integrator_module", curie=LAMBDABER.curie('integrator_module'),
                   model_uri=LAMBDABER.workflowRun__integrator_module, domain=None, range=Optional[str])

slots.workflowRun__scaler_module = Slot(uri=LAMBDABER.scaler_module, name="workflowRun__scaler_module", curie=LAMBDABER.curie('scaler_module'),
                   model_uri=LAMBDABER.workflowRun__scaler_module, domain=None, range=Optional[str])

slots.workflowRun__outlier_rejection_method = Slot(uri=LAMBDABER.outlier_rejection_method, name="workflowRun__outlier_rejection_method", curie=LAMBDABER.curie('outlier_rejection_method'),
                   model_uri=LAMBDABER.workflowRun__outlier_rejection_method, domain=None, range=Optional[str])

slots.workflowRun__phasing_method = Slot(uri=LAMBDABER.phasing_method, name="workflowRun__phasing_method", curie=LAMBDABER.curie('phasing_method'),
                   model_uri=LAMBDABER.workflowRun__phasing_method, domain=None, range=Optional[Union[str, "PhasingMethodEnum"]])

slots.workflowRun__search_model_pdb_id = Slot(uri=LAMBDABER.search_model_pdb_id, name="workflowRun__search_model_pdb_id", curie=LAMBDABER.curie('search_model_pdb_id'),
                   model_uri=LAMBDABER.workflowRun__search_model_pdb_id, domain=None, range=Optional[str])

slots.workflowRun__tls_used = Slot(uri=LAMBDABER.tls_used, name="workflowRun__tls_used", curie=LAMBDABER.curie('tls_used'),
                   model_uri=LAMBDABER.workflowRun__tls_used, domain=None, range=Optional[Union[bool, Bool]])

slots.workflowRun__ncs_used = Slot(uri=LAMBDABER.ncs_used, name="workflowRun__ncs_used", curie=LAMBDABER.curie('ncs_used'),
                   model_uri=LAMBDABER.workflowRun__ncs_used, domain=None, range=Optional[Union[bool, Bool]])

slots.workflowRun__restraints_other = Slot(uri=LAMBDABER.restraints_other, name="workflowRun__restraints_other", curie=LAMBDABER.curie('restraints_other'),
                   model_uri=LAMBDABER.workflowRun__restraints_other, domain=None, range=Optional[str])

slots.workflowRun__ligands_cofactors = Slot(uri=LAMBDABER.ligands_cofactors, name="workflowRun__ligands_cofactors", curie=LAMBDABER.curie('ligands_cofactors'),
                   model_uri=LAMBDABER.workflowRun__ligands_cofactors, domain=None, range=Optional[str])

slots.workflowRun__number_of_waters = Slot(uri=LAMBDABER.number_of_waters, name="workflowRun__number_of_waters", curie=LAMBDABER.curie('number_of_waters'),
                   model_uri=LAMBDABER.workflowRun__number_of_waters, domain=None, range=Optional[int])

slots.workflowRun__refinement_resolution_a = Slot(uri=LAMBDABER.refinement_resolution_a, name="workflowRun__refinement_resolution_a", curie=LAMBDABER.curie('refinement_resolution_a'),
                   model_uri=LAMBDABER.workflowRun__refinement_resolution_a, domain=None, range=Optional[float])

slots.workflowRun__deposited_to_pdb = Slot(uri=LAMBDABER.deposited_to_pdb, name="workflowRun__deposited_to_pdb", curie=LAMBDABER.curie('deposited_to_pdb'),
                   model_uri=LAMBDABER.workflowRun__deposited_to_pdb, domain=None, range=Optional[Union[bool, Bool]])

slots.workflowRun__pdb_id = Slot(uri=LAMBDABER.pdb_id, name="workflowRun__pdb_id", curie=LAMBDABER.curie('pdb_id'),
                   model_uri=LAMBDABER.workflowRun__pdb_id, domain=None, range=Optional[str])

slots.workflowRun__validation_report_path = Slot(uri=LAMBDABER.validation_report_path, name="workflowRun__validation_report_path", curie=LAMBDABER.curie('validation_report_path'),
                   model_uri=LAMBDABER.workflowRun__validation_report_path, domain=None, range=Optional[str])

slots.workflowRun__space_group = Slot(uri=LAMBDABER.space_group, name="workflowRun__space_group", curie=LAMBDABER.curie('space_group'),
                   model_uri=LAMBDABER.workflowRun__space_group, domain=None, range=Optional[str])

slots.workflowRun__unit_cell_a = Slot(uri=LAMBDABER.unit_cell_a, name="workflowRun__unit_cell_a", curie=LAMBDABER.curie('unit_cell_a'),
                   model_uri=LAMBDABER.workflowRun__unit_cell_a, domain=None, range=Optional[float])

slots.workflowRun__unit_cell_b = Slot(uri=LAMBDABER.unit_cell_b, name="workflowRun__unit_cell_b", curie=LAMBDABER.curie('unit_cell_b'),
                   model_uri=LAMBDABER.workflowRun__unit_cell_b, domain=None, range=Optional[float])

slots.workflowRun__unit_cell_c = Slot(uri=LAMBDABER.unit_cell_c, name="workflowRun__unit_cell_c", curie=LAMBDABER.curie('unit_cell_c'),
                   model_uri=LAMBDABER.workflowRun__unit_cell_c, domain=None, range=Optional[float])

slots.workflowRun__unit_cell_alpha = Slot(uri=LAMBDABER.unit_cell_alpha, name="workflowRun__unit_cell_alpha", curie=LAMBDABER.curie('unit_cell_alpha'),
                   model_uri=LAMBDABER.workflowRun__unit_cell_alpha, domain=None, range=Optional[float])

slots.workflowRun__unit_cell_beta = Slot(uri=LAMBDABER.unit_cell_beta, name="workflowRun__unit_cell_beta", curie=LAMBDABER.curie('unit_cell_beta'),
                   model_uri=LAMBDABER.workflowRun__unit_cell_beta, domain=None, range=Optional[float])

slots.workflowRun__unit_cell_gamma = Slot(uri=LAMBDABER.unit_cell_gamma, name="workflowRun__unit_cell_gamma", curie=LAMBDABER.curie('unit_cell_gamma'),
                   model_uri=LAMBDABER.workflowRun__unit_cell_gamma, domain=None, range=Optional[float])

slots.workflowRun__resolution_high = Slot(uri=LAMBDABER.resolution_high, name="workflowRun__resolution_high", curie=LAMBDABER.curie('resolution_high'),
                   model_uri=LAMBDABER.workflowRun__resolution_high, domain=None, range=Optional[float])

slots.workflowRun__resolution_low = Slot(uri=LAMBDABER.resolution_low, name="workflowRun__resolution_low", curie=LAMBDABER.curie('resolution_low'),
                   model_uri=LAMBDABER.workflowRun__resolution_low, domain=None, range=Optional[float])

slots.workflowRun__rmerge = Slot(uri=LAMBDABER.rmerge, name="workflowRun__rmerge", curie=LAMBDABER.curie('rmerge'),
                   model_uri=LAMBDABER.workflowRun__rmerge, domain=None, range=Optional[float])

slots.workflowRun__rpim = Slot(uri=LAMBDABER.rpim, name="workflowRun__rpim", curie=LAMBDABER.curie('rpim'),
                   model_uri=LAMBDABER.workflowRun__rpim, domain=None, range=Optional[float])

slots.workflowRun__cc_half = Slot(uri=LAMBDABER.cc_half, name="workflowRun__cc_half", curie=LAMBDABER.curie('cc_half'),
                   model_uri=LAMBDABER.workflowRun__cc_half, domain=None, range=Optional[float])

slots.workflowRun__completeness_percent = Slot(uri=LAMBDABER.completeness_percent, name="workflowRun__completeness_percent", curie=LAMBDABER.curie('completeness_percent'),
                   model_uri=LAMBDABER.workflowRun__completeness_percent, domain=None, range=Optional[float])

slots.workflowRun__i_over_sigma = Slot(uri=LAMBDABER.i_over_sigma, name="workflowRun__i_over_sigma", curie=LAMBDABER.curie('i_over_sigma'),
                   model_uri=LAMBDABER.workflowRun__i_over_sigma, domain=None, range=Optional[float])

slots.workflowRun__wilson_b_factor = Slot(uri=LAMBDABER.wilson_b_factor, name="workflowRun__wilson_b_factor", curie=LAMBDABER.curie('wilson_b_factor'),
                   model_uri=LAMBDABER.workflowRun__wilson_b_factor, domain=None, range=Optional[float])

slots.workflowRun__multiplicity = Slot(uri=LAMBDABER.multiplicity, name="workflowRun__multiplicity", curie=LAMBDABER.curie('multiplicity'),
                   model_uri=LAMBDABER.workflowRun__multiplicity, domain=None, range=Optional[float])

slots.workflowRun__rwork = Slot(uri=LAMBDABER.rwork, name="workflowRun__rwork", curie=LAMBDABER.curie('rwork'),
                   model_uri=LAMBDABER.workflowRun__rwork, domain=None, range=Optional[float])

slots.workflowRun__rfree = Slot(uri=LAMBDABER.rfree, name="workflowRun__rfree", curie=LAMBDABER.curie('rfree'),
                   model_uri=LAMBDABER.workflowRun__rfree, domain=None, range=Optional[float])

slots.workflowRun__rmsd_bonds = Slot(uri=LAMBDABER.rmsd_bonds, name="workflowRun__rmsd_bonds", curie=LAMBDABER.curie('rmsd_bonds'),
                   model_uri=LAMBDABER.workflowRun__rmsd_bonds, domain=None, range=Optional[float])

slots.workflowRun__rmsd_angles = Slot(uri=LAMBDABER.rmsd_angles, name="workflowRun__rmsd_angles", curie=LAMBDABER.curie('rmsd_angles'),
                   model_uri=LAMBDABER.workflowRun__rmsd_angles, domain=None, range=Optional[float])

slots.workflowRun__ramachandran_favored = Slot(uri=LAMBDABER.ramachandran_favored, name="workflowRun__ramachandran_favored", curie=LAMBDABER.curie('ramachandran_favored'),
                   model_uri=LAMBDABER.workflowRun__ramachandran_favored, domain=None, range=Optional[float])

slots.workflowRun__ramachandran_outliers = Slot(uri=LAMBDABER.ramachandran_outliers, name="workflowRun__ramachandran_outliers", curie=LAMBDABER.curie('ramachandran_outliers'),
                   model_uri=LAMBDABER.workflowRun__ramachandran_outliers, domain=None, range=Optional[float])

slots.workflowRun__clashscore = Slot(uri=LAMBDABER.clashscore, name="workflowRun__clashscore", curie=LAMBDABER.curie('clashscore'),
                   model_uri=LAMBDABER.workflowRun__clashscore, domain=None, range=Optional[float])

slots.workflowRun__processing_notes = Slot(uri=LAMBDABER.processing_notes, name="workflowRun__processing_notes", curie=LAMBDABER.curie('processing_notes'),
                   model_uri=LAMBDABER.workflowRun__processing_notes, domain=None, range=Optional[str])

slots.workflowRun__compute_resources = Slot(uri=LAMBDABER.compute_resources, name="workflowRun__compute_resources", curie=LAMBDABER.curie('compute_resources'),
                   model_uri=LAMBDABER.workflowRun__compute_resources, domain=None, range=Optional[Union[dict, ComputeResources]])

slots.workflowRun__started_at = Slot(uri=LAMBDABER.started_at, name="workflowRun__started_at", curie=LAMBDABER.curie('started_at'),
                   model_uri=LAMBDABER.workflowRun__started_at, domain=None, range=Optional[str])

slots.workflowRun__completed_at = Slot(uri=LAMBDABER.completed_at, name="workflowRun__completed_at", curie=LAMBDABER.curie('completed_at'),
                   model_uri=LAMBDABER.workflowRun__completed_at, domain=None, range=Optional[str])

slots.workflowRun__output_files = Slot(uri=LAMBDABER.output_files, name="workflowRun__output_files", curie=LAMBDABER.curie('output_files'),
                   model_uri=LAMBDABER.workflowRun__output_files, domain=None, range=Optional[Union[Union[str, DataFileId], list[Union[str, DataFileId]]]])

slots.dataFile__file_name = Slot(uri=LAMBDABER.file_name, name="dataFile__file_name", curie=LAMBDABER.curie('file_name'),
                   model_uri=LAMBDABER.dataFile__file_name, domain=None, range=str)

slots.dataFile__file_path = Slot(uri=LAMBDABER.file_path, name="dataFile__file_path", curie=LAMBDABER.curie('file_path'),
                   model_uri=LAMBDABER.dataFile__file_path, domain=None, range=Optional[str])

slots.dataFile__file_format = Slot(uri=LAMBDABER.file_format, name="dataFile__file_format", curie=LAMBDABER.curie('file_format'),
                   model_uri=LAMBDABER.dataFile__file_format, domain=None, range=Union[str, "FileFormatEnum"])

slots.dataFile__file_size_bytes = Slot(uri=LAMBDABER.file_size_bytes, name="dataFile__file_size_bytes", curie=LAMBDABER.curie('file_size_bytes'),
                   model_uri=LAMBDABER.dataFile__file_size_bytes, domain=None, range=Optional[int])

slots.dataFile__checksum = Slot(uri=LAMBDABER.checksum, name="dataFile__checksum", curie=LAMBDABER.curie('checksum'),
                   model_uri=LAMBDABER.dataFile__checksum, domain=None, range=Optional[str])

slots.dataFile__creation_date = Slot(uri=LAMBDABER.creation_date, name="dataFile__creation_date", curie=LAMBDABER.curie('creation_date'),
                   model_uri=LAMBDABER.dataFile__creation_date, domain=None, range=Optional[str])

slots.dataFile__data_type = Slot(uri=LAMBDABER.data_type, name="dataFile__data_type", curie=LAMBDABER.curie('data_type'),
                   model_uri=LAMBDABER.dataFile__data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.image__file_name = Slot(uri=LAMBDABER.file_name, name="image__file_name", curie=LAMBDABER.curie('file_name'),
                   model_uri=LAMBDABER.image__file_name, domain=None, range=str)

slots.image__acquisition_date = Slot(uri=LAMBDABER.acquisition_date, name="image__acquisition_date", curie=LAMBDABER.curie('acquisition_date'),
                   model_uri=LAMBDABER.image__acquisition_date, domain=None, range=Optional[str])

slots.image__pixel_size = Slot(uri=LAMBDABER.pixel_size, name="image__pixel_size", curie=LAMBDABER.curie('pixel_size'),
                   model_uri=LAMBDABER.image__pixel_size, domain=None, range=Optional[float])

slots.image__dimensions_x = Slot(uri=LAMBDABER.dimensions_x, name="image__dimensions_x", curie=LAMBDABER.curie('dimensions_x'),
                   model_uri=LAMBDABER.image__dimensions_x, domain=None, range=Optional[int])

slots.image__dimensions_y = Slot(uri=LAMBDABER.dimensions_y, name="image__dimensions_y", curie=LAMBDABER.curie('dimensions_y'),
                   model_uri=LAMBDABER.image__dimensions_y, domain=None, range=Optional[int])

slots.image__exposure_time = Slot(uri=LAMBDABER.exposure_time, name="image__exposure_time", curie=LAMBDABER.curie('exposure_time'),
                   model_uri=LAMBDABER.image__exposure_time, domain=None, range=Optional[float])

slots.image__dose = Slot(uri=LAMBDABER.dose, name="image__dose", curie=LAMBDABER.curie('dose'),
                   model_uri=LAMBDABER.image__dose, domain=None, range=Optional[float])

slots.image2D__defocus = Slot(uri=LAMBDABER.defocus, name="image2D__defocus", curie=LAMBDABER.curie('defocus'),
                   model_uri=LAMBDABER.image2D__defocus, domain=None, range=Optional[float])

slots.image2D__astigmatism = Slot(uri=LAMBDABER.astigmatism, name="image2D__astigmatism", curie=LAMBDABER.curie('astigmatism'),
                   model_uri=LAMBDABER.image2D__astigmatism, domain=None, range=Optional[float])

slots.image3D__dimensions_z = Slot(uri=LAMBDABER.dimensions_z, name="image3D__dimensions_z", curie=LAMBDABER.curie('dimensions_z'),
                   model_uri=LAMBDABER.image3D__dimensions_z, domain=None, range=Optional[int])

slots.image3D__voxel_size = Slot(uri=LAMBDABER.voxel_size, name="image3D__voxel_size", curie=LAMBDABER.curie('voxel_size'),
                   model_uri=LAMBDABER.image3D__voxel_size, domain=None, range=Optional[float])

slots.image3D__reconstruction_method = Slot(uri=LAMBDABER.reconstruction_method, name="image3D__reconstruction_method", curie=LAMBDABER.curie('reconstruction_method'),
                   model_uri=LAMBDABER.image3D__reconstruction_method, domain=None, range=Optional[str])

slots.fTIRImage__wavenumber_min = Slot(uri=LAMBDABER.wavenumber_min, name="fTIRImage__wavenumber_min", curie=LAMBDABER.curie('wavenumber_min'),
                   model_uri=LAMBDABER.fTIRImage__wavenumber_min, domain=None, range=Optional[float])

slots.fTIRImage__wavenumber_max = Slot(uri=LAMBDABER.wavenumber_max, name="fTIRImage__wavenumber_max", curie=LAMBDABER.curie('wavenumber_max'),
                   model_uri=LAMBDABER.fTIRImage__wavenumber_max, domain=None, range=Optional[float])

slots.fTIRImage__spectral_resolution = Slot(uri=LAMBDABER.spectral_resolution, name="fTIRImage__spectral_resolution", curie=LAMBDABER.curie('spectral_resolution'),
                   model_uri=LAMBDABER.fTIRImage__spectral_resolution, domain=None, range=Optional[float])

slots.fTIRImage__number_of_scans = Slot(uri=LAMBDABER.number_of_scans, name="fTIRImage__number_of_scans", curie=LAMBDABER.curie('number_of_scans'),
                   model_uri=LAMBDABER.fTIRImage__number_of_scans, domain=None, range=Optional[int])

slots.fTIRImage__apodization_function = Slot(uri=LAMBDABER.apodization_function, name="fTIRImage__apodization_function", curie=LAMBDABER.curie('apodization_function'),
                   model_uri=LAMBDABER.fTIRImage__apodization_function, domain=None, range=Optional[str])

slots.fTIRImage__molecular_signatures = Slot(uri=LAMBDABER.molecular_signatures, name="fTIRImage__molecular_signatures", curie=LAMBDABER.curie('molecular_signatures'),
                   model_uri=LAMBDABER.fTIRImage__molecular_signatures, domain=None, range=Optional[Union[str, list[str]]])

slots.fTIRImage__background_correction = Slot(uri=LAMBDABER.background_correction, name="fTIRImage__background_correction", curie=LAMBDABER.curie('background_correction'),
                   model_uri=LAMBDABER.fTIRImage__background_correction, domain=None, range=Optional[str])

slots.fluorescenceImage__excitation_wavelength = Slot(uri=LAMBDABER.excitation_wavelength, name="fluorescenceImage__excitation_wavelength", curie=LAMBDABER.curie('excitation_wavelength'),
                   model_uri=LAMBDABER.fluorescenceImage__excitation_wavelength, domain=None, range=Optional[float])

slots.fluorescenceImage__emission_wavelength = Slot(uri=LAMBDABER.emission_wavelength, name="fluorescenceImage__emission_wavelength", curie=LAMBDABER.curie('emission_wavelength'),
                   model_uri=LAMBDABER.fluorescenceImage__emission_wavelength, domain=None, range=Optional[float])

slots.fluorescenceImage__excitation_filter = Slot(uri=LAMBDABER.excitation_filter, name="fluorescenceImage__excitation_filter", curie=LAMBDABER.curie('excitation_filter'),
                   model_uri=LAMBDABER.fluorescenceImage__excitation_filter, domain=None, range=Optional[str])

slots.fluorescenceImage__emission_filter = Slot(uri=LAMBDABER.emission_filter, name="fluorescenceImage__emission_filter", curie=LAMBDABER.curie('emission_filter'),
                   model_uri=LAMBDABER.fluorescenceImage__emission_filter, domain=None, range=Optional[str])

slots.fluorescenceImage__fluorophore = Slot(uri=LAMBDABER.fluorophore, name="fluorescenceImage__fluorophore", curie=LAMBDABER.curie('fluorophore'),
                   model_uri=LAMBDABER.fluorescenceImage__fluorophore, domain=None, range=Optional[str])

slots.fluorescenceImage__channel_name = Slot(uri=LAMBDABER.channel_name, name="fluorescenceImage__channel_name", curie=LAMBDABER.curie('channel_name'),
                   model_uri=LAMBDABER.fluorescenceImage__channel_name, domain=None, range=Optional[str])

slots.fluorescenceImage__laser_power = Slot(uri=LAMBDABER.laser_power, name="fluorescenceImage__laser_power", curie=LAMBDABER.curie('laser_power'),
                   model_uri=LAMBDABER.fluorescenceImage__laser_power, domain=None, range=Optional[float])

slots.fluorescenceImage__pinhole_size = Slot(uri=LAMBDABER.pinhole_size, name="fluorescenceImage__pinhole_size", curie=LAMBDABER.curie('pinhole_size'),
                   model_uri=LAMBDABER.fluorescenceImage__pinhole_size, domain=None, range=Optional[float])

slots.fluorescenceImage__quantum_yield = Slot(uri=LAMBDABER.quantum_yield, name="fluorescenceImage__quantum_yield", curie=LAMBDABER.curie('quantum_yield'),
                   model_uri=LAMBDABER.fluorescenceImage__quantum_yield, domain=None, range=Optional[float])

slots.opticalImage__illumination_type = Slot(uri=LAMBDABER.illumination_type, name="opticalImage__illumination_type", curie=LAMBDABER.curie('illumination_type'),
                   model_uri=LAMBDABER.opticalImage__illumination_type, domain=None, range=Optional[Union[str, "IlluminationTypeEnum"]])

slots.opticalImage__magnification = Slot(uri=LAMBDABER.magnification, name="opticalImage__magnification", curie=LAMBDABER.curie('magnification'),
                   model_uri=LAMBDABER.opticalImage__magnification, domain=None, range=Optional[float])

slots.opticalImage__numerical_aperture = Slot(uri=LAMBDABER.numerical_aperture, name="opticalImage__numerical_aperture", curie=LAMBDABER.curie('numerical_aperture'),
                   model_uri=LAMBDABER.opticalImage__numerical_aperture, domain=None, range=Optional[float])

slots.opticalImage__color_channels = Slot(uri=LAMBDABER.color_channels, name="opticalImage__color_channels", curie=LAMBDABER.curie('color_channels'),
                   model_uri=LAMBDABER.opticalImage__color_channels, domain=None, range=Optional[Union[str, list[str]]])

slots.opticalImage__white_balance = Slot(uri=LAMBDABER.white_balance, name="opticalImage__white_balance", curie=LAMBDABER.curie('white_balance'),
                   model_uri=LAMBDABER.opticalImage__white_balance, domain=None, range=Optional[str])

slots.opticalImage__contrast_method = Slot(uri=LAMBDABER.contrast_method, name="opticalImage__contrast_method", curie=LAMBDABER.curie('contrast_method'),
                   model_uri=LAMBDABER.opticalImage__contrast_method, domain=None, range=Optional[str])

slots.xRFImage__beam_energy = Slot(uri=LAMBDABER.beam_energy, name="xRFImage__beam_energy", curie=LAMBDABER.curie('beam_energy'),
                   model_uri=LAMBDABER.xRFImage__beam_energy, domain=None, range=Optional[float])

slots.xRFImage__beam_size = Slot(uri=LAMBDABER.beam_size, name="xRFImage__beam_size", curie=LAMBDABER.curie('beam_size'),
                   model_uri=LAMBDABER.xRFImage__beam_size, domain=None, range=Optional[float])

slots.xRFImage__dwell_time = Slot(uri=LAMBDABER.dwell_time, name="xRFImage__dwell_time", curie=LAMBDABER.curie('dwell_time'),
                   model_uri=LAMBDABER.xRFImage__dwell_time, domain=None, range=Optional[float])

slots.xRFImage__elements_measured = Slot(uri=LAMBDABER.elements_measured, name="xRFImage__elements_measured", curie=LAMBDABER.curie('elements_measured'),
                   model_uri=LAMBDABER.xRFImage__elements_measured, domain=None, range=Optional[Union[str, list[str]]])

slots.xRFImage__source_type = Slot(uri=LAMBDABER.source_type, name="xRFImage__source_type", curie=LAMBDABER.curie('source_type'),
                   model_uri=LAMBDABER.xRFImage__source_type, domain=None, range=Optional[Union[str, "XRaySourceTypeEnum"]])

slots.xRFImage__detector_technology = Slot(uri=LAMBDABER.detector_technology, name="xRFImage__detector_technology", curie=LAMBDABER.curie('detector_technology'),
                   model_uri=LAMBDABER.xRFImage__detector_technology, domain=None, range=Optional[Union[str, "DetectorTechnologyEnum"]])

slots.xRFImage__detector_model = Slot(uri=LAMBDABER.detector_model, name="xRFImage__detector_model", curie=LAMBDABER.curie('detector_model'),
                   model_uri=LAMBDABER.xRFImage__detector_model, domain=None, range=Optional[str])

slots.xRFImage__flux = Slot(uri=LAMBDABER.flux, name="xRFImage__flux", curie=LAMBDABER.curie('flux'),
                   model_uri=LAMBDABER.xRFImage__flux, domain=None, range=Optional[float])

slots.xRFImage__calibration_standard = Slot(uri=LAMBDABER.calibration_standard, name="xRFImage__calibration_standard", curie=LAMBDABER.curie('calibration_standard'),
                   model_uri=LAMBDABER.xRFImage__calibration_standard, domain=None, range=Optional[str])

slots.imageFeature__terms = Slot(uri=LAMBDABER.terms, name="imageFeature__terms", curie=LAMBDABER.curie('terms'),
                   model_uri=LAMBDABER.imageFeature__terms, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.ontologyTerm__label = Slot(uri=LAMBDABER.label, name="ontologyTerm__label", curie=LAMBDABER.curie('label'),
                   model_uri=LAMBDABER.ontologyTerm__label, domain=None, range=Optional[str])

slots.ontologyTerm__definition = Slot(uri=LAMBDABER.definition, name="ontologyTerm__definition", curie=LAMBDABER.curie('definition'),
                   model_uri=LAMBDABER.ontologyTerm__definition, domain=None, range=Optional[str])

slots.ontologyTerm__ontology = Slot(uri=LAMBDABER.ontology, name="ontologyTerm__ontology", curie=LAMBDABER.curie('ontology'),
                   model_uri=LAMBDABER.ontologyTerm__ontology, domain=None, range=Optional[str])

slots.molecularComposition__sequences = Slot(uri=LAMBDABER.sequences, name="molecularComposition__sequences", curie=LAMBDABER.curie('sequences'),
                   model_uri=LAMBDABER.molecularComposition__sequences, domain=None, range=Optional[Union[str, list[str]]])

slots.molecularComposition__modifications = Slot(uri=LAMBDABER.modifications, name="molecularComposition__modifications", curie=LAMBDABER.curie('modifications'),
                   model_uri=LAMBDABER.molecularComposition__modifications, domain=None, range=Optional[Union[str, list[str]]])

slots.molecularComposition__ligands = Slot(uri=LAMBDABER.ligands, name="molecularComposition__ligands", curie=LAMBDABER.curie('ligands'),
                   model_uri=LAMBDABER.molecularComposition__ligands, domain=None, range=Optional[Union[str, list[str]]])

slots.bufferComposition__ph = Slot(uri=LAMBDABER.ph, name="bufferComposition__ph", curie=LAMBDABER.curie('ph'),
                   model_uri=LAMBDABER.bufferComposition__ph, domain=None, range=Optional[float])

slots.bufferComposition__components = Slot(uri=LAMBDABER.components, name="bufferComposition__components", curie=LAMBDABER.curie('components'),
                   model_uri=LAMBDABER.bufferComposition__components, domain=None, range=Optional[Union[str, list[str]]])

slots.bufferComposition__additives = Slot(uri=LAMBDABER.additives, name="bufferComposition__additives", curie=LAMBDABER.curie('additives'),
                   model_uri=LAMBDABER.bufferComposition__additives, domain=None, range=Optional[Union[str, list[str]]])

slots.storageConditions__temperature = Slot(uri=LAMBDABER.temperature, name="storageConditions__temperature", curie=LAMBDABER.curie('temperature'),
                   model_uri=LAMBDABER.storageConditions__temperature, domain=None, range=Optional[float])

slots.storageConditions__temperature_unit = Slot(uri=LAMBDABER.temperature_unit, name="storageConditions__temperature_unit", curie=LAMBDABER.curie('temperature_unit'),
                   model_uri=LAMBDABER.storageConditions__temperature_unit, domain=None, range=Optional[Union[str, "TemperatureUnitEnum"]])

slots.storageConditions__duration = Slot(uri=LAMBDABER.duration, name="storageConditions__duration", curie=LAMBDABER.curie('duration'),
                   model_uri=LAMBDABER.storageConditions__duration, domain=None, range=Optional[str])

slots.storageConditions__atmosphere = Slot(uri=LAMBDABER.atmosphere, name="storageConditions__atmosphere", curie=LAMBDABER.curie('atmosphere'),
                   model_uri=LAMBDABER.storageConditions__atmosphere, domain=None, range=Optional[str])

slots.cryoEMPreparation__grid_type = Slot(uri=LAMBDABER.grid_type, name="cryoEMPreparation__grid_type", curie=LAMBDABER.curie('grid_type'),
                   model_uri=LAMBDABER.cryoEMPreparation__grid_type, domain=None, range=Optional[Union[str, "GridTypeEnum"]])

slots.cryoEMPreparation__support_film = Slot(uri=LAMBDABER.support_film, name="cryoEMPreparation__support_film", curie=LAMBDABER.curie('support_film'),
                   model_uri=LAMBDABER.cryoEMPreparation__support_film, domain=None, range=Optional[str])

slots.cryoEMPreparation__hole_size = Slot(uri=LAMBDABER.hole_size, name="cryoEMPreparation__hole_size", curie=LAMBDABER.curie('hole_size'),
                   model_uri=LAMBDABER.cryoEMPreparation__hole_size, domain=None, range=Optional[float])

slots.cryoEMPreparation__vitrification_method = Slot(uri=LAMBDABER.vitrification_method, name="cryoEMPreparation__vitrification_method", curie=LAMBDABER.curie('vitrification_method'),
                   model_uri=LAMBDABER.cryoEMPreparation__vitrification_method, domain=None, range=Optional[Union[str, "VitrificationMethodEnum"]])

slots.cryoEMPreparation__blot_time = Slot(uri=LAMBDABER.blot_time, name="cryoEMPreparation__blot_time", curie=LAMBDABER.curie('blot_time'),
                   model_uri=LAMBDABER.cryoEMPreparation__blot_time, domain=None, range=Optional[float])

slots.cryoEMPreparation__blot_force = Slot(uri=LAMBDABER.blot_force, name="cryoEMPreparation__blot_force", curie=LAMBDABER.curie('blot_force'),
                   model_uri=LAMBDABER.cryoEMPreparation__blot_force, domain=None, range=Optional[int])

slots.cryoEMPreparation__humidity_percentage = Slot(uri=LAMBDABER.humidity_percentage, name="cryoEMPreparation__humidity_percentage", curie=LAMBDABER.curie('humidity_percentage'),
                   model_uri=LAMBDABER.cryoEMPreparation__humidity_percentage, domain=None, range=Optional[float])

slots.cryoEMPreparation__chamber_temperature = Slot(uri=LAMBDABER.chamber_temperature, name="cryoEMPreparation__chamber_temperature", curie=LAMBDABER.curie('chamber_temperature'),
                   model_uri=LAMBDABER.cryoEMPreparation__chamber_temperature, domain=None, range=Optional[float])

slots.cryoEMPreparation__plasma_treatment = Slot(uri=LAMBDABER.plasma_treatment, name="cryoEMPreparation__plasma_treatment", curie=LAMBDABER.curie('plasma_treatment'),
                   model_uri=LAMBDABER.cryoEMPreparation__plasma_treatment, domain=None, range=Optional[str])

slots.crystallizationConditions__method = Slot(uri=NSLS2.Method, name="crystallizationConditions__method", curie=NSLS2.curie('Method'),
                   model_uri=LAMBDABER.crystallizationConditions__method, domain=None, range=Optional[Union[str, "CrystallizationMethodEnum"]])

slots.crystallizationConditions__crystallization_conditions = Slot(uri=NSLS2.Conditions, name="crystallizationConditions__crystallization_conditions", curie=NSLS2.curie('Conditions'),
                   model_uri=LAMBDABER.crystallizationConditions__crystallization_conditions, domain=None, range=Optional[str])

slots.crystallizationConditions__drop_volume = Slot(uri=NSLS2.Drop_Volume, name="crystallizationConditions__drop_volume", curie=NSLS2.curie('Drop_Volume'),
                   model_uri=LAMBDABER.crystallizationConditions__drop_volume, domain=None, range=Optional[float])

slots.crystallizationConditions__protein_concentration = Slot(uri=NSLS2.Protein_Concentration, name="crystallizationConditions__protein_concentration", curie=NSLS2.curie('Protein_Concentration'),
                   model_uri=LAMBDABER.crystallizationConditions__protein_concentration, domain=None, range=Optional[float])

slots.crystallizationConditions__crystal_size_um = Slot(uri=NSLS2.Crystal_Size, name="crystallizationConditions__crystal_size_um", curie=NSLS2.curie('Crystal_Size'),
                   model_uri=LAMBDABER.crystallizationConditions__crystal_size_um, domain=None, range=Optional[str])

slots.crystallizationConditions__cryo_protectant = Slot(uri=NSLS2.Cryo_Protectant, name="crystallizationConditions__cryo_protectant", curie=NSLS2.curie('Cryo_Protectant'),
                   model_uri=LAMBDABER.crystallizationConditions__cryo_protectant, domain=None, range=Optional[str])

slots.crystallizationConditions__crystal_id = Slot(uri=NSLS2.Crystal_ID, name="crystallizationConditions__crystal_id", curie=NSLS2.curie('Crystal_ID'),
                   model_uri=LAMBDABER.crystallizationConditions__crystal_id, domain=None, range=Optional[str])

slots.crystallizationConditions__screen_name = Slot(uri=LAMBDABER.screen_name, name="crystallizationConditions__screen_name", curie=LAMBDABER.curie('screen_name'),
                   model_uri=LAMBDABER.crystallizationConditions__screen_name, domain=None, range=Optional[str])

slots.crystallizationConditions__temperature_c = Slot(uri=LAMBDABER.temperature_c, name="crystallizationConditions__temperature_c", curie=LAMBDABER.curie('temperature_c'),
                   model_uri=LAMBDABER.crystallizationConditions__temperature_c, domain=None, range=Optional[float])

slots.crystallizationConditions__drop_ratio_protein_to_reservoir = Slot(uri=LAMBDABER.drop_ratio_protein_to_reservoir, name="crystallizationConditions__drop_ratio_protein_to_reservoir", curie=LAMBDABER.curie('drop_ratio_protein_to_reservoir'),
                   model_uri=LAMBDABER.crystallizationConditions__drop_ratio_protein_to_reservoir, domain=None, range=Optional[str])

slots.crystallizationConditions__reservoir_volume_ul = Slot(uri=LAMBDABER.reservoir_volume_ul, name="crystallizationConditions__reservoir_volume_ul", curie=LAMBDABER.curie('reservoir_volume_ul'),
                   model_uri=LAMBDABER.crystallizationConditions__reservoir_volume_ul, domain=None, range=Optional[float])

slots.crystallizationConditions__seeding_type = Slot(uri=LAMBDABER.seeding_type, name="crystallizationConditions__seeding_type", curie=LAMBDABER.curie('seeding_type'),
                   model_uri=LAMBDABER.crystallizationConditions__seeding_type, domain=None, range=Optional[str])

slots.crystallizationConditions__seed_stock_dilution = Slot(uri=LAMBDABER.seed_stock_dilution, name="crystallizationConditions__seed_stock_dilution", curie=LAMBDABER.curie('seed_stock_dilution'),
                   model_uri=LAMBDABER.crystallizationConditions__seed_stock_dilution, domain=None, range=Optional[str])

slots.xRayPreparation__protein_concentration_mg_per_ml = Slot(uri=LAMBDABER.protein_concentration_mg_per_ml, name="xRayPreparation__protein_concentration_mg_per_ml", curie=LAMBDABER.curie('protein_concentration_mg_per_ml'),
                   model_uri=LAMBDABER.xRayPreparation__protein_concentration_mg_per_ml, domain=None, range=Optional[float])

slots.xRayPreparation__protein_buffer = Slot(uri=LAMBDABER.protein_buffer, name="xRayPreparation__protein_buffer", curie=LAMBDABER.curie('protein_buffer'),
                   model_uri=LAMBDABER.xRayPreparation__protein_buffer, domain=None, range=Optional[str])

slots.xRayPreparation__additives = Slot(uri=LAMBDABER.additives, name="xRayPreparation__additives", curie=LAMBDABER.curie('additives'),
                   model_uri=LAMBDABER.xRayPreparation__additives, domain=None, range=Optional[str])

slots.xRayPreparation__crystallization_method = Slot(uri=LAMBDABER.crystallization_method, name="xRayPreparation__crystallization_method", curie=LAMBDABER.curie('crystallization_method'),
                   model_uri=LAMBDABER.xRayPreparation__crystallization_method, domain=None, range=Optional[Union[str, "CrystallizationMethodEnum"]])

slots.xRayPreparation__crystallization_conditions = Slot(uri=LAMBDABER.crystallization_conditions, name="xRayPreparation__crystallization_conditions", curie=LAMBDABER.curie('crystallization_conditions'),
                   model_uri=LAMBDABER.xRayPreparation__crystallization_conditions, domain=None, range=Optional[Union[dict, CrystallizationConditions]])

slots.xRayPreparation__screen_name = Slot(uri=LAMBDABER.screen_name, name="xRayPreparation__screen_name", curie=LAMBDABER.curie('screen_name'),
                   model_uri=LAMBDABER.xRayPreparation__screen_name, domain=None, range=Optional[str])

slots.xRayPreparation__temperature_c = Slot(uri=LAMBDABER.temperature_c, name="xRayPreparation__temperature_c", curie=LAMBDABER.curie('temperature_c'),
                   model_uri=LAMBDABER.xRayPreparation__temperature_c, domain=None, range=Optional[float])

slots.xRayPreparation__drop_ratio_protein_to_reservoir = Slot(uri=LAMBDABER.drop_ratio_protein_to_reservoir, name="xRayPreparation__drop_ratio_protein_to_reservoir", curie=LAMBDABER.curie('drop_ratio_protein_to_reservoir'),
                   model_uri=LAMBDABER.xRayPreparation__drop_ratio_protein_to_reservoir, domain=None, range=Optional[str])

slots.xRayPreparation__drop_volume_nl = Slot(uri=LAMBDABER.drop_volume_nl, name="xRayPreparation__drop_volume_nl", curie=LAMBDABER.curie('drop_volume_nl'),
                   model_uri=LAMBDABER.xRayPreparation__drop_volume_nl, domain=None, range=Optional[float])

slots.xRayPreparation__reservoir_volume_ul = Slot(uri=LAMBDABER.reservoir_volume_ul, name="xRayPreparation__reservoir_volume_ul", curie=LAMBDABER.curie('reservoir_volume_ul'),
                   model_uri=LAMBDABER.xRayPreparation__reservoir_volume_ul, domain=None, range=Optional[float])

slots.xRayPreparation__seeding_type = Slot(uri=LAMBDABER.seeding_type, name="xRayPreparation__seeding_type", curie=LAMBDABER.curie('seeding_type'),
                   model_uri=LAMBDABER.xRayPreparation__seeding_type, domain=None, range=Optional[str])

slots.xRayPreparation__seed_stock_dilution = Slot(uri=LAMBDABER.seed_stock_dilution, name="xRayPreparation__seed_stock_dilution", curie=LAMBDABER.curie('seed_stock_dilution'),
                   model_uri=LAMBDABER.xRayPreparation__seed_stock_dilution, domain=None, range=Optional[str])

slots.xRayPreparation__initial_hit_condition = Slot(uri=LAMBDABER.initial_hit_condition, name="xRayPreparation__initial_hit_condition", curie=LAMBDABER.curie('initial_hit_condition'),
                   model_uri=LAMBDABER.xRayPreparation__initial_hit_condition, domain=None, range=Optional[str])

slots.xRayPreparation__optimization_strategy = Slot(uri=LAMBDABER.optimization_strategy, name="xRayPreparation__optimization_strategy", curie=LAMBDABER.curie('optimization_strategy'),
                   model_uri=LAMBDABER.xRayPreparation__optimization_strategy, domain=None, range=Optional[str])

slots.xRayPreparation__optimized_condition = Slot(uri=LAMBDABER.optimized_condition, name="xRayPreparation__optimized_condition", curie=LAMBDABER.curie('optimized_condition'),
                   model_uri=LAMBDABER.xRayPreparation__optimized_condition, domain=None, range=Optional[str])

slots.xRayPreparation__crystal_size_um = Slot(uri=LAMBDABER.crystal_size_um, name="xRayPreparation__crystal_size_um", curie=LAMBDABER.curie('crystal_size_um'),
                   model_uri=LAMBDABER.xRayPreparation__crystal_size_um, domain=None, range=Optional[str])

slots.xRayPreparation__cryoprotectant = Slot(uri=LAMBDABER.cryoprotectant, name="xRayPreparation__cryoprotectant", curie=LAMBDABER.curie('cryoprotectant'),
                   model_uri=LAMBDABER.xRayPreparation__cryoprotectant, domain=None, range=Optional[str])

slots.xRayPreparation__cryoprotectant_concentration = Slot(uri=LAMBDABER.cryoprotectant_concentration, name="xRayPreparation__cryoprotectant_concentration", curie=LAMBDABER.curie('cryoprotectant_concentration'),
                   model_uri=LAMBDABER.xRayPreparation__cryoprotectant_concentration, domain=None, range=Optional[float])

slots.xRayPreparation__soak_compound = Slot(uri=LAMBDABER.soak_compound, name="xRayPreparation__soak_compound", curie=LAMBDABER.curie('soak_compound'),
                   model_uri=LAMBDABER.xRayPreparation__soak_compound, domain=None, range=Optional[str])

slots.xRayPreparation__soak_conditions = Slot(uri=LAMBDABER.soak_conditions, name="xRayPreparation__soak_conditions", curie=LAMBDABER.curie('soak_conditions'),
                   model_uri=LAMBDABER.xRayPreparation__soak_conditions, domain=None, range=Optional[str])

slots.xRayPreparation__mounting_method = Slot(uri=NSLS2.Mount_Type, name="xRayPreparation__mounting_method", curie=NSLS2.curie('Mount_Type'),
                   model_uri=LAMBDABER.xRayPreparation__mounting_method, domain=None, range=Optional[str])

slots.xRayPreparation__flash_cooling_method = Slot(uri=LAMBDABER.flash_cooling_method, name="xRayPreparation__flash_cooling_method", curie=LAMBDABER.curie('flash_cooling_method'),
                   model_uri=LAMBDABER.xRayPreparation__flash_cooling_method, domain=None, range=Optional[str])

slots.xRayPreparation__crystal_notes = Slot(uri=LAMBDABER.crystal_notes, name="xRayPreparation__crystal_notes", curie=LAMBDABER.curie('crystal_notes'),
                   model_uri=LAMBDABER.xRayPreparation__crystal_notes, domain=None, range=Optional[str])

slots.xRayPreparation__loop_size = Slot(uri=NSLS2.Loop_Size, name="xRayPreparation__loop_size", curie=NSLS2.curie('Loop_Size'),
                   model_uri=LAMBDABER.xRayPreparation__loop_size, domain=None, range=Optional[float])

slots.xRayPreparation__mounting_temperature = Slot(uri=NSLS2.Temperature, name="xRayPreparation__mounting_temperature", curie=NSLS2.curie('Temperature'),
                   model_uri=LAMBDABER.xRayPreparation__mounting_temperature, domain=None, range=Optional[float])

slots.sAXSPreparation__concentration_series = Slot(uri=LAMBDABER.concentration_series, name="sAXSPreparation__concentration_series", curie=LAMBDABER.curie('concentration_series'),
                   model_uri=LAMBDABER.sAXSPreparation__concentration_series, domain=None, range=Optional[Union[float, list[float]]])

slots.sAXSPreparation__buffer_matching_protocol = Slot(uri=LAMBDABER.buffer_matching_protocol, name="sAXSPreparation__buffer_matching_protocol", curie=LAMBDABER.curie('buffer_matching_protocol'),
                   model_uri=LAMBDABER.sAXSPreparation__buffer_matching_protocol, domain=None, range=Optional[str])

slots.sAXSPreparation__sample_cell_type = Slot(uri=LAMBDABER.sample_cell_type, name="sAXSPreparation__sample_cell_type", curie=LAMBDABER.curie('sample_cell_type'),
                   model_uri=LAMBDABER.sAXSPreparation__sample_cell_type, domain=None, range=Optional[str])

slots.sAXSPreparation__cell_path_length = Slot(uri=LAMBDABER.cell_path_length, name="sAXSPreparation__cell_path_length", curie=LAMBDABER.curie('cell_path_length'),
                   model_uri=LAMBDABER.sAXSPreparation__cell_path_length, domain=None, range=Optional[float])

slots.sAXSPreparation__temperature_control = Slot(uri=LAMBDABER.temperature_control, name="sAXSPreparation__temperature_control", curie=LAMBDABER.curie('temperature_control'),
                   model_uri=LAMBDABER.sAXSPreparation__temperature_control, domain=None, range=Optional[str])

slots.experimentalConditions__temperature = Slot(uri=LAMBDABER.temperature, name="experimentalConditions__temperature", curie=LAMBDABER.curie('temperature'),
                   model_uri=LAMBDABER.experimentalConditions__temperature, domain=None, range=Optional[float])

slots.experimentalConditions__humidity = Slot(uri=LAMBDABER.humidity, name="experimentalConditions__humidity", curie=LAMBDABER.curie('humidity'),
                   model_uri=LAMBDABER.experimentalConditions__humidity, domain=None, range=Optional[float])

slots.experimentalConditions__pressure = Slot(uri=LAMBDABER.pressure, name="experimentalConditions__pressure", curie=LAMBDABER.curie('pressure'),
                   model_uri=LAMBDABER.experimentalConditions__pressure, domain=None, range=Optional[float])

slots.experimentalConditions__atmosphere = Slot(uri=LAMBDABER.atmosphere, name="experimentalConditions__atmosphere", curie=LAMBDABER.curie('atmosphere'),
                   model_uri=LAMBDABER.experimentalConditions__atmosphere, domain=None, range=Optional[str])

slots.experimentalConditions__beam_energy = Slot(uri=LAMBDABER.beam_energy, name="experimentalConditions__beam_energy", curie=LAMBDABER.curie('beam_energy'),
                   model_uri=LAMBDABER.experimentalConditions__beam_energy, domain=None, range=Optional[float])

slots.experimentalConditions__exposure_time = Slot(uri=LAMBDABER.exposure_time, name="experimentalConditions__exposure_time", curie=LAMBDABER.curie('exposure_time'),
                   model_uri=LAMBDABER.experimentalConditions__exposure_time, domain=None, range=Optional[float])

slots.dataCollectionStrategy__collection_mode = Slot(uri=LAMBDABER.collection_mode, name="dataCollectionStrategy__collection_mode", curie=LAMBDABER.curie('collection_mode'),
                   model_uri=LAMBDABER.dataCollectionStrategy__collection_mode, domain=None, range=Optional[Union[str, "CollectionModeEnum"]])

slots.dataCollectionStrategy__total_frames = Slot(uri=LAMBDABER.total_frames, name="dataCollectionStrategy__total_frames", curie=LAMBDABER.curie('total_frames'),
                   model_uri=LAMBDABER.dataCollectionStrategy__total_frames, domain=None, range=Optional[int])

slots.dataCollectionStrategy__frame_rate = Slot(uri=LAMBDABER.frame_rate, name="dataCollectionStrategy__frame_rate", curie=LAMBDABER.curie('frame_rate'),
                   model_uri=LAMBDABER.dataCollectionStrategy__frame_rate, domain=None, range=Optional[float])

slots.dataCollectionStrategy__total_dose = Slot(uri=LAMBDABER.total_dose, name="dataCollectionStrategy__total_dose", curie=LAMBDABER.curie('total_dose'),
                   model_uri=LAMBDABER.dataCollectionStrategy__total_dose, domain=None, range=Optional[float])

slots.dataCollectionStrategy__dose_per_frame = Slot(uri=LAMBDABER.dose_per_frame, name="dataCollectionStrategy__dose_per_frame", curie=LAMBDABER.curie('dose_per_frame'),
                   model_uri=LAMBDABER.dataCollectionStrategy__dose_per_frame, domain=None, range=Optional[float])

slots.dataCollectionStrategy__wavelength_a = Slot(uri=LAMBDABER.wavelength_a, name="dataCollectionStrategy__wavelength_a", curie=LAMBDABER.curie('wavelength_a'),
                   model_uri=LAMBDABER.dataCollectionStrategy__wavelength_a, domain=None, range=Optional[float])

slots.dataCollectionStrategy__detector_mode = Slot(uri=LAMBDABER.detector_mode, name="dataCollectionStrategy__detector_mode", curie=LAMBDABER.curie('detector_mode'),
                   model_uri=LAMBDABER.dataCollectionStrategy__detector_mode, domain=None, range=Optional[Union[str, "DetectorModeEnum"]])

slots.dataCollectionStrategy__pixel_size_calibrated = Slot(uri=LAMBDABER.pixel_size_calibrated, name="dataCollectionStrategy__pixel_size_calibrated", curie=LAMBDABER.curie('pixel_size_calibrated'),
                   model_uri=LAMBDABER.dataCollectionStrategy__pixel_size_calibrated, domain=None, range=Optional[float])

slots.dataCollectionStrategy__detector_distance_mm = Slot(uri=LAMBDABER.detector_distance_mm, name="dataCollectionStrategy__detector_distance_mm", curie=LAMBDABER.curie('detector_distance_mm'),
                   model_uri=LAMBDABER.dataCollectionStrategy__detector_distance_mm, domain=None, range=Optional[float])

slots.dataCollectionStrategy__beam_center_x_px = Slot(uri=LAMBDABER.beam_center_x_px, name="dataCollectionStrategy__beam_center_x_px", curie=LAMBDABER.curie('beam_center_x_px'),
                   model_uri=LAMBDABER.dataCollectionStrategy__beam_center_x_px, domain=None, range=Optional[int])

slots.dataCollectionStrategy__beam_center_y_px = Slot(uri=LAMBDABER.beam_center_y_px, name="dataCollectionStrategy__beam_center_y_px", curie=LAMBDABER.curie('beam_center_y_px'),
                   model_uri=LAMBDABER.dataCollectionStrategy__beam_center_y_px, domain=None, range=Optional[int])

slots.dataCollectionStrategy__beam_size_um = Slot(uri=LAMBDABER.beam_size_um, name="dataCollectionStrategy__beam_size_um", curie=LAMBDABER.curie('beam_size_um'),
                   model_uri=LAMBDABER.dataCollectionStrategy__beam_size_um, domain=None, range=Optional[float])

slots.dataCollectionStrategy__flux_photons_per_s = Slot(uri=LAMBDABER.flux_photons_per_s, name="dataCollectionStrategy__flux_photons_per_s", curie=LAMBDABER.curie('flux_photons_per_s'),
                   model_uri=LAMBDABER.dataCollectionStrategy__flux_photons_per_s, domain=None, range=Optional[float])

slots.dataCollectionStrategy__transmission_percent = Slot(uri=LAMBDABER.transmission_percent, name="dataCollectionStrategy__transmission_percent", curie=LAMBDABER.curie('transmission_percent'),
                   model_uri=LAMBDABER.dataCollectionStrategy__transmission_percent, domain=None, range=Optional[float])

slots.dataCollectionStrategy__attenuator = Slot(uri=LAMBDABER.attenuator, name="dataCollectionStrategy__attenuator", curie=LAMBDABER.curie('attenuator'),
                   model_uri=LAMBDABER.dataCollectionStrategy__attenuator, domain=None, range=Optional[str])

slots.dataCollectionStrategy__temperature_k = Slot(uri=LAMBDABER.temperature_k, name="dataCollectionStrategy__temperature_k", curie=LAMBDABER.curie('temperature_k'),
                   model_uri=LAMBDABER.dataCollectionStrategy__temperature_k, domain=None, range=Optional[float])

slots.dataCollectionStrategy__oscillation_per_image_deg = Slot(uri=LAMBDABER.oscillation_per_image_deg, name="dataCollectionStrategy__oscillation_per_image_deg", curie=LAMBDABER.curie('oscillation_per_image_deg'),
                   model_uri=LAMBDABER.dataCollectionStrategy__oscillation_per_image_deg, domain=None, range=Optional[float])

slots.dataCollectionStrategy__total_rotation_deg = Slot(uri=LAMBDABER.total_rotation_deg, name="dataCollectionStrategy__total_rotation_deg", curie=LAMBDABER.curie('total_rotation_deg'),
                   model_uri=LAMBDABER.dataCollectionStrategy__total_rotation_deg, domain=None, range=Optional[float])

slots.dataCollectionStrategy__strategy_notes = Slot(uri=LAMBDABER.strategy_notes, name="dataCollectionStrategy__strategy_notes", curie=LAMBDABER.curie('strategy_notes'),
                   model_uri=LAMBDABER.dataCollectionStrategy__strategy_notes, domain=None, range=Optional[str])

slots.qualityMetrics__resolution = Slot(uri=LAMBDABER.resolution, name="qualityMetrics__resolution", curie=LAMBDABER.curie('resolution'),
                   model_uri=LAMBDABER.qualityMetrics__resolution, domain=None, range=Optional[float])

slots.qualityMetrics__resolution_high_shell_a = Slot(uri=LAMBDABER.resolution_high_shell_a, name="qualityMetrics__resolution_high_shell_a", curie=LAMBDABER.curie('resolution_high_shell_a'),
                   model_uri=LAMBDABER.qualityMetrics__resolution_high_shell_a, domain=None, range=Optional[float])

slots.qualityMetrics__resolution_low_a = Slot(uri=LAMBDABER.resolution_low_a, name="qualityMetrics__resolution_low_a", curie=LAMBDABER.curie('resolution_low_a'),
                   model_uri=LAMBDABER.qualityMetrics__resolution_low_a, domain=None, range=Optional[float])

slots.qualityMetrics__completeness = Slot(uri=LAMBDABER.completeness, name="qualityMetrics__completeness", curie=LAMBDABER.curie('completeness'),
                   model_uri=LAMBDABER.qualityMetrics__completeness, domain=None, range=Optional[float])

slots.qualityMetrics__completeness_high_res_shell_percent = Slot(uri=LAMBDABER.completeness_high_res_shell_percent, name="qualityMetrics__completeness_high_res_shell_percent", curie=LAMBDABER.curie('completeness_high_res_shell_percent'),
                   model_uri=LAMBDABER.qualityMetrics__completeness_high_res_shell_percent, domain=None, range=Optional[float])

slots.qualityMetrics__signal_to_noise = Slot(uri=LAMBDABER.signal_to_noise, name="qualityMetrics__signal_to_noise", curie=LAMBDABER.curie('signal_to_noise'),
                   model_uri=LAMBDABER.qualityMetrics__signal_to_noise, domain=None, range=Optional[float])

slots.qualityMetrics__mean_i_over_sigma_i = Slot(uri=LAMBDABER.mean_i_over_sigma_i, name="qualityMetrics__mean_i_over_sigma_i", curie=LAMBDABER.curie('mean_i_over_sigma_i'),
                   model_uri=LAMBDABER.qualityMetrics__mean_i_over_sigma_i, domain=None, range=Optional[float])

slots.qualityMetrics__space_group = Slot(uri=LAMBDABER.space_group, name="qualityMetrics__space_group", curie=LAMBDABER.curie('space_group'),
                   model_uri=LAMBDABER.qualityMetrics__space_group, domain=None, range=Optional[str])

slots.qualityMetrics__unit_cell_a = Slot(uri=LAMBDABER.unit_cell_a, name="qualityMetrics__unit_cell_a", curie=LAMBDABER.curie('unit_cell_a'),
                   model_uri=LAMBDABER.qualityMetrics__unit_cell_a, domain=None, range=Optional[float])

slots.qualityMetrics__unit_cell_b = Slot(uri=LAMBDABER.unit_cell_b, name="qualityMetrics__unit_cell_b", curie=LAMBDABER.curie('unit_cell_b'),
                   model_uri=LAMBDABER.qualityMetrics__unit_cell_b, domain=None, range=Optional[float])

slots.qualityMetrics__unit_cell_c = Slot(uri=LAMBDABER.unit_cell_c, name="qualityMetrics__unit_cell_c", curie=LAMBDABER.curie('unit_cell_c'),
                   model_uri=LAMBDABER.qualityMetrics__unit_cell_c, domain=None, range=Optional[float])

slots.qualityMetrics__unit_cell_alpha = Slot(uri=LAMBDABER.unit_cell_alpha, name="qualityMetrics__unit_cell_alpha", curie=LAMBDABER.curie('unit_cell_alpha'),
                   model_uri=LAMBDABER.qualityMetrics__unit_cell_alpha, domain=None, range=Optional[float])

slots.qualityMetrics__unit_cell_beta = Slot(uri=LAMBDABER.unit_cell_beta, name="qualityMetrics__unit_cell_beta", curie=LAMBDABER.curie('unit_cell_beta'),
                   model_uri=LAMBDABER.qualityMetrics__unit_cell_beta, domain=None, range=Optional[float])

slots.qualityMetrics__unit_cell_gamma = Slot(uri=LAMBDABER.unit_cell_gamma, name="qualityMetrics__unit_cell_gamma", curie=LAMBDABER.curie('unit_cell_gamma'),
                   model_uri=LAMBDABER.qualityMetrics__unit_cell_gamma, domain=None, range=Optional[float])

slots.qualityMetrics__multiplicity = Slot(uri=LAMBDABER.multiplicity, name="qualityMetrics__multiplicity", curie=LAMBDABER.curie('multiplicity'),
                   model_uri=LAMBDABER.qualityMetrics__multiplicity, domain=None, range=Optional[float])

slots.qualityMetrics__cc_half = Slot(uri=LAMBDABER.cc_half, name="qualityMetrics__cc_half", curie=LAMBDABER.curie('cc_half'),
                   model_uri=LAMBDABER.qualityMetrics__cc_half, domain=None, range=Optional[float])

slots.qualityMetrics__r_merge = Slot(uri=LAMBDABER.r_merge, name="qualityMetrics__r_merge", curie=LAMBDABER.curie('r_merge'),
                   model_uri=LAMBDABER.qualityMetrics__r_merge, domain=None, range=Optional[float])

slots.qualityMetrics__r_pim = Slot(uri=LAMBDABER.r_pim, name="qualityMetrics__r_pim", curie=LAMBDABER.curie('r_pim'),
                   model_uri=LAMBDABER.qualityMetrics__r_pim, domain=None, range=Optional[float])

slots.qualityMetrics__wilson_b_factor_a2 = Slot(uri=LAMBDABER.wilson_b_factor_a2, name="qualityMetrics__wilson_b_factor_a2", curie=LAMBDABER.curie('wilson_b_factor_a2'),
                   model_uri=LAMBDABER.qualityMetrics__wilson_b_factor_a2, domain=None, range=Optional[float])

slots.qualityMetrics__anomalous_used = Slot(uri=LAMBDABER.anomalous_used, name="qualityMetrics__anomalous_used", curie=LAMBDABER.curie('anomalous_used'),
                   model_uri=LAMBDABER.qualityMetrics__anomalous_used, domain=None, range=Optional[Union[bool, Bool]])

slots.qualityMetrics__anom_corr = Slot(uri=LAMBDABER.anom_corr, name="qualityMetrics__anom_corr", curie=LAMBDABER.curie('anom_corr'),
                   model_uri=LAMBDABER.qualityMetrics__anom_corr, domain=None, range=Optional[float])

slots.qualityMetrics__anom_sig_ano = Slot(uri=LAMBDABER.anom_sig_ano, name="qualityMetrics__anom_sig_ano", curie=LAMBDABER.curie('anom_sig_ano'),
                   model_uri=LAMBDABER.qualityMetrics__anom_sig_ano, domain=None, range=Optional[float])

slots.qualityMetrics__r_work = Slot(uri=LAMBDABER.r_work, name="qualityMetrics__r_work", curie=LAMBDABER.curie('r_work'),
                   model_uri=LAMBDABER.qualityMetrics__r_work, domain=None, range=Optional[float])

slots.qualityMetrics__r_free = Slot(uri=LAMBDABER.r_free, name="qualityMetrics__r_free", curie=LAMBDABER.curie('r_free'),
                   model_uri=LAMBDABER.qualityMetrics__r_free, domain=None, range=Optional[float])

slots.qualityMetrics__ramachandran_favored_percent = Slot(uri=LAMBDABER.ramachandran_favored_percent, name="qualityMetrics__ramachandran_favored_percent", curie=LAMBDABER.curie('ramachandran_favored_percent'),
                   model_uri=LAMBDABER.qualityMetrics__ramachandran_favored_percent, domain=None, range=Optional[float])

slots.qualityMetrics__ramachandran_outliers_percent = Slot(uri=LAMBDABER.ramachandran_outliers_percent, name="qualityMetrics__ramachandran_outliers_percent", curie=LAMBDABER.curie('ramachandran_outliers_percent'),
                   model_uri=LAMBDABER.qualityMetrics__ramachandran_outliers_percent, domain=None, range=Optional[float])

slots.qualityMetrics__clashscore = Slot(uri=LAMBDABER.clashscore, name="qualityMetrics__clashscore", curie=LAMBDABER.curie('clashscore'),
                   model_uri=LAMBDABER.qualityMetrics__clashscore, domain=None, range=Optional[float])

slots.qualityMetrics__molprobity_score = Slot(uri=LAMBDABER.molprobity_score, name="qualityMetrics__molprobity_score", curie=LAMBDABER.curie('molprobity_score'),
                   model_uri=LAMBDABER.qualityMetrics__molprobity_score, domain=None, range=Optional[float])

slots.qualityMetrics__average_b_factor_a2 = Slot(uri=LAMBDABER.average_b_factor_a2, name="qualityMetrics__average_b_factor_a2", curie=LAMBDABER.curie('average_b_factor_a2'),
                   model_uri=LAMBDABER.qualityMetrics__average_b_factor_a2, domain=None, range=Optional[float])

slots.qualityMetrics__i_zero = Slot(uri=LAMBDABER.i_zero, name="qualityMetrics__i_zero", curie=LAMBDABER.curie('i_zero'),
                   model_uri=LAMBDABER.qualityMetrics__i_zero, domain=None, range=Optional[float])

slots.qualityMetrics__rg = Slot(uri=LAMBDABER.rg, name="qualityMetrics__rg", curie=LAMBDABER.curie('rg'),
                   model_uri=LAMBDABER.qualityMetrics__rg, domain=None, range=Optional[float])

slots.qualityMetrics__r_factor = Slot(uri=LAMBDABER.r_factor, name="qualityMetrics__r_factor", curie=LAMBDABER.curie('r_factor'),
                   model_uri=LAMBDABER.qualityMetrics__r_factor, domain=None, range=Optional[float])

slots.computeResources__cpu_hours = Slot(uri=LAMBDABER.cpu_hours, name="computeResources__cpu_hours", curie=LAMBDABER.curie('cpu_hours'),
                   model_uri=LAMBDABER.computeResources__cpu_hours, domain=None, range=Optional[float])

slots.computeResources__gpu_hours = Slot(uri=LAMBDABER.gpu_hours, name="computeResources__gpu_hours", curie=LAMBDABER.curie('gpu_hours'),
                   model_uri=LAMBDABER.computeResources__gpu_hours, domain=None, range=Optional[float])

slots.computeResources__memory_gb = Slot(uri=LAMBDABER.memory_gb, name="computeResources__memory_gb", curie=LAMBDABER.curie('memory_gb'),
                   model_uri=LAMBDABER.computeResources__memory_gb, domain=None, range=Optional[float])

slots.computeResources__storage_gb = Slot(uri=LAMBDABER.storage_gb, name="computeResources__storage_gb", curie=LAMBDABER.curie('storage_gb'),
                   model_uri=LAMBDABER.computeResources__storage_gb, domain=None, range=Optional[float])

slots.proteinAnnotation__protein_id = Slot(uri=LAMBDABER['functional_annotation/protein_id'], name="proteinAnnotation__protein_id", curie=LAMBDABER.curie('functional_annotation/protein_id'),
                   model_uri=LAMBDABER.proteinAnnotation__protein_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$'))

slots.proteinAnnotation__pdb_entry = Slot(uri=LAMBDABER['functional_annotation/pdb_entry'], name="proteinAnnotation__pdb_entry", curie=LAMBDABER.curie('functional_annotation/pdb_entry'),
                   model_uri=LAMBDABER.proteinAnnotation__pdb_entry, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9][A-Za-z0-9]{3}$'))

slots.proteinAnnotation__chain_id = Slot(uri=LAMBDABER['functional_annotation/chain_id'], name="proteinAnnotation__chain_id", curie=LAMBDABER.curie('functional_annotation/chain_id'),
                   model_uri=LAMBDABER.proteinAnnotation__chain_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9]+$'))

slots.proteinAnnotation__residue_range = Slot(uri=LAMBDABER['functional_annotation/residue_range'], name="proteinAnnotation__residue_range", curie=LAMBDABER.curie('functional_annotation/residue_range'),
                   model_uri=LAMBDABER.proteinAnnotation__residue_range, domain=None, range=Optional[str])

slots.proteinAnnotation__confidence_score = Slot(uri=LAMBDABER['functional_annotation/confidence_score'], name="proteinAnnotation__confidence_score", curie=LAMBDABER.curie('functional_annotation/confidence_score'),
                   model_uri=LAMBDABER.proteinAnnotation__confidence_score, domain=None, range=Optional[float])

slots.proteinAnnotation__evidence_type = Slot(uri=LAMBDABER['functional_annotation/evidence_type'], name="proteinAnnotation__evidence_type", curie=LAMBDABER.curie('functional_annotation/evidence_type'),
                   model_uri=LAMBDABER.proteinAnnotation__evidence_type, domain=None, range=Optional[Union[str, "EvidenceTypeEnum"]])

slots.proteinAnnotation__evidence_code = Slot(uri=LAMBDABER['functional_annotation/evidence_code'], name="proteinAnnotation__evidence_code", curie=LAMBDABER.curie('functional_annotation/evidence_code'),
                   model_uri=LAMBDABER.proteinAnnotation__evidence_code, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.proteinAnnotation__source_database = Slot(uri=LAMBDABER['functional_annotation/source_database'], name="proteinAnnotation__source_database", curie=LAMBDABER.curie('functional_annotation/source_database'),
                   model_uri=LAMBDABER.proteinAnnotation__source_database, domain=None, range=Optional[Union[str, "AnnotationSourceEnum"]])

slots.proteinAnnotation__annotation_method = Slot(uri=LAMBDABER['functional_annotation/annotation_method'], name="proteinAnnotation__annotation_method", curie=LAMBDABER.curie('functional_annotation/annotation_method'),
                   model_uri=LAMBDABER.proteinAnnotation__annotation_method, domain=None, range=Optional[str])

slots.proteinAnnotation__publication_ids = Slot(uri=LAMBDABER['functional_annotation/publication_ids'], name="proteinAnnotation__publication_ids", curie=LAMBDABER.curie('functional_annotation/publication_ids'),
                   model_uri=LAMBDABER.proteinAnnotation__publication_ids, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^PMID:[0-9]+$'))

slots.functionalSite__site_type = Slot(uri=LAMBDABER['functional_annotation/site_type'], name="functionalSite__site_type", curie=LAMBDABER.curie('functional_annotation/site_type'),
                   model_uri=LAMBDABER.functionalSite__site_type, domain=None, range=Union[str, "FunctionalSiteTypeEnum"])

slots.functionalSite__site_name = Slot(uri=LAMBDABER['functional_annotation/site_name'], name="functionalSite__site_name", curie=LAMBDABER.curie('functional_annotation/site_name'),
                   model_uri=LAMBDABER.functionalSite__site_name, domain=None, range=Optional[str])

slots.functionalSite__residues = Slot(uri=LAMBDABER['functional_annotation/residues'], name="functionalSite__residues", curie=LAMBDABER.curie('functional_annotation/residues'),
                   model_uri=LAMBDABER.functionalSite__residues, domain=None, range=Optional[Union[str, list[str]]])

slots.functionalSite__ligand_interactions = Slot(uri=LAMBDABER['functional_annotation/ligand_interactions'], name="functionalSite__ligand_interactions", curie=LAMBDABER.curie('functional_annotation/ligand_interactions'),
                   model_uri=LAMBDABER.functionalSite__ligand_interactions, domain=None, range=Optional[Union[Union[dict, LigandInteraction], list[Union[dict, LigandInteraction]]]])

slots.functionalSite__conservation_score = Slot(uri=LAMBDABER['functional_annotation/conservation_score'], name="functionalSite__conservation_score", curie=LAMBDABER.curie('functional_annotation/conservation_score'),
                   model_uri=LAMBDABER.functionalSite__conservation_score, domain=None, range=Optional[float])

slots.functionalSite__functional_importance = Slot(uri=LAMBDABER['functional_annotation/functional_importance'], name="functionalSite__functional_importance", curie=LAMBDABER.curie('functional_annotation/functional_importance'),
                   model_uri=LAMBDABER.functionalSite__functional_importance, domain=None, range=Optional[str])

slots.functionalSite__go_terms = Slot(uri=LAMBDABER['functional_annotation/go_terms'], name="functionalSite__go_terms", curie=LAMBDABER.curie('functional_annotation/go_terms'),
                   model_uri=LAMBDABER.functionalSite__go_terms, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.functionalSite__ec_number = Slot(uri=LAMBDABER['functional_annotation/ec_number'], name="functionalSite__ec_number", curie=LAMBDABER.curie('functional_annotation/ec_number'),
                   model_uri=LAMBDABER.functionalSite__ec_number, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'))

slots.structuralFeature__feature_type = Slot(uri=LAMBDABER['functional_annotation/feature_type'], name="structuralFeature__feature_type", curie=LAMBDABER.curie('functional_annotation/feature_type'),
                   model_uri=LAMBDABER.structuralFeature__feature_type, domain=None, range=Union[str, "StructuralFeatureTypeEnum"])

slots.structuralFeature__secondary_structure = Slot(uri=LAMBDABER['functional_annotation/secondary_structure'], name="structuralFeature__secondary_structure", curie=LAMBDABER.curie('functional_annotation/secondary_structure'),
                   model_uri=LAMBDABER.structuralFeature__secondary_structure, domain=None, range=Optional[Union[str, "SecondaryStructureEnum"]])

slots.structuralFeature__solvent_accessibility = Slot(uri=LAMBDABER['functional_annotation/solvent_accessibility'], name="structuralFeature__solvent_accessibility", curie=LAMBDABER.curie('functional_annotation/solvent_accessibility'),
                   model_uri=LAMBDABER.structuralFeature__solvent_accessibility, domain=None, range=Optional[float])

slots.structuralFeature__backbone_flexibility = Slot(uri=LAMBDABER['functional_annotation/backbone_flexibility'], name="structuralFeature__backbone_flexibility", curie=LAMBDABER.curie('functional_annotation/backbone_flexibility'),
                   model_uri=LAMBDABER.structuralFeature__backbone_flexibility, domain=None, range=Optional[float])

slots.structuralFeature__disorder_probability = Slot(uri=LAMBDABER['functional_annotation/disorder_probability'], name="structuralFeature__disorder_probability", curie=LAMBDABER.curie('functional_annotation/disorder_probability'),
                   model_uri=LAMBDABER.structuralFeature__disorder_probability, domain=None, range=Optional[float])

slots.structuralFeature__conformational_state = Slot(uri=LAMBDABER['functional_annotation/conformational_state'], name="structuralFeature__conformational_state", curie=LAMBDABER.curie('functional_annotation/conformational_state'),
                   model_uri=LAMBDABER.structuralFeature__conformational_state, domain=None, range=Optional[Union[str, "ConformationalStateEnum"]])

slots.structuralFeature__structural_motif = Slot(uri=LAMBDABER['functional_annotation/structural_motif'], name="structuralFeature__structural_motif", curie=LAMBDABER.curie('functional_annotation/structural_motif'),
                   model_uri=LAMBDABER.structuralFeature__structural_motif, domain=None, range=Optional[str])

slots.structuralFeature__domain_assignment = Slot(uri=LAMBDABER['functional_annotation/domain_assignment'], name="structuralFeature__domain_assignment", curie=LAMBDABER.curie('functional_annotation/domain_assignment'),
                   model_uri=LAMBDABER.structuralFeature__domain_assignment, domain=None, range=Optional[str])

slots.structuralFeature__domain_id = Slot(uri=LAMBDABER['functional_annotation/domain_id'], name="structuralFeature__domain_id", curie=LAMBDABER.curie('functional_annotation/domain_id'),
                   model_uri=LAMBDABER.structuralFeature__domain_id, domain=None, range=Optional[str])

slots.ligandInteraction__ligand_id = Slot(uri=LAMBDABER['functional_annotation/ligand_id'], name="ligandInteraction__ligand_id", curie=LAMBDABER.curie('functional_annotation/ligand_id'),
                   model_uri=LAMBDABER.ligandInteraction__ligand_id, domain=None, range=str)

slots.ligandInteraction__ligand_name = Slot(uri=LAMBDABER['functional_annotation/ligand_name'], name="ligandInteraction__ligand_name", curie=LAMBDABER.curie('functional_annotation/ligand_name'),
                   model_uri=LAMBDABER.ligandInteraction__ligand_name, domain=None, range=str)

slots.ligandInteraction__ligand_smiles = Slot(uri=LAMBDABER['functional_annotation/ligand_smiles'], name="ligandInteraction__ligand_smiles", curie=LAMBDABER.curie('functional_annotation/ligand_smiles'),
                   model_uri=LAMBDABER.ligandInteraction__ligand_smiles, domain=None, range=Optional[str])

slots.ligandInteraction__binding_affinity = Slot(uri=LAMBDABER['functional_annotation/binding_affinity'], name="ligandInteraction__binding_affinity", curie=LAMBDABER.curie('functional_annotation/binding_affinity'),
                   model_uri=LAMBDABER.ligandInteraction__binding_affinity, domain=None, range=Optional[float])

slots.ligandInteraction__binding_affinity_type = Slot(uri=LAMBDABER['functional_annotation/binding_affinity_type'], name="ligandInteraction__binding_affinity_type", curie=LAMBDABER.curie('functional_annotation/binding_affinity_type'),
                   model_uri=LAMBDABER.ligandInteraction__binding_affinity_type, domain=None, range=Optional[Union[str, "BindingAffinityTypeEnum"]])

slots.ligandInteraction__binding_affinity_unit = Slot(uri=LAMBDABER['functional_annotation/binding_affinity_unit'], name="ligandInteraction__binding_affinity_unit", curie=LAMBDABER.curie('functional_annotation/binding_affinity_unit'),
                   model_uri=LAMBDABER.ligandInteraction__binding_affinity_unit, domain=None, range=Optional[Union[str, "AffinityUnitEnum"]])

slots.ligandInteraction__interaction_type = Slot(uri=LAMBDABER['functional_annotation/interaction_type'], name="ligandInteraction__interaction_type", curie=LAMBDABER.curie('functional_annotation/interaction_type'),
                   model_uri=LAMBDABER.ligandInteraction__interaction_type, domain=None, range=Optional[Union[str, "InteractionTypeEnum"]])

slots.ligandInteraction__binding_site_residues = Slot(uri=LAMBDABER['functional_annotation/binding_site_residues'], name="ligandInteraction__binding_site_residues", curie=LAMBDABER.curie('functional_annotation/binding_site_residues'),
                   model_uri=LAMBDABER.ligandInteraction__binding_site_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.ligandInteraction__is_cofactor = Slot(uri=LAMBDABER['functional_annotation/is_cofactor'], name="ligandInteraction__is_cofactor", curie=LAMBDABER.curie('functional_annotation/is_cofactor'),
                   model_uri=LAMBDABER.ligandInteraction__is_cofactor, domain=None, range=Optional[Union[bool, Bool]])

slots.ligandInteraction__is_drug_like = Slot(uri=LAMBDABER['functional_annotation/is_drug_like'], name="ligandInteraction__is_drug_like", curie=LAMBDABER.curie('functional_annotation/is_drug_like'),
                   model_uri=LAMBDABER.ligandInteraction__is_drug_like, domain=None, range=Optional[Union[bool, Bool]])

slots.ligandInteraction__druggability_score = Slot(uri=LAMBDABER['functional_annotation/druggability_score'], name="ligandInteraction__druggability_score", curie=LAMBDABER.curie('functional_annotation/druggability_score'),
                   model_uri=LAMBDABER.ligandInteraction__druggability_score, domain=None, range=Optional[float])

slots.ligandInteraction__interaction_distance = Slot(uri=LAMBDABER['functional_annotation/interaction_distance'], name="ligandInteraction__interaction_distance", curie=LAMBDABER.curie('functional_annotation/interaction_distance'),
                   model_uri=LAMBDABER.ligandInteraction__interaction_distance, domain=None, range=Optional[float])

slots.proteinProteinInteraction__partner_protein_id = Slot(uri=LAMBDABER['functional_annotation/partner_protein_id'], name="proteinProteinInteraction__partner_protein_id", curie=LAMBDABER.curie('functional_annotation/partner_protein_id'),
                   model_uri=LAMBDABER.proteinProteinInteraction__partner_protein_id, domain=None, range=str)

slots.proteinProteinInteraction__partner_chain_id = Slot(uri=LAMBDABER['functional_annotation/partner_chain_id'], name="proteinProteinInteraction__partner_chain_id", curie=LAMBDABER.curie('functional_annotation/partner_chain_id'),
                   model_uri=LAMBDABER.proteinProteinInteraction__partner_chain_id, domain=None, range=Optional[str])

slots.proteinProteinInteraction__interface_residues = Slot(uri=LAMBDABER['functional_annotation/interface_residues'], name="proteinProteinInteraction__interface_residues", curie=LAMBDABER.curie('functional_annotation/interface_residues'),
                   model_uri=LAMBDABER.proteinProteinInteraction__interface_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.proteinProteinInteraction__partner_interface_residues = Slot(uri=LAMBDABER['functional_annotation/partner_interface_residues'], name="proteinProteinInteraction__partner_interface_residues", curie=LAMBDABER.curie('functional_annotation/partner_interface_residues'),
                   model_uri=LAMBDABER.proteinProteinInteraction__partner_interface_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.proteinProteinInteraction__interface_area = Slot(uri=LAMBDABER['functional_annotation/interface_area'], name="proteinProteinInteraction__interface_area", curie=LAMBDABER.curie('functional_annotation/interface_area'),
                   model_uri=LAMBDABER.proteinProteinInteraction__interface_area, domain=None, range=Optional[float])

slots.proteinProteinInteraction__binding_energy = Slot(uri=LAMBDABER['functional_annotation/binding_energy'], name="proteinProteinInteraction__binding_energy", curie=LAMBDABER.curie('functional_annotation/binding_energy'),
                   model_uri=LAMBDABER.proteinProteinInteraction__binding_energy, domain=None, range=Optional[float])

slots.proteinProteinInteraction__dissociation_constant = Slot(uri=LAMBDABER['functional_annotation/dissociation_constant'], name="proteinProteinInteraction__dissociation_constant", curie=LAMBDABER.curie('functional_annotation/dissociation_constant'),
                   model_uri=LAMBDABER.proteinProteinInteraction__dissociation_constant, domain=None, range=Optional[float])

slots.proteinProteinInteraction__complex_stability = Slot(uri=LAMBDABER['functional_annotation/complex_stability'], name="proteinProteinInteraction__complex_stability", curie=LAMBDABER.curie('functional_annotation/complex_stability'),
                   model_uri=LAMBDABER.proteinProteinInteraction__complex_stability, domain=None, range=Optional[Union[str, "ComplexStabilityEnum"]])

slots.proteinProteinInteraction__biological_assembly = Slot(uri=LAMBDABER['functional_annotation/biological_assembly'], name="proteinProteinInteraction__biological_assembly", curie=LAMBDABER.curie('functional_annotation/biological_assembly'),
                   model_uri=LAMBDABER.proteinProteinInteraction__biological_assembly, domain=None, range=Optional[Union[bool, Bool]])

slots.proteinProteinInteraction__interaction_evidence = Slot(uri=LAMBDABER['functional_annotation/interaction_evidence'], name="proteinProteinInteraction__interaction_evidence", curie=LAMBDABER.curie('functional_annotation/interaction_evidence'),
                   model_uri=LAMBDABER.proteinProteinInteraction__interaction_evidence, domain=None, range=Optional[Union[Union[str, "InteractionEvidenceEnum"], list[Union[str, "InteractionEvidenceEnum"]]]])

slots.mutationEffect__mutation = Slot(uri=LAMBDABER['functional_annotation/mutation'], name="mutationEffect__mutation", curie=LAMBDABER.curie('functional_annotation/mutation'),
                   model_uri=LAMBDABER.mutationEffect__mutation, domain=None, range=str,
                   pattern=re.compile(r'^[A-Z][0-9]+[A-Z]$'))

slots.mutationEffect__mutation_type = Slot(uri=LAMBDABER['functional_annotation/mutation_type'], name="mutationEffect__mutation_type", curie=LAMBDABER.curie('functional_annotation/mutation_type'),
                   model_uri=LAMBDABER.mutationEffect__mutation_type, domain=None, range=Optional[Union[str, "MutationTypeEnum"]])

slots.mutationEffect__effect_on_stability = Slot(uri=LAMBDABER['functional_annotation/effect_on_stability'], name="mutationEffect__effect_on_stability", curie=LAMBDABER.curie('functional_annotation/effect_on_stability'),
                   model_uri=LAMBDABER.mutationEffect__effect_on_stability, domain=None, range=Optional[Union[str, "StabilityEffectEnum"]])

slots.mutationEffect__delta_delta_g = Slot(uri=LAMBDABER['functional_annotation/delta_delta_g'], name="mutationEffect__delta_delta_g", curie=LAMBDABER.curie('functional_annotation/delta_delta_g'),
                   model_uri=LAMBDABER.mutationEffect__delta_delta_g, domain=None, range=Optional[float])

slots.mutationEffect__effect_on_function = Slot(uri=LAMBDABER['functional_annotation/effect_on_function'], name="mutationEffect__effect_on_function", curie=LAMBDABER.curie('functional_annotation/effect_on_function'),
                   model_uri=LAMBDABER.mutationEffect__effect_on_function, domain=None, range=Optional[Union[str, "FunctionalEffectEnum"]])

slots.mutationEffect__functional_impact_description = Slot(uri=LAMBDABER['functional_annotation/functional_impact_description'], name="mutationEffect__functional_impact_description", curie=LAMBDABER.curie('functional_annotation/functional_impact_description'),
                   model_uri=LAMBDABER.mutationEffect__functional_impact_description, domain=None, range=Optional[str])

slots.mutationEffect__disease_association = Slot(uri=LAMBDABER['functional_annotation/disease_association'], name="mutationEffect__disease_association", curie=LAMBDABER.curie('functional_annotation/disease_association'),
                   model_uri=LAMBDABER.mutationEffect__disease_association, domain=None, range=Optional[str])

slots.mutationEffect__omim_id = Slot(uri=LAMBDABER['functional_annotation/omim_id'], name="mutationEffect__omim_id", curie=LAMBDABER.curie('functional_annotation/omim_id'),
                   model_uri=LAMBDABER.mutationEffect__omim_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9]{6}$'))

slots.mutationEffect__clinical_significance = Slot(uri=LAMBDABER['functional_annotation/clinical_significance'], name="mutationEffect__clinical_significance", curie=LAMBDABER.curie('functional_annotation/clinical_significance'),
                   model_uri=LAMBDABER.mutationEffect__clinical_significance, domain=None, range=Optional[Union[str, "ClinicalSignificanceEnum"]])

slots.mutationEffect__allele_frequency = Slot(uri=LAMBDABER['functional_annotation/allele_frequency'], name="mutationEffect__allele_frequency", curie=LAMBDABER.curie('functional_annotation/allele_frequency'),
                   model_uri=LAMBDABER.mutationEffect__allele_frequency, domain=None, range=Optional[float])

slots.biophysicalProperty__property_type = Slot(uri=LAMBDABER['functional_annotation/property_type'], name="biophysicalProperty__property_type", curie=LAMBDABER.curie('functional_annotation/property_type'),
                   model_uri=LAMBDABER.biophysicalProperty__property_type, domain=None, range=Union[str, "BiophysicalPropertyEnum"])

slots.biophysicalProperty__value = Slot(uri=LAMBDABER['functional_annotation/value'], name="biophysicalProperty__value", curie=LAMBDABER.curie('functional_annotation/value'),
                   model_uri=LAMBDABER.biophysicalProperty__value, domain=None, range=float)

slots.biophysicalProperty__unit = Slot(uri=LAMBDABER['functional_annotation/unit'], name="biophysicalProperty__unit", curie=LAMBDABER.curie('functional_annotation/unit'),
                   model_uri=LAMBDABER.biophysicalProperty__unit, domain=None, range=str)

slots.biophysicalProperty__error = Slot(uri=LAMBDABER['functional_annotation/error'], name="biophysicalProperty__error", curie=LAMBDABER.curie('functional_annotation/error'),
                   model_uri=LAMBDABER.biophysicalProperty__error, domain=None, range=Optional[float])

slots.biophysicalProperty__measurement_conditions = Slot(uri=LAMBDABER['functional_annotation/measurement_conditions'], name="biophysicalProperty__measurement_conditions", curie=LAMBDABER.curie('functional_annotation/measurement_conditions'),
                   model_uri=LAMBDABER.biophysicalProperty__measurement_conditions, domain=None, range=Optional[str])

slots.biophysicalProperty__temperature = Slot(uri=LAMBDABER['functional_annotation/temperature'], name="biophysicalProperty__temperature", curie=LAMBDABER.curie('functional_annotation/temperature'),
                   model_uri=LAMBDABER.biophysicalProperty__temperature, domain=None, range=Optional[float])

slots.biophysicalProperty__ph = Slot(uri=LAMBDABER['functional_annotation/ph'], name="biophysicalProperty__ph", curie=LAMBDABER.curie('functional_annotation/ph'),
                   model_uri=LAMBDABER.biophysicalProperty__ph, domain=None, range=Optional[float])

slots.biophysicalProperty__ionic_strength = Slot(uri=LAMBDABER['functional_annotation/ionic_strength'], name="biophysicalProperty__ionic_strength", curie=LAMBDABER.curie('functional_annotation/ionic_strength'),
                   model_uri=LAMBDABER.biophysicalProperty__ionic_strength, domain=None, range=Optional[float])

slots.biophysicalProperty__experimental_method = Slot(uri=LAMBDABER['functional_annotation/experimental_method'], name="biophysicalProperty__experimental_method", curie=LAMBDABER.curie('functional_annotation/experimental_method'),
                   model_uri=LAMBDABER.biophysicalProperty__experimental_method, domain=None, range=Optional[Union[str, "BiophysicalMethodEnum"]])

slots.conformationalEnsemble__protein_id = Slot(uri=LAMBDABER['functional_annotation/protein_id'], name="conformationalEnsemble__protein_id", curie=LAMBDABER.curie('functional_annotation/protein_id'),
                   model_uri=LAMBDABER.conformationalEnsemble__protein_id, domain=None, range=str)

slots.conformationalEnsemble__conformational_states = Slot(uri=LAMBDABER['functional_annotation/conformational_states'], name="conformationalEnsemble__conformational_states", curie=LAMBDABER.curie('functional_annotation/conformational_states'),
                   model_uri=LAMBDABER.conformationalEnsemble__conformational_states, domain=None, range=Optional[Union[Union[dict, ConformationalState], list[Union[dict, ConformationalState]]]])

slots.conformationalEnsemble__clustering_method = Slot(uri=LAMBDABER['functional_annotation/clustering_method'], name="conformationalEnsemble__clustering_method", curie=LAMBDABER.curie('functional_annotation/clustering_method'),
                   model_uri=LAMBDABER.conformationalEnsemble__clustering_method, domain=None, range=Optional[str])

slots.conformationalEnsemble__rmsd_threshold = Slot(uri=LAMBDABER['functional_annotation/rmsd_threshold'], name="conformationalEnsemble__rmsd_threshold", curie=LAMBDABER.curie('functional_annotation/rmsd_threshold'),
                   model_uri=LAMBDABER.conformationalEnsemble__rmsd_threshold, domain=None, range=Optional[float])

slots.conformationalEnsemble__transition_pathways = Slot(uri=LAMBDABER['functional_annotation/transition_pathways'], name="conformationalEnsemble__transition_pathways", curie=LAMBDABER.curie('functional_annotation/transition_pathways'),
                   model_uri=LAMBDABER.conformationalEnsemble__transition_pathways, domain=None, range=Optional[str])

slots.conformationalEnsemble__energy_landscape = Slot(uri=LAMBDABER['functional_annotation/energy_landscape'], name="conformationalEnsemble__energy_landscape", curie=LAMBDABER.curie('functional_annotation/energy_landscape'),
                   model_uri=LAMBDABER.conformationalEnsemble__energy_landscape, domain=None, range=Optional[str])

slots.conformationalEnsemble__principal_motions = Slot(uri=LAMBDABER['functional_annotation/principal_motions'], name="conformationalEnsemble__principal_motions", curie=LAMBDABER.curie('functional_annotation/principal_motions'),
                   model_uri=LAMBDABER.conformationalEnsemble__principal_motions, domain=None, range=Optional[Union[str, list[str]]])

slots.conformationalState__state_id = Slot(uri=LAMBDABER['functional_annotation/state_id'], name="conformationalState__state_id", curie=LAMBDABER.curie('functional_annotation/state_id'),
                   model_uri=LAMBDABER.conformationalState__state_id, domain=None, range=str)

slots.conformationalState__state_name = Slot(uri=LAMBDABER['functional_annotation/state_name'], name="conformationalState__state_name", curie=LAMBDABER.curie('functional_annotation/state_name'),
                   model_uri=LAMBDABER.conformationalState__state_name, domain=None, range=Optional[str])

slots.conformationalState__pdb_entries = Slot(uri=LAMBDABER['functional_annotation/pdb_entries'], name="conformationalState__pdb_entries", curie=LAMBDABER.curie('functional_annotation/pdb_entries'),
                   model_uri=LAMBDABER.conformationalState__pdb_entries, domain=None, range=Optional[Union[str, list[str]]])

slots.conformationalState__population = Slot(uri=LAMBDABER['functional_annotation/population'], name="conformationalState__population", curie=LAMBDABER.curie('functional_annotation/population'),
                   model_uri=LAMBDABER.conformationalState__population, domain=None, range=Optional[float])

slots.conformationalState__free_energy = Slot(uri=LAMBDABER['functional_annotation/free_energy'], name="conformationalState__free_energy", curie=LAMBDABER.curie('functional_annotation/free_energy'),
                   model_uri=LAMBDABER.conformationalState__free_energy, domain=None, range=Optional[float])

slots.conformationalState__rmsd_from_reference = Slot(uri=LAMBDABER['functional_annotation/rmsd_from_reference'], name="conformationalState__rmsd_from_reference", curie=LAMBDABER.curie('functional_annotation/rmsd_from_reference'),
                   model_uri=LAMBDABER.conformationalState__rmsd_from_reference, domain=None, range=Optional[float])

slots.conformationalState__characteristic_features = Slot(uri=LAMBDABER['functional_annotation/characteristic_features'], name="conformationalState__characteristic_features", curie=LAMBDABER.curie('functional_annotation/characteristic_features'),
                   model_uri=LAMBDABER.conformationalState__characteristic_features, domain=None, range=Optional[Union[str, list[str]]])

slots.postTranslationalModification__modification_type = Slot(uri=LAMBDABER['functional_annotation/modification_type'], name="postTranslationalModification__modification_type", curie=LAMBDABER.curie('functional_annotation/modification_type'),
                   model_uri=LAMBDABER.postTranslationalModification__modification_type, domain=None, range=Union[str, "PTMTypeEnum"])

slots.postTranslationalModification__modified_residue = Slot(uri=LAMBDABER['functional_annotation/modified_residue'], name="postTranslationalModification__modified_residue", curie=LAMBDABER.curie('functional_annotation/modified_residue'),
                   model_uri=LAMBDABER.postTranslationalModification__modified_residue, domain=None, range=str)

slots.postTranslationalModification__modification_group = Slot(uri=LAMBDABER['functional_annotation/modification_group'], name="postTranslationalModification__modification_group", curie=LAMBDABER.curie('functional_annotation/modification_group'),
                   model_uri=LAMBDABER.postTranslationalModification__modification_group, domain=None, range=Optional[str])

slots.postTranslationalModification__mass_shift = Slot(uri=LAMBDABER['functional_annotation/mass_shift'], name="postTranslationalModification__mass_shift", curie=LAMBDABER.curie('functional_annotation/mass_shift'),
                   model_uri=LAMBDABER.postTranslationalModification__mass_shift, domain=None, range=Optional[float])

slots.postTranslationalModification__functional_effect = Slot(uri=LAMBDABER['functional_annotation/functional_effect'], name="postTranslationalModification__functional_effect", curie=LAMBDABER.curie('functional_annotation/functional_effect'),
                   model_uri=LAMBDABER.postTranslationalModification__functional_effect, domain=None, range=Optional[str])

slots.postTranslationalModification__regulatory_role = Slot(uri=LAMBDABER['functional_annotation/regulatory_role'], name="postTranslationalModification__regulatory_role", curie=LAMBDABER.curie('functional_annotation/regulatory_role'),
                   model_uri=LAMBDABER.postTranslationalModification__regulatory_role, domain=None, range=Optional[str])

slots.postTranslationalModification__enzyme = Slot(uri=LAMBDABER['functional_annotation/enzyme'], name="postTranslationalModification__enzyme", curie=LAMBDABER.curie('functional_annotation/enzyme'),
                   model_uri=LAMBDABER.postTranslationalModification__enzyme, domain=None, range=Optional[str])

slots.postTranslationalModification__removal_enzyme = Slot(uri=LAMBDABER['functional_annotation/removal_enzyme'], name="postTranslationalModification__removal_enzyme", curie=LAMBDABER.curie('functional_annotation/removal_enzyme'),
                   model_uri=LAMBDABER.postTranslationalModification__removal_enzyme, domain=None, range=Optional[str])

slots.databaseCrossReference__database_name = Slot(uri=LAMBDABER['functional_annotation/database_name'], name="databaseCrossReference__database_name", curie=LAMBDABER.curie('functional_annotation/database_name'),
                   model_uri=LAMBDABER.databaseCrossReference__database_name, domain=None, range=Union[str, "DatabaseNameEnum"])

slots.databaseCrossReference__database_id = Slot(uri=LAMBDABER['functional_annotation/database_id'], name="databaseCrossReference__database_id", curie=LAMBDABER.curie('functional_annotation/database_id'),
                   model_uri=LAMBDABER.databaseCrossReference__database_id, domain=None, range=str)

slots.databaseCrossReference__database_url = Slot(uri=LAMBDABER['functional_annotation/database_url'], name="databaseCrossReference__database_url", curie=LAMBDABER.curie('functional_annotation/database_url'),
                   model_uri=LAMBDABER.databaseCrossReference__database_url, domain=None, range=Optional[Union[str, URI]])

slots.databaseCrossReference__last_updated = Slot(uri=LAMBDABER['functional_annotation/last_updated'], name="databaseCrossReference__last_updated", curie=LAMBDABER.curie('functional_annotation/last_updated'),
                   model_uri=LAMBDABER.databaseCrossReference__last_updated, domain=None, range=Optional[str])

slots.evolutionaryConservation__conservation_score = Slot(uri=LAMBDABER['functional_annotation/conservation_score'], name="evolutionaryConservation__conservation_score", curie=LAMBDABER.curie('functional_annotation/conservation_score'),
                   model_uri=LAMBDABER.evolutionaryConservation__conservation_score, domain=None, range=Optional[float])

slots.evolutionaryConservation__conserved_residues = Slot(uri=LAMBDABER['functional_annotation/conserved_residues'], name="evolutionaryConservation__conserved_residues", curie=LAMBDABER.curie('functional_annotation/conserved_residues'),
                   model_uri=LAMBDABER.evolutionaryConservation__conserved_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.evolutionaryConservation__variable_residues = Slot(uri=LAMBDABER['functional_annotation/variable_residues'], name="evolutionaryConservation__variable_residues", curie=LAMBDABER.curie('functional_annotation/variable_residues'),
                   model_uri=LAMBDABER.evolutionaryConservation__variable_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.evolutionaryConservation__conservation_method = Slot(uri=LAMBDABER['functional_annotation/conservation_method'], name="evolutionaryConservation__conservation_method", curie=LAMBDABER.curie('functional_annotation/conservation_method'),
                   model_uri=LAMBDABER.evolutionaryConservation__conservation_method, domain=None, range=Optional[str])

slots.evolutionaryConservation__alignment_depth = Slot(uri=LAMBDABER['functional_annotation/alignment_depth'], name="evolutionaryConservation__alignment_depth", curie=LAMBDABER.curie('functional_annotation/alignment_depth'),
                   model_uri=LAMBDABER.evolutionaryConservation__alignment_depth, domain=None, range=Optional[int])

slots.evolutionaryConservation__taxonomic_range = Slot(uri=LAMBDABER['functional_annotation/taxonomic_range'], name="evolutionaryConservation__taxonomic_range", curie=LAMBDABER.curie('functional_annotation/taxonomic_range'),
                   model_uri=LAMBDABER.evolutionaryConservation__taxonomic_range, domain=None, range=Optional[str])

slots.evolutionaryConservation__coevolved_residues = Slot(uri=LAMBDABER['functional_annotation/coevolved_residues'], name="evolutionaryConservation__coevolved_residues", curie=LAMBDABER.curie('functional_annotation/coevolved_residues'),
                   model_uri=LAMBDABER.evolutionaryConservation__coevolved_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.aggregatedProteinView__uniprot_id = Slot(uri=LAMBDABER['functional_annotation/uniprot_id'], name="aggregatedProteinView__uniprot_id", curie=LAMBDABER.curie('functional_annotation/uniprot_id'),
                   model_uri=LAMBDABER.aggregatedProteinView__uniprot_id, domain=None, range=str)

slots.aggregatedProteinView__protein_name = Slot(uri=LAMBDABER['functional_annotation/protein_name'], name="aggregatedProteinView__protein_name", curie=LAMBDABER.curie('functional_annotation/protein_name'),
                   model_uri=LAMBDABER.aggregatedProteinView__protein_name, domain=None, range=str)

slots.aggregatedProteinView__organism = Slot(uri=LAMBDABER['functional_annotation/organism'], name="aggregatedProteinView__organism", curie=LAMBDABER.curie('functional_annotation/organism'),
                   model_uri=LAMBDABER.aggregatedProteinView__organism, domain=None, range=Optional[str])

slots.aggregatedProteinView__organism_id = Slot(uri=LAMBDABER['functional_annotation/organism_id'], name="aggregatedProteinView__organism_id", curie=LAMBDABER.curie('functional_annotation/organism_id'),
                   model_uri=LAMBDABER.aggregatedProteinView__organism_id, domain=None, range=Optional[int])

slots.aggregatedProteinView__pdb_entries = Slot(uri=LAMBDABER['functional_annotation/pdb_entries'], name="aggregatedProteinView__pdb_entries", curie=LAMBDABER.curie('functional_annotation/pdb_entries'),
                   model_uri=LAMBDABER.aggregatedProteinView__pdb_entries, domain=None, range=Optional[Union[str, list[str]]])

slots.aggregatedProteinView__functional_sites = Slot(uri=LAMBDABER['functional_annotation/functional_sites'], name="aggregatedProteinView__functional_sites", curie=LAMBDABER.curie('functional_annotation/functional_sites'),
                   model_uri=LAMBDABER.aggregatedProteinView__functional_sites, domain=None, range=Optional[Union[dict[Union[str, FunctionalSiteId], Union[dict, FunctionalSite]], list[Union[dict, FunctionalSite]]]])

slots.aggregatedProteinView__structural_features = Slot(uri=LAMBDABER['functional_annotation/structural_features'], name="aggregatedProteinView__structural_features", curie=LAMBDABER.curie('functional_annotation/structural_features'),
                   model_uri=LAMBDABER.aggregatedProteinView__structural_features, domain=None, range=Optional[Union[dict[Union[str, StructuralFeatureId], Union[dict, StructuralFeature]], list[Union[dict, StructuralFeature]]]])

slots.aggregatedProteinView__protein_interactions = Slot(uri=LAMBDABER['functional_annotation/protein_interactions'], name="aggregatedProteinView__protein_interactions", curie=LAMBDABER.curie('functional_annotation/protein_interactions'),
                   model_uri=LAMBDABER.aggregatedProteinView__protein_interactions, domain=None, range=Optional[Union[dict[Union[str, ProteinProteinInteractionId], Union[dict, ProteinProteinInteraction]], list[Union[dict, ProteinProteinInteraction]]]])

slots.aggregatedProteinView__ligand_interactions = Slot(uri=LAMBDABER['functional_annotation/ligand_interactions'], name="aggregatedProteinView__ligand_interactions", curie=LAMBDABER.curie('functional_annotation/ligand_interactions'),
                   model_uri=LAMBDABER.aggregatedProteinView__ligand_interactions, domain=None, range=Optional[Union[Union[dict, LigandInteraction], list[Union[dict, LigandInteraction]]]])

slots.aggregatedProteinView__mutations = Slot(uri=LAMBDABER['functional_annotation/mutations'], name="aggregatedProteinView__mutations", curie=LAMBDABER.curie('functional_annotation/mutations'),
                   model_uri=LAMBDABER.aggregatedProteinView__mutations, domain=None, range=Optional[Union[dict[Union[str, MutationEffectId], Union[dict, MutationEffect]], list[Union[dict, MutationEffect]]]])

slots.aggregatedProteinView__ptms = Slot(uri=LAMBDABER['functional_annotation/ptms'], name="aggregatedProteinView__ptms", curie=LAMBDABER.curie('functional_annotation/ptms'),
                   model_uri=LAMBDABER.aggregatedProteinView__ptms, domain=None, range=Optional[Union[dict[Union[str, PostTranslationalModificationId], Union[dict, PostTranslationalModification]], list[Union[dict, PostTranslationalModification]]]])

slots.aggregatedProteinView__biophysical_properties = Slot(uri=LAMBDABER['functional_annotation/biophysical_properties'], name="aggregatedProteinView__biophysical_properties", curie=LAMBDABER.curie('functional_annotation/biophysical_properties'),
                   model_uri=LAMBDABER.aggregatedProteinView__biophysical_properties, domain=None, range=Optional[Union[Union[dict, BiophysicalProperty], list[Union[dict, BiophysicalProperty]]]])

slots.aggregatedProteinView__conformational_ensemble = Slot(uri=LAMBDABER['functional_annotation/conformational_ensemble'], name="aggregatedProteinView__conformational_ensemble", curie=LAMBDABER.curie('functional_annotation/conformational_ensemble'),
                   model_uri=LAMBDABER.aggregatedProteinView__conformational_ensemble, domain=None, range=Optional[Union[dict, ConformationalEnsemble]])

slots.aggregatedProteinView__evolutionary_conservation = Slot(uri=LAMBDABER['functional_annotation/evolutionary_conservation'], name="aggregatedProteinView__evolutionary_conservation", curie=LAMBDABER.curie('functional_annotation/evolutionary_conservation'),
                   model_uri=LAMBDABER.aggregatedProteinView__evolutionary_conservation, domain=None, range=Optional[Union[dict, EvolutionaryConservation]])

slots.aggregatedProteinView__cross_references = Slot(uri=LAMBDABER['functional_annotation/cross_references'], name="aggregatedProteinView__cross_references", curie=LAMBDABER.curie('functional_annotation/cross_references'),
                   model_uri=LAMBDABER.aggregatedProteinView__cross_references, domain=None, range=Optional[Union[Union[dict, DatabaseCrossReference], list[Union[dict, DatabaseCrossReference]]]])
