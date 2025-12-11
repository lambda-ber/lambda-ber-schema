# Image Segmentation Integration for Lambda-BER-Schema

## Overview

This document explores integration of automated image segmentation workflows with the lambda-ber-schema data model, using foundation model-based approaches as a case study. Image segmentation is critical for extracting quantitative features from structural biology imaging data, and modern AI approaches are transforming how researchers analyze cryo-EM, X-ray crystallography, FIB-SEM, and other imaging modalities.

## Background: Segmentation in Structural Biology

### Role of Segmentation

Image segmentation - the process of partitioning images into meaningful regions or objects - is fundamental to structural biology image analysis across multiple scales and techniques:

**Cryo-Electron Microscopy (Cryo-EM)**
- Particle picking: Identifying individual protein particles in micrographs for single-particle analysis
- Tomogram segmentation: Delineating subcellular structures, organelles, and macromolecular complexes in cryo-electron tomography
- Membrane segmentation: Identifying lipid bilayers and membrane-associated proteins
- Example: Deep learning models like crYOLO [Wagner et al. 2019] and TOPAZ [Bepler et al. 2019] achieve near-human performance for automated particle picking

**X-ray Crystallography**
- Crystal identification and tracking during screening and data collection
- Loop detection in mounting images
- Ice ring and diffraction spot segmentation in diffraction patterns
- Solvent boundary identification in electron density maps

**Materials Science Imaging (FIB-SEM, TEM)**
- Phase segmentation: Distinguishing catalyst, ionomer, void space in electrode materials
- Pore network characterization for fuel cells and batteries
- Grain boundary detection in crystalline materials
- Multi-phase material quantification [Mukherjee et al. 2025]

**Small Angle Scattering (SAXS/SANS)**
- Background subtraction and signal region identification
- Artifact detection in 2D detector images
- Automated buffer selection from image series

### Traditional Approaches

Classical segmentation methods have been workhorses of structural biology:

1. **Thresholding Methods**
   - Otsu thresholding for intensity-based separation
   - Adaptive thresholding for varying local contrast
   - Limited effectiveness on low-SNR scientific images [Mukherjee et al. 2025]

2. **Edge-Based Methods**
   - Sobel, Canny edge detection for boundary identification
   - Struggle with noisy electron microscopy data

3. **Template Matching**
   - Normalized cross-correlation for particle picking
   - Computationally expensive, requires good templates
   - Gold standard for many years in cryo-EM [Sigworth 2004]

4. **Machine Learning (Pre-Deep Learning)**
   - Random forests, SVMs for pixel classification
   - Feature engineering required (HOG, SIFT, etc.)
   - Examples: ilastik [Sommer et al. 2011] for interactive segmentation

### Deep Learning Revolution

Modern deep learning has transformed segmentation capabilities:

**Supervised Approaches**
- U-Net architectures for biomedical image segmentation [Ronneberger et al. 2015]
- Mask R-CNN for instance segmentation
- 3D CNNs for volumetric data (3D U-Net) [Çiçek et al. 2016]
- Requires large annotated datasets - major bottleneck for scientific imaging

**Self-Supervised and Foundation Models**
- DINO (self-DIstillation with NO labels) [Liu et al. 2023] for visual representation learning
- Segment Anything Model (SAM) [Kirillov et al. 2023] for zero-shot segmentation
- SAM 2 [Ravi et al. 2024] extends to video/volumetric sequences
- Grounding DINO + SAM for text-prompted segmentation
- Domain-specific adaptations: MedSAM [Ma et al. 2024], µSAM [Archit et al. 2025] for microscopy

**Challenge: The AI-Readiness Gap**

Scientific imaging data presents unique challenges that limit direct application of foundation models [Mukherjee et al. 2025]:

- **Non-standard formats**: 16/32-bit depth, proprietary formats (CBF, IMG, H5)
- **Anisotropic sampling**: Different resolution in X/Y/Z dimensions
- **Extreme dynamic ranges**: High bit depths not compatible with 8-bit RGB models
- **Domain-specific artifacts**: Beam damage, ice contamination, diffraction artifacts
- **Lack of annotations**: No large-scale labeled datasets for most scientific domains
- **Low signal-to-noise**: Particularly acute in dose-limited cryo-EM

Recent work like Zenesis [Mukherjee et al. 2025] addresses this gap by providing lightweight adaptation techniques that make foundation models work on raw scientific data without extensive retraining or preprocessing.

## Zenesis: A Case Study in Foundation Model Segmentation

### Overview

Zenesis is a comprehensive no-code platform for zero-shot segmentation of scientific images, developed at Lawrence Berkeley National Laboratory [Mukherjee et al. 2025]. It demonstrates how modern foundation models can be adapted for non-AI-ready scientific data through:

1. **Multi-modal grounding**: GroundingDINO for text-guided bounding box detection
2. **Zero-shot segmentation**: SAM/SAM2 for mask generation without training
3. **Human-in-the-loop refinement**: Interactive correction of automated results
4. **Volumetric consistency**: Heuristic-based temporal smoothing for 3D data
5. **Real-time evaluation**: Comprehensive metrics (Dice, IoU, accuracy) at multiple granularities

### Performance

Validated on FIB-SEM imaging of catalyst materials (crystalline and amorphous IrO₂ in PEM electrolyzer ionomer films):

| Method | Sample Type | Accuracy | IoU | Dice Score |
|--------|-------------|----------|-----|------------|
| Otsu Threshold | Crystalline | 0.586±0.125 | 0.161±0.057 | 0.274±0.080 |
| Otsu Threshold | Amorphous | 0.581±0.019 | 0.407±0.024 | 0.578±0.024 |
| SAM-only | Crystalline | 0.485±0.146 | 0.100±0.083 | 0.173±0.137 |
| SAM-only | Amorphous | 0.499±0.160 | 0.405±0.088 | 0.571±0.087 |
| **Zenesis** | **Crystalline** | **0.987±0.005** | **0.857±0.029** | **0.923±0.017** |
| **Zenesis** | **Amorphous** | **0.947±0.005** | **0.858±0.015** | **0.923±0.009** |

The dramatic improvement over baselines demonstrates the value of text-guided grounding (GroundingDINO) to overcome SAM's tendency to segment high-contrast background regions rather than subtle scientific features.

### Workflow Architecture

