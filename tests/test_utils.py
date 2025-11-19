"""Tests for utils module."""

from itersys.utils import deep_get, deep_set


def test_deep_get_string_path():
    """Test deep_get with string path."""
    d = {"a": {"b": {"c": 42}}}
    assert deep_get(d, "a.b.c") == 42
    assert deep_get(d, "a.b") == {"c": 42}
    assert deep_get(d, "a") == {"b": {"c": 42}}


def test_deep_get_list_path():
    """Test deep_get with list path."""
    d = {"a": {"b": {"c": 42}}}
    assert deep_get(d, ["a", "b", "c"]) == 42
    assert deep_get(d, ["a", "b"]) == {"c": 42}


def test_deep_get_default():
    """Test deep_get with default value."""
    d = {"a": {"b": {"c": 42}}}
    assert deep_get(d, "a.b.d", default=0) == 0
    assert deep_get(d, "x.y.z", default="not found") == "not found"
    assert deep_get(d, "a.b.c.d", default=None) is None


def test_deep_set_string_path():
    """Test deep_set with string path."""
    d = {}
    deep_set(d, "a.b.c", 42)
    assert d == {"a": {"b": {"c": 42}}}
    
    deep_set(d, "a.b.d", 10)
    assert d == {"a": {"b": {"c": 42, "d": 10}}}


def test_deep_set_list_path():
    """Test deep_set with list path."""
    d = {}
    deep_set(d, ["x", "y"], 10)
    assert d == {"x": {"y": 10}}


def test_deep_set_overwrite():
    """Test deep_set overwrites existing values."""
    d = {"a": {"b": {"c": 42}}}
    deep_set(d, "a.b.c", 100)
    assert d == {"a": {"b": {"c": 100}}}


def test_deep_set_nested():
    """Test deep_set creates nested structures."""
    d = {}
    deep_set(d, "level1.level2.level3", "value")
    assert d == {"level1": {"level2": {"level3": "value"}}}

