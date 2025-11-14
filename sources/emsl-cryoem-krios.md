DRAFT Metadata Schema Document for PNNL/EMSL’s Krios Cryo-EM Workflows

Points of contact: James Evans ([james.evans@pnnl.gov](mailto:james.evans@pnnl.gov)) and Trevor Moser ([trevor.moser@pnnl.gov](mailto:trevor.moser@pnnl.gov)) 

Last modified date: October 22, 2025

Below is a modular, provenance-aware metadata schema for cryo-EM workflows from sample preparation and raw data generation through image processing, map refinement, atomic modeling, and deposition to EMDB/PDB. It is organized into entities with stable identifiers, explicit data types, units, controlled vocabularies, and lineage links. It could be implemented in JSON, YAML, or a relational database; field names are given as dotted paths for clarity. The fields highlighted in green are already part of EMSL’s cryo-EM automated metadata capture in YAML format and yellow highlights represent metadata already available through user portal or other files with manual capture. All other fields required for deposition to EMPIAR/EMDB/PDB and generation of Table 1 metrics are captured manually elsewhere. All other fields are listed for completeness but may not be necessary for general reproduction. 

GENERAL SETUP

\- Every entity has: id (UUID), name, description, created\_at, modified\_at, created\_by (ORCID or name), software and version for generated outputs, inputs (references), outputs (references), parameters, files (with path, format, size, checksum).

\- Use SI units; key domain units included below. For arrays (e.g., FSC), store numeric arrays and unit metadata.

\- Use controlled vocabularies where noted; keep free-text fields for additional notes.

\- Capture provenance: each processing step links to the exact inputs and produces outputs with immutable checksums.

\- Suggested identifiers: project.id, sample.id, session.id, step.id, file.id, empiar\_id, emdb\_id, pdb\_id.

SCHEMA

1\) Project

\- project.id \[string\]: UUID.

\- project.title \[string\]

\- project.description \[string\]

\- project.pi \[string\]: name; project.pi\_orcid \[string\]

\- project.institution \[string\]

\- project.grant\_ids \[array\<string\>\]

\- project.keywords \[array\<string\>\]

\- project.links \[array\<string\>\]: DOIs, Git repos, lab notebooks.

2\) Sample

\- sample.id \[string\]

\- sample.name \[string\]

\- sample.type \[enum\]: protein, nucleic\_acid, complex, virus, organelle, membrane, other.

\- sample.organism \[string\], sample.taxid \[integer\]

\- sample.source \[enum\]: recombinant, purified native, synthetic, other.

\- sample.construct \[object\]:

  \- construct.components \[array\<object\>\] with fields: name, type, uniprot\_id, chain\_id\_hint, modifications (PTMs, tags), mutations (HGVS or free text)

\- sample.buffer \[object\]:

  \- buffer.components \[array\<object\>\]: name, concentration \[number, units\], pH \[number\], additives \[array\<string\>\]

\- sample.concentration \[number, mg/mL or µM\]: include units

\- sample.temperature \[number, °C\]

\- sample.notes \[string\]

3\) Grid and Vitrification

\- grid.id \[string\]

\- grid.support \[string\]: e.g., Quantifoil R1.2/1.3, UltrAufoil; grid.material \[enum\]: carbon, gold, graphene, silicon nitride.

\- grid.treatment \[object\]: glow\_discharge \[boolean\], time \[s\], current \[mA\], atmosphere \[air, amylamine\], pressure \[mbar\]

\- vitrification.method \[enum\]: plunge\_freezing, spray\_vitrification, blot-free (Spotiton/IceFire), other

\- vitrification.instrument \[string\]: e.g., Vitrobot

\- vitrification.params \[object\]:

  \- blot\_time \[number, s\]

  \- blot\_force \[number, arbitrary units\]

  \- blot\_number \[integer\]

  \- wait\_time \[number, s\]

  \- humidity \[number, %\]

  \- temperature \[number, °C\]

  \-blotter\_height \[number\]

  \-blotter\_setting \[number\]

  \- sample\_applied\_volume \[number, µL\]

  \- ethane\_temp \[number, °C\]

\- grid.notes \[string\]

4\) Instrumentation

\- instrument.id \[string\]

\- microscope.make \[string\], microscope.model \[string\]

\- microscope.acceleration\_voltage \[number, kV\]

\- microscope.cs \[number, mm\]

\- microscope.c2\_aperture \[number, µm\], objective\_aperture \[number, µm\]

\- microscope.phase\_plate \[boolean\], phase\_plate\_type \[string\]

