
# Class: Sample

A biological sample used in structural biology experiments

URI: [lambdaber:Sample](https://w3id.org/lambda-ber-schema/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StructuralFeature],[StorageConditions],[DatabaseCrossReference]<database_cross_references%200..*-++[Sample&#124;sample_code:string;sample_type:SampleTypeEnum;molecular_weight:float%20%3F;concentration:float%20%3F;concentration_unit:ConcentrationUnitEnum%20%3F;preparation_method:string%20%3F;purity_percentage:float%20%3F;quality_metrics:string%20%3F;protein_name:string%20%3F;construct:string%20%3F;tag:string%20%3F;mutations:string%20%3F;expression_system:string%20%3F;ligand:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[ConformationalEnsemble]<conformational_ensemble%200..1-++[Sample],[EvolutionaryConservation]<evolutionary_conservation%200..1-++[Sample],[BiophysicalProperty]<biophysical_properties%200..*-++[Sample],[PostTranslationalModification]<ptm_annotations%200..*-++[Sample],[MutationEffect]<mutation_effects%200..*-++[Sample],[LigandInteraction]<ligand_interactions%200..*-++[Sample],[ProteinProteinInteraction]<protein_interactions%200..*-++[Sample],[StructuralFeature]<structural_features%200..*-++[Sample],[FunctionalSite]<functional_sites%200..*-++[Sample],[Sample]<parent_sample_id%200..1-%20[Sample],[OntologyTerm]<cell_type%200..1-%20[Sample],[OntologyTerm]<anatomy%200..1-%20[Sample],[OntologyTerm]<organism%200..1-%20[Sample],[StorageConditions]<storage_conditions%200..1-++[Sample],[BufferComposition]<buffer_composition%200..1-++[Sample],[MolecularComposition]<molecular_composition%200..1-++[Sample],[Study]++-%20samples%200..*>[Sample],[NamedThing]^-[Sample],[Study],[ProteinProteinInteraction],[PostTranslationalModification],[OntologyTerm],[NamedThing],[MutationEffect],[MolecularComposition],[LigandInteraction],[FunctionalSite],[EvolutionaryConservation],[DatabaseCrossReference],[ConformationalEnsemble],[BufferComposition],[BiophysicalProperty])](https://yuml.me/diagram/nofunky;dir:TB/class/[StructuralFeature],[StorageConditions],[DatabaseCrossReference]<database_cross_references%200..*-++[Sample&#124;sample_code:string;sample_type:SampleTypeEnum;molecular_weight:float%20%3F;concentration:float%20%3F;concentration_unit:ConcentrationUnitEnum%20%3F;preparation_method:string%20%3F;purity_percentage:float%20%3F;quality_metrics:string%20%3F;protein_name:string%20%3F;construct:string%20%3F;tag:string%20%3F;mutations:string%20%3F;expression_system:string%20%3F;ligand:string%20%3F;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[ConformationalEnsemble]<conformational_ensemble%200..1-++[Sample],[EvolutionaryConservation]<evolutionary_conservation%200..1-++[Sample],[BiophysicalProperty]<biophysical_properties%200..*-++[Sample],[PostTranslationalModification]<ptm_annotations%200..*-++[Sample],[MutationEffect]<mutation_effects%200..*-++[Sample],[LigandInteraction]<ligand_interactions%200..*-++[Sample],[ProteinProteinInteraction]<protein_interactions%200..*-++[Sample],[StructuralFeature]<structural_features%200..*-++[Sample],[FunctionalSite]<functional_sites%200..*-++[Sample],[Sample]<parent_sample_id%200..1-%20[Sample],[OntologyTerm]<cell_type%200..1-%20[Sample],[OntologyTerm]<anatomy%200..1-%20[Sample],[OntologyTerm]<organism%200..1-%20[Sample],[StorageConditions]<storage_conditions%200..1-++[Sample],[BufferComposition]<buffer_composition%200..1-++[Sample],[MolecularComposition]<molecular_composition%200..1-++[Sample],[Study]++-%20samples%200..*>[Sample],[NamedThing]^-[Sample],[Study],[ProteinProteinInteraction],[PostTranslationalModification],[OntologyTerm],[NamedThing],[MutationEffect],[MolecularComposition],[LigandInteraction],[FunctionalSite],[EvolutionaryConservation],[DatabaseCrossReference],[ConformationalEnsemble],[BufferComposition],[BiophysicalProperty])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞parent_sample_id](sample__parent_sample_id.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**
 *  **None** *[➞samples](study__samples.md)*  <sub>0..\*</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [➞sample_code](sample__sample_code.md)  <sub>1..1</sub>
     * Description: Human-friendly laboratory identifier or facility code for the sample (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference and tracking within laboratory workflows.
     * Range: [String](types/String.md)
 * [➞sample_type](sample__sample_type.md)  <sub>1..1</sub>
     * Description: Type of biological sample
     * Range: [SampleTypeEnum](SampleTypeEnum.md)
 * [➞molecular_composition](sample__molecular_composition.md)  <sub>0..1</sub>
     * Description: Description of molecular composition including sequences, modifications, ligands
     * Range: [MolecularComposition](MolecularComposition.md)
 * [➞molecular_weight](sample__molecular_weight.md)  <sub>0..1</sub>
     * Description: Molecular weight in kDa
     * Range: [Float](types/Float.md)
 * [➞concentration](sample__concentration.md)  <sub>0..1</sub>
     * Description: Sample concentration in mg/mL or µM
     * Range: [Float](types/Float.md)
 * [➞concentration_unit](sample__concentration_unit.md)  <sub>0..1</sub>
     * Description: Unit of concentration measurement
     * Range: [ConcentrationUnitEnum](ConcentrationUnitEnum.md)
 * [➞buffer_composition](sample__buffer_composition.md)  <sub>0..1</sub>
     * Description: Buffer composition including pH, salts, additives
     * Range: [BufferComposition](BufferComposition.md)
 * [➞preparation_method](sample__preparation_method.md)  <sub>0..1</sub>
     * Description: Method used to prepare the sample
     * Range: [String](types/String.md)
 * [➞storage_conditions](sample__storage_conditions.md)  <sub>0..1</sub>
     * Description: Storage conditions for the sample
     * Range: [StorageConditions](StorageConditions.md)
 * [➞organism](sample__organism.md)  <sub>0..1</sub>
     * Description: Source organism for the sample (e.g., NCBITaxon:3702 for Arabidopsis thaliana)
     * Range: [OntologyTerm](OntologyTerm.md)
 * [➞anatomy](sample__anatomy.md)  <sub>0..1</sub>
     * Description: Anatomical part or tissue (e.g., UBERON:0008945 for leaf)
     * Range: [OntologyTerm](OntologyTerm.md)
 * [➞cell_type](sample__cell_type.md)  <sub>0..1</sub>
     * Description: Cell type if applicable (e.g., CL:0000057 for fibroblast)
     * Range: [OntologyTerm](OntologyTerm.md)
 * [➞parent_sample_id](sample__parent_sample_id.md)  <sub>0..1</sub>
     * Description: Reference to parent sample for derivation tracking
     * Range: [Sample](Sample.md)
 * [➞purity_percentage](sample__purity_percentage.md)  <sub>0..1</sub>
     * Description: Sample purity as percentage (range: 0-100)
     * Range: [Float](types/Float.md)
 * [➞quality_metrics](sample__quality_metrics.md)  <sub>0..1</sub>
     * Description: Quality control metrics for the sample
     * Range: [String](types/String.md)
 * [➞functional_sites](sample__functional_sites.md)  <sub>0..\*</sub>
     * Description: Functional site annotations for proteins in the sample
     * Range: [FunctionalSite](FunctionalSite.md)
 * [➞structural_features](sample__structural_features.md)  <sub>0..\*</sub>
     * Description: Structural feature annotations
     * Range: [StructuralFeature](StructuralFeature.md)
 * [➞protein_interactions](sample__protein_interactions.md)  <sub>0..\*</sub>
     * Description: Protein-protein interaction annotations
     * Range: [ProteinProteinInteraction](ProteinProteinInteraction.md)
 * [➞ligand_interactions](sample__ligand_interactions.md)  <sub>0..\*</sub>
     * Description: Small molecule interaction annotations
     * Range: [LigandInteraction](LigandInteraction.md)
 * [➞mutation_effects](sample__mutation_effects.md)  <sub>0..\*</sub>
     * Description: Effects of mutations present in the sample
     * Range: [MutationEffect](MutationEffect.md)
 * [➞ptm_annotations](sample__ptm_annotations.md)  <sub>0..\*</sub>
     * Description: Post-translational modification annotations
     * Range: [PostTranslationalModification](PostTranslationalModification.md)
 * [➞biophysical_properties](sample__biophysical_properties.md)  <sub>0..\*</sub>
     * Description: Measured or predicted biophysical properties
     * Range: [BiophysicalProperty](BiophysicalProperty.md)
 * [➞evolutionary_conservation](sample__evolutionary_conservation.md)  <sub>0..1</sub>
     * Description: Evolutionary conservation data
     * Range: [EvolutionaryConservation](EvolutionaryConservation.md)
 * [➞conformational_ensemble](sample__conformational_ensemble.md)  <sub>0..1</sub>
     * Description: Conformational states and dynamics
     * Range: [ConformationalEnsemble](ConformationalEnsemble.md)
 * [➞database_cross_references](sample__database_cross_references.md)  <sub>0..\*</sub>
     * Description: Cross-references to external databases
     * Range: [DatabaseCrossReference](DatabaseCrossReference.md)
 * [➞protein_name](sample__protein_name.md)  <sub>0..1</sub>
     * Description: Name of the protein
     * Range: [String](types/String.md)
 * [➞construct](sample__construct.md)  <sub>0..1</sub>
     * Description: Construct description (e.g., domain boundaries, truncations)
     * Range: [String](types/String.md)
 * [➞tag](sample__tag.md)  <sub>0..1</sub>
     * Description: Affinity tag (e.g., His6, GST, MBP)
     * Range: [String](types/String.md)
 * [➞mutations](sample__mutations.md)  <sub>0..1</sub>
     * Description: Mutations present in the sample
     * Range: [String](types/String.md)
 * [➞expression_system](sample__expression_system.md)  <sub>0..1</sub>
     * Description: Expression system used
     * Range: [String](types/String.md)
 * [➞ligand](sample__ligand.md)  <sub>0..1</sub>
     * Description: Ligand or small molecule bound to sample
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
