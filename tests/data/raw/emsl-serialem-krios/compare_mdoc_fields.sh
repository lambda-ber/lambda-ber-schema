#!/usr/bin/env bash
# Generates a markdown table comparing metadata fields across mdoc types.
# Usage: bash compare_mdoc_fields.sh > mdoc_field_comparison.md

BASE="$(dirname "$0")"

LMM="$BASE/C5_LMM_1.mrc.mdoc"
MMM="$BASE/mmm1.mrc.mdoc"
HOLE="$BASE/screening/Hole_01.mrc.mdoc"
HIMAG="$BASE/screening/Hole_01_1-1.mrc.mdoc"
FRAME="$BASE/frames/Image_000.tif.mdoc"

# Check presence: print Y or -
present() {
    local field="$1" file="$2"
    grep -qP "^${field} =" "$file" && echo "Y" || echo "-"
}

# Emit one table row
row() {
    local field="$1"
    local lmm mmm hole himag frame
    lmm=$(present "$field" "$LMM")
    mmm=$(present "$field" "$MMM")
    hole=$(present "$field" "$HOLE")
    himag=$(present "$field" "$HIMAG")
    frame=$(present "$field" "$FRAME")
    echo "| \`$field\` | $lmm | $mmm | $hole | $himag | $frame |"
}

# Category header row
header() {
    echo "| **$1** | | | | | |"
}

echo "# mdoc field comparison"
echo ""
echo "Fields compared across all five mdoc types produced by a SerialEM SPA session."
echo ""
echo "Files compared:"
echo "- **LMM**: \`C5_LMM_1.mrc.mdoc\` — low-mag atlas montage (Mag=135, 48 tiles)"
echo "- **MMM**: \`mmm1.mrc.mdoc\` — medium-mag grid square survey (Mag=740)"
echo "- **Hole**: \`Hole_01.mrc.mdoc\` — hole-level survey (Mag=11500, integrating)"
echo "- **HiMag**: \`Hole_01_1-1.mrc.mdoc\` — high-mag screening (Mag=130000, integrating)"
echo "- **Frame**: \`Image_000.tif.mdoc\` — dose-fractionated movie (Mag=130000, 49 frames)"
echo ""
echo "| Field | LMM | MMM | Hole | HiMag | Frame |"
echo "|-------|-----|-----|------|-------|-------|"

header "Provenance & Context"
for f in Version DateTime TimeStamp NavigatorLabel ImageFile; do row "$f"; done

header "Optics"
for f in Voltage Magnification MagIndex PixelSpacing FilterSlitAndLoss ProbeMode SpotSize; do row "$f"; done

header "Stage"
for f in StagePosition StageZ TiltAngle RotationAngle; do row "$f"; done

header "Camera & Detector"
for f in CameraIndex Binning DividedBy2 CountsPerElectron OperatingMode UsingCDS; do row "$f"; done

header "Acquisition Parameters"
for f in ExposureTime ExposureDose DoseRate Intensity LowDoseConSet; do row "$f"; done

header "Focus & Alignment"
for f in Defocus TargetDefocus ImageShift; do row "$f"; done

header "Frame / Movie Specific"
for f in GainReference DefectFile SubFramePath NumSubFrames FrameDosesAndNumber; do row "$f"; done

header "Multishot / Hole Targeting"
for f in MultishotHoleAndPosition; do row "$f"; done

header "Montage / Tiling"
for f in Montage PieceSpacing PieceCoordinates AlignedPieceCoords FullMontSize FullMontNumFrames PercentileStats XedgeDxy XedgeMaxSD YedgeDxy YedgeMaxSD; do row "$f"; done

header "Montage QC / Control (low priority — SerialEM internal)"
for f in Alpha BufISXY CameraModes ConSetUsed DriftSettling FilterState FitToPolyID MontBacklash MoveStage ValidBacklash; do row "$f"; done

header "Image Metadata"
for f in ImageSize UncroppedSize DataMode MinMaxMean RotationAndFlip; do row "$f"; done

echo ""
echo "## Block Types"
echo ""
echo "The field table above captures only key=value fields. mdoc files also contain block"
echo "headers (lines of the form \`[BlockType = N]\`) that define the type and index of each"
echo "data section. Block type is the primary discriminator between integrating and"
echo "dose-fractionated acquisition modes."
echo ""
echo "| Block | LMM | MMM | Hole | HiMag | Frame | Meaning |"
echo "|-------|-----|-----|------|-------|-------|---------|"
echo "| \`[T = ...]\` | Y | Y | Y | Y | Y | Free-text comment: microscope name, facility, session timestamp. Not a data block. |"
echo "| \`[ZValue = N]\` | Y | Y | Y | Y | - | One block per image/tile in an MRC stack. N = tile index for montages, always 0 for single images. |"
echo "| \`[MontSection = N]\` | Y | - | - | - | - | One block per montage file summarising the whole mosaic (FullMontSize, tile grid shape, stage params). |"
echo "| \`[FrameSet = N]\` | - | - | - | - | Y | One block per movie file. N is always 0 (one mdoc per tif in this session). |"
echo ""
echo "The block type determines how the mdoc should be parsed:"
echo "- **\`[ZValue]\`** → integrating acquisition (atlas tile, mmm tile, screening image)"
echo "- **\`[MontSection]\`** → montage summary; appears only alongside \`[ZValue]\` blocks in montage mdocs"
echo "- **\`[FrameSet]\`** → dose-fractionated movie"