\- energy\_filter.present \[boolean\], energy\_filter.make \[string\], model \[string\], slit\_width \[number, eV\]

\- detector.make \[string\], detector.model \[string\], detector.position \[string\]

\- detector.mode \[enum\]: counting, integrating, super\_resolution

\- detector.pixel\_size\_physical \[number, µm\]

\- microscope.software \[string\]: e.g., SerialEM, EPU, Leginon; version \[string\]

\-microscope.spotsize \[number\]

\-microscope.gunlens \[number\]

\-microscope.imaging\_mode \[string\] e.g., EFTEM, TEM, STEM

\-microscope.TEM\_beam\_diameter \[number, microns\]

5\) Acquisition Session

\- session.id \[string\]

\- session.date \[datetime\]

\- operator.name \[string\], operator.orcid \[string\]

\- session.software \[string\], version \[string\]

\- session.magnification \[number, x\]

\- session.calibrated\_pixel\_size \[number, Å/pixel\]

\- session.camera\_binning \[integer\]

\- session.exposure\_time\_per\_frame \[number, ms\]

\- session.frames\_per\_movie \[integer\]

\- session.total\_exposure\_time \[number, ms\]

\- session.total\_dose \[number, e-/Å^2\]

\- session.dose\_rate \[number, e-/pixel/s or e-/Å^2/s\]

\- session.defocus\_target \[number, µm\], defocus\_range \[object\]: min \[µm\], max \[µm\], inc \[um\]

\- session.astigmatism\_target \[number, nm\]

\- session.coma \[number, nm\]

\- session.stage\_tilt \[number, degrees\]

\- session.autoloader\_slot \[string\]

\- session.notes \[string\]

\-session.shots\_per\_hole \[num\]

\-session.holes\_per\_group \[num\]

6\) Raw Data

\- raw\_data.empiar\_id \[string\] (when available)

\- movies \[array\<object\>\] each movie:

  \- movie.id \[string\]

  \- file.path \[string\], file.format \[enum\]: MRC, TIFF, EER, other

  \- file.size \[number, bytes\], file.checksum \[string, SHA256\]

  \- movie.frames \[integer\]

  \- movie.super\_resolution \[boolean\]

  \- movie.pixel\_size\_unbinned \[number, Å/pixel\]

  \- movie.timestamp \[datetime\]

  \- movie.stage\_position \[object\]: x \[µm\], y \[µm\], z \[µm\]

  \- movie.nominal\_defocus \[number, µm\]

  \- movie.dose\_per\_frame \[number, e-/Å^2\]

  \- movie.beam\_shift \[object\]: x \[µrad\], y \[µrad\]

  \- movie.ice\_thickness\_estimate \[number, nm\] (if available)

  \- movie.grid\_square\_id \[string\], hole\_id \[string\]

  \- movie.acquisition\_group \[string\] (e.g., template or area)

\- micrographs \[array\<object\>\] (if saved separately):

  \- micrograph.id \[string\]

  \- file.path, format, size, checksum

  \- pixel\_size \[number, Å/pixel\]

  \- defocus \[number, µm\]

  \- dose \[number, e-/Å^2\]

  \- origin\_movie\_id \[string\]

7\) Preprocessing

7a) Motion Correction step

\- motion\_correction.id \[string\]

\- inputs.movies \[array\<movie.id\>\]

\- software.name \[string\]: e.g., MotionCor2, Warp; version \[string\]

\- parameters:

  \- patch\_size \[integer\]

  \- binning \[integer\]

  \- dose\_weighting \[boolean\]

  \- bfactor\_dose\_weighting \[number\]

  \- anisotropic\_correction \[boolean\]

  \-frame\_grouping \[number\]

  \-outputs.binning \[number\]

\- outputs.aligned\_micrographs \[array\<object\>\]: file.path, format (MRC), checksum

\- outputs.frame\_sums \[array\<object\>\]: with and without dose-weighting

\- outputs.shift\_traces \[array\<object\>\]: per frame shifts

\- metrics:

  \- drift\_total \[number, Å\]

  \- outlier\_frames \[array\<integer\>\]

  \- motion\_plot\_file \[string\]

7b) CTF Estimation step

\- ctf\_estimation.id \[string\]

\- inputs.micrographs \[array\<micrograph.id\>\]

\- software.name \[string\]: CTFFIND4, Gctf, Warp; version \[string\]

\- parameters:

  \- defocus\_search\_range \[object\]: min \[µm\], max \[µm\]

  \- step \[number, µm\]

  \- amplitude\_contrast \[number\]

  \- cs \[number, mm\]

  \- voltage \[number, kV\]

