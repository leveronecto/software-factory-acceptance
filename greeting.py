"""Small, dependency-free fixture for Software Factory live acceptance."""

def greeting(name):
    name = name.strip()
    if not name:
        raise ValueError("Name must not be empty")
    return f"Hello, {name}!"