```
┌─────────────────────┐
│  Raw Scientific     │
│  Images/Volumes     │
│  (FIB-SEM, Cryo-EM, │
│   SAXS, XRD, etc.)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Data Harmonization  │
│ - Format conversion │
│ - Bit depth handling│
│ - Bicubic interpolation│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  GroundingDINO      │
│  (Text → BBox)      │
│  Prompt: "porous    │
│   ionomer layer"    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  SAM/SAM2           │
│  (BBox → Mask)      │
└──────────┬──────────┘
           │
           ├─────────────────────┐
           │                     │
           ▼                     ▼
┌─────────────────────┐  ┌──────────────────┐
│ Human-in-the-Loop   │  │ Volumetric       │
│ - Random box        │  │ Refinement       │
│   correction        │  │ - Sliding window │
│ - Hierarchical      │  │   averaging      │
│   segmentation      │  │ - Outlier        │
│                     │  │   correction     │
└─────────────────────┘  └──────────────────┘
           │                     │
           └──────────┬──────────┘
                      │
                      ▼
           ┌─────────────────────┐
           │  Segmentation       │
           │  Outputs            │
           │  - Masks            │
           │  - Bounding boxes   │
           │  - Metrics          │
           │  - Visualizations   │
           └─────────────────────┘
```

## Integration with Lambda-BER-Schema

### Current Schema Coverage

The existing lambda-ber-schema already supports key aspects of segmentation workflows:

**ExperimentRun**: Captures raw image acquisition
- Detector settings (bit depth, pixel size, exposure)
- Instrument parameters
- Quality metrics

**WorkflowRun**: Tracks computational processing
- Software name/version
- Parameters
- Quality metrics
- Processing status

**DataFile**: Links input/output files
- File formats
- Checksums
- Parent-child relationships

**Sample**: Provides biological/chemical context
- Molecular composition
- Buffer conditions
- Sample preparation details

### Proposed Schema Extensions

To fully support modern segmentation workflows, we propose the following additions:

#### 1. AIModelRun Class

Capture execution of AI/ML models with full reproducibility:

```yaml
AIModelRun:
  description: "Execution of an AI/ML model on scientific imaging data"
  is_a: WorkflowRun

  attributes:
    model_name:
      range: string
      required: true
      examples:
        - "GroundingDINO"
        - "SAM"
        - "SAM2"
        - "crYOLO"
        - "TOPAZ"
        - "DeepPicker"

    model_version:
      range: string
      required: true
      examples: ["1.0", "Swin-T", "ViT-H"]

    model_architecture:
      range: string
      description: "Model architecture details"
      examples:
        - "Swin-T + ViT-H"
        - "Vision Transformer (ViT-H/16)"
        - "ResNet50 + FPN"

    model_weights:
      range: string
      description: "Source of pretrained weights or checkpoint path"
      examples:
        - "COCO-pretrained"
        - "s3://models/fib-sem-finetuned-v2.pth"

    prompt_text:
      range: string
      description: "Natural language prompt for grounding/text-guided models"
      examples:
        - "porous ionomer layer"
        - "protein particle"
        - "crystalline catalyst"

    prompt_type:
      range: PromptTypeEnum
      description: "Type of prompt/guidance provided to model"

    confidence_thresholds:
      range: ConfidenceThresholds
      description: "Threshold parameters for model outputs"

    human_in_the_loop:
      range: boolean
      description: "Whether interactive refinement was performed"

    interactive_corrections:
      range: InteractiveCorrection
      multivalued: true
      description: "Log of human corrections made during processing"

    preprocessing_steps:
      range: PreprocessingStep
      multivalued: true
      description: "Data transformations applied before model inference"

PromptTypeEnum:
  permissible_values:
    text:
      description: "Natural language text prompt"
    point:
      description: "Point click prompts"
    bounding_box:
      description: "Rectangular box prompts"
    rough_mask:
      description: "Coarse segmentation outline"
    interactive:
      description: "Mixed human-in-the-loop prompting"

ConfidenceThresholds:
  attributes:
    box_threshold:
      range: float
      description: "Minimum confidence for bounding box detection"
      minimum_value: 0.0
      maximum_value: 1.0
    text_threshold:
      range: float
      description: "Minimum confidence for text-image alignment"
    mask_threshold:
      range: float
      description: "Minimum confidence for mask prediction"
```

#### 2. SegmentationOutput Class

Structured representation of segmentation results:

```yaml
SegmentationOutput:
  description: "Results from image segmentation workflow"

  attributes:
    mask_file:
      range: DataFile
      required: true
      description: "Binary or multi-class segmentation masks"

    bounding_boxes:
      range: BoundingBox
      multivalued: true
      description: "Detected object bounding boxes"

    segmentation_metrics:
      range: SegmentationMetrics
      description: "Quantitative evaluation metrics"

    extracted_segments:
      range: DataFile
      multivalued: true
      description: "Individual segmented objects/regions"

    visualization_files:
      range: DataFile
      multivalued: true
      description: "Overlay images, dashboards, etc."

    hierarchical_segments:
      range: SegmentationOutput
      multivalued: true
      description: "Nested segmentations (e.g., 'Further Segment' in Zenesis)"

BoundingBox:
  attributes:
    x_min:
      range: float
      required: true
    y_min:
      range: float
      required: true
    x_max:
      range: float
      required: true
    y_max:
      range: float
      required: true
    z_min:
      range: float
      description: "For 3D volumes"
    z_max:
      range: float
    confidence:
      range: float
      minimum_value: 0.0
      maximum_value: 1.0
    label:
      range: string
      description: "Class label or object name"

SegmentationMetrics:
  description: "Quantitative metrics for segmentation quality"
  attributes:
    dice_score:
      range: float
      description: "Dice similarity coefficient (F1 score for segmentation)"
      minimum_value: 0.0
      maximum_value: 1.0
    iou:
      range: float
      description: "Intersection over Union (Jaccard index)"
      minimum_value: 0.0
      maximum_value: 1.0
    accuracy:
      range: float
      description: "Pixel-wise accuracy"
      minimum_value: 0.0
      maximum_value: 1.0
    precision:
      range: float
      minimum_value: 0.0
      maximum_value: 1.0
    recall:
      range: float
      minimum_value: 0.0
      maximum_value: 1.0
    f1_score:
      range: float
      minimum_value: 0.0
      maximum_value: 1.0
    specificity:
      range: float
      minimum_value: 0.0
      maximum_value: 1.0
    ground_truth_available:
      range: boolean
      description: "Whether metrics are computed against ground truth"
```

#### 3. ImagePreprocessing Class

Track data transformations that achieve "AI-readiness":

