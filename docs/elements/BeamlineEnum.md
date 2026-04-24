# Enum: BeamlineEnum 




_Specific beamline instances at DOE and other major structural biology facilities_



URI: [lambda:BeamlineEnum](http://w3id.org/lambda/BeamlineEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ALS_SIBYLS | None | Structurally Integrated Biology for Life Sciences - dual SAXS/WAXS and macrom... |
| ALS_BL501 | None | Protein crystallography beamline at the Advanced Light Source |
| ALS_BL502 | None | Protein crystallography beamline at the Advanced Light Source |
| ALS_BL821 | None | Protein crystallography beamline at the Advanced Light Source |
| ALS_BL822 | None | Protein crystallography beamline at the Advanced Light Source |
| ALS_BL831 | None | High-throughput macromolecular crystallography beamline |
| ALS_BL832 | None | Hard X-ray micro-tomography beamline for non-destructive 3D imaging |
| ALS_BL1222 | None | High-throughput macromolecular crystallography beamline |
| NSLS2_FMX | None | Frontier Microfocus Macromolecular Crystallography beamline for challenging s... |
| NSLS2_AMX | None | Automated Macromolecular Crystallography beamline for high-throughput structu... |
| NSLS2_NYX | None | Newest crystallography beamline for rapid data collection |
| NSLS2_LIX | None | Life Science X-ray Scattering beamline for solution SAXS/WAXS |
| APS_GMCA_23IDB | None | General Medical Sciences and Cancer Institutes Collaborative Access Team - mi... |
| APS_GMCA_23IDD | None | General Medical Sciences and Cancer Institutes Collaborative Access Team - st... |
| APS_LSCAT_21ID | None | Life Sciences Collaborative Access Team beamline |
| APS_NECAT_24IDC | None | Northeastern Collaborative Access Team - microfocus beamline |
| APS_NECAT_24IDE | None | Northeastern Collaborative Access Team - standard beamline |
| APS_SERCAT_22ID | None | Southeast Regional Collaborative Access Team - insertion device beamline |
| APS_SERCAT_22BM | None | Southeast Regional Collaborative Access Team - bending magnet beamline |
| APS_SBCCAT_19ID | None | Structural Biology Center Collaborative Access Team beamline |
| APS_BIOCARS_14ID | None | Center for Advanced Radiation Sources - time-resolved crystallography |
| APS_BIOCAT_18ID | None | Biophysics Collaborative Access Team - fiber diffraction and SAXS |
| APS_IMCACAT_17ID | None | Industrial Macromolecular Crystallography Association Collaborative Access Te... |
| SSRL_BL92 | None | Macromolecular crystallography beamline at Stanford Synchrotron Radiation Lig... |
| SSRL_BL122 | None | Solution scattering beamline for SAXS/WAXS at Stanford Synchrotron Radiation ... |
| SSRL_BL141 | None | Macromolecular crystallography beamline at Stanford Synchrotron Radiation Lig... |
| SNS_MANDI | None | Macromolecular Neutron Diffractometer for neutron protein crystallography |
| HFIR_IMAGINE | None | Image plate single crystal diffractometer for neutron protein crystallography |
| SNS_BIOSANS | None | Biological Small-Angle Neutron Scattering instrument |
| SNS_EQSANS | None | Extended Q-Range Small-Angle Neutron Scattering instrument |








## Comments

* Each beamline is annotated with its parent facility from FacilityEnum
* Focus on beamlines used for structural biology (MX, SAXS/WAXS, neutron scattering)
* Beamline IDs follow facility-specific conventions

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: BeamlineEnum
description: Specific beamline instances at DOE and other major structural biology
  facilities
comments:
- Each beamline is annotated with its parent facility from FacilityEnum
- Focus on beamlines used for structural biology (MX, SAXS/WAXS, neutron scattering)
- Beamline IDs follow facility-specific conventions
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  ALS_SIBYLS:
    text: ALS_SIBYLS
    description: Structurally Integrated Biology for Life Sciences - dual SAXS/WAXS
      and macromolecular crystallography beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:ALS
      beamline_id:
        tag: beamline_id
        value: 12.3.1
      techniques:
        tag: techniques
        value: TechniqueEnum:saxs|TechniqueEnum:waxs|TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      mail_in_service:
        tag: mail_in_service
        value: 'true'
      website:
        tag: website
        value: https://sibyls.als.lbl.gov/
      operational_since:
        tag: operational_since
        value: '2004'
    title: SIBYLS (BL12.3.1)
    aliases:
    - SIBYLS
    - BL12.3.1
    - ALS 12.3.1
  ALS_BL501:
    text: ALS_BL501
    description: Protein crystallography beamline at the Advanced Light Source
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:ALS
      beamline_id:
        tag: beamline_id
        value: 5.0.1
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
    title: ALS BL5.0.1
    aliases:
    - BL5.0.1
  ALS_BL502:
    text: ALS_BL502
    description: Protein crystallography beamline at the Advanced Light Source
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:ALS
      beamline_id:
        tag: beamline_id
        value: 5.0.2
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
    title: ALS BL5.0.2
    aliases:
    - BL5.0.2
  ALS_BL821:
    text: ALS_BL821
    description: Protein crystallography beamline at the Advanced Light Source
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:ALS
      beamline_id:
        tag: beamline_id
        value: 8.2.1
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
    title: ALS BL8.2.1
    aliases:
    - BL8.2.1
  ALS_BL822:
    text: ALS_BL822
    description: Protein crystallography beamline at the Advanced Light Source
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:ALS
      beamline_id:
        tag: beamline_id
        value: 8.2.2
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
    title: ALS BL8.2.2
    aliases:
    - BL8.2.2
  ALS_BL831:
    text: ALS_BL831
    description: High-throughput macromolecular crystallography beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:ALS
      beamline_id:
        tag: beamline_id
        value: 8.3.1
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      mail_in_service:
        tag: mail_in_service
        value: 'true'
    title: ALS BL8.3.1
    aliases:
    - BL8.3.1
  ALS_BL832:
    text: ALS_BL832
    description: Hard X-ray micro-tomography beamline for non-destructive 3D imaging.
      Provides high-resolution micro-CT capabilities for biological, geological, and
      materials samples. Supports absorption and phase contrast imaging modes.
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:ALS
      beamline_id:
        tag: beamline_id
        value: 8.3.2
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_tomography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://microct.lbl.gov/
    title: ALS BL8.3.2
    aliases:
    - BL8.3.2
    - microCT
  ALS_BL1222:
    text: ALS_BL1222
    description: High-throughput macromolecular crystallography beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:ALS
      beamline_id:
        tag: beamline_id
        value: 12.2.2
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
    title: ALS BL12.2.2
    aliases:
    - BL12.2.2
  NSLS2_FMX:
    text: NSLS2_FMX
    description: Frontier Microfocus Macromolecular Crystallography beamline for challenging
      small crystals
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:NSLS_II
      beamline_id:
        tag: beamline_id
        value: 17-ID-1
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.bnl.gov/nsls2/beamlines/beamline.php?r=17-ID-1
      operational_since:
        tag: operational_since
        value: '2016'
    title: FMX (17-ID-1)
    aliases:
    - FMX
    - 17-ID-1
  NSLS2_AMX:
    text: NSLS2_AMX
    description: Automated Macromolecular Crystallography beamline for high-throughput
      structure determination
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:NSLS_II
      beamline_id:
        tag: beamline_id
        value: 17-ID-2
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.bnl.gov/nsls2/beamlines/beamline.php?r=17-ID-2
      operational_since:
        tag: operational_since
        value: '2016'
    title: AMX (17-ID-2)
    aliases:
    - AMX
    - 17-ID-2
  NSLS2_NYX:
    text: NSLS2_NYX
    description: Newest crystallography beamline for rapid data collection
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:NSLS_II
      beamline_id:
        tag: beamline_id
        value: 19-ID
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
    title: NYX (19-ID)
    aliases:
    - NYX
    - 19-ID
  NSLS2_LIX:
    text: NSLS2_LIX
    description: Life Science X-ray Scattering beamline for solution SAXS/WAXS
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:NSLS_II
      beamline_id:
        tag: beamline_id
        value: 16-ID
      techniques:
        tag: techniques
        value: TechniqueEnum:saxs|TechniqueEnum:waxs
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.bnl.gov/nsls2/beamlines/beamline.php?r=16-ID
    title: LiX (16-ID)
    aliases:
    - LiX
    - 16-ID
  APS_GMCA_23IDB:
    text: APS_GMCA_23IDB
    description: General Medical Sciences and Cancer Institutes Collaborative Access
      Team - microfocus beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 23-ID-B
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.gmca.anl.gov/
    title: GM/CA 23-ID-B
    aliases:
    - GM/CA-B
    - 23-ID-B
  APS_GMCA_23IDD:
    text: APS_GMCA_23IDD
    description: General Medical Sciences and Cancer Institutes Collaborative Access
      Team - standard beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 23-ID-D
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.gmca.anl.gov/
    title: GM/CA 23-ID-D
    aliases:
    - GM/CA-D
    - 23-ID-D
  APS_LSCAT_21ID:
    text: APS_LSCAT_21ID
    description: Life Sciences Collaborative Access Team beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 21-ID
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://ls-cat.org/
    title: LS-CAT (21-ID)
    aliases:
    - LS-CAT
    - 21-ID
  APS_NECAT_24IDC:
    text: APS_NECAT_24IDC
    description: Northeastern Collaborative Access Team - microfocus beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 24-ID-C
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://necat.chem.cornell.edu/
    title: NE-CAT 24-ID-C
    aliases:
    - NE-CAT-C
    - 24-ID-C
  APS_NECAT_24IDE:
    text: APS_NECAT_24IDE
    description: Northeastern Collaborative Access Team - standard beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 24-ID-E
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://necat.chem.cornell.edu/
    title: NE-CAT 24-ID-E
    aliases:
    - NE-CAT-E
    - 24-ID-E
  APS_SERCAT_22ID:
    text: APS_SERCAT_22ID
    description: Southeast Regional Collaborative Access Team - insertion device beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 22-ID
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.ser-cat.org/
    title: SER-CAT (22-ID)
    aliases:
    - SER-CAT
    - 22-ID
  APS_SERCAT_22BM:
    text: APS_SERCAT_22BM
    description: Southeast Regional Collaborative Access Team - bending magnet beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 22-BM
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.ser-cat.org/
    title: SER-CAT (22-BM)
    aliases:
    - SER-CAT-BM
    - 22-BM
  APS_SBCCAT_19ID:
    text: APS_SBCCAT_19ID
    description: Structural Biology Center Collaborative Access Team beamline
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 19-ID
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.anl.gov/sbc
    title: SBC-CAT (19-ID)
    aliases:
    - SBC-CAT
    - 19-ID
  APS_BIOCARS_14ID:
    text: APS_BIOCARS_14ID
    description: Center for Advanced Radiation Sources - time-resolved crystallography
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 14-ID
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography|TechniqueEnum:time_resolved_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://biocars.uchicago.edu/
    title: BioCARS (14-ID)
    aliases:
    - BioCARS
    - 14-ID
  APS_BIOCAT_18ID:
    text: APS_BIOCAT_18ID
    description: Biophysics Collaborative Access Team - fiber diffraction and SAXS
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 18-ID
      techniques:
        tag: techniques
        value: TechniqueEnum:saxs|TechniqueEnum:fiber_diffraction
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www.bio.aps.anl.gov/
    title: BioCAT (18-ID)
    aliases:
    - BioCAT
    - 18-ID
  APS_IMCACAT_17ID:
    text: APS_IMCACAT_17ID
    description: Industrial Macromolecular Crystallography Association Collaborative
      Access Team
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:APS
      beamline_id:
        tag: beamline_id
        value: 17-ID
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
    title: IMCA-CAT (17-ID)
    aliases:
    - IMCA-CAT
    - 17-ID
  SSRL_BL92:
    text: SSRL_BL92
    description: Macromolecular crystallography beamline at Stanford Synchrotron Radiation
      Lightsource
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:SSRL
      beamline_id:
        tag: beamline_id
        value: 9-2
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www-ssrl.slac.stanford.edu/smb/
    title: SSRL BL9-2
    aliases:
    - BL9-2
    - SSRL 9-2
  SSRL_BL122:
    text: SSRL_BL122
    description: Solution scattering beamline for SAXS/WAXS at Stanford Synchrotron
      Radiation Lightsource
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:SSRL
      beamline_id:
        tag: beamline_id
        value: 12-2
      techniques:
        tag: techniques
        value: TechniqueEnum:saxs|TechniqueEnum:waxs
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www-ssrl.slac.stanford.edu/smb/
    title: SSRL BL12-2
    aliases:
    - BL12-2
    - SSRL 12-2
  SSRL_BL141:
    text: SSRL_BL141
    description: Macromolecular crystallography beamline at Stanford Synchrotron Radiation
      Lightsource
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:SSRL
      beamline_id:
        tag: beamline_id
        value: 14-1
      techniques:
        tag: techniques
        value: TechniqueEnum:xray_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://www-ssrl.slac.stanford.edu/smb/
    title: SSRL BL14-1
    aliases:
    - BL14-1
    - SSRL 14-1
  SNS_MANDI:
    text: SNS_MANDI
    description: Macromolecular Neutron Diffractometer for neutron protein crystallography
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:SNS
      beamline_id:
        tag: beamline_id
        value: BL-11B
      techniques:
        tag: techniques
        value: TechniqueEnum:neutron_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://neutrons.ornl.gov/mandi
    title: MaNDi
    aliases:
    - MaNDi
    - BL-11B
  HFIR_IMAGINE:
    text: HFIR_IMAGINE
    description: Image plate single crystal diffractometer for neutron protein crystallography
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:HFIR
      beamline_id:
        tag: beamline_id
        value: CG-4D
      techniques:
        tag: techniques
        value: TechniqueEnum:neutron_crystallography
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://neutrons.ornl.gov/imagine
    title: IMAGINE
    aliases:
    - IMAGINE
    - CG-4D
  SNS_BIOSANS:
    text: SNS_BIOSANS
    description: Biological Small-Angle Neutron Scattering instrument
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:HFIR
      beamline_id:
        tag: beamline_id
        value: CG-3
      techniques:
        tag: techniques
        value: TechniqueEnum:sans
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://neutrons.ornl.gov/bio-sans
    title: Bio-SANS
    aliases:
    - Bio-SANS
    - CG-3
  SNS_EQSANS:
    text: SNS_EQSANS
    description: Extended Q-Range Small-Angle Neutron Scattering instrument
    annotations:
      facility:
        tag: facility
        value: FacilityEnum:SNS
      beamline_id:
        tag: beamline_id
        value: BL-6
      techniques:
        tag: techniques
        value: TechniqueEnum:sans
      doe_beamline:
        tag: doe_beamline
        value: 'true'
      website:
        tag: website
        value: https://neutrons.ornl.gov/eqsans
    title: EQ-SANS
    aliases:
    - EQ-SANS
    - BL-6

```
</details>