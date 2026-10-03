import pytest

from template_python_uv import greet


def test_greets_by_name():
    assert greet(" Allie ") == "Hello, Allie!"


def test_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("  ")
