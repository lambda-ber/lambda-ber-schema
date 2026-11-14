"""Tests for the file-based response cache."""

from lambda_ber_schema.loaders.cache import ResponseCache


def test_round_trip_leaves_no_temporary_file(tmp_path):
    cache = ResponseCache(cache_dir=tmp_path, enabled=True)
    cache.set("pdb/1HHO", {"rcsb_id": "1HHO"})
    assert cache.get("pdb/1HHO") == {"rcsb_id": "1HHO"}
    assert [p.suffix for p in tmp_path.iterdir()] == [".json"]


def test_a_file_cut_short_is_fetched_again(tmp_path):
    """A dump stopped mid-write must not fail that entry on every later run."""
    cache = ResponseCache(cache_dir=tmp_path, enabled=True)
    cache.set("pdb/1HHO", {"rcsb_id": "1HHO"})
    [cache_file] = tmp_path.glob("*.json")
    cache_file.write_text('{"rcsb_id": "1H')

    calls = []

    def fetch():
        calls.append(1)
        return {"rcsb_id": "1HHO"}

    assert cache.get("pdb/1HHO") is None
    assert cache.get_or_fetch("pdb/1HHO", fetch) == {"rcsb_id": "1HHO"}
    assert calls == [1]
    # and the good copy replaced the damaged one
    assert cache.get("pdb/1HHO") == {"rcsb_id": "1HHO"}


def test_clear_removes_leftover_temporary_files(tmp_path):
    cache = ResponseCache(cache_dir=tmp_path, enabled=True)
    cache.set("pdb/1HHO", {"rcsb_id": "1HHO"})
    (tmp_path / "pdb_1HHO_abc.json.123.456.tmp").write_text("{")
    cache.clear()
    assert list(tmp_path.iterdir()) == []


def test_disabled_cache_writes_nothing(tmp_path):
    cache = ResponseCache(cache_dir=tmp_path / "off", enabled=False)
    cache.set("pdb/1HHO", {"rcsb_id": "1HHO"})
    assert cache.get("pdb/1HHO") is None
    assert not (tmp_path / "off").exists()
