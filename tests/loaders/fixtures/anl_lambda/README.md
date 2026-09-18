# ANL LAMBDA fixtures

Hand-built responses in the shape the LAMBDA API (https://sg.bio.anl.gov/lambda) serves:
the `V_LAM_XTA` collapse for one MX experiment, its image set and frame listings, two
pages of the experiment index, and the `V_LAM_LIMS` export with its integer enums,
explicit nulls and nested organism object.

The values are not a capture. The MX summary records are marked `is_public: false`, so
only facts that are public elsewhere are kept (PDB 5DU2 and its UniProt entry, the
beamline, the PI on the deposition); sequences are truncated, primers and vector
sequences are placeholders, and the LIMS rows are invented to exercise every repair the
loader makes (stuck organism id, sequence in `mutations`, one accession on two samples
with different sequences, a sample without a UniProt cross-reference, a repeated
workflow row, a litre figure that is millilitres).