```yaml
ImagePreprocessing:
  description: "Transformations applied to raw data to make it AI-compatible"
  is_a: WorkflowRun

  attributes:
    normalization_method:
      range: NormalizationMethodEnum
      description: "Intensity normalization approach"

    bit_depth_conversion:
      range: string
      description: "Bit depth transformation"
      examples:
        - "16bit_to_8bit_percentile"
        - "preserve_16bit"
        - "32bit_float_normalize"

    contrast_adjustment:
      range: ContrastMethodEnum
      description: "Contrast enhancement method"

    resolution_harmonization:
      range: ResolutionHarmonization
      description: "Handling anisotropic voxel sizes"

    format_conversion:
      range: FormatConversion
      description: "File format transformation"

    artifact_correction:
      range: ArtifactCorrection
      multivalued: true
      description: "Domain-specific artifact removal"

NormalizationMethodEnum:
  permissible_values:
    percentile_clip:
      description: "Clip to percentile range (e.g., 1-99%)"
    zscore:
      description: "Z-score normalization"
    min_max:
      description: "Min-max scaling to [0,1]"
    histogram_equalization:
      description: "Adaptive histogram equalization (CLAHE)"
    none:
      description: "No normalization applied"

ContrastMethodEnum:
  permissible_values:
    clahe:
      description: "Contrast Limited Adaptive Histogram Equalization"
    unsharp_mask:
      description: "Unsharp masking for edge enhancement"
    gamma_correction:
      description: "Gamma adjustment"
    adaptive_threshold:
      description: "Local adaptive thresholding"
    none:
      description: "No contrast adjustment"

ResolutionHarmonization:
  description: "Methods for handling anisotropic imaging"
  attributes:
    method:
      range: ResamplingMethodEnum
    target_voxel_size:
      range: VoxelSize
    interpolation:
      range: InterpolationMethodEnum

ResamplingMethodEnum:
  permissible_values:
    isotropic_resampling:
      description: "Resample to isotropic voxels"
    slice_by_slice:
      description: "Process 2D slices independently"
    anisotropic_kernel:
      description: "Use anisotropic convolution kernels"
    preserve_native:
      description: "Keep original anisotropic sampling"

InterpolationMethodEnum:
  permissible_values:
    bicubic:
      description: "Bicubic interpolation"
    bilinear:
      description: "Bilinear interpolation"
    nearest_neighbor:
      description: "Nearest neighbor"
    lanczos:
      description: "Lanczos resampling"

ArtifactCorrection:
  attributes:
    artifact_type:
      range: ArtifactTypeEnum
    correction_method:
      range: string
    parameters:
      range: string
      description: "JSON-encoded correction parameters"

ArtifactTypeEnum:
  permissible_values:
    ice_contamination:
      description: "Ice crystals in cryo-EM"
    beam_damage:
      description: "Radiation damage artifacts"
    motion_blur:
      description: "Sample motion during acquisition"
    charging_artifacts:
      description: "Electron charging in SEM/TEM"
    diffraction_artifacts:
      description: "Unwanted diffraction in X-ray data"
    detector_artifacts:
      description: "Dead pixels, hot pixels, detector edge effects"
```

#### 4. AIReadinessAssessment

Metadata to track whether data is suitable for foundation models:

```yaml
AIReadinessAssessment:
  description: "Assessment of data compatibility with AI/ML workflows"

  attributes:
    assessed_date:
      range: string
      description: "When assessment was performed"

    bit_depth_compatible:
      range: boolean
      description: "Whether bit depth is compatible with target model"

    format_standardized:
      range: boolean
      description: "Whether file format is AI-framework compatible"

    contrast_sufficient:
      range: boolean
      description: "Whether contrast is adequate for segmentation"

    resolution_adequate:
      range: boolean
      description: "Whether spatial resolution meets model requirements"

    annotation_available:
      range: boolean
      description: "Whether ground truth annotations exist"

    signal_to_noise_ratio:
      range: float
      description: "Estimated SNR"

    preprocessing_required:
      range: string
      multivalued: true
      description: "List of required preprocessing steps"
      examples:
        - "contrast_normalization"
        - "anisotropic_voxel_correction"
        - "artifact_removal"

    foundation_model_applicable:
      range: boolean
      description: "Whether zero-shot foundation models can be applied"

    recommended_approach:
      range: SegmentationApproachEnum
      description: "Recommended segmentation strategy"

SegmentationApproachEnum:
  permissible_values:
    foundation_model_zero_shot:
      description: "Foundation models (SAM, Zenesis) without training"
    foundation_model_finetuned:
      description: "Foundation models with domain-specific fine-tuning"
    supervised_training:
      description: "Train supervised model from scratch (requires annotations)"
    classical_methods:
      description: "Traditional image processing (thresholding, edge detection)"
    hybrid:
      description: "Combination of AI and classical methods"
```

### Example: Complete Zenesis Workflow in Schema

