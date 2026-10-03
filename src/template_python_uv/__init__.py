"""Python package template: uv, pytest, ruff, PyPI trusted publishing, mise, lefthook, CI and a VitePress docs site."""


def greet(name: str) -> str:
    """Build the greeting for `name`."""
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
