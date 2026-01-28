"""
Base classes for ETL loaders.

This module defines the abstract interface that all data source loaders must implement.
"""

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel
from pydantic import Field

from lambda_ber_schema.pydantic import Dataset


class LoaderResult(BaseModel):
    """
    Result container for loader operations.

    Attributes:
        dataset: The populated Dataset object
        warnings: List of non-fatal issues encountered during loading
        source_url: URL of the source data (for provenance)
        raw_data: Original API response (optional, for debugging)

    Example:
        >>> result = LoaderResult(
        ...     dataset=Dataset(id="test:123"),
        ...     warnings=["Missing molecular weight"],
        ...     source_url="https://example.org/entry/123"
        ... )
        >>> len(result.warnings)
        1
    """

    dataset: Dataset
    warnings: list[str] = Field(default_factory=list)
    source_url: str | None = None
    raw_data: dict[str, Any] | None = None


class BaseLoader(ABC):
    """
    Abstract base class for ETL loaders.

    Defines the interface for loading data from external sources
    and transforming it into lambda-ber-schema Dataset objects.

    Subclasses must implement:
        - load(): Load a single entry by identifier
        - list_entries(): List available entry identifiers

    Attributes:
        source_name: Human-readable name of the data source
        base_url: Base URL for the data source API

    Example:
        >>> class MyLoader(BaseLoader):
        ...     source_name = "MySource"
        ...     base_url = "https://example.org/api"
        ...
        ...     def load(self, identifier: str) -> LoaderResult:
        ...         # Implementation here
        ...         pass
        ...
        ...     def list_entries(self, **filters) -> list[str]:
        ...         return []
    """

    source_name: str
    base_url: str

    @abstractmethod
    def load(self, identifier: str) -> LoaderResult:
        """
        Load a single entry by identifier.

        Args:
            identifier: Source-specific identifier (e.g., "SASDA52" for SASBDB)

        Returns:
            LoaderResult containing the populated Dataset and any warnings

        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If the identifier is invalid or not found
        """
        ...

    @abstractmethod
    def list_entries(self, **filters: Any) -> list[str]:
        """
        List available entry identifiers from the source.

        Args:
            **filters: Source-specific filters (e.g., molecular_type="protein")

        Returns:
            List of entry identifiers that can be passed to load()
        """
        ...

    def load_batch(self, identifiers: list[str]) -> list[LoaderResult]:
        """
        Load multiple entries.

        Default implementation calls load() sequentially.
        Subclasses may override for batch API efficiency.

        Args:
            identifiers: List of entry identifiers to load

        Returns:
            List of LoaderResults, one per identifier
        """
        return [self.load(id_) for id_ in identifiers]

    def make_id(self, identifier: str) -> str:
        """
        Create a prefixed ID for provenance tracking.

        Args:
            identifier: The source-specific identifier

        Returns:
            Prefixed identifier (e.g., "sasbdb:SASDA52")

        Example:
            >>> loader = SASBDBLoader()
            >>> loader.make_id("SASDA52")
            'sasbdb:SASDA52'
        """
        prefix = self.source_name.lower().replace(" ", "")
        return f"{prefix}:{identifier}"
