# REMBI Alignment: Integrating Biological Imaging Metadata Standards with lambda-ber-schema

## Executive Summary

REMBI (Recommended Metadata for Biological Images) represents a community-driven standard for biological imaging metadata that shares significant overlap with lambda-ber-schema's goals for structural biology data management. Published in Nature Methods in 2021, REMBI provides guidelines for describing imaging experiments across light microscopy, electron microscopy, and X-ray microscopy—making it highly relevant to lambda-ber-schema's multi-modal approach. This document analyzes the alignment between REMBI and lambda-ber-schema, identifying opportunities for integration and mutual reinforcement of metadata standards in structural biology.

## 1. Introduction to REMBI

### 1.1 Background and Development

REMBI emerged from a critical need in the bioimaging community to standardize metadata for the vast amounts of imaging data being generated. Developed through a collaborative workshop in Hinxton (October 2019), REMBI brought together representatives from light, electron, and X-ray microscopy communities to establish common metadata guidelines.

**Key Publication**: Sarkans, U., Chiu, W., Collinson, L., et al. (2021). REMBI: Recommended Metadata for Biological Images—enabling reuse of microscopy data in biology. *Nature Methods*, 18, 1418–1422.

### 1.2 Core Objectives

REMBI aims to:
- Enable systematic archiving of imaging data and metadata in public databases
- Support FAIR (Findable, Accessible, Interoperable, Reusable) data principles
- Facilitate automated data harvesting using machine learning techniques
- Bridge diverse imaging communities with flexible yet comprehensive metadata standards

### 1.3 Adoption and Implementation

REMBI has been adopted by major imaging repositories:
- **BioImage Archive**: Primary implementation platform
- **EMPIAR**: Electron Microscopy Public Image Archive
- **Cell-IDR**: Image Data Resource for cellular imaging
- **Tissue-IDR**: Tissue-level imaging repository

## 2. REMBI's Eight-Component Structure

### 2.1 Hierarchical Organization

REMBI organizes metadata into eight high-level components that encompass diverse biological imaging methods:

```yaml
REMBI_Structure:
  1_Study:
    description: "Top-level project metadata"
    alignment: "Dublin Core, DataCite, schema.org"
    
  2_Study_Component:
    description: "Container for organizing related data"
    example: "Separate components for EM and confocal in correlative studies"
    
  3_Biosample:
    description: "Biological sample metadata"
    importance: "Critical for biological context"
    
  4_Specimen:
    description: "Specimen preparation details"
    includes: "Fixation, staining, mounting"
    
  5_Image_Acquisition:
    description: "Microscopy technique and settings"
    audience: "Imaging scientists and microscopists"
    
  6_Image_Data:
    description: "Image file metadata"
    implementation: "File list with technical parameters"
    
  7_Image_Correlation:
    description: "Multi-modal image registration"
    status: "Optional"
    use_case: "Correlative microscopy"
    
  8_Analyzed_Data:
    description: "Image analysis and measurements"
    status: "Optional"
    format: "Typically tabular"
```

### 2.2 Target Audiences

REMBI addresses three primary user groups:

1. **Imaging Scientists**: Need detailed acquisition parameters, physical properties of instruments
2. **Computer Vision Researchers**: Require ground truth data, segmentations, labeled datasets
3. **Biologists**: Focus on biological context, experimental conditions, sample preparation

## 3. Alignment with lambda-ber-schema

### 3.1 Structural Mapping

lambda-ber-schema and REMBI share substantial conceptual overlap, with complementary strengths:

| REMBI Component | lambda-ber-schema Equivalent | Alignment Level | Notes |
|-----------------|---------------------|-----------------|-------|
| Study | Study | **High** | Direct conceptual match |
| Study Component | ExperimentRun | **High** | Both organize data collection sessions |
| Biosample | Sample | **Very High** | Core biological material description |
| Specimen | SamplePreparation | **Very High** | Preparation protocols and methods |
| Image Acquisition | Instrument + ExperimentRun | **High** | lambda-ber-schema separates instrument from run |
| Image Data | Image (2D/3D) + DataFile | **High** | lambda-ber-schema has specialized image classes |
| Image Correlation | Cross-modal relationships | **Medium** | lambda-ber-schema handles via Study relationships |
| Analyzed Data | WorkflowRun + DataFile | **High** | Processing and derived data |

### 3.2 Complementary Strengths

#### REMBI Strengths for lambda-ber-schema

1. **Comprehensive Imaging Focus**: REMBI provides deeper metadata for microscopy-specific parameters
2. **Community Consensus**: Broad acceptance across imaging communities
3. **Correlation Metadata**: Explicit support for multi-modal image registration
4. **Machine Learning Ready**: Designed with AI/ML applications in mind

