"""Python uv package template with CI, releases and docs."""


def greet(name: str) -> str:
    """Build the greeting for `name`."""
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
