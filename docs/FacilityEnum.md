# Enum: FacilityEnum 




_Major synchrotron and structural biology research facilities worldwide_



URI: [lambdaber:FacilityEnum](https://w3id.org/lambda-ber-schema/FacilityEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| NSLS_II | ROR:01q47ea17 | Fourth-generation synchrotron light source at Brookhaven National Laboratory,... |
| ALS | None | Third-generation synchrotron light source at Lawrence Berkeley National Labor... |
| SSRL | None | Synchrotron radiation facility at SLAC National Accelerator Laboratory, Menlo... |
| ESRF | ROR:02550n020 | High-energy synchrotron facility in Grenoble, France - world's most intense X... |
| DIAMOND | ROR:05etxs293 | UK's national synchrotron science facility at Harwell Science and Innovation ... |
| PHOTON_FACTORY | None | Synchrotron radiation facility at KEK (High Energy Accelerator Research Organ... |
| APS | None | High-energy synchrotron at Argonne National Laboratory, Lemont, IL, USA |
| SPRING8 | None | Large-scale synchrotron radiation facility in Harima Science Park City, Hyogo... |
| PETRA_III | None | High-brilliance synchrotron radiation source at DESY, Hamburg, Germany |
| SOLEIL | ROR:01ydb3330 | French national synchrotron facility near Paris, France |
| AUSTRALIAN_SYNCHROTRON | ROR:03vk18a84 | Australia's national synchrotron facility in Melbourne, Victoria |
| SIBYLS | None | Integrated structural biology beamline at ALS for SAXS, X-ray crystallography... |








## Comments

* This enum provides standardized identifiers for major facilities with rich metadata
* ROR (Research Organization Registry) IDs provide persistent organizational identifiers
* Not currently bound to any slots - available for future use

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: FacilityEnum
description: Major synchrotron and structural biology research facilities worldwide
comments:
- This enum provides standardized identifiers for major facilities with rich metadata
- ROR (Research Organization Registry) IDs provide persistent organizational identifiers
- Not currently bound to any slots - available for future use
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
  NSLS_II:
    text: NSLS_II
    description: Fourth-generation synchrotron light source at Brookhaven National
      Laboratory, Upton, NY, USA
    meaning: ROR:01q47ea17
    annotations:
      parent_organization:
        tag: parent_organization
        value: Brookhaven National Laboratory
      parent_ror:
        tag: parent_ror
        value: ROR:02ex6cf31
      location:
        tag: location
        value: Upton, New York, USA
      country:
        tag: country
        value: USA
      doe_facility:
        tag: doe_facility
        value: 'true'
      doe_office:
        tag: doe_office
        value: Office of Science
      wikidata_id:
        tag: wikidata_id
        value: Q30270543
      energy_gev:
        tag: energy_gev
        value: '3.0'
      operational_since:
        tag: operational_since
        value: '2015'
      beamlines_count:
        tag: beamlines_count
        value: '28'
      website:
        tag: website
        value: https://www.bnl.gov/nsls2/
    title: National Synchrotron Light Source II
    aliases:
    - NSLS-II
    - NSLS2
  ALS:
    text: ALS
    description: Third-generation synchrotron light source at Lawrence Berkeley National
      Laboratory, Berkeley, CA, USA
    annotations:
      parent_organization:
        tag: parent_organization
        value: Lawrence Berkeley National Laboratory
      parent_ror:
        tag: parent_ror
        value: ROR:02jbv0t02
      location:
        tag: location
        value: Berkeley, California, USA
      country:
        tag: country
        value: USA
      doe_facility:
        tag: doe_facility
        value: 'true'
      doe_office:
        tag: doe_office
        value: Office of Science
      wikidata_id:
        tag: wikidata_id
        value: Q4685011
      energy_gev:
        tag: energy_gev
        value: '1.9'
      operational_since:
        tag: operational_since
        value: '1993'
      website:
        tag: website
        value: https://als.lbl.gov/
    title: Advanced Light Source
    aliases:
    - Advanced Light Source
    - ALS Berkeley
  SSRL:
    text: SSRL
    description: Synchrotron radiation facility at SLAC National Accelerator Laboratory,
      Menlo Park, CA, USA
    annotations:
      parent_organization:
        tag: parent_organization
        value: SLAC National Accelerator Laboratory
      parent_ror:
        tag: parent_ror
        value: ROR:05gzmn429
      location:
        tag: location
        value: Menlo Park, California, USA
      country:
        tag: country
        value: USA
      doe_facility:
        tag: doe_facility
        value: 'true'
      doe_office:
        tag: doe_office
        value: Office of Science
      wikidata_id:
        tag: wikidata_id
        value: Q7598571
      energy_gev:
        tag: energy_gev
        value: '3.0'
      operational_since:
        tag: operational_since
        value: '1974'
      website:
        tag: website
        value: https://www-ssrl.slac.stanford.edu/
    title: Stanford Synchrotron Radiation Lightsource
    aliases:
    - Stanford Synchrotron Radiation Lightsource
    - Stanford Synchrotron
  ESRF:
    text: ESRF
    description: High-energy synchrotron facility in Grenoble, France - world's most
      intense X-ray source
    meaning: ROR:02550n020
    annotations:
      location:
        tag: location
        value: Grenoble, France
      country:
        tag: country
        value: France
      doe_facility:
        tag: doe_facility
        value: 'false'
      wikidata_id:
        tag: wikidata_id
        value: Q1163036
      energy_gev:
        tag: energy_gev
        value: '6.0'
      operational_since:
        tag: operational_since
        value: '1994'
      upgrade:
        tag: upgrade
        value: Extremely Brilliant Source (EBS) 2020
      partner_countries:
        tag: partner_countries
        value: '22'
      website:
        tag: website
        value: https://www.esrf.fr/
    title: European Synchrotron Radiation Facility
    aliases:
    - European Synchrotron
    - ESRF-EBS
  DIAMOND:
    text: DIAMOND
    description: UK's national synchrotron science facility at Harwell Science and
      Innovation Campus, Oxfordshire, UK
    meaning: ROR:05etxs293
    annotations:
      location:
        tag: location
        value: Harwell, Oxfordshire, UK
      country:
        tag: country
        value: United Kingdom
      doe_facility:
        tag: doe_facility
        value: 'false'
      wikidata_id:
        tag: wikidata_id
        value: Q652731
      energy_gev:
        tag: energy_gev
        value: '3.0'
      operational_since:
        tag: operational_since
        value: '2007'
      beamlines_count:
        tag: beamlines_count
        value: '32'
      website:
        tag: website
        value: https://www.diamond.ac.uk/
    title: Diamond Light Source
    aliases:
    - Diamond
    - Diamond Synchrotron
  PHOTON_FACTORY:
    text: PHOTON_FACTORY
    description: Synchrotron radiation facility at KEK (High Energy Accelerator Research
      Organization), Tsukuba, Japan
    annotations:
      parent_organization:
        tag: parent_organization
        value: High Energy Accelerator Research Organization (KEK)
      parent_ror:
        tag: parent_ror
        value: ROR:01g5y5k24
      location:
        tag: location
        value: Tsukuba, Ibaraki, Japan
      country:
        tag: country
        value: Japan
      doe_facility:
        tag: doe_facility
        value: 'false'
      wikidata_id:
        tag: wikidata_id
        value: Q7187717
      energy_gev:
        tag: energy_gev
        value: '2.5'
      operational_since:
        tag: operational_since
        value: '1982'
      website:
        tag: website
        value: https://www2.kek.jp/imss/pf/
    title: Photon Factory
    aliases:
    - PF
    - KEK Photon Factory
  APS:
    text: APS
    description: High-energy synchrotron at Argonne National Laboratory, Lemont, IL,
      USA
    annotations:
      parent_organization:
        tag: parent_organization
        value: Argonne National Laboratory
      parent_ror:
        tag: parent_ror
        value: ROR:05gvnxz63
      location:
        tag: location
        value: Lemont, Illinois, USA
      country:
        tag: country
        value: USA
      doe_facility:
        tag: doe_facility
        value: 'true'
      doe_office:
        tag: doe_office
        value: Office of Science
      wikidata_id:
        tag: wikidata_id
        value: Q2824628
      energy_gev:
        tag: energy_gev
        value: '7.0'
      operational_since:
        tag: operational_since
        value: '1996'
      upgrade:
        tag: upgrade
        value: APS-U upgrade 2024
      website:
        tag: website
        value: https://www.aps.anl.gov/
    title: Advanced Photon Source
    aliases:
    - Advanced Photon Source
    - Argonne APS
  SPRING8:
    text: SPRING8
    description: Large-scale synchrotron radiation facility in Harima Science Park
      City, Hyogo, Japan
    annotations:
      parent_organization:
        tag: parent_organization
        value: Japan Synchrotron Radiation Research Institute (JASRI)
      parent_ror:
        tag: parent_ror
        value: ROR:01xjv7358
      location:
        tag: location
        value: Sayo, Hyogo, Japan
      country:
        tag: country
        value: Japan
      doe_facility:
        tag: doe_facility
        value: 'false'
      wikidata_id:
        tag: wikidata_id
        value: Q1196821
      energy_gev:
        tag: energy_gev
        value: '8.0'
      operational_since:
        tag: operational_since
        value: '1997'
      website:
        tag: website
        value: http://www.spring8.or.jp/
    title: SPring-8
    aliases:
    - SPring-8
    - Super Photon ring-8 GeV
  PETRA_III:
    text: PETRA_III
    description: High-brilliance synchrotron radiation source at DESY, Hamburg, Germany
    annotations:
      parent_organization:
        tag: parent_organization
        value: Deutsches Elektronen-Synchrotron (DESY)
      parent_ror:
        tag: parent_ror
        value: ROR:01js2sh04
      location:
        tag: location
        value: Hamburg, Germany
      country:
        tag: country
        value: Germany
      doe_facility:
        tag: doe_facility
        value: 'false'
      wikidata_id:
        tag: wikidata_id
        value: Q1754942
      energy_gev:
        tag: energy_gev
        value: '6.0'
      operational_since:
        tag: operational_since
        value: '2009'
      website:
        tag: website
        value: https://photon-science.desy.de/facilities/petra_iii/
    title: PETRA III
    aliases:
    - PETRA III
    - PETRA3
  SOLEIL:
    text: SOLEIL
    description: French national synchrotron facility near Paris, France
    meaning: ROR:01ydb3330
    annotations:
      location:
        tag: location
        value: Saint-Aubin, France
      country:
        tag: country
        value: France
      doe_facility:
        tag: doe_facility
        value: 'false'
      wikidata_id:
        tag: wikidata_id
        value: Q1414116
      energy_gev:
        tag: energy_gev
        value: '2.75'
      operational_since:
        tag: operational_since
        value: '2008'
      website:
        tag: website
        value: https://www.synchrotron-soleil.fr/
    title: Synchrotron SOLEIL
    aliases:
    - SOLEIL
    - Synchrotron SOLEIL
  AUSTRALIAN_SYNCHROTRON:
    text: AUSTRALIAN_SYNCHROTRON
    description: Australia's national synchrotron facility in Melbourne, Victoria
    meaning: ROR:03vk18a84
    annotations:
      location:
        tag: location
        value: Melbourne, Victoria, Australia
      country:
        tag: country
        value: Australia
      doe_facility:
        tag: doe_facility
        value: 'false'
      wikidata_id:
        tag: wikidata_id
        value: Q782691
      energy_gev:
        tag: energy_gev
        value: '3.0'
      operational_since:
        tag: operational_since
        value: '2007'
      website:
        tag: website
        value: https://www.synchrotron.org.au/
    title: Australian Synchrotron
    aliases:
    - Australian Synchrotron
    - AS
  SIBYLS:
    text: SIBYLS
    description: Integrated structural biology beamline at ALS for SAXS, X-ray crystallography,
      and fiber diffraction
    annotations:
      parent_facility:
        tag: parent_facility
        value: Advanced Light Source
      parent_ror:
        tag: parent_ror
        value: ROR:02jbv0t02
      location:
        tag: location
        value: Berkeley, California, USA
      country:
        tag: country
        value: USA
      doe_facility:
        tag: doe_facility
        value: 'true'
      doe_office:
        tag: doe_office
        value: Office of Science - Biological and Environmental Research
      beamline_id:
        tag: beamline_id
        value: 12.3.1
      techniques:
        tag: techniques
        value: SAXS, MX, fiber diffraction
      website:
        tag: website
        value: https://bl1231.als.lbl.gov/
    title: SIBYLS Beamline 12.3.1
    aliases:
    - SIBYLS
    - ALS 12.3.1
    - Beamline 12.3.1

```
</details>