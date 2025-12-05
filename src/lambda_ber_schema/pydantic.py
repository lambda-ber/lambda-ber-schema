from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'lambdaber',
     'default_range': 'string',
     'description': 'lambda-ber-schema is a comprehensive schema for representing '
                    'multimodal structural biology imaging data, \n'
                    'from atomic-resolution structures to tissue-level '
                    'organization. It supports diverse experimental \n'
                    'techniques including cryo-EM, X-ray crystallography, '
                    'SAXS/SANS, fluorescence microscopy, and \n'
                    'spectroscopic imaging.\n'
                    '\n'
                    '## Schema Organization\n'
                    '\n'
                    'The schema follows a hierarchical structure that mirrors how '
                    'structural biology research is organized:\n'
                    '\n'
                    'The top-level entity is a [Dataset](Dataset.md), which serves '
                    'as a container for related research.\n'
                    'A dataset might represent all data from a specific grant, '
                    'collaboration, or publication.\n'
                    '\n'
                    'Each dataset contains one or more [Studies](Study.md), which '
                    'are focused investigations of specific\n'
                    'biological questions. For example, a study might investigate '
                    '"Heat stress response in Arabidopsis"\n'
                    'or "Structure of the human ribosome under different '
                    'conditions."\n'
                    '\n'
                    "Within each study, you'll find:\n"
                    '\n'
                    '### Biological Materials\n'
                    '- [Samples](Sample.md): The biological specimens being '
                    'studied (proteins, nucleic acids, complexes, \n'
                    '  cells, tissues). Each sample includes detailed molecular '
                    'composition, buffer conditions, and \n'
                    '  storage information. For example, a purified protein with '
                    'its sequence, concentration, and buffer pH.\n'
                    '\n'
                    '- [Sample Preparations](SamplePreparation.md): How samples '
                    'were prepared for specific techniques.\n'
                    '  This includes cryo-EM grid preparation (vitrification '
                    'parameters), crystallization conditions for\n'
                    '  X-ray studies, or staining protocols for fluorescence '
                    'microscopy.\n'
                    '\n'
                    '### Data Collection\n'
                    '- [Instruments](Instrument.md): The equipment used, from '
                    'Titan Krios microscopes to synchrotron \n'
                    '  beamlines. Each instrument type '
                    '([CryoEMInstrument](CryoEMInstrument.md), \n'
                    '  [XRayInstrument](XRayInstrument.md), '
                    '[SAXSInstrument](SAXSInstrument.md)) has specific parameters\n'
                    '  like accelerating voltage, detector type, or beam energy.\n'
                    '\n'
                    '- [Experiment Runs](ExperimentRun.md): Individual data '
                    'collection sessions that link samples to \n'
                    '  instruments. An experiment run captures when, how, and '
                    'under what conditions data was collected,\n'
                    '  including quality metrics like resolution and '
                    'completeness.\n'
                    '\n'
                    '### Data Processing\n'
                    '- [Workflow Runs](WorkflowRun.md): Computational processing '
                    'steps applied to raw data. This includes\n'
                    '  motion correction for cryo-EM movies, 3D reconstruction, '
                    'model building, or phase determination\n'
                    '  for crystallography. Each workflow tracks the software '
                    'used, parameters, and computational resources.\n'
                    '\n'
                    '### Data Products\n'
                    '- [Data Files](DataFile.md): Any files generated or used, '
                    'from raw data to final models. Each file\n'
                    '  is tracked with checksums for data integrity and typed '
                    '(micrograph, particles, volume, model).\n'
                    '\n'
                    '- [Images](Image.md): Specialized classes for different '
                    'imaging modalities:\n'
                    '  - [Image2D](Image2D.md): Micrographs, diffraction patterns\n'
                    '  - [Image3D](Image3D.md): 3D reconstructions, tomograms\n'
                    '  - [FTIRImage](FTIRImage.md): Molecular composition maps '
                    'from infrared spectroscopy\n'
                    '  - [FluorescenceImage](FluorescenceImage.md): '
                    'Fluorophore-labeled cellular components\n'
                    '  - [OpticalImage](OpticalImage.md): Brightfield/phase '
                    'contrast microscopy\n'
                    '  - [XRFImage](XRFImage.md): Elemental distribution maps\n'
                    '\n'
                    '## Example Usage\n'
                    '\n'
                    'A typical cryo-EM study of a protein complex would include:\n'
                    '1. Sample records for the purified complex with molecular '
                    'weight and buffer composition\n'
                    '2. Grid preparation details with vitrification parameters\n'
                    '3. Microscope specifications and data collection parameters\n'
                    '4. Processing workflows from motion correction through 3D '
                    'refinement\n'
                    '5. Final reconstructed volumes and fitted atomic models\n'
                    '\n'
                    'A multimodal plant imaging study might combine:\n'
                    '1. Whole plant optical imaging for morphology\n'
                    '2. XRF imaging to map nutrient distribution\n'
                    '3. FTIR spectroscopy to identify stress-related molecular '
                    'changes\n'
                    '4. Fluorescence microscopy to track specific protein '
                    'responses\n'
                    '5. Cryo-EM of isolated organelles for ultrastructural '
                    'details\n'
                    '\n'
                    '## Key Features\n'
                    '\n'
                    '- **Technique-agnostic core**: The same schema handles data '
                    'from any structural biology method\n'
                    '- **Rich metadata**: Comprehensive tracking from sample to '
                    'structure\n'
                    '- **Workflow provenance**: Complete computational '
                    'reproducibility\n'
                    '- **Multimodal support**: Seamlessly integrate data across '
                    'scales and techniques\n'
                    '- **Standards-compliant**: Follows FAIR principles and '
                    'integrates with existing ontologies\n',
     'id': 'https://w3id.org/lambda-ber-schema/',
     'imports': ['linkml:types', 'functional_annotation'],
     'name': 'lambda-ber-schema',
     'prefixes': {'CHMO': {'prefix_prefix': 'CHMO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/CHMO_'},
                  'CL': {'prefix_prefix': 'CL',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CL_'},
                  'GO': {'prefix_prefix': 'GO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/GO_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'ROR': {'prefix_prefix': 'ROR',
                          'prefix_reference': 'https://ror.org/'},
                  'UBERON': {'prefix_prefix': 'UBERON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/UBERON_'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'imgCIF': {'prefix_prefix': 'imgCIF',
                             'prefix_reference': 'https://github.com/dials/cbflib/blob/main/doc/cif_img_1.8.6.dic#'},
                  'lambdaber': {'prefix_prefix': 'lambdaber',
                                'prefix_reference': 'https://w3id.org/lambda-ber-schema/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mmCIF': {'prefix_prefix': 'mmCIF',
                            'prefix_reference': 'http://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/'},
                  'nmdc': {'prefix_prefix': 'nmdc',
                           'prefix_reference': 'https://w3id.org/nmdc/'},
                  'nsls2': {'prefix_prefix': 'nsls2',
                            'prefix_reference': 'https://github.com/NSLS2/BER-LAMBDA/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'sio': {'prefix_prefix': 'sio',
                          'prefix_reference': 'http://semanticscience.org/resource/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'wikidata': {'prefix_prefix': 'wikidata',
                               'prefix_reference': 'http://www.wikidata.org/entity/'}},
     'source_file': 'src/lambda_ber_schema/schema/lambda-ber-schema.yaml'} )

class FunctionalSiteTypeEnum(str, Enum):
    """
    Types of functional sites in proteins
    """
    active_site = "active_site"
    """
    Enzyme active site
    """
    catalytic_site = "catalytic_site"
    """
    Catalytic residues
    """
    binding_site = "binding_site"
    """
    General binding site
    """
    allosteric_site = "allosteric_site"
    """
    Allosteric regulation site
    """
    substrate_binding = "substrate_binding"
    """
    Substrate binding site
    """
    cofactor_binding = "cofactor_binding"
    """
    Cofactor binding site
    """
    inhibitor_binding = "inhibitor_binding"
    """
    Inhibitor binding site
    """
    metal_binding = "metal_binding"
    """
    Metal ion binding site
    """
    nucleotide_binding = "nucleotide_binding"
    """
    Nucleotide binding site
    """
    phosphorylation_site = "phosphorylation_site"
    """
    Phosphorylation site
    """
    glycosylation_site = "glycosylation_site"
    """
    Glycosylation site
    """
    ubiquitination_site = "ubiquitination_site"
    """
    Ubiquitination site
    """
    sumoylation_site = "sumoylation_site"
    """
    SUMOylation site
    """
    acetylation_site = "acetylation_site"
    """
    Acetylation site
    """
    methylation_site = "methylation_site"
    """
    Methylation site
    """
    protein_binding = "protein_binding"
    """
    Protein-protein interaction site
    """
    dna_binding = "dna_binding"
    """
    DNA binding site
    """
    rna_binding = "rna_binding"
    """
    RNA binding site
    """
    lipid_binding = "lipid_binding"
    """
    Lipid binding site
    """


class StructuralFeatureTypeEnum(str, Enum):
    """
    Types of structural features
    """
    alpha_helix = "alpha_helix"
    """
    Alpha helix
    """
    beta_sheet = "beta_sheet"
    """
    Beta sheet
    """
    beta_strand = "beta_strand"
    """
    Beta strand
    """
    turn = "turn"
    """
    Turn structure
    """
    coil = "coil"
    """
    Random coil
    """
    disordered_region = "disordered_region"
    """
    Intrinsically disordered region
    """
    transmembrane_helix = "transmembrane_helix"
    """
    Transmembrane helix
    """
    signal_peptide = "signal_peptide"
    """
    Signal peptide
    """
    transit_peptide = "transit_peptide"
    """
    Transit peptide
    """
    domain = "domain"
    """
    Protein domain
    """
    repeat = "repeat"
    """
    Sequence repeat
    """
    zinc_finger = "zinc_finger"
    """
    Zinc finger motif
    """
    zinc_binding = "zinc_binding"
    """
    Zinc binding site
    """
    coiled_coil = "coiled_coil"
    """
    Coiled coil
    """
    motif = "motif"
    """
    Structural motif
    """
    cavity = "cavity"
    """
    Structural cavity
    """
    channel = "channel"
    """
    Molecular channel
    """
    pore = "pore"
    """
    Molecular pore
    """
    hinge = "hinge"
    """
    Hinge region
    """
    linker = "linker"
    """
    Linker region
    """


class SecondaryStructureEnum(str, Enum):
    """
    Secondary structure types
    """
    helix = "helix"
    """
    Helix structure
    """
    sheet = "sheet"
    """
    Beta sheet
    """
    turn = "turn"
    """
    Turn
    """
    coil = "coil"
    """
    Random coil
    """
    helix_310 = "helix_310"
    """
    3-10 helix
    """
    helix_pi = "helix_pi"
    """
    Pi helix
    """
    bend = "bend"
    """
    Bend
    """
    bridge = "bridge"
    """
    Beta bridge
    """


class ConformationalStateEnum(str, Enum):
    """
    Conformational states
    """
    open = "open"
    """
    Open conformation
    """
    closed = "closed"
    """
    Closed conformation
    """
    intermediate = "intermediate"
    """
    Intermediate state
    """
    active = "active"
    """
    Active conformation
    """
    inactive = "inactive"
    """
    Inactive conformation
    """
    apo = "apo"
    """
    Apo form
    """
    holo = "holo"
    """
    Holo form
    """
    substrate_bound = "substrate_bound"
    """
    Substrate-bound
    """
    product_bound = "product_bound"
    """
    Product-bound
    """
    inhibitor_bound = "inhibitor_bound"
    """
    Inhibitor-bound
    """
    partially_open = "partially_open"
    """
    Partially open
    """
    partially_closed = "partially_closed"
    """
    Partially closed
    """
    disordered = "disordered"
    """
    Disordered state
    """


class InteractionTypeEnum(str, Enum):
    """
    Types of molecular interactions
    """
    covalent = "covalent"
    """
    Covalent bond
    """
    hydrogen_bond = "hydrogen_bond"
    """
    Hydrogen bond
    """
    ionic = "ionic"
    """
    Ionic interaction
    """
    van_der_waals = "van_der_waals"
    """
    Van der Waals interaction
    """
    hydrophobic = "hydrophobic"
    """
    Hydrophobic interaction
    """
    aromatic = "aromatic"
    """
    Aromatic interaction
    """
    pi_stacking = "pi_stacking"
    """
    Pi-pi stacking
    """
    cation_pi = "cation_pi"
    """
    Cation-pi interaction
    """
    metal_coordination = "metal_coordination"
    """
    Metal coordination
    """
    disulfide = "disulfide"
    """
    Disulfide bond
    """


class BindingAffinityTypeEnum(str, Enum):
    """
    Types of binding affinity measurements
    """
    kd = "kd"
    """
    Dissociation constant
    """
    ki = "ki"
    """
    Inhibition constant
    """
    ic50 = "ic50"
    """
    Half maximal inhibitory concentration
    """
    ec50 = "ec50"
    """
    Half maximal effective concentration
    """
    ka = "ka"
    """
    Association constant
    """
    km = "km"
    """
    Michaelis constant
    """


class AffinityUnitEnum(str, Enum):
    """
    Units for affinity measurements
    """
    molar = "molar"
    """
    Molar (M)
    """
    millimolar = "millimolar"
    """
    Millimolar (mM)
    """
    micromolar = "micromolar"
    """
    Micromolar (µM)
    """
    nanomolar = "nanomolar"
    """
    Nanomolar (nM)
    """
    picomolar = "picomolar"
    """
    Picomolar (pM)
    """


class ComplexStabilityEnum(str, Enum):
    """
    Stability of protein complexes
    """
    stable = "stable"
    """
    Stable complex
    """
    transient = "transient"
    """
    Transient interaction
    """
    weak = "weak"
    """
    Weak interaction
    """
    strong = "strong"
    """
    Strong interaction
    """
    obligate = "obligate"
    """
    Obligate complex
    """
    non_obligate = "non_obligate"
    """
    Non-obligate complex
    """


class InteractionEvidenceEnum(str, Enum):
    """
    Evidence for interactions
    """
    experimental = "experimental"
    """
    Experimental evidence
    """
    predicted = "predicted"
    """
    Computational prediction
    """
    homology = "homology"
    """
    Homology-based
    """
    coexpression = "coexpression"
    """
    Co-expression data
    """
    colocalization = "colocalization"
    """
    Co-localization
    """
    genetic = "genetic"
    """
    Genetic evidence
    """
    physical = "physical"
    """
    Physical interaction
    """
    functional = "functional"
    """
    Functional association
    """


class MutationTypeEnum(str, Enum):
    """
    Types of mutations
    """
    missense = "missense"
    """
    Missense mutation
    """
    nonsense = "nonsense"
    """
    Nonsense mutation
    """
    frameshift = "frameshift"
    """
    Frameshift mutation
    """
    deletion = "deletion"
    """
    Deletion
    """
    insertion = "insertion"
    """
    Insertion
    """
    duplication = "duplication"
    """
    Duplication
    """
    substitution = "substitution"
    """
    Substitution
    """


class StabilityEffectEnum(str, Enum):
    """
    Effect on protein stability
    """
    stabilizing = "stabilizing"
    """
    Increases stability
    """
    destabilizing = "destabilizing"
    """
    Decreases stability
    """
    neutral = "neutral"
    """
    No significant effect
    """
    highly_stabilizing = "highly_stabilizing"
    """
    Strongly increases stability
    """
    highly_destabilizing = "highly_destabilizing"
    """
    Strongly decreases stability
    """


class FunctionalEffectEnum(str, Enum):
    """
    Effect on protein function
    """
    loss_of_function = "loss_of_function"
    """
    Loss of function
    """
    gain_of_function = "gain_of_function"
    """
    Gain of function
    """
    altered_function = "altered_function"
    """
    Altered function
    """
    no_effect = "no_effect"
    """
    No functional effect
    """
    partial_loss = "partial_loss"
    """
    Partial loss of function
    """
    enhanced_function = "enhanced_function"
    """
    Enhanced function
    """


class ClinicalSignificanceEnum(str, Enum):
    """
    Clinical significance of variants
    """
    pathogenic = "pathogenic"
    """
    Pathogenic
    """
    likely_pathogenic = "likely_pathogenic"
    """
    Likely pathogenic
    """
    benign = "benign"
    """
    Benign
    """
    likely_benign = "likely_benign"
    """
    Likely benign
    """
    uncertain_significance = "uncertain_significance"
    """
    Uncertain significance
    """


class BiophysicalPropertyEnum(str, Enum):
    """
    Types of biophysical properties
    """
    melting_temperature = "melting_temperature"
    """
    Melting temperature (Tm)
    """
    stability = "stability"
    """
    Thermodynamic stability
    """
    folding_rate = "folding_rate"
    """
    Folding rate
    """
    unfolding_rate = "unfolding_rate"
    """
    Unfolding rate
    """
    aggregation_propensity = "aggregation_propensity"
    """
    Aggregation propensity
    """
    solubility = "solubility"
    """
    Solubility
    """
    hydrophobicity = "hydrophobicity"
    """
    Hydrophobicity
    """
    isoelectric_point = "isoelectric_point"
    """
    Isoelectric point (pI)
    """
    extinction_coefficient = "extinction_coefficient"
    """
    Extinction coefficient
    """
    molecular_weight = "molecular_weight"
    """
    Molecular weight
    """
    diffusion_coefficient = "diffusion_coefficient"
    """
    Diffusion coefficient
    """
    sedimentation_coefficient = "sedimentation_coefficient"
    """
    Sedimentation coefficient
    """
    radius_of_gyration = "radius_of_gyration"
    """
    Radius of gyration
    """
    hydrodynamic_radius = "hydrodynamic_radius"
    """
    Hydrodynamic radius
    """


class BiophysicalMethodEnum(str, Enum):
    """
    Methods for biophysical measurements
    """
    differential_scanning_calorimetry = "differential_scanning_calorimetry"
    """
    DSC
    """
    isothermal_titration_calorimetry = "isothermal_titration_calorimetry"
    """
    ITC
    """
    circular_dichroism = "circular_dichroism"
    """
    CD spectroscopy
    """
    fluorescence_spectroscopy = "fluorescence_spectroscopy"
    """
    Fluorescence
    """
    surface_plasmon_resonance = "surface_plasmon_resonance"
    """
    SPR
    """
    dynamic_light_scattering = "dynamic_light_scattering"
    """
    DLS
    """
    analytical_ultracentrifugation = "analytical_ultracentrifugation"
    """
    AUC
    """
    nuclear_magnetic_resonance = "nuclear_magnetic_resonance"
    """
    NMR
    """
    mass_spectrometry = "mass_spectrometry"
    """
    MS
    """


class PTMTypeEnum(str, Enum):
    """
    Types of post-translational modifications
    """
    acetylation = "acetylation"
    """
    protein acetylation
    """
    acylation = "acylation"
    """
    protein acylation
    """
    adp_ribosylation = "adp_ribosylation"
    """
    ADP-ribosylation
    """
    alkylation = "alkylation"
    """
    protein alkylation
    """
    arginylation = "arginylation"
    """
    protein arginylation
    """
    carbamoylation = "carbamoylation"
    """
    protein carbamoylation
    """
    carboxylation = "carboxylation"
    """
    protein carboxylation
    """
    deacylation = "deacylation"
    """
    protein deacylation
    """
    dealkylation = "dealkylation"
    """
    protein dealkylation
    """
    deamidation = "deamidation"
    """
    deamidation
    """
    deamination = "deamination"
    """
    protein deamination
    """
    deglutathionylation = "deglutathionylation"
    """
    protein deglutathionylation
    """
    deglycation = "deglycation"
    """
    protein deglycation
    """
    deglycosylation = "deglycosylation"
    """
    protein deglycosylation
    """
    dephosphorylation = "dephosphorylation"
    """
    protein dephosphorylation
    """
    flavinylation = "flavinylation"
    """
    protein flavinylation
    """
    glutathionylation = "glutathionylation"
    """
    protein glutathionylation
    """
    glycosylation = "glycosylation"
    """
    protein glycosylation
    """
    hydroxylation = "hydroxylation"
    """
    protein hydroxylation
    """
    lipidation = "lipidation"
    """
    protein lipidation
    """
    methylation = "methylation"
    """
    protein methylation
    """
    myristoylation = "myristoylation"
    """
    protein myristoylation
    """
    nitrosylation = "nitrosylation"
    """
    protein nitrosylation
    """
    oxidation = "oxidation"
    """
    protein oxidation
    """
    palmitoylation = "palmitoylation"
    """
    protein palmitoylation
    """
    peptidyl_amino_acid_modification = "peptidyl_amino_acid_modification"
    """
    peptidyl-amino acid modification
    """
    phosphorylation = "phosphorylation"
    """
    protein phosphorylation
    """
    post_translational_protein_modification = "post_translational_protein_modification"
    """
    post-translational protein modification
    """
    prenylation = "prenylation"
    """
    protein prenylation
    """
    proteolysis = "proteolysis"
    """
    proteolysis
    """
    sulfation = "sulfation"
    """
    protein sulfation
    """
    sulfhydration = "sulfhydration"
    """
    protein sulfhydration
    """
    sumoylation = "sumoylation"
    """
    protein sumoylation
    """
    ubiquitination = "ubiquitination"
    """
    protein ubiquitination
    """


class EvidenceTypeEnum(str, Enum):
    """
    Types of evidence
    """
    experimental = "experimental"
    """
    Direct experimental evidence
    """
    predicted = "predicted"
    """
    Computational prediction
    """
    inferred = "inferred"
    """
    Inferred from homology
    """
    literature = "literature"
    """
    Literature curation
    """
    author_statement = "author_statement"
    """
    Author statement
    """
    curator_inference = "curator_inference"
    """
    Curator inference
    """


class AnnotationSourceEnum(str, Enum):
    """
    Sources of functional annotations
    """
    pdbe = "pdbe"
    """
    PDBe
    """
    pdbe_kb = "pdbe_kb"
    """
    PDBe-KB
    """
    uniprot = "uniprot"
    """
    UniProt
    """
    pfam = "pfam"
    """
    Pfam
    """
    cath = "cath"
    """
    CATH
    """
    scop = "scop"
    """
    SCOP
    """
    interpro = "interpro"
    """
    InterPro
    """
    channelsdb = "channelsdb"
    """
    ChannelsDB
    """
    dynamine = "dynamine"
    """
    DynaMine
    """
    foldx = "foldx"
    """
    FoldX
    """
    p2rank = "p2rank"
    """
    P2rank
    """
    number_3dligandsite = "3dligandsite"
    """
    3D-LigandSite
    """
    arpeggio = "arpeggio"
    """
    Arpeggio
    """
    covalentizer = "covalentizer"
    """
    Covalentizer
    """
    depth = "depth"
    """
    DEPTH
    """
    elmpdb = "elmpdb"
    """
    ELM-PDB
    """
    frustration = "frustration"
    """
    Frustration
    """
    kincore = "kincore"
    """
    KinCore
    """
    membranome = "membranome"
    """
    Membranome
    """
    missense3d = "missense3d"
    """
    Missense3D
    """
    mobi = "mobi"
    """
    MobiDB
    """
    nucleos = "nucleos"
    """
    Nucleos
    """
    number_14_3_3_pred = "14_3_3_pred"
    """
    14-3-3-Pred
    """
    akid = "akid"
    """
    AKID
    """
    camkinet = "camkinet"
    """
    CamKiNet
    """
    cansar = "cansar"
    """
    canSAR
    """
    credo = "credo"
    """
    CREDO
    """
    klifs = "klifs"
    """
    KLIFS
    """
    m_csm = "m_csm"
    """
    mCSM
    """
    moondb = "moondb"
    """
    MoonDB
    """
    pocketome = "pocketome"
    """
    Pocketome
    """
    propka = "propka"
    """
    PROPKA
    """
    proteins_api = "proteins_api"
    """
    Proteins API
    """
    validation = "validation"
    """
    Validation
    """
    alphafold = "alphafold"
    """
    AlphaFold
    """
    modbase = "modbase"
    """
    ModBase
    """
    swiss_model = "swiss_model"
    """
    SWISS-MODEL
    """
    intact = "intact"
    """
    IntAct
    """
    cosmic = "cosmic"
    """
    COSMIC
    """
    clinvar = "clinvar"
    """
    ClinVar
    """


class DatabaseNameEnum(str, Enum):
    """
    External database names
    """
    uniprot = "uniprot"
    """
    UniProt
    """
    pdb = "pdb"
    """
    Protein Data Bank
    """
    pfam = "pfam"
    """
    Pfam
    """
    cath = "cath"
    """
    CATH
    """
    scop = "scop"
    """
    SCOP
    """
    interpro = "interpro"
    """
    InterPro
    """
    chembl = "chembl"
    """
    ChEMBL
    """
    chebi = "chebi"
    """
    ChEBI
    """
    pubchem = "pubchem"
    """
    PubChem
    """
    drugbank = "drugbank"
    """
    DrugBank
    """
    omim = "omim"
    """
    OMIM
    """
    clinvar = "clinvar"
    """
    ClinVar
    """
    cosmic = "cosmic"
    """
    COSMIC
    """
    gnomad = "gnomad"
    """
    gnomAD
    """
    intact = "intact"
    """
    IntAct
    """
    string = "string"
    """
    STRING
    """
    biogrid = "biogrid"
    """
    BioGRID
    """
    reactome = "reactome"
    """
    Reactome
    """
    kegg = "kegg"
    """
    KEGG
    """
    go = "go"
    """
    Gene Ontology
    """


class FacilityEnum(str, Enum):
    """
    Major synchrotron and structural biology research facilities worldwide
    """
    National_Synchrotron_Light_Source_II = "NSLS_II"
    """
    Fourth-generation synchrotron light source at Brookhaven National Laboratory, Upton, NY, USA
    """
    Advanced_Light_Source = "ALS"
    """
    Third-generation synchrotron light source at Lawrence Berkeley National Laboratory, Berkeley, CA, USA
    """
    Stanford_Synchrotron_Radiation_Lightsource = "SSRL"
    """
    Synchrotron radiation facility at SLAC National Accelerator Laboratory, Menlo Park, CA, USA
    """
    European_Synchrotron_Radiation_Facility = "ESRF"
    """
    High-energy synchrotron facility in Grenoble, France - world's most intense X-ray source
    """
    Diamond_Light_Source = "DIAMOND"
    """
    UK's national synchrotron science facility at Harwell Science and Innovation Campus, Oxfordshire, UK
    """
    Photon_Factory = "PHOTON_FACTORY"
    """
    Synchrotron radiation facility at KEK (High Energy Accelerator Research Organization), Tsukuba, Japan
    """
    Advanced_Photon_Source = "APS"
    """
    High-energy synchrotron at Argonne National Laboratory, Lemont, IL, USA
    """
    SPring_8 = "SPRING8"
    """
    Large-scale synchrotron radiation facility in Harima Science Park City, Hyogo, Japan
    """
    PETRA_III = "PETRA_III"
    """
    High-brilliance synchrotron radiation source at DESY, Hamburg, Germany
    """
    Synchrotron_SOLEIL = "SOLEIL"
    """
    French national synchrotron facility near Paris, France
    """
    Australian_Synchrotron = "AUSTRALIAN_SYNCHROTRON"
    """
    Australia's national synchrotron facility in Melbourne, Victoria
    """
    SIBYLS_Beamline_12FULL_STOP3FULL_STOP1 = "SIBYLS"
    """
    Integrated structural biology beamline at ALS for SAXS, X-ray crystallography, and fiber diffraction
    """


class SampleTypeEnum(str, Enum):
    """
    Types of biological samples
    """
    protein = "protein"
    """
    Protein sample
    """
    nucleic_acid = "nucleic_acid"
    """
    Nucleic acid sample (DNA or RNA)
    """
    complex = "complex"
    """
    Protein-protein or protein-nucleic acid complex
    """
    membrane_protein = "membrane_protein"
    """
    Membrane protein sample
    """
    virus = "virus"
    """
    Viral particle
    """
    organelle = "organelle"
    """
    Cellular organelle
    """


class ConcentrationUnitEnum(str, Enum):
    """
    Units for concentration measurement
    """
    mg_per_ml = "mg_per_ml"
    """
    Milligrams per milliliter
    """
    micromolar = "micromolar"
    """
    Micromolar
    """
    millimolar = "millimolar"
    """
    Millimolar
    """
    nanomolar = "nanomolar"
    """
    Nanomolar
    """


class TemperatureUnitEnum(str, Enum):
    """
    Units for temperature measurement
    """
    celsius = "celsius"
    """
    Degrees Celsius
    """
    kelvin = "kelvin"
    """
    Kelvin
    """
    fahrenheit = "fahrenheit"
    """
    Degrees Fahrenheit
    """


class PreparationTypeEnum(str, Enum):
    """
    Types of sample preparation
    """
    cryo_em = "cryo_em"
    """
    Cryo-EM preparation
    """
    xray_crystallography = "xray_crystallography"
    """
    X-ray crystallography preparation
    """
    saxs = "saxs"
    """
    SAXS/WAXS preparation
    """
    sans = "sans"
    """
    SANS preparation
    """
    protein_expression = "protein_expression"
    """
    Protein expression in host cells
    """
    protein_purification = "protein_purification"
    """
    Protein purification
    """
    negative_stain = "negative_stain"
    """
    Negative stain EM preparation
    """


class GridTypeEnum(str, Enum):
    """
    Types of EM grids
    """
    c_flat = "c_flat"
    """
    C-flat holey carbon grid
    """
    quantifoil = "quantifoil"
    """
    Quantifoil holey carbon grid
    """
    lacey_carbon = "lacey_carbon"
    """
    Lacey carbon grid
    """
    ultrathin_carbon = "ultrathin_carbon"
    """
    Ultrathin carbon film
    """
    gold = "gold"
    """
    Gold grid
    """


class GridMaterialEnum(str, Enum):
    """
    Materials used for EM grids
    """
    carbon = "carbon"
    """
    Carbon grid
    """
    gold = "gold"
    """
    Gold grid
    """
    graphene = "graphene"
    """
    Graphene grid
    """
    silicon_nitride = "silicon_nitride"
    """
    Silicon nitride grid
    """


class VitrificationMethodEnum(str, Enum):
    """
    Methods for vitrification
    """
    plunge_freezing = "plunge_freezing"
    """
    Plunge freezing in liquid ethane
    """
    high_pressure_freezing = "high_pressure_freezing"
    """
    High pressure freezing
    """
    slam_freezing = "slam_freezing"
    """
    Slam freezing
    """


class SymmetryEnum(str, Enum):
    """
    Crystallographic and non-crystallographic symmetry groups for cryo-EM
    """
    C1 = "C1"
    """
    C1 symmetry (no symmetry)
    """
    C2 = "C2"
    """
    C2 cyclic symmetry (2-fold)
    """
    C3 = "C3"
    """
    C3 cyclic symmetry (3-fold)
    """
    C4 = "C4"
    """
    C4 cyclic symmetry (4-fold)
    """
    C5 = "C5"
    """
    C5 cyclic symmetry (5-fold)
    """
    C6 = "C6"
    """
    C6 cyclic symmetry (6-fold)
    """
    C7 = "C7"
    """
    C7 cyclic symmetry (7-fold)
    """
    C8 = "C8"
    """
    C8 cyclic symmetry (8-fold)
    """
    C9 = "C9"
    """
    C9 cyclic symmetry (9-fold)
    """
    C10 = "C10"
    """
    C10 cyclic symmetry (10-fold)
    """
    D2 = "D2"
    """
    D2 dihedral symmetry (2-fold)
    """
    D3 = "D3"
    """
    D3 dihedral symmetry (3-fold)
    """
    D4 = "D4"
    """
    D4 dihedral symmetry (4-fold)
    """
    D5 = "D5"
    """
    D5 dihedral symmetry (5-fold)
    """
    D6 = "D6"
    """
    D6 dihedral symmetry (6-fold)
    """
    D7 = "D7"
    """
    D7 dihedral symmetry (7-fold)
    """
    D8 = "D8"
    """
    D8 dihedral symmetry (8-fold)
    """
    D9 = "D9"
    """
    D9 dihedral symmetry (9-fold)
    """
    D10 = "D10"
    """
    D10 dihedral symmetry (10-fold)
    """
    T = "T"
    """
    Tetrahedral symmetry
    """
    O = "O"
    """
    Octahedral symmetry
    """
    I = "I"
    """
    Icosahedral symmetry
    """


class CrystallizationMethodEnum(str, Enum):
    """
    Methods for protein crystallization
    """
    vapor_diffusion_hanging = "vapor_diffusion_hanging"
    """
    Vapor diffusion hanging drop
    """
    vapor_diffusion_sitting = "vapor_diffusion_sitting"
    """
    Vapor diffusion sitting drop
    """
    batch = "batch"
    """
    Batch crystallization
    """
    microbatch = "microbatch"
    """
    Microbatch under oil
    """
    lcp = "lcp"
    """
    Lipidic cubic phase (LCP)
    """
    dialysis = "dialysis"
    """
    Dialysis method
    """
    free_interface_diffusion = "free_interface_diffusion"
    """
    Free interface diffusion
    """


class InstrumentStatusEnum(str, Enum):
    """
    Operational status of instruments
    """
    operational = "operational"
    """
    Instrument is operational
    """
    maintenance = "maintenance"
    """
    Instrument under maintenance
    """
    offline = "offline"
    """
    Instrument is offline
    """
    commissioning = "commissioning"
    """
    Instrument being commissioned
    """


class ImagingModeEnum(str, Enum):
    """
    Imaging modes for electron microscopy
    """
    EFTEM = "EFTEM"
    """
    Energy-filtered transmission electron microscopy
    """
    TEM = "TEM"
    """
    Transmission electron microscopy
    """
    STEM = "STEM"
    """
    Scanning transmission electron microscopy
    """


class DetectorTypeEnum(str, Enum):
    """
    DEPRECATED: Use DetectorTechnologyEnum instead. Legacy enum mixing technologies and brands.
    """
    direct_electron = "direct_electron"
    """
    Direct electron detector
    """
    ccd = "ccd"
    """
    CCD camera
    """
    cmos = "cmos"
    """
    CMOS detector
    """
    hybrid_pixel = "hybrid_pixel"
    """
    Hybrid pixel detector
    """
    eiger = "eiger"
    """
    Dectris EIGER detector (hybrid photon counting)
    """
    pilatus = "pilatus"
    """
    Dectris PILATUS detector
    """
    rayonix = "rayonix"
    """
    Rayonix CCD detector
    """
    adsc = "adsc"
    """
    ADSC CCD detector
    """
    mar = "mar"
    """
    MAR CCD or imaging plate detector
    """


class DetectorTechnologyEnum(str, Enum):
    """
    Generic detector technologies for structural biology imaging
    """
    direct_electron_detector = "direct_electron_detector"
    """
    Direct electron detector for cryo-EM (e.g., Gatan K2/K3, ThermoFisher Falcon, DirectElectron DE-64)
    """
    ccd = "ccd"
    """
    Charge-coupled device camera
    """
    cmos = "cmos"
    """
    Complementary metal-oxide-semiconductor detector
    """
    hybrid_photon_counting = "hybrid_photon_counting"
    """
    Hybrid pixel photon counting detector for X-ray crystallography
    """
    scintillator_coupled = "scintillator_coupled"
    """
    Scintillator-coupled indirect detection
    """
    imaging_plate = "imaging_plate"
    """
    Imaging plate detector
    """
    film = "film"
    """
    Photographic film
    """


class DetectorModeEnum(str, Enum):
    """
    Operating modes for detectors during data collection
    """
    counting = "counting"
    """
    Electron/photon counting mode
    """
    integrating = "integrating"
    """
    Integrating mode (analog)
    """
    super_resolution = "super_resolution"
    """
    Super-resolution mode with oversampling
    """
    linear = "linear"
    """
    Linear response mode
    """
    correlated_double_sampling = "correlated_double_sampling"
    """
    Correlated double sampling mode
    """


class XRaySourceTypeEnum(str, Enum):
    """
    Types of X-ray sources
    """
    synchrotron = "synchrotron"
    """
    Synchrotron radiation source
    """
    rotating_anode = "rotating_anode"
    """
    Rotating anode generator
    """
    microfocus = "microfocus"
    """
    Microfocus sealed tube
    """
    metal_jet = "metal_jet"
    """
    Liquid metal jet source
    """


class TechniqueEnum(str, Enum):
    """
    Structural biology techniques
    """
    cryo_em = "cryo_em"
    """
    Cryo-electron microscopy
    """
    xray_crystallography = "xray_crystallography"
    """
    X-ray crystallography
    """
    saxs = "saxs"
    """
    Small-angle X-ray scattering
    """
    waxs = "waxs"
    """
    Wide-angle X-ray scattering
    """
    sans = "sans"
    """
    Small-angle neutron scattering
    """
    cryo_et = "cryo_et"
    """
    Cryo-electron tomography
    """
    electron_microscopy = "electron_microscopy"
    """
    General electron microscopy
    """
    mass_spectrometry = "mass_spectrometry"
    """
    Mass spectrometry
    """


class ProcessingStatusEnum(str, Enum):
    """
    Processing status
    """
    raw = "raw"
    """
    Raw data
    """
    preprocessing = "preprocessing"
    """
    Being preprocessed
    """
    processing = "processing"
    """
    Being processed
    """
    completed = "completed"
    """
    Processing completed
    """
    failed = "failed"
    """
    Processing failed
    """


class WorkflowTypeEnum(str, Enum):
    """
    Types of processing workflows
    """
    motion_correction = "motion_correction"
    """
    Motion correction for cryo-EM
    """
    ctf_estimation = "ctf_estimation"
    """
    CTF estimation
    """
    particle_picking = "particle_picking"
    """
    Particle picking
    """
    classification_2d = "classification_2d"
    """
    2D classification
    """
    classification_3d = "classification_3d"
    """
    3D classification
    """
    refinement = "refinement"
    """
    3D refinement
    """
    model_building = "model_building"
    """
    Atomic model building
    """
    phasing = "phasing"
    """
    Phase determination
    """
    integration = "integration"
    """
    Data integration
    """
    scaling = "scaling"
    """
    Data scaling
    """
    saxs_analysis = "saxs_analysis"
    """
    SAXS data analysis
    """
    em_2d_classification = "em_2d_classification"
    """
    EM 2D classification
    """
    mass_spec_deconvolution = "mass_spec_deconvolution"
    """
    Mass spectrometry deconvolution
    """
    particle_extraction = "particle_extraction"
    """
    Particle extraction from micrographs
    """
    ab_initio = "ab_initio"
    """
    Ab initio 3D reconstruction
    """
    postprocessing = "postprocessing"
    """
    Map post-processing and sharpening
    """
    map_validation = "map_validation"
    """
    3D map validation
    """
    model_refinement = "model_refinement"
    """
    Atomic model refinement
    """
    model_validation = "model_validation"
    """
    Model validation and quality assessment
    """


class FileFormatEnum(str, Enum):
    """
    File formats
    """
    mrc = "mrc"
    """
    MRC format for EM data
    """
    tiff = "tiff"
    """
    TIFF image format
    """
    hdf5 = "hdf5"
    """
    HDF5 hierarchical data format
    """
    star = "star"
    """
    STAR format for metadata
    """
    pdb = "pdb"
    """
    PDB coordinate format
    """
    mmcif = "mmcif"
    """
    mmCIF format
    """
    mtz = "mtz"
    """
    MTZ reflection format
    """
    cbf = "cbf"
    """
    Crystallographic Binary Format
    """
    cbf_zst = "cbf_zst"
    """
    Zstandard-compressed CBF format
    """
    img = "img"
    """
    Generic diffraction image format
    """
    h5 = "h5"
    """
    HDF5 format (alternative extension)
    """
    ascii = "ascii"
    """
    ASCII text format
    """
    thermo_raw = "thermo_raw"
    """
    Thermo Fisher RAW format
    """
    zip = "zip"
    """
    ZIP compressed archive
    """
    mrcs = "mrcs"
    """
    MRC stack format for particle stacks
    """
    eer = "eer"
    """
    EER format for electron counting
    """
    cs = "cs"
    """
    CryoSPARC format
    """
    json = "json"
    """
    JSON data format
    """
    csv = "csv"
    """
    Comma-separated values format
    """
    ccp4 = "ccp4"
    """
    CCP4 map format
    """
    gz = "gz"
    """
    Gzip compressed format
    """


class DataTypeEnum(str, Enum):
    """
    Types of data
    """
    micrograph = "micrograph"
    """
    Electron micrograph
    """
    diffraction = "diffraction"
    """
    Diffraction pattern
    """
    scattering = "scattering"
    """
    Scattering data
    """
    particles = "particles"
    """
    Particle stack
    """
    volume = "volume"
    """
    3D volume
    """
    model = "model"
    """
    Atomic model
    """
    metadata = "metadata"
    """
    Metadata file
    """
    raw_data = "raw_data"
    """
    Raw experimental data
    """
    processed_data = "processed_data"
    """
    Processed data
    """
    movie = "movie"
    """
    Raw cryo-EM movie
    """
    motion_corrected = "motion_corrected"
    """
    Motion-corrected micrograph
    """
    ctf_estimation = "ctf_estimation"
    """
    CTF estimation results
    """
    particle_coordinates = "particle_coordinates"
    """
    Particle picking coordinates
    """
    class_averages = "class_averages"
    """
    2D or 3D class averages
    """
    fsc_curve = "fsc_curve"
    """
    Fourier Shell Correlation data
    """
    map_half = "map_half"
    """
    Half-map for gold-standard refinement
    """
    validation_report = "validation_report"
    """
    Validation report
    """


class CollectionModeEnum(str, Enum):
    """
    Data collection modes
    """
    counting = "counting"
    """
    Counting mode
    """
    super_resolution = "super_resolution"
    """
    Super-resolution mode
    """
    continuous = "continuous"
    """
    Continuous collection
    """
    oscillation = "oscillation"
    """
    Oscillation method
    """
    still = "still"
    """
    Still images
    """
    batch = "batch"
    """
    Batch mode collection
    """
    sec_saxs = "sec_saxs"
    """
    SEC-SAXS collection mode
    """
    single_particle = "single_particle"
    """
    Single particle analysis mode
    """


class IlluminationTypeEnum(str, Enum):
    """
    Types of illumination for optical microscopy
    """
    brightfield = "brightfield"
    """
    Brightfield illumination
    """
    darkfield = "darkfield"
    """
    Darkfield illumination
    """
    phase_contrast = "phase_contrast"
    """
    Phase contrast microscopy
    """
    dic = "dic"
    """
    Differential interference contrast (DIC/Nomarski)
    """
    fluorescence = "fluorescence"
    """
    Fluorescence illumination
    """
    confocal = "confocal"
    """
    Confocal laser scanning
    """
    polarized = "polarized"
    """
    Polarized light microscopy
    """
    oblique = "oblique"
    """
    Oblique illumination
    """


class ExpressionSystemEnum(str, Enum):
    """
    Expression systems for recombinant protein production
    """
    bacteria = "bacteria"
    """
    Bacterial expression (e.g., E. coli)
    """
    yeast = "yeast"
    """
    Yeast expression (e.g., S. cerevisiae, P. pastoris)
    """
    insect = "insect"
    """
    Insect cell expression (e.g., Sf9, High Five)
    """
    mammalian = "mammalian"
    """
    Mammalian cell expression (e.g., HEK293, CHO)
    """
    cell_free = "cell_free"
    """
    Cell-free expression system
    """


class PurificationStepEnum(str, Enum):
    """
    Protein purification steps and methods
    """
    affinity_ni_nta = "affinity_ni_nta"
    """
    Affinity chromatography using Ni-NTA resin
    """
    affinity_co_nta = "affinity_co_nta"
    """
    Affinity chromatography using Co-NTA resin
    """
    affinity_strep = "affinity_strep"
    """
    Affinity chromatography using Strep-tag
    """
    affinity_mbp = "affinity_mbp"
    """
    Affinity chromatography using maltose-binding protein (MBP)
    """
    affinity_gst = "affinity_gst"
    """
    Affinity chromatography using glutathione S-transferase (GST)
    """
    tag_cleavage = "tag_cleavage"
    """
    Proteolytic cleavage of purification tags
    """
    ion_exchange = "ion_exchange"
    """
    Ion-exchange chromatography (IEX)
    """
    hydrophobic_interaction = "hydrophobic_interaction"
    """
    Hydrophobic interaction chromatography (HIC)
    """
    size_exclusion = "size_exclusion"
    """
    Size-exclusion chromatography (SEC)
    """
    dialysis = "dialysis"
    """
    Dialysis or buffer exchange
    """


class PhasingMethodEnum(str, Enum):
    """
    Methods for phase determination in X-ray crystallography
    """
    molecular_replacement = "molecular_replacement"
    """
    Molecular replacement (MR)
    """
    sad = "sad"
    """
    Single-wavelength anomalous diffraction (SAD)
    """
    mad = "mad"
    """
    Multi-wavelength anomalous diffraction (MAD)
    """
    sir = "sir"
    """
    Single isomorphous replacement (SIR)
    """
    mir = "mir"
    """
    Multiple isomorphous replacement (MIR)
    """
    siras = "siras"
    """
    Single isomorphous replacement with anomalous scattering (SIRAS)
    """
    miras = "miras"
    """
    Multiple isomorphous replacement with anomalous scattering (MIRAS)
    """
    fragile_mr = "fragile_mr"
    """
    Fragile molecular replacement or ensemble-based MR
    """


class ExperimentalMethodEnum(str, Enum):
    """
    Experimental methods for structure determination
    """
    x_ray_diffraction = "x_ray_diffraction"
    """
    X-ray diffraction
    """
    neutron_diffraction = "neutron_diffraction"
    """
    Neutron diffraction
    """
    electron_diffraction = "electron_diffraction"
    """
    Electron diffraction (e.g., microED)
    """
    fiber_diffraction = "fiber_diffraction"
    """
    Fiber diffraction
    """



class NamedThing(ConfiguredBaseModel):
    """
    A named thing
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class ProteinAnnotation(NamedThing):
    """
    Base class for all protein-related functional and structural annotations
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    protein_id: str = Field(default=..., description="""UniProt accession number""", json_schema_extra = { "linkml_meta": {'alias': 'protein_id',
         'domain_of': ['ProteinAnnotation', 'ConformationalEnsemble']} })
    pdb_entry: Optional[str] = Field(default=None, description="""PDB identifier""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entry', 'domain_of': ['ProteinAnnotation']} })
    chain_id: Optional[str] = Field(default=None, description="""Chain identifier in the PDB structure""", json_schema_extra = { "linkml_meta": {'alias': 'chain_id', 'domain_of': ['ProteinAnnotation']} })
    residue_range: Optional[str] = Field(default=None, description="""Range of residues (e.g., '1-100', '25,27,30-35')""", json_schema_extra = { "linkml_meta": {'alias': 'residue_range', 'domain_of': ['ProteinAnnotation']} })
    confidence_score: Optional[float] = Field(default=None, description="""Confidence score for the annotation (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'confidence_score', 'domain_of': ['ProteinAnnotation']} })
    evidence_type: Optional[EvidenceTypeEnum] = Field(default=None, description="""Type of evidence supporting this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ProteinAnnotation']} })
    evidence_code: Optional[str] = Field(default=None, description="""Evidence and Conclusion Ontology (ECO) code""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_code', 'domain_of': ['ProteinAnnotation']} })
    source_database: Optional[AnnotationSourceEnum] = Field(default=None, description="""Source database or resource that provided this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'source_database', 'domain_of': ['ProteinAnnotation']} })
    annotation_method: Optional[str] = Field(default=None, description="""Computational or experimental method used""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_method', 'domain_of': ['ProteinAnnotation']} })
    publication_ids: Optional[list[str]] = Field(default=None, description="""IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'publication_ids', 'domain_of': ['ProteinAnnotation']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })

    @field_validator('protein_id')
    def pattern_protein_id(cls, v):
        pattern=re.compile(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid protein_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid protein_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('pdb_entry')
    def pattern_pdb_entry(cls, v):
        pattern=re.compile(r"^[0-9][A-Za-z0-9]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pdb_entry format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pdb_entry format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chain_id')
    def pattern_chain_id(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chain_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chain_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('residue_range')
    def pattern_residue_range(cls, v):
        pattern=re.compile(r"^[0-9,\-]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid residue_range format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid residue_range format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publication_ids')
    def pattern_publication_ids(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publication_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publication_ids format: {v}"
            raise ValueError(err_msg)
        return v


class FunctionalSite(ProteinAnnotation):
    """
    Functional sites including catalytic, binding, and regulatory sites
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    site_type: FunctionalSiteTypeEnum = Field(default=..., description="""Type of functional site""", json_schema_extra = { "linkml_meta": {'alias': 'site_type', 'domain_of': ['FunctionalSite']} })
    site_name: Optional[str] = Field(default=None, description="""Common name for this site""", json_schema_extra = { "linkml_meta": {'alias': 'site_name', 'domain_of': ['FunctionalSite']} })
    residues: Optional[list[str]] = Field(default=None, description="""List of residues forming the functional site. Each should be specified as a string (e.g., \"45\", \"120A\").""", json_schema_extra = { "linkml_meta": {'alias': 'residues', 'domain_of': ['FunctionalSite']} })
    ligand_interactions: Optional[list[LigandInteraction]] = Field(default=None, description="""Ligands that interact with this site""", json_schema_extra = { "linkml_meta": {'alias': 'ligand_interactions',
         'domain_of': ['FunctionalSite', 'AggregatedProteinView', 'Sample']} })
    conservation_score: Optional[float] = Field(default=None, description="""Evolutionary conservation score (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'conservation_score',
         'domain_of': ['FunctionalSite', 'EvolutionaryConservation']} })
    functional_importance: Optional[str] = Field(default=None, description="""Description of functional importance""", json_schema_extra = { "linkml_meta": {'alias': 'functional_importance', 'domain_of': ['FunctionalSite']} })
    go_terms: Optional[list[str]] = Field(default=None, description="""Associated Gene Ontology terms""", json_schema_extra = { "linkml_meta": {'alias': 'go_terms', 'domain_of': ['FunctionalSite']} })
    ec_number: Optional[str] = Field(default=None, description="""Enzyme Commission number for catalytic sites""", json_schema_extra = { "linkml_meta": {'alias': 'ec_number', 'domain_of': ['FunctionalSite']} })
    protein_id: str = Field(default=..., description="""UniProt accession number""", json_schema_extra = { "linkml_meta": {'alias': 'protein_id',
         'domain_of': ['ProteinAnnotation', 'ConformationalEnsemble']} })
    pdb_entry: Optional[str] = Field(default=None, description="""PDB identifier""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entry', 'domain_of': ['ProteinAnnotation']} })
    chain_id: Optional[str] = Field(default=None, description="""Chain identifier in the PDB structure""", json_schema_extra = { "linkml_meta": {'alias': 'chain_id', 'domain_of': ['ProteinAnnotation']} })
    residue_range: Optional[str] = Field(default=None, description="""Range of residues (e.g., '1-100', '25,27,30-35')""", json_schema_extra = { "linkml_meta": {'alias': 'residue_range', 'domain_of': ['ProteinAnnotation']} })
    confidence_score: Optional[float] = Field(default=None, description="""Confidence score for the annotation (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'confidence_score', 'domain_of': ['ProteinAnnotation']} })
    evidence_type: Optional[EvidenceTypeEnum] = Field(default=None, description="""Type of evidence supporting this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ProteinAnnotation']} })
    evidence_code: Optional[str] = Field(default=None, description="""Evidence and Conclusion Ontology (ECO) code""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_code', 'domain_of': ['ProteinAnnotation']} })
    source_database: Optional[AnnotationSourceEnum] = Field(default=None, description="""Source database or resource that provided this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'source_database', 'domain_of': ['ProteinAnnotation']} })
    annotation_method: Optional[str] = Field(default=None, description="""Computational or experimental method used""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_method', 'domain_of': ['ProteinAnnotation']} })
    publication_ids: Optional[list[str]] = Field(default=None, description="""IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'publication_ids', 'domain_of': ['ProteinAnnotation']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })

    @field_validator('ec_number')
    def pattern_ec_number(cls, v):
        pattern=re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ec_number format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ec_number format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('protein_id')
    def pattern_protein_id(cls, v):
        pattern=re.compile(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid protein_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid protein_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('pdb_entry')
    def pattern_pdb_entry(cls, v):
        pattern=re.compile(r"^[0-9][A-Za-z0-9]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pdb_entry format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pdb_entry format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chain_id')
    def pattern_chain_id(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chain_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chain_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('residue_range')
    def pattern_residue_range(cls, v):
        pattern=re.compile(r"^[0-9,\-]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid residue_range format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid residue_range format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publication_ids')
    def pattern_publication_ids(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publication_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publication_ids format: {v}"
            raise ValueError(err_msg)
        return v


class StructuralFeature(ProteinAnnotation):
    """
    Structural features and properties of protein regions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    feature_type: StructuralFeatureTypeEnum = Field(default=..., description="""Type of structural feature""", json_schema_extra = { "linkml_meta": {'alias': 'feature_type', 'domain_of': ['StructuralFeature']} })
    secondary_structure: Optional[SecondaryStructureEnum] = Field(default=None, description="""Secondary structure assignment""", json_schema_extra = { "linkml_meta": {'alias': 'secondary_structure', 'domain_of': ['StructuralFeature']} })
    solvent_accessibility: Optional[float] = Field(default=None, description="""Relative solvent accessible surface area (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'solvent_accessibility', 'domain_of': ['StructuralFeature']} })
    backbone_flexibility: Optional[float] = Field(default=None, description="""B-factor or flexibility measure""", json_schema_extra = { "linkml_meta": {'alias': 'backbone_flexibility', 'domain_of': ['StructuralFeature']} })
    disorder_probability: Optional[float] = Field(default=None, description="""Probability of disorder (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'disorder_probability', 'domain_of': ['StructuralFeature']} })
    conformational_state: Optional[ConformationalStateEnum] = Field(default=None, description="""Conformational state descriptor""", json_schema_extra = { "linkml_meta": {'alias': 'conformational_state', 'domain_of': ['StructuralFeature']} })
    structural_motif: Optional[str] = Field(default=None, description="""Known structural motif""", json_schema_extra = { "linkml_meta": {'alias': 'structural_motif', 'domain_of': ['StructuralFeature']} })
    domain_assignment: Optional[str] = Field(default=None, description="""Domain database assignment (CATH, SCOP, Pfam)""", json_schema_extra = { "linkml_meta": {'alias': 'domain_assignment', 'domain_of': ['StructuralFeature']} })
    domain_id: Optional[str] = Field(default=None, description="""Domain identifier from domain database""", json_schema_extra = { "linkml_meta": {'alias': 'domain_id', 'domain_of': ['StructuralFeature']} })
    protein_id: str = Field(default=..., description="""UniProt accession number""", json_schema_extra = { "linkml_meta": {'alias': 'protein_id',
         'domain_of': ['ProteinAnnotation', 'ConformationalEnsemble']} })
    pdb_entry: Optional[str] = Field(default=None, description="""PDB identifier""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entry', 'domain_of': ['ProteinAnnotation']} })
    chain_id: Optional[str] = Field(default=None, description="""Chain identifier in the PDB structure""", json_schema_extra = { "linkml_meta": {'alias': 'chain_id', 'domain_of': ['ProteinAnnotation']} })
    residue_range: Optional[str] = Field(default=None, description="""Range of residues (e.g., '1-100', '25,27,30-35')""", json_schema_extra = { "linkml_meta": {'alias': 'residue_range', 'domain_of': ['ProteinAnnotation']} })
    confidence_score: Optional[float] = Field(default=None, description="""Confidence score for the annotation (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'confidence_score', 'domain_of': ['ProteinAnnotation']} })
    evidence_type: Optional[EvidenceTypeEnum] = Field(default=None, description="""Type of evidence supporting this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ProteinAnnotation']} })
    evidence_code: Optional[str] = Field(default=None, description="""Evidence and Conclusion Ontology (ECO) code""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_code', 'domain_of': ['ProteinAnnotation']} })
    source_database: Optional[AnnotationSourceEnum] = Field(default=None, description="""Source database or resource that provided this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'source_database', 'domain_of': ['ProteinAnnotation']} })
    annotation_method: Optional[str] = Field(default=None, description="""Computational or experimental method used""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_method', 'domain_of': ['ProteinAnnotation']} })
    publication_ids: Optional[list[str]] = Field(default=None, description="""IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'publication_ids', 'domain_of': ['ProteinAnnotation']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })

    @field_validator('protein_id')
    def pattern_protein_id(cls, v):
        pattern=re.compile(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid protein_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid protein_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('pdb_entry')
    def pattern_pdb_entry(cls, v):
        pattern=re.compile(r"^[0-9][A-Za-z0-9]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pdb_entry format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pdb_entry format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chain_id')
    def pattern_chain_id(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chain_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chain_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('residue_range')
    def pattern_residue_range(cls, v):
        pattern=re.compile(r"^[0-9,\-]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid residue_range format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid residue_range format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publication_ids')
    def pattern_publication_ids(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publication_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publication_ids format: {v}"
            raise ValueError(err_msg)
        return v


class ProteinProteinInteraction(ProteinAnnotation):
    """
    Protein-protein interactions and interfaces
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    partner_protein_id: str = Field(default=..., description="""UniProt ID of interacting partner""", json_schema_extra = { "linkml_meta": {'alias': 'partner_protein_id', 'domain_of': ['ProteinProteinInteraction']} })
    partner_chain_id: Optional[str] = Field(default=None, description="""Chain ID of interacting partner""", json_schema_extra = { "linkml_meta": {'alias': 'partner_chain_id', 'domain_of': ['ProteinProteinInteraction']} })
    interface_residues: Optional[list[str]] = Field(default=None, description="""Residues at the interaction interface""", json_schema_extra = { "linkml_meta": {'alias': 'interface_residues', 'domain_of': ['ProteinProteinInteraction']} })
    partner_interface_residues: Optional[list[str]] = Field(default=None, description="""Partner residues at the interaction interface""", json_schema_extra = { "linkml_meta": {'alias': 'partner_interface_residues',
         'domain_of': ['ProteinProteinInteraction']} })
    interface_area: Optional[float] = Field(default=None, description="""Buried surface area at interface (Ų)""", json_schema_extra = { "linkml_meta": {'alias': 'interface_area',
         'domain_of': ['ProteinProteinInteraction'],
         'unit': {'ucum_code': 'Angstrom2'}} })
    binding_energy: Optional[float] = Field(default=None, description="""Calculated binding energy (kcal/mol)""", json_schema_extra = { "linkml_meta": {'alias': 'binding_energy',
         'domain_of': ['ProteinProteinInteraction'],
         'unit': {'ucum_code': 'kcal/mol'}} })
    dissociation_constant: Optional[float] = Field(default=None, description="""Experimental Kd if available""", json_schema_extra = { "linkml_meta": {'alias': 'dissociation_constant', 'domain_of': ['ProteinProteinInteraction']} })
    complex_stability: Optional[ComplexStabilityEnum] = Field(default=None, description="""Stability assessment of the complex""", json_schema_extra = { "linkml_meta": {'alias': 'complex_stability', 'domain_of': ['ProteinProteinInteraction']} })
    biological_assembly: Optional[bool] = Field(default=None, description="""Whether this represents a biological assembly""", json_schema_extra = { "linkml_meta": {'alias': 'biological_assembly', 'domain_of': ['ProteinProteinInteraction']} })
    interaction_evidence: Optional[list[InteractionEvidenceEnum]] = Field(default=None, description="""Evidence for this interaction""", json_schema_extra = { "linkml_meta": {'alias': 'interaction_evidence', 'domain_of': ['ProteinProteinInteraction']} })
    protein_id: str = Field(default=..., description="""UniProt accession number""", json_schema_extra = { "linkml_meta": {'alias': 'protein_id',
         'domain_of': ['ProteinAnnotation', 'ConformationalEnsemble']} })
    pdb_entry: Optional[str] = Field(default=None, description="""PDB identifier""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entry', 'domain_of': ['ProteinAnnotation']} })
    chain_id: Optional[str] = Field(default=None, description="""Chain identifier in the PDB structure""", json_schema_extra = { "linkml_meta": {'alias': 'chain_id', 'domain_of': ['ProteinAnnotation']} })
    residue_range: Optional[str] = Field(default=None, description="""Range of residues (e.g., '1-100', '25,27,30-35')""", json_schema_extra = { "linkml_meta": {'alias': 'residue_range', 'domain_of': ['ProteinAnnotation']} })
    confidence_score: Optional[float] = Field(default=None, description="""Confidence score for the annotation (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'confidence_score', 'domain_of': ['ProteinAnnotation']} })
    evidence_type: Optional[EvidenceTypeEnum] = Field(default=None, description="""Type of evidence supporting this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ProteinAnnotation']} })
    evidence_code: Optional[str] = Field(default=None, description="""Evidence and Conclusion Ontology (ECO) code""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_code', 'domain_of': ['ProteinAnnotation']} })
    source_database: Optional[AnnotationSourceEnum] = Field(default=None, description="""Source database or resource that provided this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'source_database', 'domain_of': ['ProteinAnnotation']} })
    annotation_method: Optional[str] = Field(default=None, description="""Computational or experimental method used""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_method', 'domain_of': ['ProteinAnnotation']} })
    publication_ids: Optional[list[str]] = Field(default=None, description="""IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'publication_ids', 'domain_of': ['ProteinAnnotation']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })

    @field_validator('protein_id')
    def pattern_protein_id(cls, v):
        pattern=re.compile(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid protein_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid protein_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('pdb_entry')
    def pattern_pdb_entry(cls, v):
        pattern=re.compile(r"^[0-9][A-Za-z0-9]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pdb_entry format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pdb_entry format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chain_id')
    def pattern_chain_id(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chain_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chain_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('residue_range')
    def pattern_residue_range(cls, v):
        pattern=re.compile(r"^[0-9,\-]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid residue_range format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid residue_range format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publication_ids')
    def pattern_publication_ids(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publication_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publication_ids format: {v}"
            raise ValueError(err_msg)
        return v


class MutationEffect(ProteinAnnotation):
    """
    Effects of mutations and variants on protein structure and function
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    mutation: str = Field(default=..., description="""Mutation in standard notation (e.g., 'A123V')""", json_schema_extra = { "linkml_meta": {'alias': 'mutation', 'domain_of': ['MutationEffect']} })
    mutation_type: Optional[MutationTypeEnum] = Field(default=None, description="""Type of mutation""", json_schema_extra = { "linkml_meta": {'alias': 'mutation_type', 'domain_of': ['MutationEffect']} })
    effect_on_stability: Optional[StabilityEffectEnum] = Field(default=None, description="""Effect on protein stability""", json_schema_extra = { "linkml_meta": {'alias': 'effect_on_stability', 'domain_of': ['MutationEffect']} })
    delta_delta_g: Optional[float] = Field(default=None, description="""Change in folding free energy (kcal/mol)""", json_schema_extra = { "linkml_meta": {'alias': 'delta_delta_g',
         'domain_of': ['MutationEffect'],
         'unit': {'ucum_code': 'kcal/mol'}} })
    effect_on_function: Optional[FunctionalEffectEnum] = Field(default=None, description="""Effect on protein function""", json_schema_extra = { "linkml_meta": {'alias': 'effect_on_function', 'domain_of': ['MutationEffect']} })
    functional_impact_description: Optional[str] = Field(default=None, description="""Description of functional impact""", json_schema_extra = { "linkml_meta": {'alias': 'functional_impact_description', 'domain_of': ['MutationEffect']} })
    disease_association: Optional[str] = Field(default=None, description="""Associated disease or phenotype""", json_schema_extra = { "linkml_meta": {'alias': 'disease_association', 'domain_of': ['MutationEffect']} })
    omim_id: Optional[str] = Field(default=None, description="""OMIM database identifier""", json_schema_extra = { "linkml_meta": {'alias': 'omim_id', 'domain_of': ['MutationEffect']} })
    clinical_significance: Optional[ClinicalSignificanceEnum] = Field(default=None, description="""Clinical significance""", json_schema_extra = { "linkml_meta": {'alias': 'clinical_significance', 'domain_of': ['MutationEffect']} })
    allele_frequency: Optional[float] = Field(default=None, description="""Population allele frequency (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'allele_frequency', 'domain_of': ['MutationEffect']} })
    protein_id: str = Field(default=..., description="""UniProt accession number""", json_schema_extra = { "linkml_meta": {'alias': 'protein_id',
         'domain_of': ['ProteinAnnotation', 'ConformationalEnsemble']} })
    pdb_entry: Optional[str] = Field(default=None, description="""PDB identifier""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entry', 'domain_of': ['ProteinAnnotation']} })
    chain_id: Optional[str] = Field(default=None, description="""Chain identifier in the PDB structure""", json_schema_extra = { "linkml_meta": {'alias': 'chain_id', 'domain_of': ['ProteinAnnotation']} })
    residue_range: Optional[str] = Field(default=None, description="""Range of residues (e.g., '1-100', '25,27,30-35')""", json_schema_extra = { "linkml_meta": {'alias': 'residue_range', 'domain_of': ['ProteinAnnotation']} })
    confidence_score: Optional[float] = Field(default=None, description="""Confidence score for the annotation (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'confidence_score', 'domain_of': ['ProteinAnnotation']} })
    evidence_type: Optional[EvidenceTypeEnum] = Field(default=None, description="""Type of evidence supporting this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ProteinAnnotation']} })
    evidence_code: Optional[str] = Field(default=None, description="""Evidence and Conclusion Ontology (ECO) code""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_code', 'domain_of': ['ProteinAnnotation']} })
    source_database: Optional[AnnotationSourceEnum] = Field(default=None, description="""Source database or resource that provided this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'source_database', 'domain_of': ['ProteinAnnotation']} })
    annotation_method: Optional[str] = Field(default=None, description="""Computational or experimental method used""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_method', 'domain_of': ['ProteinAnnotation']} })
    publication_ids: Optional[list[str]] = Field(default=None, description="""IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'publication_ids', 'domain_of': ['ProteinAnnotation']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })

    @field_validator('mutation')
    def pattern_mutation(cls, v):
        pattern=re.compile(r"^[A-Z][0-9]+[A-Z]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid mutation format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid mutation format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('omim_id')
    def pattern_omim_id(cls, v):
        pattern=re.compile(r"^[0-9]{6}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid omim_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid omim_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('protein_id')
    def pattern_protein_id(cls, v):
        pattern=re.compile(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid protein_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid protein_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('pdb_entry')
    def pattern_pdb_entry(cls, v):
        pattern=re.compile(r"^[0-9][A-Za-z0-9]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pdb_entry format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pdb_entry format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chain_id')
    def pattern_chain_id(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chain_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chain_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('residue_range')
    def pattern_residue_range(cls, v):
        pattern=re.compile(r"^[0-9,\-]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid residue_range format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid residue_range format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publication_ids')
    def pattern_publication_ids(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publication_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publication_ids format: {v}"
            raise ValueError(err_msg)
        return v


class ConformationalEnsemble(NamedThing):
    """
    Ensemble of conformational states for a protein
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    protein_id: str = Field(default=..., description="""UniProt accession""", json_schema_extra = { "linkml_meta": {'alias': 'protein_id',
         'domain_of': ['ProteinAnnotation', 'ConformationalEnsemble']} })
    conformational_states: Optional[list[ConformationalState]] = Field(default=None, description="""Individual conformational states""", json_schema_extra = { "linkml_meta": {'alias': 'conformational_states', 'domain_of': ['ConformationalEnsemble']} })
    clustering_method: Optional[str] = Field(default=None, description="""Method used for conformational clustering""", json_schema_extra = { "linkml_meta": {'alias': 'clustering_method', 'domain_of': ['ConformationalEnsemble']} })
    rmsd_threshold: Optional[float] = Field(default=None, description="""RMSD threshold for clustering (Angstroms)""", json_schema_extra = { "linkml_meta": {'alias': 'rmsd_threshold',
         'domain_of': ['ConformationalEnsemble'],
         'unit': {'ucum_code': 'Angstrom'}} })
    transition_pathways: Optional[str] = Field(default=None, description="""Description of transition pathways between states""", json_schema_extra = { "linkml_meta": {'alias': 'transition_pathways', 'domain_of': ['ConformationalEnsemble']} })
    energy_landscape: Optional[str] = Field(default=None, description="""Description of the energy landscape""", json_schema_extra = { "linkml_meta": {'alias': 'energy_landscape', 'domain_of': ['ConformationalEnsemble']} })
    principal_motions: Optional[list[str]] = Field(default=None, description="""Description of principal motions""", json_schema_extra = { "linkml_meta": {'alias': 'principal_motions', 'domain_of': ['ConformationalEnsemble']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class PostTranslationalModification(ProteinAnnotation):
    """
    Post-translational modifications observed or predicted
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    modification_type: PTMTypeEnum = Field(default=..., description="""Type of PTM""", json_schema_extra = { "linkml_meta": {'alias': 'modification_type', 'domain_of': ['PostTranslationalModification']} })
    modified_residue: str = Field(default=..., description="""Residue that is modified""", json_schema_extra = { "linkml_meta": {'alias': 'modified_residue', 'domain_of': ['PostTranslationalModification']} })
    modification_group: Optional[str] = Field(default=None, description="""Chemical group added (e.g., 'phosphate', 'methyl')""", json_schema_extra = { "linkml_meta": {'alias': 'modification_group', 'domain_of': ['PostTranslationalModification']} })
    mass_shift: Optional[float] = Field(default=None, description="""Mass change due to modification (Da)""", json_schema_extra = { "linkml_meta": {'alias': 'mass_shift',
         'domain_of': ['PostTranslationalModification'],
         'unit': {'ucum_code': 'Da'}} })
    functional_effect: Optional[str] = Field(default=None, description="""Known functional effect of this PTM""", json_schema_extra = { "linkml_meta": {'alias': 'functional_effect', 'domain_of': ['PostTranslationalModification']} })
    regulatory_role: Optional[str] = Field(default=None, description="""Role in regulation""", json_schema_extra = { "linkml_meta": {'alias': 'regulatory_role', 'domain_of': ['PostTranslationalModification']} })
    enzyme: Optional[str] = Field(default=None, description="""Enzyme responsible for modification""", json_schema_extra = { "linkml_meta": {'alias': 'enzyme', 'domain_of': ['PostTranslationalModification']} })
    removal_enzyme: Optional[str] = Field(default=None, description="""Enzyme that removes modification""", json_schema_extra = { "linkml_meta": {'alias': 'removal_enzyme', 'domain_of': ['PostTranslationalModification']} })
    protein_id: str = Field(default=..., description="""UniProt accession number""", json_schema_extra = { "linkml_meta": {'alias': 'protein_id',
         'domain_of': ['ProteinAnnotation', 'ConformationalEnsemble']} })
    pdb_entry: Optional[str] = Field(default=None, description="""PDB identifier""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entry', 'domain_of': ['ProteinAnnotation']} })
    chain_id: Optional[str] = Field(default=None, description="""Chain identifier in the PDB structure""", json_schema_extra = { "linkml_meta": {'alias': 'chain_id', 'domain_of': ['ProteinAnnotation']} })
    residue_range: Optional[str] = Field(default=None, description="""Range of residues (e.g., '1-100', '25,27,30-35')""", json_schema_extra = { "linkml_meta": {'alias': 'residue_range', 'domain_of': ['ProteinAnnotation']} })
    confidence_score: Optional[float] = Field(default=None, description="""Confidence score for the annotation (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'confidence_score', 'domain_of': ['ProteinAnnotation']} })
    evidence_type: Optional[EvidenceTypeEnum] = Field(default=None, description="""Type of evidence supporting this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ProteinAnnotation']} })
    evidence_code: Optional[str] = Field(default=None, description="""Evidence and Conclusion Ontology (ECO) code""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_code', 'domain_of': ['ProteinAnnotation']} })
    source_database: Optional[AnnotationSourceEnum] = Field(default=None, description="""Source database or resource that provided this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'source_database', 'domain_of': ['ProteinAnnotation']} })
    annotation_method: Optional[str] = Field(default=None, description="""Computational or experimental method used""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_method', 'domain_of': ['ProteinAnnotation']} })
    publication_ids: Optional[list[str]] = Field(default=None, description="""IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'publication_ids', 'domain_of': ['ProteinAnnotation']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })

    @field_validator('protein_id')
    def pattern_protein_id(cls, v):
        pattern=re.compile(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid protein_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid protein_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('pdb_entry')
    def pattern_pdb_entry(cls, v):
        pattern=re.compile(r"^[0-9][A-Za-z0-9]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pdb_entry format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pdb_entry format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chain_id')
    def pattern_chain_id(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chain_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chain_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('residue_range')
    def pattern_residue_range(cls, v):
        pattern=re.compile(r"^[0-9,\-]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid residue_range format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid residue_range format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publication_ids')
    def pattern_publication_ids(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publication_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publication_ids format: {v}"
            raise ValueError(err_msg)
        return v


class EvolutionaryConservation(ProteinAnnotation):
    """
    Evolutionary conservation information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    conservation_score: Optional[float] = Field(default=None, description="""Overall conservation score (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'conservation_score',
         'domain_of': ['FunctionalSite', 'EvolutionaryConservation']} })
    conserved_residues: Optional[list[str]] = Field(default=None, description="""Highly conserved residues""", json_schema_extra = { "linkml_meta": {'alias': 'conserved_residues', 'domain_of': ['EvolutionaryConservation']} })
    variable_residues: Optional[list[str]] = Field(default=None, description="""Highly variable residues""", json_schema_extra = { "linkml_meta": {'alias': 'variable_residues', 'domain_of': ['EvolutionaryConservation']} })
    conservation_method: Optional[str] = Field(default=None, description="""Method used for conservation analysis""", json_schema_extra = { "linkml_meta": {'alias': 'conservation_method', 'domain_of': ['EvolutionaryConservation']} })
    alignment_depth: Optional[int] = Field(default=None, description="""Number of sequences in alignment""", json_schema_extra = { "linkml_meta": {'alias': 'alignment_depth', 'domain_of': ['EvolutionaryConservation']} })
    taxonomic_range: Optional[str] = Field(default=None, description="""Taxonomic range of conservation""", json_schema_extra = { "linkml_meta": {'alias': 'taxonomic_range', 'domain_of': ['EvolutionaryConservation']} })
    coevolved_residues: Optional[list[str]] = Field(default=None, description="""Pairs of coevolved residues""", json_schema_extra = { "linkml_meta": {'alias': 'coevolved_residues', 'domain_of': ['EvolutionaryConservation']} })
    protein_id: str = Field(default=..., description="""UniProt accession number""", json_schema_extra = { "linkml_meta": {'alias': 'protein_id',
         'domain_of': ['ProteinAnnotation', 'ConformationalEnsemble']} })
    pdb_entry: Optional[str] = Field(default=None, description="""PDB identifier""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entry', 'domain_of': ['ProteinAnnotation']} })
    chain_id: Optional[str] = Field(default=None, description="""Chain identifier in the PDB structure""", json_schema_extra = { "linkml_meta": {'alias': 'chain_id', 'domain_of': ['ProteinAnnotation']} })
    residue_range: Optional[str] = Field(default=None, description="""Range of residues (e.g., '1-100', '25,27,30-35')""", json_schema_extra = { "linkml_meta": {'alias': 'residue_range', 'domain_of': ['ProteinAnnotation']} })
    confidence_score: Optional[float] = Field(default=None, description="""Confidence score for the annotation (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'confidence_score', 'domain_of': ['ProteinAnnotation']} })
    evidence_type: Optional[EvidenceTypeEnum] = Field(default=None, description="""Type of evidence supporting this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ProteinAnnotation']} })
    evidence_code: Optional[str] = Field(default=None, description="""Evidence and Conclusion Ontology (ECO) code""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_code', 'domain_of': ['ProteinAnnotation']} })
    source_database: Optional[AnnotationSourceEnum] = Field(default=None, description="""Source database or resource that provided this annotation""", json_schema_extra = { "linkml_meta": {'alias': 'source_database', 'domain_of': ['ProteinAnnotation']} })
    annotation_method: Optional[str] = Field(default=None, description="""Computational or experimental method used""", json_schema_extra = { "linkml_meta": {'alias': 'annotation_method', 'domain_of': ['ProteinAnnotation']} })
    publication_ids: Optional[list[str]] = Field(default=None, description="""IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.""", json_schema_extra = { "linkml_meta": {'alias': 'publication_ids', 'domain_of': ['ProteinAnnotation']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })

    @field_validator('protein_id')
    def pattern_protein_id(cls, v):
        pattern=re.compile(r"^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid protein_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid protein_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('pdb_entry')
    def pattern_pdb_entry(cls, v):
        pattern=re.compile(r"^[0-9][A-Za-z0-9]{3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid pdb_entry format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid pdb_entry format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('chain_id')
    def pattern_chain_id(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid chain_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid chain_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('residue_range')
    def pattern_residue_range(cls, v):
        pattern=re.compile(r"^[0-9,\-]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid residue_range format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid residue_range format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('publication_ids')
    def pattern_publication_ids(cls, v):
        pattern=re.compile(r"^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid publication_ids format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid publication_ids format: {v}"
            raise ValueError(err_msg)
        return v


class AggregatedProteinView(NamedThing):
    """
    Aggregated view of all structural and functional data for a protein
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    uniprot_id: str = Field(default=..., description="""UniProt accession""", json_schema_extra = { "linkml_meta": {'alias': 'uniprot_id',
         'domain_of': ['AggregatedProteinView', 'ProteinConstruct']} })
    protein_name: str = Field(default=..., description="""Protein name""", json_schema_extra = { "linkml_meta": {'alias': 'protein_name', 'domain_of': ['AggregatedProteinView', 'Sample']} })
    organism: Optional[str] = Field(default=None, description="""Source organism""", json_schema_extra = { "linkml_meta": {'alias': 'organism', 'domain_of': ['AggregatedProteinView', 'Sample']} })
    organism_id: Optional[int] = Field(default=None, description="""NCBI taxonomy ID""", json_schema_extra = { "linkml_meta": {'alias': 'organism_id', 'domain_of': ['AggregatedProteinView']} })
    pdb_entries: Optional[list[str]] = Field(default=None, description="""All PDB entries for this protein""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entries',
         'domain_of': ['ConformationalState', 'AggregatedProteinView']} })
    functional_sites: Optional[list[FunctionalSite]] = Field(default=None, description="""All functional site annotations""", json_schema_extra = { "linkml_meta": {'alias': 'functional_sites', 'domain_of': ['AggregatedProteinView', 'Sample']} })
    structural_features: Optional[list[StructuralFeature]] = Field(default=None, description="""All structural feature annotations""", json_schema_extra = { "linkml_meta": {'alias': 'structural_features',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    protein_interactions: Optional[list[ProteinProteinInteraction]] = Field(default=None, description="""All protein-protein interactions""", json_schema_extra = { "linkml_meta": {'alias': 'protein_interactions',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    ligand_interactions: Optional[list[LigandInteraction]] = Field(default=None, description="""All ligand interactions""", json_schema_extra = { "linkml_meta": {'alias': 'ligand_interactions',
         'domain_of': ['FunctionalSite', 'AggregatedProteinView', 'Sample']} })
    mutations: Optional[list[MutationEffect]] = Field(default=None, description="""All mutation annotations""", json_schema_extra = { "linkml_meta": {'alias': 'mutations', 'domain_of': ['AggregatedProteinView', 'Sample']} })
    ptms: Optional[list[PostTranslationalModification]] = Field(default=None, description="""All post-translational modifications""", json_schema_extra = { "linkml_meta": {'alias': 'ptms', 'domain_of': ['AggregatedProteinView']} })
    biophysical_properties: Optional[list[BiophysicalProperty]] = Field(default=None, description="""All biophysical properties""", json_schema_extra = { "linkml_meta": {'alias': 'biophysical_properties',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    conformational_ensemble: Optional[ConformationalEnsemble] = Field(default=None, description="""Conformational ensemble data""", json_schema_extra = { "linkml_meta": {'alias': 'conformational_ensemble',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    evolutionary_conservation: Optional[EvolutionaryConservation] = Field(default=None, description="""Conservation analysis""", json_schema_extra = { "linkml_meta": {'alias': 'evolutionary_conservation',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    cross_references: Optional[list[DatabaseCrossReference]] = Field(default=None, description="""Database cross-references""", json_schema_extra = { "linkml_meta": {'alias': 'cross_references', 'domain_of': ['AggregatedProteinView']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class MeasurementConditions(NamedThing):
    """
    Conditions under which biophysical measurements were made
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    buffer_composition: Optional[BufferComposition] = Field(default=None, description="""Composition of the buffer used""", json_schema_extra = { "linkml_meta": {'alias': 'buffer_composition',
         'domain_of': ['MeasurementConditions', 'Sample']} })
    ph: Optional[float] = Field(default=None, description="""pH value of the solution during measurement (range: 0-14)""", ge=0, le=14, json_schema_extra = { "linkml_meta": {'alias': 'ph', 'domain_of': ['MeasurementConditions', 'BufferComposition']} })
    ionic_strength: Optional[float] = Field(default=None, description="""Ionic strength in molar of material in solution""", json_schema_extra = { "linkml_meta": {'alias': 'ionic_strength',
         'domain_of': ['MeasurementConditions'],
         'unit': {'ucum_code': 'mol/L'}} })
    temperature: Optional[float] = Field(default=None, description="""Temperature in Kelvin during measurement""", json_schema_extra = { "linkml_meta": {'alias': 'temperature',
         'domain_of': ['MeasurementConditions',
                       'StorageConditions',
                       'ExperimentalConditions'],
         'unit': {'ucum_code': 'K'}} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class AttributeGroup(ConfiguredBaseModel):
    """
    A grouping of related data attributes that form a logical unit
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class LigandInteraction(AttributeGroup):
    """
    Small molecule/ligand interactions with proteins
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    ligand_id: str = Field(default=..., description="""Ligand identifier (ChEMBL, ChEBI, PubChem)""", json_schema_extra = { "linkml_meta": {'alias': 'ligand_id', 'domain_of': ['LigandInteraction']} })
    ligand_name: str = Field(default=..., description="""Common name of the ligand""", json_schema_extra = { "linkml_meta": {'alias': 'ligand_name', 'domain_of': ['LigandInteraction']} })
    ligand_smiles: Optional[str] = Field(default=None, description="""SMILES representation of the ligand""", json_schema_extra = { "linkml_meta": {'alias': 'ligand_smiles', 'domain_of': ['LigandInteraction']} })
    binding_affinity: Optional[float] = Field(default=None, description="""Binding affinity value""", json_schema_extra = { "linkml_meta": {'alias': 'binding_affinity', 'domain_of': ['LigandInteraction']} })
    binding_affinity_type: Optional[BindingAffinityTypeEnum] = Field(default=None, description="""Type of binding measurement (Kd, Ki, IC50)""", json_schema_extra = { "linkml_meta": {'alias': 'binding_affinity_type', 'domain_of': ['LigandInteraction']} })
    binding_affinity_unit: Optional[AffinityUnitEnum] = Field(default=None, description="""Unit of binding affinity""", json_schema_extra = { "linkml_meta": {'alias': 'binding_affinity_unit', 'domain_of': ['LigandInteraction']} })
    interaction_type: Optional[InteractionTypeEnum] = Field(default=None, description="""Type of interaction""", json_schema_extra = { "linkml_meta": {'alias': 'interaction_type', 'domain_of': ['LigandInteraction']} })
    binding_site_residues: Optional[list[str]] = Field(default=None, description="""Residues involved in ligand binding""", json_schema_extra = { "linkml_meta": {'alias': 'binding_site_residues', 'domain_of': ['LigandInteraction']} })
    is_cofactor: Optional[bool] = Field(default=None, description="""Whether the ligand is a cofactor""", json_schema_extra = { "linkml_meta": {'alias': 'is_cofactor', 'domain_of': ['LigandInteraction']} })
    is_drug_like: Optional[bool] = Field(default=None, description="""Whether the ligand has drug-like properties""", json_schema_extra = { "linkml_meta": {'alias': 'is_drug_like', 'domain_of': ['LigandInteraction']} })
    druggability_score: Optional[float] = Field(default=None, description="""Druggability score of the binding site (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'druggability_score', 'domain_of': ['LigandInteraction']} })
    interaction_distance: Optional[float] = Field(default=None, description="""Distance criteria for interaction (Angstroms)""", json_schema_extra = { "linkml_meta": {'alias': 'interaction_distance',
         'domain_of': ['LigandInteraction'],
         'unit': {'ucum_code': 'Angstrom'}} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class BiophysicalProperty(AttributeGroup):
    """
    Measured or calculated biophysical properties
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    property_type: BiophysicalPropertyEnum = Field(default=..., description="""Type of biophysical property""", json_schema_extra = { "linkml_meta": {'alias': 'property_type', 'domain_of': ['BiophysicalProperty']} })
    value: float = Field(default=..., description="""Numerical value of the property""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['BiophysicalProperty']} })
    unit: str = Field(default=..., description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['BiophysicalProperty']} })
    error: Optional[float] = Field(default=None, description="""Experimental error or uncertainty""", json_schema_extra = { "linkml_meta": {'alias': 'error', 'domain_of': ['BiophysicalProperty']} })
    measurement_conditions: Optional[list[MeasurementConditions]] = Field(default=None, description="""Conditions under which measurement was made. If multiple sets of conditions were used, this will represent that the same values were obtained under different conditions. If values differ under different conditions, separate BiophysicalProperty instances should be created.""", json_schema_extra = { "linkml_meta": {'alias': 'measurement_conditions', 'domain_of': ['BiophysicalProperty']} })
    experimental_method: Optional[BiophysicalMethodEnum] = Field(default=None, description="""Method used for measurement""", json_schema_extra = { "linkml_meta": {'alias': 'experimental_method',
         'domain_of': ['BiophysicalProperty', 'ExperimentRun']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class ConformationalState(AttributeGroup):
    """
    Individual conformational state
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    state_id: str = Field(default=..., description="""Identifier for this state""", json_schema_extra = { "linkml_meta": {'alias': 'state_id', 'domain_of': ['ConformationalState']} })
    state_name: Optional[str] = Field(default=None, description="""Descriptive name (e.g., 'open', 'closed')""", json_schema_extra = { "linkml_meta": {'alias': 'state_name', 'domain_of': ['ConformationalState']} })
    pdb_entries: Optional[list[str]] = Field(default=None, description="""PDB entries representing this state""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_entries',
         'domain_of': ['ConformationalState', 'AggregatedProteinView']} })
    population: Optional[float] = Field(default=None, description="""Relative population of this state (range: 0-1)""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'population', 'domain_of': ['ConformationalState']} })
    free_energy: Optional[float] = Field(default=None, description="""Relative free energy (kcal/mol)""", json_schema_extra = { "linkml_meta": {'alias': 'free_energy',
         'domain_of': ['ConformationalState'],
         'unit': {'ucum_code': 'kcal/mol'}} })
    rmsd_from_reference: Optional[float] = Field(default=None, description="""RMSD from reference structure""", json_schema_extra = { "linkml_meta": {'alias': 'rmsd_from_reference',
         'domain_of': ['ConformationalState'],
         'unit': {'ucum_code': 'Angstrom'}} })
    characteristic_features: Optional[list[str]] = Field(default=None, description="""Key features of this conformation""", json_schema_extra = { "linkml_meta": {'alias': 'characteristic_features', 'domain_of': ['ConformationalState']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class DatabaseCrossReference(AttributeGroup):
    """
    Cross-references to external databases
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/functional_annotation'})

    database_name: DatabaseNameEnum = Field(default=..., description="""Name of the external database""", json_schema_extra = { "linkml_meta": {'alias': 'database_name', 'domain_of': ['DatabaseCrossReference']} })
    database_id: str = Field(default=..., description="""Identifier in the external database""", json_schema_extra = { "linkml_meta": {'alias': 'database_id', 'domain_of': ['DatabaseCrossReference']} })
    database_url: Optional[str] = Field(default=None, description="""URL to the database entry""", json_schema_extra = { "linkml_meta": {'alias': 'database_url', 'domain_of': ['DatabaseCrossReference']} })
    last_updated: Optional[str] = Field(default=None, description="""Date of last update""", json_schema_extra = { "linkml_meta": {'alias': 'last_updated', 'domain_of': ['DatabaseCrossReference']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Dataset(NamedThing):
    """
    A collection of studies
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/', 'tree_root': True})

    keywords: Optional[list[str]] = Field(default=None, description="""Keywords or tags describing the dataset for search and categorization""", json_schema_extra = { "linkml_meta": {'alias': 'keywords', 'domain_of': ['Dataset']} })
    instruments: Optional[list[Instrument]] = Field(default=None, description="""Instruments used across all studies in this dataset""", json_schema_extra = { "linkml_meta": {'alias': 'instruments', 'domain_of': ['Dataset']} })
    studies: Optional[list[Study]] = Field(default=None, description="""Individual research studies contained in this dataset""", json_schema_extra = { "linkml_meta": {'alias': 'studies', 'domain_of': ['Dataset']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Study(NamedThing):
    """
    A focused research investigation that groups related samples, experiments, and data collection around a specific biological question or hypothesis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    protein_constructs: Optional[list[ProteinConstruct]] = Field(default=None, description="""Protein constructs and cloning information""", json_schema_extra = { "linkml_meta": {'alias': 'protein_constructs', 'domain_of': ['Study']} })
    samples: Optional[list[Sample]] = Field(default=None, description="""Experimental samples used in this study, including biological samples """, json_schema_extra = { "linkml_meta": {'alias': 'samples', 'domain_of': ['Study']} })
    sample_preparations: Optional[list[SamplePreparation]] = Field(default=None, description="""Sample preparation procedures performed in this study""", json_schema_extra = { "linkml_meta": {'alias': 'sample_preparations', 'domain_of': ['Study']} })
    instrument_runs: Optional[list[ExperimentRun]] = Field(default=None, description="""Experimental data collection runs performed in this study""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_runs', 'domain_of': ['Study']} })
    workflow_runs: Optional[list[WorkflowRun]] = Field(default=None, description="""Computational workflow executions for data processing in this study""", json_schema_extra = { "linkml_meta": {'alias': 'workflow_runs', 'domain_of': ['Study']} })
    data_files: Optional[list[DataFile]] = Field(default=None, description="""Data files generated or used in this study""", json_schema_extra = { "linkml_meta": {'alias': 'data_files', 'domain_of': ['Study']} })
    images: Optional[list[Image]] = Field(default=None, description="""Images acquired or generated in this study""", json_schema_extra = { "linkml_meta": {'alias': 'images', 'domain_of': ['Study']} })
    aggregated_protein_views: Optional[list[AggregatedProteinView]] = Field(default=None, description="""Aggregated functional and structural annotations for proteins in this study""", json_schema_extra = { "linkml_meta": {'alias': 'aggregated_protein_views', 'domain_of': ['Study']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Sample(NamedThing):
    """
    A biological sample used in structural biology experiments
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    sample_code: str = Field(default=..., description="""Human-friendly laboratory identifier or facility code for the sample (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference and tracking within laboratory workflows.""", json_schema_extra = { "linkml_meta": {'alias': 'sample_code', 'domain_of': ['Sample']} })
    sample_type: SampleTypeEnum = Field(default=..., description="""Type of biological sample""", json_schema_extra = { "linkml_meta": {'alias': 'sample_type', 'domain_of': ['Sample']} })
    molecular_composition: Optional[MolecularComposition] = Field(default=None, description="""Description of molecular composition including sequences, modifications, ligands""", json_schema_extra = { "linkml_meta": {'alias': 'molecular_composition', 'domain_of': ['Sample']} })
    molecular_weight: Optional[float] = Field(default=None, description="""Molecular weight in kDa""", json_schema_extra = { "linkml_meta": {'alias': 'molecular_weight',
         'domain_of': ['Sample'],
         'unit': {'ucum_code': 'kDa'}} })
    concentration: Optional[float] = Field(default=None, description="""Sample concentration in mg/mL or µM""", json_schema_extra = { "linkml_meta": {'alias': 'concentration', 'domain_of': ['Sample']} })
    concentration_unit: Optional[ConcentrationUnitEnum] = Field(default=None, description="""Unit of concentration measurement""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_unit', 'domain_of': ['Sample']} })
    buffer_composition: Optional[BufferComposition] = Field(default=None, description="""Buffer composition including pH, salts, additives""", json_schema_extra = { "linkml_meta": {'alias': 'buffer_composition',
         'domain_of': ['MeasurementConditions', 'Sample']} })
    preparation_method: Optional[str] = Field(default=None, description="""Method used to prepare the sample""", json_schema_extra = { "linkml_meta": {'alias': 'preparation_method', 'domain_of': ['Sample']} })
    storage_conditions: Optional[StorageConditions] = Field(default=None, description="""Storage conditions for the sample""", json_schema_extra = { "linkml_meta": {'alias': 'storage_conditions', 'domain_of': ['Sample']} })
    organism: Optional[str] = Field(default=None, description="""Source organism for the sample (e.g., NCBITaxon:3702 for Arabidopsis thaliana)""", json_schema_extra = { "linkml_meta": {'alias': 'organism', 'domain_of': ['AggregatedProteinView', 'Sample']} })
    anatomy: Optional[str] = Field(default=None, description="""Anatomical part or tissue (e.g., UBERON:0008945 for leaf)""", json_schema_extra = { "linkml_meta": {'alias': 'anatomy', 'domain_of': ['Sample']} })
    cell_type: Optional[str] = Field(default=None, description="""Cell type if applicable (e.g., CL:0000057 for fibroblast)""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type', 'domain_of': ['Sample']} })
    parent_sample_id: Optional[str] = Field(default=None, description="""Reference to parent sample for derivation tracking""", json_schema_extra = { "linkml_meta": {'alias': 'parent_sample_id', 'domain_of': ['Sample']} })
    purity_percentage: Optional[float] = Field(default=None, description="""Sample purity as percentage (range: 0-100)""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'alias': 'purity_percentage', 'domain_of': ['Sample']} })
    quality_metrics: Optional[str] = Field(default=None, description="""Quality control metrics for the sample""", json_schema_extra = { "linkml_meta": {'alias': 'quality_metrics', 'domain_of': ['Sample', 'ExperimentRun']} })
    functional_sites: Optional[list[FunctionalSite]] = Field(default=None, description="""Functional site annotations for proteins in the sample""", json_schema_extra = { "linkml_meta": {'alias': 'functional_sites', 'domain_of': ['AggregatedProteinView', 'Sample']} })
    structural_features: Optional[list[StructuralFeature]] = Field(default=None, description="""Structural feature annotations""", json_schema_extra = { "linkml_meta": {'alias': 'structural_features',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    protein_interactions: Optional[list[ProteinProteinInteraction]] = Field(default=None, description="""Protein-protein interaction annotations""", json_schema_extra = { "linkml_meta": {'alias': 'protein_interactions',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    ligand_interactions: Optional[list[LigandInteraction]] = Field(default=None, description="""Small molecule interaction annotations""", json_schema_extra = { "linkml_meta": {'alias': 'ligand_interactions',
         'domain_of': ['FunctionalSite', 'AggregatedProteinView', 'Sample']} })
    mutation_effects: Optional[list[MutationEffect]] = Field(default=None, description="""Effects of mutations present in the sample""", json_schema_extra = { "linkml_meta": {'alias': 'mutation_effects', 'domain_of': ['Sample']} })
    ptm_annotations: Optional[list[PostTranslationalModification]] = Field(default=None, description="""Post-translational modification annotations""", json_schema_extra = { "linkml_meta": {'alias': 'ptm_annotations', 'domain_of': ['Sample']} })
    biophysical_properties: Optional[list[BiophysicalProperty]] = Field(default=None, description="""Measured or predicted biophysical properties""", json_schema_extra = { "linkml_meta": {'alias': 'biophysical_properties',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    evolutionary_conservation: Optional[EvolutionaryConservation] = Field(default=None, description="""Evolutionary conservation data""", json_schema_extra = { "linkml_meta": {'alias': 'evolutionary_conservation',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    conformational_ensemble: Optional[ConformationalEnsemble] = Field(default=None, description="""Conformational states and dynamics""", json_schema_extra = { "linkml_meta": {'alias': 'conformational_ensemble',
         'domain_of': ['AggregatedProteinView', 'Sample']} })
    database_cross_references: Optional[list[DatabaseCrossReference]] = Field(default=None, description="""Cross-references to external databases""", json_schema_extra = { "linkml_meta": {'alias': 'database_cross_references', 'domain_of': ['Sample']} })
    protein_name: Optional[str] = Field(default=None, description="""Name of the protein""", json_schema_extra = { "linkml_meta": {'alias': 'protein_name',
         'comments': ['Maps to NSLS2 spreadsheet: Protein_Name'],
         'domain_of': ['AggregatedProteinView', 'Sample'],
         'slot_uri': 'nsls2:Protein_Name'} })
    construct: Optional[str] = Field(default=None, description="""Construct description (e.g., domain boundaries, truncations)""", json_schema_extra = { "linkml_meta": {'alias': 'construct',
         'comments': ['Maps to NSLS2 spreadsheet: Construct'],
         'domain_of': ['Sample'],
         'slot_uri': 'nsls2:Construct'} })
    tag: Optional[str] = Field(default=None, description="""Affinity tag (e.g., His6, GST, MBP)""", json_schema_extra = { "linkml_meta": {'alias': 'tag',
         'comments': ['Maps to NSLS2 spreadsheet: Tag'],
         'domain_of': ['Sample'],
         'slot_uri': 'nsls2:Tag'} })
    mutations: Optional[str] = Field(default=None, description="""Mutations present in the sample""", json_schema_extra = { "linkml_meta": {'alias': 'mutations',
         'comments': ['Maps to NSLS2 spreadsheet: Mutations'],
         'domain_of': ['AggregatedProteinView', 'Sample'],
         'slot_uri': 'nsls2:Mutations'} })
    expression_system: Optional[str] = Field(default=None, description="""Expression system used""", json_schema_extra = { "linkml_meta": {'alias': 'expression_system',
         'comments': ['Maps to NSLS2 spreadsheet: Expression_System'],
         'domain_of': ['Sample', 'SamplePreparation'],
         'slot_uri': 'nsls2:Expression_System'} })
    ligand: Optional[str] = Field(default=None, description="""Ligand or small molecule bound to sample""", json_schema_extra = { "linkml_meta": {'alias': 'ligand',
         'comments': ['Maps to NSLS2 spreadsheet: Ligand'],
         'domain_of': ['Sample'],
         'slot_uri': 'nsls2:Ligand'} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class ProteinConstruct(NamedThing):
    """
    Detailed information about a protein construct including cloning and sequence design
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    construct_id: str = Field(default=..., description="""Unique identifier for this construct""", json_schema_extra = { "linkml_meta": {'alias': 'construct_id', 'domain_of': ['ProteinConstruct']} })
    uniprot_id: Optional[str] = Field(default=None, description="""UniProt accession for the target protein""", json_schema_extra = { "linkml_meta": {'alias': 'uniprot_id',
         'domain_of': ['AggregatedProteinView', 'ProteinConstruct']} })
    gene_name: Optional[str] = Field(default=None, description="""Gene name""", json_schema_extra = { "linkml_meta": {'alias': 'gene_name', 'domain_of': ['ProteinConstruct']} })
    ncbi_taxid: Optional[str] = Field(default=None, description="""NCBI Taxonomy ID for source organism""", json_schema_extra = { "linkml_meta": {'alias': 'ncbi_taxid', 'domain_of': ['ProteinConstruct']} })
    sequence_length_aa: Optional[int] = Field(default=None, description="""Length of the protein sequence in amino acids""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_length_aa', 'domain_of': ['ProteinConstruct']} })
    construct_description: Optional[str] = Field(default=None, description="""Human-readable description of the construct""", json_schema_extra = { "linkml_meta": {'alias': 'construct_description', 'domain_of': ['ProteinConstruct']} })
    gene_synthesis_provider: Optional[str] = Field(default=None, description="""Company or facility that synthesized the gene""", json_schema_extra = { "linkml_meta": {'alias': 'gene_synthesis_provider', 'domain_of': ['ProteinConstruct']} })
    codon_optimization_organism: Optional[str] = Field(default=None, description="""Organism for which codons were optimized""", json_schema_extra = { "linkml_meta": {'alias': 'codon_optimization_organism', 'domain_of': ['ProteinConstruct']} })
    vector_backbone: Optional[str] = Field(default=None, description="""Base plasmid backbone used""", json_schema_extra = { "linkml_meta": {'alias': 'vector_backbone', 'domain_of': ['ProteinConstruct']} })
    vector_name: Optional[str] = Field(default=None, description="""Complete vector name""", json_schema_extra = { "linkml_meta": {'alias': 'vector_name', 'domain_of': ['ProteinConstruct']} })
    promoter: Optional[str] = Field(default=None, description="""Promoter used for expression""", json_schema_extra = { "linkml_meta": {'alias': 'promoter', 'domain_of': ['ProteinConstruct']} })
    tag_nterm: Optional[str] = Field(default=None, description="""N-terminal tag (e.g., His6, MBP, GST)""", json_schema_extra = { "linkml_meta": {'alias': 'tag_nterm', 'domain_of': ['ProteinConstruct']} })
    tag_cterm: Optional[str] = Field(default=None, description="""C-terminal tag""", json_schema_extra = { "linkml_meta": {'alias': 'tag_cterm', 'domain_of': ['ProteinConstruct']} })
    cleavage_site: Optional[str] = Field(default=None, description="""Protease cleavage site sequence""", json_schema_extra = { "linkml_meta": {'alias': 'cleavage_site', 'domain_of': ['ProteinConstruct']} })
    signal_peptide: Optional[str] = Field(default=None, description="""Signal peptide sequence if present""", json_schema_extra = { "linkml_meta": {'alias': 'signal_peptide', 'domain_of': ['ProteinConstruct']} })
    selectable_marker: Optional[str] = Field(default=None, description="""Antibiotic resistance or other selectable marker""", json_schema_extra = { "linkml_meta": {'alias': 'selectable_marker', 'domain_of': ['ProteinConstruct']} })
    cloning_method: Optional[str] = Field(default=None, description="""Method used for cloning (e.g., restriction digest, Gibson, InFusion)""", json_schema_extra = { "linkml_meta": {'alias': 'cloning_method', 'domain_of': ['ProteinConstruct']} })
    insert_boundaries: Optional[str] = Field(default=None, description="""Start and end positions of insert in vector""", json_schema_extra = { "linkml_meta": {'alias': 'insert_boundaries', 'domain_of': ['ProteinConstruct']} })
    sequence_file_path: Optional[str] = Field(default=None, description="""Path to sequence file""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_file_path', 'domain_of': ['ProteinConstruct']} })
    sequence_verified_by: Optional[str] = Field(default=None, description="""Method or person who verified the sequence""", json_schema_extra = { "linkml_meta": {'alias': 'sequence_verified_by', 'domain_of': ['ProteinConstruct']} })
    verification_notes: Optional[str] = Field(default=None, description="""Notes from sequence verification""", json_schema_extra = { "linkml_meta": {'alias': 'verification_notes', 'domain_of': ['ProteinConstruct']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class SamplePreparation(NamedThing):
    """
    A process that prepares a sample for imaging
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    preparation_type: PreparationTypeEnum = Field(default=..., description="""Type of sample preparation""", json_schema_extra = { "linkml_meta": {'alias': 'preparation_type', 'domain_of': ['SamplePreparation']} })
    sample_id: str = Field(default=..., description="""Reference to the sample being prepared""", json_schema_extra = { "linkml_meta": {'alias': 'sample_id', 'domain_of': ['SamplePreparation', 'ExperimentRun']} })
    preparation_date: Optional[str] = Field(default=None, description="""Date of sample preparation""", json_schema_extra = { "linkml_meta": {'alias': 'preparation_date', 'domain_of': ['SamplePreparation']} })
    operator_id: Optional[str] = Field(default=None, description="""Identifier or name of the person who performed the sample preparation (e.g., 'jsmith', 'John Smith', or personnel ID)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['SamplePreparation', 'ExperimentRun']} })
    protocol_description: Optional[str] = Field(default=None, description="""Detailed protocol description""", json_schema_extra = { "linkml_meta": {'alias': 'protocol_description', 'domain_of': ['SamplePreparation']} })
    expression_system: Optional[ExpressionSystemEnum] = Field(default=None, description="""Expression system used for recombinant protein production""", json_schema_extra = { "linkml_meta": {'alias': 'expression_system', 'domain_of': ['Sample', 'SamplePreparation']} })
    host_strain_or_cell_line: Optional[str] = Field(default=None, description="""Specific strain or cell line used (e.g., BL21(DE3), Sf9, HEK293F)""", json_schema_extra = { "linkml_meta": {'alias': 'host_strain_or_cell_line', 'domain_of': ['SamplePreparation']} })
    culture_volume_l: Optional[float] = Field(default=None, description="""Culture volume in liters""", json_schema_extra = { "linkml_meta": {'alias': 'culture_volume_l',
         'domain_of': ['SamplePreparation'],
         'unit': {'ucum_code': 'L'}} })
    medium: Optional[str] = Field(default=None, description="""Growth medium used""", json_schema_extra = { "linkml_meta": {'alias': 'medium', 'domain_of': ['SamplePreparation']} })
    antibiotic_selection: Optional[str] = Field(default=None, description="""Antibiotic or selection agent used""", json_schema_extra = { "linkml_meta": {'alias': 'antibiotic_selection', 'domain_of': ['SamplePreparation']} })
    growth_temperature_c: Optional[float] = Field(default=None, description="""Growth temperature in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'growth_temperature_c',
         'domain_of': ['SamplePreparation'],
         'unit': {'ucum_code': 'Cel'}} })
    induction_agent: Optional[str] = Field(default=None, description="""Agent used to induce expression (e.g., IPTG, tetracycline)""", json_schema_extra = { "linkml_meta": {'alias': 'induction_agent', 'domain_of': ['SamplePreparation']} })
    inducer_concentration: Optional[str] = Field(default=None, description="""Concentration of induction agent""", json_schema_extra = { "linkml_meta": {'alias': 'inducer_concentration', 'domain_of': ['SamplePreparation']} })
    induction_temperature_c: Optional[float] = Field(default=None, description="""Temperature during induction in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'induction_temperature_c', 'domain_of': ['SamplePreparation']} })
    induction_time_h: Optional[float] = Field(default=None, description="""Duration of induction in hours""", json_schema_extra = { "linkml_meta": {'alias': 'induction_time_h', 'domain_of': ['SamplePreparation']} })
    od600_at_induction: Optional[float] = Field(default=None, description="""Optical density at 600nm when induction was started""", json_schema_extra = { "linkml_meta": {'alias': 'od600_at_induction', 'domain_of': ['SamplePreparation']} })
    harvest_timepoint: Optional[str] = Field(default=None, description="""Time point when cells were harvested""", json_schema_extra = { "linkml_meta": {'alias': 'harvest_timepoint', 'domain_of': ['SamplePreparation']} })
    lysis_method: Optional[str] = Field(default=None, description="""Method used for cell lysis""", json_schema_extra = { "linkml_meta": {'alias': 'lysis_method', 'domain_of': ['SamplePreparation']} })
    protease_inhibitors: Optional[str] = Field(default=None, description="""Protease inhibitors added""", json_schema_extra = { "linkml_meta": {'alias': 'protease_inhibitors', 'domain_of': ['SamplePreparation']} })
    purification_steps: Optional[list[PurificationStepEnum]] = Field(default=None, description="""Ordered list of purification steps performed""", json_schema_extra = { "linkml_meta": {'alias': 'purification_steps', 'domain_of': ['SamplePreparation']} })
    affinity_type: Optional[str] = Field(default=None, description="""Type of affinity chromatography""", json_schema_extra = { "linkml_meta": {'alias': 'affinity_type', 'domain_of': ['SamplePreparation']} })
    affinity_column: Optional[str] = Field(default=None, description="""Affinity column specifications""", json_schema_extra = { "linkml_meta": {'alias': 'affinity_column', 'domain_of': ['SamplePreparation']} })
    lysis_buffer: Optional[str] = Field(default=None, description="""Buffer composition for lysis""", json_schema_extra = { "linkml_meta": {'alias': 'lysis_buffer', 'domain_of': ['SamplePreparation']} })
    wash_buffer: Optional[str] = Field(default=None, description="""Buffer composition for washing""", json_schema_extra = { "linkml_meta": {'alias': 'wash_buffer', 'domain_of': ['SamplePreparation']} })
    elution_buffer: Optional[str] = Field(default=None, description="""Buffer composition for elution""", json_schema_extra = { "linkml_meta": {'alias': 'elution_buffer', 'domain_of': ['SamplePreparation']} })
    tag_removal: Optional[bool] = Field(default=None, description="""Whether and how affinity tag was removed""", json_schema_extra = { "linkml_meta": {'alias': 'tag_removal', 'domain_of': ['SamplePreparation']} })
    protease: Optional[str] = Field(default=None, description="""Protease used for tag cleavage""", json_schema_extra = { "linkml_meta": {'alias': 'protease', 'domain_of': ['SamplePreparation']} })
    protease_ratio: Optional[str] = Field(default=None, description="""Ratio of protease to protein""", json_schema_extra = { "linkml_meta": {'alias': 'protease_ratio', 'domain_of': ['SamplePreparation']} })
    cleavage_time_h: Optional[float] = Field(default=None, description="""Duration of protease cleavage in hours""", json_schema_extra = { "linkml_meta": {'alias': 'cleavage_time_h', 'domain_of': ['SamplePreparation']} })
    cleavage_temperature_c: Optional[float] = Field(default=None, description="""Temperature during cleavage in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'cleavage_temperature_c', 'domain_of': ['SamplePreparation']} })
    second_affinity_reverse: Optional[str] = Field(default=None, description="""Second affinity or reverse affinity step""", json_schema_extra = { "linkml_meta": {'alias': 'second_affinity_reverse', 'domain_of': ['SamplePreparation']} })
    iex_column: Optional[str] = Field(default=None, description="""Ion-exchange column used""", json_schema_extra = { "linkml_meta": {'alias': 'iex_column', 'domain_of': ['SamplePreparation']} })
    hic_column: Optional[str] = Field(default=None, description="""Hydrophobic interaction column used""", json_schema_extra = { "linkml_meta": {'alias': 'hic_column', 'domain_of': ['SamplePreparation']} })
    sec_column: Optional[str] = Field(default=None, description="""Size-exclusion column used""", json_schema_extra = { "linkml_meta": {'alias': 'sec_column', 'domain_of': ['SamplePreparation']} })
    sec_buffer: Optional[str] = Field(default=None, description="""Buffer for size-exclusion chromatography""", json_schema_extra = { "linkml_meta": {'alias': 'sec_buffer', 'domain_of': ['SamplePreparation']} })
    concentration_method: Optional[str] = Field(default=None, description="""Method used to concentrate protein""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_method', 'domain_of': ['SamplePreparation']} })
    final_buffer: Optional[str] = Field(default=None, description="""Final buffer composition after purification""", json_schema_extra = { "linkml_meta": {'alias': 'final_buffer', 'domain_of': ['SamplePreparation']} })
    final_concentration_mg_per_ml: Optional[float] = Field(default=None, description="""Final protein concentration in mg/mL""", json_schema_extra = { "linkml_meta": {'alias': 'final_concentration_mg_per_ml', 'domain_of': ['SamplePreparation']} })
    yield_mg: Optional[float] = Field(default=None, description="""Total yield in milligrams""", json_schema_extra = { "linkml_meta": {'alias': 'yield_mg', 'domain_of': ['SamplePreparation']} })
    purity_by_sds_page_percent: Optional[float] = Field(default=None, description="""Purity percentage by SDS-PAGE""", json_schema_extra = { "linkml_meta": {'alias': 'purity_by_sds_page_percent', 'domain_of': ['SamplePreparation']} })
    aggregation_assessment: Optional[str] = Field(default=None, description="""Assessment of protein aggregation state""", json_schema_extra = { "linkml_meta": {'alias': 'aggregation_assessment', 'domain_of': ['SamplePreparation']} })
    aliquoting: Optional[str] = Field(default=None, description="""How the protein was aliquoted for storage""", json_schema_extra = { "linkml_meta": {'alias': 'aliquoting', 'domain_of': ['SamplePreparation']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Instrument(NamedThing):
    """
    An instrument used to collect data
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    instrument_code: str = Field(default=..., description="""Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_code', 'domain_of': ['Instrument']} })
    manufacturer: Optional[str] = Field(default=None, description="""Instrument manufacturer""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer', 'domain_of': ['Instrument']} })
    model: Optional[str] = Field(default=None, description="""Instrument model""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['Instrument']} })
    installation_date: Optional[str] = Field(default=None, description="""Date of instrument installation""", json_schema_extra = { "linkml_meta": {'alias': 'installation_date', 'domain_of': ['Instrument']} })
    current_status: Optional[InstrumentStatusEnum] = Field(default=None, description="""Current operational status""", json_schema_extra = { "linkml_meta": {'alias': 'current_status', 'domain_of': ['Instrument']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class CryoEMInstrument(Instrument):
    """
    Cryo-EM microscope specifications
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    accelerating_voltage: Optional[int] = Field(default=None, description="""Accelerating voltage in kV""", json_schema_extra = { "linkml_meta": {'alias': 'accelerating_voltage',
         'any_of': [{'equals_number': 120},
                    {'equals_number': 200},
                    {'equals_number': 300}],
         'domain_of': ['CryoEMInstrument']} })
    cs_corrector: Optional[bool] = Field(default=None, description="""Spherical aberration corrector present""", json_schema_extra = { "linkml_meta": {'alias': 'cs_corrector', 'domain_of': ['CryoEMInstrument']} })
    phase_plate: Optional[bool] = Field(default=None, description="""Phase plate available""", json_schema_extra = { "linkml_meta": {'alias': 'phase_plate', 'domain_of': ['CryoEMInstrument']} })
    detector_technology: Optional[DetectorTechnologyEnum] = Field(default=None, description="""Generic detector technology type""", json_schema_extra = { "linkml_meta": {'alias': 'detector_technology',
         'comments': ['Use this for technology classification (e.g., '
                      'direct_electron_detector, ccd)',
                      'See detector_manufacturer and detector_model for specific '
                      'equipment details'],
         'domain_of': ['CryoEMInstrument', 'XRayInstrument', 'XRFImage']} })
    detector_manufacturer: Optional[str] = Field(default=None, description="""Detector manufacturer (e.g., Gatan, ThermoFisher, DirectElectron)""", json_schema_extra = { "linkml_meta": {'alias': 'detector_manufacturer',
         'comments': ['Examples: Gatan, ThermoFisher Scientific, DirectElectron'],
         'domain_of': ['CryoEMInstrument', 'XRayInstrument']} })
    detector_model: Optional[str] = Field(default=None, description="""Detector model (e.g., K3, Falcon 4i, DE-64)""", json_schema_extra = { "linkml_meta": {'alias': 'detector_model',
         'comments': ['Examples: K3 BioQuantum, Falcon 4i, DE-64'],
         'domain_of': ['CryoEMInstrument', 'XRayInstrument', 'XRFImage']} })
    detector_mode: Optional[DetectorModeEnum] = Field(default=None, description="""Supported or default detector operating mode""", json_schema_extra = { "linkml_meta": {'alias': 'detector_mode',
         'comments': ['Indicates operating mode capabilities (e.g., counting, '
                      'super_resolution)'],
         'domain_of': ['CryoEMInstrument', 'DataCollectionStrategy']} })
    detector_position: Optional[str] = Field(default=None, description="""Physical position of detector in microscope (e.g., post-GIF, pre-column)""", json_schema_extra = { "linkml_meta": {'alias': 'detector_position', 'domain_of': ['CryoEMInstrument']} })
    detector_dimensions: Optional[str] = Field(default=None, description="""Detector dimensions in pixels (e.g., 4096x4096, 5760x4092)""", json_schema_extra = { "linkml_meta": {'alias': 'detector_dimensions', 'domain_of': ['CryoEMInstrument']} })
    pixel_size_physical_um: Optional[float] = Field(default=None, description="""Physical pixel size of the detector in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size_physical_um',
         'comments': ['Hardware specification, independent of magnification',
                      'Calibrated pixel size (Å/pixel) depends on magnification and is '
                      'stored in ExperimentRun'],
         'domain_of': ['CryoEMInstrument']} })
    autoloader_capacity: Optional[int] = Field(default=None, description="""Number of grids the autoloader can hold""", json_schema_extra = { "linkml_meta": {'alias': 'autoloader_capacity', 'domain_of': ['CryoEMInstrument']} })
    cs: Optional[float] = Field(default=None, description="""Spherical aberration (Cs) in millimeters""", json_schema_extra = { "linkml_meta": {'alias': 'cs', 'domain_of': ['CryoEMInstrument']} })
    c2_aperture: Optional[float] = Field(default=None, description="""C2 aperture size in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'c2_aperture', 'domain_of': ['CryoEMInstrument']} })
    objective_aperture: Optional[float] = Field(default=None, description="""Objective aperture size in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'objective_aperture', 'domain_of': ['CryoEMInstrument']} })
    phase_plate_type: Optional[str] = Field(default=None, description="""Type of phase plate if present""", json_schema_extra = { "linkml_meta": {'alias': 'phase_plate_type', 'domain_of': ['CryoEMInstrument']} })
    energy_filter_present: Optional[bool] = Field(default=None, description="""Whether energy filter is present""", json_schema_extra = { "linkml_meta": {'alias': 'energy_filter_present', 'domain_of': ['CryoEMInstrument']} })
    energy_filter_make: Optional[str] = Field(default=None, description="""Energy filter manufacturer""", json_schema_extra = { "linkml_meta": {'alias': 'energy_filter_make', 'domain_of': ['CryoEMInstrument']} })
    energy_filter_model: Optional[str] = Field(default=None, description="""Energy filter model""", json_schema_extra = { "linkml_meta": {'alias': 'energy_filter_model', 'domain_of': ['CryoEMInstrument']} })
    energy_filter_slit_width: Optional[float] = Field(default=None, description="""Energy filter slit width in eV""", json_schema_extra = { "linkml_meta": {'alias': 'energy_filter_slit_width', 'domain_of': ['CryoEMInstrument']} })
    pixel_size_physical: Optional[float] = Field(default=None, description="""Physical pixel size in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size_physical', 'domain_of': ['CryoEMInstrument']} })
    microscope_software: Optional[str] = Field(default=None, description="""Microscope control software (e.g., SerialEM, EPU, Leginon)""", json_schema_extra = { "linkml_meta": {'alias': 'microscope_software', 'domain_of': ['CryoEMInstrument']} })
    microscope_software_version: Optional[str] = Field(default=None, description="""Software version""", json_schema_extra = { "linkml_meta": {'alias': 'microscope_software_version', 'domain_of': ['CryoEMInstrument']} })
    spotsize: Optional[int] = Field(default=None, description="""Electron beam spot size setting""", json_schema_extra = { "linkml_meta": {'alias': 'spotsize', 'domain_of': ['CryoEMInstrument']} })
    gunlens: Optional[int] = Field(default=None, description="""Gun lens setting""", json_schema_extra = { "linkml_meta": {'alias': 'gunlens', 'domain_of': ['CryoEMInstrument']} })
    imaging_mode: Optional[ImagingModeEnum] = Field(default=None, description="""Imaging mode for electron microscopy""", json_schema_extra = { "linkml_meta": {'alias': 'imaging_mode', 'domain_of': ['CryoEMInstrument']} })
    tem_beam_diameter: Optional[float] = Field(default=None, description="""TEM beam diameter in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'tem_beam_diameter', 'domain_of': ['CryoEMInstrument']} })
    instrument_code: str = Field(default=..., description="""Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_code', 'domain_of': ['Instrument']} })
    manufacturer: Optional[str] = Field(default=None, description="""Instrument manufacturer""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer', 'domain_of': ['Instrument']} })
    model: Optional[str] = Field(default=None, description="""Instrument model""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['Instrument']} })
    installation_date: Optional[str] = Field(default=None, description="""Date of instrument installation""", json_schema_extra = { "linkml_meta": {'alias': 'installation_date', 'domain_of': ['Instrument']} })
    current_status: Optional[InstrumentStatusEnum] = Field(default=None, description="""Current operational status""", json_schema_extra = { "linkml_meta": {'alias': 'current_status', 'domain_of': ['Instrument']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class XRayInstrument(Instrument):
    """
    X-ray diffractometer or synchrotron beamline specifications
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    source_type: Optional[XRaySourceTypeEnum] = Field(default=None, description="""Type of X-ray source""", json_schema_extra = { "linkml_meta": {'alias': 'source_type', 'domain_of': ['XRayInstrument', 'XRFImage']} })
    detector_technology: Optional[DetectorTechnologyEnum] = Field(default=None, description="""Generic detector technology type""", json_schema_extra = { "linkml_meta": {'alias': 'detector_technology',
         'comments': ['Use this for technology classification (e.g., '
                      'hybrid_photon_counting, ccd)',
                      'Maps to CBF: Detector (may contain model name)',
                      'Maps to PDB: _diffrn_detector.type',
                      'See detector_manufacturer and detector_model for specific '
                      'equipment details'],
         'domain_of': ['CryoEMInstrument', 'XRayInstrument', 'XRFImage'],
         'slot_uri': 'nsls2:Detector'} })
    detector_manufacturer: Optional[str] = Field(default=None, description="""Detector manufacturer (e.g., Dectris, Bruker, Rigaku, Rayonix)""", json_schema_extra = { "linkml_meta": {'alias': 'detector_manufacturer',
         'comments': ['Examples: Dectris, Bruker, Rigaku, Rayonix, ADSC, MAR Research'],
         'domain_of': ['CryoEMInstrument', 'XRayInstrument']} })
    detector_model: Optional[str] = Field(default=None, description="""Detector model (e.g., EIGER2 X 16M, PILATUS3 X 6M, PHOTON III)""", json_schema_extra = { "linkml_meta": {'alias': 'detector_model',
         'comments': ['Examples: EIGER2 X 16M, PILATUS3 X 6M, PHOTON III, '
                      'HyPix-6000HE'],
         'domain_of': ['CryoEMInstrument', 'XRayInstrument', 'XRFImage']} })
    beamline_id: Optional[str] = Field(default=None, description="""Beamline identifier at synchrotron facility""", json_schema_extra = { "linkml_meta": {'alias': 'beamline_id',
         'domain_of': ['XRayInstrument'],
         'slot_uri': 'nsls2:Beamline'} })
    energy_min: Optional[float] = Field(default=None, description="""Minimum X-ray energy in keV""", json_schema_extra = { "linkml_meta": {'alias': 'energy_min', 'domain_of': ['XRayInstrument']} })
    energy_max: Optional[float] = Field(default=None, description="""Maximum X-ray energy in keV""", json_schema_extra = { "linkml_meta": {'alias': 'energy_max', 'domain_of': ['XRayInstrument']} })
    beam_size_min: Optional[float] = Field(default=None, description="""Minimum beam size in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'beam_size_min', 'domain_of': ['XRayInstrument']} })
    beam_size_max: Optional[float] = Field(default=None, description="""Maximum beam size in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'beam_size_max', 'domain_of': ['XRayInstrument']} })
    flux_density: Optional[float] = Field(default=None, description="""Photon flux density in photons/s/mm²""", json_schema_extra = { "linkml_meta": {'alias': 'flux_density', 'domain_of': ['XRayInstrument']} })
    monochromator_type: Optional[str] = Field(default=None, description="""Type of monochromator""", json_schema_extra = { "linkml_meta": {'alias': 'monochromator_type', 'domain_of': ['XRayInstrument']} })
    goniometer_type: Optional[str] = Field(default=None, description="""Type of goniometer""", json_schema_extra = { "linkml_meta": {'alias': 'goniometer_type', 'domain_of': ['XRayInstrument']} })
    crystal_cooling_capability: Optional[bool] = Field(default=None, description="""Crystal cooling system available""", json_schema_extra = { "linkml_meta": {'alias': 'crystal_cooling_capability', 'domain_of': ['XRayInstrument']} })
    instrument_code: str = Field(default=..., description="""Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_code', 'domain_of': ['Instrument']} })
    manufacturer: Optional[str] = Field(default=None, description="""Instrument manufacturer""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer', 'domain_of': ['Instrument']} })
    model: Optional[str] = Field(default=None, description="""Instrument model""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['Instrument']} })
    installation_date: Optional[str] = Field(default=None, description="""Date of instrument installation""", json_schema_extra = { "linkml_meta": {'alias': 'installation_date', 'domain_of': ['Instrument']} })
    current_status: Optional[InstrumentStatusEnum] = Field(default=None, description="""Current operational status""", json_schema_extra = { "linkml_meta": {'alias': 'current_status', 'domain_of': ['Instrument']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class SAXSInstrument(Instrument):
    """
    SAXS/WAXS instrument specifications
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    q_range_min: Optional[float] = Field(default=None, description="""Minimum q value in inverse Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'q_range_min', 'domain_of': ['SAXSInstrument']} })
    q_range_max: Optional[float] = Field(default=None, description="""Maximum q value in inverse Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'q_range_max', 'domain_of': ['SAXSInstrument']} })
    detector_distance_min: Optional[float] = Field(default=None, description="""Minimum detector distance in mm""", json_schema_extra = { "linkml_meta": {'alias': 'detector_distance_min', 'domain_of': ['SAXSInstrument']} })
    detector_distance_max: Optional[float] = Field(default=None, description="""Maximum detector distance in mm""", json_schema_extra = { "linkml_meta": {'alias': 'detector_distance_max', 'domain_of': ['SAXSInstrument']} })
    sample_changer_capacity: Optional[int] = Field(default=None, description="""Number of samples in automatic sample changer""", json_schema_extra = { "linkml_meta": {'alias': 'sample_changer_capacity', 'domain_of': ['SAXSInstrument']} })
    temperature_control_range: Optional[str] = Field(default=None, description="""Temperature control range in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_control_range', 'domain_of': ['SAXSInstrument']} })
    instrument_code: str = Field(default=..., description="""Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_code', 'domain_of': ['Instrument']} })
    manufacturer: Optional[str] = Field(default=None, description="""Instrument manufacturer""", json_schema_extra = { "linkml_meta": {'alias': 'manufacturer', 'domain_of': ['Instrument']} })
    model: Optional[str] = Field(default=None, description="""Instrument model""", json_schema_extra = { "linkml_meta": {'alias': 'model', 'domain_of': ['Instrument']} })
    installation_date: Optional[str] = Field(default=None, description="""Date of instrument installation""", json_schema_extra = { "linkml_meta": {'alias': 'installation_date', 'domain_of': ['Instrument']} })
    current_status: Optional[InstrumentStatusEnum] = Field(default=None, description="""Current operational status""", json_schema_extra = { "linkml_meta": {'alias': 'current_status', 'domain_of': ['Instrument']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class ExperimentRun(NamedThing):
    """
    An experimental data collection session
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    experiment_code: str = Field(default=..., description="""Human-friendly laboratory or facility identifier for the experiment (e.g., 'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and cross-referencing within laboratory systems.""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_code', 'domain_of': ['ExperimentRun']} })
    sample_id: str = Field(default=..., description="""Reference to the sample being analyzed""", json_schema_extra = { "linkml_meta": {'alias': 'sample_id', 'domain_of': ['SamplePreparation', 'ExperimentRun']} })
    instrument_id: str = Field(default=..., description="""Reference to the instrument used""", json_schema_extra = { "linkml_meta": {'alias': 'instrument_id', 'domain_of': ['ExperimentRun']} })
    experiment_date: Optional[str] = Field(default=None, description="""Date of the experiment""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_date', 'domain_of': ['ExperimentRun']} })
    operator_id: Optional[str] = Field(default=None, description="""Identifier or name of the person who performed the experiment data collection (e.g., 'jsmith', 'John Smith', or personnel ID)""", json_schema_extra = { "linkml_meta": {'alias': 'operator_id', 'domain_of': ['SamplePreparation', 'ExperimentRun']} })
    technique: TechniqueEnum = Field(default=..., description="""Technique used for data collection""", json_schema_extra = { "linkml_meta": {'alias': 'technique', 'domain_of': ['ExperimentRun']} })
    experimental_method: Optional[ExperimentalMethodEnum] = Field(default=None, description="""Specific experimental method for structure determination (particularly for diffraction techniques)""", json_schema_extra = { "linkml_meta": {'alias': 'experimental_method',
         'domain_of': ['BiophysicalProperty', 'ExperimentRun']} })
    experimental_conditions: Optional[ExperimentalConditions] = Field(default=None, description="""Environmental and experimental conditions""", json_schema_extra = { "linkml_meta": {'alias': 'experimental_conditions', 'domain_of': ['ExperimentRun']} })
    data_collection_strategy: Optional[DataCollectionStrategy] = Field(default=None, description="""Strategy for data collection""", json_schema_extra = { "linkml_meta": {'alias': 'data_collection_strategy', 'domain_of': ['ExperimentRun']} })
    quality_metrics: Optional[QualityMetrics] = Field(default=None, description="""Quality metrics for the experiment""", json_schema_extra = { "linkml_meta": {'alias': 'quality_metrics', 'domain_of': ['Sample', 'ExperimentRun']} })
    raw_data_location: Optional[str] = Field(default=None, description="""Location of raw data files""", json_schema_extra = { "linkml_meta": {'alias': 'raw_data_location', 'domain_of': ['ExperimentRun']} })
    processing_status: Optional[ProcessingStatusEnum] = Field(default=None, description="""Current processing status""", json_schema_extra = { "linkml_meta": {'alias': 'processing_status', 'domain_of': ['ExperimentRun']} })
    magnification: Optional[int] = Field(default=None, description="""Magnification used during data collection""", json_schema_extra = { "linkml_meta": {'alias': 'magnification', 'domain_of': ['ExperimentRun', 'OpticalImage']} })
    calibrated_pixel_size: Optional[float] = Field(default=None, description="""Calibrated pixel size in Angstroms per pixel""", json_schema_extra = { "linkml_meta": {'alias': 'calibrated_pixel_size', 'domain_of': ['ExperimentRun']} })
    camera_binning: Optional[int] = Field(default=None, description="""Camera binning factor""", json_schema_extra = { "linkml_meta": {'alias': 'camera_binning', 'domain_of': ['ExperimentRun']} })
    exposure_time_per_frame: Optional[float] = Field(default=None, description="""Exposure time per frame in milliseconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time_per_frame', 'domain_of': ['ExperimentRun']} })
    frames_per_movie: Optional[int] = Field(default=None, description="""Number of frames per movie""", json_schema_extra = { "linkml_meta": {'alias': 'frames_per_movie', 'domain_of': ['ExperimentRun']} })
    total_exposure_time: Optional[float] = Field(default=None, description="""Total exposure time in milliseconds""", json_schema_extra = { "linkml_meta": {'alias': 'total_exposure_time', 'domain_of': ['ExperimentRun']} })
    total_dose: Optional[float] = Field(default=None, description="""Total electron dose in e-/Angstrom^2""", json_schema_extra = { "linkml_meta": {'alias': 'total_dose',
         'domain_of': ['ExperimentRun', 'DataCollectionStrategy']} })
    dose_rate: Optional[float] = Field(default=None, description="""Dose rate in e-/pixel/s or e-/Angstrom^2/s""", json_schema_extra = { "linkml_meta": {'alias': 'dose_rate', 'domain_of': ['ExperimentRun']} })
    defocus_target: Optional[float] = Field(default=None, description="""Target defocus value in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_target', 'domain_of': ['ExperimentRun']} })
    defocus_range_min: Optional[float] = Field(default=None, description="""Minimum defocus range in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_range_min', 'domain_of': ['ExperimentRun']} })
    defocus_range_max: Optional[float] = Field(default=None, description="""Maximum defocus range in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_range_max', 'domain_of': ['ExperimentRun']} })
    defocus_range_increment: Optional[float] = Field(default=None, description="""Defocus range increment in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_range_increment', 'domain_of': ['ExperimentRun']} })
    astigmatism_target: Optional[float] = Field(default=None, description="""Target astigmatism in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'astigmatism_target', 'domain_of': ['ExperimentRun']} })
    coma: Optional[float] = Field(default=None, description="""Coma aberration in nanometers""", json_schema_extra = { "linkml_meta": {'alias': 'coma', 'domain_of': ['ExperimentRun']} })
    stage_tilt: Optional[float] = Field(default=None, description="""Stage tilt angle in degrees""", json_schema_extra = { "linkml_meta": {'alias': 'stage_tilt', 'domain_of': ['ExperimentRun']} })
    autoloader_slot: Optional[str] = Field(default=None, description="""Autoloader slot identifier""", json_schema_extra = { "linkml_meta": {'alias': 'autoloader_slot', 'domain_of': ['ExperimentRun']} })
    shots_per_hole: Optional[int] = Field(default=None, description="""Number of shots taken per hole""", json_schema_extra = { "linkml_meta": {'alias': 'shots_per_hole', 'domain_of': ['ExperimentRun']} })
    holes_per_group: Optional[int] = Field(default=None, description="""Number of holes per group""", json_schema_extra = { "linkml_meta": {'alias': 'holes_per_group', 'domain_of': ['ExperimentRun']} })
    acquisition_software: Optional[str] = Field(default=None, description="""Acquisition software used (e.g., SerialEM, EPU, Leginon)""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_software', 'domain_of': ['ExperimentRun']} })
    acquisition_software_version: Optional[str] = Field(default=None, description="""Version of acquisition software""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_software_version', 'domain_of': ['ExperimentRun']} })
    wavelength: Optional[float] = Field(default=None, description="""X-ray wavelength""", json_schema_extra = { "linkml_meta": {'alias': 'wavelength',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Wavelength',
                            'imgCIF:_diffrn_radiation_wavelength.wavelength',
                            'mmCIF:_diffrn_radiation_wavelength.wavelength'],
         'unit': {'ucum_code': 'Ao'}} })
    oscillation_angle: Optional[float] = Field(default=None, description="""Oscillation angle per image""", json_schema_extra = { "linkml_meta": {'alias': 'oscillation_angle',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Angle_increment',
                            'imgCIF:_diffrn_scan_axis.angle_increment',
                            'mmCIF:_diffrn_scan.angle_increment'],
         'unit': {'ucum_code': 'deg'}} })
    start_angle: Optional[float] = Field(default=None, description="""Starting rotation angle""", json_schema_extra = { "linkml_meta": {'alias': 'start_angle',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Start_angle',
                            'imgCIF:_diffrn_scan_axis.angle_start'],
         'unit': {'ucum_code': 'deg'}} })
    number_of_images: Optional[int] = Field(default=None, description="""Total number of diffraction images collected""", json_schema_extra = { "linkml_meta": {'alias': 'number_of_images',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Number_of_images', 'imgCIF:_diffrn_scan.frames']} })
    beam_center_x: Optional[float] = Field(default=None, description="""Beam center X coordinate""", json_schema_extra = { "linkml_meta": {'alias': 'beam_center_x',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Beam_xy_x',
                            'imgCIF:_diffrn_detector.beam_centre_x',
                            'mmCIF:_diffrn_detector.beam_center_x'],
         'unit': {'ucum_code': '[px]'}} })
    beam_center_y: Optional[float] = Field(default=None, description="""Beam center Y coordinate""", json_schema_extra = { "linkml_meta": {'alias': 'beam_center_y',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Beam_xy_y',
                            'imgCIF:_diffrn_detector.beam_centre_y',
                            'mmCIF:_diffrn_detector.beam_center_y'],
         'unit': {'ucum_code': '[px]'}} })
    detector_distance: Optional[float] = Field(default=None, description="""Distance from sample to detector""", json_schema_extra = { "linkml_meta": {'alias': 'detector_distance',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Detector_distance',
                            'imgCIF:_diffrn_measurement.sample_detector_distance',
                            'mmCIF:_diffrn_detector.distance'],
         'unit': {'ucum_code': 'mm'}} })
    pixel_size_x: Optional[float] = Field(default=None, description="""Pixel size X dimension""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size_x',
         'comments': ['imgCIF: _array_element_size.size[1]'],
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Pixel_size_x', 'imgCIF:_array_element_size.size'],
         'unit': {'ucum_code': 'um'}} })
    pixel_size_y: Optional[float] = Field(default=None, description="""Pixel size Y dimension""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size_y',
         'comments': ['imgCIF: _array_element_size.size[2]'],
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Pixel_size_y', 'imgCIF:_array_element_size.size'],
         'unit': {'ucum_code': 'um'}} })
    total_rotation: Optional[float] = Field(default=None, description="""Total rotation range collected""", json_schema_extra = { "linkml_meta": {'alias': 'total_rotation',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Total_rotation_deg',
                            'imgCIF:_diffrn_scan_axis.angle_range'],
         'unit': {'ucum_code': 'deg'}} })
    beamline: Optional[str] = Field(default=None, description="""Beamline identifier (e.g., FMX, AMX, 12.3.1)""", json_schema_extra = { "linkml_meta": {'alias': 'beamline',
         'domain_of': ['ExperimentRun'],
         'exact_mappings': ['nsls2:Beamline',
                            'mmCIF:_diffrn_source.pdbx_synchrotron_beamline']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class WorkflowRun(NamedThing):
    """
    A computational processing workflow execution
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    workflow_code: str = Field(default=..., description="""Human-friendly identifier for the computational workflow run (e.g., 'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing pipelines and computational provenance.""", json_schema_extra = { "linkml_meta": {'alias': 'workflow_code', 'domain_of': ['WorkflowRun']} })
    workflow_type: WorkflowTypeEnum = Field(default=..., description="""Type of processing workflow""", json_schema_extra = { "linkml_meta": {'alias': 'workflow_type', 'domain_of': ['WorkflowRun']} })
    experiment_id: str = Field(default=..., description="""Reference to the source experiment""", json_schema_extra = { "linkml_meta": {'alias': 'experiment_id', 'domain_of': ['WorkflowRun']} })
    processing_level: Optional[int] = Field(default=None, description="""Processing level (0=raw, 1=corrected, 2=derived, 3=model)""", ge=0, le=4, json_schema_extra = { "linkml_meta": {'alias': 'processing_level', 'domain_of': ['WorkflowRun']} })
    software_name: str = Field(default=..., description="""Software used for processing""", json_schema_extra = { "linkml_meta": {'alias': 'software_name', 'domain_of': ['WorkflowRun']} })
    software_version: Optional[str] = Field(default=None, description="""Software version""", json_schema_extra = { "linkml_meta": {'alias': 'software_version', 'domain_of': ['WorkflowRun']} })
    additional_software: Optional[str] = Field(default=None, description="""Additional software used in pipeline""", json_schema_extra = { "linkml_meta": {'alias': 'additional_software', 'domain_of': ['WorkflowRun']} })
    processing_parameters: Optional[str] = Field(default=None, description="""Parameters used in processing""", json_schema_extra = { "linkml_meta": {'alias': 'processing_parameters', 'domain_of': ['WorkflowRun']} })
    parameters_file_path: Optional[str] = Field(default=None, description="""Path to parameters file or text of key parameters""", json_schema_extra = { "linkml_meta": {'alias': 'parameters_file_path', 'domain_of': ['WorkflowRun']} })
    indexer_module: Optional[str] = Field(default=None, description="""Indexing module used (e.g., MOSFLM, XDS)""", json_schema_extra = { "linkml_meta": {'alias': 'indexer_module', 'domain_of': ['WorkflowRun']} })
    integrator_module: Optional[str] = Field(default=None, description="""Integration module used""", json_schema_extra = { "linkml_meta": {'alias': 'integrator_module', 'domain_of': ['WorkflowRun']} })
    scaler_module: Optional[str] = Field(default=None, description="""Scaling module used (e.g., AIMLESS, SCALA)""", json_schema_extra = { "linkml_meta": {'alias': 'scaler_module', 'domain_of': ['WorkflowRun']} })
    outlier_rejection_method: Optional[str] = Field(default=None, description="""Method for rejecting outlier reflections""", json_schema_extra = { "linkml_meta": {'alias': 'outlier_rejection_method', 'domain_of': ['WorkflowRun']} })
    phasing_method: Optional[PhasingMethodEnum] = Field(default=None, description="""Phasing method used for X-ray crystallography structure determination""", json_schema_extra = { "linkml_meta": {'alias': 'phasing_method', 'domain_of': ['WorkflowRun']} })
    search_model_pdb_id: Optional[str] = Field(default=None, description="""PDB ID of search model for molecular replacement""", json_schema_extra = { "linkml_meta": {'alias': 'search_model_pdb_id', 'domain_of': ['WorkflowRun']} })
    tls_used: Optional[bool] = Field(default=None, description="""Whether TLS (Translation/Libration/Screw) refinement was used""", json_schema_extra = { "linkml_meta": {'alias': 'tls_used', 'domain_of': ['WorkflowRun']} })
    ncs_used: Optional[bool] = Field(default=None, description="""Whether Non-Crystallographic Symmetry restraints were used""", json_schema_extra = { "linkml_meta": {'alias': 'ncs_used', 'domain_of': ['WorkflowRun']} })
    restraints_other: Optional[str] = Field(default=None, description="""Other restraints applied during refinement""", json_schema_extra = { "linkml_meta": {'alias': 'restraints_other', 'domain_of': ['WorkflowRun']} })
    ligands_cofactors: Optional[str] = Field(default=None, description="""Ligands or cofactors modeled in the structure""", json_schema_extra = { "linkml_meta": {'alias': 'ligands_cofactors', 'domain_of': ['WorkflowRun']} })
    number_of_waters: Optional[int] = Field(default=None, description="""Number of water molecules modeled""", json_schema_extra = { "linkml_meta": {'alias': 'number_of_waters', 'domain_of': ['WorkflowRun']} })
    refinement_resolution_a: Optional[float] = Field(default=None, description="""Resolution cutoff used for refinement in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'refinement_resolution_a', 'domain_of': ['WorkflowRun']} })
    deposited_to_pdb: Optional[bool] = Field(default=None, description="""Whether structure was deposited to PDB""", json_schema_extra = { "linkml_meta": {'alias': 'deposited_to_pdb', 'domain_of': ['WorkflowRun']} })
    pdb_id: Optional[str] = Field(default=None, description="""PDB accession code if deposited""", json_schema_extra = { "linkml_meta": {'alias': 'pdb_id', 'domain_of': ['WorkflowRun']} })
    validation_report_path: Optional[str] = Field(default=None, description="""Path to validation report""", json_schema_extra = { "linkml_meta": {'alias': 'validation_report_path', 'domain_of': ['WorkflowRun']} })
    space_group: Optional[str] = Field(default=None, description="""Crystallographic space group""", json_schema_extra = { "linkml_meta": {'alias': 'space_group',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Space_Group',
                            'mmCIF:_symmetry.space_group_name_H-M']} })
    unit_cell_a: Optional[float] = Field(default=None, description="""Unit cell parameter a""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_a',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Unit_Cell_a', 'mmCIF:_cell.length_a'],
         'unit': {'ucum_code': 'Ao'}} })
    unit_cell_b: Optional[float] = Field(default=None, description="""Unit cell parameter b""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_b',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Unit_Cell_b', 'mmCIF:_cell.length_b'],
         'unit': {'ucum_code': 'Ao'}} })
    unit_cell_c: Optional[float] = Field(default=None, description="""Unit cell parameter c""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_c',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Unit_Cell_c', 'mmCIF:_cell.length_c'],
         'unit': {'ucum_code': 'Ao'}} })
    unit_cell_alpha: Optional[float] = Field(default=None, description="""Unit cell angle alpha""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_alpha',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Unit_Cell_alpha', 'mmCIF:_cell.angle_alpha'],
         'unit': {'ucum_code': 'deg'}} })
    unit_cell_beta: Optional[float] = Field(default=None, description="""Unit cell angle beta""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_beta',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Unit_Cell_beta', 'mmCIF:_cell.angle_beta'],
         'unit': {'ucum_code': 'deg'}} })
    unit_cell_gamma: Optional[float] = Field(default=None, description="""Unit cell angle gamma""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_gamma',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Unit_Cell_gamma', 'mmCIF:_cell.angle_gamma'],
         'unit': {'ucum_code': 'deg'}} })
    resolution_high: Optional[float] = Field(default=None, description="""High resolution limit""", json_schema_extra = { "linkml_meta": {'alias': 'resolution_high',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Resolution_High_A',
                            'mmCIF:_reflns.d_resolution_high'],
         'unit': {'ucum_code': 'Ao'}} })
    resolution_low: Optional[float] = Field(default=None, description="""Low resolution limit""", json_schema_extra = { "linkml_meta": {'alias': 'resolution_low',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Resolution_Low_A', 'mmCIF:_reflns.d_resolution_low'],
         'unit': {'ucum_code': 'Ao'}} })
    rmerge: Optional[float] = Field(default=None, description="""Rmerge - merge R-factor""", json_schema_extra = { "linkml_meta": {'alias': 'rmerge',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Rmerge', 'mmCIF:_reflns.pdbx_Rmerge_I_obs']} })
    rpim: Optional[float] = Field(default=None, description="""Rpim - precision-indicating merging R-factor""", json_schema_extra = { "linkml_meta": {'alias': 'rpim',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Rpim', 'mmCIF:_reflns.pdbx_Rpim_I_all']} })
    cc_half: Optional[float] = Field(default=None, description="""Half-set correlation coefficient CC(1/2)""", json_schema_extra = { "linkml_meta": {'alias': 'cc_half',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:CC_half', 'mmCIF:_reflns.pdbx_CC_half']} })
    completeness_percent: Optional[float] = Field(default=None, description="""Data completeness percentage""", json_schema_extra = { "linkml_meta": {'alias': 'completeness_percent',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Completeness', 'mmCIF:_reflns.percent_possible_obs'],
         'unit': {'ucum_code': '%'}} })
    i_over_sigma: Optional[float] = Field(default=None, description="""Mean I/sigma(I) - signal to noise ratio""", json_schema_extra = { "linkml_meta": {'alias': 'i_over_sigma',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:I_over_sigma',
                            'mmCIF:_reflns.pdbx_netI_over_sigmaI']} })
    wilson_b_factor: Optional[float] = Field(default=None, description="""Wilson B-factor""", json_schema_extra = { "linkml_meta": {'alias': 'wilson_b_factor',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Wilson_B', 'mmCIF:_reflns.B_iso_Wilson_estimate'],
         'unit': {'ucum_code': 'Ao2'}} })
    multiplicity: Optional[float] = Field(default=None, description="""Data multiplicity (redundancy)""", json_schema_extra = { "linkml_meta": {'alias': 'multiplicity',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Multiplicity', 'mmCIF:_reflns.pdbx_redundancy']} })
    rwork: Optional[float] = Field(default=None, description="""Refinement R-factor (working set)""", json_schema_extra = { "linkml_meta": {'alias': 'rwork',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Rwork', 'mmCIF:_refine.ls_R_factor_R_work']} })
    rfree: Optional[float] = Field(default=None, description="""R-free (test set)""", json_schema_extra = { "linkml_meta": {'alias': 'rfree',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Rfree', 'mmCIF:_refine.ls_R_factor_R_free']} })
    rmsd_bonds: Optional[float] = Field(default=None, description="""RMSD from ideal bond lengths""", json_schema_extra = { "linkml_meta": {'alias': 'rmsd_bonds',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:RMSD_bonds', 'mmCIF:_refine.ls_d_res_high'],
         'unit': {'ucum_code': 'Ao'}} })
    rmsd_angles: Optional[float] = Field(default=None, description="""RMSD from ideal bond angles""", json_schema_extra = { "linkml_meta": {'alias': 'rmsd_angles',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:RMSD_angles', 'mmCIF:_refine.ls_d_res_low'],
         'unit': {'ucum_code': 'deg'}} })
    ramachandran_favored: Optional[float] = Field(default=None, description="""Percentage of residues in favored Ramachandran regions""", json_schema_extra = { "linkml_meta": {'alias': 'ramachandran_favored',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Ramachandran_Favored',
                            'mmCIF:_refine.pdbx_overall_ESU_R'],
         'unit': {'ucum_code': '%'}} })
    ramachandran_outliers: Optional[float] = Field(default=None, description="""Percentage of Ramachandran outliers""", json_schema_extra = { "linkml_meta": {'alias': 'ramachandran_outliers',
         'domain_of': ['WorkflowRun'],
         'exact_mappings': ['nsls2:Ramachandran_Outliers',
                            'mmCIF:_refine.pdbx_overall_ESU_R_Free'],
         'unit': {'ucum_code': '%'}} })
    clashscore: Optional[float] = Field(default=None, description="""MolProbity clashscore""", json_schema_extra = { "linkml_meta": {'alias': 'clashscore',
         'domain_of': ['WorkflowRun', 'QualityMetrics'],
         'exact_mappings': ['nsls2:Clashscore']} })
    processing_notes: Optional[str] = Field(default=None, description="""Additional notes about processing""", json_schema_extra = { "linkml_meta": {'alias': 'processing_notes', 'domain_of': ['WorkflowRun']} })
    compute_resources: Optional[ComputeResources] = Field(default=None, description="""Computational resources used""", json_schema_extra = { "linkml_meta": {'alias': 'compute_resources', 'domain_of': ['WorkflowRun']} })
    started_at: Optional[str] = Field(default=None, description="""Workflow start time""", json_schema_extra = { "linkml_meta": {'alias': 'started_at', 'domain_of': ['WorkflowRun']} })
    completed_at: Optional[str] = Field(default=None, description="""Workflow completion time""", json_schema_extra = { "linkml_meta": {'alias': 'completed_at', 'domain_of': ['WorkflowRun']} })
    motion_correction_params: Optional[MotionCorrectionParameters] = Field(default=None, description="""Motion correction specific parameters""", json_schema_extra = { "linkml_meta": {'alias': 'motion_correction_params', 'domain_of': ['WorkflowRun']} })
    ctf_estimation_params: Optional[CTFEstimationParameters] = Field(default=None, description="""CTF estimation specific parameters""", json_schema_extra = { "linkml_meta": {'alias': 'ctf_estimation_params', 'domain_of': ['WorkflowRun']} })
    particle_picking_params: Optional[ParticlePickingParameters] = Field(default=None, description="""Particle picking specific parameters""", json_schema_extra = { "linkml_meta": {'alias': 'particle_picking_params', 'domain_of': ['WorkflowRun']} })
    refinement_params: Optional[RefinementParameters] = Field(default=None, description="""3D refinement specific parameters""", json_schema_extra = { "linkml_meta": {'alias': 'refinement_params', 'domain_of': ['WorkflowRun']} })
    fsc_curve: Optional[FSCCurve] = Field(default=None, description="""Fourier Shell Correlation curve data""", json_schema_extra = { "linkml_meta": {'alias': 'fsc_curve', 'domain_of': ['WorkflowRun']} })
    output_files: Optional[list[str]] = Field(default=None, description="""Output files generated""", json_schema_extra = { "linkml_meta": {'alias': 'output_files', 'domain_of': ['WorkflowRun']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class DataFile(NamedThing):
    """
    A data file generated or used in the study
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    file_name: str = Field(default=..., description="""Name of the file""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    file_path: Optional[str] = Field(default=None, description="""Path to the file""", json_schema_extra = { "linkml_meta": {'alias': 'file_path', 'domain_of': ['DataFile']} })
    file_format: FileFormatEnum = Field(default=..., description="""File format""", json_schema_extra = { "linkml_meta": {'alias': 'file_format', 'domain_of': ['DataFile']} })
    file_size_bytes: Optional[int] = Field(default=None, description="""File size in bytes""", json_schema_extra = { "linkml_meta": {'alias': 'file_size_bytes', 'domain_of': ['DataFile']} })
    checksum: Optional[str] = Field(default=None, description="""SHA-256 checksum for data integrity""", json_schema_extra = { "linkml_meta": {'alias': 'checksum', 'domain_of': ['DataFile']} })
    creation_date: Optional[str] = Field(default=None, description="""File creation date""", json_schema_extra = { "linkml_meta": {'alias': 'creation_date', 'domain_of': ['DataFile']} })
    data_type: Optional[DataTypeEnum] = Field(default=None, description="""Type of data in the file""", json_schema_extra = { "linkml_meta": {'alias': 'data_type', 'domain_of': ['DataFile']} })
    storage_uri: Optional[str] = Field(default=None, description="""Storage URI (S3, Globus, etc.)""", json_schema_extra = { "linkml_meta": {'alias': 'storage_uri', 'domain_of': ['DataFile']} })
    related_entity: Optional[str] = Field(default=None, description="""ID of the entity that owns this file""", json_schema_extra = { "linkml_meta": {'alias': 'related_entity', 'domain_of': ['DataFile']} })
    file_role: Optional[str] = Field(default=None, description="""Role of the file (raw, intermediate, final, diagnostic, metadata)""", json_schema_extra = { "linkml_meta": {'alias': 'file_role', 'domain_of': ['DataFile']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Image(NamedThing):
    """
    An image file from structural biology experiments
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    dose: Optional[float] = Field(default=None, description="""Electron dose in e-/Å²""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Image2D(Image):
    """
    A 2D image (micrograph, diffraction pattern)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    defocus: Optional[float] = Field(default=None, description="""Defocus value in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus', 'domain_of': ['Image2D']} })
    astigmatism: Optional[float] = Field(default=None, description="""Astigmatism value in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'astigmatism', 'domain_of': ['Image2D']} })
    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    dose: Optional[float] = Field(default=None, description="""Electron dose in e-/Å²""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Image3D(Image):
    """
    A 3D volume or tomogram
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    dimensions_z: Optional[int] = Field(default=None, description="""Image depth in pixels/slices""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_z', 'domain_of': ['Image3D']} })
    voxel_size: Optional[float] = Field(default=None, description="""Voxel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'voxel_size', 'domain_of': ['Image3D']} })
    reconstruction_method: Optional[str] = Field(default=None, description="""Method used for 3D reconstruction""", json_schema_extra = { "linkml_meta": {'alias': 'reconstruction_method', 'domain_of': ['Image3D']} })
    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    dose: Optional[float] = Field(default=None, description="""Electron dose in e-/Å²""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Movie(Image2D):
    """
    Raw cryo-EM movie with frame-by-frame metadata for motion correction
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    frames: Optional[int] = Field(default=None, description="""Number of frames in the movie""", json_schema_extra = { "linkml_meta": {'alias': 'frames', 'domain_of': ['Movie']} })
    super_resolution: Optional[bool] = Field(default=None, description="""Whether super-resolution mode was used""", json_schema_extra = { "linkml_meta": {'alias': 'super_resolution', 'domain_of': ['Movie']} })
    pixel_size_unbinned: Optional[float] = Field(default=None, description="""Unbinned pixel size in Angstroms per pixel""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size_unbinned', 'domain_of': ['Movie']} })
    timestamp: Optional[str] = Field(default=None, description="""Acquisition timestamp""", json_schema_extra = { "linkml_meta": {'alias': 'timestamp', 'domain_of': ['Movie']} })
    stage_position_x: Optional[float] = Field(default=None, description="""Stage X position in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'stage_position_x', 'domain_of': ['Movie']} })
    stage_position_y: Optional[float] = Field(default=None, description="""Stage Y position in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'stage_position_y', 'domain_of': ['Movie']} })
    stage_position_z: Optional[float] = Field(default=None, description="""Stage Z position in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'stage_position_z', 'domain_of': ['Movie']} })
    nominal_defocus: Optional[float] = Field(default=None, description="""Nominal defocus value in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'nominal_defocus', 'domain_of': ['Movie']} })
    dose_per_frame: Optional[float] = Field(default=None, description="""Electron dose per frame in e-/Angstrom^2""", json_schema_extra = { "linkml_meta": {'alias': 'dose_per_frame', 'domain_of': ['Movie', 'DataCollectionStrategy']} })
    beam_shift_x: Optional[float] = Field(default=None, description="""Beam shift X in microradians""", json_schema_extra = { "linkml_meta": {'alias': 'beam_shift_x', 'domain_of': ['Movie']} })
    beam_shift_y: Optional[float] = Field(default=None, description="""Beam shift Y in microradians""", json_schema_extra = { "linkml_meta": {'alias': 'beam_shift_y', 'domain_of': ['Movie']} })
    ice_thickness_estimate: Optional[float] = Field(default=None, description="""Estimated ice thickness in nanometers""", json_schema_extra = { "linkml_meta": {'alias': 'ice_thickness_estimate', 'domain_of': ['Movie']} })
    grid_square_id: Optional[str] = Field(default=None, description="""Grid square identifier""", json_schema_extra = { "linkml_meta": {'alias': 'grid_square_id', 'domain_of': ['Movie']} })
    hole_id: Optional[str] = Field(default=None, description="""Hole identifier within grid square""", json_schema_extra = { "linkml_meta": {'alias': 'hole_id', 'domain_of': ['Movie']} })
    acquisition_group: Optional[str] = Field(default=None, description="""Acquisition group identifier (e.g., template or area)""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_group', 'domain_of': ['Movie']} })
    defocus: Optional[float] = Field(default=None, description="""Defocus value in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus', 'domain_of': ['Image2D']} })
    astigmatism: Optional[float] = Field(default=None, description="""Astigmatism value in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'astigmatism', 'domain_of': ['Image2D']} })
    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    dose: Optional[float] = Field(default=None, description="""Electron dose in e-/Å²""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class Micrograph(Image2D):
    """
    Motion-corrected micrograph derived from movie
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/',
         'slot_usage': {'astigmatism': {'description': 'Astigmatism in Angstroms',
                                        'name': 'astigmatism'},
                        'defocus': {'description': 'Measured defocus in micrometers',
                                    'name': 'defocus'},
                        'pixel_size': {'description': 'Final pixel size in Angstroms '
                                                      'per pixel',
                                       'name': 'pixel_size'}}})

    dose: Optional[float] = Field(default=None, description="""Total electron dose in e-/Angstrom^2""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    origin_movie_id: Optional[str] = Field(default=None, description="""Reference to original movie file""", json_schema_extra = { "linkml_meta": {'alias': 'origin_movie_id', 'domain_of': ['Micrograph']} })
    defocus_u: Optional[float] = Field(default=None, description="""Defocus U in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_u', 'domain_of': ['Micrograph']} })
    defocus_v: Optional[float] = Field(default=None, description="""Defocus V in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_v', 'domain_of': ['Micrograph']} })
    astigmatism_angle: Optional[float] = Field(default=None, description="""Astigmatism angle in degrees""", json_schema_extra = { "linkml_meta": {'alias': 'astigmatism_angle', 'domain_of': ['Micrograph']} })
    resolution_fit_limit: Optional[float] = Field(default=None, description="""Resolution fit limit in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'resolution_fit_limit', 'domain_of': ['Micrograph']} })
    ctf_quality_score: Optional[float] = Field(default=None, description="""CTF estimation quality score""", json_schema_extra = { "linkml_meta": {'alias': 'ctf_quality_score', 'domain_of': ['Micrograph']} })
    defocus: Optional[float] = Field(default=None, description="""Measured defocus in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus', 'domain_of': ['Image2D']} })
    astigmatism: Optional[float] = Field(default=None, description="""Astigmatism in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'astigmatism', 'domain_of': ['Image2D']} })
    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Final pixel size in Angstroms per pixel""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class FTIRImage(Image):
    """
    Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    wavenumber_min: Optional[float] = Field(default=None, description="""Minimum wavenumber in cm⁻¹""", json_schema_extra = { "linkml_meta": {'alias': 'wavenumber_min', 'domain_of': ['FTIRImage']} })
    wavenumber_max: Optional[float] = Field(default=None, description="""Maximum wavenumber in cm⁻¹""", json_schema_extra = { "linkml_meta": {'alias': 'wavenumber_max', 'domain_of': ['FTIRImage']} })
    spectral_resolution: Optional[float] = Field(default=None, description="""Spectral resolution in cm⁻¹""", json_schema_extra = { "linkml_meta": {'alias': 'spectral_resolution', 'domain_of': ['FTIRImage']} })
    number_of_scans: Optional[int] = Field(default=None, description="""Number of scans averaged for the spectrum""", json_schema_extra = { "linkml_meta": {'alias': 'number_of_scans', 'domain_of': ['FTIRImage']} })
    apodization_function: Optional[str] = Field(default=None, description="""Mathematical function used for apodization""", json_schema_extra = { "linkml_meta": {'alias': 'apodization_function', 'domain_of': ['FTIRImage']} })
    molecular_signatures: Optional[list[str]] = Field(default=None, description="""Identified molecular signatures or peaks""", json_schema_extra = { "linkml_meta": {'alias': 'molecular_signatures', 'domain_of': ['FTIRImage']} })
    background_correction: Optional[str] = Field(default=None, description="""Method used for background correction""", json_schema_extra = { "linkml_meta": {'alias': 'background_correction', 'domain_of': ['FTIRImage']} })
    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    dose: Optional[float] = Field(default=None, description="""Electron dose in e-/Å²""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class FluorescenceImage(Image2D):
    """
    Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    excitation_wavelength: Optional[float] = Field(default=None, description="""Excitation wavelength in nanometers""", json_schema_extra = { "linkml_meta": {'alias': 'excitation_wavelength', 'domain_of': ['FluorescenceImage']} })
    emission_wavelength: Optional[float] = Field(default=None, description="""Emission wavelength in nanometers""", json_schema_extra = { "linkml_meta": {'alias': 'emission_wavelength', 'domain_of': ['FluorescenceImage']} })
    excitation_filter: Optional[str] = Field(default=None, description="""Specifications of the excitation filter""", json_schema_extra = { "linkml_meta": {'alias': 'excitation_filter', 'domain_of': ['FluorescenceImage']} })
    emission_filter: Optional[str] = Field(default=None, description="""Specifications of the emission filter""", json_schema_extra = { "linkml_meta": {'alias': 'emission_filter', 'domain_of': ['FluorescenceImage']} })
    fluorophore: Optional[str] = Field(default=None, description="""Name or type of fluorophore used""", json_schema_extra = { "linkml_meta": {'alias': 'fluorophore', 'domain_of': ['FluorescenceImage']} })
    channel_name: Optional[str] = Field(default=None, description="""Name of the fluorescence channel (e.g., DAPI, GFP, RFP)""", json_schema_extra = { "linkml_meta": {'alias': 'channel_name', 'domain_of': ['FluorescenceImage']} })
    laser_power: Optional[float] = Field(default=None, description="""Laser power in milliwatts or percentage""", json_schema_extra = { "linkml_meta": {'alias': 'laser_power', 'domain_of': ['FluorescenceImage']} })
    pinhole_size: Optional[float] = Field(default=None, description="""Pinhole size in Airy units for confocal microscopy""", json_schema_extra = { "linkml_meta": {'alias': 'pinhole_size', 'domain_of': ['FluorescenceImage']} })
    quantum_yield: Optional[float] = Field(default=None, description="""Quantum yield of the fluorophore""", json_schema_extra = { "linkml_meta": {'alias': 'quantum_yield', 'domain_of': ['FluorescenceImage']} })
    defocus: Optional[float] = Field(default=None, description="""Defocus value in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus', 'domain_of': ['Image2D']} })
    astigmatism: Optional[float] = Field(default=None, description="""Astigmatism value in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'astigmatism', 'domain_of': ['Image2D']} })
    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    dose: Optional[float] = Field(default=None, description="""Electron dose in e-/Å²""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class OpticalImage(Image2D):
    """
    Visible light optical microscopy or photography image
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    illumination_type: Optional[IlluminationTypeEnum] = Field(default=None, description="""Type of illumination (brightfield, darkfield, phase contrast, DIC)""", json_schema_extra = { "linkml_meta": {'alias': 'illumination_type', 'domain_of': ['OpticalImage']} })
    magnification: Optional[float] = Field(default=None, description="""Optical magnification factor""", json_schema_extra = { "linkml_meta": {'alias': 'magnification', 'domain_of': ['ExperimentRun', 'OpticalImage']} })
    numerical_aperture: Optional[float] = Field(default=None, description="""Numerical aperture of the objective lens""", json_schema_extra = { "linkml_meta": {'alias': 'numerical_aperture', 'domain_of': ['OpticalImage']} })
    color_channels: Optional[list[str]] = Field(default=None, description="""Color channels present (e.g., RGB, grayscale)""", json_schema_extra = { "linkml_meta": {'alias': 'color_channels', 'domain_of': ['OpticalImage']} })
    white_balance: Optional[str] = Field(default=None, description="""White balance settings""", json_schema_extra = { "linkml_meta": {'alias': 'white_balance', 'domain_of': ['OpticalImage']} })
    contrast_method: Optional[str] = Field(default=None, description="""Contrast enhancement method used""", json_schema_extra = { "linkml_meta": {'alias': 'contrast_method', 'domain_of': ['OpticalImage']} })
    defocus: Optional[float] = Field(default=None, description="""Defocus value in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus', 'domain_of': ['Image2D']} })
    astigmatism: Optional[float] = Field(default=None, description="""Astigmatism value in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'astigmatism', 'domain_of': ['Image2D']} })
    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    dose: Optional[float] = Field(default=None, description="""Electron dose in e-/Å²""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class XRFImage(Image2D):
    """
    X-ray fluorescence (XRF) image showing elemental distribution
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    beam_energy: Optional[float] = Field(default=None, description="""X-ray beam energy in keV""", json_schema_extra = { "linkml_meta": {'alias': 'beam_energy', 'domain_of': ['XRFImage', 'ExperimentalConditions']} })
    beam_size: Optional[float] = Field(default=None, description="""X-ray beam size in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'beam_size', 'domain_of': ['XRFImage']} })
    dwell_time: Optional[float] = Field(default=None, description="""Dwell time per pixel in milliseconds""", json_schema_extra = { "linkml_meta": {'alias': 'dwell_time', 'domain_of': ['XRFImage']} })
    elements_measured: Optional[list[str]] = Field(default=None, description="""Elements detected and measured""", json_schema_extra = { "linkml_meta": {'alias': 'elements_measured', 'domain_of': ['XRFImage']} })
    source_type: Optional[XRaySourceTypeEnum] = Field(default=None, description="""X-ray source type (synchrotron or lab-source)""", json_schema_extra = { "linkml_meta": {'alias': 'source_type', 'domain_of': ['XRayInstrument', 'XRFImage']} })
    detector_technology: Optional[DetectorTechnologyEnum] = Field(default=None, description="""Type of X-ray detector technology used""", json_schema_extra = { "linkml_meta": {'alias': 'detector_technology',
         'comments': ['For XRF, typically energy-dispersive or wavelength-dispersive '
                      'detectors'],
         'domain_of': ['CryoEMInstrument', 'XRayInstrument', 'XRFImage']} })
    detector_model: Optional[str] = Field(default=None, description="""Specific detector model used for XRF measurement""", json_schema_extra = { "linkml_meta": {'alias': 'detector_model',
         'domain_of': ['CryoEMInstrument', 'XRayInstrument', 'XRFImage']} })
    flux: Optional[float] = Field(default=None, description="""Photon flux in photons/second""", json_schema_extra = { "linkml_meta": {'alias': 'flux', 'domain_of': ['XRFImage']} })
    calibration_standard: Optional[str] = Field(default=None, description="""Reference standard used for calibration""", json_schema_extra = { "linkml_meta": {'alias': 'calibration_standard', 'domain_of': ['XRFImage']} })
    defocus: Optional[float] = Field(default=None, description="""Defocus value in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus', 'domain_of': ['Image2D']} })
    astigmatism: Optional[float] = Field(default=None, description="""Astigmatism value in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'astigmatism', 'domain_of': ['Image2D']} })
    file_name: str = Field(default=..., description="""Image file name""", json_schema_extra = { "linkml_meta": {'alias': 'file_name', 'domain_of': ['DataFile', 'Image']} })
    acquisition_date: Optional[str] = Field(default=None, description="""Date image was acquired""", json_schema_extra = { "linkml_meta": {'alias': 'acquisition_date', 'domain_of': ['Image']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    dimensions_x: Optional[int] = Field(default=None, description="""Image width in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_x', 'domain_of': ['Image']} })
    dimensions_y: Optional[int] = Field(default=None, description="""Image height in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'dimensions_y', 'domain_of': ['Image']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    dose: Optional[float] = Field(default=None, description="""Electron dose in e-/Å²""", json_schema_extra = { "linkml_meta": {'alias': 'dose', 'domain_of': ['Image', 'Micrograph']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class ImageFeature(AttributeGroup):
    """
    Semantic annotations describing features identified in images using controlled vocabulary terms
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    terms: Optional[list[OntologyTerm]] = Field(default=None, description="""Ontology terms describing features identified in the image""", json_schema_extra = { "linkml_meta": {'alias': 'terms', 'domain_of': ['ImageFeature', 'OntologyTerm']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class OntologyTerm(NamedThing):
    """
    A term from a controlled vocabulary or ontology
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    terms: Optional[list[OntologyTerm]] = Field(default=None, description="""Collection of ontology terms""", json_schema_extra = { "linkml_meta": {'alias': 'terms', 'domain_of': ['ImageFeature', 'OntologyTerm']} })
    label: Optional[str] = Field(default=None, description="""The human-readable label or name of the ontology term""", json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['OntologyTerm']} })
    definition: Optional[str] = Field(default=None, description="""The formal definition or meaning of the ontology term""", json_schema_extra = { "linkml_meta": {'alias': 'definition', 'domain_of': ['OntologyTerm']} })
    ontology: Optional[str] = Field(default=None, description="""The ontology or controlled vocabulary this term comes from (e.g., GO, SO, UBERON)""", json_schema_extra = { "linkml_meta": {'alias': 'ontology', 'domain_of': ['OntologyTerm']} })
    id: str = Field(default=..., description="""Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    title: Optional[str] = Field(default=None, description="""A human-readable name or title for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['NamedThing'], 'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A detailed textual description of this entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class MolecularComposition(AttributeGroup):
    """
    Molecular composition of a sample
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    sequences: Optional[list[str]] = Field(default=None, description="""Amino acid or nucleotide sequences""", json_schema_extra = { "linkml_meta": {'alias': 'sequences', 'domain_of': ['MolecularComposition']} })
    modifications: Optional[list[str]] = Field(default=None, description="""Post-translational modifications or chemical modifications""", json_schema_extra = { "linkml_meta": {'alias': 'modifications', 'domain_of': ['MolecularComposition']} })
    ligands: Optional[list[str]] = Field(default=None, description="""Bound ligands or cofactors""", json_schema_extra = { "linkml_meta": {'alias': 'ligands', 'domain_of': ['MolecularComposition']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class BufferComposition(AttributeGroup):
    """
    Buffer composition for sample storage
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    ph: Optional[float] = Field(default=None, description="""pH of the buffer (range: 0-14)""", ge=0, le=14, json_schema_extra = { "linkml_meta": {'alias': 'ph', 'domain_of': ['MeasurementConditions', 'BufferComposition']} })
    components: Optional[list[str]] = Field(default=None, description="""Buffer components and their concentrations""", json_schema_extra = { "linkml_meta": {'alias': 'components', 'domain_of': ['BufferComposition']} })
    additives: Optional[list[str]] = Field(default=None, description="""Additional additives in the buffer""", json_schema_extra = { "linkml_meta": {'alias': 'additives', 'domain_of': ['BufferComposition', 'XRayPreparation']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class StorageConditions(AttributeGroup):
    """
    Storage conditions for samples
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    temperature: Optional[float] = Field(default=None, description="""Storage temperature in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'temperature',
         'domain_of': ['MeasurementConditions',
                       'StorageConditions',
                       'ExperimentalConditions']} })
    temperature_unit: Optional[TemperatureUnitEnum] = Field(default=None, description="""Temperature unit""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_unit', 'domain_of': ['StorageConditions']} })
    duration: Optional[str] = Field(default=None, description="""Storage duration""", json_schema_extra = { "linkml_meta": {'alias': 'duration', 'domain_of': ['StorageConditions']} })
    atmosphere: Optional[str] = Field(default=None, description="""Storage atmosphere conditions""", json_schema_extra = { "linkml_meta": {'alias': 'atmosphere',
         'domain_of': ['StorageConditions', 'ExperimentalConditions']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class TechniqueSpecificPreparation(AttributeGroup):
    """
    Base class for technique-specific preparation details
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class CryoEMPreparation(TechniqueSpecificPreparation):
    """
    Cryo-EM specific sample preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    grid_type: Optional[GridTypeEnum] = Field(default=None, description="""Type of EM grid used""", json_schema_extra = { "linkml_meta": {'alias': 'grid_type', 'domain_of': ['CryoEMPreparation']} })
    support_film: Optional[str] = Field(default=None, description="""Support film type""", json_schema_extra = { "linkml_meta": {'alias': 'support_film', 'domain_of': ['CryoEMPreparation']} })
    hole_size: Optional[float] = Field(default=None, description="""Hole size in micrometers (range: 0.5-5.0)""", ge=0.5, le=5.0, json_schema_extra = { "linkml_meta": {'alias': 'hole_size', 'domain_of': ['CryoEMPreparation']} })
    vitrification_method: Optional[VitrificationMethodEnum] = Field(default=None, description="""Method used for vitrification""", json_schema_extra = { "linkml_meta": {'alias': 'vitrification_method', 'domain_of': ['CryoEMPreparation']} })
    blot_time: Optional[float] = Field(default=None, description="""Blotting time in seconds (range: 0.5-10.0)""", ge=0.5, le=10.0, json_schema_extra = { "linkml_meta": {'alias': 'blot_time', 'domain_of': ['CryoEMPreparation']} })
    blot_force: Optional[int] = Field(default=None, description="""Blotting force setting""", json_schema_extra = { "linkml_meta": {'alias': 'blot_force', 'domain_of': ['CryoEMPreparation']} })
    humidity_percentage: Optional[float] = Field(default=None, description="""Chamber humidity during vitrification (range: 0-100)""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'alias': 'humidity_percentage', 'domain_of': ['CryoEMPreparation']} })
    chamber_temperature: Optional[float] = Field(default=None, description="""Chamber temperature in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'chamber_temperature', 'domain_of': ['CryoEMPreparation']} })
    grid_material: Optional[GridMaterialEnum] = Field(default=None, description="""Grid material""", json_schema_extra = { "linkml_meta": {'alias': 'grid_material', 'domain_of': ['CryoEMPreparation']} })
    glow_discharge_applied: Optional[bool] = Field(default=None, description="""Whether glow discharge treatment was applied""", json_schema_extra = { "linkml_meta": {'alias': 'glow_discharge_applied', 'domain_of': ['CryoEMPreparation']} })
    glow_discharge_time: Optional[float] = Field(default=None, description="""Glow discharge time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'glow_discharge_time', 'domain_of': ['CryoEMPreparation']} })
    glow_discharge_current: Optional[float] = Field(default=None, description="""Glow discharge current in milliamperes""", json_schema_extra = { "linkml_meta": {'alias': 'glow_discharge_current', 'domain_of': ['CryoEMPreparation']} })
    glow_discharge_atmosphere: Optional[str] = Field(default=None, description="""Glow discharge atmosphere (air, amylamine)""", json_schema_extra = { "linkml_meta": {'alias': 'glow_discharge_atmosphere', 'domain_of': ['CryoEMPreparation']} })
    glow_discharge_pressure: Optional[float] = Field(default=None, description="""Glow discharge pressure in millibar""", json_schema_extra = { "linkml_meta": {'alias': 'glow_discharge_pressure', 'domain_of': ['CryoEMPreparation']} })
    vitrification_instrument: Optional[str] = Field(default=None, description="""Vitrification instrument used (e.g., Vitrobot)""", json_schema_extra = { "linkml_meta": {'alias': 'vitrification_instrument', 'domain_of': ['CryoEMPreparation']} })
    blot_number: Optional[int] = Field(default=None, description="""Number of blots applied""", json_schema_extra = { "linkml_meta": {'alias': 'blot_number', 'domain_of': ['CryoEMPreparation']} })
    wait_time: Optional[float] = Field(default=None, description="""Wait time before blotting in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'wait_time', 'domain_of': ['CryoEMPreparation']} })
    blotter_height: Optional[float] = Field(default=None, description="""Blotter height setting""", json_schema_extra = { "linkml_meta": {'alias': 'blotter_height', 'domain_of': ['CryoEMPreparation']} })
    blotter_setting: Optional[float] = Field(default=None, description="""Blotter setting value""", json_schema_extra = { "linkml_meta": {'alias': 'blotter_setting', 'domain_of': ['CryoEMPreparation']} })
    sample_applied_volume: Optional[float] = Field(default=None, description="""Volume of sample applied in microliters""", json_schema_extra = { "linkml_meta": {'alias': 'sample_applied_volume', 'domain_of': ['CryoEMPreparation']} })
    ethane_temperature: Optional[float] = Field(default=None, description="""Ethane temperature in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'ethane_temperature', 'domain_of': ['CryoEMPreparation']} })
    plasma_treatment: Optional[str] = Field(default=None, description="""Plasma treatment details""", json_schema_extra = { "linkml_meta": {'alias': 'plasma_treatment', 'domain_of': ['CryoEMPreparation']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class CrystallizationConditions(AttributeGroup):
    """
    Crystal growth conditions for X-ray crystallography (NSLS2 Crystallization mapping)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    method: Optional[CrystallizationMethodEnum] = Field(default=None, description="""Crystallization method used""", json_schema_extra = { "linkml_meta": {'alias': 'method',
         'comments': ['Maps to NSLS2 spreadsheet: Method'],
         'domain_of': ['CrystallizationConditions'],
         'slot_uri': 'nsls2:Method'} })
    crystallization_conditions: Optional[str] = Field(default=None, description="""Complete description of crystallization conditions including precipitant, pH, salts""", json_schema_extra = { "linkml_meta": {'alias': 'crystallization_conditions',
         'comments': ['Maps to NSLS2 spreadsheet: Conditions'],
         'domain_of': ['CrystallizationConditions', 'XRayPreparation'],
         'slot_uri': 'nsls2:Conditions'} })
    drop_volume: Optional[float] = Field(default=None, description="""Total drop volume in nanoliters""", json_schema_extra = { "linkml_meta": {'alias': 'drop_volume',
         'comments': ['Maps to NSLS2 spreadsheet: Drop_Volume'],
         'domain_of': ['CrystallizationConditions'],
         'slot_uri': 'nsls2:Drop_Volume'} })
    protein_concentration: Optional[float] = Field(default=None, description="""Protein concentration for crystallization in mg/mL""", json_schema_extra = { "linkml_meta": {'alias': 'protein_concentration',
         'comments': ['Maps to NSLS2 spreadsheet: Protein_Concentration'],
         'domain_of': ['CrystallizationConditions'],
         'slot_uri': 'nsls2:Protein_Concentration'} })
    crystal_size_um: Optional[str] = Field(default=None, description="""Crystal dimensions in micrometers (length x width x height)""", json_schema_extra = { "linkml_meta": {'alias': 'crystal_size_um',
         'comments': ['Maps to NSLS2 spreadsheet: Crystal_Size'],
         'domain_of': ['CrystallizationConditions', 'XRayPreparation'],
         'slot_uri': 'nsls2:Crystal_Size'} })
    cryo_protectant: Optional[str] = Field(default=None, description="""Cryoprotectant used for crystal cooling""", json_schema_extra = { "linkml_meta": {'alias': 'cryo_protectant',
         'comments': ['Maps to NSLS2 spreadsheet: Cryo_Protectant'],
         'domain_of': ['CrystallizationConditions'],
         'slot_uri': 'nsls2:Cryo_Protectant'} })
    crystal_id: Optional[str] = Field(default=None, description="""Identifier for the specific crystal used""", json_schema_extra = { "linkml_meta": {'alias': 'crystal_id',
         'comments': ['Maps to NSLS2 spreadsheet: Crystal_ID'],
         'domain_of': ['CrystallizationConditions'],
         'slot_uri': 'nsls2:Crystal_ID'} })
    screen_name: Optional[str] = Field(default=None, description="""Name of crystallization screen used""", json_schema_extra = { "linkml_meta": {'alias': 'screen_name',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    temperature_c: Optional[float] = Field(default=None, description="""Crystallization temperature in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_c',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    drop_ratio_protein_to_reservoir: Optional[str] = Field(default=None, description="""Ratio of protein to reservoir solution in drop (e.g., 1:1, 2:1)""", json_schema_extra = { "linkml_meta": {'alias': 'drop_ratio_protein_to_reservoir',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    reservoir_volume_ul: Optional[float] = Field(default=None, description="""Reservoir volume in microliters""", json_schema_extra = { "linkml_meta": {'alias': 'reservoir_volume_ul',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    seeding_type: Optional[str] = Field(default=None, description="""Type of seeding used (micro, macro, streak)""", json_schema_extra = { "linkml_meta": {'alias': 'seeding_type',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    seed_stock_dilution: Optional[str] = Field(default=None, description="""Dilution factor for seed stock""", json_schema_extra = { "linkml_meta": {'alias': 'seed_stock_dilution',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class XRayPreparation(TechniqueSpecificPreparation):
    """
    X-ray crystallography specific preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    protein_concentration_mg_per_ml: Optional[float] = Field(default=None, description="""Protein concentration for crystallization in mg/mL""", json_schema_extra = { "linkml_meta": {'alias': 'protein_concentration_mg_per_ml', 'domain_of': ['XRayPreparation']} })
    protein_buffer: Optional[str] = Field(default=None, description="""Buffer composition for protein solution""", json_schema_extra = { "linkml_meta": {'alias': 'protein_buffer', 'domain_of': ['XRayPreparation']} })
    additives: Optional[str] = Field(default=None, description="""Additives mixed with protein before crystallization""", json_schema_extra = { "linkml_meta": {'alias': 'additives', 'domain_of': ['BufferComposition', 'XRayPreparation']} })
    crystallization_method: Optional[CrystallizationMethodEnum] = Field(default=None, description="""Method used for crystallization""", json_schema_extra = { "linkml_meta": {'alias': 'crystallization_method', 'domain_of': ['XRayPreparation']} })
    crystallization_conditions: Optional[CrystallizationConditions] = Field(default=None, description="""Detailed crystallization conditions""", json_schema_extra = { "linkml_meta": {'alias': 'crystallization_conditions',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    screen_name: Optional[str] = Field(default=None, description="""Name of crystallization screen used""", json_schema_extra = { "linkml_meta": {'alias': 'screen_name',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    temperature_c: Optional[float] = Field(default=None, description="""Crystallization temperature in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_c',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    drop_ratio_protein_to_reservoir: Optional[str] = Field(default=None, description="""Ratio of protein to reservoir solution in drop (e.g., 1:1, 2:1)""", json_schema_extra = { "linkml_meta": {'alias': 'drop_ratio_protein_to_reservoir',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    drop_volume_nl: Optional[float] = Field(default=None, description="""Total drop volume in nanoliters""", json_schema_extra = { "linkml_meta": {'alias': 'drop_volume_nl', 'domain_of': ['XRayPreparation']} })
    reservoir_volume_ul: Optional[float] = Field(default=None, description="""Reservoir volume in microliters""", json_schema_extra = { "linkml_meta": {'alias': 'reservoir_volume_ul',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    seeding_type: Optional[str] = Field(default=None, description="""Type of seeding used (micro, macro, streak)""", json_schema_extra = { "linkml_meta": {'alias': 'seeding_type',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    seed_stock_dilution: Optional[str] = Field(default=None, description="""Dilution factor for seed stock""", json_schema_extra = { "linkml_meta": {'alias': 'seed_stock_dilution',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    initial_hit_condition: Optional[str] = Field(default=None, description="""Description of initial crystallization hit condition""", json_schema_extra = { "linkml_meta": {'alias': 'initial_hit_condition', 'domain_of': ['XRayPreparation']} })
    optimization_strategy: Optional[str] = Field(default=None, description="""Strategy used to optimize crystals""", json_schema_extra = { "linkml_meta": {'alias': 'optimization_strategy', 'domain_of': ['XRayPreparation']} })
    optimized_condition: Optional[str] = Field(default=None, description="""Final optimized crystallization condition""", json_schema_extra = { "linkml_meta": {'alias': 'optimized_condition', 'domain_of': ['XRayPreparation']} })
    crystal_size_um: Optional[str] = Field(default=None, description="""Crystal dimensions in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'crystal_size_um',
         'domain_of': ['CrystallizationConditions', 'XRayPreparation']} })
    cryoprotectant: Optional[str] = Field(default=None, description="""Cryoprotectant used""", json_schema_extra = { "linkml_meta": {'alias': 'cryoprotectant', 'domain_of': ['XRayPreparation']} })
    cryoprotectant_concentration: Optional[float] = Field(default=None, description="""Cryoprotectant concentration percentage""", json_schema_extra = { "linkml_meta": {'alias': 'cryoprotectant_concentration', 'domain_of': ['XRayPreparation']} })
    soak_compound: Optional[str] = Field(default=None, description="""Compound used for soaking (ligand, heavy atom)""", json_schema_extra = { "linkml_meta": {'alias': 'soak_compound', 'domain_of': ['XRayPreparation']} })
    soak_conditions: Optional[str] = Field(default=None, description="""Conditions for crystal soaking""", json_schema_extra = { "linkml_meta": {'alias': 'soak_conditions', 'domain_of': ['XRayPreparation']} })
    mounting_method: Optional[str] = Field(default=None, description="""Crystal mounting method""", json_schema_extra = { "linkml_meta": {'alias': 'mounting_method',
         'comments': ['Maps to NSLS2 spreadsheet: Mount_Type'],
         'domain_of': ['XRayPreparation'],
         'slot_uri': 'nsls2:Mount_Type'} })
    flash_cooling_method: Optional[str] = Field(default=None, description="""Flash cooling protocol""", json_schema_extra = { "linkml_meta": {'alias': 'flash_cooling_method', 'domain_of': ['XRayPreparation']} })
    crystal_notes: Optional[str] = Field(default=None, description="""Additional notes about crystal quality and handling""", json_schema_extra = { "linkml_meta": {'alias': 'crystal_notes', 'domain_of': ['XRayPreparation']} })
    loop_size: Optional[float] = Field(default=None, description="""Loop size in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'loop_size',
         'comments': ['Maps to NSLS2 spreadsheet: Loop_Size'],
         'domain_of': ['XRayPreparation'],
         'slot_uri': 'nsls2:Loop_Size'} })
    mounting_temperature: Optional[float] = Field(default=None, description="""Temperature during mounting in Kelvin""", json_schema_extra = { "linkml_meta": {'alias': 'mounting_temperature',
         'comments': ['Maps to NSLS2 spreadsheet: Temperature'],
         'domain_of': ['XRayPreparation'],
         'slot_uri': 'nsls2:Temperature'} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class SAXSPreparation(TechniqueSpecificPreparation):
    """
    SAXS/WAXS specific preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    concentration_series: Optional[list[float]] = Field(default=None, description="""Concentration values for series measurements""", json_schema_extra = { "linkml_meta": {'alias': 'concentration_series', 'domain_of': ['SAXSPreparation']} })
    buffer_matching_protocol: Optional[str] = Field(default=None, description="""Protocol for buffer matching""", json_schema_extra = { "linkml_meta": {'alias': 'buffer_matching_protocol', 'domain_of': ['SAXSPreparation']} })
    sample_cell_type: Optional[str] = Field(default=None, description="""Type of sample cell used""", json_schema_extra = { "linkml_meta": {'alias': 'sample_cell_type', 'domain_of': ['SAXSPreparation']} })
    cell_path_length: Optional[float] = Field(default=None, description="""Path length in mm""", json_schema_extra = { "linkml_meta": {'alias': 'cell_path_length', 'domain_of': ['SAXSPreparation']} })
    temperature_control: Optional[str] = Field(default=None, description="""Temperature control settings""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_control', 'domain_of': ['SAXSPreparation']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class ExperimentalConditions(AttributeGroup):
    """
    Environmental and experimental conditions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    temperature: Optional[float] = Field(default=None, description="""Temperature in Celsius""", json_schema_extra = { "linkml_meta": {'alias': 'temperature',
         'domain_of': ['MeasurementConditions',
                       'StorageConditions',
                       'ExperimentalConditions']} })
    humidity: Optional[float] = Field(default=None, description="""Humidity percentage""", json_schema_extra = { "linkml_meta": {'alias': 'humidity', 'domain_of': ['ExperimentalConditions']} })
    pressure: Optional[float] = Field(default=None, description="""Pressure in kPa""", json_schema_extra = { "linkml_meta": {'alias': 'pressure', 'domain_of': ['ExperimentalConditions']} })
    atmosphere: Optional[str] = Field(default=None, description="""Atmosphere composition""", json_schema_extra = { "linkml_meta": {'alias': 'atmosphere',
         'domain_of': ['StorageConditions', 'ExperimentalConditions']} })
    beam_energy: Optional[float] = Field(default=None, description="""Beam energy in keV""", json_schema_extra = { "linkml_meta": {'alias': 'beam_energy', 'domain_of': ['XRFImage', 'ExperimentalConditions']} })
    exposure_time: Optional[float] = Field(default=None, description="""Exposure time in seconds""", json_schema_extra = { "linkml_meta": {'alias': 'exposure_time', 'domain_of': ['Image', 'ExperimentalConditions']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class DataCollectionStrategy(AttributeGroup):
    """
    Strategy for data collection
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    collection_mode: Optional[CollectionModeEnum] = Field(default=None, description="""Mode of data collection""", json_schema_extra = { "linkml_meta": {'alias': 'collection_mode', 'domain_of': ['DataCollectionStrategy']} })
    total_frames: Optional[int] = Field(default=None, description="""Total number of frames/images""", json_schema_extra = { "linkml_meta": {'alias': 'total_frames', 'domain_of': ['DataCollectionStrategy']} })
    frame_rate: Optional[float] = Field(default=None, description="""Frames per second""", json_schema_extra = { "linkml_meta": {'alias': 'frame_rate', 'domain_of': ['DataCollectionStrategy']} })
    total_dose: Optional[float] = Field(default=None, description="""Total electron dose for cryo-EM""", json_schema_extra = { "linkml_meta": {'alias': 'total_dose',
         'domain_of': ['ExperimentRun', 'DataCollectionStrategy']} })
    dose_per_frame: Optional[float] = Field(default=None, description="""Dose per frame""", json_schema_extra = { "linkml_meta": {'alias': 'dose_per_frame', 'domain_of': ['Movie', 'DataCollectionStrategy']} })
    wavelength_a: Optional[float] = Field(default=None, description="""X-ray wavelength in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'wavelength_a', 'domain_of': ['DataCollectionStrategy']} })
    detector_mode: Optional[DetectorModeEnum] = Field(default=None, description="""Detector operating mode used during this experiment""", json_schema_extra = { "linkml_meta": {'alias': 'detector_mode',
         'comments': ['For cryo-EM: counting, integrating, or super_resolution',
                      'Detector technology, manufacturer, and model are specified in '
                      'the Instrument'],
         'domain_of': ['CryoEMInstrument', 'DataCollectionStrategy']} })
    pixel_size_calibrated: Optional[float] = Field(default=None, description="""Calibrated pixel size for this experiment""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size_calibrated',
         'comments': ['For cryo-EM: depends on magnification (Å/pixel)',
                      'For X-ray: typically mm/pixel or µm/pixel',
                      'Physical pixel size is hardware spec stored in Instrument'],
         'domain_of': ['DataCollectionStrategy'],
         'unit': {'ucum_code': 'Ao/px'}} })
    detector_distance_mm: Optional[float] = Field(default=None, description="""Detector distance in millimeters""", json_schema_extra = { "linkml_meta": {'alias': 'detector_distance_mm', 'domain_of': ['DataCollectionStrategy']} })
    beam_center_x_px: Optional[int] = Field(default=None, description="""Beam center X coordinate in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'beam_center_x_px', 'domain_of': ['DataCollectionStrategy']} })
    beam_center_y_px: Optional[int] = Field(default=None, description="""Beam center Y coordinate in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'beam_center_y_px', 'domain_of': ['DataCollectionStrategy']} })
    beam_size_um: Optional[float] = Field(default=None, description="""Beam size in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'beam_size_um', 'domain_of': ['DataCollectionStrategy']} })
    flux_photons_per_s: Optional[float] = Field(default=None, description="""Photon flux in photons per second""", json_schema_extra = { "linkml_meta": {'alias': 'flux_photons_per_s', 'domain_of': ['DataCollectionStrategy']} })
    transmission_percent: Optional[float] = Field(default=None, description="""Beam transmission percentage""", json_schema_extra = { "linkml_meta": {'alias': 'transmission_percent', 'domain_of': ['DataCollectionStrategy']} })
    attenuator: Optional[str] = Field(default=None, description="""Attenuator setting used""", json_schema_extra = { "linkml_meta": {'alias': 'attenuator', 'domain_of': ['DataCollectionStrategy']} })
    temperature_k: Optional[float] = Field(default=None, description="""Data collection temperature in Kelvin""", json_schema_extra = { "linkml_meta": {'alias': 'temperature_k', 'domain_of': ['DataCollectionStrategy']} })
    oscillation_per_image_deg: Optional[float] = Field(default=None, description="""Oscillation angle per image in degrees""", json_schema_extra = { "linkml_meta": {'alias': 'oscillation_per_image_deg', 'domain_of': ['DataCollectionStrategy']} })
    total_rotation_deg: Optional[float] = Field(default=None, description="""Total rotation range in degrees""", json_schema_extra = { "linkml_meta": {'alias': 'total_rotation_deg', 'domain_of': ['DataCollectionStrategy']} })
    strategy_notes: Optional[str] = Field(default=None, description="""Notes about data collection strategy""", json_schema_extra = { "linkml_meta": {'alias': 'strategy_notes', 'domain_of': ['DataCollectionStrategy']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class QualityMetrics(AttributeGroup):
    """
    Quality metrics for experiments
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    resolution: Optional[float] = Field(default=None, description="""Resolution in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'resolution', 'domain_of': ['QualityMetrics']} })
    resolution_high_shell_a: Optional[float] = Field(default=None, description="""High resolution shell limit in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'resolution_high_shell_a', 'domain_of': ['QualityMetrics']} })
    resolution_low_a: Optional[float] = Field(default=None, description="""Low resolution limit in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'resolution_low_a', 'domain_of': ['QualityMetrics']} })
    completeness: Optional[float] = Field(default=None, description="""Data completeness percentage""", json_schema_extra = { "linkml_meta": {'alias': 'completeness', 'domain_of': ['QualityMetrics']} })
    completeness_high_res_shell_percent: Optional[float] = Field(default=None, description="""Completeness in highest resolution shell""", json_schema_extra = { "linkml_meta": {'alias': 'completeness_high_res_shell_percent',
         'domain_of': ['QualityMetrics']} })
    signal_to_noise: Optional[float] = Field(default=None, description="""Signal to noise ratio""", json_schema_extra = { "linkml_meta": {'alias': 'signal_to_noise', 'domain_of': ['QualityMetrics']} })
    mean_i_over_sigma_i: Optional[float] = Field(default=None, description="""Mean I/sigma(I)""", json_schema_extra = { "linkml_meta": {'alias': 'mean_i_over_sigma_i', 'domain_of': ['QualityMetrics']} })
    space_group: Optional[str] = Field(default=None, description="""Crystallographic space group""", json_schema_extra = { "linkml_meta": {'alias': 'space_group', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    unit_cell_a: Optional[float] = Field(default=None, description="""Unit cell parameter a in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_a', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    unit_cell_b: Optional[float] = Field(default=None, description="""Unit cell parameter b in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_b', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    unit_cell_c: Optional[float] = Field(default=None, description="""Unit cell parameter c in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_c', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    unit_cell_alpha: Optional[float] = Field(default=None, description="""Unit cell angle alpha in degrees""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_alpha', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    unit_cell_beta: Optional[float] = Field(default=None, description="""Unit cell angle beta in degrees""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_beta', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    unit_cell_gamma: Optional[float] = Field(default=None, description="""Unit cell angle gamma in degrees""", json_schema_extra = { "linkml_meta": {'alias': 'unit_cell_gamma', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    multiplicity: Optional[float] = Field(default=None, description="""Data multiplicity (redundancy)""", json_schema_extra = { "linkml_meta": {'alias': 'multiplicity', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    cc_half: Optional[float] = Field(default=None, description="""Half-set correlation coefficient CC(1/2)""", json_schema_extra = { "linkml_meta": {'alias': 'cc_half', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    r_merge: Optional[float] = Field(default=None, description="""Rmerge - merge R-factor""", json_schema_extra = { "linkml_meta": {'alias': 'r_merge', 'domain_of': ['QualityMetrics']} })
    r_pim: Optional[float] = Field(default=None, description="""Rpim - precision-indicating merging R-factor""", json_schema_extra = { "linkml_meta": {'alias': 'r_pim', 'domain_of': ['QualityMetrics']} })
    wilson_b_factor_a2: Optional[float] = Field(default=None, description="""Wilson B-factor in Angstroms squared""", json_schema_extra = { "linkml_meta": {'alias': 'wilson_b_factor_a2', 'domain_of': ['QualityMetrics']} })
    anomalous_used: Optional[bool] = Field(default=None, description="""Whether anomalous signal was used""", json_schema_extra = { "linkml_meta": {'alias': 'anomalous_used', 'domain_of': ['QualityMetrics']} })
    anom_corr: Optional[float] = Field(default=None, description="""Anomalous correlation""", json_schema_extra = { "linkml_meta": {'alias': 'anom_corr', 'domain_of': ['QualityMetrics']} })
    anom_sig_ano: Optional[float] = Field(default=None, description="""Anomalous signal strength""", json_schema_extra = { "linkml_meta": {'alias': 'anom_sig_ano', 'domain_of': ['QualityMetrics']} })
    r_work: Optional[float] = Field(default=None, description="""Refinement R-factor (working set)""", json_schema_extra = { "linkml_meta": {'alias': 'r_work', 'domain_of': ['QualityMetrics']} })
    r_free: Optional[float] = Field(default=None, description="""R-free (test set)""", json_schema_extra = { "linkml_meta": {'alias': 'r_free', 'domain_of': ['QualityMetrics']} })
    ramachandran_favored_percent: Optional[float] = Field(default=None, description="""Percentage of residues in favored Ramachandran regions""", json_schema_extra = { "linkml_meta": {'alias': 'ramachandran_favored_percent', 'domain_of': ['QualityMetrics']} })
    ramachandran_outliers_percent: Optional[float] = Field(default=None, description="""Percentage of Ramachandran outliers""", json_schema_extra = { "linkml_meta": {'alias': 'ramachandran_outliers_percent', 'domain_of': ['QualityMetrics']} })
    clashscore: Optional[float] = Field(default=None, description="""MolProbity clashscore""", json_schema_extra = { "linkml_meta": {'alias': 'clashscore', 'domain_of': ['WorkflowRun', 'QualityMetrics']} })
    molprobity_score: Optional[float] = Field(default=None, description="""Overall MolProbity score""", json_schema_extra = { "linkml_meta": {'alias': 'molprobity_score', 'domain_of': ['QualityMetrics']} })
    average_b_factor_a2: Optional[float] = Field(default=None, description="""Average B-factor in Angstroms squared""", json_schema_extra = { "linkml_meta": {'alias': 'average_b_factor_a2', 'domain_of': ['QualityMetrics']} })
    i_zero: Optional[float] = Field(default=None, description="""Forward scattering intensity I(0)""", json_schema_extra = { "linkml_meta": {'alias': 'i_zero', 'domain_of': ['QualityMetrics']} })
    rg: Optional[float] = Field(default=None, description="""Radius of gyration in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'rg', 'domain_of': ['QualityMetrics']} })
    r_factor: Optional[float] = Field(default=None, description="""R-factor for crystallography (deprecated, use r_work)""", json_schema_extra = { "linkml_meta": {'alias': 'r_factor', 'domain_of': ['QualityMetrics']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class ComputeResources(AttributeGroup):
    """
    Computational resources used
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    cpu_hours: Optional[float] = Field(default=None, description="""CPU hours used""", json_schema_extra = { "linkml_meta": {'alias': 'cpu_hours', 'domain_of': ['ComputeResources']} })
    gpu_hours: Optional[float] = Field(default=None, description="""GPU hours used""", json_schema_extra = { "linkml_meta": {'alias': 'gpu_hours', 'domain_of': ['ComputeResources']} })
    memory_gb: Optional[float] = Field(default=None, description="""Maximum memory used in GB""", json_schema_extra = { "linkml_meta": {'alias': 'memory_gb', 'domain_of': ['ComputeResources']} })
    storage_gb: Optional[float] = Field(default=None, description="""Storage used in GB""", json_schema_extra = { "linkml_meta": {'alias': 'storage_gb', 'domain_of': ['ComputeResources']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class MotionCorrectionParameters(AttributeGroup):
    """
    Parameters specific to motion correction workflows
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    patch_size: Optional[int] = Field(default=None, description="""Patch size for local motion correction""", json_schema_extra = { "linkml_meta": {'alias': 'patch_size', 'domain_of': ['MotionCorrectionParameters']} })
    binning: Optional[int] = Field(default=None, description="""Binning factor applied during motion correction""", json_schema_extra = { "linkml_meta": {'alias': 'binning', 'domain_of': ['MotionCorrectionParameters']} })
    dose_weighting: Optional[bool] = Field(default=None, description="""Whether dose weighting was applied""", json_schema_extra = { "linkml_meta": {'alias': 'dose_weighting', 'domain_of': ['MotionCorrectionParameters']} })
    bfactor_dose_weighting: Optional[float] = Field(default=None, description="""B-factor for dose weighting""", json_schema_extra = { "linkml_meta": {'alias': 'bfactor_dose_weighting', 'domain_of': ['MotionCorrectionParameters']} })
    anisotropic_correction: Optional[bool] = Field(default=None, description="""Whether anisotropic motion correction was applied""", json_schema_extra = { "linkml_meta": {'alias': 'anisotropic_correction', 'domain_of': ['MotionCorrectionParameters']} })
    frame_grouping: Optional[int] = Field(default=None, description="""Number of frames grouped together""", json_schema_extra = { "linkml_meta": {'alias': 'frame_grouping', 'domain_of': ['MotionCorrectionParameters']} })
    output_binning: Optional[int] = Field(default=None, description="""Output binning factor""", json_schema_extra = { "linkml_meta": {'alias': 'output_binning', 'domain_of': ['MotionCorrectionParameters']} })
    drift_total: Optional[float] = Field(default=None, description="""Total drift in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'drift_total', 'domain_of': ['MotionCorrectionParameters']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class CTFEstimationParameters(AttributeGroup):
    """
    Parameters specific to CTF estimation workflows
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    defocus_search_min: Optional[float] = Field(default=None, description="""Minimum defocus search range in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_search_min', 'domain_of': ['CTFEstimationParameters']} })
    defocus_search_max: Optional[float] = Field(default=None, description="""Maximum defocus search range in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_search_max', 'domain_of': ['CTFEstimationParameters']} })
    defocus_step: Optional[float] = Field(default=None, description="""Defocus search step in micrometers""", json_schema_extra = { "linkml_meta": {'alias': 'defocus_step', 'domain_of': ['CTFEstimationParameters']} })
    amplitude_contrast: Optional[float] = Field(default=None, description="""Amplitude contrast value""", json_schema_extra = { "linkml_meta": {'alias': 'amplitude_contrast', 'domain_of': ['CTFEstimationParameters']} })
    cs_used_in_estimation: Optional[float] = Field(default=None, description="""Spherical aberration (Cs) value used during CTF estimation (in millimeters); may differ from instrument specification""", json_schema_extra = { "linkml_meta": {'alias': 'cs_used_in_estimation', 'domain_of': ['CTFEstimationParameters']} })
    voltage_used_in_estimation: Optional[float] = Field(default=None, description="""Accelerating voltage value used during CTF estimation (in kV); may differ from instrument specification""", json_schema_extra = { "linkml_meta": {'alias': 'voltage_used_in_estimation',
         'domain_of': ['CTFEstimationParameters']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class ParticlePickingParameters(AttributeGroup):
    """
    Parameters specific to particle picking workflows
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    picking_method: Optional[str] = Field(default=None, description="""Method used (manual, template_matching, deep_learning, LoG, Topaz, other)""", json_schema_extra = { "linkml_meta": {'alias': 'picking_method', 'domain_of': ['ParticlePickingParameters']} })
    box_size: Optional[int] = Field(default=None, description="""Particle box size in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'box_size',
         'domain_of': ['ParticlePickingParameters', 'RefinementParameters']} })
    threshold: Optional[float] = Field(default=None, description="""Picking threshold""", json_schema_extra = { "linkml_meta": {'alias': 'threshold', 'domain_of': ['ParticlePickingParameters']} })
    power_score: Optional[float] = Field(default=None, description="""Power score threshold""", json_schema_extra = { "linkml_meta": {'alias': 'power_score', 'domain_of': ['ParticlePickingParameters']} })
    ncc_score: Optional[float] = Field(default=None, description="""Normalized cross-correlation score threshold""", json_schema_extra = { "linkml_meta": {'alias': 'ncc_score', 'domain_of': ['ParticlePickingParameters']} })
    model_file: Optional[str] = Field(default=None, description="""Path to deep learning model file if used""", json_schema_extra = { "linkml_meta": {'alias': 'model_file', 'domain_of': ['ParticlePickingParameters']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class RefinementParameters(AttributeGroup):
    """
    Parameters specific to 3D refinement workflows
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    symmetry: Optional[SymmetryEnum] = Field(default=None, description="""Symmetry applied (C1, Cn, Dn, T, O, I)""", json_schema_extra = { "linkml_meta": {'alias': 'symmetry', 'domain_of': ['RefinementParameters']} })
    pixel_size: Optional[float] = Field(default=None, description="""Pixel size in Angstroms per pixel""", json_schema_extra = { "linkml_meta": {'alias': 'pixel_size', 'domain_of': ['Image', 'RefinementParameters']} })
    box_size: Optional[int] = Field(default=None, description="""Box size in pixels""", json_schema_extra = { "linkml_meta": {'alias': 'box_size',
         'domain_of': ['ParticlePickingParameters', 'RefinementParameters']} })
    gold_standard: Optional[bool] = Field(default=None, description="""Whether gold-standard refinement was used""", json_schema_extra = { "linkml_meta": {'alias': 'gold_standard', 'domain_of': ['RefinementParameters']} })
    split_strategy: Optional[str] = Field(default=None, description="""Strategy for data splitting""", json_schema_extra = { "linkml_meta": {'alias': 'split_strategy', 'domain_of': ['RefinementParameters']} })
    resolution_0_143: Optional[float] = Field(default=None, description="""Resolution at FSC=0.143 in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'resolution_0_143', 'domain_of': ['RefinementParameters']} })
    resolution_0_5: Optional[float] = Field(default=None, description="""Resolution at FSC=0.5 in Angstroms""", json_schema_extra = { "linkml_meta": {'alias': 'resolution_0_5', 'domain_of': ['RefinementParameters']} })
    map_sharpening_bfactor: Optional[float] = Field(default=None, description="""B-factor used for map sharpening in Angstroms^2""", json_schema_extra = { "linkml_meta": {'alias': 'map_sharpening_bfactor', 'domain_of': ['RefinementParameters']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


class FSCCurve(AttributeGroup):
    """
    Fourier Shell Correlation curve data.

    The `resolution_angstrom` and `fsc_value` arrays must be of equal length, with each value at index i in `resolution_angstrom`
    corresponding to the value at index i in `fsc_value`. Both arrays should not exceed 10,000 elements.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lambda-ber-schema/'})

    resolution_angstrom: Optional[list[float]] = Field(default=None, description="""Resolution values in Angstroms""", max_length=10000, json_schema_extra = { "linkml_meta": {'alias': 'resolution_angstrom', 'domain_of': ['FSCCurve']} })
    fsc_value: Optional[list[float]] = Field(default=None, description="""FSC values corresponding to each resolution""", max_length=10000, json_schema_extra = { "linkml_meta": {'alias': 'fsc_value', 'domain_of': ['FSCCurve']} })
    description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing', 'AttributeGroup']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
ProteinAnnotation.model_rebuild()
FunctionalSite.model_rebuild()
StructuralFeature.model_rebuild()
ProteinProteinInteraction.model_rebuild()
MutationEffect.model_rebuild()
ConformationalEnsemble.model_rebuild()
PostTranslationalModification.model_rebuild()
EvolutionaryConservation.model_rebuild()
AggregatedProteinView.model_rebuild()
MeasurementConditions.model_rebuild()
AttributeGroup.model_rebuild()
LigandInteraction.model_rebuild()
BiophysicalProperty.model_rebuild()
ConformationalState.model_rebuild()
DatabaseCrossReference.model_rebuild()
Dataset.model_rebuild()
Study.model_rebuild()
Sample.model_rebuild()
ProteinConstruct.model_rebuild()
SamplePreparation.model_rebuild()
Instrument.model_rebuild()
CryoEMInstrument.model_rebuild()
XRayInstrument.model_rebuild()
SAXSInstrument.model_rebuild()
ExperimentRun.model_rebuild()
WorkflowRun.model_rebuild()
DataFile.model_rebuild()
Image.model_rebuild()
Image2D.model_rebuild()
Image3D.model_rebuild()
Movie.model_rebuild()
Micrograph.model_rebuild()
FTIRImage.model_rebuild()
FluorescenceImage.model_rebuild()
OpticalImage.model_rebuild()
XRFImage.model_rebuild()
ImageFeature.model_rebuild()
OntologyTerm.model_rebuild()
MolecularComposition.model_rebuild()
BufferComposition.model_rebuild()
StorageConditions.model_rebuild()
TechniqueSpecificPreparation.model_rebuild()
CryoEMPreparation.model_rebuild()
CrystallizationConditions.model_rebuild()
XRayPreparation.model_rebuild()
SAXSPreparation.model_rebuild()
ExperimentalConditions.model_rebuild()
DataCollectionStrategy.model_rebuild()
QualityMetrics.model_rebuild()
ComputeResources.model_rebuild()
MotionCorrectionParameters.model_rebuild()
CTFEstimationParameters.model_rebuild()
ParticlePickingParameters.model_rebuild()
RefinementParameters.model_rebuild()
FSCCurve.model_rebuild()

