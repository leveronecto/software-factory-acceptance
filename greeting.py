"""Small, dependency-free fixture for Software Factory live acceptance."""


def greeting(name):
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}!"
