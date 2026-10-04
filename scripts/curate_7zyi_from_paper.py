"""
Build the curated 7ZYI example: the PDB loader's output plus what Liu et al. 2022 adds, schema unchanged.

Run from the repository root after regenerating Dataset-pdb-7ZYI-NTCP-fab-nanobody.yaml:

    uv run python scripts/curate_7zyi_from_paper.py
"""
import yaml
SRC = 'tests/data/valid/Dataset-pdb-7ZYI-NTCP-fab-nanobody.yaml'
OUT = 'tests/data/valid/Dataset-pdb-7ZYI-NTCP-curated-from-paper.yaml'
d = yaml.safe_load(open(SRC))
PAPER = "Liu et al. 2022, Cell Res 32:773 (doi:10.1038/s41422-022-00680-4)"
def cite(text, where):
    return f"{text} [{PAPER}, {where}]"

d['id'] = 'lambdaber:pdb-7ZYI-curated'
d['title'] = 'Human NTCP with Fab, nanobody and bile salt: PDB 7ZYI curated against its primary publication'
d['description'] = ("The PDB loader's output for 7ZYI with the facts its primary publication adds, written in "
    "the schema as it stands. Rows and values taken from the paper say so in their description; "
    "see docs/examples/pdb-7zyi-ntcp-case-study.md.")

comp = {c['id']: c for c in d['sample_components']}
S = 'pdb:7ZYI/sample'
NTCP, HC, LC, NB, CLR, GCDC, NA = (f'pdb:7ZYI/component/{i}' for i in range(1, 8))

# Roles: NTCP is the target; Fab and nanobody are there to make the particle tractable
comp[NTCP]['role'] = 'target'
for c in (HC, LC, NB):
    comp[c]['role'] = 'chaperone'
comp[HC]['description'] = cite("Heavy chain of NTCP_Fab12, a synthetic Fab raised against NTCP's external face; adds mass and a rigid feature for particle alignment", "main text, Fig. 1c")
comp[LC]['description'] = cite("Light chain of NTCP_Fab12", "Fig. 1c")
comp[NB]['description'] = cite("Fab-binding nanobody, bound to the Fab rather than to NTCP", "main text")
for a in d['sample_protein_associations']:
    a['role'] = 'target' if a['protein_id'] == 'uniprot:Q14973' else 'chaperone'

# GCDC was added to the grids as the substrate, at 100 uM
comp[GCDC]['role'] = 'substrate'
comp[GCDC]['concentration'] = {'numeric_value': 100, 'unit': 'micromolar'}
comp[GCDC]['description'] = cite("Glycochenodeoxycholic acid, a bile salt substrate of NTCP, present at 100 uM, about 170 times its reported K_M", "main text")

# Constituents the PDB entry does not list
d['small_molecules'].append({
    'id': 'CHEBI:138742', 'title': 'CHOLESTEROL HEMISUCCINATE', 'small_molecule_name': 'cholesteryl hemisuccinate',
    'chebi_id': 'CHEBI:138742', 'pdb_ligand_id': 'pdb.ligand:Y01', 'chemical_class': 'lipid',
    'molecular_formula': 'C31H50O4', 'inchikey': 'WLNARFZDISHUGS-MIXBDBMTSA-N',
})
d['sample_components'] += [
    {'id': 'pdb:7ZYI/component/nanodisc', 'sample_id': S, 'component_type': 'membrane_mimetic',
     'title': 'lipid nanodisc', 'role': 'carrier',
     'description': cite("NTCP was purified in detergent and reconstituted into lipid nanodiscs; scaffold and lipids are given only in the supplement", "main text, Supplementary Fig. S1")},
    {'id': 'pdb:7ZYI/component/chs', 'sample_id': S, 'component_type': 'small_molecule',
     'small_molecule_id': 'CHEBI:138742', 'role': 'additive',
     'description': cite("Present during NTCP purification and nanodisc reconstitution", "main text")},
]

def interaction(subject, obj, itype, status, description, **extra):
    row = {'sample_id': S, 'subject_id': subject, 'object_id': obj, 'interaction_type': itype,
           'interaction_status': status, 'evidence': ['experimental'], 'description': description}
    row.update(extra)
    return row

inter = d['sample_component_interactions']
# The loader writes one row per sodium and per bile salt copy, with the residues the deposited
# model puts in contact or in coordination. The paper names the sites; it also lists one more
# residue per sodium site than the deposited coordination bonds do. Both are kept: the PDB's
# residues in object_site, the paper's reading in the description.
paper_na = {"Q68,G97,S99,Q261": ("Na2", "Q68,G97,C98,S99,Q261"), "S105,S119,T123,E257": ("Na1", "S105,N106,S119,T123,E257")}
for i in inter:
    if i['subject_id'] == NA and i.get('object_site') in paper_na:
        site, residues = paper_na[i['object_site']]
        i['description'] = i['description'] + "; " + cite(
            f"site {site}, between TM3 and TM8; the paper lists {residues}, contacts from side chains and main-chain carbonyls",
            "Fig. 1e, i")
    if i['subject_id'] == GCDC:
        i['description'] = i['description'] + "; " + cite(
            "one of the two bile salts in the tunnel, at S_out or S_in (the deposition does not say which copy is which), "
            "clamped between TM1, TM3b, TM6 and TM9; density also compatible with cholesterol or CHS, assigned to GCDC "
            "because of its concentration and because GCDC, unlike CHS, inhibits transport", "Fig. 1d, f-h")
