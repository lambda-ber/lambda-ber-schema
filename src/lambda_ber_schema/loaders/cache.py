"""
Simple file-based cache for API responses.

Useful for development and testing to avoid hitting APIs repeatedly.
"""

import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable


class ResponseCache:
    """
    File-based cache for API responses.

    Stores JSON responses in a directory structure, with configurable TTL.
    Useful during development to avoid hitting rate limits and speed up iteration.

    Attributes:
        cache_dir: Directory to store cached responses
        ttl: Time-to-live for cached entries
        enabled: Whether caching is active

    Example:
        >>> cache = ResponseCache(cache_dir=Path(".cache"), ttl=timedelta(hours=24))
        >>> data = cache.get_or_fetch("sasbdb/SASDA52", lambda: fetch_from_api())
    """

    def __init__(
        self,
        cache_dir: Path | None = None,
        ttl: timedelta = timedelta(hours=24),
        enabled: bool = True,
    ):
        """
        Initialize the cache.

        Args:
            cache_dir: Directory for cache files. Defaults to .cache in current dir.
            ttl: How long entries remain valid
            enabled: Set False to disable caching entirely
        """
        self.cache_dir = cache_dir or Path(".cache")
        self.ttl = ttl
        self.enabled = enabled

        if self.enabled:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _key_to_path(self, key: str) -> Path:
        """Convert a cache key to a file path."""
        # Hash the key to handle special characters and long keys
        key_hash = hashlib.sha256(key.encode()).hexdigest()[:16]
        safe_key = "".join(c if c.isalnum() or c in "-_" else "_" for c in key)
        return self.cache_dir / f"{safe_key[:50]}_{key_hash}.json"

    def _is_valid(self, cache_file: Path) -> bool:
        """Check if a cache file exists and is within TTL."""
        if not cache_file.exists():
            return False
        mtime = datetime.fromtimestamp(cache_file.stat().st_mtime)
        return datetime.now() - mtime < self.ttl

    def get(self, key: str) -> dict[str, Any] | None:
        """
        Get cached response if valid.

        Args:
            key: Cache key (e.g., "sasbdb/SASDA52")

        Returns:
            Cached data dict, or None if not cached or expired
        """
        if not self.enabled:
            return None

        cache_file = self._key_to_path(key)
        if not self._is_valid(cache_file):
            return None

        return json.loads(cache_file.read_text())

    def set(self, key: str, data: dict[str, Any]) -> None:
        """
        Cache a response.

        Args:
            key: Cache key
            data: Data to cache (must be JSON-serializable)
        """
        if not self.enabled:
            return

        cache_file = self._key_to_path(key)
        cache_file.write_text(json.dumps(data, indent=2))

    def get_or_fetch(
        self, key: str, fetch_func: Callable[[], dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Get from cache or fetch and cache.

        Args:
            key: Cache key
            fetch_func: Function to call if cache miss

        Returns:
            Cached or freshly fetched data
        """
        cached = self.get(key)
        if cached is not None:
            return cached

        data = fetch_func()
        self.set(key, data)
        return data

    def clear(self) -> None:
        """Clear all cached responses."""
        if self.cache_dir.exists():
            for cache_file in self.cache_dir.glob("*.json"):
                cache_file.unlink()
