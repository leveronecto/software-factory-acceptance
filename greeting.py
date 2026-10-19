"""Small, dependency-free fixture for Software Factory live acceptance."""


def greeting(name):
    trimmed = name.strip()
    if not trimmed:
        raise ValueError("name must not be empty")
    return f"Hello, {trimmed}!"
