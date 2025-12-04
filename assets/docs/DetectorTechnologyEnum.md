
# Enum: DetectorTechnologyEnum

Generic detector technologies for structural biology imaging

URI: [lambdaber:DetectorTechnologyEnum](https://w3id.org/lambda-ber-schema/DetectorTechnologyEnum)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| direct_electron_detector | Direct electron detector for cryo-EM (e.g., Gatan K2/K3, ThermoFisher Falcon, DirectElectron DE-64) |  | {'comments': ['Modern cryo-EM detectors with direct electron counting capability']} |
| ccd | Charge-coupled device camera |  | {'comments': ['Used in both cryo-EM (older systems) and X-ray crystallography']} |
| cmos | Complementary metal-oxide-semiconductor detector |  | {'comments': ['Used in both cryo-EM and X-ray crystallography (e.g., Rigaku HyPix, Bruker PIXIUM)']} |
| hybrid_photon_counting | Hybrid pixel photon counting detector for X-ray crystallography |  | {'comments': ['Modern X-ray detectors (e.g., Dectris EIGER/PILATUS, Bruker PHOTON)']} |
| scintillator_coupled | Scintillator-coupled indirect detection |  | {'comments': ['Indirect detection via scintillator conversion']} |
| imaging_plate | Imaging plate detector |  | {'comments': ['Storage phosphor technology, historically common in X-ray crystallography']} |
| film | Photographic film |  | {'comments': ['Legacy detector type for historical datasets']} |



## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Separates detector technology from manufacturer/model for better ontology mapping |
|  | | Use detector_manufacturer and detector_model fields for specific equipment details |
