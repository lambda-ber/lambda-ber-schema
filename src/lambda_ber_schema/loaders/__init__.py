"""
ETL loaders for importing data from external structural biology repositories.

Available loaders:
- SASBDBLoader: Small Angle Scattering Biological Data Bank
- SimpleScatteringLoader: Simple Scattering (SEC-SAXS from SIBYLS)

Example:
    >>> from lambda_ber_schema.loaders import SASBDBLoader
    >>> loader = SASBDBLoader()
    >>> result = loader.load("SASDA52")
    >>> result.dataset.id
    'sasbdb:SASDA52'
"""

from lambda_ber_schema.loaders.base import BaseLoader, LoaderResult
from lambda_ber_schema.loaders.cache import ResponseCache
from lambda_ber_schema.loaders.pdb import PDBLoader
from lambda_ber_schema.loaders.sasbdb import SASBDBLoader
from lambda_ber_schema.loaders.simplescattering import SimpleScatteringLoader

__all__ = [
    "BaseLoader",
    "LoaderResult",
    "ResponseCache",
    "PDBLoader",
    "SASBDBLoader",
    "SimpleScatteringLoader",
]