\- outputs.ctf\_tables \[file.path, format: STAR/CSV/JSON, checksum\]

\- per\_micrograph\_ctf \[array\<object\>\]:

  \- micrograph\_id

  \- defocus\_u \[number, µm\]

  \- defocus\_v \[number, µm\]

  \- astigmatism \[number, Å\]

  \- angle \[number, degrees\]

  \- resolution\_fit\_limit \[number, Å\]

  \- quality\_score \[number\]

\- diagnostics \[file.path\]: Thon ring fits, power spectra

8\) Particle Picking

\- particle\_picking.id \[string\]

\- inputs.micrographs \[array\<micrograph.id\>\]

\- method \[enum\]: manual, template\_matching, deep\_learning, LoG, Topaz, other

\- software.name \[string\]; version \[string\]

\- parameters:

  \- box\_size \[integer, pixels\]

  \- threshold \[number\]

  \-power\_score \[number\]

  \-NCC\_score \[number\]

  \- template\_ids \[array\<string\>\] (if template-based)

  \- model\_file \[string\] (if DL)

\- outputs.particle\_coordinates \[file.path, format: STAR/CSV/CS, checksum\]

\- metrics:

  \- picks\_per\_micrograph \[array\<object\>\]: micrograph\_id, count

  \- false\_positive\_estimate \[number\]

  \- picker\_confidence\_stats \[object\]

9\) Particle Extraction

\- particle\_extraction.id \[string\]

\- inputs.particle\_coordinates \[file.path\]

\- inputs.aligned\_micrographs \[array\<micrograph.id\>\]

\- parameters:

  \- box\_size \[integer, pixels\]

  \- binning \[integer\]

  \- normalization \[enum\]: none, mean-std, robust

\- outputs.particle\_stacks \[array\<object\>\]: file.path (MRCS/CS/HDF5), checksum, count

\- outputs.meta \[file.path\]: STAR/CS/JSON

\- metrics: total\_particles \[integer\]

10\) 2D Classification

\- classification\_2d.id \[string\]

\- inputs.particle\_stacks \[array\<file\>\]

\- software.name \[string\]: RELION, cryoSPARC, EMAN2, cisTEM; version \[string\]

\- parameters:

  \- number\_of\_classes \[integer\]

  \- mask\_diameter \[number, Å\]

  \- iterations \[integer\]

  \- angular\_sampling \[number, degrees\]

\- outputs.class\_averages \[array\<file\>\]

\- outputs.assignments \[file.path\]

\- metrics:

  \- particles\_kept \[integer\]

  \- class\_distribution \[array\<object\>\]: class\_id, count

  \- SNR\_per\_class \[array\<number\>\]

11\) Ab Initio / Initial Model

\- ab\_initio.id \[string\]

\- inputs.filtered\_particles \[file\]

\- software.name; version

\- parameters:

  \- symmetry \[enum\]: C1, Cn, Dn, T, O, I

  \- number\_of\_models \[integer\]

\- outputs.initial\_volumes \[array\<file\>\]: MRC

\- metrics: map\_resolution\_estimate \[number, Å\]

12\) 3D Classification

\- classification\_3d.id \[string\]

\- inputs.particles \[file\], initial\_model \[file\]

\- software.name; version

\- parameters:

  \- number\_of\_classes \[integer\]

  \- symmetry \[enum\]

  \- angular\_sampling \[number, degrees\]

  \- solvent\_mask \[file\] (optional)

\- outputs.class\_volumes \[array\<file\>\]

\- outputs.class\_assignments \[file\]

\- metrics: class\_counts, heterogeneity\_notes \[string\]

13\) 3D Refinement

\- refinement\_3d.id \[string\]

\- inputs.particles \[file\], initial\_model \[file\]

\- software.name; version

\- parameters:

  \- symmetry \[enum\]

  \- pixel\_size \[number, Å/pixel\]

  \- box\_size \[integer, pixels\]

  \- gold\_standard \[boolean\], split\_strategy \[string\]

  \- optics\_groups \[array\<object\>\]

\- outputs.refined\_map\_half1 \[file\], refined\_map\_half2 \[file\], refined\_map\_full \[file\]

\- outputs.refined\_parameters \[file\]: orientations, shifts

\- metrics:

  \- FSC\_curve \[array\<object\>\]: resolution \[Å\], FSC \[number\]

  \- resolution\_0\_143 \[number, Å\]

  \- resolution\_0\_5 \[number, Å\]

  \- map\_sharpening\_bfactor \[number, Å^2\] (if auto-estimated)

14\) Post-processing / Map Polishing

