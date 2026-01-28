"""
Simple Scattering loader.

Website: https://www.simplescattering.com/
Note: Simple Scattering does not have a documented REST API.
This loader parses HTML pages to extract dataset metadata.
"""

import re
from typing import Any

import requests
from bs4 import BeautifulSoup

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.pydantic import (
    BufferComposition,
    DataFile,
    Dataset,
    ExperimentInstrumentAssociation,
    ExperimentRun,
    ExperimentSampleAssociation,
    FileFormatEnum,
    QuantityValue,
    Sample,
    SampleTypeEnum,
    SAXSInstrument,
    Study,
    StudyExperimentAssociation,
    StudySampleAssociation,
    TechniqueEnum,
)


class SimpleScatteringLoader(BaseLoader):
    """
    Loader for Simple Scattering (SEC-SAXS data from SIBYLS beamline).

    Simple Scattering is a repository for SAXS/SANS data primarily from
    the SIBYLS beamline at the Advanced Light Source, Berkeley Lab.

    Note: This loader scrapes HTML pages since no JSON API is available.

    Example:
        >>> loader = SimpleScatteringLoader()
        >>> result = loader.load("xsbhevph")
        >>> result.dataset.id
        'simplescattering:xsbhevph'
    """

    source_name = "simplescattering"
    base_url = "https://www.simplescattering.com"

    def __init__(self, cache: ResponseCache | None = None):
        """
        Initialize the Simple Scattering loader.

        Args:
            cache: Optional response cache for development/testing
        """
        self.cache = cache or ResponseCache(enabled=False)

    def load(self, dataset_code: str) -> LoaderResult:
        """
        Load a Simple Scattering dataset by code.

        Args:
            dataset_code: Dataset code (e.g., "xsbhevph")

        Returns:
            LoaderResult with populated Dataset

        Raises:
            requests.HTTPError: If the page request fails
            ValueError: If the dataset is not found
        """
        html = self._fetch_dataset_page(dataset_code)
        warnings: list[str] = []

        # Parse the HTML
        soup = BeautifulSoup(html, "html.parser")

        # Build the dataset
        dataset_id = self.make_id(dataset_code)
        source_url = f"{self.base_url}/open_dataset/{dataset_code}"

        # Extract metadata from page
        metadata = self._extract_metadata(soup, warnings)

        # Create instrument (SIBYLS beamline)
        instrument = self._create_instrument(metadata, warnings)

        # Create sample
        sample = self._create_sample(metadata, dataset_code, warnings)

        # Create experiment run
        experiment = self._create_experiment_run(
            metadata, dataset_code, warnings)

        # Create data files
        data_files = self._create_data_files(soup, dataset_code, warnings)

        # Create lightweight study
        study = Study(
            id=f"{dataset_id}/study",
            title=metadata.get(
                "title", f"Simple Scattering Dataset {dataset_code}"),
        )

        # Create association tables
        study_sample_associations = [
            StudySampleAssociation(study_id=study.id, sample_id=sample.id)
        ]
        study_experiment_associations = [
            StudyExperimentAssociation(
                study_id=study.id, experiment_id=experiment.id)
        ]
        experiment_sample_associations = [
            ExperimentSampleAssociation(
                experiment_id=experiment.id, sample_id=sample.id
            )
        ]
        experiment_instrument_associations = [
            ExperimentInstrumentAssociation(
                experiment_id=experiment.id, instrument_id=instrument.id
            )
        ]

        # Create dataset
        dataset = Dataset(
            id=dataset_id,
            title=metadata.get(
                "title", f"Simple Scattering Dataset {dataset_code}"),
            studies=[study],
            instruments=[instrument],
            samples=[sample],
            experiment_runs=[experiment],
            data_files=data_files,
            study_sample_associations=study_sample_associations,
            study_experiment_associations=study_experiment_associations,
            experiment_sample_associations=experiment_sample_associations,
            experiment_instrument_associations=experiment_instrument_associations,
        )

        return LoaderResult(
            dataset=dataset,
            warnings=warnings,
            source_url=source_url,
            raw_data={"html": html, "metadata": metadata},
        )

    def list_entries(self, limit: int | None = None, **filters: Any) -> list[str]:
        """
        List available dataset codes from Simple Scattering.

        Args:
            limit: Maximum number of entries to return
            **filters: Not currently supported

        Returns:
            List of dataset codes
        """
        cache_key = "simplescattering/open_datasets"

        def fetch() -> dict[str, Any]:
            url = f"{self.base_url}/open_datasets"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return {"html": response.text}

        result = self.cache.get_or_fetch(cache_key, fetch)
        html = result["html"]

        # Parse HTML and extract dataset codes
        soup = BeautifulSoup(html, "html.parser")
        codes = []

        for link in soup.find_all("a", href=True):
            href = link["href"]
            match = re.match(r"/open_dataset/([a-z0-9]+)", href)
            if match:
                codes.append(match.group(1))

        # Remove duplicates while preserving order
        codes = list(dict.fromkeys(codes))

        if limit:
            codes = codes[:limit]

        return codes

    def _fetch_dataset_page(self, dataset_code: str) -> str:
        """Fetch dataset HTML page."""
        cache_key = f"simplescattering/{dataset_code}"

        def fetch() -> dict[str, Any]:
            url = f"{self.base_url}/open_dataset/{dataset_code}"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return {"html": response.text}

        result = self.cache.get_or_fetch(cache_key, fetch)
        return result["html"]

    def _extract_metadata(
        self, soup: BeautifulSoup, warnings: list[str]
    ) -> dict[str, Any]:
        """Extract metadata from the HTML page."""
        metadata: dict[str, Any] = {}

        # Title is in <h1> tag
        h1 = soup.find("h1")
        if h1:
            metadata["title"] = h1.get_text(strip=True)

        # Description is often in a paragraph after title
        container = soup.find("div", class_="container")
        if container:
            # Find the description paragraph
            for p in container.find_all("p"):
                text = p.get_text(strip=True)
                if len(text) > 100:  # Likely the main description
                    metadata["description"] = text
                    break

            # Extract text content for parsing
            text_content = container.get_text(separator="\n")
            metadata["raw_text"] = text_content

            # Try to extract key values from text
            self._extract_values_from_text(text_content, metadata, warnings)

        # Look for table rows with metadata
        for row in soup.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) >= 2:
                key = cells[0].get_text(strip=True).lower().replace(" ", "_")
                value = cells[1].get_text(strip=True)
                if key and value:
                    metadata[key] = value

        return metadata

    def _extract_values_from_text(
        self, text: str, metadata: dict[str, Any], warnings: list[str]
    ) -> None:
        """Extract specific values from text using regex."""
        # Wavelength
        wavelength_match = re.search(
            r"wavelength[:\s]+(\d+\.?\d*)\s*[ÅA]", text, re.IGNORECASE
        )
        if wavelength_match:
            metadata["wavelength_angstroms"] = float(wavelength_match.group(1))

        # Detector distance
        distance_match = re.search(
            r"(\d+(?:,\d+)?)\s*mm\s*(?:away|distance)", text, re.IGNORECASE
        )
        if distance_match:
            metadata["detector_distance_mm"] = float(
                distance_match.group(1).replace(",", "")
            )

        # q-range
        q_match = re.search(
            r"q\s*(?:range)?[:\s]+(\d+\.?\d*)\s*(?:to|-)\s*(\d+\.?\d*)\s*[ÅA]",
            text,
            re.IGNORECASE,
        )
        if q_match:
            metadata["q_min"] = float(q_match.group(1))
            metadata["q_max"] = float(q_match.group(2))

        # Concentration
        conc_match = re.search(
            r"(\d+\.?\d*)\s*mg/mL", text, re.IGNORECASE
        )
        if conc_match:
            metadata["concentration_mg_ml"] = float(conc_match.group(1))

        # pH
        ph_match = re.search(r"pH\s*(\d+\.?\d*)", text, re.IGNORECASE)
        if ph_match:
            metadata["ph"] = float(ph_match.group(1))

        # Buffer components
        buffer_match = re.search(
            r"(\d+\s*mM\s+\w+(?:,\s*\d+\s*mM\s+\w+)*)", text, re.IGNORECASE
        )
        if buffer_match:
            metadata["buffer_text"] = buffer_match.group(1)

        # Beamline
        if "SIBYLS" in text or "BL12.3.1" in text:
            metadata["beamline"] = "SIBYLS BL12.3.1"
            metadata["facility"] = "Advanced Light Source"

        # Sample type inference
        text_lower = text.lower()
        if "protein" in text_lower:
            metadata["sample_type"] = "protein"
        elif "rna" in text_lower:
            metadata["sample_type"] = "nucleic_acid"
        elif "dna" in text_lower:
            metadata["sample_type"] = "nucleic_acid"
        elif "lipid" in text_lower:
            metadata["sample_type"] = "complex"

        # Technique
        if "SEC-SAXS" in text or "sec-saxs" in text.lower():
            metadata["technique"] = "sec_saxs"
        elif "SANS" in text:
            metadata["technique"] = "sans"
        else:
            metadata["technique"] = "saxs"

    def _create_instrument(
        self, metadata: dict[str, Any], warnings: list[str]
    ) -> SAXSInstrument:
        """Create SAXSInstrument from metadata."""
        beamline = metadata.get("beamline", "SIBYLS BL12.3.1")

        return SAXSInstrument(
            id="simplescattering:instrument/sibyls-bl12.3.1",
            title="SIBYLS BL12.3.1",
            instrument_code="ALS-SIBYLS-BL12.3.1",
            description="SEC-SAXS beamline at Advanced Light Source, Berkeley Lab",
            manufacturer="Lawrence Berkeley National Laboratory",
        )

    def _create_sample(
        self, metadata: dict[str, Any], dataset_code: str, warnings: list[str]
    ) -> Sample:
        """Create Sample from metadata."""
        # Determine sample type
        sample_type_str = metadata.get("sample_type", "protein")
        sample_type_map = {
            "protein": SampleTypeEnum.protein,
            "nucleic_acid": SampleTypeEnum.nucleic_acid,
            "complex": SampleTypeEnum.complex,
        }
        sample_type = sample_type_map.get(
            sample_type_str, SampleTypeEnum.protein)

        # Create concentration QuantityValue
        concentration = None
        if metadata.get("concentration_mg_ml"):
            concentration = QuantityValue(
                numeric_value=metadata["concentration_mg_ml"],
                unit="mg/mL",
            )

        # Create buffer composition
        buffer_composition = None
        if metadata.get("ph") or metadata.get("buffer_text"):
            ph_value = None
            if metadata.get("ph"):
                ph_value = QuantityValue(
                    numeric_value=metadata["ph"],
                    unit="pH",
                )
            buffer_composition = BufferComposition(
                ph=ph_value,
                components=[metadata.get("buffer_text")]
                if metadata.get("buffer_text")
                else None,
            )

        return Sample(
            id=f"simplescattering:{dataset_code}/sample",
            sample_code=f"SS-{dataset_code.upper()}",
            sample_type=sample_type,
            title=metadata.get("title"),
            description=metadata.get("description"),
            concentration=concentration,
            buffer_composition=buffer_composition,
        )

    def _create_experiment_run(
        self, metadata: dict[str, Any], dataset_code: str, warnings: list[str]
    ) -> ExperimentRun:
        """Create ExperimentRun from metadata."""
        # Determine technique
        technique_str = metadata.get("technique", "saxs")
        technique_map = {
            "saxs": TechniqueEnum.saxs,
            "sec_saxs": TechniqueEnum.saxs,  # SEC-SAXS is a variant of SAXS
            "sans": TechniqueEnum.sans,
        }
        technique = technique_map.get(technique_str, TechniqueEnum.saxs)

        # Create wavelength QuantityValue
        wavelength = None
        if metadata.get("wavelength_angstroms"):
            wavelength = QuantityValue(
                numeric_value=metadata["wavelength_angstroms"],
                unit="Angstroms",
            )

        # Create detector distance QuantityValue
        detector_distance = None
        if metadata.get("detector_distance_mm"):
            detector_distance = QuantityValue(
                numeric_value=metadata["detector_distance_mm"],
                unit="mm",
            )

        return ExperimentRun(
            id=f"simplescattering:{dataset_code}/experiment",
            experiment_code=f"SS-{dataset_code.upper()}-EXP",
            technique=technique,
            wavelength=wavelength,
            detector_distance=detector_distance,
            beamline=metadata.get("beamline"),
        )

    def _create_data_files(
        self, soup: BeautifulSoup, dataset_code: str, warnings: list[str]
    ) -> list[DataFile]:
        """Create DataFile entries from download links."""
        files = []
        seen_urls = set()

        # Find download links (Rails Active Storage blobs)
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if "/rails/active_storage/" in href or href.endswith(
                (".dat", ".zip", ".pdb", ".cif")
            ):
                # Skip duplicates
                if href in seen_urls:
                    continue
                seen_urls.add(href)

                # Extract filename from URL path (after last /)
                # For Rails Active Storage, filename is at the end before query params
                url_path = href.split("?")[0]
                filename = url_path.split("/")[-1]

                # Determine file format
                file_format = FileFormatEnum.ascii
                if filename.endswith(".pdb"):
                    file_format = FileFormatEnum.pdb
                elif filename.endswith(".zip"):
                    file_format = FileFormatEnum.zip
                elif filename.endswith(".cif"):
                    file_format = FileFormatEnum.mmcif

                # Build full URL
                full_url = href
                if href.startswith("/"):
                    full_url = f"{self.base_url}{href}"

                # Create unique ID from filename
                file_id = (
                    filename.replace(".", "_").replace(" ", "_").lower()[:50]
                )
                files.append(
                    DataFile(
                        id=f"simplescattering:{dataset_code}/file/{file_id}",
                        file_name=filename,
                        file_format=file_format,
                        file_path=full_url,
                        description=f"Data file from Simple Scattering dataset {dataset_code}",
                    )
                )

        return files