```yaml
Dataset:
  dataset_id: "CIWE-2025-001"
  title: "Iridium Oxide Catalyst Distribution in PEM Electrolyzer Ionomer Films"
  studies:
    - study_code: "CIWE-IrO2-FIB-SEM-2025"
      description: "FIB-SEM imaging of crystalline and amorphous IrO₂ catalysts"

      # Sample metadata
      samples:
        - sample_code: "IrO2-crystalline-001"
          sample_type: catalyst
          molecular_composition:
            - molecule_name: "Iridium oxide (crystalline)"
              chemical_formula: "IrO2"
              concentration: 0.85
              concentration_unit: mg_per_cm2
          storage_conditions:
            storage_temperature: -80
            temperature_unit: celsius
          notes: "Needle-like morphology, specific surface area ~110 m²/g"

        - sample_code: "IrO2-amorphous-001"
          sample_type: catalyst
          molecular_composition:
            - molecule_name: "Iridium oxide (amorphous)"
              chemical_formula: "IrOx"
              concentration: 0.85
              concentration_unit: mg_per_cm2
          notes: "Specific surface area ~50 m²/g"

      # FIB-SEM acquisition
      instrument_runs:
        - experiment_code: "FIB-SEM-20250630-001"
          technique: fib_sem
          sample_id: "IrO2-crystalline-001"
          instrument_id: "LBNL-FIB-SEM-01"
          start_date: "2025-06-30"
          collection_mode: volumetric
          detector_settings:
            bit_depth: 16
            pixel_size_x: 5.0  # nm
            pixel_size_y: 5.0
            voxel_size_z: 10.0  # anisotropic
          quality_metrics:
            - metric_name: "Signal-to-Noise Ratio"
              metric_value: "12.5"
          ai_readiness_assessment:
            assessed_date: "2025-06-30"
            bit_depth_compatible: true
            format_standardized: true
            contrast_sufficient: false
            resolution_adequate: true
            annotation_available: false
            preprocessing_required:
              - "contrast_normalization"
              - "anisotropic_voxel_correction"
            foundation_model_applicable: true
            recommended_approach: foundation_model_zero_shot

        - experiment_code: "FIB-SEM-20250630-002"
          technique: fib_sem
          sample_id: "IrO2-amorphous-001"
          instrument_id: "LBNL-FIB-SEM-01"
          start_date: "2025-06-30"
          collection_mode: volumetric
          detector_settings:
            bit_depth: 16
            pixel_size_x: 5.0
            pixel_size_y: 5.0
            voxel_size_z: 10.0

      # Data preprocessing workflow
      workflow_runs:
        - workflow_code: "PREPROCESS-001"
          workflow_type: image_preprocessing
          experiment_id: "FIB-SEM-20250630-001"
          software_name: "Zenesis"
          software_version: "1.0"
          processing_status: completed
          start_date: "2025-06-30T14:00:00"
          end_date: "2025-06-30T14:15:00"
          parameters:
            normalization_method: "percentile_clip"
            bit_depth_conversion: "16bit_to_8bit_percentile"
            contrast_adjustment: "clahe"
            resolution_harmonization:
              method: "isotropic_resampling"
              interpolation: "bicubic"

        # Zenesis segmentation workflow
        - workflow_code: "ZENESIS-SEG-001"
          workflow_type: ai_segmentation
          experiment_id: "FIB-SEM-20250630-001"
          software_name: "Zenesis"
          software_version: "1.0"
          processing_status: completed
          start_date: "2025-06-30T14:15:00"
          end_date: "2025-06-30T15:30:00"
          parameters:
            model_name: "GroundingDINO + SAM"
            model_version: "Swin-T + ViT-H"
            model_architecture: "Swin Transformer + Vision Transformer"
            prompt_text: "porous ionomer layer"
            prompt_type: "text"
            box_threshold: 0.35
            text_threshold: 0.25
            human_in_the_loop: true
            preprocessing_pipeline: "PREPROCESS-001"
            volumetric_refinement:
              enabled: true
              method: "sliding_window_average"
              window_size: 5
              height_factor_threshold: 2.0
          quality_metrics:
            - metric_name: "Dice Score"
              metric_value: "0.923"
            - metric_name: "IoU"
              metric_value: "0.857"
            - metric_name: "Accuracy"
              metric_value: "0.987"
            - metric_name: "Processing Time"
              metric_value: "75"
              metric_unit: "minutes"
          segmentation_output:
            mask_file: "zenesis_masks_crystalline.npy"
            bounding_boxes:
              - x_min: 150
                y_min: 200
                x_max: 1800
                y_max: 450
                confidence: 0.92
                label: "ionomer_layer"
            segmentation_metrics:
              dice_score: 0.923
              iou: 0.857
              accuracy: 0.987
              ground_truth_available: true
            visualization_files:
              - "zenesis_overlay_crystalline.png"
              - "zenesis_dashboard_crystalline.html"

        - workflow_code: "ZENESIS-SEG-002"
          workflow_type: ai_segmentation
          experiment_id: "FIB-SEM-20250630-002"
          software_name: "Zenesis"
          software_version: "1.0"
          processing_status: completed
          parameters:
            model_name: "GroundingDINO + SAM"
            prompt_text: "porous ionomer layer"
            prompt_type: "text"
            human_in_the_loop: true
          quality_metrics:
            - metric_name: "Dice Score"
              metric_value: "0.923"
            - metric_name: "IoU"
              metric_value: "0.858"
            - metric_name: "Accuracy"
              metric_value: "0.947"
          segmentation_output:
            segmentation_metrics:
              dice_score: 0.923
              iou: 0.858
              accuracy: 0.947
              ground_truth_available: true

        # Feature extraction from segmentations
        - workflow_code: "FEATURE-EXTRACT-001"
          workflow_type: quantitative_analysis
          experiment_id: "FIB-SEM-20250630-001"
          software_name: "scikit-image"
          software_version: "0.24.0"
          processing_status: completed
          parent_workflow: "ZENESIS-SEG-001"
          parameters:
            input_masks: "zenesis_masks_crystalline.npy"
            features_computed:
              - "ionomer_coverage_fraction"
              - "catalyst_particle_count"
              - "pore_size_distribution"
              - "interfacial_area"
          quality_metrics:
            - metric_name: "Ionomer Coverage"
              metric_value: "68.5"
              metric_unit: "percent"
            - metric_name: "Average Pore Size"
              metric_value: "45.2"
              metric_unit: "nm"

      # Data files with provenance
      data_files:
        # Raw data
        - file_name: "crystalline_IrO2_volume.tiff"
          file_format: tiff
          file_size_mb: 2500
          data_type: raw_image
          checksum: "sha256:abc123def456..."
          experiment_id: "FIB-SEM-20250630-001"

        - file_name: "amorphous_IrO2_volume.tiff"
          file_format: tiff
          file_size_mb: 2400
          data_type: raw_image
          experiment_id: "FIB-SEM-20250630-002"

        # Preprocessed data
        - file_name: "crystalline_normalized.npy"
          file_format: numpy
          file_size_mb: 1200
          data_type: processed_image
          parent_file: "crystalline_IrO2_volume.tiff"
          workflow_id: "PREPROCESS-001"

        # Segmentation outputs
        - file_name: "zenesis_masks_crystalline.npy"
          file_format: numpy
          file_size_mb: 150
          data_type: segmentation_mask
          parent_file: "crystalline_normalized.npy"
          workflow_id: "ZENESIS-SEG-001"
          checksum: "sha256:seg789mask012..."

        - file_name: "zenesis_bboxes_crystalline.json"
          file_format: json
          file_size_mb: 0.5
          data_type: annotation
          workflow_id: "ZENESIS-SEG-001"

        - file_name: "zenesis_overlay_crystalline.png"
          file_format: png
          file_size_mb: 25
          data_type: visualization
          workflow_id: "ZENESIS-SEG-001"

        - file_name: "zenesis_dashboard_crystalline.html"
          file_format: html
          file_size_mb: 2
          data_type: visualization
          workflow_id: "ZENESIS-SEG-001"

        # Feature tables
        - file_name: "ionomer_features_crystalline.parquet"
          file_format: parquet
          file_size_mb: 5
          data_type: derived_data
          workflow_id: "FEATURE-EXTRACT-001"
          parent_file: "zenesis_masks_crystalline.npy"
```