\- postprocessing.id \[string\]

\- inputs.refined\_map\_half1/half2 \[files\], solvent\_mask \[file\]

\- software.name; version: e.g., RELION postprocess, Phenix, LocalDeblur

\- parameters:

  \- mask\_applied \[file\]

  \- sharpening \[enum\]: bfactor, autosharpen, none

  \- bfactor\_applied \[number, Å^2\]

  \- lowpass/highpass\_filters \[number, Å\]

  \- map\_norm\_method \[string\]

\- outputs.final\_map \[file.path, format: MRC/CCP4\]

\- outputs.local\_resolution\_map \[file\] (optional)

\- metrics:

  \- FSC\_gold\_standard \[array\<object\>\]

  \- map\_mean\_std \[object\]

  \- estimated\_B\_iso \[number, Å^2\]

15\) Map Validation

\- map\_validation.id \[string\]

\- inputs.final\_map \[file\], mask \[file\]

\- software.name; version: e.g., 3DFSC, ResMap, MonoRes

\- metrics:

  \- directional\_FSC \[object\]: file.path

  \- sphericity \[number\]

  \- local\_resolution\_stats \[object\]: min/max/median \[Å\]

  \- map\_symmetry \[enum\], enforced\_symmetry \[enum\]

  \- map\_contour\_level \[number\] (relative to RMS)

\- notes \[string\]

16\) Atomic Modeling (Build)

\- model\_building.id \[string\]

\- inputs.final\_map \[file\], sequence(s) \[file\], initial\_model \[file\] (if any)

\- software.name; version: e.g., Coot, Phenix, Rosetta, ISOLDE, ModelAngelo

\- parameters:

  \- map\_weight \[number\]

  \- restraints \[object\]: geometry, secondary structure, symmetry

\- outputs.model\_initial \[file.path, format: PDB/mmCIF\]

\- outputs.segmentation \[file\] (if used)

\- notes \[string\]

17\) Model Refinement

\- model\_refinement.id \[string\]

\- inputs.model\_initial \[file\], final\_map \[file\]

\- software.name; version: e.g., Phenix real-space refine, Refmac

\- parameters:

  \- refinement\_strategy \[enum\]: rigid\_body, real\_space, morph, B-factor

  \- resolution\_limit \[number, Å\]

  \- geometry\_weight \[number\]

  \- map\_sharpening\_used \[boolean\]

\- outputs.model\_final \[file.path, PDB/mmCIF\]

\- outputs.bfactor\_map \[file\] (optional)

\- metrics:

  \- model\_map\_cc \[number\]

  \- EMRinger\_score \[number\]

  \- MolProbity\_score \[number\]

  \- clashscore \[number\]

  \- Ramachandran \[object\]: favored \[%\], allowed \[%\], outliers \[%\]

  \- rotamer\_outliers \[%\]

  \- Cα RMSD to initial \[number, Å\]

18\) Model Validation

\- model\_validation.id \[string\]

\- inputs.model\_final \[file\], final\_map \[file\]

\- software.name; version: e.g., Phenix validation, TEMPy, CaBLAM

\- metrics:

  \- map\_vs\_model\_FSC \[array\<object\>\]

  \- per-chain CC \[array\<object\>\]: chain\_id, CC

  \- geometry\_summary \[object\]

  \- ligand\_validation \[object\]

\- notes \[string\]

19\) Deposition

\- deposition.id \[string\]

\- empiar \[object\]:

  \- empiar\_id \[string\]

  \- datasets \[array\<object\>\]: raw\_movies \[file lists\], aligned\_micrographs \[file lists\], metadata\_files \[file lists\]

  \- embargo\_date \[datetime\]

\- emdb \[object\]:

  \- emdb\_id \[string\]

  \- map\_file \[file.path\], format \[MRC/CCP4\], checksum

  \- sampling\_rate \[number, Å/pixel\]

  \- map\_dimensions \[object\]: nx, ny, nz \[integer\]

  \- origin \[object\]: x, y, z \[Å\]

  \- contour\_level \[number\]

  \- resolution\_method \[enum\]: FSC\_0.143, FSC\_0.5, others

  \- reported\_resolution \[number, Å\]

  \- symmetry \[enum\]

  \- experiment\_type \[enum\]: single\_particle, tomography\_subvolume, helical, other

  \- processing\_software \[array\<object\>\]: name, version

  \- validation\_reports \[array\<file\>\]

  \- sample\_description \[object\] link: sample.id