#### lambda-ber-schema Strengths for REMBI

1. **Structural Biology Depth**: Specialized support for crystallography, SAXS/SANS, spectroscopy
2. **Workflow Provenance**: Detailed computational processing tracking
3. **Multi-Scale Integration**: From atomic to tissue-level organization
4. **LinkML Foundation**: Semantic web compatibility and validation

### 3.3 Integration Opportunities

```yaml
Integration_Strategy:
  metadata_harmonization:
    - Map REMBI fields to lambda-ber-schema schema
    - Extend lambda-ber-schema with REMBI-specific attributes
    - Create bidirectional converters
    
  shared_vocabularies:
    - Adopt REMBI controlled terms for microscopy
    - Contribute structural biology terms to REMBI
    - Align with common ontologies (UBERON, CL, etc.)
    
  tool_ecosystem:
    - Support REMBI export from lambda-ber-schema
    - Import REMBI-compliant data
    - Validation across both standards
```

## 4. Specific Relevance to Structural Biology

### 4.1 Cryo-EM Applications

REMBI's adoption by EMPIAR creates direct relevance for structural biology:

**Case Study: EMPIAR-10061**
- Dataset: β-galactosidase raw cryo-EM data (12.4 TB)
- Original resolution: 2.2 Å
- Reuse examples:
  - Reprocessed to higher resolution by multiple groups
  - Used for algorithm development
  - Training data for deep learning particle picking
  - Cloud processing pipeline development

This demonstrates how REMBI metadata enables extensive data reuse in structural biology.

### 4.2 Correlative Microscopy

REMBI's Image Correlation component is particularly valuable for multi-modal structural biology:

```yaml
Correlative_Example:
  technique_1:
    type: "Cryo-EM"
    resolution: "3-5 Å"
    provides: "Molecular structure"
    
  technique_2:
    type: "Fluorescence"
    resolution: "200-300 nm"
    provides: "Cellular context"
    
  correlation_metadata:
    transformation_matrix: "3x4 affine"
    registration_error: "50 nm"
    fiducial_markers: "Gold particles"
    
  lambda-ber-schema_extension:
    add_rembi_correlation: true
    maintain_provenance: true
    cross_validate: true
```

### 4.3 Light Microscopy Integration

Many structural biology studies now incorporate light microscopy for context:

- **Live cell imaging** before vitrification
- **Fluorescence-guided** lamella preparation
- **CLEM** (Correlative Light and Electron Microscopy)
- **Super-resolution** microscopy for validation

REMBI provides the metadata framework for these techniques that lambda-ber-schema can leverage.

## 5. Implementation Recommendations

### 5.1 Short-Term Integration (0-6 months)

#### Metadata Mapping

Create explicit mappings between REMBI and lambda-ber-schema:

```python
class REMBIlambda-ber-schemaMapper:
    """Bidirectional mapper between REMBI and lambda-ber-schema schemas"""
    
    def rembi_to_lambda-ber-schema(self, rembi_data):
        lambda-ber-schema_study = {
            'title': rembi_data['study']['title'],
            'description': rembi_data['study']['description'],
            'samples': self.map_biosamples(rembi_data['biosample']),
            'sample_preparations': self.map_specimen(rembi_data['specimen']),
            'instrument_runs': self.map_acquisition(rembi_data['image_acquisition']),
            'images': self.map_image_data(rembi_data['image_data'])
        }
        
        # Handle optional correlation data
        if 'image_correlation' in rembi_data:
            lambda-ber-schema_study['cross_modal_registration'] = \
                self.map_correlation(rembi_data['image_correlation'])
        
        return lambda-ber-schema_study
    
    def lambda-ber-schema_to_rembi(self, lambda-ber-schema_data):
        # Inverse mapping for REMBI compliance
        pass
```

#### Vocabulary Alignment

Harmonize controlled vocabularies:

```yaml
Vocabulary_Mapping:
  sample_types:
    rembi: ["cell", "tissue", "organism", "molecule"]
    lambda-ber-schema: ["protein", "nucleic_acid", "complex", "cell", "tissue"]
    unified: ["protein", "nucleic_acid", "complex", "cell", "tissue", "organism", "small_molecule"]
    
  preparation_methods:
    rembi: ["fixation", "staining", "mounting"]
    lambda-ber-schema: ["vitrification", "crystallization", "purification"]
    unified: # Combine both sets with clear categories
    
  imaging_techniques:
    rembi: ["brightfield", "fluorescence", "confocal", "EM", "super-resolution"]
    lambda-ber-schema: ["cryo_em", "x_ray", "saxs", "sans", "ftir", "xrf"]
    unified: # Comprehensive technique ontology
```