inter += [
    interaction(GCDC, NTCP, 'is_substrate_of', 'expected',
        "GCDC is a bona fide NTCP substrate with K_M about 0.6 uM, reported by Jani et al. 2018 (Toxicol In Vitro 46:189) and cited by the paper",
        affinity={'numeric_value': 0.6, 'unit': 'micromolar'}, affinity_type='km'),
    interaction(GCDC, NTCP, 'inhibits', 'observed',
        cite("100 uM GCDC reduced Na+-driven uptake of radiolabelled taurocholate into HEK293 cells by about 80%", "Fig. 1b")),
    interaction('pdb:7ZYI/component/chs', NTCP, 'inhibits', 'not_observed',
        cite("100 uM CHS did not inhibit taurocholate uptake", "Fig. 1b")),
    interaction(HC, NTCP, 'binds', 'observed',
        cite("NTCP_Fab12 binds the external surface of NTCP with an apparent K_d of 60 nM", "Supplementary Fig. S2"),
        affinity={'numeric_value': 60, 'unit': 'nanomolar'}, affinity_type='kd'),
    interaction(HC, NTCP, 'inhibits', 'not_observed',
        cite("0.75 uM NTCP_Fab12, 12 times its apparent K_d, did not reduce taurocholate uptake, so the Fab is taken to capture a functional state", "Fig. 1b")),
]

# Preparation the paper describes and the PDB does not
d['sample_preparations'].append({
    'id': 'pdb:7ZYI/preparation/purification-ntcp', 'preparation_type': 'protein_purification', 'sample_id': S,
    'title': 'Purification and nanodisc reconstitution of NTCP',
    'protocol_description': cite("Wild-type full-length human NTCP expressed in HEK293 cells, purified in detergent and reconstituted into lipid nanodiscs; NTCP_Fab12 selected from a synthetic library", "main text, Supplementary Figs. S1, S2"),
})

# People: full names, affiliations and the corresponding author come from the paper
full = ["Hongtao Liu", "Rossitza N. Irobalieva", "Rose Bang-Sørensen", "Kamil Nosol", "Somnath Mukherjee",
        "Parth Agrawal", "Bruno Stieger", "Anthony A. Kossiakoff", "Kaspar P. Locher"]
persons = {p['id']: p for p in d['persons']}
for a in d['study_person_associations']:
    p = persons[a['person_id']]
    p['full_name'] = full[a['author_position'] - 1]
    p['title'] = p['full_name']
    if a['author_position'] == 9:
        a['corresponding'] = True
orgs = [
    ('pdb:organization/eth-zurich-imbb', 'Institute of Molecular Biology and Biophysics, ETH Zürich', 'university', [1, 2, 3, 4, 9]),
    ('pdb:organization/uchicago-bmb', 'Department of Biochemistry and Molecular Biology, University of Chicago', 'university', [5, 6, 8]),
    ('pdb:organization/usz-clinical-pharmacology', 'Department of Clinical Pharmacology and Toxicology, University Hospital Zürich, University of Zürich', 'hospital', [7]),
]
d.setdefault('person_organization_associations', [])
by_pos = {a['author_position']: a['person_id'] for a in d['study_person_associations']}
for oid, name, kind, members in orgs:
    d['organizations'].append({'id': oid, 'title': name, 'organization_type': kind})
    for m in members:
        d['person_organization_associations'].append({'person_id': by_pos[m], 'organization_id': oid, 'role': 'primary_affiliation'})
d['organizations'].append({'id': 'pdb:organization/scopem-eth-zurich', 'title': 'ScopeM, ETH Zürich',
    'organization_type': 'research_institute', 'description': cite("Cryo-EM data were collected at ScopeM", "Acknowledgements")})
d['study_organization_associations'].append({'study_id': 'pdb:7ZYI/study', 'organization_id': 'pdb:organization/scopem-eth-zurich', 'role': 'operating_institution'})
# Funding: the PDB names SNSF only; the paper gives its award and a second funder
for a in d['study_organization_associations']:
    if a['organization_id'] == 'pdb:organization/swiss-national-science-foundation':
        a['award_number'] = '310030_189111'
d['organizations'].append({'id': 'pdb:organization/national-institutes-of-health', 'title': 'National Institutes of Health',
    'organization_type': 'funding_agency', 'country': 'United States',
    'description': cite("Listed in the paper's acknowledgements, not in the PDB entry", "Acknowledgements")})
d['study_organization_associations'].append({'study_id': 'pdb:7ZYI/study', 'organization_id': 'pdb:organization/national-institutes-of-health', 'role': 'funder', 'award_number': 'GM117372'})

# Study: what the paper is about, kept to statements the paper makes
study = d['studies'][0]
study['description'] = cite(
    "Cryo-EM structure of human NTCP (SLC10A1), the liver's sodium-taurocholate co-transporting polypeptide and the receptor for hepatitis B and D viruses, "
    "bound to a non-inhibitory Fab, a Fab-binding nanobody and the substrate GCDC. The authors locate two bile salt sites (S_out, S_in) in a tunnel open to the outer membrane leaflet "
    "and two sodium sites (Na1, Na2), and propose a 2 Na+ : 1 bile salt transport mechanism in which a bile salt shuttles from S_out to S_in", "abstract-level summary")
study['keywords'] = study['keywords'] + ['bile acid:sodium symporter activity', 'GO:0008508']

yaml.safe_dump(d, open(OUT, 'w'), sort_keys=False, allow_unicode=True, width=120)
print('wrote', OUT)
