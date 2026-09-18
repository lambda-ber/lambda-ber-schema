# mdoc field comparison

Fields compared across all five mdoc types produced by a SerialEM SPA session.

Files compared:
- **LMM**: `C5_LMM_1.mrc.mdoc` — low-mag atlas montage (Mag=135, 48 tiles)
- **MMM**: `mmm1.mrc.mdoc` — medium-mag grid square survey (Mag=740)
- **Hole**: `Hole_01.mrc.mdoc` — hole-level survey (Mag=11500, integrating)
- **HiMag**: `Hole_01_1-1.mrc.mdoc` — high-mag screening (Mag=130000, integrating)
- **Frame**: `Image_000.tif.mdoc` — dose-fractionated movie (Mag=130000, 49 frames)

| Field | LMM | MMM | Hole | HiMag | Frame |
|-------|-----|-----|------|-------|-------|
| **Provenance & Context** | | | | | |
| `Version` | Y | Y | Y | Y | - |
| `DateTime` | Y | Y | Y | Y | Y |
| `TimeStamp` | Y | Y | Y | Y | Y |
| `NavigatorLabel` | - | Y | Y | Y | Y |
| `ImageFile` | Y | Y | Y | Y | - |
| **Optics** | | | | | |
| `Voltage` | Y | Y | Y | Y | Y |
| `Magnification` | Y | Y | Y | Y | Y |
| `MagIndex` | Y | Y | Y | Y | Y |
| `PixelSpacing` | Y | Y | Y | Y | Y |
| `FilterSlitAndLoss` | Y | Y | Y | Y | Y |
| `ProbeMode` | Y | Y | Y | Y | Y |
| `SpotSize` | Y | Y | Y | Y | Y |
| **Stage** | | | | | |
| `StagePosition` | Y | Y | Y | Y | Y |
| `StageZ` | Y | Y | Y | Y | Y |
| `TiltAngle` | Y | Y | Y | Y | Y |
| `RotationAngle` | Y | Y | Y | Y | Y |
| **Camera & Detector** | | | | | |
| `CameraIndex` | Y | Y | Y | Y | Y |
| `Binning` | Y | Y | Y | Y | Y |
| `DividedBy2` | Y | Y | Y | Y | Y |
| `CountsPerElectron` | Y | Y | Y | Y | Y |
| `OperatingMode` | Y | Y | Y | Y | Y |
| `UsingCDS` | Y | Y | Y | Y | Y |
| **Acquisition Parameters** | | | | | |
| `ExposureTime` | Y | Y | Y | Y | Y |
| `ExposureDose` | Y | Y | Y | Y | Y |
| `DoseRate` | Y | Y | Y | Y | - |
| `Intensity` | Y | Y | Y | Y | Y |
| `LowDoseConSet` | Y | Y | Y | Y | Y |
| **Focus & Alignment** | | | | | |
| `Defocus` | Y | Y | Y | Y | Y |
| `TargetDefocus` | Y | Y | Y | Y | Y |
| `ImageShift` | Y | Y | Y | Y | Y |
| **Frame / Movie Specific** | | | | | |
| `GainReference` | - | - | - | - | Y |
| `DefectFile` | - | - | - | - | Y |
| `SubFramePath` | - | - | - | - | Y |
| `NumSubFrames` | - | - | - | - | Y |
| `FrameDosesAndNumber` | - | - | - | - | Y |
| **Multishot / Hole Targeting** | | | | | |
| `MultishotHoleAndPosition` | - | - | - | Y | - |
| **Montage / Tiling** | | | | | |
| `Montage` | Y | - | - | - | - |
| `PieceSpacing` | Y | - | - | - | - |
| `PieceCoordinates` | Y | - | - | - | - |
| `AlignedPieceCoords` | Y | - | - | - | - |
| `FullMontSize` | Y | - | - | - | - |
| `FullMontNumFrames` | Y | - | - | - | - |
| `PercentileStats` | Y | - | - | - | - |
| `XedgeDxy` | Y | - | - | - | - |
| `XedgeMaxSD` | Y | - | - | - | - |
| `YedgeDxy` | Y | - | - | - | - |
| `YedgeMaxSD` | Y | - | - | - | - |
| **Montage QC / Control (low priority — SerialEM internal)** | | | | | |
| `Alpha` | Y | - | - | - | - |
| `BufISXY` | Y | - | - | - | - |
| `CameraModes` | Y | - | - | - | - |
| `ConSetUsed` | Y | - | - | - | - |
| `DriftSettling` | Y | - | - | - | - |
| `FilterState` | Y | - | - | - | - |
| `FitToPolyID` | Y | - | - | - | - |
| `MontBacklash` | Y | - | - | - | - |
| `MoveStage` | Y | - | - | - | - |
| `ValidBacklash` | Y | - | - | - | - |
| **Image Metadata** | | | | | |
| `ImageSize` | Y | Y | Y | Y | - |
| `UncroppedSize` | Y | Y | Y | Y | Y |
| `DataMode` | Y | Y | Y | Y | - |
| `MinMaxMean` | Y | Y | Y | Y | - |
| `RotationAndFlip` | Y | Y | Y | Y | Y |

## Block Types

The field table above captures only key=value fields. mdoc files also contain block
headers (lines of the form `[BlockType = N]`) that define the type and index of each
data section. Block type is the primary discriminator between integrating and
dose-fractionated acquisition modes.

| Block | LMM | MMM | Hole | HiMag | Frame | Meaning |
|-------|-----|-----|------|-------|-------|---------|
| `[T = ...]` | Y | Y | Y | Y | Y | Free-text comment: microscope name, facility, session timestamp. Not a data block. |
| `[ZValue = N]` | Y | Y | Y | Y | - | One block per image/tile in an MRC stack. N = tile index for montages, always 0 for single images. |
| `[MontSection = N]` | Y | - | - | - | - | One block per montage file summarising the whole mosaic (FullMontSize, tile grid shape, stage params). |
| `[FrameSet = N]` | - | - | - | - | Y | One block per movie file. N is always 0 (one mdoc per tif in this session). |

The block type determines how the mdoc should be parsed:
- **`[ZValue]`** → integrating acquisition (atlas tile, mmm tile, screening image)
- **`[MontSection]`** → montage summary; appears only alongside `[ZValue]` blocks in montage mdocs
- **`[FrameSet]`** → dose-fractionated movie