## Lakehouse Integration Architecture

### Bronze Layer: Raw Scientific Data

**Purpose**: Store raw, unmodified acquisition data with minimal schema validation

**Storage Format**: Native scientific formats with Delta Lake metadata overlay

```
s3://lakehouse/bronze/
├── fib-sem/
│   ├── technique=fib_sem/
│   │   └── year=2025/month=06/day=30/
│   │       ├── crystalline_IrO2_volume.tiff
│   │       ├── amorphous_IrO2_volume.tiff
│   │       └── _delta_log/
│   └── metadata/
│       └── lambda-ber-schema/
│           └── experiment_runs.json
├── cryo-em/
│   └── technique=cryo_em/
└── xray/
    └── technique=xrd/
```

**Lambda-BER-Schema Role**:
- Catalog all raw acquisitions with provenance
- Link to instrument parameters, sample metadata
- Track AI readiness assessment
- Enable cross-technique queries

**Example Query**:
```sql
-- Find all 16-bit FIB-SEM volumes with high SNR
SELECT
    e.experiment_code,
    e.sample_id,
    s.molecular_composition,
    e.detector_settings.bit_depth,
    e.quality_metrics
FROM experiment_runs e
JOIN samples s ON e.sample_id = s.sample_code
WHERE e.technique = 'fib_sem'
  AND e.collection_mode = 'volumetric'
  AND e.detector_settings.bit_depth = 16
  AND json_extract(e.quality_metrics, '$[?(@.metric_name=="Signal-to-Noise Ratio")].metric_value') > 10
  AND e.ai_readiness_assessment.foundation_model_applicable = true
```

### Silver Layer: Preprocessed and Segmented Data

**Purpose**: Store AI-ready data and segmentation results with quality metrics

**Storage Format**: Standardized formats (NumPy, Zarr, Parquet) in Delta Lake tables

```
s3://lakehouse/silver/
├── preprocessed/
│   ├── technique=fib_sem/preprocessing=zenesis/
│   │   ├── data/
│   │   │   ├── crystalline_normalized.zarr/
│   │   │   └── amorphous_normalized.zarr/
│   │   └── _delta_log/
│   └── metadata/
│       └── image_preprocessing_workflows.parquet
│
├── segmentations/
│   ├── model=zenesis/prompt=ionomer_layer/
│   │   ├── masks/
│   │   │   ├── crystalline_masks.zarr/
│   │   │   └── amorphous_masks.zarr/
│   │   ├── bounding_boxes/
│   │   │   └── all_bboxes.parquet
│   │   └── _delta_log/
│   └── metadata/
│       └── segmentation_workflows.parquet
│
└── quality_metrics/
    ├── per_slice_metrics.parquet
    ├── per_sample_metrics.parquet
    └── _delta_log/
```

**Lambda-BER-Schema Role**:
- Track preprocessing transformations (WorkflowRun with ImagePreprocessing)
- Record segmentation parameters (AIModelRun)
- Store quality metrics (SegmentationMetrics)
- Link outputs to input experiments

**Example Query**:
```sql
-- Compare segmentation quality across different samples
SELECT
    w.workflow_code,
    e.sample_id,
    s.sample_type,
    s.molecular_composition[0].molecule_name as catalyst_type,
    json_extract(w.quality_metrics, '$[?(@.metric_name=="Dice Score")].metric_value') as dice_score,
    json_extract(w.quality_metrics, '$[?(@.metric_name=="IoU")].metric_value') as iou,
    w.parameters.prompt_text,
    w.parameters.human_in_the_loop
FROM workflow_runs w
JOIN experiment_runs e ON w.experiment_id = e.experiment_code
JOIN samples s ON e.sample_id = s.sample_code
WHERE w.workflow_type = 'ai_segmentation'
  AND w.software_name = 'Zenesis'
  AND json_extract(w.quality_metrics, '$[?(@.metric_name=="Dice Score")].metric_value') > 0.90
ORDER BY dice_score DESC
```

### Gold Layer: Analytics-Ready Feature Tables

**Purpose**: Store derived quantitative features and aggregated metrics for scientific analysis

**Storage Format**: Parquet tables optimized for analytics queries

```
s3://lakehouse/gold/
├── feature_tables/
│   ├── ionomer_coverage/
│   │   ├── coverage_by_sample.parquet
│   │   ├── coverage_by_depth.parquet
│   │   └── _delta_log/
│   ├── catalyst_distribution/
│   │   ├── particle_counts.parquet
│   │   ├── size_distributions.parquet
│   │   └── _delta_log/
│   ├── pore_network/
│   │   ├── pore_sizes.parquet
│   │   ├── connectivity.parquet
│   │   └── _delta_log/
│   └── interfacial_properties/
│       ├── surface_areas.parquet
│       └── _delta_log/
│
├── aggregated_metrics/
│   ├── study_summary.parquet
│   ├── technique_comparison.parquet
│   └── _delta_log/
│
└── visualizations/
    ├── dashboards/
    │   └── segmentation_quality_overview.html
    └── reports/
        └── material_characterization_report.pdf
```

**Lambda-BER-Schema Role**:
- Link derived features to original samples and experiments
- Track feature extraction workflows
- Enable cross-study comparisons
- Support hypothesis testing and correlation analysis

**Example Query**:
```sql
-- Correlate catalyst morphology with segmentation difficulty
SELECT
    s.sample_code,
    s.molecular_composition[0].molecule_name as catalyst,
    json_extract(s.notes, '$.specific_surface_area') as surface_area,
    w.quality_metrics.dice_score,
    f.ionomer_coverage,
    f.avg_pore_size,
    f.interfacial_area
FROM samples s
JOIN experiment_runs e ON s.sample_code = e.sample_id
JOIN workflow_runs w ON e.experiment_code = w.experiment_id
JOIN feature_tables.ionomer_coverage f ON w.workflow_code = f.workflow_id
WHERE w.software_name = 'Zenesis'
ORDER BY surface_area DESC
```

### Data Flow Pipeline