### 5.2 Medium-Term Development (6-12 months)

#### Schema Extension

Extend lambda-ber-schema to incorporate REMBI-specific fields:

```yaml
# Addition to lambda-ber-schema schema
ImageCorrelation:
  is_a: AttributeGroup
  description: "REMBI-compatible image correlation metadata"
  attributes:
    source_image:
      range: Image
      description: "Reference image for alignment"
    target_image:
      range: Image
      description: "Image to be aligned"
    transformation_type:
      range: string
      description: "Type of transformation (affine, deformable, etc.)"
    transformation_parameters:
      range: float
      multivalued: true
      description: "Transformation matrix or parameters"
    registration_error:
      range: float
      description: "Registration accuracy in nm"
    fiducial_markers:
      range: string
      description: "Type of fiducial markers used"
    correlation_coefficient:
      range: float
      description: "Correlation quality metric"
```

#### Validation Framework

Implement cross-standard validation:

```python
class CrossStandardValidator:
    """Validate data against both REMBI and lambda-ber-schema"""
    
    def validate(self, data):
        results = {
            'lambda-ber-schema_valid': self.validate_lambda-ber-schema(data),
            'rembi_valid': self.validate_rembi(data),
            'cross_compatible': self.check_compatibility(data),
            'warnings': [],
            'errors': []
        }
        
        # Check for conflicts between standards
        if results['lambda-ber-schema_valid'] and not results['rembi_valid']:
            results['warnings'].append(
                "Data valid for lambda-ber-schema but missing REMBI requirements"
            )
        
        return results
```

### 5.3 Long-Term Vision (1-2 years)

#### Unified Imaging Metadata Standard

Work toward a unified standard that combines strengths:

```yaml
Future_Standard:
  name: "Unified Biological Imaging Metadata (UBIM)"
  foundation: "LinkML"
  components:
    - structural_biology: "From lambda-ber-schema"
    - light_microscopy: "From REMBI"
    - image_correlation: "From REMBI"
    - workflow_provenance: "From lambda-ber-schema"
    - ai_readiness: "From both"
  
  governance:
    - committee: "Joint REMBI-lambda-ber-schema working group"
    - stakeholders: ["wwPDB", "EMDB", "BioImage Archive", "IDR"]
    - update_cycle: "Annual"
```

## 6. Practical Examples

### 6.1 Example: Cryo-CLEM Study

Combining cryo-EM with fluorescence microscopy:

```yaml
Study:
  title: "Mitochondrial ATP synthase in situ structure"
  
  # REMBI-style biosample
  biosample:
    organism: "Homo sapiens"
    cell_type: "HeLa"
    organelle: "Mitochondria"
    
  # REMBI-style specimen preparation
  specimen:
    fixation: "Vitrification"
    temperature: "-180°C"
    fluorescent_label: "MitoTracker Green"
    
  # lambda-ber-schema-style experiment runs
  experiments:
    - technique: "fluorescence_microscopy"
      rembi_metadata:
        excitation_wavelength: "488 nm"
        emission_wavelength: "510 nm"
        objective: "100x/1.4 NA"
        
    - technique: "cryo_em"
      voltage: "300 kV"
      detector: "K3"
      pixel_size: "0.83 Å"
      
  # REMBI image correlation
  correlation:
    method: "Fiducial-based"
    markers: "100 nm gold"
    accuracy: "50 nm"
    software: "ec-CLEM"
```

### 6.2 Example: Multi-Scale Plant Imaging

From organ to molecular level:

```yaml
Study:
  title: "Chloroplast structure under stress"
  
  study_components:
    - name: "Whole leaf imaging"
      technique: "optical_microscopy"
      rembi_compliance: true
      scale: "mm"
      
    - name: "Cellular imaging"
      technique: "confocal_microscopy"
      rembi_compliance: true
      scale: "μm"
      
    - name: "Chloroplast ultrastructure"
      technique: "cryo_em_tomography"
      lambda-ber-schema_compliance: true
      scale: "nm"
      
    - name: "Protein structure"
      technique: "single_particle_cryoem"
      lambda-ber-schema_compliance: true
      scale: "Å"
      
  cross_scale_correlation:
    registration_method: "Hierarchical"
    coordinate_system: "Unified 3D"
    metadata_standard: "REMBI+lambda-ber-schema"
```

## 7. Benefits of Integration

### 7.1 For the Structural Biology Community