\- pdb \[object\]:

  \- pdb\_id \[string\]

  \- model\_file \[file.path, mmCIF\], checksum

  \- associated\_emdb\_id \[string\]

  \- polymer\_entities \[array\<object\>\]: chain\_id, uniprot\_id, sequence\_md5

  \- ligands \[array\<object\>\]: id, smiles/inchi, restraints\_file

  \- model\_vs\_map\_metrics \[object\]: CC, FSC

  \- validation\_report \[file.path\]

\- deposition.contacts \[array\<object\>\]: name, email, ORCID

\- deposition.citations \[array\<object\>\]: doi, title, authors, journal, year

20\) Files and Storage

\- file.id \[string\]

\- file.path \[string\]

\- file.storage\_uri \[string\] (S3/Globus)

\- file.format \[enum\]: MRC, MRCS, CS, STAR, TIFF, EER, JSON, CSV, mmCIF, PDB, PDF

\- file.size \[number, bytes\]

\- file.checksum \[string, SHA256\]

\- file.created\_at \[datetime\]

\- file.related\_entity \[string\]: id of owner (movie/micrograph/map/model)

\- file.role \[enum\]: raw, intermediate, final, diagnostic, metadata

21\) Provenance and Lineage

\- provenance.graph \[array\<object\>\]: edges linking step.id \-\> outputs.file.id, and outputs.file.id \-\> next step inputs

\- provenance.environment \[object\]: compute\_node, GPU model/count, CPU, RAM, OS, container image digest

\- provenance.random\_seeds \[object\]: per software step for reproducibility

\- provenance.logs \[array\<file\>\]

22\) Quality Control Summary

\- qc.id \[string\]

\- qc.raw\_data \[object\]: number\_of\_movies, rejected\_movies \[count\], reason\_distribution

\- qc.preprocess \[object\]: micrographs\_kept, ctf\_quality\_stats

\- qc.particles \[object\]: total\_picks, filtered\_counts

\- qc.map \[object\]: resolution\_0\_143 \[Å\], anisotropy\_sphericity, local\_res\_min/median/max \[Å\]

\- qc.model \[object\]: MolProbity, EMRinger, CC, outliers

\- qc.notes \[string\]

GENERAL NOTES

Controlled vocabularies and units

\- symmetry: C1, Cn (n integer), Dn, T, O, I

\- detector.mode: counting, integrating, super\_resolution

\- experiment\_type: single\_particle, tomography\_subvolume, helical, other (MicroED workflow would need separate workflow to capture diffraction settings, phasing and other parameter space)

\- file.format: MRC, MRCS, CCP4, CS, STAR, TIFF, EER, HDF5, JSON, CSV, mmCIF, PDB, PDF

\- Units: Å, Å^2, µm, nm, kV, eV, ms, s, degrees, e-/Å^2, pixels.

Crosswalk to EMPIAR, EMDB, PDB

\- EMPIAR requires: raw data description, microscope/detector details, acquisition settings (voltage, magnification/pixel size, dose, defocus), grid/sample description, file inventory with checksums. Mapped to: instrumentation.\*, session.\*, sample.\*, grid.\*, raw\_data.\*, files.\*.

\- EMDB requires: final map file and sampling, resolution and method, symmetry, processing software, experiment type, sample description, contour level. Mapped to: postprocessing.outputs.final\_map, refinement\_3d.metrics.\*, postprocessing.parameters.\*, deposition.emdb.\*, sample.\*, instrumentation.\*, processing steps software/parameters.

\- PDB (mmCIF) requires: final coordinates, polymer/lipid/ligand entities, links to EMDB map, model validation metrics, assembly/bio-unit info. Mapped to: model\_refinement.outputs.model\_final, model\_validation.metrics.\*, deposition.pdb.\*, sample.construct.\*, symmetry (assembly), EMDB link.

Minimal required fields to ensure reproducibility

\- Instrumentation: microscope.model, acceleration\_voltage, cs, energy\_filter (presence and slit), detector.model, detector.mode.

\- Acquisition: calibrated\_pixel\_size, magnification or optics calibration info, defocus\_range, total\_dose, frames\_per\_movie, exposure\_time\_per\_frame.

\- Preprocessing: software names/versions, motion correction parameters; CTF parameters and results per micrograph.

\- Processing: particle picking method and parameters, extraction box size/binning; 2D/3D class counts, symmetry; refinement strategy (gold-standard), pixel size, box size.

\- Map: final map file and FSC curve with reported resolution; mask used; sharpening parameters.

\- Model: sequence sources, software and parameters for building/refinement; model-map fit metrics; validation scores.

\- Deposition: EMPIAR dataset details, EMDB map info, PDB mmCIF and validation report.