```python
# Conceptual data pipeline using Delta Lake + lambda-ber-schema

from delta import DeltaTable
import yaml
import numpy as np
from zenesis import SegmentationPipeline

# 1. BRONZE: Ingest raw FIB-SEM data with schema metadata
def ingest_raw_data(tiff_path, schema_metadata_path):
    """Bronze layer: raw data + lambda-ber-schema metadata"""

    # Load schema metadata
    with open(schema_metadata_path) as f:
        metadata = yaml.safe_load(f)

    experiment = metadata['instrument_runs'][0]

    # Write to Delta Lake with partitioning
    (spark.read.format("geotiff")
        .load(tiff_path)
        .withColumn("experiment_code", lit(experiment['experiment_code']))
        .withColumn("technique", lit(experiment['technique']))
        .withColumn("sample_id", lit(experiment['sample_id']))
        .withColumn("bit_depth", lit(experiment['detector_settings']['bit_depth']))
        .withColumn("acquisition_date", lit(experiment['start_date']))
        .write
        .format("delta")
        .partitionBy("technique", "acquisition_date")
        .mode("append")
        .save("s3://lakehouse/bronze/fib-sem/"))

    # Also write full schema metadata
    (spark.createDataFrame([metadata])
        .write
        .format("delta")
        .mode("append")
        .save("s3://lakehouse/bronze/metadata/lambda-ber-schema/"))

# 2. SILVER: Run Zenesis segmentation and track in schema
def run_segmentation_pipeline(experiment_code):
    """Silver layer: AI processing with full provenance"""

    # Read raw data from Bronze
    raw_df = (spark.read.format("delta")
        .load("s3://lakehouse/bronze/fib-sem/")
        .filter(f"experiment_code = '{experiment_code}'"))

    # Read metadata from schema
    metadata_df = (spark.read.format("delta")
        .load("s3://lakehouse/bronze/metadata/lambda-ber-schema/")
        .filter(f"instrument_runs.experiment_code = '{experiment_code}'"))

    experiment = metadata_df.first()['instrument_runs'][0]
    sample_id = experiment['sample_id']

    # Check AI readiness
    ai_readiness = experiment.get('ai_readiness_assessment', {})
    if not ai_readiness.get('foundation_model_applicable', False):
        raise ValueError(f"Experiment {experiment_code} not suitable for foundation models")

    # Configure Zenesis from schema
    pipeline = SegmentationPipeline(
        model="GroundingDINO+SAM",
        prompt=ai_readiness.get('segmentation_prompt', 'porous ionomer layer'),
        box_threshold=0.35,
        text_threshold=0.25,
        human_in_the_loop=True,
        volumetric_refinement=True
    )

    # Run segmentation
    volume = raw_df.select("data").first()["data"]
    results = pipeline.run(volume)

    # Create workflow metadata for lambda-ber-schema
    workflow = {
        'workflow_code': f"ZENESIS-{experiment_code}",
        'workflow_type': 'ai_segmentation',
        'experiment_id': experiment_code,
        'software_name': 'Zenesis',
        'software_version': '1.0',
        'processing_status': 'completed',
        'parameters': {
            'model_name': 'GroundingDINO + SAM',
            'prompt_text': 'porous ionomer layer',
            'prompt_type': 'text',
            'box_threshold': 0.35,
            'text_threshold': 0.25,
            'human_in_the_loop': True
        },
        'quality_metrics': [
            {'metric_name': 'Dice Score', 'metric_value': str(results.metrics.dice_score)},
            {'metric_name': 'IoU', 'metric_value': str(results.metrics.iou)},
            {'metric_name': 'Accuracy', 'metric_value': str(results.metrics.accuracy)}
        ],
        'segmentation_output': {
            'mask_file': f"zenesis_masks_{sample_id}.zarr",
            'bounding_boxes': [bbox.to_dict() for bbox in results.bboxes],
            'segmentation_metrics': results.metrics.to_dict()
        }
    }

    # Write masks to Silver layer
    (spark.createDataFrame(results.masks)
        .write
        .format("delta")
        .partitionBy("model", "prompt")
        .mode("append")
        .save("s3://lakehouse/silver/segmentations/masks/"))

    # Write workflow metadata
    (spark.createDataFrame([workflow])
        .write
        .format("delta")
        .mode("append")
        .save("s3://lakehouse/silver/metadata/segmentation_workflows/"))

    return workflow

# 3. GOLD: Extract features and aggregate
def extract_features(workflow_code):
    """Gold layer: analytics-ready feature tables"""

    from skimage import measure, morphology

    # Read segmentation from Silver
    masks = (spark.read.format("delta")
        .load("s3://lakehouse/silver/segmentations/masks/")
        .filter(f"workflow_code = '{workflow_code}'"))

    workflow = (spark.read.format("delta")
        .load("s3://lakehouse/silver/metadata/segmentation_workflows/")
        .filter(f"workflow_code = '{workflow_code}'")
        .first())

    experiment_code = workflow['experiment_id']

    # Compute features
    mask_array = masks.select("data").first()["data"]

    # Ionomer coverage
    ionomer_fraction = np.sum(mask_array > 0) / mask_array.size

    # Pore size distribution
    labeled_pores = measure.label(mask_array == 0)
    pore_props = measure.regionprops(labeled_pores)
    pore_sizes = [prop.area for prop in pore_props]

    # Interfacial area
    perimeter = np.sum(morphology.erosion(mask_array) != mask_array)

    feature_table = {
        'workflow_code': workflow_code,
        'experiment_code': experiment_code,
        'sample_id': workflow['sample_id'],
        'ionomer_coverage': float(ionomer_fraction),
        'pore_count': len(pore_sizes),
        'mean_pore_size': float(np.mean(pore_sizes)),
        'std_pore_size': float(np.std(pore_sizes)),
        'interfacial_area': float(perimeter),
        'segmentation_quality': workflow['quality_metrics']
    }

    # Write to Gold layer
    (spark.createDataFrame([feature_table])
        .write
        .format("delta")
        .mode("append")
        .save("s3://lakehouse/gold/feature_tables/ionomer_coverage/"))

    return feature_table

# 4. Query across the lakehouse with schema context
def analyze_catalyst_performance():
    """Cross-layer analytics query"""

    query = """
    SELECT
        s.sample_code,
        s.molecular_composition[0].molecule_name as catalyst_type,
        s.molecular_composition[0].concentration as loading,
        e.detector_settings.bit_depth,
        e.quality_metrics[?(@.metric_name=='Signal-to-Noise Ratio')].metric_value as snr,
        w.quality_metrics[?(@.metric_name=='Dice Score')].metric_value as seg_quality,
        f.ionomer_coverage,
        f.mean_pore_size,
        f.interfacial_area
    FROM delta.`s3://lakehouse/bronze/metadata/lambda-ber-schema/` s
    JOIN delta.`s3://lakehouse/bronze/fib-sem/` raw
        ON s.samples.sample_code = raw.sample_id
    JOIN delta.`s3://lakehouse/silver/metadata/segmentation_workflows/` w
        ON raw.experiment_code = w.experiment_id
    JOIN delta.`s3://lakehouse/gold/feature_tables/ionomer_coverage/` f
        ON w.workflow_code = f.workflow_code
    WHERE w.software_name = 'Zenesis'
      AND w.quality_metrics[?(@.metric_name=='Dice Score')].metric_value > 0.90
    ORDER BY f.ionomer_coverage DESC
    """

    return spark.sql(query)
```

### Real-Time Quality Monitoring Dashboard

Building on Zenesis's evaluation dashboard (Figure 8 in the paper), integrate with lambda-ber-schema for comprehensive monitoring:

```python
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import duckdb

# Connect to lakehouse
con = duckdb.connect()

st.title("Zenesis Segmentation Quality Monitor")

# Query metadata from lambda-ber-schema + results
df = con.execute("""
    SELECT
        w.workflow_code,
        w.start_date::DATE as processing_date,
        e.technique,
        s.sample_code,
        s.sample_type,
        s.molecular_composition[1].molecule_name as material,
        CAST(json_extract(w.quality_metrics,
            '$[?(@.metric_name=="Dice Score")].metric_value') AS FLOAT) as dice,
        CAST(json_extract(w.quality_metrics,
            '$[?(@.metric_name=="IoU")].metric_value') AS FLOAT) as iou,
        CAST(json_extract(w.quality_metrics,
            '$[?(@.metric_name=="Accuracy")].metric_value') AS FLOAT) as accuracy,
        w.parameters.prompt_text as prompt,
        w.parameters.human_in_the_loop as interactive,
        CAST(json_extract(w.quality_metrics,
            '$[?(@.metric_name=="Processing Time")].metric_value') AS FLOAT) as proc_time_min
    FROM read_json_auto('s3://lakehouse/silver/metadata/segmentation_workflows/*.json') w
    JOIN read_json_auto('s3://lakehouse/bronze/metadata/lambda-ber-schema/*.json') schema
        ON w.experiment_id = schema.instrument_runs.experiment_code
    JOIN unnest(schema.samples) s
        ON schema.instrument_runs.sample_id = s.sample_code
    JOIN unnest(schema.instrument_runs) e
        ON w.experiment_id = e.experiment_code
    WHERE w.software_name = 'Zenesis'
      AND w.processing_status = 'completed'
    ORDER BY w.start_date DESC