1. **Broader Data Integration**: Seamlessly combine molecular structures with cellular context
2. **Enhanced Discoverability**: REMBI-compliant data more findable in imaging repositories
3. **Improved Reproducibility**: Comprehensive metadata across scales
4. **AI/ML Readiness**: Standardized metadata for training algorithms

### 7.2 For the Imaging Community

1. **Structural Context**: Link cellular images to molecular structures
2. **Advanced Analytics**: Leverage structural biology computational tools
3. **Multi-Modal Workflows**: Streamlined correlative approaches
4. **Validation Frameworks**: Benefit from structural biology's rigorous validation

### 7.3 For Data Repositories

1. **Interoperability**: Exchange data between EMPIAR, BioImage Archive, and others
2. **Reduced Redundancy**: Shared metadata models reduce duplication
3. **Unified Submission**: Single pipeline for multi-modal studies
4. **Enhanced Services**: Offer cross-repository search and analysis

## 8. Challenges and Mitigation

### 8.1 Technical Challenges

| Challenge | Mitigation Strategy |
|-----------|-------------------|
| Schema complexity | Provide user-friendly tools and wizards |
| Vocabulary conflicts | Create mapping tables and conversion tools |
| Validation overhead | Implement automated validation pipelines |
| Storage requirements | Use hierarchical storage with metadata separation |

### 8.2 Community Challenges

| Challenge | Mitigation Strategy |
|-----------|-------------------|
| Adoption resistance | Demonstrate clear benefits through case studies |
| Training needs | Develop comprehensive educational materials |
| Legacy data | Provide migration tools and services |
| Governance | Establish joint committees with clear mandates |

## 9. Implementation Roadmap

### Phase 1: Foundation (Months 1-3)
- Establish working group with REMBI representatives
- Create detailed field mapping documentation
- Develop proof-of-concept converter tools
- Identify pilot projects for testing

### Phase 2: Integration (Months 4-9)
- Implement bidirectional converters
- Extend lambda-ber-schema schema with REMBI fields
- Develop validation frameworks
- Launch pilot projects with early adopters

### Phase 3: Deployment (Months 10-12)
- Release integrated tools and documentation
- Train repository staff and users
- Process feedback and iterate
- Plan long-term governance structure

### Phase 4: Maturation (Year 2+)
- Establish formal partnership with REMBI
- Contribute to standard evolution
- Expand adoption across communities
- Develop advanced integration features

## 10. Conclusions

### 10.1 Strategic Importance

The alignment between REMBI and lambda-ber-schema represents a critical opportunity to bridge the imaging and structural biology communities. With REMBI's broad adoption in biological imaging and lambda-ber-schema's comprehensive structural biology support, integration of these standards will enable unprecedented multi-scale, multi-modal studies.

### 10.2 Mutual Benefits

Both standards benefit from integration:
- REMBI gains access to structural biology's sophisticated data models and validation frameworks
- lambda-ber-schema gains established imaging metadata standards and community adoption
- The scientific community gains a more complete picture from molecules to organisms

### 10.3 Path Forward

The path to integration is clear and achievable:
1. Start with metadata mapping and vocabulary alignment
2. Build practical tools for data conversion
3. Demonstrate value through pilot projects
4. Formalize collaboration through governance structures
5. Work toward eventual standard convergence

### 10.4 Call to Action

We recommend:
1. **Immediate**: Contact REMBI maintainers to discuss collaboration
2. **Short-term**: Implement REMBI support in lambda-ber-schema tools
3. **Medium-term**: Joint workshops and training materials
4. **Long-term**: Co-develop next-generation unified standards

The convergence of REMBI and lambda-ber-schema will accelerate scientific discovery by enabling researchers to seamlessly navigate from cellular contexts to atomic details, ultimately advancing our understanding of biological systems across all scales.

## References

1. Sarkans, U., et al. (2021). REMBI: Recommended Metadata for Biological Images—enabling reuse of microscopy data in biology. *Nature Methods*, 18, 1418–1422.

2. REMBI Overview. European Bioinformatics Institute. https://www.ebi.ac.uk/bioimage-archive/rembi-help-overview/

3. Iudin, A., et al. (2016). EMPIAR: a public archive for raw electron microscopy image data. *Nature Methods*, 13, 387–388.

4. Williams, E., et al. (2017). The Image Data Resource: A Bioimage Data Integration and Publication Platform. *Nature Methods*, 14, 775–781.

5. Hartley, M., et al. (2022). The BioImage Archive – Building a Home for Life-Sciences Microscopy Data. *Journal of Molecular Biology*, 434(11), 167505.