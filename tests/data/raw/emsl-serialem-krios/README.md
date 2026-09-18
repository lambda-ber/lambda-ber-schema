# Fixture: emsl-serialem-krios

Representative subset of a SerialEM single-particle cryo-EM session from a Titan Krios.
Mirrors the directory structure and file types of a real EMSL acquisition archive.
Identifying information has been genericized. Large binary files (`.mrc`, `.tif`, `.dm4`)
are zero-byte stubs; all sidecar text files (`.mdoc`, `.nav`, `.txt`) are real content.

---

```
emsl-serialem-krios/
│
│  C5_LMM_1.mrc          stub  Low-magnification atlas montage of grid square C5 (48 tiles, Mag=135)
│  C5_LMM_1.mrc.mdoc     real  Per-tile metadata for the atlas; one [ZValue=N] block per tile
│  C5.nav                real  SerialEM navigator: all acquisition targets as [Item=N] blocks with stage coords and map references
│  mmm1.mrc              stub  Medium-magnification survey image of grid area 1 (Mag=740)
│  mmm1.mrc.mdoc         real  Metadata for mmm1; one [ZValue=0] block
│  mmm2.mrc              stub  Medium-magnification survey image of grid area 2
│  mmm2.mrc.mdoc         real  Metadata for mmm2
│
├─ frames/
│   Image_000.tif        stub  Dose-fractionated movie for acquisition target 0 (49 frames, Mag=130000)
│   Image_000.tif.mdoc   real  Per-movie metadata; [FrameSet=0] block with NumSubFrames, SubFramePath, GainReference, DefectFile
│   Image_001.tif        stub  Movie for target 1
│   Image_001.tif.mdoc   real  Per-movie metadata for Image_001
│   Image_002.tif        stub  Movie for target 2
│   Image_002.tif.mdoc   real  Per-movie metadata for Image_002
│   SuperRef_Image_000.dm4  stub  Gain reference in DigitalMicrograph 4 format; normalizes camera sensitivity; referenced by all frame mdocs
│   defects_GS_01_H_01_000.txt  real  Camera defect map (bad columns, unusable areas); referenced by all frame mdocs
│
└─ screening/
    Hole_01.mrc          stub  Hole-level survey image at medium mag (Mag=11500) to assess ice/particle quality
    Hole_01.mrc.mdoc     real  Metadata for Hole_01 survey
    Hole_01_1-1.mrc      stub  High-mag image of multishot sub-position 1-1 within hole 1 (Mag=130000)
    Hole_01_1-1.mrc.mdoc real  Metadata for Hole_01_1-1; includes MultishotHoleAndPosition field
```