""").df()

# Overall metrics summary
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Segmentations", len(df))
col2.metric("Avg Dice Score", f"{df['dice'].mean():.3f}")
col3.metric("Avg IoU", f"{df['iou'].mean():.3f}")
col4.metric("Avg Accuracy", f"{df['accuracy'].mean():.3f}")

# Quality distribution by material type
fig1 = px.box(df, x='material', y='dice', color='technique',
              title='Segmentation Quality by Material Type',
              labels={'dice': 'Dice Score', 'material': 'Material'})
st.plotly_chart(fig1)

# Time series of segmentation quality
fig2 = px.scatter(df, x='processing_date', y='dice', color='material',
                  size='iou', hover_data=['workflow_code', 'prompt'],
                  title='Segmentation Quality Over Time')
st.plotly_chart(fig2)

# Interactive vs automated performance comparison
fig3 = go.Figure()
for interactive in [True, False]:
    subset = df[df['interactive'] == interactive]
    fig3.add_trace(go.Box(
        y=subset['dice'],
        name='Interactive' if interactive else 'Fully Automated',
        boxmean='sd'
    ))
fig3.update_layout(title='Impact of Human-in-the-Loop on Quality',
                   yaxis_title='Dice Score')
st.plotly_chart(fig3)

# Processing efficiency
fig4 = px.scatter(df, x='proc_time_min', y='dice', color='technique',
                  hover_data=['sample_code', 'material'],
                  title='Processing Time vs Quality',
                  labels={'proc_time_min': 'Processing Time (min)', 'dice': 'Dice Score'})
st.plotly_chart(fig4)

# Per-sample detailed table
st.subheader("Detailed Results")
st.dataframe(df[['workflow_code', 'sample_code', 'material', 'technique',
                 'dice', 'iou', 'accuracy', 'prompt', 'interactive']]
             .sort_values('dice', ascending=False))
```

## Use Cases Across Imaging Modalities

### 1. Cryo-EM Particle Picking

```yaml
# Cryo-EM single particle workflow
ExperimentRun:
  experiment_code: "CryoEM-20250701-001"
  technique: cryo_em
  sample_id: "Apoferritin-001"
  instrument_id: "Titan-Krios-300kV"
  detector_settings:
    detector_type: "K3 direct electron detector"
    pixel_size: 0.83  # Angstroms/pixel
    total_dose: 50  # e-/Angstrom^2
    number_of_frames: 40

WorkflowRun:
  workflow_code: "PARTICLE-PICK-001"
  workflow_type: "particle_picking"
  software_name: "TOPAZ"  # or "crYOLO" or Zenesis-adapted
  parameters:
    model_name: "TOPAZ-pretrained"
    particle_radius: 100  # Angstroms
    expected_particle_count: 500
    confidence_threshold: 0.5
  quality_metrics:
    - metric_name: "Particles Picked"
      metric_value: "12547"
    - metric_name: "Estimated Precision"
      metric_value: "0.92"
    - metric_name: "Estimated Recall"
      metric_value: "0.88"
```

### 2. X-ray Crystallography Loop Detection

```yaml
# Loop detection for automated mounting
ExperimentRun:
  experiment_code: "XRay-LoopImaging-001"
  technique: loop_imaging
  sample_id: "Lysozyme-Crystal-9B7F"

WorkflowRun:
  workflow_code: "LOOP-DETECT-001"
  workflow_type: "object_detection"
  software_name: "Zenesis"
  parameters:
    model_name: "GroundingDINO + SAM"
    prompt_text: "sample loop with mounted crystal"
    prompt_type: "text"
  segmentation_output:
    bounding_boxes:
      - x_min: 450
        y_min: 320
        x_max: 680
        y_max: 550
        confidence: 0.95
        label: "loop"
      - x_min: 520
        y_min: 410
        x_max: 590
        y_max: 480
        confidence: 0.88
        label: "crystal"
```

### 3. SAXS Background Segmentation

```yaml
# Automated buffer subtraction for SAXS
ExperimentRun:
  experiment_code: "SAXS-20250702-001"
  technique: saxs
  sample_id: "Protein-Complex-A"

WorkflowRun:
  workflow_code: "SAXS-BG-SEG-001"
  workflow_type: "background_segmentation"
  software_name: "Zenesis"
  parameters:
    prompt_text: "scattering signal region"
    artifact_detection_enabled: true
  segmentation_output:
    mask_file: "signal_mask_001.npy"
    segmentation_metrics:
      signal_fraction: 0.65
      artifact_count: 3
```

### 4. Multi-Technique Integrative Study

```yaml
# Same sample analyzed with multiple techniques
Study:
  study_code: "INTEGRATIVE-CATALYST-2025"

  samples:
    - sample_code: "PtRu-Catalyst-001"

  instrument_runs:
    # FIB-SEM for 3D morphology
    - experiment_code: "FIB-SEM-001"
      technique: fib_sem
      sample_id: "PtRu-Catalyst-001"

    # TEM for high-resolution particle imaging
    - experiment_code: "TEM-001"
      technique: tem
      sample_id: "PtRu-Catalyst-001"

    # XRD for crystallographic structure
    - experiment_code: "XRD-001"
      technique: xrd
      sample_id: "PtRu-Catalyst-001"

  workflow_runs:
    # Zenesis for FIB-SEM morphology
    - workflow_code: "ZENESIS-FIB-001"
      experiment_id: "FIB-SEM-001"
      software_name: "Zenesis"
      parameters:
        prompt_text: "catalyst nanoparticles"

    # Zenesis for TEM particle segmentation
    - workflow_code: "ZENESIS-TEM-001"
      experiment_id: "TEM-001"
      software_name: "Zenesis"
      parameters:
        prompt_text: "individual nanoparticle"

    # Integration workflow combining all modalities
    - workflow_code: "CORRELATIVE-ANALYSIS-001"
      workflow_type: "integrative_analysis"
      parent_workflows:
        - "ZENESIS-FIB-001"
        - "ZENESIS-TEM-001"
      parameters:
        correlation_method: "registration-based"
```

## Future Directions

### 1. Active Learning Integration

Incorporate feedback loops where segmentation results inform which samples to image next:

```yaml
ActiveLearningWorkflow:
  attributes:
    uncertainty_threshold:
      range: float
      description: "Confidence below which human review is requested"
    sampling_strategy:
      range: SamplingStrategyEnum
      enum_values: [uncertainty, diversity, expected_improvement]
    feedback_incorporated:
      range: boolean
    retraining_triggered:
      range: boolean
```

### 2. Multi-Modal Foundation Models

Extend to models that jointly process images and other data types:

```yaml
MultiModalModelRun:
  attributes:
    modalities:
      range: ModalityTypeEnum
      multivalued: true
      enum_values: [image, text, spectrum, diffraction_pattern, graph]
    fusion_strategy:
      range: FusionStrategyEnum
      enum_values: [early_fusion, late_fusion, cross_attention]
```

### 3. Federated Learning for Privacy-Sensitive Data

Support collaborative model training across institutions without sharing raw data:

```yaml
FederatedLearningRun:
  attributes:
    participating_institutions:
      range: string
      multivalued: true
    aggregation_method:
      range: string
    privacy_mechanism:
      range: PrivacyMechanismEnum
      enum_values: [differential_privacy, secure_aggregation, homomorphic_encryption]
    local_data_kept_private:
      range: boolean
```

### 4. Explainable AI for Segmentation

Track interpretability methods to understand model decisions:

```yaml
ExplainabilityAnalysis:
  attributes:
    method:
      range: ExplainabilityMethodEnum
      enum_values: [grad_cam, attention_maps, saliency_maps, shap]
    explanation_visualizations:
      range: DataFile
      multivalued: true
    confidence_calibration:
      range: CalibrationMetrics
```

## References

**Foundation Models**

Archit, A., et al. (2025). Segment anything for microscopy. *Nature Methods*, 22(3), 579-591.

Bepler, T., et al. (2019). Positive-unlabeled convolutional neural networks for particle picking in cryo-electron micrographs. *Nature Methods*, 16(11), 1153-1160.

Kirillov, A., et al. (2023). Segment anything. In *Proceedings of the IEEE/CVF International Conference on Computer Vision* (pp. 3899-3910).

Liu, S., et al. (2023). Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection. *arXiv preprint arXiv:2303.05499*.

Ma, J., et al. (2024). Segment anything in medical images. *Nature Communications*, 15(1), 1-9.

Mukherjee, S., et al. (2025). Foundation models for zero-shot segmentation of scientific images without AI-ready data. *arXiv preprint arXiv:2506.24039*.

Ravi, N., et al. (2024). SAM 2: Segment anything in images and videos. *arXiv preprint arXiv:2408.00714*.

Wagner, T., et al. (2019). SPHIRE-crYOLO is a fast and accurate fully automated particle picker for cryo-EM. *Communications Biology*, 2(1), 218.

**Deep Learning Architectures**

Çiçek, Ö., et al. (2016). 3D U-Net: Learning dense volumetric segmentation from sparse annotation. In *International Conference on Medical Image Computing and Computer-Assisted Intervention* (pp. 424-432). Springer.

Ronneberger, O., et al. (2015). U-Net: Convolutional networks for biomedical image segmentation. In *International Conference on Medical Image Computing and Computer-Assisted Intervention* (pp. 234-241). Springer.

**Traditional Methods**

Sigworth, F. J. (2004). Classical detection theory and the cryo-EM particle selection problem. *Journal of Structural Biology*, 145(1-2), 111-122.

Sommer, C., et al. (2011). ilastik: Interactive learning and segmentation toolkit. In *2011 IEEE International Symposium on Biomedical Imaging: From Nano to Macro* (pp. 230-233). IEEE.

**Data Readiness**

Hiniduma, K., Byna, S., & Bez, J. L. (2025). Data readiness for AI: A 360-degree survey. *ACM Computing Surveys*, 57(9).

**Materials Science Applications**

Fornaciari, J. C., et al. (2024). Achieving the hydrogen shot: Interrogating ionomer interfaces. *MRS Energy & Sustainability*, 1-9.

Kwon, O., et al. (2024). Understanding structure differences of iridium oxides depends on loading in proton exchange membrane electrolyzers. *Electrochemical Society Meeting Abstracts*.
